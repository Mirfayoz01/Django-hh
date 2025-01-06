from django.db import models


class Data(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    location = models.CharField(max_length=100)
    full_time = models.CharField(max_length=100)

