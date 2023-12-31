# Generated by Django 3.2.20 on 2023-08-24 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_alter_agent_api_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='agents', to='auth.user'),
            preserve_default=False,
        ),
    ]
