@echo off
echo Installing Hermes Agent...
pip install -r requirements.txt

echo Starting Hermes Gateway...
hermes gateway start
pause
