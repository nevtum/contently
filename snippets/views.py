from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
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
            snippets = Snippet.with_votes.all()
        else:
            search = self.request.GET['search']
            snippets = Snippet.with_votes.filter(
                Q(body__icontains=search) | Q(tags__name__in=[search])| Q(title__icontains=search))
        
        return snippets.order_by('-submitted_date')

class SnippetCreateView(CreateView):
    model = Snippet
    fields = ['title', 'body', 'tags']
    template_name = 'submit_snippet.html'
    
    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super(SnippetCreateView, self).form_valid(form)

class SnippetUpdateView(UpdateView):
    model = Snippet
    slug_field = 'id'
    fields = ['title', 'body', 'tags']
    template_name = 'update_snippet.html'
    
    def get_object(self, queryset=None):
        snippet = super(SnippetUpdateView, self).get_object(queryset)
        if snippet.submitter != self.request.user:
            raise Exception("Cannot edit someone else's snippet!")
        return snippet

class SnippetDetailView(DetailView):
    model = Snippet
    context_object_name = 'snippet'
    slug_field = 'id'
    template_name = 'snippet_detail.html'