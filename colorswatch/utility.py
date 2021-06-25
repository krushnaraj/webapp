import pandas as pd
from  .models import  ColorToHexCodeMapping, GridColor

class utility:

	def __init__(self):
		print('Initializing utility class')

	def generate_colorhex_data(self):

		df = pd.read_csv('.color/csv')
		for index, row in df.iterrows():

			name = ''.join(e for e in str(row['Code_Name']).lower() if e.isalnum())
			parent = ''

			if 'blue' in name:
				parent = 'blue'
			elif 'green' in name:
				parent = 'green'
			elif 'red' in name:
				parent = 'red'
			elif 'orange' in name:
				parent = 'orange'
			elif 'yellow' in name:
				parent = 'yellow'
			elif 'pink' in name:
				parent = 'pink'
			elif 'brown' in name:
				parent = 'brown'
			elif 'purple' in name:
				parent = 'purple'
			elif 'grey' in name:
				parent = 'grey'

			if parent !='':
				hex_value = str(row['Hex'])
				record = ColorToHexCodeMapping(parent = parent, code_name=name, hex_value = hex_value)
				record.save()

	def generate_colorgrid(self):
		colors_grid = GridColor.objects.all()
		if len(colors_grid)==0:
			print('true')
			for i in range(0, len(colors)-4, 4):
				print(type(colors))
				print(colors[i+1].hex_value)

				record = GridColor(parent1 = colors[i].parent, 
									parent2 = colors[i+1].parent,
									parent3 = colors[i+2].parent,
									parent4 = colors[i+3].parent,
									name1 = colors[i].code_name,
									name2 = colors[i+1].code_name,
									name3 = colors[i+2].code_name,
									name4 = colors[i+3].code_name,
									color1 = colors[i].hex_value,
									color2 = colors[i+1].hex_value,
									color3 = colors[i+2].hex_value,
									color4 = colors[i+3].hex_value)

				record.save()
