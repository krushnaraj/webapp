# Generated by Django 3.2.4 on 2021-06-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colorswatch', '0005_colorsgrid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorsMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(max_length=50)),
                ('hex_value', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='ColorsMapping',
        ),
    ]