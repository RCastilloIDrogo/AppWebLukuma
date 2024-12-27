from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from menu.views import MenuAPIView

def home(request):
    return HttpResponse("Bienvenido a la API del restaurante. Visita /api/menu/ para ver el menú.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/menu/', MenuAPIView.as_view(), name='menu'),
    path('', home),  # Ruta para la raíz
]
