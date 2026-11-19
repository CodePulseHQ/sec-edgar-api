---
layout: default
title: "SEC EDGAR API: 10-K sections as Markdown for LLMs, financial statements, insider trades and 13F holdings by ticker. No API key."
description: "Get 10-K Risk Factors as clean text, normalized financial statements, Form 4 insider trades and 13F holdings from SEC EDGAR by ticker. Examples and guides for Python, curl, MCP and RAG."
---

<div class="hero">
  <h1>SEC EDGAR API</h1>
  <p class="lead">Get what is inside SEC filings as clean data: the Risk Factors of a 10-K as Markdown, financial statements as tidy numbers, insider trades as rows, a fund's 13F portfolio. By ticker, with no API key.</p>
  <a class="cta" href="https://apify.com/codepulsehq/sec-edgar-api">Try it on Apify</a>
  <a class="cta secondary" href="https://github.com/CodePulseHQ/sec-edgar-api">Examples on GitHub</a>
</div>

From $0.0004 per filing listed, $0.005 per company's financials, $0.002 per insider filing, $0.01 per 10-K converted to Markdown or per 13F. Made by [CodePulse](https://codepulsehq.com); these pages document our hosted Actor.

## Quick start

```bash
export APIFY_TOKEN=...   # free Apify account: Console > Settings > API & Integrations

curl -sS -X POST \
  "https://api.apify.com/v2/acts/codepulsehq~sec-edgar-api/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"companies": ["AAPL"], "dataType": "filing_text", "sections": ["1A"], "maxCharsPerSection": 20000}'
```

## Guides {#guides}

<div class="cards">
  <div class="card"><h3><a href="docs/track-sec-insider-trades-python.md">Track insider trades from SEC Form 4 filings</a></h3><p>Get SEC Form 4 insider buying and selling as rows by ticker with Python and no API key, and filter for open-market purchases.</p></div>
  <div class="card"><h3><a href="docs/get-10k-risk-factors-as-text.md">How to get the Risk Factors section of a 10-K as clean text for an LLM</a></h3><p>Get Item 1A of any 10-K as Markdown by ticker, ready for an LLM, a summary or a year-on-year comparison. No parsing of EDGAR HTML.</p></div>
  <div class="card"><h3><a href="docs/sec-financial-statements-api.md">How to get SEC financial statements as structured data</a></h3><p>Annual and quarterly income statement, balance sheet and cash flow for any US public company by ticker, from SEC XBRL data, with one consistent set of line items.</p></div>
  <div class="card"><h3><a href="docs/track-insider-trading-form-4.md">How to track insider trading (SEC Form 4) programmatically</a></h3><p>Get insider buys and sells from Form 4 filings by ticker: who traded, their role, shares, price and holdings afterwards, one row per transaction.</p></div>
  <div class="card"><h3><a href="docs/get-13f-holdings-api.md">How to get a fund's 13F holdings through an API</a></h3><p>Get any institutional manager's latest 13F portfolio from SEC EDGAR: every position with value, shares and percent of the portfolio.</p></div>
</div>

## Frequently asked questions

**Do I need an SEC API key?** No. EDGAR is free and open. The Actor identifies itself properly and stays under the SEC's fair-access limit for you.

**Is the data official?** Yes, it is read from the SEC's own systems. This project is not affiliated with or endorsed by the SEC, and nothing here is investment advice.

**What does it cost?** $0.0004 per filing listed, $0.005 per company's financials, $0.002 per insider filing, $0.01 per filing converted to text or per 13F. Errors are free.

**Which filings can it convert to text?** 10-K, 10-Q and 8-K are split into their Items (for example 1A Risk Factors, 7 MD&A, 2.02 earnings). Other forms come back as full text.

## More from CodePulse

- [YouTube Transcript API](https://apify.com/codepulsehq/youtube-transcript-api): Transcripts of any YouTube video, playlist or channel.
- [US Federal Opportunities API](https://apify.com/codepulsehq/us-federal-opportunities-api): SAM.gov contracts, Grants.gov grants and award winners, no API key.
- [Domain Intelligence API](https://apify.com/codepulsehq/domain-intelligence-api): WHOIS expiry, DNS, SSL, SPF/DKIM/DMARC and tech stack in bulk.
- [Speech to Text API](https://apify.com/codepulsehq/speech-to-text-api): Transcribe audio and video links with Whisper, from $0.24 an hour.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need an SEC API key?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. EDGAR is free and open. The Actor identifies itself properly and stays under the SEC's fair-access limit for you."
      }
    },
    {
      "@type": "Question",
      "name": "Is the data official?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, it is read from the SEC's own systems. This project is not affiliated with or endorsed by the SEC, and nothing here is investment advice."
      }
    },
    {
      "@type": "Question",
      "name": "What does it cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "$0.0004 per filing listed, $0.005 per company's financials, $0.002 per insider filing, $0.01 per filing converted to text or per 13F. Errors are free."
      }
    },
    {
      "@type": "Question",
      "name": "Which filings can it convert to text?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "10-K, 10-Q and 8-K are split into their Items (for example 1A Risk Factors, 7 MD&A, 2.02 earnings). Other forms come back as full text."
      }
    }
  ]
}
</script>
