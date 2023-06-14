# Generated by Django 4.2.2 on 2023-06-14 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=100, verbose_name='名前')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='メールアドレス')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='住所')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='誕生日')),
                ('hire_date', models.DateField(blank=True, null=True, verbose_name='入社日')),
                ('at_desk', models.BooleanField(default=False, verbose_name='出社状態')),
            ],
        ),
    ]
