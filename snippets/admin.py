from django.contrib import admin
from .models import Snippet, Vote, UserProfile

# Register your models here.
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('submitted_date', 'title', 'submitter')
    search_fields = ['body']

class VoteAdmin(admin.ModelAdmin):
    list_display = ('snippet', 'voted_by')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'last_active')
    search_fields = ['bio']

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Vote, VoteAdmin)