# This file is auto-generated by the CDP protocol generator.
# Do not edit this file manually as your changes will be overwritten.
# Generated from Chrome DevTools Protocol specifications.

"""CDP Emulation Domain Commands"""

from typing import List
from typing_extensions import NotRequired, TypedDict

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..dom.types import RGBA
    from ..network.types import TimeSinceEpoch
    from ..page.types import Viewport
    from .types import DevicePosture
    from .types import DisabledImageType
    from .types import DisplayFeature
    from .types import MediaFeature
    from .types import PressureMetadata
    from .types import PressureSource
    from .types import PressureState
    from .types import SafeAreaInsets
    from .types import ScreenOrientation
    from .types import SensorMetadata
    from .types import SensorReading
    from .types import SensorType
    from .types import UserAgentMetadata
    from .types import VirtualTimePolicy

class CanEmulateReturns(TypedDict):
    result: "bool"
    """True if emulation is supported."""



class SetFocusEmulationEnabledParameters(TypedDict):
    enabled: "bool"
    """Whether to enable to disable focus emulation."""





class SetAutoDarkModeOverrideParameters(TypedDict, total=False):
    enabled: "bool"
    """Whether to enable or disable automatic dark mode.
If not specified, any existing override will be cleared."""





class SetCPUThrottlingRateParameters(TypedDict):
    rate: "float"
    """Throttling rate as a slowdown factor (1 is no throttle, 2 is 2x slowdown, etc)."""





class SetDefaultBackgroundColorOverrideParameters(TypedDict, total=False):
    color: "RGBA"
    """RGBA of the default background color. If not specified, any existing override will be
cleared."""





class SetSafeAreaInsetsOverrideParameters(TypedDict):
    insets: "SafeAreaInsets"





class SetDeviceMetricsOverrideParameters(TypedDict):
    width: "int"
    """Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override."""
    height: "int"
    """Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override."""
    deviceScaleFactor: "float"
    """Overriding device scale factor value. 0 disables the override."""
    mobile: "bool"
    """Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text
autosizing and more."""
    scale: "NotRequired[float]"
    """Scale to apply to resulting view image."""
    screenWidth: "NotRequired[int]"
    """Overriding screen width value in pixels (minimum 0, maximum 10000000)."""
    screenHeight: "NotRequired[int]"
    """Overriding screen height value in pixels (minimum 0, maximum 10000000)."""
    positionX: "NotRequired[int]"
    """Overriding view X position on screen in pixels (minimum 0, maximum 10000000)."""
    positionY: "NotRequired[int]"
    """Overriding view Y position on screen in pixels (minimum 0, maximum 10000000)."""
    dontSetVisibleSize: "NotRequired[bool]"
    """Do not set visible view size, rely upon explicit setVisibleSize call."""
    screenOrientation: "NotRequired[ScreenOrientation]"
    """Screen orientation override."""
    viewport: "NotRequired[Viewport]"
    """If set, the visible area of the page will be overridden to this viewport. This viewport
change is not observed by the page, e.g. viewport-relative elements do not change positions."""
    displayFeature: "NotRequired[DisplayFeature]"
    """If set, the display feature of a multi-segment screen. If not set, multi-segment support
is turned-off.
Deprecated, use Emulation.setDisplayFeaturesOverride."""
    devicePosture: "NotRequired[DevicePosture]"
    """If set, the posture of a foldable device. If not set the posture is set
to continuous.
Deprecated, use Emulation.setDevicePostureOverride."""





class SetDevicePostureOverrideParameters(TypedDict):
    posture: "DevicePosture"





class SetDisplayFeaturesOverrideParameters(TypedDict):
    features: "List[DisplayFeature]"





class SetScrollbarsHiddenParameters(TypedDict):
    hidden: "bool"
    """Whether scrollbars should be always hidden."""





class SetDocumentCookieDisabledParameters(TypedDict):
    disabled: "bool"
    """Whether document.coookie API should be disabled."""





class SetEmitTouchEventsForMouseParameters(TypedDict):
    enabled: "bool"
    """Whether touch emulation based on mouse input should be enabled."""
    configuration: "NotRequired[str]"
    """Touch/gesture events configuration. Default: current platform."""





class SetEmulatedMediaParameters(TypedDict, total=False):
    media: "str"
    """Media type to emulate. Empty string disables the override."""
    features: "List[MediaFeature]"
    """Media features to emulate."""





class SetEmulatedVisionDeficiencyParameters(TypedDict):
    type: "str"
    """Vision deficiency to emulate. Order: best-effort emulations come first, followed by any
physiologically accurate emulations for medically recognized color vision deficiencies."""





