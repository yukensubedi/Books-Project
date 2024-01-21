from django.urls import path
from . import views
from books.views import *

urlpatterns = [
    path('test/', views.test)
]