from django.urls import path

# import views

from .views import UserInfoApiView , changeProfileImage ,searchProfiles

urlpatterns = [
    path("" , UserInfoApiView.as_view()),
    path("image/" , changeProfileImage),
    # search
    path("search/<str:username>/" , searchProfiles),
]
