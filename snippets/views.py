from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Snippet

# Create your views here.
class SnippetListView(ListView):
    model = Snippet
    ordering = ('-submitted_date')
    context_object_name = 'snippets'
    template_name = 'snippet_list.html'
    paginate_by = 5        

class SnippetDetailView(DetailView):
    model = Snippet
    context_object_name = 'snippet'    
    slug_field = 'id'
    template_name = 'snippet_detail.html'