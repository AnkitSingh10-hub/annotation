from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PlantImage, Annotation
from django.http import JsonResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response


class ImageListView(ListView):
    model = PlantImage
    template_name = "plantrecognitionapp/image_list.html"


class ImageDetailView(DetailView):
    model = PlantImage
    template_name = "plantrecognitionapp/image_detail.html"


"""
@csrf_exempt
def save_annotation(request):
    if request.method == "POST":
        try:
            # Retrieve the JSON data from the request's body
            # data = json.loads(request.body)
            annotation_json = request.data.get("annotation")
            print(annotation_json)
            # print(data)
            # Process and save the data to your models or database
            # Example: Saving data to a Django model

            # annotation = Annotation(json_data=data["annotation"])
            # annotation.plant_images = data["image_id"]
            # annotation.save()

            # Return a JSON response indicating success
            return JsonResponse({"message": "Data saved successfully"})
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"message": "An error occurred"}, status=500)
    else:
        return JsonResponse({"message": "Invalid request method"}, status=405)
"""


class AnnotationView(APIView):
    def post(self, request):

        annotation_data = request.data.get("annotation_data")
        image_id = request.data.get("image_id")
        image = PlantImage.objects.filter(id=image_id).first()

        b = Annotation.objects.create(plant_images=image, json_data=annotation_data)
        b.save()

        return Response("server side verified")

    def get(self, request):
        return Response("hello")
