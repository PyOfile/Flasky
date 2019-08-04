#!/bin/bash

#updates and installs the venv your can cange the name in at the venv to the name you like at the end of the script

sudo apt update && sudo apt upgrade -y && sudo apt install python3-pip && sudo pip3 install virtualenv && sudo virtualenv venv
