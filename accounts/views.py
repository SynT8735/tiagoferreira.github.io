from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'accounts/index.html')

def blender(request):
    return render(request, 'accounts/blender.html')

def unity(request):
    return render(request, 'accounts/unity.html')

def godot(request):
    return render(request, 'accounts/godot.html')

def graphic_design(request):
    return render(request, 'accounts/graphic_design.html')

def sound_design(request):
    return render(request, 'accounts/sound_design.html')

def photography(request):
    return render(request, 'accounts/photography.html')
