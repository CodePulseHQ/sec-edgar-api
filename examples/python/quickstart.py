"""SEC EDGAR API: quick start.

    pip install apify-client
    export APIFY_TOKEN=...
    python quickstart.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("codepulsehq/sec-edgar-api").call(
    max_total_charge_usd=1,  # never spend more than $1 on this run
    logger=None,  # quiet: do not stream the Actor log
    run_input={"companies": ["AAPL"], "dataType": "filing_text", "sections": ["1A"], "maxCharsPerSection": 20000},
)

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(json.dumps(item, indent=2)[:1500])
