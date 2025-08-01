# This file is auto-generated by the CDP protocol generator.
# Do not edit this file manually as your changes will be overwritten.
# Generated from Chrome DevTools Protocol specifications.

"""CDP Console Domain Events"""

from typing_extensions import TypedDict

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .types import ConsoleMessage

"""Issued when new console message is added."""
class MessageAddedEvent(TypedDict):
    message: "ConsoleMessage"
    """Console message that has been added."""
