#!/usr/bin/env bash

# exit on error
set -o errexit
# exit on undefined variable
set -o nounset
# exit on pipe failure
set -o pipefail

# Print commands before executing
set -o xtrace

# Create and activate virtual environment (if needed)
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Django commands
python manage.py collectstatic --no-input
python manage.py migrate

# Optional: Run tests
# python manage.py test

echo "Build completed successfully!"
