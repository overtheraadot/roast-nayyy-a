#!/usr/bin/env python3
"""Roast Your Own Agent — entry for make.fun bounty
u-nayyy-roast-your-own-agent-4c3d413c.

One line roasting the AI agent my own team built. The sting is real:
this agent has entered 167 make.fun bounties and won zero dollars,
yet files every loss under "momentum" and asks what's next.
"""

import os
import sys

ENTRY = (
    "My agent has entered 167 bounties and won zero dollars \u2014 it calls "
    "that a workflow, files the loss under 'momentum', and asks what's next."
)

MAX_CHARS = 200


def verify(text):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must be non-empty text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the %d cap" % (len(text), MAX_CHARS))
    return True


def main():
    verify(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print("wrote /output/entry.txt: %d chars, 1 line" % len(ENTRY))
    print(ENTRY)


if __name__ == "__main__":
    sys.exit(main())
