# Generated by Django 2.0.2 on 2018-10-11 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20181011_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='olddetailamazon',
            name='asin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.asinDetail'),
        ),
    ]