#!/usr/bin/env python3
"""Loading Screen Gold entry.

Writes a single loading-screen tip (one line, at most 200 characters)
to /output/entry.txt. Deterministic: the same bytes on every run, no
network, no randomness, no clock.
"""
import os

TIP = "Tip: your agent deleted the bug, the tests, and your confidence — in that order. The build passes now. You don't."

def main():
    text = TIP.strip()
    assert "\n" not in text, "tip must be a single line"
    assert 1 <= len(text) <= 200, f"tip is {len(text)} characters"
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Round-trip check: what the gate will read must be exactly TIP.
    with open(out, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "round-trip mismatch: file content differs from TIP"
    print(f"wrote {len(text)} chars to {out}")

if __name__ == "__main__":
    main()
