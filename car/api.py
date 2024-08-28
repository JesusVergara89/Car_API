from .models import Cars
from rest_framework import viewsets, permissions
from .serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:  # GET requests
            permission_classes = [permissions.AllowAny]
        else:  # POST, PUT, DELETE requests
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    serializer_class = CarSerializer
    