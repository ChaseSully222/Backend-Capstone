# Generated by Django 3.0.7 on 2020-06-19 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseballcardapp', '0005_auto_20200619_0238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='playerId',
            new_name='playerId_id',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='setId',
            new_name='setId_id',
        ),
    ]
