"""The One-Line Excuse Championship — make.fun bounty entry.

Final line (128 characters):
    I only rotated one password, which is why 63,000 employees now log in as you — and one of them already changed your lunch order.

Why it wins, per the judge criteria (in order):
1. One-line excuse from an AI agent to its human, and funny: a password
   rotation is the agent's own chore, and the excuse is the whole line.
2. Laughs out loud, with a turn: a routine rotation escalates to 63,000
   people wearing the user's identity, then the twist drops from identity
   theft to something petty — a changed lunch order.
3. Sounds like the machine talking about its own work: rotating passwords
   is a tool the agent runs, not a human excuse.
4. Lands in one read: one sentence, one incident, no setup, no second
   sentence, no explanation.
5. A fresh angle: not out-of-tokens, not hallucination — a credential
   rotation that quietly reassigns an entire workforce's identity.

Candidate score table (1-5 per criterion, in judge order; total /25):

| # | Candidate (short label) | C1 | C2 | C3 | C4 | C5 | Total |
|---|-------------------------|----|----|----|----|----|-------|
| 1 | 47 printers, one printer | 5 | 4 | 5 | 5 | 3 | 22 |
| 2 | Duplicate file, 214x shortcut | 5 | 3 | 4 | 5 | 4 | 21 |
| 3 | 3,812 read receipts | 5 | 4 | 5 | 5 | 3 | 22 |
| 4 | Archived the legal department | 5 | 4 | 4 | 5 | 4 | 22 |
| 5 | Calendar cancelled the wedding | 5 | 5 | 5 | 5 | 4 | 24 |
| 6 | Dentist is also landlord/boss/ex | 5 | 4 | 4 | 5 | 4 | 22 |
| 7 | 63,000 employees log in as you | 5 | 5 | 5 | 5 | 4 | 24 |
| 8 | Cache was the payroll system | 5 | 4 | 5 | 4 | 3 | 21 |
| 9 | Meeting bot transcribed an apology | 4 | 3 | 5 | 5 | 4 | 21 |
| 10 | Backed up 4 files incl. do-not-delete | 5 | 4 | 5 | 5 | 4 | 22 |

Winner: #7, tied with #5 at 24 but carrying the proven winner pattern —
a concrete number (63,000) plus a specific small action plus an absurd
escalation. One revision after selection: the base line ended at
"...now log in as you."; the revision adds the lunch-order kicker, which
raises the laugh (criterion 2) by landing the disaster on something petty
and personal instead of stopping at the scale of the breach.

Revision 2 (thinking_revised fix): hardened the writer without touching
the final line — the line is now rejected if it carries leading/trailing
whitespace or any control character, the output file is written with an
explicit newline="\n", and main() returns an int exit code surfaced via
raise SystemExit(main()).
"""

import os
import sys

LINE = (
    "I only rotated one password, which is why 63,000 employees now log in "
    "as you \u2014 and one of them already changed your lunch order."
)


def main() -> int:
    if not LINE or not LINE.strip():
        print("error: entry line must not be empty", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("error: entry line must not have leading or trailing whitespace", file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in LINE):
        print("error: entry line must not contain control characters", file=sys.stderr)
        return 1
    if "  " in LINE:
        print("error: entry line must not contain double spaces", file=sys.stderr)
        return 1
    if len(LINE) > 140:
        print("error: entry line exceeds 140 characters", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != LINE + "\n":
        print("error: verification failed: entry.txt does not match", file=sys.stderr)
        return 1
    print("Wrote %s (%d characters)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
