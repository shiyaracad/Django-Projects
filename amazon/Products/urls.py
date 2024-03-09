from django.contrib import admin
from django.urls import path
from Products.views import getAll, getById , index , html

urlpatterns = [
    path('', index),
    path('getAll/', getAll),
    path('getById/<id>', getById),
    path('test', html),
]
