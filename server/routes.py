
from flask import Blueprint, jsonify, request
import csv
from datetime import datetime
from models import Mobile, db  # Import necessary models

# Create the mobile_routes blueprint
mobile_routes = Blueprint('mobile_routes', __name__)

# Route to fetch all mobiles or search based on query
@mobile_routes.route('/mobiles', methods=['GET'])  # Update the route to match /api/mobiles
def get_mobiles():
    search = request.args.get('search', '').strip().lower()
    try:
        if search:
            # Case-insensitive search
            mobiles = Mobile.query.filter(Mobile.name.ilike(f'%{search}%')).all()
        else:
            # If no search query is provided, return all mobiles
            mobiles = Mobile.query.all()

        if not mobiles:
            return jsonify({'message': 'No phones found', 'data': []}), 200  # Return 200 with empty data

        # Convert mobiles to dictionaries
        return jsonify({'data': [mobile.to_dict() for mobile in mobiles]}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'message': 'An error occurred while fetching mobiles', 'error': str(e)}), 500

# Route to handle booking of a mobile
@mobile_routes.route('/book', methods=['POST'])  # Should match the route defined in app.py
def book_mobile():
    try:
        data = request.get_json()

        # Validate input fields
        name = data.get('name')
        phone_name = data.get('phone_name')
        mobile_number = data.get('mobile_number')
        address = data.get('address')
        delivery_date = data.get('delivery_date')

        if not all([name, phone_name, mobile_number, address, delivery_date]):
            return jsonify({'message': 'All fields are required'}), 400

        # Prepare the booking data to write to CSV
        booking_data = [name, phone_name, mobile_number, address, delivery_date, datetime.now().strftime('%Y-%m-%d %H:%M:%S')]

        # Write to CSV file
        with open('bookings.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            # Check if file is empty and write header if needed
            if file.tell() == 0:
                writer.writerow(['Name', 'Phone Name', 'Mobile Number', 'Address', 'Delivery Date', 'Booking Time'])  # Write header
            writer.writerow(booking_data)  # Write the new booking data

        return jsonify({'message': 'Your phone is booked successfully!'}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'message': 'An error occurred while booking the phone', 'error': str(e)}), 500
