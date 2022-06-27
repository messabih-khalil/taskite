from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# import models 
from accounts.models import UserProfile 
from friends.models import Friend
from django.db.models import Q
# import serializer

from .serializers import UserInfoSerializer

# import permissions

from methods.permissions import IsUser

# Create your views here.

# User info

class UserInfoApiView(APIView):

    permission_classes = (IsUser,)

    def get(self , request):
        
            try:
                profile = UserProfile.objects.get(user=request.user)
                try : 
                    self.check_object_permissions(request, profile)
                except :
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            except :
                return Response({"Error" : "User not found"} , status = status.HTTP_400_BAD_REQUEST)
            serializer = UserInfoSerializer(profile , context={"request":request})
            return Response(data=serializer.data , status = status.HTTP_200_OK)

    def put(self , request):
        if request.data != None:
            try:
                profile = UserProfile.objects.get(user = request.user)
            except: 
                return Response(status=status.HTTP_400_BAD_REQUEST)

            profile.nick_name = request.data["nick_name"]
            profile.facebook = request.data["facebook"]
            profile.instagram = request.data["instagram"]
            profile.twitter = request.data["twitter"]
            profile.github = request.data["github"]

            profile.save()

            serializer = UserInfoSerializer(profile)

            return Response(data = serializer.data , status=status.HTTP_200_OK)


@api_view(["POST"])
def changeProfileImage(request):
    if request.data != None:
        profile = UserProfile.objects.get(user = request.user)
        if profile.user == request.user:
            profile.profile_image = request.data["image"]
            profile.save()
            serializer = UserInfoSerializer(profile , context={"request":request})
            return Response(data=serializer.data , status=status.HTTP_200_OK)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST)

# search about user
@api_view(["GET"])
def searchProfiles(request,username):
    print(username)
    if username:
        # try:
            friends = Friend.objects.filter((Q(friend__user_name__icontains=username) & Q(user = request.user)))
            friends2 = Friend.objects.filter((Q(user__user_name__icontains=username) & Q(friend = request.user)))
            usernames = []
            for user in friends:
                usernames.append(user.friend.user_name)
            for user in friends2:
                usernames.append(user.user.user_name)
            # get profiles of user in friends
            friendsProfile =  UserProfile.objects.filter(Q(username__in=usernames))
            # get profile of users is not in friend model
            profiles = UserProfile.objects.filter(Q(username__icontains=username) & ~Q(user=request.user) & ~Q(username__in=usernames))
            # serializer data
            friends = UserInfoSerializer(friendsProfile , many=True , context={"request":request})
            profiles = UserInfoSerializer(profiles , many=True , context={"request":request})
            return Response({
                "friends" : friends.data,
                "profiles" : profiles.data,
            })
        # except:
            # pass