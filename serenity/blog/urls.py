from django.urls import path
from . import  views
from .views import (PostDetailView,
                    PostListView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
                    UserPostDetailView)


urlpatterns = [
    path('',views.home,name='landing'),

    path('user/profile/<username>/', views.get_user_profile,name='user-profile'),
    path('blog/' , PostListView.as_view() , name = 'blog-home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('user/<str:username>/<int:pk>/', UserPostDetailView.as_view(), name='user-post-detail'),
    path('paasword-reser', auth_views.PasswordResetView.as_view(template='users/password_reset.html'), name='password_reset')
]