from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager

class SnippetVoteCountManager(models.Manager):
    def get_queryset(self):
        return super(SnippetVoteCountManager, self).get_queryset().annotate(
            nr_votes=models.Count('vote'))

# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=100)
    submitter = models.ForeignKey(User)
    submitted_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    
    with_votes = SnippetVoteCountManager()
    objects = models.Manager()
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('snippet-detail', kwargs={'slug': self.id})

class Vote(models.Model):
    voted_by = models.ForeignKey(User)
    snippet = models.ForeignKey(Snippet)
    vote_type = ('UPVOTE', 'DOWNVOTE')

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    last_active = models.DateTimeField(null=True)
    bio = models.TextField(null=True)