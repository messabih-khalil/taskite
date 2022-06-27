from django.urls import path


from .views import FriendsApiView  , addFriend , delete_friend , get_invitations , accept_invitaion , delete_invitaion
urlpatterns = [
    # Get friends ENDPOINT
    path("" , FriendsApiView.as_view()),
    # Add friends ENDPOINT
    path("add/" , addFriend),
    # delete friend ENDPOINT
    path("delete/" , delete_friend),
    # Get Invitations
    path("inv/" , get_invitations),
    # delete invitation
    path("inv/delete/" , delete_invitaion),
    # accept Invitations
    path("inv/accept/" , accept_invitaion),


]
