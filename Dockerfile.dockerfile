# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies (including python3.11-venv)
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.11-venv \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container
COPY . /app

# Create a virtual environment and install Python dependencies
RUN python3.11 -m venv venv && \
    source venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the default port
ENV PORT=8000
EXPOSE $PORT

# Run the application
CMD ["sh", "-c", "source venv/bin/activate && \
    python3 manage.py migrate && \
    python3 manage.py collectstatic --noinput && \
    gunicorn forge.wsgi:application --bind 0.0.0.0:$PORT --timeout 120 --workers 4 --preload"]