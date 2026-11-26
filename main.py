"""Out-of-office, in one line: an away message negotiated with a houseplant.

This program has a single job: place one fixed reply into
``/output/entry.txt``. The reply is a constant, and it is checked against
the competition gate (1-160 characters, a single line, printable ASCII)
before anything is written, so a bad constant can never produce output.
"""

import os
import sys

MAX_CHARS = 160

TEXT = "Currently away in a meeting with my houseplant about boundaries. Back Monday, slightly photosynthesized."

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def _problems(text):
    """Collect every gate violation found in *text* as error messages.

    The type check runs first and raises directly, because none of the
    other checks make sense on a non-string. The remaining checks are a
    table of (failed, message) pairs evaluated in order; every failure
    is reported, the first one is raised by the caller.
    """
    if not isinstance(text, str):
        raise TypeError("entry text must be str")
    checks = [
        (not text.strip(),
         "entry text must not be empty or whitespace-only"),
        (len(text) > MAX_CHARS,
         "entry text exceeds %d characters" % MAX_CHARS),
        (("\n" in text) or ("\r" in text),
         "entry text must be a single line"),
        (any(ord(ch) < 32 or ord(ch) == 127 for ch in text),
         "entry text must not contain control characters"),
    ]
    return [message for failed, message in checks if failed]


def validate_entry_text(text):
    """Return *text* unchanged when it passes the gate, else raise."""
    failures = _problems(text)
    if failures:
        raise ValueError(failures[0])
    return text


def main(argv=None):
    """Write the validated reply to the output file; return exit status 0."""
    text = validate_entry_text(TEXT)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(OUT_PATH, "rb") as handle:
        written = handle.read()
    if written != text.encode("utf-8"):
        raise RuntimeError("written output does not match the entry text")
    return 0


if __name__ == "__main__":
    sys.exit(main())
