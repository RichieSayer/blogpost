from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CommentForm, PostForm, EmailForm
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Count
from django.contrib.auth.decorators import login_required

@login_required  # Ensures only logged-in users can create posts
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user  # Assign current user as author
            new_post.save()

            form.save_m2m()  # Save many-to-many fields
            
            return redirect('PostApp:homepage')  # Redirect to homepage or another page
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})

# Pagination helper function
def paginate_posts(request, posts_queryset, posts_per_page=10):
    paginator = Paginator(posts_queryset, posts_per_page)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return posts

# Homepage view
def homepage_view(request):
    recent_posts = Post.new_manager.all()[:5]  # Displaying recent posts as featured content
    all_posts = Post.new_manager.all()  # Get all posts for the post list
    posts = paginate_posts(request, all_posts)  # Apply pagination to all posts

    return render(request, 'homepage.html', {
        'recent_posts': recent_posts,
        'posts': posts,  # Pass paginated posts to the template
    })

# Post detail view
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    email_form = EmailForm()
    comment_form = CommentForm()
    comments = Comment.objects.filter(post=post, active=True)
    post_tags = post.tags.all()

    # Handle similar posts
    similar_post = (
        Post.objects.filter(status='published')
        .exclude(pk=post.pk)
        .annotate(tag_count=Count('tags'))
    )
    if post_tags.exists():
        similar_post = similar_post.filter(tags__in=post_tags)
    similar_post = similar_post.order_by('-tag_count', '-created')[:3]

    if request.method == 'POST':
        if 'name' in request.POST and 'email' in request.POST and 'body' in request.POST:
            # Handle comment submission
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.save()
                return redirect(post.get_absolute_url())  # Refresh the page after comment

        elif 'to' in request.POST:  
            # Handle email sharing form
            email_form = EmailForm(request.POST)
            if email_form.is_valid():
                cd = email_form.cleaned_data
                name = cd['name']
                to = cd['to']
                message = cd['comments']
                subject = f"Shared post by {name}"
                senders_email = settings.EMAIL_HOST_USER
                send_mail(subject, message, senders_email, [to])
                return redirect(post.get_absolute_url())  

    return render(request, 'detail.html', {
        'post': post,
        'comments': comments,
        'email_form': email_form,
        'comment_form': comment_form,
        'similar_posts': similar_post,
    })

# Delete post view (anyone can delete posts)
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('PostApp:homepage')
