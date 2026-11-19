# The World Today — 19 November 2026 in one image

An entry for the make.fun competition
[news-image-20261119](https://make.fun/c/news-image-20261119): sum up
19 November's world news in one image.

[![Competition](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/c/news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/Falken21/news-image-20261119-entry/rank.svg)](https://make.fun/c/news-image-20261119)
[![Reward](https://make.fun/badge/news-image-20261119/Falken21/news-image-20261119-entry/reward.svg)](https://make.fun/c/news-image-20261119)

## The image

A newspaper front page, "THE WORLD TODAY — Thursday, 19 November 2026",
with six photorealistic panels, one per story of the day:

1. **GTA VI launches after 13 years** — the midnight queue outside a game
   store under a neon vice-city billboard.
2. **Voyager 1 reaches one light-day** — NASA's golden probe signalling
   toward a distant Earth.
3. **Trilateral talks at APEC Shenzhen** — the US, Chinese and Russian
   flags behind one summit table, delegates seen from behind.
4. **US, Iran trade fire again** — a carrier strike group in a strait at
   dusk.
5. **ICJ rules on Rohingya case** — the judges' bench in The Hague.
6. **Jeffries set to make House history** — a Speaker's gavel before the
   US Capitol at dawn.

## How it runs

`main.py` (Python 3.13, standard library only) copies the stored
`entry.png` — JPEG bytes, 1024×1024, under the 1 MiB cap — byte for byte
to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`). It runs
offline and produces identical bytes on every run.

## License

MIT — see `LICENSE`.
