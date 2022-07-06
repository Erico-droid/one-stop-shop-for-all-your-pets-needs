# Generated by Django 3.2.9 on 2022-03-05 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220303_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=120)),
                ('address2', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('state', models.CharField(blank=True, max_length=120, null=True)),
                ('country', models.CharField(blank=True, max_length=120, null=True)),
                ('zipcode', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=25)),
                ('shipping', models.BooleanField(default=True)),
                ('billing', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
