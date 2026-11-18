---
layout: default
title: "How to track insider trading (SEC Form 4) programmatically"
description: "Get insider buys and sells from Form 4 filings by ticker: who traded, their role, shares, price and holdings afterwards, one row per transaction."
---

# How to track insider trading (SEC Form 4) programmatically

**Short answer:** Form 4 is the filing company insiders must submit within two business days of trading their company's stock. The Actor parses each Form 4 into one row per transaction, with the insider's role, shares, price and shares owned afterwards.

```bash
curl -sS -X POST \
  "https://api.apify.com/v2/acts/codepulsehq~sec-edgar-api/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"companies": ["NVDA"], "dataType": "insider_trades", "maxFilingsPerCompany": 20}'
```

```json
{ "ticker": "NVDA", "owners": ["Teter Timothy S."], "transaction_date": "2026-09-23", "transaction_type": "Open-market sale",
  "shares": 12483, "price_per_share": 222.19, "shares_owned_after": 2705637, "owner_details": [{ "title": "EVP, General Counsel and Secretary" }] }
```

## What the transaction codes mean

| Code | Meaning | Worth watching? |
|---|---|---|
| P | Open-market purchase | Yes: an insider spending their own money |
| S | Open-market sale | Often routine, but large or clustered sales can matter |
| A | Grant or award | Compensation, not a trade decision |
| M | Exercise or conversion of a derivative | Often followed by a sale |
| F | Shares withheld to pay tax or exercise price | Mechanical |
| G | Gift | Usually estate or charity planning |
| D | Sale back to the issuer | Mechanical |

Each row carries `transaction_type` in plain English so you can filter out the mechanical ones.

## Doing it yourself

List a company's recent filings of form `4` from `data.sec.gov/submissions`, then for each filing fetch the raw XML next to the rendered HTML (the `primaryDocument` path starts with an `xslF345` folder you must strip) and parse `nonDerivativeTransaction` and `derivativeTransaction` blocks. Send an identifying User-Agent and stay under 10 requests per second.

## Limits

- Form 4 only; Forms 3 and 5 aren't included.
- A filing can cover several insiders and many transactions; each transaction is its own row.
- Planned-sale (10b5-1) flags aren't extracted.

Ready-made page: [insider trading tracker (Form 4)](https://apify.com/codepulsehq/sec-edgar-api/examples/insider-trading-form-4-tracker).
