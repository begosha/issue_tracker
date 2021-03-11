from django import forms

from webapp.models import Task, Type, Status


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        task_type = forms.ModelChoiceField(queryset=Type.objects.all())
        status = forms.ModelChoiceField(queryset=Status.objects.all())
        fields = ('summary','description', 'status', 'task_type')

