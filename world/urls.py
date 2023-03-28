from django.urls import path, include
from rest_framework_nested import routers
from world.views import CityFlexViewSet, CountryListViewSet, CountryWritableViewSet, StateListViewSet, CityListViewSet, StateFlexViewSet


# nested routers
country_router = routers.SimpleRouter()
country_router.register(r'country', CountryListViewSet)

state_nested_router = routers.NestedSimpleRouter(country_router, r'country', lookup='country')
state_nested_router.register(r'state', StateListViewSet)

city_nested_router = routers.NestedSimpleRouter(state_nested_router, r'state', lookup='state')
city_nested_router.register(r'city', CityListViewSet)

# expandable routers
state_flex_router = routers.SimpleRouter()
state_flex_router.register(r'state', StateFlexViewSet)

city_flex_router = routers.SimpleRouter()
city_flex_router.register(r'city', CityFlexViewSet)

# writable nested router
country_nested_router = routers.SimpleRouter()
country_nested_router.register(r'country', CountryWritableViewSet)


urlpatterns = [ 
    # nested routes
    path('nested/', include(country_router.urls)),
    path('nested/', include(state_nested_router.urls)),
    path('nested/', include(city_nested_router.urls)),

    # expandable routes
    path('expandable/', include(state_flex_router.urls)),
    path('expandable/', include(city_flex_router.urls)),

    # writable nested routes
    path('writable/', include(country_nested_router.urls)),
]