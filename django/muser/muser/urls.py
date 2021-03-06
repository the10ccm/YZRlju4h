"""muser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from core.views import UserList, UserCreate, UserDelete, UserUpdate


urlpatterns = [
    url(r'^$', UserList.as_view(), name='user_list'),
    url(r'user/create/$', UserCreate.as_view(), name='user_create'),
    url(r'user/(?P<pk>[0-9]+)?/$', UserUpdate.as_view(), name='user_update'),
    url(r'user/(?P<pk>[0-9]+)/delete/$', UserDelete.as_view(), name='user_delete'),
    url(r'^admin/', admin.site.urls),
]
