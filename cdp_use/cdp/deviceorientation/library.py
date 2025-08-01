# This file is auto-generated by the CDP protocol generator.
# Do not edit this file manually as your changes will be overwritten.
# Generated from Chrome DevTools Protocol specifications.

"""CDP DeviceOrientation Domain Library"""

from typing import Any, Dict, Optional, cast

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...client import CDPClient
    from .commands import SetDeviceOrientationOverrideParameters

class DeviceOrientationClient:
    """Client for DeviceOrientation domain commands."""

    def __init__(self, client: 'CDPClient'):
        self._client = client

    async def clearDeviceOrientationOverride(
        self,
        params: None = None,
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        """Clears the overridden Device Orientation."""
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="DeviceOrientation.clearDeviceOrientationOverride",
            params=params,
            session_id=session_id,
        ))

    async def setDeviceOrientationOverride(
        self,
        params: "SetDeviceOrientationOverrideParameters",
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        """Overrides the Device Orientation."""
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="DeviceOrientation.setDeviceOrientationOverride",
            params=params,
            session_id=session_id,
        ))


