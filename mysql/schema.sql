-- Create the database
CREATE DATABASE IF NOT EXISTS mobile_store;

-- Switch to the newly created database
USE mobile_store;

-- Create the mobile table
CREATE TABLE IF NOT EXISTS mobile (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,  -- Use DECIMAL for better precision in monetary values
    imageUrl VARCHAR(200) NOT NULL,
    link VARCHAR(200) NOT NULL
);

-- Create the booking table
CREATE TABLE IF NOT EXISTS booking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL,
    delivery_date DATE NOT NULL,
    mobile_id INT,
    FOREIGN KEY (mobile_id) REFERENCES mobile(id)  -- Ensure foreign key is valid
);
