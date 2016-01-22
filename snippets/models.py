from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=100)
    submitter = models.ForeignKey(User)
    submitted_date = models.DateTimeField()
    body = models.TextField()

class Vote(models.Model):
    voted_by = models.ForeignKey(User)
    snippet = models.ForeignKey(Snippet)
    vote_type = ('UPVOTE', 'DOWNVOTE')