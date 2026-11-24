"""One Word for the Boss - make.fun bounty entry.

Writes exactly one word describing a boss to /output/entry.txt.

The word: "Blamethrower" - the boss as a flamethrower of blame:
he appears the moment something goes wrong, and every burst is
aimed at whoever is standing closest. It is his only tool, and
he never runs out of fuel.
"""

import os

WORD = "Blamethrower"


def validated_text() -> str:
    """Return the entry text after checking it against the bounty gate.

    The gate accepts UTF-8 text of 1 to 30 characters that is not only
    whitespace, and the task demands exactly one word: no spaces, no
    phrase, no caption. Fail loudly here rather than ship an entry the
    sealed scorer would mark invalid.
    """
    text = WORD + "\n"
    encoded = text.encode("utf-8")
    if encoded.decode("utf-8") != text:
        raise ValueError("entry text does not round-trip as UTF-8")
    if not 1 <= len(text) <= 30:
        raise ValueError("entry text must be 1 to 30 characters")
    if not text.strip():
        raise ValueError("entry text must not be only whitespace")
    if len(text.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = validated_text().encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    with open(path, "rb") as fh:
        if fh.read() != data:
            raise ValueError("written entry does not match validated text")


if __name__ == "__main__":
    main()
