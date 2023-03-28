from rest_framework.serializers import ModelSerializer
from world.models import Country,State,City


class CityModelSerializer(ModelSerializer):
    """
    serializer for cities
    """

    class Meta:
        model = City
        fields = '__all__'


class StateModelSerializer(ModelSerializer):
    """
    serializer for states
    """

    class Meta:
        model = State
        fields = '__all__'
    

class CountryModelSerializer(ModelSerializer):
    """
    serializer for countries
    """

    class Meta:
        model = Country
        fields = '__all__'

        

