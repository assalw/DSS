from django.contrib import admin
from models import GitHubUser

# Register your models here.

class GitHubUserAdmin(admin.ModelAdmin):
    list_display = ['username']

admin.site.register(GitHubUser, GitHubUserAdmin)