# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
import string
import random

# Create your models here.
def random_generator(size=9, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "%s/%s" %(instance.id, filename)
class Post(models.Model):
    author = models.ForeignKey(User,editable=False)
    title = models.CharField(max_length=120)
    slug = models.SlugField(editable=False)
    image = ResizedImageField( upload_to=upload_location, null=True, blank=True)
    content = RichTextField()
    preview_content = models.TextField(max_length=130, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug":self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = "%s-%s" %(slugify(self.title),random_generator())
        super(Post, self).save(*args, **kwargs)


            
