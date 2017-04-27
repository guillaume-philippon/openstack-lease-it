# pylint: skip-file
from django.db import models

# Create your models here.


class Instances(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField()