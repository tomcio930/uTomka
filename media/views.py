# Create your views here.
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from media.models import Image
from uTomka.settings import IMAGES_PER_PAGE, ADDRESS
from django.core.paginator import Paginator, EmptyPage


def index(request, page="1"):
    page = int(page)
    
    images = Image.objects.all()
    paginator = Paginator(images, IMAGES_PER_PAGE)
    try:
        images_to_show = paginator.page(page)
    except EmptyPage:
        images_to_show = paginator.page(paginator.num_pages)
        page = paginator.num_pages
    previous_pages_count = 4
    next_pages_count = 5
    
    first_page = page - previous_pages_count
    last_page = page + next_pages_count
    
    
    if(first_page < 1):
        last_page -= first_page
        first_page = 1
    if(last_page > paginator.num_pages):
        last_page = paginator.num_pages
    
    return render(request, 'media/index.html', {'images': images_to_show, 'pages_list': range(first_page, last_page+1), 'current_page':page, 'adress':ADDRESS})

def image(request, image_id):
    images = Image.objects.filter(id=image_id)
    
    if(images):
        return render(request, 'media/image.html', {'images':images, 'adress':ADDRESS})
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    
def go_to_page(request):
    page = request.GET['page']
    return redirect('/'+page)


