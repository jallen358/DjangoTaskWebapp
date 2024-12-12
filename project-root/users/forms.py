from django import forms
from tasks.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','role']