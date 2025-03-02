from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from productos.views import CategoriaViewSet, ProductoViewSet
from pedidos.views import PedidoViewSet
from mesas.views import MesaViewSet
from usuarios.views import UsuarioViewSet

# Mensaje de bienvenida en la raíz de la API
def home(request):
    return HttpResponse("Bienvenido a la API del restaurante. Visita /api/ para ver los endpoints disponibles.")

# Configuración del enrutador para ViewSets
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'mesas', MesaViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Incluye todas las rutas registradas en el router
    path('', home),  # Página de bienvenida en la raíz
]
