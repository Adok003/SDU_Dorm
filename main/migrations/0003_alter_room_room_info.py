# Generated by Django 4.0.3 on 2022-03-24 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_room_room_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_info',
            field=models.CharField(max_length=100, verbose_name='Room info'),
        ),
    ]
