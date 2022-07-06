# Generated by Django 3.2.9 on 2022-03-03 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
            ],
        ),
        migrations.CreateModel(
            name='RescueServices',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('is_approved', models.BooleanField(default=False)),
                ('service_information', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('is_approved', models.BooleanField(default=False)),
                ('service_information', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('is_approved', models.BooleanField(default=False)),
                ('experience', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_rescue_service',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_serviceprovider',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_vet',
            field=models.BooleanField(default=False),
        ),
    ]