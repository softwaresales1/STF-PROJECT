"""
Optimized Gunicorn configuration for deploying the Django application on Render.
This configuration dynamically adjusts workers, enables threading, and enhances performance.
"""

import os
import multiprocessing

# Bind Gunicorn to the host and port (default: 0.0.0.0:10000)
bind = os.getenv('GUNICORN_BIND', '0.0.0.0:10000')

# Dynamically calculate the number of workers (2x CPU cores)
cpu_cores = multiprocessing.cpu_count()
workers = int(os.getenv('GUNICORN_WORKERS', max(2, cpu_cores * 2)))  # Minimum 2 workers

# Enable threads for better concurrency handling
threads = int(os.getenv('GUNICORN_THREADS', '2'))  # Each worker handles 2 threads

# Set worker class to async (Uvicorn for ASGI support)
worker_class = os.getenv('GUNICORN_WORKER_CLASS', 'uvicorn.workers.UvicornWorker')

# Log level (e.g., debug, info, warning)
loglevel = os.getenv('GUNICORN_LOG_LEVEL', 'info')

# Enable keep-alive to reduce connection overhead (Render default is 5s)
keepalive = int(os.getenv('GUNICORN_KEEPALIVE', '75'))  # 75 seconds

# Set a timeout for handling long-running requests
timeout = int(os.getenv('GUNICORN_TIMEOUT', '120'))  # 120 seconds

# Limit request line size (default: 4094 bytes)
limit_request_line = 8190  # Handles long URLs

# Limit HTTP header size (default: 8190 bytes)
limit_request_field_size = 16384  # Prevents large headers from causing issues

# Preload application for faster startup and lower memory usage
preload_app = os.getenv('GUNICORN_PRELOAD_APP', 'true').lower() in ('true', '1', 'yes')

# Disable automatic reload in production (prevents excessive restarts)
reload = os.getenv('GUNICORN_RELOAD', 'false').lower() in ('true', '1', 'yes')

# Graceful worker timeout and maximum requests to prevent memory leaks
graceful_timeout = int(os.getenv('GUNICORN_GRACEFUL_TIMEOUT', '30'))
max_requests = int(os.getenv('GUNICORN_MAX_REQUESTS', '5000'))
max_requests_jitter = int(os.getenv('GUNICORN_MAX_REQUESTS_JITTER', '500'))

# Log access and errors for debugging
accesslog = os.getenv('GUNICORN_ACCESS_LOG', '-')
errorlog = os.getenv('GUNICORN_ERROR_LOG', '-')

# Suppress noisy request headers logging
forwarded_allow_ips = "*"
proxy_allow_ips = "*"

# Print Gunicorn settings on startup (for debugging)
if os.getenv('GUNICORN_DEBUG', 'false').lower() in ('true', '1', 'yes'):
    print(f"""
    Gunicorn Configuration:
    ------------------------
    Bind: {bind}
    Workers: {workers}
    Threads: {threads}
    Worker Class: {worker_class}
    Log Level: {loglevel}
    Keep-Alive: {keepalive}s
    Timeout: {timeout}s
    Preload App: {preload_app}
    Max Requests Before Restart: {max_requests} (±{max_requests_jitter})
    """)
