# Generated by Django 3.1.2 on 2020-11-23 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20201120_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='variants',
            name='discount_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='variants',
            name='price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
