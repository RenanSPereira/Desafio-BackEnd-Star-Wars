from rest_framework import routers, serializers, viewsets
from .models import Planet
from .swapi_service import get_films_qty

class PlanetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Planet
        fields = [
            'pk',
            'name', 
            'climate', 
            'terrain',
            'films_qty',
            'created',
            'edited',
        ]
      
        extra_kwargs = {
            'films_qty': {'read_only': True}
        }
            
 
    def create(self, validated_data):
        planet = Planet.objects.create(
            name=validated_data['name'],
            climate=validated_data['climate'],
            terrain=validated_data['terrain']
        )
        planet.films_qty = get_films_qty(name=validated_data['name'])
        planet.save()
        return planet
    
    def update(self,instance, validated_data):
        instance.name=validated_data.get('name')
        instance.climate=validated_data.get('climate')
        instance.terrain=validated_data.get('terrain')
        instance.films_qty = get_films_qty(name=validated_data['name'])
        instance.save()
        return instance