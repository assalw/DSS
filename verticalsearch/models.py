from django.db import models

# Create your models here.

class GitHubUser(models.Model):
    username = models.CharField(max_length=200)
