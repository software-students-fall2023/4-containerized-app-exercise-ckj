import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.utils import to_categorical
from tensorflow.keras import layers
from keras.layers import Conv2D, Dense, Dropoout, Flatten, MaxPooling2D
import numpy as np
import matplotlib.pylot as plt
from keras.datasets import ImageNet
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
from pymongo import MongoClient

# Initialize MongoDB Connection
client = MongoClient('mongodb://localhost:27017/')
db = client.project4
collection = db.images



#(x_train, y_train), (x_test, y_test) = ImageNet.load_data()









# Load Pre-trained Model
model = InceptionV3(weights='imagenet')

# Function to classify image and return the class
def classify_clothing(img_path):
    # Load the image file, resizing it to 299x299 pixels (required input size for InceptionV3)
    img = image.load_img(img_path, target_size=(299, 299))
    # Convert the image to a numpy array
    img_array = image.img_to_array(img)
    # Add a dimension to the image array to represent the batch size
    img_array = np.expand_dims(img_array, axis=0)
    # Preprocess the image for the model
    img_array = preprocess_input(img_array)
    # Predict the class of the image
    predictions = model.predict(img_array)
    # Decode the predictions to get human-readable labels
    decoded_predictions = decode_predictions(predictions)

    top_prediction = decoded_predictions[0][0]
    # The top_prediction is a tuple like ('n02504458', 'African_elephant', 0.82658267)
    # Let's assume the second element in the tuple is the clothing type
    clothing_type = top_prediction[1]
    return clothing_type

# # Example usage
# image_path = '/Users/liwenqian/Desktop/Team/4-containerized-app-exercise-ckj/clothing-dataset-small/shirt.jpeg'
# clothing_type = classify_clothing(image_path)
# print(f'Clothing type: {clothing_type}')
