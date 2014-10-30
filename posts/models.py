from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True, default=datetime.now)
    date_last_edit = models.DateTimeField(auto_now=True, default=datetime.now)
    votes = models.IntegerField(default=0)