from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, MaxLengthValidator

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Task(BaseModel):

    summary = models.CharField(max_length=300, null=False, blank=False, verbose_name='Title', validators=(MinLengthValidator(5), MaxLengthValidator(1000),))
    description = models.TextField(max_length=3000, verbose_name='Description', validators=(MinLengthValidator(5), MaxLengthValidator(1000),))
    status = models.ForeignKey('webapp.Status', related_name='task_statuses', on_delete=models.PROTECT, verbose_name='Status', null=False,blank=False) 
    task_type = models.ManyToManyField('webapp.Type', related_name='types', verbose_name='Type') 
    
    class Meta:
        db_table = 'tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):

        return "{}. {}".format(self.pk, self.summary)


class Status(BaseModel):
    status = models.CharField(max_length=11, null=False, blank=False,verbose_name='Status')
    
    class Meta:
        db_table = 'statuses'
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
    def __str__(self):
        return "{}".format(self.status)


class Type(BaseModel):
    task_type = models.CharField(max_length=11, null=False, blank=False, verbose_name='Type')
    
    class Meta:
        db_table = 'types'
        verbose_name = 'Type'
        verbose_name_plural = 'Types'
    def __str__(self):
        return "{}".format(self.task_type)

