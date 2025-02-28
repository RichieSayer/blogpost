from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from .models import Post

class LatestPostFeed(Feed):
    title = 'My Super Blog'
    link = '/feed/'  # The base URL for the feed
    description = 'New Post'

    def items(self):
        return Post.objects.filter(status='published')[:5]  # Use published posts only
    
    def item_title(self, item):
        return item.title  # Title of the post
    
    def item_description(self, item):
        return truncatewords(item.body, 30)  # Truncate post content to 30 words
    
    def item_link(self, item):
        # Ensure you're using the slug for the URL
        return reverse('PostApp:detail_view', args=[item.slug])
