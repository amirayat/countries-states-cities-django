from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound
from world.serializers import CountryModelSerializer, StateModelSerializer, CityModelSerializer
from world.models import Country, State, City


class CountryListViewSet(ReadOnlyModelViewSet):
    """
    list of countries
    """
    pagination_class = None
    permission_classes = (AllowAny,)
    serializer_class = CountryModelSerializer
    queryset = Country.objects.all()


class StateListViewSet(ReadOnlyModelViewSet):
    """
    list of states for a country
    """
    pagination_class = None
    permission_classes = (AllowAny,)
    serializer_class = StateModelSerializer
    queryset = State.objects.all()

    def list(self, request, country_pk=None):
        queryset = self.filter_queryset(
            self.get_queryset().filter(country_id=country_pk))

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, country_pk=None):
        try:
            instance = self.get_queryset().filter(country_id=country_pk).get(pk=pk)
        except:
            raise NotFound
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CityListViewSet(ReadOnlyModelViewSet):
    """
    list of cities for a state
    """
    pagination_class = None
    permission_classes = (AllowAny,)
    serializer_class = CityModelSerializer
    queryset = City.objects.all()

    def list(self, request, country_pk=None, state_pk=None):
        queryset = self.filter_queryset(self.get_queryset().filter(
            country_id=country_pk, state_id=state_pk))

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, country_pk=None, state_pk=None):
        try:
            instance = self.get_queryset().filter(
                country_id=country_pk, state_id=state_pk).get(pk=pk)
        except:
            raise NotFound
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
