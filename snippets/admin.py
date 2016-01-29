from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Snippet, Vote, UserProfile

# Register your models here.
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('submitted_date', 'title', 'submitter')
    search_fields = ['body']

class VoteAdmin(admin.ModelAdmin):
    list_display = ('snippet', 'voted_by')

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserProfileAdmin)
admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Vote, VoteAdmin)

def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

from django.db.models.signals import post_save
post_save.connect(create_profile, sender=User)