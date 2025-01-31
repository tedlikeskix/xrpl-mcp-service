# XRPL MCP Service

A Model Context Protocol (MCP) server providing comprehensive access to the XRP Ledger (XRPL). This service enables AI models to interact with XRPL through standardized endpoints.

## Features

### Account Information
- `xrpl_account_info` - Basic account details
- `xrpl_account_balances` - XRP and token balances (human-readable)
- `xrpl_account_lines` - Trust lines
- `xrpl_account_offers` - Active trading offers
- `xrpl_account_nfts` - NFT holdings
- `xrpl_account_tx` - Transaction history

### Decentralized Exchange
- `xrpl_order_book` - View order book for currency pairs
- `xrpl_market_price` - Get current market prices
- `xrpl_amm_info` - Automated Market Maker information

### NFT Operations
- `xrpl_nft_offers` - View NFT buy/sell offers

### Trust Lines & Payments
- `xrpl_set_trust_line` - Establish new trust lines
- `xrpl_remove_trust_line` - Remove existing trust lines
- `xrpl_payment_channels` - Payment channel information
- `xrpl_find_path` - Payment path finding
- `xrpl_deposit_auth` - Check payment authorization

### System
- `xrpl_server_info` - Node status and information
- `xrpl_submit_tx` - Submit signed transactions

## Setup

1. Create a `.env` file:
```env
XRPL_NODE_URL=https://xrplcluster.com
```

2. Install dependencies:
```bash
pip install xrpl-py fastapi uvicorn python-dotenv
```

3. Run the server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## API Usage Examples

### Get Account Info
```json
POST /call-tool/xrpl_account_info
{
  "account": "rsuUjfWxrACCAwGQDsNeZUhpzXf1n1NK5Z"
}
```

### Get Account Balances
```json
POST /call-tool/xrpl_account_balances
{
  "account": "rsuUjfWxrACCAwGQDsNeZUhpzXf1n1NK5Z"
}
```

### Set Trust Line
```json
POST /call-tool/xrpl_set_trust_line
{
  "wallet_seed": "sXXXXXXXXXXXXXXXXXXXX",
  "currency": "USD",
  "issuer": "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B",
  "limit": "1000"
}
```

### Get AMM Info
```json
POST /call-tool/xrpl_amm_info
{
  "asset": {
    "currency": "XRP"
  },
  "asset2": {
    "currency": "USD",
    "issuer": "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B"
  }
}
```

### Get Market Price
```json
POST /call-tool/xrpl_market_price
{
  "base_currency": {
    "currency": "XRP"
  },
  "quote_currency": {
    "currency": "USD",
    "issuer": "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B"
  }
}
```

## Project Structure

```
├── main.py              # FastAPI application entry point
├── tools/
│   ├── __init__.py
│   ├── register_tools.py # Tool registration
│   └── xrpl_tools.py    # XRPL endpoint implementations
```

## Key Components

1. **xrpl_tools.py**
   - Core XRPL interaction functions
   - Async implementation with event loop handling
   - Error handling and response formatting

2. **register_tools.py**
   - MCP tool registration
   - Endpoint mapping and configuration

## Future Enhancements

1. AMM (Liquidity Pool) Operations
   - Create pools
   - Add/remove liquidity
   - Vote on pool parameters

2. Advanced Trading
   - Create/cancel offers
   - Automated trading functions
   - Price alerts

3. NFT Operations
   - Mint NFTs
   - Create/accept offers
   - Collection management

## Common Issues

1. **Async Event Loop**: If you see "asyncio.run() cannot be called from a running event loop", check the async implementation in xrpl_tools.py

2. **Rate Limiting**: Consider implementing rate limiting for production use

## Contributing

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Submit a pull request

## Important Notes

- Always use "validated" ledger for production
- Secure wallet seeds and private keys
- Monitor transaction fees
- Test thoroughly on testnet first

## Resources

- [XRPL Documentation](https://xrpl.org/docs.html)
- [MCP Protocol Docs](https://docs.anthropic.com/claude/docs/model-context-protocol)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## License

MIT