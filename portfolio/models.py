from django.db import models


class Landing(models.Model):
    alt = models.CharField(max_length=100)
    image = models.ImageField(upload_to="",  default=None, blank=True, null=True)


class Fashion(models.Model):
    alt = models.CharField(max_length=100)
    image = models.ImageField(upload_to="",  default=None, blank=True, null=True)

