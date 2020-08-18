from django.shortcuts import render
from .models import Post
from django.views.generic import (ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)


# Create your views here.
"""def home(request):

    posts = Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})
"""


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3
