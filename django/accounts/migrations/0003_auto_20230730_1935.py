# Generated by Django 3.2.20 on 2023-07-30 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20230730_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaddress',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='emailaddress',
            name='verify_key',
            field=models.CharField(default='VXHLwFm7qA9BHhpuGWkYKviQk05bcUkg', max_length=255),
        ),
    ]
