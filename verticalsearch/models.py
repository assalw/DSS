from django.db import models

# Create your models here.

class RedditUser(models.Model):
    username = models.CharField(max_length=200)
