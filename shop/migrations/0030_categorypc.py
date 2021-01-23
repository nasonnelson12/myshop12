# Generated by Django 3.1.2 on 2021-01-14 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_auto_20210105_0635'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('product_id', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='item_pc')),
            ],
        ),
    ]