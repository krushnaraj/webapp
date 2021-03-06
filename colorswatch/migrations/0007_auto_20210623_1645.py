# Generated by Django 3.2.4 on 2021-06-23 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colorswatch', '0006_auto_20210623_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorGrid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=10)),
                ('name2', models.CharField(max_length=10)),
                ('name3', models.CharField(max_length=10)),
                ('name4', models.CharField(max_length=10)),
                ('color1', models.CharField(max_length=10)),
                ('color2', models.CharField(max_length=10)),
                ('color3', models.CharField(max_length=10)),
                ('color4', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ColorToHexMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.CharField(max_length=50)),
                ('code_name', models.CharField(max_length=50)),
                ('hex_value', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='ColorsGrid',
        ),
        migrations.DeleteModel(
            name='ColorsMap',
        ),
    ]
