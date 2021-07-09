from django.shortcuts import render,reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
import django.contrib.auth

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        existing_user = User.objects.filter(username=username)
        if existing_user is not None:
            render(request, 'users/register.html', { 'error': 'A user with that name already exists.'})
            user = User.objects.create_user(username, email, password)
            django.contrib.auth.login(request, user)
        return HttpResponseRedirect(reverse('bigshop:index'))
    return render(request, 'users/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(request, username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request, user)
            return HttpResponseRedirect(reverse('bigshop:index'))
        else:
            return render(request, 'users/login.html', {'error': 'Bad username / password'})
    return render(request, 'users/login.html')
   

def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse('users:login'))

