from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear_libro, name='crear'),
    path('libros/editar/<int:id_libro>',views.editar_libro,name='editar'),
    path('eliminar/<int:id_libro>', views.eliminar_libro, name='eliminar'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)