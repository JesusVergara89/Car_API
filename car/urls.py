from rest_framework import routers
from .api import CarViewSet

router = routers.DefaultRouter()

router.register('api/cars',CarViewSet, 'cars' )

urlpatterns = router.urls