# XRPL MCP Service

A Model Context Protocol (MCP) server implementation for interacting with the XRP Ledger blockchain. This service provides a standardized way for AI models to interact with the XRP Ledger.

## Prerequisites

- Python 3.9 or higher
- Poetry for dependency management
- XRP Ledger account (for testing)

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/tedlikeskix/xrpl-mcp-service.git
cd xrpl-mcp-service
```

2. Install dependencies:
```bash
poetry install
```

3. Start the server:
```bash
poetry run uvicorn src.xrpl_mcp.server:create_app --reload
```

## Testing the Service

You can test the service using curl commands. Here are some examples:

1. Get server info:
```bash
curl -X POST http://localhost:8000/mcp/v1 \
  -H "Content-Type: application/json" \
  -d '{
    "type": "server_info",
    "params": {}
  }'
```

2. Get account info:
```bash
curl -X POST http://localhost:8000/mcp/v1 \
  -H "Content-Type: application/json" \
  -d '{
    "type": "account_info",
    "params": {
      "account": "rHb9CJAWyB4rj91VRWn96DkukG4bwdtyTh"
    }
  }'
```

3. Check server health:
```bash
curl http://localhost:8000/health
```

## Integration with Your Existing Server

To integrate this with your existing MCP server:

1. Install the package in your project:
```bash
cd your-existing-project
poetry add xrpl-mcp-service
```

2. Register the XRPL tools in your register_tools.py:
```python
from xrpl_mcp.handlers import XRPLRequestHandler
from xrpl.clients import JsonRpcClient

def register_tools(mcp):
    # Initialize XRPL client
    client = JsonRpcClient("https://s.altnet.rippletest.net:51234")
    handler = XRPLRequestHandler(client)
    
    # Register XRPL tools
    @mcp.tool(name="xrpl_account_info")
    async def handle_account_info(account: str):
        return await handler._handle_account_info({"account": account})
        
    @mcp.tool(name="xrpl_server_info")
    async def handle_server_info():
        return await handler._handle_server_info({})

    # Add more tools as needed
```

## Available Endpoints

The service provides the following MCP-compatible endpoints:

- Account Methods:
  - account_info
  - account_lines
  - account_nfts
  - account_transactions
  
- Server Methods:
  - server_info
  
- Transaction Methods:
  - submit_transaction
  - transaction_info
  
- Trading Methods:
  - book_offers

## Error Handling

The service uses standard HTTP status codes and returns errors in this format:

```json
{
  "result": {},
  "error": "Error description here"
}
```

## Development

To run in development mode with auto-reload:
```bash
poetry run uvicorn src.xrpl_mcp.server:create_app --reload --port 8000
```

## License

MIT