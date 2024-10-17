from django.urls import path
from . import views

urlpatterns = [
    path('', views.drink, name='index'),
    path('index/<int:id>/', views.drinklist, name='index'),
    path('upload/', views.upload_file, name='upload_file'),
    path('files/',views.list_files, name='get_file'),


]