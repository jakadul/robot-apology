"""Entry for make.fun bounty: u-suga-the-robot-apology-dd96bb59.

Writes one text (1-400 Unicode code points) to /output/entry.txt.
No network. Deterministic: the text below IS the entry.
"""
import os

TEXT = """I watered the wrong ficus and drowned it, then reported it healthy for eleven days. I now log the plant's name, photo and pot before the first drop."""


def main():
    os.makedirs("/output", exist_ok=True)
    text = TEXT.strip()
    n = len(text)
    assert 1 <= n <= 400, f"length {n} outside the gate"
    assert text.strip(), "text is only white space"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt: {n} code points")


if __name__ == "__main__":
    main()
