from django.urls import path

# IMPORT VIEWS
from .views import ProjectAPIView , UpdateAndDeleteProject , updateStatus ,getTeamProjects

urlpatterns = [
    # POST and GET Project ENDPOINT 
    path("",ProjectAPIView.as_view()),
    # PUT adn DELETE Project ENDPOINT
    path("<int:project_id>/",UpdateAndDeleteProject.as_view()),
    # change project Status ENDPOINT
    path("status/<int:project_id>/",updateStatus),
    # team ENDPOINT
    path("team/",getTeamProjects),

]
