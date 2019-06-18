"""blogify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from .views import (
    author_blog_list, all_blog_list, post_detail, create_post, update_post,
    delete_post,
)

urlpatterns = [
    url(r'^blogs/$', all_blog_list, name='all-blog-list'),
    url(r'^post/create/$', create_post, name='create-post'),
    url(r'^post/update/(?P<pk>\d+)/$', update_post, name='update-post'),
    url(r'^post/delete/(?P<pk>\d+)/$', delete_post, name='delete-post'),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post-detail'),
    url(r'^$', author_blog_list, name='author-blog-list'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
