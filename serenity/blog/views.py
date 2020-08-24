from django.shortcuts import render
from .models import Post,User
from django.views.generic import (ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)


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


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)
