from rest_framework import routers, serializers, viewsets
from .models import Planet

class PlanetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Planet
        fields = [
            'name', 
            'climate', 
            'terrain',
        ]