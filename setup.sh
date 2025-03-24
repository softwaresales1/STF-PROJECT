#!/bin/bash

set -e  # Exit immediately if a command fails

# Set PORT explicitly for Render deployment
export PORT=10000  

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3.11 -m venv venv --without-pip
fi

# Activate the virtual environment
source venv/bin/activate

# Install pip manually if missing
if ! command -v pip &>/dev/null; then
    curl -sS https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    rm get-pip.py
fi

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn with explicit port binding
exec gunicorn Work.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 4 \
    --timeout 120 \
    --log-level=info