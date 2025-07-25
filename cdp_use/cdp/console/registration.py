# This file is auto-generated by the CDP protocol generator.
# Do not edit this file manually as your changes will be overwritten.
# Generated from Chrome DevTools Protocol specifications.

"""CDP Console Domain Event Registration"""

from typing import Callable, Optional

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..registry import EventRegistry
    from .events import MessageAddedEvent

class ConsoleRegistration:
    """Event registration interface for Console domain."""

    def __init__(self, registry: 'EventRegistry'):
        self._registry = registry
        self._domain = "Console"

    def messageAdded(
        self,
        callback: Callable[['MessageAddedEvent', Optional[str]], None],
    ) -> None:
        """
        Register a callback for messageAdded events.
        
        Issued when new console message is added.
        
        Args:
            callback: Function to call when event occurs.
                     Receives (event_data, session_id) as parameters.
        """
        self._registry.register("Console.messageAdded", callback)

