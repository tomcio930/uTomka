# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from media.models import Image

def index(request, page="1"):
    page = int(page)
    images_count = Image.objects.all().__len__()
    
    images_per_page = 1
    start = (page-1)*images_per_page
    end = page*images_per_page
    
    #if(images_count < start or page < 1):
    #    return HttpResponseNotFound('<h1>Page not found</h1>')
    
    images = Image.objects.all()[start:end]
    
    previous_pages_count = 4
    next_pages_count = 5
    
    first_page = page - previous_pages_count
    last_page = page + next_pages_count
    
    
    if(first_page < 1):
        last_page -= first_page
        first_page = 1
        
    return render(request, 'media/index.html', {'images': images, 'pages_list': range(first_page, last_page+1), 'current_page':page})