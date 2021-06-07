from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Serializer
from .models import Task


# Create your views here.

@api_view(['GET'])
def OverviewApi(request):
    api_urls = {
        'List': '/task-list/',
        'Detail-view': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


# to display all the tasks sotred in the DB
@api_view(['GET'])
def Listtask(request):
    tasks = Task.obj.all()
    serializer = Serializer(tasks, many=True)
    return Response(serializer.data)


# To update a single task depending on the id input  by user
@api_view(['POST'])
def Updatetask(request, pk):
    task = Task.obj.get(id=pk)
    serializer = Serializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# To create a new task
@api_view(['POST'])
def Createtask(request):
    serializer = Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# To delete a taskfrom the DB
@api_view(['DELETE'])
def Deletetask(request, pk):
    task = Task.obj.get(id=pk)
    task.delete()
    return Response("Tasks deleted successfully.")

