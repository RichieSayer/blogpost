from django import forms
from .models import Comment, Post

class EmailForm(forms.Form):
    name = forms.CharField(max_length=50)
    to = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)  # Renamed from 'comments' to 'comment'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'status', 'tags']  # Add fields you want to be editable
        widgets = {
            'body': forms.Textarea(attrs={'rows': 6, 'resize': 'none'}),
        }