#!/bin/bash

# Update ALLOWED_HOSTS and add STATIC_ROOT to LifeLoader/settings.py
SETTINGS_FILE="LifeLoader/settings.py"
NEW_ALLOWED_HOSTS="['<ip of the server>']" # edit this one to have your server ip
NEW_STATIC_ROOT="STATIC_ROOT = Path.joinpath(BASE_DIR, 'static')"

# Update ALLOWED_HOSTS
sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = $NEW_ALLOWED_HOSTS/" $SETTINGS_FILE

# Add STATIC_ROOT line
sed -i "/^STATIC_URL/a $NEW_STATIC_ROOT" $SETTINGS_FILE

# Run collectstatic command
python3 manage.py collectstatic