from django.urls import path
from . import views

app_name = 'plantrecognitionapp'

urlpatterns = [
    path('', views.ImageListView.as_view(), name='image_list'),
    path('<int:pk>/', views.ImageDetailView.as_view(), name='image_detail'),
    path('save_annotation/', views.save_annotation, name='save_annotation'),

]
