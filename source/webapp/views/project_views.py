from django.shortcuts import render, get_object_or_404, redirect
from ..models import Task, Status, Type, Project
from ..forms import TaskForm, SimpleSearchForm, ProjectForm
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from ..base_view import CustomFormView
from django.db.models import Q
from django.utils.http import urlencode


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

class ProjectCreate(CreateView):
    template_name = 'project/project_add_view.html'
    form_class = ProjectForm
    model = Project

    def form_valid(self, form):
        project = Project()
        for key, value in form.cleaned_data.items():
            setattr(project, key, value)

        project.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')

class TaskCreate(CreateView):
    template_name = 'task/task_add_view.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse(
            'project',
            kwargs={'pk': self.kwargs.get('pk')}
        )

    def form_valid(self, form):
        project = get_object_or_404(Project, id=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)

class ProjectUpdateView(UpdateView):
    form_class = ProjectForm
    model = Project
    template_name = 'project/project_update_view.html'
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project', kwargs={'pk': self.kwargs.get('pk')})


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('index')
# class ProjectUpdate(FormView):
#     form_class = ProjectForm
#     template_name = 'project/project_update_view.html'
#
#     def dispatch(self, request, *args, **kwargs):
#         self.project = self.get_object()
#         return super().dispatch(request, *args, **kwargs)
#
#     def get_initial(self):
#         return super().get_initial()
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['instance'] = self.project
#         return kwargs
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['project'] = self.project
#         return context
#
#     def get_object(self):
#         project = get_object_or_404(
#             Project, id=self.kwargs.get('pk')
#             )
#         return project
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('project', kwargs={'pk': self.kwargs.get('pk')})
#
# class DeleteProject(TemplateView):
#     template_name = 'project/index.html'
#
#     def get_context_data(self, **kwargs):
#         project = get_object_or_404(Project, id=kwargs.get('pk'))
#         project.delete()
#         kwargs['projects'] = Project.objects.all()
#         return super().get_context_data(**kwargs)
#
