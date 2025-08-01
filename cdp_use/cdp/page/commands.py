# This file is auto-generated by the CDP protocol generator.
# Do not edit this file manually as your changes will be overwritten.
# Generated from Chrome DevTools Protocol specifications.

"""CDP Page Domain Commands"""

from typing import Any, List
from typing_extensions import NotRequired, TypedDict

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..debugger.types import SearchMatch
    from ..dom.types import NodeId
    from ..dom.types import Rect
    from ..emulation.types import ScreenOrientation
    from ..io.types import StreamHandle
    from ..network.types import LoaderId
    from ..runtime.types import ExecutionContextId
    from .types import AdScriptId
    from .types import AppManifestError
    from .types import AppManifestParsedProperties
    from .types import AutoResponseMode
    from .types import CompilationCacheParams
    from .types import FontFamilies
    from .types import FontSizes
    from .types import FrameId
    from .types import FrameResourceTree
    from .types import FrameTree
    from .types import InstallabilityError
    from .types import LayoutViewport
    from .types import NavigationEntry
    from .types import OriginTrial
    from .types import PermissionsPolicyFeatureState
    from .types import ReferrerPolicy
    from .types import ScriptFontFamilies
    from .types import ScriptIdentifier
    from .types import TransitionType
    from .types import Viewport
    from .types import VisualViewport
    from .types import WebAppManifest

class AddScriptToEvaluateOnLoadParameters(TypedDict):
    scriptSource: "str"


class AddScriptToEvaluateOnLoadReturns(TypedDict):
    identifier: "ScriptIdentifier"
    """Identifier of the added script."""



class AddScriptToEvaluateOnNewDocumentParameters(TypedDict):
    source: "str"
    worldName: "NotRequired[str]"
    """If specified, creates an isolated world with the given name and evaluates given script in it.
This world name will be used as the ExecutionContextDescription::name when the corresponding
event is emitted."""
    includeCommandLineAPI: "NotRequired[bool]"
    """Specifies whether command line API should be available to the script, defaults
to false."""
    runImmediately: "NotRequired[bool]"
    """If true, runs the script immediately on existing execution contexts or worlds.
Default: false."""


class AddScriptToEvaluateOnNewDocumentReturns(TypedDict):
    identifier: "ScriptIdentifier"
    """Identifier of the added script."""



class CaptureScreenshotParameters(TypedDict, total=False):
    format: "str"
    """Image compression format (defaults to png)."""
    quality: "int"
    """Compression quality from range [0..100] (jpeg only)."""
    clip: "Viewport"
    """Capture the screenshot of a given region only."""
    fromSurface: "bool"
    """Capture the screenshot from the surface, rather than the view. Defaults to true."""
    captureBeyondViewport: "bool"
    """Capture the screenshot beyond the viewport. Defaults to false."""
    optimizeForSpeed: "bool"
    """Optimize image encoding for speed, not for resulting size (defaults to false)"""


class CaptureScreenshotReturns(TypedDict):
    data: "Any"
    """Base64-encoded image data."""



class CaptureSnapshotParameters(TypedDict, total=False):
    format: "str"
    """Format (defaults to mhtml)."""


class CaptureSnapshotReturns(TypedDict):
    data: "str"
    """Serialized page data."""



class CreateIsolatedWorldParameters(TypedDict):
    frameId: "FrameId"
    """Id of the frame in which the isolated world should be created."""
    worldName: "NotRequired[str]"
    """An optional name which is reported in the Execution Context."""
    grantUniveralAccess: "NotRequired[bool]"
    """Whether or not universal access should be granted to the isolated world. This is a powerful
option, use with caution."""


class CreateIsolatedWorldReturns(TypedDict):
    executionContextId: "ExecutionContextId"
    """Execution context of the isolated world."""



class DeleteCookieParameters(TypedDict):
    cookieName: "str"
    """Name of the cookie to remove."""
    url: "str"
    """URL to match cooke domain and path."""





class EnableParameters(TypedDict, total=False):
    enableFileChooserOpenedEvent: "bool"
    """If true, the `Page.fileChooserOpened` event will be emitted regardless of the state set by
`Page.setInterceptFileChooserDialog` command (default: false)."""





