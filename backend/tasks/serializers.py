from rest_framework import serializers

# import models 
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['pk','title', 'description', 'start_time', 'end_time' , 'status' ,'created_at']
        read_only_fields = ('pk', 'status' , 'created_at',)
        write_only_fields = ('user',)