# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return self.username

    class Meta(object):
        ordering = ('id',)


class FollowUp(models.Model):
    subscriber = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='subscriber_set'
    )
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower_set'
    )
