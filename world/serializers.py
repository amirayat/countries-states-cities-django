from rest_framework.serializers import ModelSerializer
from rest_flex_fields import FlexFieldsModelSerializer
from drf_writable_nested import WritableNestedModelSerializer
from world.models import Country, State, City


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


class StateFlexSerializer(FlexFieldsModelSerializer):
    """
    flex serializer for states
    """

    class Meta:
        model = State
        fields = '__all__'
        expandable_fields = {
            'country': CountryModelSerializer
        }


class CityFlexSerializer(FlexFieldsModelSerializer):
    """
    flex serializer for cities
    """

    class Meta:
        model = City
        fields = '__all__'
        expandable_fields = {
            'state': StateModelSerializer,
            'country': CountryModelSerializer
        }


class StateNestedModelSerializer(WritableNestedModelSerializer):
    """
    nested serializer for states and their cities
    """
    state_city = CityModelSerializer(many=True)

    class Meta:
        model = State
        fields = [
            'name',
            'country_code',
            'country_name',
            'state_code',
            'type',
            'latitude',
            'longitude',
            'state_city'
        ]


class CountryNestedModelSerializer(WritableNestedModelSerializer):
    """
    nested serializer for countries and their states
    """
    country_state = StateNestedModelSerializer(many=True)

    class Meta:
        model = Country
        fields = [
            'name',
            'iso3',
            'iso2',
            'numeric_code',
            'phone_code',
            'capital',
            'currency',
            'currency_name',
            'currency_symbol',
            'tld',
            'native',
            'region',
            'subregion',
            'timezones',
            'translations',
            'latitude',
            'longitude',
            'emoji',
            'emojiU',
            'country_state'
        ]
