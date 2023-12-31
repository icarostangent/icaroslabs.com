# Generated by Django 3.2.20 on 2023-08-24 20:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20230824_0431'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agent',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='agent',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='domain',
            name='agent',
            field=models.OneToOneField(blank=True, default=2, on_delete=django.db.models.deletion.PROTECT, related_name='agent', to='api.agent'),
            preserve_default=False,
        ),
    ]
