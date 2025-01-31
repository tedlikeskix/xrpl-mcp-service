"""
XRPL MCP Service - FastAPI Server Implementation
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
from xrpl.clients import JsonRpcClient

from .handlers import XRPLRequestHandler

class MCPRequest(BaseModel):
    type: str
    params: Dict[str, Any]

class MCPResponse(BaseModel):
    result: Dict[str, Any]
    error: Optional[str] = None

class XRPLMCPServer:
    def __init__(self, xrpl_url: str = "https://s.altnet.rippletest.net:51234"):
        self.client = JsonRpcClient(xrpl_url)
        self.handler = XRPLRequestHandler(self.client)
        self.app = FastAPI(
            title="XRPL MCP Service",
            description="MCP server for interacting with the XRP Ledger",
            version="0.1.0"
        )
        self._setup_routes()

    def _setup_routes(self):
        @self.app.post("/mcp/v1")
        async def handle_mcp_request(request: MCPRequest) -> MCPResponse:
            """
            Handle MCP requests for XRPL interactions
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
            return {"status": "healthy"}

def create_app(xrpl_url: str = "https://s.altnet.rippletest.net:51234") -> FastAPI:
    """
    Create and configure the FastAPI application
    """
    server = XRPLMCPServer(xrpl_url)
    return server.app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(create_app(), host="0.0.0.0", port=8000)