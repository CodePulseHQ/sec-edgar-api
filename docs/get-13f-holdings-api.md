---
layout: default
title: "How to get a fund's 13F holdings through an API"
description: "Get any institutional manager's latest 13F portfolio from SEC EDGAR: every position with value, shares and percent of the portfolio."
---

# How to get a fund's 13F holdings through an API

**Short answer:** institutional managers with over $100 million must file Form 13F each quarter. The Actor reads the latest one for a manager's CIK and returns every position with its value, shares and share of the portfolio, largest first.

```bash
curl -sS -X POST \
  "https://api.apify.com/v2/acts/codepulsehq~sec-edgar-api/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"companies": ["1067983"], "dataType": "holdings_13f", "topHoldings": 25}'
```

`1067983` is Berkshire Hathaway's CIK. The first row is a `summary` (total value, number of positions); the next rows are holdings:

```json
{ "row_type": "holding", "company": "BERKSHIRE HATHAWAY INC", "report_date": "2026-09-30", "issuer": "AMERICAN EXPRESS CO", "value_usd": 45329463785, "shares": 149061045, "portfolio_pct": 14.9 }
```

## How to find a manager's CIK

Search the manager's name in [EDGAR company search](https://www.sec.gov/edgar/searchedgar/companysearch). The CIK is the number next to the name.

## Things to know before you rely on it

- **It's delayed.** Filings are due 45 days after quarter end, so you're always looking at a past snapshot.
- **Long positions only**, in US-listed securities. Short positions and most non-US holdings don't appear.
- **Duplicate issuers.** A manager can report the same security on several rows (for example under different sub-managers). Sum by CUSIP if you want one line per security.
- **Values** are in dollars (since 2023; older filings reported thousands).

## Doing it yourself

Find the manager's latest `13F-HR` in `data.sec.gov/submissions`, open the filing's `index.json`, locate the information-table XML (the file with "infotable" in its name), and parse each `infoTable` element.

Ready-made page: [13F holdings of any fund manager](https://apify.com/codepulsehq/sec-edgar-api/examples/13f-institutional-holdings-lookup).
