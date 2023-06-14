# Generated by Django 4.2.2 on 2023-06-14 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0003_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp2.department', verbose_name='所属部署'),
        ),
    ]