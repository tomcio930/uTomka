# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from media.models import Image

def index(request):
    images = Image.objects.all()
    return render(request, 'media/index.html', {'images': images})