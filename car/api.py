from .models import Cars
from rest_framework import viewsets, permissions
from .serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CarSerializer
    