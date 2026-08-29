# Use an official, lightweight Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Prevent Python from writing .pyc files to disk and buffering logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install required network dependencies directly
RUN pip install --no-cache-dir requests

# Copy the SCADA engine script into the container
COPY facility_scada.py .

# Run the script when the container launches
CMD ["python", "facility_scada.py"]