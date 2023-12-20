#!/bin/bash

CONFIG_FILE="/home/omar/life/LifeLoaderConfig.json" # change this path to where you want your file to be

# Check if the file exists, and create it if not
if [ ! -f "$CONFIG_FILE" ]; then
    touch "$CONFIG_FILE"
fi

# Set variables for sensitive information
SECRET_KEY="your_secret_key"
DJANGO_EMAIL="your_email@example.com"
DJANGO_PASS="your_email_password"
DB_NAME="your_db_name"
DB_USER="your_db_user"
DB_PASS="your_db_password"

# Update the configuration file
cat <<EOF > "$CONFIG_FILE"
{
  "SECRET_KEY": "$SECRET_KEY",
  "DJANGO_EMAIL": "$DJANGO_EMAIL",
  "DJANGO_PASS": "$DJANGO_PASS",
  "DB_NAME": "$DB_NAME",
  "DB_USER": "$DB_USER",
  "DB_PASS": "$DB_PASS"
}
EOF
