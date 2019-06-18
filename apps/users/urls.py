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
from django.conf.urls import url

from users.views import my_follow_up_list, subscribe_to, feeds

urlpatterns = [
    url(r'^subscribe-to/(?P<pk>\d+)/$', subscribe_to, name='subscribe-to'),
    url(r'^feeds/$', feeds, name='feeds'),
    url(r'^$', my_follow_up_list, name='my-follow-up-list'),
]
