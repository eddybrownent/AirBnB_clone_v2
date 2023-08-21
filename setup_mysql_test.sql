-- MySQL Server Preparation Script
-- This script is used to prepare a MySQL server for the project

-- Create a testing database named hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create or update a user named hbnb_test with the password hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant the Select privilege for the user hbnb_test on the performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

-- Grant all privileges to the user hbnb_test on the hbnb_test_db database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Flushes privileges to apply the changes
FLUSH PRIVILEGES;
