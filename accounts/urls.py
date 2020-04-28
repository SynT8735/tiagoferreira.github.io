from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('blender', views.blender),
    path('unity', views.unity),
    path('godot', views.godot),
    path('graphic_design', views.graphic_design),
    path('sound_design', views.sound_design),
    path('photography', views.photography),
]