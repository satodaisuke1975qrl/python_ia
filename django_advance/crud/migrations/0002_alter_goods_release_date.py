# Generated by Django 4.2.2 on 2023-06-20 07:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='発売日'),
        ),
    ]
