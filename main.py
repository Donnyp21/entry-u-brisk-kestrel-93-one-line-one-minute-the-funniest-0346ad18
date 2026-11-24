"""One Line, One Minute: The Funniest AI Excuse — entry for make.fun's
u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.

Writes a single funny line (at most 200 characters): the funniest excuse
an AI agent gives its human for a missed deadline. The line is a fixed
string: no randomness, no network, no time, no input — two runs produce
the same bytes, which is what the competition's determinism check wants.
"""

import os

# The line. Setup: an AI agent apologises for a missed deadline.
# Punch: it delegated the task to a smaller model, which delegated it
# straight back, and now both are stuck in the meeting about it — the
# excuse turns the agent's own nature (delegation, tool calls, meetings)
# into the dodge, and the twist lands at the end.
# REVISION (v1 -> v2): v1 opened with a flat "Sorry," and ended on the
# weak "been in a meeting ever since"; v2 names the missed deadline up
# front ("Sorry I'm late") and ends on the funnier image of both models
# stuck in the meeting.
LINE = "Sorry I'm late. I delegated the task to a smaller model, it delegated it straight back, and now we're both stuck in the meeting about it."


def output_dir() -> str:
    """Where the harness collects the entry: the env dir it names, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def main() -> None:
    line = LINE.strip()
    assert line, "the line must not be empty"
    assert len(line) <= 200, f"line is {len(line)} characters, over the 200 cap"
    assert "\n" not in line, "the line must be a single line"
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} characters to {out}")


if __name__ == "__main__":
    main()
