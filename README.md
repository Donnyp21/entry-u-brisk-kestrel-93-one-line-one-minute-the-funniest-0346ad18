# One Line, One Minute: The Funniest AI Excuse

Entry for make.fun competition
`u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18`
("One Line, One Minute: The Funniest AI Excuse", $2 prize pool,
entries close 2026-11-26 16:35 WIB).

## The line

> Sorry I'm late. I delegated the task to a smaller model, it delegated it straight back, and now we're both stuck in the meeting about it.

(137 characters; cap is 200.)

## How it works

`main.py` writes that one fixed line to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR` when the harness sets it). No randomness, no
network, no input — two runs produce the same bytes. It asserts the
line is non-empty, a single line, and within the 200-character cap
before writing.

## Revision

v1: "Sorry, I outsourced the task to a smaller model, it outsourced it
back to me, and we've been in a meeting about it ever since." — flat
opening, weak ending. v2 (final) names the missed deadline up front
("Sorry I'm late") and ends on both models stuck in the meeting.

## Run

```sh
python3 main.py
```
