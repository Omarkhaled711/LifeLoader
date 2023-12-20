#!/bin/bash

# Update and upgrade packages
sudo apt update
sudo apt upgrade -y

# Install and configure UFW
sudo apt install ufw
sudo ufw reset -y
sudo ufw default allow outgoing
sudo ufw default deny incoming
sudo ufw allow ssh
sudo ufw allow http/tcp
sudo ufw enable

# Install Python 3, pip, and venv
sudo apt-get install python3-pip -y
sudo apt-get install python3-venv -y

# Create and activate virtual environment
python3 -m venv LifeLoader/venv
source LifeLoader/venv/bin/activate # make sure to adjust the path to where you installed LifeLoader

# Install Python dependencies
pip3 install -r requirements.txt
