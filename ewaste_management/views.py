from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from device.models import device_choices, brand_choices, model_choices

import pandas as pd

#import ewaste_management.image_recognition 
#from ewaste_management.image_recognition import recognize

from keras.applications import InceptionV3, imagenet_utils
from keras.applications.inception_v3 import preprocess_input
from keras.preprocessing.image import img_to_array, load_img
import numpy as np


device_choices_dict = {
	'DW': 'Dishwasher',
	'TV': 'TV',
	'LP': 'Laptop',
	'RF': 'Refrigerator',
	'MS': 'Mouse',
	'KB': 'Keyboard',
	'HD': 'Hair Dryer',
	'PD': 'iPod',
	'MW': 'Microwave',
	'MP': 'Microphone',
	'RC': 'Remote Control'
}



def recognize(filename):
	input_shape = (299, 299)
	preprocess = preprocess_input
	Network = InceptionV3
	model = Network(weights = 'imagenet')
	
	image_path = "media/"+filename
	image = load_img(image_path, target_size = input_shape)
	image = img_to_array(image)
	image = np.expand_dims(image, axis = 0)
	image = preprocess(image)
	print('=====================')
	preds = model.predict(image)
	P = imagenet_utils.decode_predictions(preds)
	print('+++++++++++++++++++++')
	imagenetID, label, prob = P[0][0]

	return (label, prob)


# Create your views here.
def index(request):
	if request.method == 'POST' and request.FILES['device']:
		device = request.FILES['device']

		device_type = request.POST['device_type']
		brand = request.POST['brand']
		model = request.POST['model']

		df = pd.read_csv('Devices.csv')
		device_type_from_code = device_choices_dict[device_type]


		elements = list(df[df['Device'] == device_type_from_code]['Elements'])[0].split(', ')
		price = list(df[df['Device'] == device_type_from_code]['Price'])[0]


		df_el = pd.read_csv('Elements.csv')

		final_list = []
		lis = list(df_el['Element'])
		for element in elements:
			idx = lis.index(element.strip())
			final_list.append(df_el['Effect'].iloc[idx])

		zip_list = zip(elements, final_list)

		fs = FileSystemStorage()
		filename = fs.save(device.name, device)
		#(label, prob) = recognize(filename)
		uploaded_file_url = fs.url(filename)
		return render(request, 'ewaste_management/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'device_type': device_type_from_code,
            'brand': brand,
            'model': model,
            'elements':zip_list,
            'price': price
            #'label': label,
            #'prob': prob
        })
	return render(request, 'ewaste_management/index.html', {
		'devices': device_choices,
		'brands': brand_choices,
		'models': model_choices
		})