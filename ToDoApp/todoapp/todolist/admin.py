from django.contrib import admin
from . import models
# Register your models here.
class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "due_date")

admin.site.register(models.Task, TodoListAdmin)