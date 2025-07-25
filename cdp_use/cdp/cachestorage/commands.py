# This file is auto-generated by the CDP protocol generator.
# Do not edit this file manually as your changes will be overwritten.
# Generated from Chrome DevTools Protocol specifications.

"""CDP CacheStorage Domain Commands"""

from typing import List
from typing_extensions import NotRequired, TypedDict

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..storage.types import StorageBucket
    from .types import Cache
    from .types import CacheId
    from .types import CachedResponse
    from .types import DataEntry
    from .types import Header

class DeleteCacheParameters(TypedDict):
    cacheId: "CacheId"
    """Id of cache for deletion."""





class DeleteEntryParameters(TypedDict):
    cacheId: "CacheId"
    """Id of cache where the entry will be deleted."""
    request: "str"
    """URL spec of the request."""





class RequestCacheNamesParameters(TypedDict, total=False):
    securityOrigin: "str"
    """At least and at most one of securityOrigin, storageKey, storageBucket must be specified.
Security origin."""
    storageKey: "str"
    """Storage key."""
    storageBucket: "StorageBucket"
    """Storage bucket. If not specified, it uses the default bucket."""


class RequestCacheNamesReturns(TypedDict):
    caches: "List[Cache]"
    """Caches for the security origin."""



class RequestCachedResponseParameters(TypedDict):
    cacheId: "CacheId"
    """Id of cache that contains the entry."""
    requestURL: "str"
    """URL spec of the request."""
    requestHeaders: "List[Header]"
    """headers of the request."""


class RequestCachedResponseReturns(TypedDict):
    response: "CachedResponse"
    """Response read from the cache."""



class RequestEntriesParameters(TypedDict):
    cacheId: "CacheId"
    """ID of cache to get entries from."""
    skipCount: "NotRequired[int]"
    """Number of records to skip."""
    pageSize: "NotRequired[int]"
    """Number of records to fetch."""
    pathFilter: "NotRequired[str]"
    """If present, only return the entries containing this substring in the path"""


class RequestEntriesReturns(TypedDict):
    cacheDataEntries: "List[DataEntry]"
    """Array of object store data entries."""
    returnCount: "float"
    """Count of returned entries from this storage. If pathFilter is empty, it
is the count of all entries from this storage."""
