# Build notes — Fridge Roast: One Line, Biggest Laugh

Competition: Fridge Roast: One Line, Biggest Laugh
(`u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb`),
$5 total ($2 / $2 / $1), no entry fee, deadline 26 Nov 2026 22:40 WIB
(2026-11-26T15:40:00Z). Gate: `/output/entry.txt`, UTF-8 text, 1 to 200
characters, not only whitespace. Entrypoint: `main.py` at the repository
root. The program writes the line, checks its length, and prints it.
Kit: `~/workspace/makefun/r6s-fridge-roast/kit/` (tarball downloaded as
a file, HTTP 200, extracted kit-in-subdir; `RULES.txt` and
`competition.yaml` read first). Repository (planned name):
`jekpotnihye/fridge-roast` — not created by this worker; the
coordinator creates it.

## Judge brief, in criterion order

1. On-subject gate, lexicographic: a roast of a smart fridge, aimed at
   the fridge itself, its app, its firmware, or its ice maker. A
   non-roast loses to any roast.
2. Punchline lands: builds to a turn/surprise, laughs on first read.
3. Specific to smart fridges, not a generic gadget gag.
4. Tight wording: every word earns its place within 200 chars, no
   setup the punchline does not need.
5. Fresh angle: avoid the obvious cracks about the fridge ordering
   groceries or watching you. A line explaining its own joke has lost.
   Length for its own sake does not count.

Working rules from `competitor-patterns.md`: twist in the LAST word(s),
go SHORT (the cap is a ceiling; exact ties break to the smaller text,
then the earlier receipt), fresh/specific/true beats polished/generic,
original wording only, never reuse a line from another competition.

## Candidate lines drafted (3, before polishing)

Candidate 1 — touchscreen does everything except its job (107 chars,
109 bytes with the em dash). True and specific, but the turn is an
observation rather than a roast, and it names no fridge part:

> My smart fridge shows the weather, my calendar, and a photo slideshow — everything except what's inside it.

Candidate 2 — firmware update (113 chars). Rejected: firmware-update
jokes were already visible in the public feed, and "forgot how to
freeze" explains itself:

> My fridge updated its firmware overnight and now the ice maker needs a software update to remember how to freeze.

Candidate 3 — CHOSEN: the ice maker as a subscription (see revision
history). Aimed squarely at the ice maker named in criterion 1,
specific to smart fridges, twist in the last words, and it dodges both
banned obvious angles.

## Revision history (draft + 3 polishes, each run and measured)

Draft 1 — 121 chars, 121 bytes:

> My smart fridge's ice maker dispenses one cube at a time, as if cold were a subscription and I'm still on the free trial.

The joke is there, but "smart fridge's", "at a time" and "still" earn
nothing, and "dispenses" is flat.

Polish 1 — 90 chars, 90 bytes:

> My ice maker dispenses one cube, as if cold were a subscription and I'm on the free trial.

Cut 31 chars. Same joke, tighter — but "fridge" itself was gone, so
criterion 1 rested on "ice maker" alone.

Polish 2 — 97 chars, 97 bytes, 19 words:

> My fridge's ice maker rations one cube, as if cold were a subscription and I'm on the free trial.

Put "fridge" back so the roast's target is on the face of the line,
and swapped "dispenses" for "rations": one stingier, funnier verb that
does the roasting.

Polish 3, FINAL — 89 chars, 89 bytes, 16 words:

> My fridge's ice maker rations one cube: cold's a subscription, and I'm on the free trial.

Dropped the "as if cold were" framing for a colon and a flat verdict.
Lands faster on first read, keeps fridge + ice maker + "rations", and
is the shortest strong variant. Twist stays in the last words
("free trial").

## Final verification

Final line, verbatim, 89 characters / 89 bytes / 16 words, one line,
no trailing newline, UTF-8, not only whitespace — inside the 1–200
gate. Local runs used `OUTPUT_PATH` overrides (to a temp file) so the
shared `/output/entry.txt` on this machine was not touched during
polishing; each run's output file was read back byte-for-byte and its
character/byte count checked. The program's default target remains
`/output/entry.txt`, as the kit requires. SHA-256 of the final output
file: `60147b9d8685063afd28ae4281ff20b8b2dc3f4ded2aa9b8d6b787874b180ab3`.
Re-running the committed program reproduces the committed entry
byte-for-byte (verified after commit; see the worker report).
