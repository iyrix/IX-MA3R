from dynamorm import DynaModel
from marshmallow import fields, EXCLUDE
from django.conf import settings
from django.db import models

class Task(models.Model):
    task_id = models.UUIDField(primary_key=True, max_length=255)
    task_name = models.CharField(max_length=255)
    next_task_id = models.CharField(null=True, max_length=255)
    previous_task_id = models.CharField(null=True, max_length=255)
