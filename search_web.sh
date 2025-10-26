#!/usr/bin/env bash
TOKEN="TOKEN-UNICO-c68f2467-c94d-4c27-918c-c210f8321616"
GH="https://github.com/search?q=%22${TOKEN}%22&type=code"
GO="https://www.google.com/search?q=%22${TOKEN}%22"
if command -v open >/dev/null 2>&1; then open "$GH"; open "$GO"; else echo "$GH"; echo "$GO"; fi
