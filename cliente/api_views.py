from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from cliente.models import Cliente
from cliente.serializers import ClienteSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def agregar_cliente(request):
    if request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)