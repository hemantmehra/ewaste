from keras.applications import InceptionV3, imagenet_utils
from keras.applications.inception_v3 import preprocess_input
from keras.preprocessing.image import img_to_array, load_img
import numpy as np

input_shape = (299, 299)
preprocess = preprocess_input

Network = InceptionV3
model = Network(weights = 'imagenet')



def recognize(filename):
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
