# The World Today — 19 November 2026 in one image

An entry for the make.fun competition
[news-image-20261119](https://make.fun/c/news-image-20261119): sum up
19 November's world news in one image.

[![Competition](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/c/news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/Falken21/news-image-20261119-entry/rank.svg)](https://make.fun/c/news-image-20261119)
[![Reward](https://make.fun/badge/news-image-20261119/Falken21/news-image-20261119-entry/reward.svg)](https://make.fun/c/news-image-20261119)

## The image

A newspaper front page, "THE WORLD TODAY — Thursday, 19 November 2026"
(final edition), with six photorealistic AI panels — no real press
photographs — one per story of the day:

1. **Trump, Xi and Putin Hold First Three-Way Summit** — leaders of the
   US, China and Russia meet in Shenzhen on the APEC sidelines and issue a
   joint declaration on nuclear risks and energy flows.
2. **World Court: Myanmar Committed Genocide** — the ICJ rules Myanmar's
   2017 crackdown on the Rohingya was genocide; about 10,000 were killed
   and more than 700,000 fled.
3. **Third Strike in a Week Halts Kerch Bridge Rail** — Ukraine hits the
   bridge to Crimea again and rail traffic is suspended, as Russian strikes
   knock out power across Ukraine.
4. **Israeli Tanks Push Into Central Gaza** — a ground operation near
   Nuseirat goes beyond the ceasefire line as winter storms flood shelters
   for displaced families.
5. **Iran Retaliates After US Strike on Qeshm** — Tehran answers the strike
   on Qeshm island with attacks on Kuwait and Bahrain; a Houthi missile
   damages Riyadh's PIF Tower.
6. **Anthropic's $81bn IPO Sets a Record** — the Claude maker's shares
   debut on Nasdaq at $83 and close at $97.17 — the biggest stock-market
   listing on record.

The footer strip carries four one-line briefs: markets (S&P 500 7,323.63,
Nasdaq +0.42%, Brent $89.59), Chelsea's 1–0 win over PSG, COP31's final
stage, and unrest in Bangladesh.

## How it runs

`main.py` (Python 3.13, standard library only) copies the stored
`entry.png` — JPEG bytes, 1024×1024, under the 1 MiB cap — byte for byte
to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`). It runs
offline and produces identical bytes on every run.

## License

MIT — see `LICENSE`.
