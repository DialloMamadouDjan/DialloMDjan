import os

os.system("echo 'UBUNTU POST-INSTALL SCRIPT' ")
os.system("echo 'Updating APT...' ")
# To get update and install them 
os.system("sudo apt-get update")

os.system("echo 'Installing base package' ")
# To install Git and python essentials builds
os.system("sudo apt-get install --yes git git-extras build-essential python3-pip htop glances")

os.system("clear")
# To Install discord
os.system("sudo snap install discord")

os.system("clear")
# To install Visual Studio 
os.system("sudo snap install --classic code")

