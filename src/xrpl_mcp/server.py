"""
XRPL MCP Service - FastAPI Server Implementation
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
from xrpl.clients import JsonRpcClient
import os
from dotenv import load_dotenv

from .handlers import XRPLRequestHandler

load_dotenv()

# Use mainnet URL
XRPL_NODE = os.getenv('XRPL_NODE_URL', 'https://xrplcluster.com')

class MCPRequest(BaseModel):
    type: str
    params: Dict[str, Any]

class MCPResponse(BaseModel):
    result: Dict[str, Any]
    error: Optional[str] = None

class XRPLMCPServer:
    def __init__(self, xrpl_url: str = XRPL_NODE):
        self.client = JsonRpcClient(xrpl_url)
        self.handler = XRPLRequestHandler(self.client)
        self.app = FastAPI(
            title="XRPL MCP Service",
            description="MCP server for interacting with the XRP Ledger Mainnet",
            version="0.1.0"
        )
        self._setup_routes()

    def _setup_routes(self):
        @self.app.post("/mcp/v1")
        async def handle_mcp_request(request: MCPRequest) -> MCPResponse:
            """
            Handle MCP requests for XRPL interactions.
            
            Example requests:
            ```json
            {
                "type": "account_info",
                "params": {
                    "account": "rsuUjfWxrACCAwGQDsNeZUhpzXf1n1NK5Z"
                }
            }
            ```
            
            ```json
            {
                "type": "server_info",
                "params": {}
            }
            ```
            """
            try:
                result = await self.handler.handle_request(
                    request_type=request.type,
                    params=request.params
                )
                return MCPResponse(result=result)
            except Exception as e:
                return MCPResponse(result={}, error=str(e))
        
        @self.app.get("/health")
        async def health_check():
            """
            Health check endpoint
            """
            try:
                # Try to get server info as health check
                server_info = await self.handler.handle_request("server_info", {})
                return {"status": "healthy", "xrpl_connected": True}
            except:
                return {"status": "unhealthy", "xrpl_connected": False}

def create_app(xrpl_url: str = XRPL_NODE) -> FastAPI:
    """
    Create and configure the FastAPI application
    """
    server = XRPLMCPServer(xrpl_url)
    return server.app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(create_app(), host="0.0.0.0", port=8000)