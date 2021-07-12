from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
import json
from .models import SavedRecipe

@login_required
def index(request):
    key_test = settings.API_KEY
    print(key_test)
    context = {
        'key': settings.API_KEY
    }
    return render(request, 'bigshop/index.html', context)


def save(request):
    print(request.body)
    data_json = request.body
    recipe_data = json.loads(data_json)
    recipe = SavedRecipe(name=recipe_data['title'], image=recipe_data['image'], source=recipe_data['details']['sourceUrl'], ingredients=recipe_data['ingredients'], calories=recipe_data['nutrition']['calories'], protein=recipe_data['nutrition']['protein'], carbs=recipe_data['nutrition']['carbs'], fat=recipe_data['nutrition']['fat'], instructions=recipe_data['instructions'], user=request.user )
    recipe.save()
    return HttpResponse('Yo!')


def recipe_book(request):
    
    return render(request, 'bigshop/book.html')

def get_saved_recipes(request):
    recipes = SavedRecipe.objects.all()
    recipes_data = []
    for recipe in recipes:
        recipes_data.append({
            'name': recipe.name,
            'image': recipe.image,
            'source': recipe.source,
            'ingredients': recipe.ingredients,
            'calories': recipe.calories,
            'protein:': recipe.protein,
            'carbs': recipe.carbs,
            'fat': recipe.fat,
            'instructions': recipe.instructions,

        })
    return JsonResponse({'recipes': recipes_data})




def grocery_list(request):
    return HttpResponse('Shopping list goes here!!')

