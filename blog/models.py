from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import string
import random

# Create your models here.
def random_generator(size=2, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "%s/%s" %(instance.id, filename)
class Post(models.Model):
    author = models.ForeignKey(User,editable=False)
    title = models.CharField(max_length=120)
    slug = models.SlugField(editable=False)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field", height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    content = RichTextField()
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


            
