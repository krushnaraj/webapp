# Generated by Django 3.2.4 on 2021-06-22 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colorswatch', '0002_auto_20210621_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorsMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('shades', models.CharField(max_length=10)),
            ],
        ),
    ]
