from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (TaskView, UpdateView, DeleteView, IndexView, ProjectView, TaskCreate, ProjectCreate, DeleteProject)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', ProjectView.as_view(), name='project'),
    path('<int:pk>/task', TaskView.as_view(), name='task'),
    path('add/', ProjectCreate.as_view(), name='project-add'),
    # path('<int:pk>/update', UpdateView.as_view(), name='project-update'),
    path('<int:pk>/add/', TaskCreate.as_view(), name='task_add'),
    path('<int:pk>/update', UpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete', DeleteView.as_view(), name='task-delete'),
    path('<int:pk>/delete/project', DeleteProject.as_view(), name='project-delete'),

]