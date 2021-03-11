from django.contrib import admin
from django.apps import apps
from webapp.models import Status, Task, Type

class StatusAdmin(admin.ModelAdmin):
    list_display = ['status']
    list_filter = ['status']
    search_fields = ['status']
    fields = ['status']

class TypeAdmin(admin.ModelAdmin):
    list_display = ['task_type']
    list_filter = ['task_type']
    search_fields = ['task_type']
    fields = ['task_type']

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description','status', 'task_type','created_at', 'updated_at']
    list_filter = ['summary']
    search_fields = ['status', 'task_type']
    fields = ['id', 'summary', 'description', 'status', 'task_type', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at', 'id']


admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Task, TaskAdmin)