# Generated by Django 4.0.3 on 2022-03-11 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_user_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='E-mail'),
        ),
    ]