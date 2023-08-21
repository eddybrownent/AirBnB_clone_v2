-- This is a script to prepare a MySQL sever for The project 
-- creates a database for development purposes and sets user with necessary privileges

-- create Database name : hbnb_dev_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;


-- creating user named : hbnb_dev with the password hbnb_dev_pwd if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';


-- granting all privilages on the hbnb_dev_db database to the hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- flushing the privileges to apply the changes
FLUSH PRIVILEGES;


-- grant SELECT privilege for hbnb_dev user in the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- flushing privileges again
FLUSH PRIVILEGES;
