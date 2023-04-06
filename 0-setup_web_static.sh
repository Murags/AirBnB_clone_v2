#!/usr/bin/env bash
# install nginx an configure server
hbnb_location="\tlocation /hbnb_static {\n\
		# hbnb web_static\n\
        alias /data/web_static/current;\n\
		index index.html;\n\
	}\n"

# install nginx
sudo apt -y update
sudo apt -y upgrade
sudo apt -y install nginx


sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo  -e "You have been served" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R  ubuntu:ubuntu /data/
sudo sed -i "53i\\$hbnb_location" /etc/nginx/sites-available/default

service nginx restart
