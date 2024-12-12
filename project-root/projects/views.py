from django.shortcuts import render, get_object_or_404, redirect
from tasks.models import Project, User, Task
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from tasks.serializer import UserSerializer, ProjectSerializer, TaskSerializer
from django.http import Http404
# Create your views here.
class ProjectView(APIView):
    def get(self, request):
        project = [{"id" : project.id,
                    "title" : project.name,
                   "description" : project.description,
                   "owner":UserSerializer(User.objects.get(id=project.owner_id)).data,
                   "created_at":project.created_at,
                   "updated_at":project.updated_at}
                  for project in Project.objects.all()] 
        return Response(project)
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class ProjectDetail(APIView):
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ProjectTaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    
    @action(detail=True, methods=['get'])
    def get_byProject(self, request, pk):
        tasks=Task.objects.filter(project_id=pk)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)