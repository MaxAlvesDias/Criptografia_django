from django.urls import path
from core import views

from django.conf.urls.static import static
from django.conf  import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('descriptografar/', views.descriptografar, name='descriptografar'),
    path('criptografar/', views.criptografar, name='criptografar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
