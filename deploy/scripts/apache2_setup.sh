#!/bin/bash

# Install Apache and mod_wsgi
sudo apt-get install apache2 -y
sudo apt-get install libapache2-mod-wsgi-py3 -y

# Copy the default Apache configuration file
sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/LifeLoader.conf

# Add configurations to LifeLoader.conf using sed
CONFIGS_TO_ADD=$(cat <<'EOF'
        Alias /static /home/ubuntu/LifeLoader/static
        <Directory /home/ubuntu/LifeLoader/static>
                Require all granted
        </Directory>

        Alias /media /home/ubuntu/LifeLoader/media
        <Directory /home/ubuntu/LifeLoader/media>
                Require all granted
        </Directory>

        <Directory /home/ubuntu/LifeLoader/LifeLoader>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        WSGIScriptAlias / /home/ubuntu/LifeLoader/LifeLoader/wsgi.py
        WSGIDaemonProcess LifeLoader_app python-path=/home/ubuntu/LifeLoader python-home=/home/ubuntu/LifeLoader/venv
        WSGIProcessGroup LifeLoader_app
EOF
)

# Add configurations to LifeLoader.conf
sudo sed -i "/<\/VirtualHost>/i $CONFIGS_TO_ADD" /etc/apache2/sites-available/LifeLoader.conf

# Enable the LifeLoader site
sudo a2ensite LifeLoader
sudo a2dissite 000-default.conf

# Restart Apache to apply changes
sudo systemctl restart apache2
