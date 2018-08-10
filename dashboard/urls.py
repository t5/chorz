from django.urls import path
import django
from django.urls import include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
