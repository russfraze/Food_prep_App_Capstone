from django.contrib import admin
from .models import SavedRecipe, SavedListItem

admin.site.register(SavedRecipe)
admin.site.register(SavedListItem)
