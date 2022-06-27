from django.contrib import admin

# import models
from .models import Task , SubTask
# Register your models here.

admin.site.register(Task)
admin.site.register(SubTask)