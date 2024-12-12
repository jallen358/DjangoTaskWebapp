from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'users'

class Project(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey('User', models.CASCADE, related_name='projects', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __self__(self):
        return self.name or "Unnamed Project"
    class Meta:
        db_table = 'projects'

class Task(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey('Project', models.CASCADE, related_name='tasks', blank=True, null=True)
    assigned_to = models.ForeignKey('User', models.CASCADE, related_name='assigned_tasks', blank=True, null=True, db_column='assigned_to')
    created_by = models.ForeignKey('User', models.CASCADE, related_name='created_tasks', blank=True, null=True, db_column='created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'tasks'

class Comment(models.Model):
    task = models.ForeignKey('Task', models.CASCADE, related_name='comments', blank=True, null=True)
    created_by = models.ForeignKey('User', models.CASCADE, related_name='comments', blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'

class Notification(models.Model):
    user = models.ForeignKey('User', models.CASCADE, related_name='notifications', blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notifications'

class TaskAssignment(models.Model):
    task = models.ForeignKey('Task', models.CASCADE, related_name='assignments', blank=True, null=True)
    user = models.ForeignKey('User', models.CASCADE, related_name='assignments', blank=True, null=True)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'task_assignments'
