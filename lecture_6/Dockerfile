# Using the official Python image
FROM python:3.12.3-slim

# Install uv package manager
RUN pip install uv

# Set the working directory to /app inside the container
WORKDIR /app

# Copy the pyproject file and install dependencies
COPY pyproject.toml uv.lock ./

# Download all requirements
RUN uv pip install --system -r pyproject.toml

# Copy the rest of the application code
COPY . .

# Expose port (adjust as needed)
EXPOSE 8000

# Define the command to run the application when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
