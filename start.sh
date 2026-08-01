#!/bin/bash
set -e

echo "Installing Hermes Agent..."
pip install -r requirements.txt

echo "Starting Hermes Gateway..."
exec hermes gateway start
