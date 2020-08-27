from django.urls import path
from . import  views
from .views import (PostDetailView,
                    PostListView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView)


urlpatterns = [
    path('',views.home,name='landing'),
    path('user/profile/<username>/', views.get_user_profile,name='user-profile'),
    path('blog/' , PostListView.as_view() , name = 'blog-home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]