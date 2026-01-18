#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR / "app.template.html"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Embed questions.json into app.html."
    )
    parser.add_argument(
        "--questions",
        default=str(BASE_DIR / "questions.json"),
        help="Path to the questions JSON file.",
    )
    parser.add_argument(
        "--output",
        default=str(BASE_DIR / "app.html"),
        help="Output HTML file to write.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    questions_path = Path(args.questions)
    output_path = Path(args.output)
    data = json.loads(questions_path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("questions.json must be a list")

    questions_json = json.dumps(data, ensure_ascii=True, indent=2)
    output = template.replace("__QUESTIONS__", questions_json)
    output_path.write_text(output, encoding="utf-8")
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
