FROM python:3.6-buster

# Set workdir

WORKDIR /app

# Install system dependencies

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev

# Install python requirements

RUN python -m pip install pip==9.0.3

COPY requirements.txt ./
COPY requirements_dev.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements_dev.txt

# Copy project files

COPY . .
