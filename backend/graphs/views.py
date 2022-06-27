# import models 
from venv import create
from tasks.models import Task

from projects.models import Project

from django.utils.timezone import get_current_timezone

from datetime import date


# import rest_framework

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from rest_framework.decorators import api_view , permission_classes

# Create your views here.

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def daily_task_progress(request):
    tasks = Task.objects.filter(user = request.user , created_at = date.today())
    return Response({
        "new_task" : tasks.filter(status="new" ).count(),
        "inprogress_task" : tasks.filter(status="inProgress").count(),
        "completed_task" : tasks.filter(status="done").count(),
    })
