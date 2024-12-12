from django import forms
from tasks.models import Project
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','description','owner']