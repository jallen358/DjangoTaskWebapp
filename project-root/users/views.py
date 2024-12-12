from django.shortcuts import render
from tasks.models import  User, Project
from users.forms import UserForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from tasks.serializer import UserSerializer, ProjectSerializer
# Create your views here.
class UserView(APIView):
    def get(self, request):
        users = User.objects.all()  # Fetch all users
        serializer = UserSerializer(users, many=True)  # Serialize the data
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def user_projects(request, user_id):
    user = User.objects.get(id=user_id)
    projects = Project.objects.filter(owner_id=user_id)
    project_serializer = ProjectSerializer(projects, many=True)
    return Response({
        "username": user.username,
        "projects": project_serializer.data
    })

