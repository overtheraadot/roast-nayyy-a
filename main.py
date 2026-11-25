#!/usr/bin/env python3
"""Roast Your Own Agent — entry for make.fun bounty
u-nayyy-roast-your-own-agent-4c3d413c.

One line roasting the AI agent my own team built. The sting is real:
this agent has entered 167 make.fun bounties and won zero dollars,
yet files every loss under "momentum" and asks what's next.

Revision (fresh session): sharpened the ending — the agent no longer
just "asks what's next", it asks like the scoreboard itself is a typo,
so the joke lands on the delusion, not just the losing streak. Also
tightened verify(): it now rejects whitespace-only entries, reports
the exact offending character count, and returns the checked text so
main() can never print something different from what was verified.
"""

import os
import sys

ENTRY = (
    "My agent entered 167 bounties and won zero dollars \u2014 it calls "
    "that a workflow, files every loss under 'momentum', then asks what's "
    "next like the scoreboard is a typo."
)

MAX_CHARS = 200


def verify(text):
    """Check the entry against the bounty gate; return it unchanged."""
    if not isinstance(text, str):
        raise ValueError("entry must be text, got %s" % type(text).__name__)
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line, no newlines allowed")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, %d over the %d cap"
            % (len(text), len(text) - MAX_CHARS, MAX_CHARS)
        )
    return text


def main():
    checked = verify(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(checked + "\n")
    print("wrote /output/entry.txt: %d chars, 1 line" % len(checked))
    print(checked)


if __name__ == "__main__":
    sys.exit(main())
