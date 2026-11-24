"""The Funniest Toaster Error Message.

Writes one deadpan appliance error line to /output/entry.txt.
Deterministic, stdlib only, no network, no randomness.
"""

LINE = "CRUMB TRAY FULL. I HAVE BEEN QUIETLY KEEPING THIS FROM YOU FOR MONTHS."


def validate(line: str) -> str:
    """Enforce the competition's hard rules: one line, at most 120 chars."""
    stripped = line.strip()
    assert "\n" not in stripped, "entry must be a single line"
    assert len(stripped) <= 120, f"entry is {len(stripped)} chars, max 120"
    assert stripped, "entry must not be empty"
    return stripped


def main() -> None:
    import os

    line = validate(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
