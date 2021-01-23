# Generated by Django 3.1.2 on 2020-10-26 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField()),
                ('discount_parcent', models.IntegerField()),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('availability', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping', models.CharField(blank=True, max_length=50, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='item_pc')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_set', to='shop.category')),
            ],
        ),
    ]