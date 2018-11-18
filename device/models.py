from django.db import models

device_choices = (
	('DW', 'Dish Washer'),
	('TV', 'TV'),
	('LP', 'Laptop'),
	('RF', 'Refrigerator'),
	('MS', 'Mouse'),
	('KB', 'Keyboard'),
	('HD', 'Hair Dryer'),
	('PD', 'iPod'),
	('MW', 'Microwave'),
	('MP', 'Microphone'),
	('RC', 'Remote Control')
)

brand_choices = (
	('LG', 'LG'),
	('SM', 'Samsung'),
	('XYZ', 'XYZ')
)

model_choices = (
	('XY456', 'XY456'),
	('ABC89', 'ABC89'),
	('PQR56', 'PQR56')
)

element_choices = (
	('Co', 'Copper'),
	('Si', 'Silver'),
	('Pl', 'Platinum'),
	('Go', 'Gold'),
	('Pa', 'Palladium'),
	('Ta', 'Tantalum'),
	('Wh', 'Whetstone'),
	('Ti', 'Tin'),
	('Zi', 'Zinc'),
	('St', 'Steel'),
	('Bi', 'Bismuth'),
	('Ir', 'Iron'),
	('An', 'Antimony'),
	('Ni', 'Nickel'),
	('Al', 'Aluminium'),
	('Co', 'Cobalt'),
	('Ox', 'Oxygen'),
	('Ca', 'Carbon'),
	('Si', 'Silicon'),
	('In', 'Indium'),
	('Ga', 'Gallium'),
	('Ne', 'Neodymium'),
	('Me', 'Mercury'),
	('Ca', 'Cadmium'),
	('Su', 'Sulphur'),
	('Br', 'Brominated Flame Retardants'),
	('Pe', 'Perfluorooctanoic acid'),
	('Be', 'Beryllium Oxide'),
	('Po', 'Polyvinyl Chloride'),
	('He', 'Hexavalent Chromium'),
	('Le', 'Lead'),
	('Am', 'Americium')
)

# Create your models here.
class Element(models.Model):
	name = models.CharField(max_length=2, choices=element_choices)
	effect = models.CharField(max_length=1000)

	def __str__(self):
		return self.name

class Device(models.Model):
	device_type = models.CharField(max_length=2, choices=device_choices)
	price = models.IntegerField(default=0)
	elements = models.ManyToManyField(Element)

	def __str__(self):
		return self.device_type


