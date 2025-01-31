# XRPL MCP Service

An MCP server implementation for interacting with the XRP Ledger blockchain. This service provides a standardized way for AI models to interact with the XRP Ledger through the Model Context Protocol (MCP).

## Features

- XRPL account information retrieval
- Server status checking
- Transaction submission and monitoring
- More features coming soon...

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/xrpl-mcp-service.git
cd xrpl-mcp-service

# Install dependencies using Poetry
poetry install
```

## Usage

```bash
# Start the server
poetry run uvicorn src.xrpl_mcp.server:create_app --reload
```

## API Documentation

Once the server is running, you can access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## License

MIT