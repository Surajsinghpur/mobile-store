// export default SearchBar;
import React, { useState } from 'react';

const SearchBar = ({ onSearch }) => {
    const [query, setQuery] = useState('');

    const handleSearch = () => {
        if (query.trim()) {
            onSearch(query.trim()); // Pass query to parent component
        }
    };

    return (
        <div className="input-group">
            <input
                type="text"
                className="form-control"
                placeholder="Search for mobiles..."
                value={query}
                onChange={(e) => setQuery(e.target.value)} // Update state with query
                onKeyDown={(e) => e.key === 'Enter' && handleSearch()} // Trigger search on Enter key
            />
            <button className="btn btn-primary" onClick={handleSearch}>
                Search
            </button>
        </div>
    );
};

export default SearchBar;
