"""news-image-20261119 entry (final edition): copies the stored front-page
image to the output.

The repository holds the finished image as entry.png (JPEG bytes, detected
by magic bytes per the competition rules). This program copies it, byte for
byte, to entry.png inside $MAKEFUN_OUTPUT_DIR, or /output when the variable
is not set. Standard library only, no network, deterministic: two runs
produce identical bytes.

Final edition — "THE WORLD TODAY, Thursday 19 November 2026": six
photorealistic AI panels (no real press photographs) summarising the day's
news — the Trump-Xi-Putin three-way summit in Shenzhen; the ICJ genocide
ruling on Myanmar; the third strike on the Kerch bridge; Israeli tanks in
central Gaza; Iran's retaliation after the US strike on Qeshm; and
Anthropic's record $81bn IPO.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"stored image missing: {SOURCE}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    # The gate compares the two grading runs byte for byte, so fail loudly
    # here rather than hand it a short or empty file.
    if target.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit("copied image size mismatch")


if __name__ == "__main__":
    main()
