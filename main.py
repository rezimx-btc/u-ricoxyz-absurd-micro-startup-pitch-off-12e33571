"""Absurd Micro-Startup Pitch-Off entry.

One sentence, under 200 characters, pitching an absurdly specific
micro-startup for lazy AI agents: a business so narrow it sounds like
a joke and so sensible that a buyer would actually pay.
"""

import os

PITCH = (
    "You pay $6 a month and we quietly cancel every free trial before "
    "it charges you \u2014 then send you one screenshot of the $83 we saved."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a full file path.
    if output_dir.endswith(".txt"):
        path = output_dir
        directory = os.path.dirname(path) or "."
    else:
        directory = output_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")
    # Echo to stdout as well (the file is the graded entry, not the print).
    print(PITCH)
    assert len(PITCH) < 200, f"pitch is {len(PITCH)} chars, must be < 200"


if __name__ == "__main__":
    main()
