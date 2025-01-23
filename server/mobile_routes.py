from flask import Blueprint, jsonify
from models import Mobile  # Import your Mobile model from models.py

# Create a blueprint for mobile-related routes
mobile_routes = Blueprint('mobile_routes', __name__)

@mobile_routes.route('/get_mobiles', methods=['GET'])
def get_mobiles():
    # Define the phone_images mapping here
    phone_images = {
        'iphone': '/static/images/iphone.jpg',
        'samsung': '/static/images/samsung.jpg',
        'oneplus': '/static/images/oneplus.jpg',
        'google pixel': '/static/images/pixel.jpg',
    }
    
    print("Inside '/get_mobiles' route.")  # Log to verify route is being hit
    phones = Mobile.query.all()  # Fetch all mobile phones from the database
    if phones:
        return jsonify([{
            "id": phone.id,
            "name": phone.name,
            "price": phone.price,
            "details": phone.details,
            "image_url": phone.image_url 
        } for phone in phones])
    else:
        return jsonify({'message': 'No phones found'}), 404

# Helper function to get the phone image
def get_phone_image(phone_name, phone_images):
    for key in phone_images:
        if key.lower() in phone_name.lower():
            return phone_images[key]
    return '/static/images/default.jpg'  # Fallback image


