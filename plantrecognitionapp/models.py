from django.db import models


class PlantImage(models.Model):
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=100)
    description = models.TextField()


class Annotation(models.Model):
    plant_images = models.ForeignKey(PlantImage, on_delete=models.CASCADE, null=True)
    json_data = models.JSONField(null=True)
