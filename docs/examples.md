# XRPL MCP Service Examples

This document provides examples of how to use the XRPL MCP Service.

## Setup

First, install and run the service:

```bash
# Install dependencies
poetry install

# Run the server
poetry run uvicorn src.xrpl_mcp.server:create_app --reload
```

## Making Requests

The MCP service accepts POST requests to `/mcp/v1` with a JSON body containing:
- `type`: The type of request
- `params`: Parameters for the request

### Example Requests

1. Get Account Information:
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

2. Get Server Info:
```bash
curl -X POST http://localhost:8000/mcp/v1 \
  -H "Content-Type: application/json" \
  -d '{
    "type": "server_info",
    "params": {}
  }'
```

3. Get Account NFTs:
```bash
curl -X POST http://localhost:8000/mcp/v1 \
  -H "Content-Type: application/json" \
  -d '{
    "type": "account_nfts",
    "params": {
      "account": "rHb9CJAWyB4rj91VRWn96DkukG4bwdtyTh"
    }
  }'
```

4. Get Order Book:
```bash
curl -X POST http://localhost:8000/mcp/v1 \
  -H "Content-Type: application/json" \
  -d '{
    "type": "book_offers",
    "params": {
      "taker_gets": {"currency": "XRP"},
      "taker_pays": {
        "currency": "USD",
        "issuer": "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B"
      }
    }
  }'
```

## Python Client Example

Here's how to use the service from Python:

```python
import requests

def make_mcp_request(type: str, params: dict) -> dict:
    response = requests.post(
        "http://localhost:8000/mcp/v1",
        json={
            "type": type,
            "params": params
        }
    )
    return response.json()

# Get account info
result = make_mcp_request(
    "account_info",
    {"account": "rHb9CJAWyB4rj91VRWn96DkukG4bwdtyTh"}
)
print(result)

# Get server info
result = make_mcp_request("server_info", {})
print(result)
```

## Available Request Types

1. Account Methods:
   - `account_info`: Get basic account information
   - `account_lines`: Get account trust lines
   - `account_nfts`: Get account NFTs
   - `account_transactions`: Get account transaction history

2. Server Methods:
   - `server_info`: Get server status and info

3. Transaction Methods:
   - `submit_transaction`: Submit a signed transaction
   - `transaction_info`: Get transaction details

4. Trading Methods:
   - `book_offers`: Get order book data

## Error Handling

The service returns errors in the following format:
```json
{
    "result": {},
    "error": "Error message here"
}
```

Common errors include:
- Invalid request type
- Missing required parameters
- XRPL network errors
- Invalid account addresses