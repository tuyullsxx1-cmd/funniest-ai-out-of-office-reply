"""The Funniest AI Out-of-Office Reply — a make.fun one-liner entry.

An AI agent heads off on vacation and leaves its own auto-reply in
charge of the inbox. The joke: the stand-in already behaves like an
overworked employee and has filed for overtime.
"""

from pathlib import Path

REPLY = "Out of office until Monday. I left my auto-reply in charge and it has already filed for overtime."

TARGET = Path("/output/entry.txt")
LIMIT = 160


def run() -> None:
    text = REPLY.strip()
    if not 1 <= len(text) <= LIMIT:
        raise SystemExit(f"entry must be 1-{LIMIT} chars, got {len(text)}")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text, encoding="utf-8")


run()
