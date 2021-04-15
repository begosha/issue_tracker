from django.shortcuts import render, get_object_or_404, redirect
from ..models import Task, Status, Type, Project
from ..forms import TaskForm, SimpleSearchForm, ProjectForm
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from ..base_view import CustomFormView
from django.db.models import Q
from django.utils.http import urlencode
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class IndexView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(project_name__icontains=self.search_value) | Q(project_description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

class ProjectView(DetailView):
    model = Project
    template_name = 'project/project_view.html'

class ProjectCreate(PermissionRequiredMixin, CreateView):
    template_name = 'project/project_add_view.html'
    form_class = ProjectForm
    model = Project
    permission_required = 'webapp.add_project'


    def form_valid(self, form):
        project = form.save(commit=False)
        project.author = self.request.user
        project.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')

class TaskCreate(PermissionRequiredMixin, CreateView):
    template_name = 'task/task_add_view.html'
    form_class = TaskForm
    model = Task
    permission_required = 'webapp.add_task'

    def has_permission(self):
        project = get_object_or_404(Project, id=self.kwargs.get('pk'))
        return project.author == self.request.user and super().has_permission()


    def get_success_url(self):
        return reverse(
            'project',
            kwargs={'pk': self.kwargs.get('pk')}
        )

    def form_valid(self, form):
        project = get_object_or_404(Project, id=self.kwargs.get('pk'))
        task = form.instance
        task.project = project
        task.author = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = ProjectForm
    model = Project
    template_name = 'project/project_update_view.html'
    context_object_name = 'project'
    permission_required = 'webapp.change_project'


    def get_success_url(self):
        return reverse('project', kwargs={'pk': self.kwargs.get('pk')})


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    model = Project
    context_object_name = 'product'
    success_url = reverse_lazy('index')
    permission_required ='webapp.delete_project'


    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


