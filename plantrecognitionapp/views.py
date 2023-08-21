from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PlantImage, Annotation
from django.http import JsonResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .serializers import *


class ImageListView(ListView):
    model = PlantImage
    template_name = "plantrecognitionapp/image_list.html"


class ImageDetailView(DetailView):
    model = PlantImage
    template_name = "plantrecognitionapp/image_detail.html"


class AnnotationView(APIView):
    def post(self, request):
        print(request.data, "\n")
        serializer = AnnotationSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            print(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
      
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response("hello")
