# Generated by Django 4.1.7 on 2023-03-28 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36)),
                ('iso3', models.CharField(max_length=3)),
                ('iso2', models.CharField(max_length=2)),
                ('numeric_code', models.CharField(max_length=3)),
                ('phone_code', models.CharField(max_length=16)),
                ('capital', models.CharField(max_length=20, null=True)),
                ('currency', models.CharField(max_length=3)),
                ('currency_name', models.CharField(max_length=39)),
                ('currency_symbol', models.CharField(max_length=6)),
                ('tld', models.CharField(max_length=3)),
                ('native', models.CharField(max_length=50, null=True)),
                ('region', models.CharField(max_length=8, null=True)),
                ('subregion', models.CharField(max_length=25, null=True)),
                ('timezones', models.JSONField(default=list)),
                ('translations', models.JSONField()),
                ('latitude', models.CharField(max_length=12)),
                ('longitude', models.CharField(max_length=13)),
                ('emoji', models.CharField(max_length=2)),
                ('emojiU', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('country_code', models.CharField(max_length=2)),
                ('country_name', models.CharField(max_length=32)),
                ('state_code', models.CharField(max_length=5)),
                ('type', models.CharField(max_length=45, null=True)),
                ('latitude', models.CharField(max_length=12, null=True)),
                ('longitude', models.CharField(max_length=13, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_state', to='world.country')),
            ],
            options={
                'db_table': 'states',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=59)),
                ('state_code', models.CharField(max_length=5)),
                ('state_name', models.CharField(max_length=56)),
                ('country_code', models.CharField(max_length=2)),
                ('country_name', models.CharField(max_length=32)),
                ('latitude', models.CharField(max_length=12)),
                ('longitude', models.CharField(max_length=13)),
                ('wikiDataId', models.CharField(max_length=10, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_city', to='world.country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_city', to='world.state')),
            ],
            options={
                'db_table': 'cities',
            },
        ),
    ]
