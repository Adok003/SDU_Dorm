# Generated by Django 4.0.3 on 2022-03-24 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_entry_first_name_remove_entry_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
