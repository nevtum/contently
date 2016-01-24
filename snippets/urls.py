from django.conf.urls import url
from .views import (
    SnippetListView,
    SnippetCreateView,
    SnippetDetailView)

urlpatterns = [
    url(r'^$', SnippetListView.as_view(), name='snippets'),
    url(r'^submitsnippet/$', SnippetCreateView.as_view(), name='new-snippet'),
    url(r'^(?P<slug>[-\w]+)/$', SnippetDetailView.as_view(), name='snippet-detail'),
]
