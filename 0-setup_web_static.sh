#!/usr/bin/env bash
#setting up nginx
if [ -x "$(command -v nginx)" ]; then
      echo "Nginx already installed. Skipping installation..."
else
        sudo apt update
        sudo apt-get -y install nginx
        sudo apt-get -y install ufw
        sudo ufw --force enable
        sudo ufw allow 'Nginx HTTP'
        sudo ufw allow 22/tcp
        sudo nginx -s reload
fi
sudo mkdir -p /data
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
sudo echo "
<html>
  <head>
  </head>
  <body>
     School is good!
  </body>
</html>
" > /data/web_static/releases/test/index.html
sudo rm -f /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
