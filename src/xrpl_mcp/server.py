from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from xrpl.clients import JsonRpcClient
from xrpl.models import AccountInfo, ServerInfo

class MCPRequest(BaseModel):
    type: str
    params: Dict[str, Any]

class MCPResponse(BaseModel):
    result: Dict[str, Any]
    error: Optional[str] = None

class XRPLMCPServer:
    def __init__(self, xrpl_url: str = "https://s.altnet.rippletest.net:51234"):
        self.client = JsonRpcClient(xrpl_url)
        self.app = FastAPI(
            title="XRPL MCP Service",
            description="MCP server for interacting with the XRP Ledger",
            version="0.1.0"
        )
        self._setup_routes()

    def _setup_routes(self):
        @self.app.post("/mcp/v1")
        async def handle_mcp_request(request: MCPRequest) -> MCPResponse:
            try:
                if request.type == "account_info":
                    response = self.client.request(AccountInfo(
                        account=request.params.get("account")
                    ))
                    return MCPResponse(result=response.result)
                elif request.type == "server_info":
                    response = self.client.request(ServerInfo())
                    return MCPResponse(result=response.result)
                else:
                    raise HTTPException(
                        status_code=400,
                        detail=f"Unsupported request type: {request.type}"
                    )
            except Exception as e:
                return MCPResponse(result={}, error=str(e))

def create_app(xrpl_url: str = "https://s.altnet.rippletest.net:51234") -> FastAPI:
    server = XRPLMCPServer(xrpl_url)
    return server.app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(create_app(), host="0.0.0.0", port=8000)