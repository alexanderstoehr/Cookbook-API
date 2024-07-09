from django.contrib import admin

from cookbooks.models import Cookbook

# Register your models here.

class CookbookAdmin(admin.ModelAdmin):
    list_display = ("id","description",'title', 'author', 'updated_at')

admin.site.register(Cookbook, CookbookAdmin)