#!/usr/bin/env bash
# This is a script that sets a web server for deploying a web_static

# Install nginx if not installed
if ! command -v nginx &> /dev/null; then
	sudo apt-get update
	sudo apt-get install -y nginx
fi

# create directories if they dont exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# creating a HTML file
sudo echo "<!DOCTYPE html>
<html>
<head>
</head>
<body>
This is a test Holberton School
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# creating and recrating a symbolic link
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# giving owership to Ubuntu users and group
sudo chown -R ubuntu:ubuntu /data/

# updating nginx configuration
config_file="/etc/nginx/sites-enabled/default"
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/; }' "$config_file"

# restart nginx
sudo service nginx restart
