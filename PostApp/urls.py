from django.urls import path
from . import views
from .feeds import LatestPostFeed

app_name = 'PostApp'

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('detail/<slug:slug>/', views.post_detail, name='detail_view'),
    path('feed/', LatestPostFeed(), name='latest_feed'),
    path('create/', views.create_post, name='create_post'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),  # Delete post route
]
