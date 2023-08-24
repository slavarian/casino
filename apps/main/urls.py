
''' MAIN URLS'''


from django.contrib import admin
from django.urls import path
from django.conf import settings
from main.views import main_page 
from . import views
from django.conf.urls.static import static 



urlpatterns = [
    path('', main_page),
    path('image/<int:image_id>/', main_page, name='image-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
