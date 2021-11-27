from django.shortcuts import render,redirect
from .models import Image,Location,Category

def index(request):
    images=Image.objects.all()
    locations = Location.all_locations()
    
    return render(request,'all-gallery/home.html',{'images': images, 'locations': locations})

def get_category(request):   
    title = "Category"
    locations = Location.objects.all()
    
    if 'category' in request.GET and request.GET["category"]:
        search_category=request.GET.get("category")
        searched_category = Image.search_image(search_category)
        message = f"{search_category}"
        
        return render(request,'all-gallery/search.html',{'message':message,'images':searched_category,'title':title,'locations':locations})
    else:
        message = "You haven't searched for any category"
        return render(request, 'all-gallery/search.html',{"message":message})
    
def get_location(request,search_location):
    title = "Location"
    locations = Location.objects.all()
    images = Image.filter_by_location(search_location)
    return render(request, 'all-gallery/location.html',{"images":images,'locations':locations,'title':title})

    
        
    