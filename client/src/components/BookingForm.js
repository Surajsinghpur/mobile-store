
import React, { useState } from 'react';

function BookingForm({ phones, closeModal }) {
    const [name, setName] = useState('');
    const [mobileNumber, setMobileNumber] = useState('');
    const [address, setAddress] = useState('');
    const [deliveryDate, setDeliveryDate] = useState('');
    const [selectedPhone, setSelectedPhone] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!name || !mobileNumber || !address || !deliveryDate || !selectedPhone) {
            setMessage('All fields are required!');
            return;
        }

        const bookingData = {
            name: name,
            phone_name: selectedPhone,
            mobile_number: mobileNumber,
            address: address,
            delivery_date: deliveryDate,
        };

        try {
            const response = await fetch('http://127.0.0.1:8000/api/book', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(bookingData),
            });

            const result = await response.json();
            if (response.ok) {
                setMessage('Booking successful!');
            } else {
                setMessage(result.message || 'Error booking phone. Please try again.');
            }
        } catch (error) {
            setMessage('Error booking phone. Please try again later.');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className="form-group">
                <label>Name</label>
                <input
                    type="text"
                    className="form-control"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required
                />
            </div>
            <div className="form-group">
                <label>Mobile Number</label>
                <input
                    type="text"
                    className="form-control"
                    value={mobileNumber}
                    onChange={(e) => setMobileNumber(e.target.value)}
                    required
                />
            </div>
            <div className="form-group">
                <label>Address</label>
                <textarea
                    className="form-control"
                    value={address}
                    onChange={(e) => setAddress(e.target.value)}
                    required
                />
            </div>
            <div className="form-group">
                <label>Delivery Date</label>
                <input
                    type="date"
                    className="form-control"
                    value={deliveryDate}
                    onChange={(e) => setDeliveryDate(e.target.value)}
                    required
                />
            </div>
            <div className="form-group">
                <label>Select Phone</label>
                <select
                    className="form-control"
                    value={selectedPhone}
                    onChange={(e) => setSelectedPhone(e.target.value)}
                    required
                >
                    <option value="">Select a phone</option>
                    {phones.map((phone) => (
                        <option key={phone.id} value={phone.name}>
                            {phone.name}
                        </option>
                    ))}
                </select>
            </div>
            <button type="submit" className="btn btn-primary">
                Submit
            </button>
            {message && <div className="mt-3">{message}</div>}
        </form>
    );
}

export default BookingForm;
