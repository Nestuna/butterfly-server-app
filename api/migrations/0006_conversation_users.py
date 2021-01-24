# Generated by Django 3.1.4 on 2021-01-24 15:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_auto_20210120_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='users',
            field=models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
