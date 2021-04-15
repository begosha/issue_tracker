from django import forms
from django.contrib.auth.models import User
from .models import Task, Type, Status, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        task_type = forms.ModelMultipleChoiceField(required=False, label='Types',queryset=Type.objects.all())
        status = forms.ModelChoiceField(queryset=Status.objects.all())
        fields = ('summary','description', 'status', 'task_type',)

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_name','project_description', 'start_date', 'end_date')

class UsersForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, label='Users',queryset=User.objects.all())
    class Meta:
        model = Project
        fields=('users',)
        

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search")

