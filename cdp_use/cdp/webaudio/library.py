# This file is auto-generated by the CDP protocol generator.
# Do not edit this file manually as your changes will be overwritten.
# Generated from Chrome DevTools Protocol specifications.

"""CDP WebAudio Domain Library"""

from typing import Any, Dict, Optional, cast

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...client import CDPClient
    from .commands import GetRealtimeDataParameters
    from .commands import GetRealtimeDataReturns

class WebAudioClient:
    """Client for WebAudio domain commands."""

    def __init__(self, client: 'CDPClient'):
        self._client = client

    async def enable(
        self,
        params: None = None,
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        """Enables the WebAudio domain and starts sending context lifetime events."""
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="WebAudio.enable",
            params=params,
            session_id=session_id,
        ))

    async def disable(
        self,
        params: None = None,
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        """Disables the WebAudio domain."""
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="WebAudio.disable",
            params=params,
            session_id=session_id,
        ))

    async def getRealtimeData(
        self,
        params: "GetRealtimeDataParameters",
        session_id: Optional[str] = None,
    ) -> "GetRealtimeDataReturns":
        """Fetch the realtime data from the registered contexts."""
        return cast("GetRealtimeDataReturns", await self._client.send_raw(
            method="WebAudio.getRealtimeData",
            params=params,
            session_id=session_id,
        ))


