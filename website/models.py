from django.db import models
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    sub_title = models.CharField(max_length=200, null=False, default='')
    content = models.TextField(null=False, default='')
    slug = models.SlugField(unique=True, default='')

    def save(self,  *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
