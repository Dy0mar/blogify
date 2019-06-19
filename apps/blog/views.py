# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from blog.models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'posts/post_list.html'

    def get_next_link(self):
        raise NotImplemented

    def get_queryset(self):
        # TODO: ajax need use for pagination.
        return self.model.objects.order_by(
            '-created_at').prefetch_related('author')


class AuthorPostListView(PostListView):

    def get_queryset(self):
        # TODO: ajax need use for pagination.
        return self.model.objects.filter(
            author=self.request.user
        ).order_by('-created_at').prefetch_related('author')

    def get_next_link(self):
        return reverse('author-blog-list')

    def get_context_data(self, **kwargs):
        context = super(AuthorPostListView, self).get_context_data(**kwargs)
        context['current_page'] = 'author_blog_list'
        context['next_link'] = self.get_next_link()
        context['title'] = 'My blog'

        return context


author_blog_list = AuthorPostListView.as_view()


class AllPostListView(PostListView):
    def get_next_link(self):
        return reverse('all-blog-list')

    def get_context_data(self, **kwargs):
        context = super(AllPostListView, self).get_context_data(**kwargs)
        context['current_page'] = 'all_blog_list'
        context['next_link'] = self.get_next_link()
        context['title'] = 'User Blogs'
        return context


all_blog_list = AllPostListView.as_view()


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


post_detail = PostDetail.as_view()


class PostBaseView(LoginRequiredMixin):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('author-blog-list')


class PostCreate(PostBaseView, CreateView):
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


create_post = PostCreate.as_view()


class PostUpdate(PostBaseView, UpdateView):
    def get_object(self, queryset=None):
        obj = super(PostUpdate, self).get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj


update_post = PostUpdate.as_view()


class PostDelete(PostBaseView, DeleteView):
    def get_object(self, queryset=None):
        obj = super(PostDelete, self).get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj


delete_post = PostDelete.as_view()
