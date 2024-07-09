from django.contrib import admin

from favorites.models import Favorite

# Register your models here.
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', "cookbook")

admin.site.register(Favorite, FavoriteAdmin)