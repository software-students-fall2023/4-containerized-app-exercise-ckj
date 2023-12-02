import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
from pymongo import MongoClient

# Initialize MongoDB Connection
client = MongoClient('mongodb://localhost:27017/')
db = client.project4
collection = db.images

# Load Pre-trained Model
model = InceptionV3(weights='imagenet')

def dsimilar_image(img_path):
    #TO DO

# Example usage
image_path = 'path_to_your_image.jpg'
print(similar_image(image_path))
