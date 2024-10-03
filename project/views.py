from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Client, Message, ProjectType, Project, Task
from .serializers import ClientSerializer, MessageSerializer, ProjectSerializer, ProjectTypeSerializer, TaskSerializer

# Create your views here.

class ProjectTypeView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = ProjectType.objects.all()  
        serializers = ProjectTypeSerializer(result, many=True)  
        return Response({'status': 'success', "ProjectType":serializers.data}, status=200)  
    
class ClientView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Client.objects.all()  
        serializers = ClientSerializer(result, many=True)  
        return Response({'status': 'success', "client":serializers.data}, status=200)  

class ProjectView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Project.objects.all()  
        serializers = ProjectSerializer(result, many=True)  
        return Response({'status': 'success', "Project":serializers.data}, status=200)  
    
class TaskView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Task.objects.all()  
        serializers = TaskSerializer(result, many=True)  
        return Response({'status': 'success', "Task":serializers.data}, status=200)  

class MessageView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Message.objects.all()  
        serializers = MessageSerializer(result, many=True)  
        return Response({'status': 'success', "Message":serializers.data}, status=200)  