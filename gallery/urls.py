from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
    path('',views.index,name='galleryHome'),
    path('search/',views.get_category,name='category'),
    path('location/<str:search_location>/',views.get_location,name='location'),
    #  url(r'^location/(?P<image_location>\d+)', views.location_filter, name='location_filter'),
    
]