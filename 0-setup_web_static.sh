#!/usr/bin/env bash
# Install Nginx
sudo apt-get update
sudo apt-get install -y nginx

# Create directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a simple HTML file
echo "<html>
  <head></head>
  <body>Holberton School</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx config with new location block for /hbnb_static
sudo sed -i '/^\tserver_name _;/a \\\n\tlocation /hbnb_static/ {\n\t\talias /alu-AirBnB_clone_v2/web_static/;\n\t\tindex index.html;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
