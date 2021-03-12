from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from webapp.views import (IndexView, TaskView, TaskAddView, UpdateView, DeleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', TaskView.as_view(), name='task'),
    path('add/', TaskAddView.as_view(), name='task_add'),
    path('<int:pk>/update', UpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete', DeleteView.as_view(), name='task-delete')
]
