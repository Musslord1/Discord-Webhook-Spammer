@echo off
Title Download Modules...
python --version 3>NUL
if errorlevel 1 goto errorNoPython
pip -v>NUL
if errorlevel 1 goto errorNoPip
pip install dhook
pip install requests
cls
Title Downloading Modules
echo
start Webhook_Spammer.py