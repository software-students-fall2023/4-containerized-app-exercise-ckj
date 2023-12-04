import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
import numpy as np
from pymongo import MongoClient

# Initialize MongoDB Connection
client = MongoClient('mongodb://localhost:27017/')
db = client.project4
collection = db.images

# Load Pre-trained Model
model = InceptionV3(weights='imagenet')

# Function to classify image and return the class
def classify_clothing(image_data):
    # Convert the base64 string to a PIL image
    img = image.load_img(io.BytesIO(base64.b64decode(image_data)), target_size=(299, 299))
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
    # Let's assume the second element in the tuple is the clothing type
    clothing_type = top_prediction[1]
    return clothing_type
