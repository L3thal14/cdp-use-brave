import asyncio
import logging
import json
import httpx

from cdp_use.client import CDPClient

# Configure logging to see what's happening
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


async def main():
    # Get WebSocket URL using async HTTPX
    async with httpx.AsyncClient() as client:
        version_info = await client.get("http://localhost:9222/json/version")
        browser_ws_url = version_info.json()["webSocketDebuggerUrl"]
    # browser_ws_url = "ws://localhost:3000"

    # Connect to Chrome DevTools with type-safe CDP client
    async with CDPClient(browser_ws_url) as cdp:
        # List all targets (tabs, extensions, etc.) - fully type-safe!
        targets_result = await cdp.send.Target.getTargets()
        page_targets = [t for t in targets_result["targetInfos"] if t["type"] == "page"]

        if not page_targets:
            raise RuntimeError("No page targets found.")

        target_id = page_targets[0]["targetId"]

        print(target_id, targets_result)

        # Attach to selected tab
        attach_result = await cdp.send.Target.attachToTarget(
            params={"targetId": target_id, "flatten": True}
        )
        session_id = attach_result["sessionId"]

        # Enable DOM domain
        await cdp.send.DOM.enable(session_id=session_id)

        await cdp.send.Page.navigate(
            params={"url": "https://www.google.com"}, session_id=session_id
        )

        # Get full DOM tree
        dom_result = await cdp.send.DOM.getDocument(
            params={"depth": -1, "pierce": True}, session_id=session_id
        )

        ax_tree = await cdp.send.Accessibility.getFullAXTree(
            params={}, session_id=session_id
        )
        print(ax_tree)

        print("Root node ID:", dom_result["root"]["nodeId"])

        # Execute 10 concurrent CDP requests with full type safety
        tasks = [
            cdp.send.DOM.getDocument(
                params={"depth": -1, "pierce": True}, session_id=session_id
            )
            for _ in range(10)
        ]
        results = await asyncio.gather(*tasks)
        print(len(results))
        await asyncio.sleep(10)
        pagegraph_result = await cdp.send.Page.generatePageGraph(session_id=session_id)
        with open("brave_pagegraph.graphml", "w") as f:
            json.dump(pagegraph_result['data'], f)
        # print(results[-1])


asyncio.run(main())