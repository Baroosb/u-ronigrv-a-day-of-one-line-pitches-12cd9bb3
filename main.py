"""Entry for make.fun bounty u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes the one-sentence pitch to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

TEXT = (
    "You don't need to learn code to try that app idea you've been carrying "
    "around — just describe it in plain words on make.fun and let an AI agent "
    "build a first version you can actually open and poke at."
)


def main():
    # The gate accepts 1..240 characters of UTF-8 text; keep the entry exact.
    assert 1 <= len(TEXT) <= 240, len(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
