from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (TaskView,
                    TaskUpdateView,
                    TaskDeleteView,
                    IndexView,
                    ProjectView,
                    TaskCreate,
                    ProjectCreate,
                    ProjectDeleteView,
                    ProjectUpdateView,
                    UsersAddView,
                    UsersDeleteView
                    )

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', ProjectView.as_view(), name='project'),
    path('<int:pk>/task', TaskView.as_view(), name='task'),
    path('add/project', ProjectCreate.as_view(), name='project-add'),
    path('<int:pk>/update/project', ProjectUpdateView.as_view(), name='project-update'),
    path('<int:pk>/add/', TaskCreate.as_view(), name='task_add'),
    path('<int:pk>/update', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    path('<int:pk>/delete/project', ProjectDeleteView.as_view(), name='project-delete'),
    path('<int:pk>/add/users', UsersAddView.as_view(), name='users-add'),
    path('<int:pk>/delete/users', UsersDeleteView.as_view(), name='users-delete'),
]