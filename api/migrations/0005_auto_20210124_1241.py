# Generated by Django 3.1.4 on 2021-01-24 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='author',
            new_name='username',
        ),
    ]