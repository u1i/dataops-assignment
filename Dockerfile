# Use the official Python base image
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application files to the working directory
COPY app.py .

# Expose port 8080 for the Flask application
EXPOSE 8080

# Run the Flask application using Gunicorn as the WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]


