# Generated by Django 2.0.2 on 2018-10-10 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_empdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empdetail',
            name='asin_done',
        ),
        migrations.AddField(
            model_name='asindetail',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='empdetail',
            name='asin_done_c',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
