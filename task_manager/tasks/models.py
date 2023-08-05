from django.db import models
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.contrib.auth.models import User


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status,
                               on_delete=models.SET_DEFAULT,
                               default=None)
    author = models.ForeignKey(User,
                               on_delete=models.PROTECT,
                               related_name="author")
    executor = models.ForeignKey(User,
                                 on_delete=models.SET_DEFAULT,
                                 default=None,
                                 related_name="executor",
                                 null=True,
                                 blank=True)
    labels = models.ManyToManyField(Label,
                                    related_name="labels",
                                    blank=True)
