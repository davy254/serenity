from django.shortcuts import render
from .models import Post,User
from django.views.generic import (ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)


# Create your views here.
def home(request):
    return render(request,'blog/landing.html')

def get_user_profile(request,username):
    user = User.objects.get(username=username)
    return render(request,'users/profile.html',{'user':user })


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6
