# Use a minimal and secure Python runtime as base image
FROM python:3.11-alpine

# Set environment variables for performance & security
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=10000 \
    VENV_PATH="/app/venv" \
    PATH="/app/venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Install system dependencies and clean up to reduce image size
RUN apk add --no-cache --update \
    build-base \
    libpq \
    postgresql-dev \
    && rm -rf /var/cache/apk/*

# Copy only dependency files first for Docker caching
COPY requirements.txt .

# Create virtual environment and install dependencies efficiently
RUN python3 -m venv $VENV_PATH && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the remaining application files
COPY . .

# Set proper permissions for the working directory
RUN addgroup -S appgroup && adduser -S appuser -G appgroup && chown -R appuser:appgroup /app

# Expose port for Render deployment
EXPOSE $PORT

# Switch to a non-root user for security
USER appuser

# Start the application
CMD ["sh", "-c", "
    python manage.py migrate --noinput && \
    python manage.py collectstatic --noinput && \
    gunicorn Work.wsgi:application --bind 0.0.0.0:$PORT --timeout 120 --workers $(nproc) --preload"]