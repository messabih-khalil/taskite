# IMPORT SERIALIZER
from dataclasses import fields
import profile
from statistics import mode
from rest_framework import serializers
from urllib3 import Retry

from accounts.models import NewUser, UserProfile

# IMPORT MODELS
from .models import Project

# IMPORT METHODS 
# from methods.getUserInfo import user_info

# import serializer
from persons.serializers import TeamFriendsSerializer

class ProjectSerializer(serializers.ModelSerializer):
    users_profile = serializers.SerializerMethodField("get_users_profile")

    def get_users_profile(self, obj):
        persons_in_team = obj.team.all()
        profiles = []
        for person in persons_in_team:
            user = NewUser.objects.get(user_name = person.user_name)
            profile = UserProfile.objects.filter(user = user)
            serializer = TeamFriendsSerializer(profile , many=True)
            profiles += serializer.data

       
        return profiles
    class Meta:
        model = Project
        fields = [
            "pk","admin","title","description","users_profile","status","start_date", "end_date","created_at"
        ]

        read_only_fields = ('pk', 'status' , 'created_at',  'users_profile')
        write_only_fields = ("admin","team")

