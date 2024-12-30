# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install common system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gdal-bin \
    libgdal-dev \
    python3-gdal \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy project requirements
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Expose ports for Django
EXPOSE 8000

# Use an argument to determine the command to run
# ARG SERVICE
# CMD ["sh", "-c", "$SERVICE"]
