from django.db import models


class Status(models.Model):

    status_name = models.CharField('name', max_length=100)
    date_of_creation = models.DateTimeField('date_creation', auto_now_add=True)
