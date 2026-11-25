#!/usr/bin/env python3
"""Frost Best Advice — one sentence on the best advice ever received.

Writes a single 118-character sentence to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set). Stdlib only, no network.
"""

import os
import sys

LINE = (
    "Grandma said never trust a man who says 'trust me' — "
    "forty years later, every single one of them has proved her right."
)


def main() -> int:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        print(f"gate: line is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if text.count(".") > 1 or "\n" in text:
        print("gate: entry must be a single sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what landed on disk must be exactly the line.
    with open(path, encoding="utf-8") as f:
        if f.read() != text:
            print("gate: round-trip mismatch", file=sys.stderr)
            return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
