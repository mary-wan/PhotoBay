from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='galleryHome'),
    path('search/',views.get_category,name='category')
    
]