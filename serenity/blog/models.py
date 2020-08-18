from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import  Image


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_image = models.ImageField(default='default.png', upload_to='blog_pics')


    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.blog_image.path)

        output_size = (350, 262.5)
        img.thumbnail(output_size)
        img.save(self.blog_image.path)
