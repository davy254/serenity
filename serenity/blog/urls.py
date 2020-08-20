from django.urls import path
from . import  views
from .views import PostDetailView, PostListView


urlpatterns = [
    path('',views.home,name='landing'),
    path('blog/' , PostListView.as_view() , name = 'blog-home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]