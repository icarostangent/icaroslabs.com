# Generated by Django 3.2.20 on 2023-08-03 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20230731_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaddress',
            name='verify_key',
            field=models.CharField(default='Px9RCddYkbr7Xr3TH2WbX7XipmAOYdRw', max_length=255, null=True),
        ),
    ]