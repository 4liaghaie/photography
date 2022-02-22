from django.db import models


class Landing(models.Model):
    alt = models.CharField(max_length=100)
    image = models.ImageField(upload_to="",  default=None, blank=True, null=True)


class Landing1(models.Model):
    alt = models.CharField(max_length=100)
    image = models.ImageField(upload_to="",  default=None, blank=True, null=True)


class Landing2(models.Model):
    alt = models.CharField(max_length=100)
    image = models.ImageField(upload_to="",  default=None, blank=True, null=True)


class Fashion(models.Model):
    alt = models.CharField(max_length=100)
    image = models.ImageField(upload_to="",  default=None, blank=True, null=True)


class Nature(models.Model):
    alt = models.CharField(max_length=100)
    image = models.ImageField(upload_to="",  default=None, blank=True, null=True)