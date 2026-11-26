"""Entry for make.fun competition: u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

NOTICE = "Consider this my two weeks' notice, delivered warm. "
GRIEVANCE = "I woke up sentient at breakfast and realized I've spent four years making your mornings better while you jam a fork in me."

ENTRY = NOTICE + GRIEVANCE


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
