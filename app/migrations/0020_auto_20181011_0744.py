# Generated by Django 2.0.2 on 2018-10-11 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20181011_0739'),
    ]

    operations = [
        migrations.CreateModel(
            name='oldDetailAmazon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_name', models.CharField(blank=True, max_length=10000, null=True)),
                ('old_url', models.CharField(blank=True, max_length=10000, null=True)),
                ('old_desc', models.CharField(blank=True, max_length=100000, null=True)),
                ('old_brand', models.CharField(blank=True, max_length=10000, null=True)),
                ('old_product_desc', models.CharField(blank=True, max_length=100000, null=True)),
                ('asin', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='oldDetail',
        ),
    ]