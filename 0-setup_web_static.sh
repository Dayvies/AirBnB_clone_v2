#!/usr/bin/env bash
#setting up nginx
if [ -x "$(command -v nginx)" ]; then
      true
else
        apt update
        apt-get -y install nginx
        apt-get -y install ufw
        ufw --force enable
        ufw allow 'Nginx HTTP'
        ufw allow 22/tcp
        nginx -s reload
fi
mkdir -p /data
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
echo "
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
service nginx restart
exit 0
