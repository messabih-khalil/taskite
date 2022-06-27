from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.decorators import api_view
# import serializer
from .serializers import TaskSerializer
# import models
from .models import Task
# import permissions
from rest_framework.permissions import IsAuthenticated

from methods.permissions import IsUser
# Create your views here.


# Create and delete TASK

class TaskApiView(APIView):

    permission_classes = (IsAuthenticated,)
    def get(self , request):
        try:
            tasks = Task.objects.filter(user=request.user).order_by("-created_at")
            try:
                serializer = TaskSerializer(tasks , many=True)
                return Response(serializer.data)
            except:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except :
            return Response({"err" : "there is no data"})
            
        
        
        
    def post(self , request):
        task = Task.objects.create(
            user = request.user,
            title = request.data["title"],
            description = request.data["description"],
            start_time = request.data["start_time"],
            end_time = request.data["end_time"],
        )
       
        task.save()
        serializer = TaskSerializer(task , many=False)
        return Response(serializer.data ,status=status.HTTP_201_CREATED)


    

# Update And Delete task 

class DeleteUpdateTaskAPIView(APIView):
    permission_classes = (IsUser,)
    # Delete Task
    def delete(self , request , task_id):
        try:
            if task_id :
                try :
                    task = Task.objects.get(pk=task_id)
                    if task :
                        try:
                            self.check_object_permissions(request, task)
                        except:
                            return Response(status=status.HTTP_401_UNAUTHORIZED)
                        task.delete()
                        return Response({"message" : "Task Was Deleted"} , status=status.HTTP_204_NO_CONTENT)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)

        except : 
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # Update Task

    def put(self , request , task_id):
        try:
            if task_id :
                    try :
                        task = Task.objects.get(pk=task_id)
                        try:
                            self.check_object_permissions(request, task)
                        except:
                            return Response(status=status.HTTP_401_UNAUTHORIZED) 
                        task.title = request.data["title"]
                        task.description = request.data["description"]
                        task.start_time = request.data["start_time"]
                        task.end_time = request.data["end_time"]
                        
                        task.save()

                        return Response({"message" : "Task Was Updated"} , status=status.HTTP_200_OK)
                        
                    except :
                        return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            

# Update Task Status 

@api_view(["PUT"])
def updateTaskStatus(request , task_id):
    if task_id :
        try :
            task = Task.objects.get(pk=task_id)
            if task.user == request.user:
                try:
                    task.status = request.data["status"]
                    task.save()
                    return Response({"message" : "status changed"} , status = status.HTTP_200_OK)
                except:
                    return Response({"error" : "Process error"} , status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        except :
            return Response({"message" : "task is not exist"},status=status.HTTP_400_BAD_REQUEST)