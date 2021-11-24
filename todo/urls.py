from django.urls import path
from .views import *

urlpatterns = [
    path('todo/', todo, name = 'todo'),
    path('tdlist', display_todo, name = 'tdlist')
]
