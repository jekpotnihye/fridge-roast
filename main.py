"""Fridge Roast: One Line, Biggest Laugh.

Write one roast of a smart fridge to /output/entry.txt, judged in
criterion order: a roast aimed at the fridge / its ice maker first,
a punchline that lands on first read, specific to smart fridges,
tight wording, and a fresh angle (no ordering-groceries / watching-you
cracks, no explaining the joke).
"""

import os

# Polish 3, FINAL (89 chars): drop the "as if cold were" framing
# for a colon and a flat verdict — "cold's a subscription" lands
# faster on first read, keeps fridge + ice maker + "rations", and
# is the shortest strong variant. Twist stays in the last words.
ENTRY = (
    "My fridge's ice maker rations one cube: "
    "cold's a subscription, and I'm on the free trial."
)


def main() -> None:
    line = ENTRY.strip()
    size = len(line)
    if size < 1 or size > 200:
        raise ValueError(f"Refusing to write an entry of {size} characters.")
    target = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(line)
    print(f"chars: {size}")


if __name__ == "__main__":
    main()
