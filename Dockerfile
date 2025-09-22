# Use official Python runtime as the base image
FROM python:3.9-slim

# Set environment variables to prevent buffering issues
ENV PYTHONUNBUFFERED=1

# Set work directory inside container
WORKDIR /app

# Copy requirement files and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project code
COPY . /app

# Expose port matching your app's listening port
EXPOSE 8081

# Command to run your FastAPI app with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8081"]
