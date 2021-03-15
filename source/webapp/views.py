from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, Status, Type
from webapp.forms import TaskForm
from django.urls import reverse
from django.views.generic import View, TemplateView, RedirectView


class IndexView(TemplateView):
   template_name = 'index.html'
   
   def get_context_data(self, **kwargs):
       kwargs['tasks'] = Task.objects.all()
       return super().get_context_data(**kwargs)


class TaskView(TemplateView):

    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        kwargs['task'] = get_object_or_404(Task, id=kwargs.get('pk'))
        return super().get_context_data(**kwargs)

class TaskAddView(View):

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'task_add_view.html', context={'form': form})
       
    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)  
        if form.is_valid():  
            task = Task.objects.create(
                summary=form.cleaned_data.get('summary'),
                description=form.cleaned_data.get('description'),
                status=form.cleaned_data.get('status'),
                task_type=form.cleaned_data.get('task_type')
            )
            return redirect('task', pk=task.id)  
        return render(request, 'task_add_view.html', context={'form': form}) 

class UpdateView(View):
    
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get('pk'))
        print(task)
        form = TaskForm(initial={ 
            'summary': task.summary,
            'description': task.description,
            'status': task.status,
            'task_type': task.task_type.all()
            
        })  
        return render(request, 'task_update_view.html', context={'form': form, 'task': task})  
    
    def post(self, request, *args, **kwargs):
        kwargs ["task"] = get_object_or_404(Task, id=kwargs.get("pk"))
        form = TaskForm(data=request.POST)
        if form.is_valid(): 
            kwargs ["task"].summary = form.cleaned_data.get("summary")
            kwargs ["task"].description = form.cleaned_data.get("description")
            kwargs ["task"].status = form.cleaned_data.get("status")
            type_new = form.cleaned_data.pop('task_type')
            kwargs ["task"].save()
            kwargs ["task"].task_type.set(type_new) 
            return redirect('task', pk=kwargs ["task"].id)   

        return render(request, 'task_update_view.html', context={'form': form, 'task': kwargs ["task"]}) 
        

       
class DeleteView(TemplateView):
   template_name = 'index.html'
   
   def get_context_data(self, **kwargs):
       task = get_object_or_404(Task, id=kwargs.get('pk'))
       task.delete()
       kwargs['tasks'] = Task.objects.all()
       return super().get_context_data(**kwargs)

