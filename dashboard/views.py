from django.shortcuts import render
from .models import Chore
from django.views import generic

# Create your views here.

class Index(generic.ListView):
    model = Chore

    template_name = 'index.html'
