from rest_framework import viewsets
from .models import Mesa
from .serializers import MesaSerializer

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
