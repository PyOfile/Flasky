#!/bin/bash

#updates &upgrades debian system and installs the venv. You can change the name at the replacing venv to the name you like.

sudo apt update && sudo apt upgrade -y && sudo apt install python3-pip && sudo -H pip3 install virtualenv && sudo virtualenv venv
