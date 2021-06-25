from django.db import models

# Create your models here.


class ColorToHexCodeMapping(models.Model):
	parent = models.CharField(max_length=50)
	code_name = models.CharField(max_length=50)
	hex_value = models.CharField(max_length=10)

class GridColor(models.Model):
	parent1 = models.CharField(max_length=10)
	parent2 = models.CharField(max_length=10)
	parent3 = models.CharField(max_length=10)
	parent4 = models.CharField(max_length=10)
	name1 = models.CharField(max_length=10)
	name2 = models.CharField(max_length=10)
	name3 = models.CharField(max_length=10)
	name4 = models.CharField(max_length=10)
	color1 = models.CharField(max_length=10)
	color2 = models.CharField(max_length=10)
	color3 = models.CharField(max_length=10)
	color4 = models.CharField(max_length=10)

