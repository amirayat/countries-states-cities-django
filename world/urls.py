from django.urls import path, include
from rest_framework_nested import routers
from world.views import CountryListViewSet, StateListViewSet, CityListViewSet


country_router = routers.SimpleRouter()
country_router.register(r'country', CountryListViewSet)

state_router = routers.NestedSimpleRouter(country_router, r'country', lookup='country')
state_router.register(r'state', StateListViewSet)

city_router = routers.NestedSimpleRouter(state_router, r'state', lookup='state')
city_router.register(r'city', CityListViewSet)


urlpatterns = [ 
    path('', include(country_router.urls)),
    path('', include(state_router.urls)),
    path('', include(city_router.urls)),
]