# Generated by Django 4.0.3 on 2022-03-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_room_room_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='floor',
            options={'ordering': ('floor_number',)},
        ),
        migrations.AlterField(
            model_name='floor',
            name='floor_number',
            field=models.IntegerField(verbose_name='Floor number'),
        ),
    ]
