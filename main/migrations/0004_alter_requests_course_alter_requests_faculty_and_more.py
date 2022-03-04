# Generated by Django 4.0.2 on 2022-03-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_requests_delete_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='course',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], max_length=50, verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='faculty',
            field=models.CharField(choices=[('Faculty of Law and Social Sciences', 'Faculty of Law and Social Sciences'), ('Faculty of Education and Humanities Sciences', 'Faculty of Education and Humanities Sciences'), ('Faculty of Engineering and Natural Sciences', 'Faculty of Engineering and Natural Sciences'), ('Business school', 'Business school')], max_length=50, verbose_name='Faculty'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=10, verbose_name='Gender'),
        ),
    ]
