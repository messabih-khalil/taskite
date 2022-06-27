from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
# import serializer
from .serializers import ProjectSerializer 
# import models
from .models import Project 
from accounts.models import NewUser

# import permission 
from rest_framework.permissions import IsAuthenticated

from methods.permissions import IsAdmin
# Create your views here.


# GET and POST projects

class ProjectAPIView(APIView):

    permission_classes = (IsAuthenticated,)
    # GET all PROJECTS

    def get(self , request):
        try:
            projects = Project.objects.filter(admin=request.user)
            serializer = ProjectSerializer(projects , many=True)
            return Response(data=serializer.data , status=status.HTTP_200_OK)
        except :
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # POST new PROJECT

    def post(self , request):
        try:
            if request.data:
                project = Project.objects.create(
                    admin = request.user ,
                    title = str(request.data["title"]),
                    description = str(request.data["description"]),
                    start_date = str(request.data["start_date"]),
                    end_date = str(request.data["end_date"]),
                )

                try :
                    for friend_username in request.data["team"]:
                            friend = NewUser.objects.get(user_name=str(friend_username))
                            project.team.add(friend)
                except:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                project.save()
             
                serializer = ProjectSerializer(project)

                return Response(data=serializer.data , status=status.HTTP_201_CREATED)
        except:
            return Response({"error" : "Data should not be empty"} , status=status.HTTP_204_NO_CONTENT)

    
# PUT and DELETE PROJECT

class UpdateAndDeleteProject(APIView):

    # UPDATE project
    permission_classes = (IsAdmin,)

    def put(self , request , project_id):
        try : 
            project = Project.objects.get(pk=int(project_id))
            try : 
                self.check_object_permissions(request, project)
            except :
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            if project:

                project.title = str(request.data["title"])
                project.description = str(request.data["description"])
                project.start_date = str(request.data["start_date"])
                project.end_date = str(request.data["end_date"])

                project.team.clear()

                try :
                    for friend_username in request.data["team"]:
                            friend = NewUser.objects.get(user_name=str(friend_username))
                            project.team.add(friend)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)

                project.save()

                serializer = ProjectSerializer(project)

                return Response(data=serializer.data , status=status.HTTP_200_OK)
        except : 
            return Response(status=status.HTTP_400_BAD_REQUEST)

        
    # DELETE projects 

    def delete(self , request , project_id):
        try:
            project = Project.objects.get(pk=int(project_id))
            try : 
                self.check_object_permissions(request, project)
            except :
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            if project:
                project.delete()
                return Response({"message" : "Project Was Deleted"} , status=status.HTTP_204_NO_CONTENT)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Update Project Status 

@api_view(["PUT"])
def updateStatus(request , project_id):
    if project_id :
        try :
            project = Project.objects.get(pk=project_id)
            try:
                project.status = request.data["status"]
                project.save()
                return Response({"message" : "status changed"} , status = status.HTTP_200_OK)
            except:
                return Response({"error" : "Process error"} , status=status.HTTP_400_BAD_REQUEST)

        except :
            return Response({"message" : "task is not exist"},status=status.HTTP_400_BAD_REQUEST)
     



# GET Projects when user inside the team


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getTeamProjects(request):
    
    project = Project.objects.filter(team = request.user)
    serializer = ProjectSerializer(project , many=True)
    return Response(data=serializer.data , status=status.HTTP_200_OK)
    

