from django.contrib import admin
from models import RedditUser

# Register your models here.

class RedditUserAdmin(admin.ModelAdmin):
    list_display = ['username']

admin.site.register(RedditUser, RedditUserAdmin)