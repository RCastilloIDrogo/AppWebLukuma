from rest_framework import serializers
from .models import Pedido, PedidoDetalle

class PedidoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoDetalle
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    productos = PedidoDetalleSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = '__all__'
