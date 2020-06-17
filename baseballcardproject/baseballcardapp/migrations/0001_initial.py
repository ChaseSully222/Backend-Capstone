# Generated by Django 3.0.7 on 2020-06-17 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('imagePath', models.CharField(max_length=50)),
                ('cardNumber', models.CharField(max_length=50)),
                ('attribute', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('notes', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Set',
                'verbose_name_plural': 'Sets',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phoneNumber', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('createdAt', models.DateTimeField()),
                ('lastLogin', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=50)),
                ('cardId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='baseballcardapp.Card')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='baseballcardapp.User')),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
            },
        ),
        migrations.AddField(
            model_name='card',
            name='playerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='baseballcardapp.Player'),
        ),
        migrations.AddField(
            model_name='card',
            name='setId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='baseballcardapp.Set'),
        ),
    ]