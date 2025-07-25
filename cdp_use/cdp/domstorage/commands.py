# This file is auto-generated by the CDP protocol generator.
# Do not edit this file manually as your changes will be overwritten.
# Generated from Chrome DevTools Protocol specifications.

"""CDP DOMStorage Domain Commands"""

from typing import List
from typing_extensions import TypedDict

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .types import Item
    from .types import StorageId

class ClearParameters(TypedDict):
    storageId: "StorageId"





class GetDOMStorageItemsParameters(TypedDict):
    storageId: "StorageId"


class GetDOMStorageItemsReturns(TypedDict):
    entries: "List[Item]"



class RemoveDOMStorageItemParameters(TypedDict):
    storageId: "StorageId"
    key: "str"





class SetDOMStorageItemParameters(TypedDict):
    storageId: "StorageId"
    key: "str"
    value: "str"


