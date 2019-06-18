# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_set'
    )

    def __str__(self):
        return '<Post: {}... User: {}>'.format(self.title[:10], self.author)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-id']


class Feeds(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField()
