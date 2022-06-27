from django.urls import path

# import views

from .views import TaskApiView ,DeleteUpdateTaskAPIView , updateTaskStatus

urlpatterns = [
    # GET and POST task ENDPOINT
    path("" , TaskApiView.as_view(),),
    # update and delete task ENDPOINT
    path("<int:task_id>/" , DeleteUpdateTaskAPIView.as_view(),),
    # Change Task status ENDPOINT
    path("status/<int:task_id>/" , updateTaskStatus),

]
