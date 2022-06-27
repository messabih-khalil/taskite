from django.contrib import admin


# import models

from .models import Friend , Invitation
# Register your models here.

admin.site.register(Friend)
admin.site.register(Invitation)
