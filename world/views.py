from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound
from rest_framework.pagination import LimitOffsetPagination
from rest_flex_fields import is_expanded
from world.models import Country, State, City
from world.serializers import CityFlexSerializer, CountryModelSerializer, StateFlexSerializer, StateModelSerializer, CityModelSerializer


class CountryListViewSet(ReadOnlyModelViewSet):
    """
    list of countries
    """
    permission_classes = (AllowAny,)
    serializer_class = CountryModelSerializer
    queryset = Country.objects.all()


class StateListViewSet(ReadOnlyModelViewSet):
    """
    list of states for a country
    """
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


class StateFlexViewSet(ModelViewSet):
    """
    list of states and their country
    example query parameters
    ?limit=10&offset=10&expand=country&fields=id,name,country
    """
    pagination_class = LimitOffsetPagination
    permission_classes = (AllowAny,)
    serializer_class = StateFlexSerializer
    queryset = State.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if is_expanded(self.request, 'country'):
            queryset = queryset.select_related('country')
        return queryset


class CityFlexViewSet(ModelViewSet):
    """
    list of city and their country and state
    example query parameters
    ?limit=10&offset=10&expand=country,state&fields=id,name,country,state
    """
    pagination_class = LimitOffsetPagination
    permission_classes = (AllowAny,)
    serializer_class = CityFlexSerializer
    queryset = City.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if is_expanded(self.request, 'country'):
            queryset = queryset.select_related('country')
        if is_expanded(self.request, 'state'):
            queryset = queryset.select_related('state')
        return queryset

