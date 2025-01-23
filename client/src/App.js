
import React, { useState, useEffect } from 'react';
import MobileCard from './components/MobileCard';  // Importing MobileCard component
import BookingForm from './components/BookingForm';  // Importing BookingForm component

function App() {
    const [phones, setPhones] = useState([]);
    const [searchQuery, setSearchQuery] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(true);
    const [selectedPhone, setSelectedPhone] = useState(null);
    const [showModal, setShowModal] = useState(false);

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

    const handleBookClick = () => {
        setShowModal(true);
    };

    const closeModal = () => {
        setShowModal(false);
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

            {phones.length > 0 && (
                <div className="text-center mt-4">
                    <button
                        className="btn btn-success"
                        onClick={handleBookClick}
                    >
                        Book Now
                    </button>
                </div>
            )}

            {showModal && (
                <div className="modal" style={{ display: 'block' }}>
                    <div className="modal-dialog">
                        <div className="modal-content">
                            <div className="modal-header">
                                <h5 className="modal-title">Book a Phone</h5>
                                <button
                                    type="button"
                                    className="close"
                                    onClick={closeModal}
                                >
                                    &times;
                                </button>
                            </div>
                            <div className="modal-body">
                                <BookingForm phones={phones} closeModal={closeModal} />
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}

export default App;
