#!/bin/bash

# Change ownership for LifeLoader directory
sudo chown :www-data LifeLoader/

# Change ownership and permissions for media directory
sudo chown -R :www-data LifeLoader/media/
sudo chmod -R 775 LifeLoader/media

# Change permissions for LifeLoader directory
sudo chmod 775 LifeLoader/
