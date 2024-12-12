from django.shortcuts import render, get_object_or_404, redirect
from tasks.models import Task
from tasks.forms import TaskForm
from rest_framework.views import APIView
from rest_framework.response import Response
from tasks.serializer import *

class TaskView(APIView):
    def get(self, request):
        task = [{"title" : task.title,
                   "description" : task.description,
                   "status":task.status,
                   "priority":task.priority,
                   "due_date":task.due_date,
                   "project": ProjectSerializer(task.project).data,
                   "assigned_to":UserSerializer(task.assigned_to).data,
                   "created_by":UserSerializer(task.created_by).data,
                   "created_at":task.created_at,
                   "updated_at":task.updated_at}
                  for task in Task.objects.all()] 
        return Response(task)
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

def task_list(request): 
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks':tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html',{'task': task})

def task_create(request):
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form':form})

def task_edit(request, task_id):
    task=get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'task': task})
