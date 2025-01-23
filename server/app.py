
from flask import Flask, jsonify, Blueprint, request
from flask_migrate import Migrate
from flask_cors import CORS
from extensions import db
import pymysql
import logging
import os
import csv
from datetime import datetime
from models import Mobile

# Initialize Flask app
app = Flask(__name__, static_folder=os.path.join(os.getcwd(), 'static'))

# Enable CORS for all routes, making sure to allow React on port 3000
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Database configuration for MySQL (only for mobile data)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Thought%401234@localhost/mobile_store'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Define Blueprint for mobile routes
mobile_routes = Blueprint('mobile_routes', __name__)

# Route to get all phones with optional search query
@mobile_routes.route('/phones', methods=['GET'])
def get_phones():
    search_query = request.args.get('search', '').lower()

    if search_query:
        phones = Mobile.query.filter(Mobile.name.ilike(f"%{search_query}%")).all()
    else:
        phones = Mobile.query.all()

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

# Route to handle booking of a mobile
@mobile_routes.route('/book', methods=['POST'])
def book_mobile():
    try:
        data = request.get_json()

        # Log the incoming data
        app.logger.debug(f"Received data: {data}")

        # Validate input fields
        name = data.get('name')
        phone_name = data.get('phone_name')
        mobile_number = data.get('mobile_number')
        address = data.get('address')
        delivery_date = data.get('delivery_date')

        required_fields = ['name', 'phone_name', 'mobile_number', 'address', 'delivery_date']
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            app.logger.error(f"Missing fields: {', '.join(missing_fields)}")
            return jsonify({'message': 'All fields are required'}), 400

        # Prepare the booking data to write to CSV
        booking_data = [name, phone_name, mobile_number, address, delivery_date, datetime.now().strftime('%Y-%m-%d %H:%M:%S')]

        app.logger.debug(f"Booking data: {booking_data}")

        # Write to CSV file
        with open('bookings.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['Name', 'Phone Name', 'Mobile Number', 'Address', 'Delivery Date', 'Booking Time'])
            writer.writerow(booking_data)

        return jsonify({'message': 'Your phone is booked successfully!'}), 201

    except Exception as e:
        app.logger.error(f"Error occurred while booking the phone: {str(e)}")
        return jsonify({'message': 'An error occurred while booking the phone', 'error': str(e)}), 500

# Register the Blueprint
app.register_blueprint(mobile_routes, url_prefix='/api')

# Add logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Test the database connection
def test_db_connection():
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="Thought@1234",
            database="mobile_store"
        )
        logging.debug("Database connection successful!")
        connection.close()
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")

# Test the connection
test_db_connection()

# Create tables if they don't exist (for mobile data)
with app.app_context():
    db.create_all()

# Run the app
if __name__ == '__main__':
    logging.debug("Starting the Flask server...")
    app.run(debug=True, host='127.0.0.1', port=8000)
