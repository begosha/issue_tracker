from django import forms
from .models import Task, Type, Status


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        task_type = forms.ModelMultipleChoiceField(required=False, label='Types',queryset=Type.objects.all())
        status = forms.ModelChoiceField(queryset=Status.objects.all())
        fields = ('summary','description', 'status', 'task_type')

class SimpleSearchForm(forms.Form):

    search = forms.CharField(max_length=100, required=False, label="Search")
