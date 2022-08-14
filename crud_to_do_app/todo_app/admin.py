from django.contrib import admin
from .models import TodoData

# Register your models here.


class TodoDataAdmin(admin.ModelAdmin):
    list_display = ['task_to_do']

admin.site.register(TodoData, TodoDataAdmin)
