# SEC EDGAR API: examples and guides

Get what is inside SEC filings as clean data: the Risk Factors of a 10-K as Markdown, financial statements as tidy numbers, insider trades as rows, a fund's 13F portfolio. By ticker, with no API key.

This repository contains runnable examples and how-to guides for the **[SEC EDGAR API on Apify](https://apify.com/codepulsehq/sec-edgar-api)**, made by [CodePulse](https://codepulsehq.com). The examples call that hosted Actor, so you need a free [Apify](https://apify.com) account and API token. The code here is MIT licensed; the Actor is a paid, hosted service. From $0.0004 per filing listed, $0.005 per company's financials, $0.002 per insider filing, $0.01 per 10-K converted to Markdown or per 13F.

**Read the guides as a website:** [codepulsehq.github.io/sec-edgar-api](https://codepulsehq.github.io/sec-edgar-api/)

## Quick start

```bash
export APIFY_TOKEN=...   # free Apify account: Console > Settings > API & Integrations

curl -sS -X POST \
  "https://api.apify.com/v2/acts/codepulsehq~sec-edgar-api/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"companies": ["AAPL"], "dataType": "filing_text", "sections": ["1A"], "maxCharsPerSection": 20000}'
```

## Guides

| Question | Guide |
|---|---|
| How to get the Risk Factors section of a 10-K as clean text for an LLM | [docs/get-10k-risk-factors-as-text.md](docs/get-10k-risk-factors-as-text.md) |
| How to get SEC financial statements as structured data | [docs/sec-financial-statements-api.md](docs/sec-financial-statements-api.md) |
| How to track insider trading (SEC Form 4) programmatically | [docs/track-insider-trading-form-4.md](docs/track-insider-trading-form-4.md) |
| How to get a fund's 13F holdings through an API | [docs/get-13f-holdings-api.md](docs/get-13f-holdings-api.md) |

## Examples

| File | What it does |
|---|---|
| [`examples/curl/quickstart.sh`](examples/curl/quickstart.sh) | One request, results back |
| [`examples/python/quickstart.py`](examples/python/quickstart.py) | The same with the Apify Python client, with a spend cap |

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

## Feedback

Found a problem or want an example added? Open an issue here, or use the **Issues** tab on the Actor's Apify page.
