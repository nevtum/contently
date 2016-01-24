from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.db.models import Q
from django.core.urlresolvers import reverse
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
    
    def get_success_url(self):
        return reverse('snippet-detail', kwargs={'slug': self.object.id})

class SnippetDetailView(DetailView):
    model = Snippet
    context_object_name = 'snippet'
    slug_field = 'id'
    template_name = 'snippet_detail.html'