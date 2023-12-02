from flask import Flask, render_template, request, redirect, url_for 
from pymongo import MongoClient 
import base64
import bson


app = Flask(__name__)
client = MongoClient('localhost', 27017) 
database = client.get_database('project4')  
users = database.get_collection('images') 


@app.route('/')
def start():
    return render_template('home_page.html')

@app.route('/save-image', methods=['POST'])
def save_image():
    data = request.json
    image_data = data['image']
    image_data = image_data.split(',')[1]  # Remove the base64 prefix

    # Convert base64 to binary
    image_binary = base64.b64decode(image_data)

    # Save to MongoDB
    image_id = users.insert_one({'image': bson.binary.Binary(image_binary)}).inserted_id

    return
@app.route('/result')
def get_image():
    # Fetch the latest image from MongoDB
    image_data = users.find_one(sort=[('_id', -1)])  # Adjust this query as per your need
    if image_data and 'image' in image_data:
        image_binary = image_data['image']
        # Convert binary to base64 for HTML display
        image_base64 = base64.b64encode(image_binary).decode('utf-8')
        return render_template('result.html', image_data=image_base64)
    return "No image found", 404

if __name__ == '__main__':
    app.run()