class GetAppManifestParameters(TypedDict, total=False):
    manifestId: "str"


class GetAppManifestReturns(TypedDict):
    url: "str"
    """Manifest location."""
    errors: "List[AppManifestError]"
    data: "str"
    """Manifest content."""
    parsed: "AppManifestParsedProperties"
    """Parsed manifest properties. Deprecated, use manifest instead."""
    manifest: "WebAppManifest"



class GetInstallabilityErrorsReturns(TypedDict):
    installabilityErrors: "List[InstallabilityError]"



class GetManifestIconsReturns(TypedDict):
    primaryIcon: "Any"



class GetAppIdReturns(TypedDict):
    appId: "str"
    """App id, either from manifest's id attribute or computed from start_url"""
    recommendedId: "str"
    """Recommendation for manifest's id attribute to match current id computed from start_url"""



class GetAdScriptAncestryIdsParameters(TypedDict):
    frameId: "FrameId"


class GetAdScriptAncestryIdsReturns(TypedDict):
    adScriptAncestryIds: "List[AdScriptId]"
    """The ancestry chain of ad script identifiers leading to this frame's
creation, ordered from the most immediate script (in the frame creation
stack) to more distant ancestors (that created the immediately preceding
script). Only sent if frame is labelled as an ad and ids are available."""



class GetFrameTreeReturns(TypedDict):
    frameTree: "FrameTree"
    """Present frame tree structure."""



class GetLayoutMetricsReturns(TypedDict):
    layoutViewport: "LayoutViewport"
    """Deprecated metrics relating to the layout viewport. Is in device pixels. Use `cssLayoutViewport` instead."""
    visualViewport: "VisualViewport"
    """Deprecated metrics relating to the visual viewport. Is in device pixels. Use `cssVisualViewport` instead."""
    contentSize: "Rect"
    """Deprecated size of scrollable area. Is in DP. Use `cssContentSize` instead."""
    cssLayoutViewport: "LayoutViewport"
    """Metrics relating to the layout viewport in CSS pixels."""
    cssVisualViewport: "VisualViewport"
    """Metrics relating to the visual viewport in CSS pixels."""
    cssContentSize: "Rect"
    """Size of scrollable area in CSS pixels."""



class GetNavigationHistoryReturns(TypedDict):
    currentIndex: "int"
    """Index of the current navigation history entry."""
    entries: "List[NavigationEntry]"
    """Array of navigation history entries."""



class GetResourceContentParameters(TypedDict):
    frameId: "FrameId"
    """Frame id to get resource for."""
    url: "str"
    """URL of the resource to get content for."""


class GetResourceContentReturns(TypedDict):
    content: "str"
    """Resource content."""
    base64Encoded: "bool"
    """True, if content was served as base64."""



class GetResourceTreeReturns(TypedDict):
    frameTree: "FrameResourceTree"
    """Present frame / resource tree structure."""



class HandleJavaScriptDialogParameters(TypedDict):
    accept: "bool"
    """Whether to accept or dismiss the dialog."""
    promptText: "NotRequired[str]"
    """The text to enter into the dialog prompt before accepting. Used only if this is a prompt
dialog."""





class NavigateParameters(TypedDict):
    url: "str"
    """URL to navigate the page to."""
    referrer: "NotRequired[str]"
    """Referrer URL."""
    transitionType: "NotRequired[TransitionType]"
    """Intended transition type."""
    frameId: "NotRequired[FrameId]"
    """Frame id to navigate, if not specified navigates the top frame."""
    referrerPolicy: "NotRequired[ReferrerPolicy]"
    """Referrer-policy used for the navigation."""


class NavigateReturns(TypedDict):
    frameId: "FrameId"
    """Frame id that has navigated (or failed to navigate)"""
    loaderId: "LoaderId"
    """Loader identifier. This is omitted in case of same-document navigation,
as the previously committed loaderId would not change."""
    errorText: "str"
    """User friendly error message, present if and only if navigation has failed."""



