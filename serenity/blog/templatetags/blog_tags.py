from ..models import Post
from django import template

# instatiating the template.Library class
register= template.Library()


# registering the get_recent_posts function to be used as tags
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-date_posted')[:num]


