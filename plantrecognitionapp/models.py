from django.db import models

class PlantImage(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    description = models.TextField()

class Annotation(models.Model):
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)