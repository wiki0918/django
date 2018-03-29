"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from mainapp.views import get_index,get_user,update_user,get_signup,post_signup,post_login,post_logout,set_cookie,get_cookie,set_session,get_session


urlpatterns = [
    url(r'^set_cookie', set_cookie),
    url(r'^get_cookie', get_cookie),
    url(r'^set_session', set_session),
    url(r'^get_session', get_session),
    url(r'^signup$', get_signup),
    url(r'^signup/post', post_signup),
    url(r'^login/post', post_login),
    url(r'^logout/post', post_logout),
    url(r'^admin/', admin.site.urls) ,
    url(r'^user$', get_user),
    url(r'^user/update', update_user),
    url(r'^', get_index),
]
