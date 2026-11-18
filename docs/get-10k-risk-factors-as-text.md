---
layout: default
title: "How to get the Risk Factors section of a 10-K as clean text for an LLM"
description: "Get Item 1A of any 10-K as Markdown by ticker, ready for an LLM, a summary or a year-on-year comparison. No parsing of EDGAR HTML."
---

# How to get the Risk Factors section of a 10-K as clean text for an LLM

**Short answer:** ask for the filing as sections. One request returns Item 1A (Risk Factors) of a company's latest 10-K as Markdown, with a character count and a rough token count, so you can feed it straight into a prompt or a vector database.

```bash
export APIFY_TOKEN=...   # free Apify account: Console > Settings > API & Integrations

curl -sS -X POST \
  "https://api.apify.com/v2/acts/codepulsehq~sec-edgar-api/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"companies": ["AAPL"], "dataType": "filing_text", "sections": ["1A"], "maxCharsPerSection": 20000}'
```

You get a row per filing with `sections[].markdown`, `characters`, `approx_tokens` and a `truncated` flag. Use `"sections": ["1", "1A", "7", "7A"]` for Business, Risk Factors, MD&A and market risk, or `["all"]` for every Item.

## Why this is harder than it looks

A 10-K on EDGAR is a single HTML (inline XBRL) document of several hundred thousand characters. Item headings aren't consistent between companies, the table of contents repeats every heading, and tables are split into cells (a dollar sign, a number and a bracket sit in separate cells). The Actor handles all of that: hidden XBRL headers are dropped, tables become Markdown tables with the numbers stitched back together, and for each Item it keeps the occurrence that spans the most text, so the table of contents isn't mistaken for the section.

## Doing it yourself

1. Look up the company's filings at `https://data.sec.gov/submissions/CIK##########.json` (a CIK padded to 10 digits). Send a `User-Agent` that names you and gives an email, and stay under 10 requests per second, or the SEC will block you.
2. Download the primary document of the latest 10-K from `https://www.sec.gov/Archives/edgar/data/<cik>/<accession-without-dashes>/<primary document>`.
3. Convert the HTML to text, then split on headings that start with "Item 1A", "Item 1B" and so on, ignoring the table of contents.

Step 3 is where most of the time goes.

## Tips

- **Compare years:** set `maxFilingsPerCompany` to 3 to get the last three annual reports and diff the Risk Factors.
- **Long sections:** Risk Factors often exceed 80,000 characters. Raise `maxCharsPerSection` (up to 400,000) or chunk the text for embedding.
- **Quarterly reports:** `"forms": ["10-Q"]` returns Part I and Part II items.

Ready-made pages: [10-K risk factors as text](https://apify.com/codepulsehq/sec-edgar-api/examples/get-10k-risk-factors-as-text) and [10-K sections for LLMs and RAG](https://apify.com/codepulsehq/sec-edgar-api/examples/sec-10k-sections-for-llms).
