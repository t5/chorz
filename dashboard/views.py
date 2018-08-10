from django.shortcuts import render
from .models import Chore
from .models import Scheduler 
from django.views import generic

# Create your views here.

class Index(generic.ListView):
    model = Chore
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scheduler = Scheduler.objects.get(pk=1)
        context['start_date'] = scheduler.start
        return context
