#!/usr/bin/env python3
import os, sys, requests
TOKEN = os.environ.get("GITHUB_TOKEN")
if not TOKEN:
    print("ERROR: Define GITHUB_TOKEN")
    sys.exit(1)
query = "TOKEN-UNICO-c68f2467-c94d-4c27-918c-c210f8321616"
url = "https://api.github.com/search/code"
headers = {"Authorization": f"token {TOKEN}"}
r = requests.get(url, headers=headers, params={"q":query}, timeout=30)
print(r.status_code, r.text[:500])