class NavigateToHistoryEntryParameters(TypedDict):
    entryId: "int"
    """Unique id of the entry to navigate to."""





class PrintToPDFParameters(TypedDict, total=False):
    landscape: "bool"
    """Paper orientation. Defaults to false."""
    displayHeaderFooter: "bool"
    """Display header and footer. Defaults to false."""
    printBackground: "bool"
    """Print background graphics. Defaults to false."""
    scale: "float"
    """Scale of the webpage rendering. Defaults to 1."""
    paperWidth: "float"
    """Paper width in inches. Defaults to 8.5 inches."""
    paperHeight: "float"
    """Paper height in inches. Defaults to 11 inches."""
    marginTop: "float"
    """Top margin in inches. Defaults to 1cm (~0.4 inches)."""
    marginBottom: "float"
    """Bottom margin in inches. Defaults to 1cm (~0.4 inches)."""
    marginLeft: "float"
    """Left margin in inches. Defaults to 1cm (~0.4 inches)."""
    marginRight: "float"
    """Right margin in inches. Defaults to 1cm (~0.4 inches)."""
    pageRanges: "str"
    """Paper ranges to print, one based, e.g., '1-5, 8, 11-13'. Pages are
printed in the document order, not in the order specified, and no
more than once.
Defaults to empty string, which implies the entire document is printed.
The page numbers are quietly capped to actual page count of the
document, and ranges beyond the end of the document are ignored.
If this results in no pages to print, an error is reported.
It is an error to specify a range with start greater than end."""
    headerTemplate: "str"
    """HTML template for the print header. Should be valid HTML markup with following
classes used to inject printing values into them:
- `date`: formatted print date
- `title`: document title
- `url`: document location
- `pageNumber`: current page number
- `totalPages`: total pages in the document

For example, `<span class=title></span>` would generate span containing the title."""
    footerTemplate: "str"
    """HTML template for the print footer. Should use the same format as the `headerTemplate`."""
    preferCSSPageSize: "bool"
    """Whether or not to prefer page size as defined by css. Defaults to false,
in which case the content will be scaled to fit the paper size."""
    transferMode: "str"
    """return as stream"""
    generateTaggedPDF: "bool"
    """Whether or not to generate tagged (accessible) PDF. Defaults to embedder choice."""
    generateDocumentOutline: "bool"
    """Whether or not to embed the document outline into the PDF."""


class PrintToPDFReturns(TypedDict):
    data: "Any"
    """Base64-encoded pdf data. Empty if |returnAsStream| is specified."""
    stream: "StreamHandle"
    """A handle of the stream that holds resulting PDF data."""



class ReloadParameters(TypedDict, total=False):
    ignoreCache: "bool"
    """If true, browser cache is ignored (as if the user pressed Shift+refresh)."""
    scriptToEvaluateOnLoad: "str"
    """If set, the script will be injected into all frames of the inspected page after reload.
Argument will be ignored if reloading dataURL origin."""
    loaderId: "LoaderId"
    """If set, an error will be thrown if the target page's main frame's
loader id does not match the provided id. This prevents accidentally
reloading an unintended target in case there's a racing navigation."""





class RemoveScriptToEvaluateOnLoadParameters(TypedDict):
    identifier: "ScriptIdentifier"





class RemoveScriptToEvaluateOnNewDocumentParameters(TypedDict):
    identifier: "ScriptIdentifier"





class ScreencastFrameAckParameters(TypedDict):
    sessionId: "int"
    """Frame number."""





class SearchInResourceParameters(TypedDict):
    frameId: "FrameId"
    """Frame id for resource to search in."""
    url: "str"
    """URL of the resource to search in."""
    query: "str"
    """String to search for."""
    caseSensitive: "NotRequired[bool]"
    """If true, search is case sensitive."""
    isRegex: "NotRequired[bool]"
    """If true, treats string parameter as regex."""


class SearchInResourceReturns(TypedDict):
    result: "List[SearchMatch]"
    """List of search matches."""



class SetAdBlockingEnabledParameters(TypedDict):
    enabled: "bool"
    """Whether to block ads."""





