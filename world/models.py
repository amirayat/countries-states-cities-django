from django.db import models
from django.utils.translation import gettext as _


class Country(models.Model):
    """
    class model for countries
    """
    name = models.CharField(max_length=36)
    iso3 = models.CharField(max_length=3)
    iso2 = models.CharField(max_length=2)
    numeric_code = models.CharField(max_length=3)
    phone_code = models.CharField(max_length=16)
    capital = models.CharField(max_length=20, null=True)
    currency = models.CharField(max_length=3)
    currency_name = models.CharField(max_length=39)
    currency_symbol = models.CharField(max_length=6)
    tld = models.CharField(max_length=3)
    native = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=8, null=True)
    subregion = models.CharField(max_length=25, null=True)
    timezones = models.JSONField(default=list)
    translations = models.JSONField()
    latitude = models.CharField(max_length=12)
    longitude = models.CharField(max_length=13)
    emoji = models.CharField(max_length=2)
    emojiU = models.CharField(max_length=15)

    class Meta:
        db_table = 'countries'


class State(models.Model):
    """
    class model for states
    """
    country = models.ForeignKey(
        Country, related_name=_('country_state'), on_delete=models.CASCADE)
    name = models.CharField(max_length=56)
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=32)
    state_code = models.CharField(max_length=5)
    type = models.CharField(max_length=45, null=True)
    latitude = models.CharField(max_length=12, null=True)
    longitude = models.CharField(max_length=13, null=True)

    class Meta:
        db_table = 'states'


class City(models.Model):
    """
    class model for cities
    """
    state = models.ForeignKey(
        State, related_name=_('state_city'), on_delete=models.CASCADE)
    country = models.ForeignKey(
        Country, related_name=_('country_city'), on_delete=models.CASCADE)
    name = models.CharField(max_length=59)
    state_code = models.CharField(max_length=5)
    state_name = models.CharField(max_length=56)
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=32)
    latitude = models.CharField(max_length=12)
    longitude = models.CharField(max_length=13)
    wikiDataId = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = 'cities'
