# This file is auto-generated by the CDP protocol generator.
# Do not edit this file manually as your changes will be overwritten.
# Generated from Chrome DevTools Protocol specifications.

"""CDP HeapProfiler Domain Events"""

from typing import List
from typing_extensions import NotRequired, TypedDict

class AddHeapSnapshotChunkEvent(TypedDict):
    chunk: "str"



"""If heap objects tracking has been started then backend may send update for one or more fragments"""
class HeapStatsUpdateEvent(TypedDict):
    statsUpdate: "List[int]"
    """An array of triplets. Each triplet describes a fragment. The first integer is the fragment
index, the second integer is a total count of objects for the fragment, the third integer is
a total size of the objects for the fragment."""



"""If heap objects tracking has been started then backend regularly sends a current value for last
seen object id and corresponding timestamp. If the were changes in the heap since last event
then one or more heapStatsUpdate events will be sent before a new lastSeenObjectId event."""
class LastSeenObjectIdEvent(TypedDict):
    lastSeenObjectId: "int"
    timestamp: "float"



class ReportHeapSnapshotProgressEvent(TypedDict):
    done: "int"
    total: "int"
    finished: "NotRequired[bool]"



class ResetProfilesEvent(TypedDict):
    pass
