import io
import numpy as np
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image as keras_image


# Load the pre-trained InceptionV3 model
model = InceptionV3(weights='imagenet')


def classify_clothing(image_binary):
    """Classifies the given image using the InceptionV3 model.

    Args:
        image_binary (bytes): The binary data of the image.

    Returns:
        str: The predicted clothing type.
    """
    try:
        # Convert binary data to a PIL Image
        image = Image.open(io.BytesIO(image_binary))

        # Resize and preprocess the image
        image = image.resize((299, 299))
        image_array = img_to_array(image)
        image_array = np.expand_dims(image_array, axis=0)
        image_array = preprocess_input(image_array)

        # Classify the image using the InceptionV3 model
        predictions = model.predict(image_array)
        decoded_predictions = decode_predictions(predictions, top=1)
        clothing_type = decoded_predictions[0][0][1]

        return clothing_type
    except Exception as e:
        # Log any errors during classification
        print(f"An error occurred during classification: {e}")
        return "Error in classification"