class SetBypassCSPParameters(TypedDict):
    enabled: "bool"
    """Whether to bypass page CSP."""





class GetPermissionsPolicyStateParameters(TypedDict):
    frameId: "FrameId"


class GetPermissionsPolicyStateReturns(TypedDict):
    states: "List[PermissionsPolicyFeatureState]"



class GetOriginTrialsParameters(TypedDict):
    frameId: "FrameId"


class GetOriginTrialsReturns(TypedDict):
    originTrials: "List[OriginTrial]"



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
    """The viewport dimensions and scale. If not set, the override is cleared."""





class SetDeviceOrientationOverrideParameters(TypedDict):
    alpha: "float"
    """Mock alpha"""
    beta: "float"
    """Mock beta"""
    gamma: "float"
    """Mock gamma"""





class SetFontFamiliesParameters(TypedDict):
    fontFamilies: "FontFamilies"
    """Specifies font families to set. If a font family is not specified, it won't be changed."""
    forScripts: "NotRequired[List[ScriptFontFamilies]]"
    """Specifies font families to set for individual scripts."""





class SetFontSizesParameters(TypedDict):
    fontSizes: "FontSizes"
    """Specifies font sizes to set. If a font size is not specified, it won't be changed."""





class SetDocumentContentParameters(TypedDict):
    frameId: "FrameId"
    """Frame id to set HTML for."""
    html: "str"
    """HTML content to set."""





class SetDownloadBehaviorParameters(TypedDict):
    behavior: "str"
    """Whether to allow all or deny all download requests, or use default Chrome behavior if
available (otherwise deny)."""
    downloadPath: "NotRequired[str]"
    """The default path to save downloaded files to. This is required if behavior is set to 'allow'"""





class SetGeolocationOverrideParameters(TypedDict, total=False):
    latitude: "float"
    """Mock latitude"""
    longitude: "float"
    """Mock longitude"""
    accuracy: "float"
    """Mock accuracy"""





class SetLifecycleEventsEnabledParameters(TypedDict):
    enabled: "bool"
    """If true, starts emitting lifecycle events."""





class SetTouchEmulationEnabledParameters(TypedDict):
    enabled: "bool"
    """Whether the touch event emulation should be enabled."""
    configuration: "NotRequired[str]"
    """Touch/gesture events configuration. Default: current platform."""





class StartScreencastParameters(TypedDict, total=False):
    format: "str"
    """Image compression format."""
    quality: "int"
    """Compression quality from range [0..100]."""
    maxWidth: "int"
    """Maximum screenshot width."""
    maxHeight: "int"
    """Maximum screenshot height."""
    everyNthFrame: "int"
    """Send every n-th frame."""





class SetWebLifecycleStateParameters(TypedDict):
    state: "str"
    """Target lifecycle state"""





class ProduceCompilationCacheParameters(TypedDict):
    scripts: "List[CompilationCacheParams]"





class AddCompilationCacheParameters(TypedDict):
    url: "str"
    data: "Any"
    """Base64-encoded data"""





class SetSPCTransactionModeParameters(TypedDict):
    mode: "AutoResponseMode"





class SetRPHRegistrationModeParameters(TypedDict):
    mode: "AutoResponseMode"





class GenerateTestReportParameters(TypedDict):
    message: "str"
    """Message to be displayed in the report."""
    group: "NotRequired[str]"
    """Specifies the endpoint group to deliver the report to."""





class SetInterceptFileChooserDialogParameters(TypedDict):
    enabled: "bool"
    cancel: "NotRequired[bool]"
    """If true, cancels the dialog by emitting relevant events (if any)
in addition to not showing it if the interception is enabled
(default: false)."""





class SetPrerenderingAllowedParameters(TypedDict):
    isAllowed: "bool"





class GeneratePageGraphReturns(TypedDict):
    data: "str"
    """Generated page graph GraphML."""



class GeneratePageGraphNodeReportParameters(TypedDict):
    nodeId: "NodeId"
    """Id of the element to report on."""


class GeneratePageGraphNodeReportReturns(TypedDict):
    report: "List[str]"
    """Generated report lines"""
