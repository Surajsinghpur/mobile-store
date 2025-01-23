
import React, { useState, useEffect } from 'react';
import MobileCard from './components/MobileCard';
import BookingForm from './components/BookingForm';

function MobileStore() {
    const [phones, setPhones] = useState([]);
    const [searchQuery, setSearchQuery] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(true);
    const [selectedPhone, setSelectedPhone] = useState(null);  // Store selected phone for booking
    const [showModal, setShowModal] = useState(false);  // State to control modal visibility

    useEffect(() => {
        fetchPhones();
    }, []);

    const fetchPhones = async (query = '') => {
        setLoading(true);
        setError('');
        const url = query
            ? `http://127.0.0.1:8000/api/phones?search=${query}`
            : `http://127.0.0.1:8000/api/phones`;

        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error('Failed to fetch data from the server.');
            }
            const data = await response.json();
            if (data.message === 'No phones found') {
                setPhones([]);
                setError('No phones found');
            } else {
                setPhones(data);
            }
        } catch (err) {
            console.error('Error fetching phones:', err);
            setError('Failed to fetch data. Please try again later.');
        } finally {
            setLoading(false);
        }
    };

    const handleSearch = () => {
        fetchPhones(searchQuery.trim());
    };

    // Open modal with selected phone details
    const handleBookClick = (phone) => {
        setSelectedPhone(phone);  // Set the selected phone for booking
        setShowModal(true);  // Show modal using state
    };

    // Close modal
    const closeModal = () => {
        setShowModal(false);  // Hide modal using state
    };

    return (
        <div className="container mt-4">
            <h1 className="text-center">Mobile Store</h1>

            <div className="input-group mb-3">
                <input
                    type="text"
                    className="form-control"
                    placeholder="Search phones"
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                />
                <button className="btn btn-primary" onClick={handleSearch}>
                    Search
                </button>
            </div>

            <div className="row">
                {phones.length > 0 ? (
                    phones.map((phone) => (
                        <div key={phone.id} className="col-md-4 mb-4">
                            <MobileCard mobile={phone} />
                        </div>
                    ))
                ) : (
                    <p className="text-center">No phones found</p>
                )}
            </div>

            {/* Book Now button at the end */}
            {phones.length > 0 && (
                <button
                    className="btn btn-success mt-4"
                    onClick={() => handleBookClick(phones[0])} // Assuming you want to book the first phone
                >
                    Book Now
                </button>
            )}

            {/* Modal for Booking Form */}
            {showModal && selectedPhone && (
                <div className="modal" style={{ display: 'block' }}>
                    <div className="modal-dialog">
                        <div className="modal-content">
                            <div className="modal-header">
                                <h5 className="modal-title">Book {selectedPhone.name}</h5>
                                <button
                                    type="button"
                                    className="close"
                                    onClick={closeModal}
                                >
                                    &times;
                                </button>
                            </div>
                            <div className="modal-body">
                                <BookingForm phoneName={selectedPhone.name} />
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}

export default MobileStore;
