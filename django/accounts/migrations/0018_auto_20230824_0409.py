# Generated by Django 3.2.20 on 2023-08-24 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20230824_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaddress',
            name='verify_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='client_reference_id',
            field=models.CharField(max_length=255),
        ),
    ]
