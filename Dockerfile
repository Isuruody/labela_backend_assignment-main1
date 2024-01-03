# Use Python 3.10 as the base image
FROM python:3.10

# Create a virtual environment
RUN python -m venv /venv

# Set the virtual environment as the active one
ENV PATH="/venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Install necessary system packages
RUN apt-get update && apt-get install -y bash vim nano postgresql-client

# Upgrade pip and install major pinned python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir flake8==3.8.4 uWSGI

# Copy requirements and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire codebase into the container
COPY . .

# Set environment variables
ENV WORKERS=2
ENV PORT=8080 
ENV PYTHONUNBUFFERED=1

# Expose the specified port
EXPOSE ${PORT}

# Set the command to start the uWSGI server
CMD uwsgi --http :${PORT} --processes ${WORKERS} --static-map /static=/static --module autocompany.wsgi:application