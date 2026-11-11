import json
import os
import sys
import urllib.request

status = sys.argv[1]
icon = "✅" if status == "SUCCESS" else "❌"
text = (f"{icon} **{os.environ.get('JOB_NAME')}** build "
        f"#{os.environ.get('BUILD_NUMBER')}: **{status}**\n\n"
        f"{os.environ.get('BUILD_URL')}")

req = urllib.request.Request(
    "https://webexapis.com/v1/messages",
    data=json.dumps({"roomId": os.environ["WEBEX_ROOM"], "markdown": text}).encode(),
    headers={
        "Authorization": "Bearer " + os.environ["WEBEX_TOKEN"],
        "Content-Type": "application/json",
    },
)
print("Webex response:", urllib.request.urlopen(req).status)
