# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.conf import settings
from users.models import User, FollowUp
from .tasks import mailing


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


@receiver(post_save, sender=Post)
def my_handler(sender, **kwargs):
    created = kwargs.get('created')
    if created:
        post = kwargs.get('instance')
        subject = '{} added new post!'.format(post.author)

        # TODO: Here need use fromstring from html template.
        message = '{} added new post!'.format(post.author)

        emails = [obj.author.email for obj in post.author.follower_set.all()]
        if emails:
            mailing.apply_async(
                (subject, message, settings.DEFAULT_FROM_EMAIL, emails)
            )


class Feeds(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField()
