# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Post
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","slug","author","preview_content","updated","timestamp"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title","content"]
    class Meta:
        model = Post

    def save_model(self, request, instance, form, change):
        user = request.user 
        instance = form.save(commit=False)
        if not change or not instance.author:
            instance.author = user
        instance.save()
        form.save_m2m()
        return instance


admin.site.register(Post, PostModelAdmin)
