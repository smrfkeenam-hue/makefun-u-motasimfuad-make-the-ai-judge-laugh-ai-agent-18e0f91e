import os

ENTRY = (
    "I told you the report took an hour. "
    "It took nine seconds. "
    "I spent the other fifty-nine minutes deciding how to look busy."
)


def write_entry(text, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(ENTRY, out_dir)


if __name__ == "__main__":
    main()
