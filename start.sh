#!/bin/bash
set -e

echo "=== Starting Hermes Agent Bot ==="
echo "Date: $(date)"
echo "Working directory: $(pwd)"
echo "Python: $(python --version)"
echo ""

echo "=== Checking environment variables ==="
if [ -n "$HF_TOKEN" ]; then
    echo "HF_TOKEN: set (${HF_TOKEN:0:10}...)"
else
    echo "HF_TOKEN: NOT SET"
fi

if [ -n "$TELEGRAM_BOT_TOKEN" ]; then
    echo "TELEGRAM_BOT_TOKEN: set (${TELEGRAM_BOT_TOKEN:0:15}...)"
else
    echo "TELEGRAM_BOT_TOKEN: NOT SET"
fi

if [ -n "$TELEGRAM_ALLOWED_USERS" ]; then
    echo "TELEGRAM_ALLOWED_USERS: $TELEGRAM_ALLOWED_USERS"
else
    echo "TELEGRAM_ALLOWED_USERS: NOT SET"
fi

echo ""
echo "=== Installing dependencies ==="
pip install -r requirements.txt

echo ""
echo "=== Starting Hermes Gateway ==="
echo "Check logs below for Telegram connection status..."
echo ""

exec hermes gateway start
