# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return self.username

    class Meta(object):
        ordering = ('id',)


class FollowUp(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower_set'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_set'
    )
