# This file is auto-generated by the CDP protocol generator.
# Do not edit this file manually as your changes will be overwritten.
# Generated from Chrome DevTools Protocol specifications.

"""CDP DeviceAccess Domain Types"""

from typing_extensions import TypedDict

RequestId = str
"""Device request id."""



DeviceId = str
"""A device id."""



class PromptDevice(TypedDict):
    """Device information displayed in a user prompt to select a device."""

    id: "DeviceId"
    name: "str"
    """Display name as it appears in a device request user prompt."""
