# This file is auto-generated by the CDP protocol generator.
# Do not edit this file manually as your changes will be overwritten.
# Generated from Chrome DevTools Protocol specifications.

"""CDP ServiceWorker Domain Library"""

from typing import Any, Dict, Optional, cast

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...client import CDPClient
    from .commands import DeliverPushMessageParameters
    from .commands import DispatchPeriodicSyncEventParameters
    from .commands import DispatchSyncEventParameters
    from .commands import InspectWorkerParameters
    from .commands import SetForceUpdateOnPageLoadParameters
    from .commands import SkipWaitingParameters
    from .commands import StartWorkerParameters
    from .commands import StopWorkerParameters
    from .commands import UnregisterParameters
    from .commands import UpdateRegistrationParameters

class ServiceWorkerClient:
    """Client for ServiceWorker domain commands."""

    def __init__(self, client: 'CDPClient'):
        self._client = client

    async def deliverPushMessage(
        self,
        params: "DeliverPushMessageParameters",
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="ServiceWorker.deliverPushMessage",
            params=params,
            session_id=session_id,
        ))

    async def disable(
        self,
        params: None = None,
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="ServiceWorker.disable",
            params=params,
            session_id=session_id,
        ))

    async def dispatchSyncEvent(
        self,
        params: "DispatchSyncEventParameters",
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="ServiceWorker.dispatchSyncEvent",
            params=params,
            session_id=session_id,
        ))

    async def dispatchPeriodicSyncEvent(
        self,
        params: "DispatchPeriodicSyncEventParameters",
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="ServiceWorker.dispatchPeriodicSyncEvent",
            params=params,
            session_id=session_id,
        ))

    async def enable(
        self,
        params: None = None,
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="ServiceWorker.enable",
            params=params,
            session_id=session_id,
        ))

    async def inspectWorker(
        self,
        params: "InspectWorkerParameters",
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="ServiceWorker.inspectWorker",
            params=params,
            session_id=session_id,
        ))

    async def setForceUpdateOnPageLoad(
        self,
        params: "SetForceUpdateOnPageLoadParameters",
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="ServiceWorker.setForceUpdateOnPageLoad",
            params=params,
            session_id=session_id,
        ))

    async def skipWaiting(
        self,
        params: "SkipWaitingParameters",
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="ServiceWorker.skipWaiting",
            params=params,
            session_id=session_id,
        ))

    async def startWorker(
        self,
        params: "StartWorkerParameters",
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="ServiceWorker.startWorker",
            params=params,
            session_id=session_id,
        ))

    async def stopAllWorkers(
        self,
        params: None = None,
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="ServiceWorker.stopAllWorkers",
            params=params,
            session_id=session_id,
        ))

    async def stopWorker(
        self,
        params: "StopWorkerParameters",
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="ServiceWorker.stopWorker",
            params=params,
            session_id=session_id,
        ))

    async def unregister(
        self,
        params: "UnregisterParameters",
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="ServiceWorker.unregister",
            params=params,
            session_id=session_id,
        ))

    async def updateRegistration(
        self,
        params: "UpdateRegistrationParameters",
        session_id: Optional[str] = None,
    ) -> "Dict[str, Any]":
        return cast("Dict[str, Any]", await self._client.send_raw(
            method="ServiceWorker.updateRegistration",
            params=params,
            session_id=session_id,
        ))


