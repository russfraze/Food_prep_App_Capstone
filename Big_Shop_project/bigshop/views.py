from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
import json
from .models import SavedRecipe, SavedListItem

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
    recipe = SavedRecipe(name=recipe_data['title'], 
        image=recipe_data['image'], 
        source=recipe_data['details']['sourceUrl'], 
        ingredients=json.dumps(recipe_data['ingredients']),
        calories=recipe_data['nutrition']['calories'],
        protein=recipe_data['nutrition']['protein'],
        carbs=recipe_data['nutrition']['carbs'],
        fat=recipe_data['nutrition']['fat'],
        instructions=recipe_data['instructions'],
        user=request.user )
    recipe.save()
    return HttpResponse('Yo!')


def recipe_book(request):
    
    return render(request,'bigshop/book.html')

def get_saved_recipes(request):
    recipes = SavedRecipe.objects.filter(user=request.user)
    recipes_data = []
    for recipe in recipes:
        recipes_data.append({
            'id': recipe.id,
            'name': recipe.name,
            'image': recipe.image,
            'source': recipe.source,
            'ingredients': json.loads(recipe.ingredients),
            'calories': recipe.calories,
            'protein': recipe.protein,
            'carbs': recipe.carbs,
            'fat': recipe.fat,
            'instructions': recipe.instructions,

        })
    return JsonResponse({'recipes': recipes_data})

def delete(request):
    print(request.GET['id'])
    id = request.GET['id']
    recipe = SavedRecipe.objects.get(id=id)
    recipe.delete()
    return HttpResponse('zap!')


def grocery_list(request):
    return render(request,'bigshop/list.html')

def add_ingredients(request):
    print(request.GET['id'])
    # look up the recipe given the id
    # turn the ingredients into a list of dictionaries
    # loop over those ingredients
    # create a 'SavedListItem' for each ingredient and save it
    id = request.GET['id']
    recipe = SavedRecipe.objects.get(id=id)
    ingredients_json = recipe.ingredients
    ingredients_list = json.loads(ingredients_json)
    for ingredient in ingredients_list:
        list_item = SavedListItem(
            amount = ingredient['amount'], 
            unit= ingredient['unit'], 
            name = ingredient['name'], 
            aisle= ingredient['aisle'],
            user= request.user)
        list_item.save()
        print(ingredient['name'],ingredient['aisle'])

    # print(ingredients_list)

    return HttpResponse('yo')


def get_saved_list(request):
    ingredients = SavedListItem.objects.filter(user=request.user)
    ingredients_data = []
    for ingredient in ingredients:
        ingredients_data.append({
            'name': ingredient.name,
            'amount': ingredient.amount,
            'unit': ingredient.unit,
            'aisle': ingredient.aisle,

        })
    return JsonResponse({'ingredients': ingredients_data})


def clear_list(request):
    clear = SavedListItem.objects.filter(user=request.user)
    clear.delete()
    return HttpResponseRedirect(reverse('bigshop:grocery_list')) 