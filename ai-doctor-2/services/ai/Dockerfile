FROM python:3.12-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and the .env file
COPY . .

# Expose the port the application runs on
EXPOSE 8002

# Run the application
CMD ["python", "main.py"]
