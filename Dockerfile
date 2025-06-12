# Use Python as the base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies and Chrome
RUN apt-get update && apt-get install -y \
    wget gnupg unzip curl \
    chromium-driver chromium

# Create app directory
WORKDIR /app
COPY . /app

# Install Python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Default run command
CMD ["python", "app.py"]