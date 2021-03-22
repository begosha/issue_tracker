from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, Status, Type
from webapp.forms import TaskForm
from django.urls import reverse
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView
from .base_view import CustomFormView


class IndexView(ListView):
   template_name = 'index.html'
   context_object_name = 'tasks'
   model = Task
   ordering = ['-created_at']
   paginate_by = 10
   paginate_orphans = 1
   
#    def get_context_data(self, **kwargs):
#        kwargs['tasks'] = Task.objects.all()
#        return super().get_context_data(**kwargs)


class TaskView(TemplateView):

    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        kwargs['task'] = get_object_or_404(Task, id=kwargs.get('pk'))
        return super().get_context_data(**kwargs)

class TaskAddView(CustomFormView):
    template_name = 'task_add_view.html'
    form_class = TaskForm
    redirect_url = 'index'
    def form_valid(self, form):
        task_type = form.cleaned_data.pop('task_type')
        task = Task()
        for key, value in form.cleaned_data.items():
            setattr(task, key, value)
        task = form.save()
        task.task_type.set(task_type)

        return super().form_valid(form)


        
class UpdateView(FormView):
    form_class = TaskForm
    template_name = 'task_update_view.html'

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        return super().get_initial()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_object(self):
        task = get_object_or_404(
            Task, id=self.kwargs.get('pk')
            )
        return task

    def form_valid(self, form):
        task_type = form.cleaned_data.pop('task_type')
        form.save()
        self.task.task_type.set(task_type)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task', kwargs={'pk': self.kwargs.get('pk')})

       
class DeleteView(TemplateView):
   template_name = 'index.html'
   
   def get_context_data(self, **kwargs):
       task = get_object_or_404(Task, id=kwargs.get('pk'))
       task.delete()
       kwargs['tasks'] = Task.objects.all()
       return super().get_context_data(**kwargs)

