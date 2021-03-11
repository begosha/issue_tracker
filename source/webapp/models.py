from django.db import models

status_choices = [('new', 'New'), ('in_progress', 'In progress'),  ('done', 'Done')]
type_choices = [('t', 'Task'), ('b', 'Bug'),  ('e', 'Enhancement')]

class Status(models.Model):
    status = models.CharField(max_length=11, choices=status_choices, verbose_name='Status')

    def __str__(self):
        return "{}".format(self.status)


class Type(models.Model):
    task_type = models.CharField(max_length=11, choices=type_choices, verbose_name='Type')

    def __str__(self):
        return "{}".format(self.task_type)

class Task(models.Model):

    summary = models.CharField(max_length=300, null=False, blank=False, verbose_name='Title')
    description = models.TextField(max_length=3000, verbose_name='Description')
    status = models.ForeignKey('webapp.Status', related_name='status', on_delete=models.PROTECT, verbose_name='Status')
    task_type = models.ForeignKey('webapp.Type', related_name='type', on_delete=models.PROTECT, verbose_name='Type') 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')


    def __str__(self):

        return "{}. {}".format(self.pk, self.summary)


