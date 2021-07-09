from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required

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
    return HttpResponse('Yo!')


def recipe_book(request):
    return('Saved recipes go here!')


def grocery_list(request):
    return('Shopping list goes here!!')