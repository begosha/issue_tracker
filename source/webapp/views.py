from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, Status, Type
from django.urls import reverse
from django.views.generic import View, TemplateView, RedirectView


class IndexView(TemplateView):
   template_name = 'index.html'
   
   def get_context_data(self, **kwargs):
       kwargs['tasks'] = Task.objects.all()
       return super().get_context_data(**kwargs)

