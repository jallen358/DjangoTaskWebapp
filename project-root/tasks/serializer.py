from rest_framework import serializers

from tasks.models import Task, Project, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','username','email','role']      
        
class ProjectSerializer(serializers.ModelSerializer):
    owner_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='owner')
    class Meta:
        model = Project        
        fields = ['id','name', 'description', 'owner_id', 'owner']  
        
class TaskSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)  
    assigned_to = UserSerializer(read_only=True)  
    project = ProjectSerializer(read_only=True)
    class Meta:
        model = Task 
        fields = ['title', 'description', 'status','priority','due_date', 'project', 'assigned_to', 'created_by','created_at', 'updated_at']


