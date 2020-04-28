from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home(request):
    return render(request, 'hub/hub.html')

def html(request):
    return render(request, 'hub/index.html')
