# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView

from blog.models import Post


class BlogListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'posts/post_list.html'

    def get_next_link(self):
        raise NotImplemented

    def get_queryset(self):
        return self.model.objects.order_by('-created_at')


class AuthorBlogListView(BlogListView):

    def get_queryset(self):
        return self.model.objects.filter(
            author=self.request.user
        ).order_by('-created_at')

    def get_next_link(self):
        return reverse('author-blog-list')

    def get_context_data(self, **kwargs):
        context = super(AuthorBlogListView, self).get_context_data(**kwargs)
        context['current_page'] = 'author_blog_list'
        context['next_link'] = self.get_next_link()

        return context


author_blog_list = AuthorBlogListView.as_view()


class AllBlogListView(BlogListView):
    def get_next_link(self):
        return reverse('all-blog-list')

    def get_context_data(self, **kwargs):
        context = super(AllBlogListView, self).get_context_data(**kwargs)
        context['current_page'] = 'all_blog_list'
        context['next_link'] = self.get_next_link()
        return context


all_blog_list = AllBlogListView.as_view()
