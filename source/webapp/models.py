from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth import get_user_model

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Project(models.Model):
    start_date = models.DateField(auto_now_add=False, null=False, blank=False, verbose_name='Start Date')
    end_date = models.DateField(null=True, verbose_name='End Date')
    project_name = models.CharField(max_length=15, null=False, blank=False, verbose_name='Title', validators=(MaxLengthValidator(15),))
    project_description = models.TextField(max_length=3000, verbose_name='Description', validators=(MinLengthValidator(10),))
    users = models.ManyToManyField(get_user_model(), related_name='projects')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='project'
    )
    
    class Meta:
        db_table = 'projects'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        permissions = [
            
        ('user_list_change', 'Can change the list of users of the project')

    ]

    def __str__(self):
        return self.project_name

class Task(BaseModel):
    delete_choices = [('0', 'True'), ('1', 'Active')]
    project = models.ForeignKey(
        'webapp.Project',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Task',
        null=False,
        blank=False
    )
    summary = models.CharField(max_length=15, null=False, blank=False, verbose_name='Title', validators=(MaxLengthValidator(15),))
    description = models.TextField(max_length=3000, verbose_name='Description', validators=(MinLengthValidator(10),))
    status = models.ForeignKey('webapp.Status', related_name='task_statuses', on_delete=models.PROTECT, verbose_name='Status', null=False,blank=False) 
    task_type = models.ManyToManyField('webapp.Type', related_name='types', verbose_name='Type') 
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='tasks'
    )
    
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


