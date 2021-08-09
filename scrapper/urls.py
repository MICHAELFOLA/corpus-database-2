from django.urls import path
from scrapper import views
from .task import json_result
from .views import download

app_name = 'scrapper'

urlpatterns = [

    
    path("", views.webcrawl_input, name='search'),
    path('result/', json_result, name='result'),
    path('download/', download, name='download'),



]