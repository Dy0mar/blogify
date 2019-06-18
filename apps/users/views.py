# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView

from blog.models import Post
from users.models import FollowUp, User


class FeedsListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'posts/post_list.html'

    def get_queryset(self):
        return self.model.objects.filter(
            author__author_set__follower=self.request.user
        ).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(FeedsListView, self).get_context_data(**kwargs)
        context['current_page'] = 'feeds'
        return context


feeds = FeedsListView.as_view()


class MyFollowUpList(LoginRequiredMixin, ListView):
    model = FollowUp
    paginate_by = 10
    context_object_name = 'subscribe_list'
    template_name = 'users/subscribe_list.html'

    def get_queryset(self):
        return self.model.objects.filter(
            follower=self.request.user
        )


my_follow_up_list = MyFollowUpList.as_view()


def subscribe_to(request, pk):
    author = get_object_or_404(User, pk=pk)
    FollowUp.objects.get_or_create(
        follower=request.user,
        author=author
    )
    return redirect('my-follow-up-list')
