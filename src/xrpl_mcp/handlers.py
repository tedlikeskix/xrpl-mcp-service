"""
XRPL MCP Service - Request Handlers
"""
from typing import Dict, Any, Optional
from xrpl.clients import JsonRpcClient
from xrpl.models import (
    AccountInfo,
    AccountLines,
    AccountNFTs,
    AccountTx,
    ServerInfo,
    Submit,
    Tx,
    BookOffers
)
from xrpl.utils import hex_to_str

class XRPLRequestHandler:
    def __init__(self, client: JsonRpcClient):
        self.client = client

    async def handle_request(self, request_type: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle different types of XRPL requests
        """
        handlers = {
            "account_info": self._handle_account_info,
            "account_lines": self._handle_account_lines,
            "account_nfts": self._handle_account_nfts,
            "account_transactions": self._handle_account_transactions,
            "server_info": self._handle_server_info,
            "submit_transaction": self._handle_submit_transaction,
            "transaction_info": self._handle_transaction_info,
            "book_offers": self._handle_book_offers
        }

        handler = handlers.get(request_type)
        if not handler:
            raise ValueError(f"Unsupported request type: {request_type}")
        
        return await handler(params)

    async def _handle_account_info(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Get account information"""
        response = self.client.request(AccountInfo(
            account=params.get("account")
        ))
        return response.result

    async def _handle_account_lines(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Get account trust lines"""
        response = self.client.request(AccountLines(
            account=params.get("account")
        ))
        return response.result

    async def _handle_account_nfts(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Get account NFTs"""
        response = self.client.request(AccountNFTs(
            account=params.get("account")
        ))
        return response.result

    async def _handle_account_transactions(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Get account transactions"""
        response = self.client.request(AccountTx(
            account=params.get("account")
        ))
        return response.result

    async def _handle_server_info(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Get server information"""
        response = self.client.request(ServerInfo())
        return response.result

    async def _handle_submit_transaction(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Submit a signed transaction"""
        response = self.client.request(Submit(
            tx_blob=params.get("tx_blob")
        ))
        return response.result

    async def _handle_transaction_info(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Get transaction information"""
        response = self.client.request(Tx(
            transaction=params.get("hash")
        ))
        return response.result

    async def _handle_book_offers(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Get order book offers"""
        response = self.client.request(BookOffers(
            taker_gets=params.get("taker_gets"),
            taker_pays=params.get("taker_pays")
        ))
        return response.result