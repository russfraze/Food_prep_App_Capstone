from django.urls import path
from . import views

app_name = 'bigshop'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('save/', views.save, name='save')
]

