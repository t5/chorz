from django.shortcuts import render
from .models import Chore
from .models import Scheduler 
from django.views import generic
import datetime
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.

class Index(generic.ListView):
    model = Chore
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        # if the button is pressed, switch the 'is_done'
        try:
            users_chore = Chore.objects.get(user__username=self.request.user.username)
        except Chore.DoesNotExist:
            users_chore = None

        if users_chore:
            users_chore.is_done = not users_chore.is_done
            users_chore.save()

        return HttpResponseRedirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        scheduler = Scheduler.objects.get(pk=1)

        start_date = scheduler.start
        end_date = start_date + datetime.timedelta(days=7)

        this_date = datetime.date.today()
        
        def rotate(l, rotations):
            return l[rotations:] + l[:rotations]

        rotations = 0
        if this_date >= end_date:
            # rotate the housemates by calculating how many rotations
            rotations = (this_date - start_date).days // 7
            currentUsers = []
            for chore in Chore.objects.all():
                currentUsers.append(chore.user)

            newUsers = rotate(currentUsers, rotations)
            for chore, user in zip(Chore.objects.all(), newUsers):
                chore.user = user
                chore.save()

            scheduler.start = end_date
            start_date = scheduler.start
            end_date = start_date + datetime.timedelta(days=7)
            scheduler.save()

        # check if the user has completed the task
        try:
            users_chore = Chore.objects.get(user__username=self.request.user.username)
        except Chore.DoesNotExist:
            users_chore = None
            
        context['start_date'] = f'{start_date.month}/{start_date.day}' 
        context['end_date'] = f'{end_date.month}/{end_date.day}'
        context['this_date'] = this_date
        context['rotations'] = rotations
        context['logged_in_user'] = self.request.user
        context['users_chore'] = users_chore 

        return context
