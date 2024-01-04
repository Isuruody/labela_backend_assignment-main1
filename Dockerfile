
# Use Python 3.10.4 as the base image
FROM python:3.10.4 as builder

# Create a virtual environment
RUN python -m venv /venv

# Set the virtual environment as the active one
ENV PATH="/venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Install necessary build dependencies
RUN apt-get update && apt-get install -y bash vim nano postgresql-client libpq-dev

# Install major pinned Python dependencies for build
RUN pip install --no-cache-dir --upgrade pip==21.3.1 \
    && pip install --no-cache-dir flake8==3.8.4 uWSGI

# Copy requirements and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt || { echo "Failed to install dependencies"; exit 1; }

# Intermediate image for build, not used in the final image
FROM python:3.10.4-alpine

# Create a virtual environment
RUN python -m venv /venv

# Set the virtual environment as the active one
ENV PATH="/venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Install necessary system packages
RUN apk add --no-cache bash vim nano postgresql-client libpq-dev

# Copy from the builder image
COPY --from=builder /venv /venv
COPY . .

# Set environment variables
ENV WORKERS=2
ENV PORT=8080 
ENV PYTHONUNBUFFERED=1

# Expose the specified port
EXPOSE $PORT

# Set the command to start the uWSGI server
CMD uwsgi --http :$PORT --processes $WORKERS --static-map /static=/static --module autocompany.wsgi:application