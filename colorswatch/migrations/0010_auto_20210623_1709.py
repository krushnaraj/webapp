# Generated by Django 3.2.4 on 2021-06-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colorswatch', '0009_auto_20210623_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorsGrid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent1', models.CharField(max_length=10)),
                ('parent2', models.CharField(max_length=10)),
                ('parent3', models.CharField(max_length=10)),
                ('parent4', models.CharField(max_length=10)),
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
        migrations.DeleteModel(
            name='ColorGrid',
        ),
    ]