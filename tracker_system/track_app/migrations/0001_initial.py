# Generated by Django 4.1.5 on 2023-01-24 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('employees', models.ManyToManyField(related_name='companies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('serial_number', models.CharField(max_length=255, unique=True)),
                ('model', models.CharField(max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(default='available', max_length=255)),
                ('checked_out', models.BooleanField(default=False)),
                ('condition_at_checkout', models.CharField(blank=True, max_length=255)),
                ('condition_at_return', models.CharField(blank=True, max_length=255)),
                ('assigned_employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='track_app.company')),
            ],
        ),
    ]
