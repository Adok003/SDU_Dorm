# Generated by Django 4.0.3 on 2022-03-11 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_room_course_room_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='course',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], max_length=50, verbose_name='Course'),
        ),
    ]
