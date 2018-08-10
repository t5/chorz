from django.contrib import admin

# Register your models here.

from .models import Chore
from .models import Scheduler

@admin.register(Chore)
class ChoreAdmin(admin.ModelAdmin):
    list_display = ('name','description', 'user')
    fields = ['name', 'description', 'user']

@admin.register(Scheduler)
class SchedulerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        no = self.model.objects.count()
        if no >= 1:
            return False
        else:
            return True

