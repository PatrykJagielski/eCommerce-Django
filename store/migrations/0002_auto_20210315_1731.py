# Generated by Django 3.1.7 on 2021-03-15 17:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Protuct',
            new_name='Product',
        ),
    ]