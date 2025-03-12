"""
Gunicorn configuration file for deploying the Django application.
This configuration supports environment variable overrides for increased flexibility.
"""

import os

# Bind to the host and port (default: 0.0.0.0:8000)
bind = os.getenv('GUNICORN_BIND', '0.0.0.0:8000')

# Number of workers (default: 3)
workers = int(os.getenv('GUNICORN_WORKERS', '3'))

# Log level (e.g., debug, info, warning)
loglevel = os.getenv('GUNICORN_LOG_LEVEL', 'info')

# Preload app for faster worker boot time
preload_app = os.getenv('GUNICORN_PRELOAD_APP', 'true').lower() in ('true', '1', 'yes')

# Auto-reload (disable in production)
reload = os.getenv('GUNICORN_RELOAD', 'false').lower() in ('true', '1', 'yes')