class SetGeolocationOverrideParameters(TypedDict, total=False):
    latitude: "float"
    """Mock latitude"""
    longitude: "float"
    """Mock longitude"""
    accuracy: "float"
    """Mock accuracy"""
    altitude: "float"
    """Mock altitude"""
    altitudeAccuracy: "float"
    """Mock altitudeAccuracy"""
    heading: "float"
    """Mock heading"""
    speed: "float"
    """Mock speed"""





class GetOverriddenSensorInformationParameters(TypedDict):
    type: "SensorType"


class GetOverriddenSensorInformationReturns(TypedDict):
    requestedSamplingFrequency: "float"



class SetSensorOverrideEnabledParameters(TypedDict):
    enabled: "bool"
    type: "SensorType"
    metadata: "NotRequired[SensorMetadata]"





class SetSensorOverrideReadingsParameters(TypedDict):
    type: "SensorType"
    reading: "SensorReading"





class SetPressureSourceOverrideEnabledParameters(TypedDict):
    enabled: "bool"
    source: "PressureSource"
    metadata: "NotRequired[PressureMetadata]"





class SetPressureStateOverrideParameters(TypedDict):
    source: "PressureSource"
    state: "PressureState"





class SetPressureDataOverrideParameters(TypedDict):
    source: "PressureSource"
    state: "PressureState"
    ownContributionEstimate: "NotRequired[float]"





class SetIdleOverrideParameters(TypedDict):
    isUserActive: "bool"
    """Mock isUserActive"""
    isScreenUnlocked: "bool"
    """Mock isScreenUnlocked"""





class SetNavigatorOverridesParameters(TypedDict):
    platform: "str"
    """The platform navigator.platform should return."""





class SetPageScaleFactorParameters(TypedDict):
    pageScaleFactor: "float"
    """Page scale factor."""





class SetScriptExecutionDisabledParameters(TypedDict):
    value: "bool"
    """Whether script execution should be disabled in the page."""





class SetTouchEmulationEnabledParameters(TypedDict):
    enabled: "bool"
    """Whether the touch event emulation should be enabled."""
    maxTouchPoints: "NotRequired[int]"
    """Maximum touch points supported. Defaults to one."""





class SetVirtualTimePolicyParameters(TypedDict):
    policy: "VirtualTimePolicy"
    budget: "NotRequired[float]"
    """If set, after this many virtual milliseconds have elapsed virtual time will be paused and a
virtualTimeBudgetExpired event is sent."""
    maxVirtualTimeTaskStarvationCount: "NotRequired[int]"
    """If set this specifies the maximum number of tasks that can be run before virtual is forced
forwards to prevent deadlock."""
    initialVirtualTime: "NotRequired[TimeSinceEpoch]"
    """If set, base::Time::Now will be overridden to initially return this value."""


class SetVirtualTimePolicyReturns(TypedDict):
    virtualTimeTicksBase: "float"
    """Absolute timestamp at which virtual time was first enabled (up time in milliseconds)."""



class SetLocaleOverrideParameters(TypedDict, total=False):
    locale: "str"
    """ICU style C locale (e.g. \"en_US\"). If not specified or empty, disables the override and
restores default host system locale."""





class SetTimezoneOverrideParameters(TypedDict):
    timezoneId: "str"
    """The timezone identifier. List of supported timezones:
https://source.chromium.org/chromium/chromium/deps/icu.git/+/faee8bc70570192d82d2978a71e2a615788597d1:source/data/misc/metaZones.txt
If empty, disables the override and restores default host system timezone."""





class SetVisibleSizeParameters(TypedDict):
    width: "int"
    """Frame width (DIP)."""
    height: "int"
    """Frame height (DIP)."""





class SetDisabledImageTypesParameters(TypedDict):
    imageTypes: "List[DisabledImageType]"
    """Image types to disable."""





class SetHardwareConcurrencyOverrideParameters(TypedDict):
    hardwareConcurrency: "int"
    """Hardware concurrency to report"""





class SetUserAgentOverrideParameters(TypedDict):
    userAgent: "str"
    """User agent to use."""
    acceptLanguage: "NotRequired[str]"
    """Browser language to emulate."""
    platform: "NotRequired[str]"
    """The platform navigator.platform should return."""
    userAgentMetadata: "NotRequired[UserAgentMetadata]"
    """To be sent in Sec-CH-UA-* headers and returned in navigator.userAgentData"""





class SetAutomationOverrideParameters(TypedDict):
    enabled: "bool"
    """Whether the override should be enabled."""





class SetSmallViewportHeightDifferenceOverrideParameters(TypedDict):
    difference: "int"
    """This will cause an element of size 100svh to be `difference` pixels smaller than an element
of size 100lvh."""


