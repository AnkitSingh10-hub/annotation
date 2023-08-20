from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PlantImage, Annotation
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class ImageListView(ListView):
    model = PlantImage
    template_name = 'plantrecognitionapp/image_list.html'

class ImageDetailView(DetailView):
    model = PlantImage
    template_name = 'plantrecognitionapp/image_detail.html'

@csrf_exempt
def save_annotation(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        x = request.POST.get('x')
        y = request.POST.get('y')
        width = request.POST.get('width')
        height = request.POST.get('height')
        color = request.POST.get('color')

        annotation = Annotation(
            id=image_id,
            x=x,
            y=y,
            width=width,
            height=height,
            color=color
        )
        annotation.save()

        return JsonResponse({'message': 'Annotation saved successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
