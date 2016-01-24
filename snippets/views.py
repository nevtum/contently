from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Snippet

# Create your views here.
class SnippetListView(ListView):
    model = Snippet
    context_object_name = 'snippets'
    template_name = 'snippet_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        if not self.request.GET.get('search'):
            snippets = Snippet.objects.all()
        else:
            search = self.request.GET['search']
            snippets = Snippet.objects.filter(
                Q(body__icontains=search) | Q(tags__name__in=[search])| Q(title__icontains=search))
        
        return snippets.order_by('-submitted_date')
        
class SnippetDetailView(DetailView):
    model = Snippet
    context_object_name = 'snippet'
    slug_field = 'id'
    template_name = 'snippet_detail.html'