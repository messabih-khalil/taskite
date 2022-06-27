from os import stat
import profile
from time import sleep
from webbrowser import get
from django.shortcuts import render

from django.db.models import Q

# rest framework
from rest_framework.decorators import api_view ,permission_classes

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
# import models

from accounts.models import NewUser , UserProfile
from .models import Friend, Invitation

# import serializers

from persons.serializers import TeamFriendsSerializer

# Create your views here.



# GET ALL FRIENDS

class FriendsApiView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self , request):
       
            try:
                user = request.user
                try :
                    # Filtering all friends that accepted invitation
                    
                    friends = (Friend.objects.filter(Q(user = user) | Q(friend=user))).filter(Q(status_friend = 'accept'))
                    profiles_QS = []
                    # Add friend to profile_qs 
                    for friend in friends:
                        # Check if user passed in match the friend.user
                        if friend.user == user:
                            profile = UserProfile.objects.filter(user__user_name=friend.friend.user_name)
                        # Check if user passed in match the friend.friend
                        else:
                            profile = UserProfile.objects.filter(user__user_name=friend.user.user_name)
                        # Add user profile to profile_qs list 
                        profiles_QS += profile
                    # converting profile_qs queryset's to json format with serializer
                    serializer = TeamFriendsSerializer(profiles_QS , many=True , context={"request":request})

                    return Response(data=serializer.data,status=status.HTTP_200_OK)
                except : 
                    return Response(status = status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"Error" : "User not found"} , status=status.HTTP_400_BAD_REQUEST)

            

# Add new friends

@api_view(["POST"])
@permission_classes([IsAuthenticated])

def addFriend(request):
    friend_name = str(request.data['friend_name'])
    send_invitation = Friend.objects.create(user=request.user , friend = NewUser.objects.get(user_name=friend_name))

    send_invitation.save()
    return Response({"message" : "add"} , status=status.HTTP_200_OK)



# Delete friends or invitation

@api_view(["DELETE"])
def delete_friend(request):
    friend = str(request.data['friend_name'])
    invitation = Invitation.objects.filter(Q(user__user_name = friend , invitation_from=request.user)|Q(user = request.user , invitation_from__user_name=friend))
    print(invitation)
    get_friend_qs = Friend.objects.get(Q(user = request.user , friend__user_name = friend)|Q(user__user_name = friend , friend = request.user))
    print(get_friend_qs)
    if get_friend_qs.user == request.user or get_friend_qs.friend == request.user:
        if(invitation.exists()):
            invitation.delete()
        get_friend_qs.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
                


@api_view(["DELETE"])
def delete_invitaion(request):
    try:
        friend = NewUser.objects.get(user_name = str(request.data['friend_name']))
        try:
            get_invitation = Invitation.objects.get(user = request.user , invitation_from = friend)
            get_friend_qs = Friend.objects.get(user__user_name = friend , friend = request.user)
            if get_invitation.user == request.user:
                get_invitation.delete()
                get_friend_qs.delete()
                return Response({"message" : "Deleted"} , status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Get All Invitation in progress

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_invitations(request):
    
    inv = Invitation.objects.filter(user = request.user , invitation_status="inProgress").order_by('-created_at')
    if inv:
        profiles = []
        for i in inv:
            profile = UserProfile.objects.get(user__user_name=i.invitation_from.user_name)
            profiles.append(profile)

        serializer = TeamFriendsSerializer(profiles , many=True , context={"request":request})
        return Response(data = serializer.data , status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)

# Accept Invitaion
@api_view(["POST"])
def accept_invitaion(request):
    user = request.user
    invitation_from = NewUser.objects.get(user_name = request.data["invitation_from"])
    try:
        inv = Invitation.objects.get(user = user , invitation_from = invitation_from)
        friend = Friend.objects.get(user = invitation_from , friend = user)
        if inv:
            if inv.user == request.user:
                friend.status_friend = "accept"
                friend.save()
                if friend.status_friend == "accept":
                    inv.delete()

                return Response(status=status.HTTP_200_OK)
        else :
            return Response(status= status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST) 