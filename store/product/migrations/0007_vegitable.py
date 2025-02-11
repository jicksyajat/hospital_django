# Generated by Django 5.1.2 on 2024-10-22 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_doctors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vegitable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veg_name', models.CharField(max_length=200)),
                ('veg_price', models.BigIntegerField()),
                ('veg_image', models.ImageField(default='defaults_image.jpg', upload_to='vegitable')),
            ],
        ),
    ]
