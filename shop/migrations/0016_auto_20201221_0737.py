# Generated by Django 3.1.2 on 2020-12-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_variation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(choices=[('None', 'None'), ('size', 'size'), ('color', 'color'), ('package', 'package')], default='None', max_length=120),
        ),
    ]
