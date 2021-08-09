from django.urls import path
from scrapper import views
from .task import add

app_name = 'scrapper'

urlpatterns = [

    
    path("", views.webcrawl_input, name='search'),
    path('result/', add, name='result'),



]