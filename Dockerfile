# Generated by https://smithery.ai. See: https://smithery.ai/docs/config#dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project descriptor files into the container
COPY pyproject.toml /app/
COPY src /app/src

# Install Poetry
RUN pip install poetry

# Install the Python dependencies specified in pyproject.toml
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV XRPL_NODE_URL=https://xrplcluster.com

# Run the application
CMD ["uvicorn", "src.xrpl_mcp.server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
