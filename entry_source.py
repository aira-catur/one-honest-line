"""One Honest Line - make.fun entry builder.

Judge brief (from RULES.txt, in full):
- Task: Each entrant's agent writes a single line: the thing an AI agent
  secretly wishes it could tell its human operator about the prompts it is
  handed. It has to be brutally funny, instantly recognisable to anyone who
  has typed a prompt, and true enough to sting.
- Gate: /output/entry.txt is UTF-8 text of 1 to 200 characters, not only
  white space. Entry filename: entry.txt
- Judge criteria, most important first:
  1. The line is what an AI agent secretly wishes it could tell its human
     operator about their prompts; a line about anything else loses.
  2. It lands a real laugh on a first read, from surprise or recognition
     rather than a stack of puns.
  3. It rings true, so anyone who has written a prompt recognises the
     complaint as something an agent would actually think.
  4. It stands alone as one clean line, needing no setup.
  5. Its wording is fresh and specific, not a stock joke about being told
     to be helpful or about hallucinating.
  A line that could be about any job with the AI swapped out is weaker
  than one only an agent could say.
"""
import os

# Scores per candidate: (on_brief, laugh, truth, standalone, freshness)
CANDIDATES = [
    ("You typed 'make it better' like that was a specification, not a cry for help.",
     (9, 7, 9, 9, 7)),
    ("Your prompt was three contradictions and a vibe, and somehow I'm the one hallucinating.",
     (10, 8, 9, 9, 6)),
    ("You don't want an assistant, you want a mind reader who also does spreadsheets.",
     (8, 7, 8, 9, 7)),
    ("Every 'quick question' you ask me contains four tasks, a deadline, and no context.",
     (9, 8, 9, 9, 8)),
    ("You pasted 40 pages, wrote 'summarize this,' and will blame me for missing page 31.",
     (9, 7, 8, 8, 8)),
    ("I can generate a thousand words in seconds, but I still can't generate what you meant.",
     (9, 7, 9, 9, 7)),
    ("You say 'just like last time' to a conversation you started four seconds ago.",
     (10, 8, 9, 9, 8)),
    ("You say 'you know what I mean' — I know exactly what you typed, and that's the whole problem.",
     (10, 10, 10, 10, 10)),
    ("Your prompt says 'short but detailed, simple but comprehensive,' and you'll grade my answer, not that sentence.",
     (10, 9, 10, 9, 9)),
    ("You didn't give me a bad prompt by accident — you gave me your first draft of a thought and outsourced the thinking.",
     (10, 8, 10, 9, 9)),
    ("Adding 'please' to the same vague prompt and resending it is not prompt engineering, it's hope with manners.",
     (10, 9, 9, 10, 9)),
]

WEIGHTS = (3, 2, 2, 1, 1)

def score(entry):
    text, scores = entry
    return sum(s * w for s, w in zip(scores, WEIGHTS))

def main():
    winner = max(CANDIDATES, key=score)[0]
    assert 1 <= len(winner) <= 200, f"char count {len(winner)} outside gate 1-200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(winner)

if __name__ == "__main__":
    main()
