from django.shortcuts import render, get_object_or_404
from .models import Post,User
from django.views.generic import (ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)

from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
# Create your views here.

# Home view
def home(request):
    return render(request,'blog/landing.html')



# View for getting a users profile
def get_user_profile(request,username):
    user = User.objects.get(username=username)
    return render(request,'users/profile.html',{'user':user })


# class-based view for displaying post in full
class PostDetailView(DetailView):
    model = Post


# class-based view for displaying summary of various posts,
# odering by latest and page pagination
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return  Post.objects.filter(author=user).order_by('-date_posted')


class UserPostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False