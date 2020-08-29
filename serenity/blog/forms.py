from django.forms  import ModelForm
from .models import Post


# create the form class

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields  = [ 'title', 'content', 'blog_image' ]