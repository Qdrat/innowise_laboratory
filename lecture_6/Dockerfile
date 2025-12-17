# Use official Python runtime as base image
FROM python:3.12-slim

# Install uv package manager
RUN pip install uv

# Set working directory inside container
WORKDIR /app

# Copy dependency configuration files first (for layer caching)
COPY pyproject.toml uv.lock ./

# Install project dependencies using uv (without dev dependencies)
RUN uv sync --frozen --no-dev

# Copy application source code
COPY . .

# Expose application port (FastAPI default)
EXPOSE 8000

# Run the application using uv's environment with uvicorn server
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
