#!/usr/bin/env bash
# Needs an Apify API token (free account): export APIFY_TOKEN=...
set -euo pipefail

curl -sS -X POST \
  "https://api.apify.com/v2/acts/codepulsehq~sec-edgar-api/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"companies": ["AAPL"], "dataType": "filing_text", "sections": ["1A"], "maxCharsPerSection": 20000}'
