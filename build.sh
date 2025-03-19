#!/usr/bin/env bash

# Enhanced error handling
set -o errexit
set -o nounset
set -o pipefail
set -o xtrace

# Logging function
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

# Install dependencies
log "Upgrading pip..."
pip install --upgrade pip || { log "Failed to upgrade pip"; exit 1; }

log "Installing requirements..."
pip install -r requirements.txt || { log "Failed to install requirements"; exit 1; }

# Django commands
log "Running Django migrations..."
python manage.py migrate --no-input || { log "Failed to run migrations"; exit 1; }

log "Collecting static files..."
python manage.py collectstatic --no-input || { log "Failed to collect static files"; exit 1; }

log "Build completed successfully!"
