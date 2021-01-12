#!/bin/bash
echo "UBUNTU POST-INSTALL SCRIPT"
echo "Updating API..."
sudo apt-get update
sudo apt-get install --yes git git-extras build essentials python3-pip
sudo snap install discord
sudo snap install code