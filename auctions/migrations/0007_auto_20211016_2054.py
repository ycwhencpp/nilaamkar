# Generated by Django 3.2.7 on 2021-10-16 15:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20211014_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listing',
            name='is_watched',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='watchlist',
        ),
    ]