# Generated by Django 3.0.7 on 2020-06-23 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseballcardapp', '0008_auto_20200622_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='notes',
            field=models.CharField(max_length=50, null=True),
        ),
    ]