# Use Python 3.10 base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements (if you have any) and install
COPY setup.cfg ./
RUN pip install --no-cache-dir flask

# Copy the application code
COPY app.py ./
COPY __init__.py ./

# Expose the port your app runs on
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
