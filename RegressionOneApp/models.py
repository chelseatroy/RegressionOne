from __future__ import unicode_literals

from django.db import models

class Thingamabob(models.Model):
    description = models.CharField(max_length=30)
    done = models.BooleanField()
    updated = models.DateTimeField(auto_now_add=True)
