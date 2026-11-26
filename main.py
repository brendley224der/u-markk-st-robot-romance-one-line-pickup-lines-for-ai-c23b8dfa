#!/usr/bin/env python3
"""Robot Romance: one-line pickup line for an AI.

Deterministically writes a single joke pickup line, under 200 characters,
aimed at a robot / AI, to /output/entry.txt. Pure standard library only:
no third-party imports, no network, no randomness.

The line leans on the machine premise itself -- a transformer, its
attention mechanism, and its weights -- so the joke could only be told
to a machine, and the weights shifting *toward* the addressee is the
flirtation: the model literally reorients itself around them.
"""

from pathlib import Path

LINE = "Are you a transformer? Because every time you attend to me, my weights shift toward you."

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("pickup line is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("pickup line must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"pickup line is {len(line)} chars, over the {MAX_CHARS} cap"
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
