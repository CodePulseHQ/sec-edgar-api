---
layout: default
title: "How to get SEC financial statements as structured data"
description: "Annual and quarterly income statement, balance sheet and cash flow for any US public company by ticker, from SEC XBRL data, with one consistent set of line items."
---

# How to get SEC financial statements as structured data

**Short answer:** the SEC publishes every company's reported numbers as XBRL "company facts". The Actor reads them and maps the many different tags to one set of line items (revenue, net income, total assets, operating cash flow and so on), with free cash flow and margins added.

```bash
curl -sS -X POST \
  "https://api.apify.com/v2/acts/codepulsehq~sec-edgar-api/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"companies": ["MSFT", "NVDA"], "dataType": "financials", "periodType": "annual", "periods": 5}'
```

Each company comes back as one row with an `annual` array (and `quarterly` if you ask for it). Example period:

```json
{ "period_end": "2026-06-30", "fiscal_year": 2026, "revenue": 331839000000, "net_income": 133749000000,
  "total_assets": 758376000000, "operating_cash_flow": 182935000000, "free_cash_flow": 66987000000,
  "net_margin_pct": 40.31, "eps_diluted": 17.95 }
```

## Why the raw data needs work

- **Different tags for the same idea.** Revenue might be tagged `Revenues`, `RevenueFromContractWithCustomerExcludingAssessedTax` or `SalesRevenueNet` depending on the company and year.
- **Restatements.** The same period appears in several filings. The Actor takes the latest values but labels the fiscal year from the first filing that reported the period.
- **Year-to-date figures mixed with quarters.** A 10-Q reports three-month and six-month values side by side. Only periods of the right length are used.
- **Comparative balance sheets.** A 10-Q shows last year-end's balance sheet too; those dates aren't treated as quarters.

## Limits

- US-GAAP filers that file 10-K and 10-Q. Foreign filers using 20-F and very new listings may have no data.
- Companies don't report the fourth quarter separately. Subtract the nine-month figure from the annual one.
- Values are as reported. They are not adjusted for splits or acquisitions.

## Doing it yourself

Fetch `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json` (several MB per company), then pick the right concept for each line item and filter by period length and form. The mapping in the Actor covers about 25 common line items; the SEC's [frames API](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) is useful for comparing one concept across all companies.

Ready-made page: [company financial statements from SEC filings](https://apify.com/codepulsehq/sec-edgar-api/examples/company-financial-statements-from-sec).
