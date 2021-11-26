from django.shortcuts import render,redirect
from .models import Image,Location,Category

def index(request):
    images=Image.objects.all()
    locations = Location.all_locations()
    
    return render(request,'all-gallery/home.html')

