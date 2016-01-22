from django.shortcuts import render
from django.views.generic import ListView
from .models import Snippet

# Create your views here.
class SnippetListView(ListView):
    context_object_name = 'snippets'
    template_name = 'snippet_list.html'
    model = Snippet
    paginate_by = 5