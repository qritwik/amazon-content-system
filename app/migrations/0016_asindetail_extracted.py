# Generated by Django 2.0.2 on 2018-10-11 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20181010_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='asindetail',
            name='extracted',
            field=models.BooleanField(default=False),
        ),
    ]