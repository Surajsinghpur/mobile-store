
import React from 'react';
import PropTypes from 'prop-types';

const MobileCard = ({ mobile }) => {
    return (
        <div className="card shadow-sm" style={{ width: "80%", maxWidth: "300px", margin: "10px auto", minHeight: '6px' }}>
            <img
                src={mobile.image_url || "https://via.placeholder.com/200"}
                alt={mobile.name}
                className="card-img-top"
                style={{ height: '200px', objectFit: 'cover' }}
            />
            <div className="card-body">
                <h5 className="card-title">{mobile.name}</h5>
                <p className="card-text text-muted" style={{ fontSize: '16px' }}>
                    {mobile.details || "No details available."}
                </p>
                <p className="card-text font-weight-bold text-primary">
                    Price: ₹{mobile.price ? mobile.price.toFixed(2) : "Not Available"}
                </p>
            </div>
        </div>
    );
};

MobileCard.propTypes = {
    mobile: PropTypes.shape({
        name: PropTypes.string.isRequired,
        image_url: PropTypes.string,
        details: PropTypes.string,
        price: PropTypes.number,
    }).isRequired,
};

export default MobileCard;
