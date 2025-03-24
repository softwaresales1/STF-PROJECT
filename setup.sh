#!/bin/bash

set -e  # Exit immediately if a command fails

# Set PORT explicitly for Render deployment
export PORT=10000  

# Ensure the virtual environment exists
if [ ! -d "venv" ]; then
    python3.11 -m venv venv --without-pip
fi

# Activate the virtual environment
source venv/bin/activate

# Ensure pip is installed
if ! command -v pip &>/dev/null; then
    curl -sS https://bootstrap.pypa.io/get-pip.py | python
fi

# Upgrade pip and install dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput --clear

# Start Gunicorn with optimized settings
exec gunicorn Work.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers $(nproc) \
    --timeout 120 \
    --preload \
    --log-level=info