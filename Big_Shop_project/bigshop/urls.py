from django.urls import path
from . import views

app_name = 'bigshop'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('save/', views.save, name='save'),
    path('recipe_book/', views.recipe_book, name='recipe_book'),
    path('grocery_list/', views.grocery_list, name='grocery_list'),
    path('get_saved_recipes/', views.get_saved_recipes, name='get_saved_recipes')

]

