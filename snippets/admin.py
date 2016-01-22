from django.contrib import admin
from .models import Snippet, Vote

# Register your models here.
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('submitted_date', 'title', 'submitter')
    search_fields = ['body']

class VoteAdmin(admin.ModelAdmin):
    list_display = ('snippet', 'voted_by')

admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Vote, VoteAdmin)