from django.contrib import admin

# Register your models here.

from .models import Chore

@admin.register(Chore)
class ChoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_start', 'date_end', 'description')
    fields = ['name', 'description', ('date_start', 'date_end')]
