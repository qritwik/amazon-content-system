# Generated by Django 2.0.2 on 2018-10-17 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20181016_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='olddetailamazon',
            name='old_from_manufacture',
            field=models.CharField(blank=True, max_length=1000000, null=True),
        ),
    ]
