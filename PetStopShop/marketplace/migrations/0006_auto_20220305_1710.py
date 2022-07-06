# Generated by Django 3.2.9 on 2022-03-05 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marketplace', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='final_total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=1000, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='sub_total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=1000, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tax_total',
            field=models.DecimalField(blank=True, decimal_places=2, default=120.0, max_digits=1000, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]