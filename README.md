# XRPL MCP Service

A Model Context Protocol (MCP) server implementation for interacting with the XRP Ledger blockchain. This service allows AI models to interact with XRPL through standardized MCP endpoints.

## Quick Start for Replit

1. Clone this repository in Replit
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with:
```env
XRPL_NODE_URL=https://s.altnet.rippletest.net:51234
```

4. Run the server:
```bash
uvicorn src.xrpl_mcp.server:create_app --host 0.0.0.0 --port 8080 --reload
```

## Available Endpoints

### MCP Endpoint (`/mcp/v1`)
Accepts POST requests with:
```json
{
    "type": "string",  // Type of request
    "params": {}       // Parameters for the request
}
```

### Available Request Types:
1. Account Methods:
   - `account_info`: Get basic account information
   - `account_lines`: Get account trust lines
   - `account_nfts`: Get account NFTs
   - `account_transactions`: Get account history

2. Server Methods:
   - `server_info`: Get XRPL node status

3. Transaction Methods:
   - `submit_transaction`: Submit signed transaction
   - `transaction_info`: Get transaction details

## Testing

1. Get Server Info:
```bash
curl -X POST http://localhost:8080/mcp/v1 \
  -H "Content-Type: application/json" \
  -d '{
    "type": "server_info",
    "params": {}
  }'
```

2. Get Account Info:
```bash
curl -X POST http://localhost:8080/mcp/v1 \
  -H "Content-Type: application/json" \
  -d '{
    "type": "account_info",
    "params": {
      "account": "rHb9CJAWyB4rj91VRWn96DkukG4bwdtyTh"
    }
  }'
```

## Integration with Existing MCP Server

To add this as a tool to your existing MCP server:

1. Install XRPL dependencies:
```bash
pip install xrpl-py fastapi uvicorn
```

2. Add to your tools/register_tools.py:
```python
from xrpl_mcp import create_app as create_xrpl_app

def register_tools(mcp):
    # Your existing tool registrations...
    
    # Register XRPL tools
    xrpl_app = create_xrpl_app()
    mcp.tool("xrpl")(xrpl_app)
```

## Development

1. Install dev dependencies:
```bash
pip install -r requirements-dev.txt
```

2. Run tests:
```bash
pytest
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT