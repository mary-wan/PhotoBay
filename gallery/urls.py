from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.index,name='galleryHome'),
    path('search/',views.get_category,name='category'),
    path('location/<str:search_location>/',views.get_location,name='location'),
    path('image/<int:image_id>/',views.get_image,name='singleImage'),
    # path('error/',views.error_404,name='error'),   
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# handler404 = "gallery.views.page_not_found_view"