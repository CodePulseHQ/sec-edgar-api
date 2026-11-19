---
layout: default
title: "Track insider buying and selling from SEC Form 4 filings (Python, no API key)"
description: "Get SEC Form 4 insider buying and selling as rows by ticker with Python and no API key, and filter for open-market purchases."
---

When executives buy or sell their own company's stock, they have to report it to the SEC within two business days on a Form 4. It's public, free and sometimes interesting. The catch is that Form 4s are XML files you have to find, download and parse.

This post gets them as rows with one call, by ticker.

*Information only, not investment advice.*

## Get recent insider trades

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("codepulsehq/sec-edgar-api").call(run_input={
    "dataType": "insider_trades",
    "companies": ["NVDA", "AAPL"],
    "maxFilingsPerCompany": 20,
})
trades = list(client.dataset(run.default_dataset_id).iterate_items())
for t in trades[:10]:
    if t.get("success") is False:
        continue
    print(t["ticker"], t["transaction_date"], ", ".join(t["owners"]), t["transaction_type"],
          t["shares"], "@", t["price_per_share"])
```

`maxFilingsPerCompany` counts filings, and one filing can hold several transactions, so you may get more rows than that. Each row is one transaction: who, when, buy or sell, shares, price and how many shares they hold afterwards. A transaction can be a routine tax withholding or a scheduled plan sale, so look at the type before reading meaning into it.

## Only open-market buys

Insiders sell for many reasons, but they usually buy for one. Filter the rows yourself:

```python
buys = [t for t in trades if t.get("success") is not False
        and "purchase" in (t.get("transaction_type") or "").lower()]
```

`transaction_type` is plain English, for example "Open-market sale", "Open-market purchase" or "Gift". Print the distinct values for your companies first and adjust the filter to match.

## Run it every morning

Create a saved Task in Apify with the input above and give it a daily schedule, then add a webhook or the email integration for the results. Or run the script from cron. At $0.002 per filing, a 20-company watchlist costs a few cents a day.

## Other things from the same Actor

- `"dataType": "financials"`: annual and quarterly statements by ticker.
- `"dataType": "filing_text"`: sections of a 10-K as Markdown (for example `"sections": ["1A"]` for Risk Factors).
- `"dataType": "holdings_13f"`: a fund's portfolio.

Everything comes from the SEC's own EDGAR system, and the Actor stays within the SEC's rate limit for you.

Actor page: <https://apify.com/codepulsehq/sec-edgar-api> - guides: <https://codepulsehq.github.io/sec-edgar-api/>
