from PIL import Image, UnidentifiedImageError
import io
import base64
import bson
from pymongo import MongoClient
from machine_learning_client.ml_client import classify_clothing

app = Flask(__name__)
client = MongoClient('localhost', 27017)
database = client.get_database('project4')
users = database.get_collection('images')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/classify-image', methods=['POST'])
def classify_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'}), 400

    try:
        file = request.files['image']
        image_data = base64.b64decode(file.read())
        image = Image.open(io.BytesIO(image_data))
    except UnidentifiedImageError:
        return jsonify({'error': 'Invalid image format'})

    # Convert PIL Image to binary format for classification
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    image_binary = buffer.getvalue()

    # Save image and classification to MongoDB
    image_document = {
        'image': bson.binary.Binary(image_binary),
        'classification': classify_clothing(image_binary)
    }
    users.insert_one(image_document)

    # Convert binary data back to base64 for response
    image_base64 = base64.b64encode(image_binary).decode('utf-8')

    return jsonify({'image_data': image_base64, 'classification': image_document['classification']})


if __name__ == '__main__':
    app.run(debug=True)
