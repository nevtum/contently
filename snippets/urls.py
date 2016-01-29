from django.conf.urls import url
from django.contrib.auth.decorators import login_required as auth
from .views import (
    SnippetListView,
    SnippetCreateView,
    SnippetDetailView,
    SnippetUpdateView)

urlpatterns = [
    url(r'^$', SnippetListView.as_view(), name='snippets'),
    url(r'^submitsnippet/$', auth(SnippetCreateView.as_view()), name='new-snippet'),
    url(r'^(?P<slug>[-\w]+)/$', SnippetDetailView.as_view(), name='snippet-detail'),
    url(r'^(?P<slug>[-\w]+)/update$', auth(SnippetUpdateView.as_view()), name='update-snippet'),
]
