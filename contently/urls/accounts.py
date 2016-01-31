from django.conf.urls import url
from django.contrib.auth.decorators import login_required as auth
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done)

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout', kwargs={ 'next_page': 'snippets' }),
    url(r'^reset/$', password_reset, name='password_reset'),
    url(r'^reset_done/$', password_reset_done, name='password_reset_done'),
]
