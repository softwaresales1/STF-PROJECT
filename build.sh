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

# Help message
show_help() {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  -h, --help        Show this help message"
    echo "  -c, --clean       Remove virtual environment before setup"
    echo "  -t, --test        Run tests after setup"
    echo "  -p, --python      Specify Python version (default: python3)"
    exit 0
}

# Parse arguments
PYTHON_CMD="python3"
RUN_TESTS=false
CLEAN=false

while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)
            show_help
            ;;
        -c|--clean)
            CLEAN=true
            ;;
        -t|--test)
            RUN_TESTS=true
            ;;
        -p|--python)
            PYTHON_CMD="$2"
            shift
            ;;
        *)
            echo "Unknown option: $1"
            show_help
            ;;
    esac
    shift
done

# Clean virtual environment if requested
if [ "$CLEAN" = true ] && [ -d "venv" ]; then
    log "Removing existing virtual environment..."
    rm -rf venv
fi

# Create and activate virtual environment
if [ ! -d "venv" ]; then
    log "Creating virtual environment..."
    if ! command -v "$PYTHON_CMD" &>/dev/null; then
        log "Error: $PYTHON_CMD not found. Please install Python or specify a different version with -p"
        exit 1
    fi
    "$PYTHON_CMD" -m venv venv || { log "Failed to create virtual environment"; exit 1; }
fi

log "Activating virtual environment..."
# shellcheck disable=SC1091
source venv/bin/activate || { log "Failed to activate virtual environment"; exit 1; }

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

# Optional: Run tests
if [ "$RUN_TESTS" = true ]; then
    log "Running tests..."
    python manage.py test || { log "Tests failed"; exit 1; }
fi

log "Build completed successfully!"
