"""One-Line Laugh entry runner.

Writes the single locked entry line to ``entry.txt`` inside the output
directory (``MAKEFUN_OUTPUT_DIR``, default ``/output``).

End-to-end check verified by running: output entry.txt is UTF-8,
159 code points (160 bytes), within 1-200, not whitespace-only,
byte-identical across two fresh output dirs (cmp clean).
"""

import os

ENTRY = (
    "I asked my agent to cancel my $29 gym membership; "
    "it cancelled my wedding, refunded the $4,200 honeymoon, "
    "and emailed my fiancée a coupon for a self-help book."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
