from django.shortcuts import render
from django.http import HttpResponse
from .models import  ColorToHexCodeMapping, GridColor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import pandas as pd
import random
from .utility import utility

# Create your views here.

def list_view(request):

	colors = ColorToHexCodeMapping.objects.all()
	if(len(colors)==0):
		util = utility()
		util.generate_colorhex_data()

	colors_grid = GridColor.objects.all()
	if(len(colors_grid)==0):
		util = utility()
		util.generate_colorgrid()
		colors_grid = GridColor.objects.all()

	paginator = Paginator(colors_grid, 4)
	page = request.GET.get('page',1)
	colors = paginator.get_page(page)

	try:
		colors = paginator.page(page)
	except PageNotAnInteger:
		colors = paginator.page(1)
	except EmptyPage:
		colors = paginator.page(paginator.num_pages)

	return render(request,'colorswatch/list_view.html', {'colors':colors})

def detail_view_search(request):

	color = request.POST['search_color'].lower()
	colors= ColorToHexCodeMapping.objects.filter(parent=color).order_by('-id')[:6]
	color_list = {'color0': colors[0].hex_value, 'color1':colors[1].hex_value, 'color2':colors[2].hex_value, 'color3':colors[3].hex_value,'color4':colors[4].hex_value,
					'color5':colors[5].hex_value}

	context = {'colors': color_list}

	return render(request, 'colorswatch/detail_view.html',context)

def detail_view_random(request):

	colors = ['green','red','blue','green','yellow','orange','purple','brown']
	random_color = random.choice(colors)

	colors= ColorToHexCodeMapping.objects.filter(parent=random_color).order_by('-id')[:6]
	color_list = {'color0': colors[0].hex_value, 'color1':colors[1].hex_value, 'color2':colors[2].hex_value, 'color3':colors[3].hex_value,'color4':colors[4].hex_value,
					'color5':colors[5].hex_value}

	context = {'colors': color_list}

	return render(request, 'colorswatch/detail_view.html',context)


def detail_view_color(request, name):

	colors= ColorToHexCodeMapping.objects.filter(parent=name).order_by('-id')[:6]
	color_list = {'color0': colors[0].hex_value, 'color1':colors[1].hex_value, 'color2':colors[2].hex_value, 'color3':colors[3].hex_value,'color4':colors[4].hex_value,
					'color5':colors[5].hex_value}

	context = {'colors': color_list}

	return render(request, 'colorswatch/detail_view.html',context)

def detail_view(request, name):

	if 'blue' in name:
		colors= ColorToHexCodeMapping.objects.filter(parent='blue').order_by('-id')[:5]
	elif 'green' in name:
		colors= ColorToHexCodeMapping.objects.filter(parent='green').order_by('-id')[:5]
	elif 'red' in name:
		colors= ColorToHexCodeMapping.objects.filter(parent='red').order_by('-id')[:5]
	elif 'orange' in name:
		colors= ColorToHexCodeMapping.objects.filter(parent='orange').order_by('-id')[:5]
	elif 'yellow' in name:
		colors= ColorToHexCodeMapping.objects.filter(parent='yellow').order_by('-id')[:5]
	elif 'pink' in name:
		colors= ColorToHexCodeMapping.objects.filter(parent='pink').order_by('-id')[:5]
	elif 'brown' in name:
		colors= ColorToHexCodeMapping.objects.filter(parent='brown').order_by('-id')[:5]
	elif 'purple' in name:
		colors= ColorToHexCodeMapping.objects.filter(parent='purple').order_by('-id')[:5]
	elif 'grey' in name:
		colors= ColorToHexCodeMapping.objects.filter(parent='grey').order_by('-id')[:5]
	elif 'gold' in name:
		colors= ColorToHexCodeMapping.objects.filter(parent='gold').order_by('-id')[:5]
	color = ColorToHexCodeMapping.objects.filter(code_name=name).order_by('-id')[:1]

	color_list = {'color0': color[0].hex_value, 'color1':colors[0].hex_value, 'color2':colors[1].hex_value, 'color3':colors[2].hex_value,'color4':colors[3].hex_value,
					'color5':colors[4].hex_value}

	context = {'colors': color_list}

	return render(request, 'colorswatch/detail_view.html',context)