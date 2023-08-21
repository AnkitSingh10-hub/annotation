from rest_framework import serializers
from .models import PlantImage, Annotation  # Import your models

class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = '__all__'  # You can specify the fields you want to include here

class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = '__all__'  # You can specify the fields you want to include here
