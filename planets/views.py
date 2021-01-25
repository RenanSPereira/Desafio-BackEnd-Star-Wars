from rest_framework import routers, serializers, viewsets
from .models import Planet
from .serializer import PlanetSerializer

class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer