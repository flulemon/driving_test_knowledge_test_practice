# Question Trainer

A single-page quiz app for practicing driving knowledge questions. It loads questions from `questions.json`, supports multiple study modes, re-asks missed questions until they are answered correctly, and shows a clear summary of first-attempt results.

## Features

- Multiple modes: fixed ranges (1-50, 51-100, 101-150, 151+) plus Random 5/25/50.
- Immediate feedback via colored option highlights.
- Retry loop: missed questions are asked again at the end until answered correctly.
- Summary shows first-attempt results only (so you can see what was missed).
- Static HTML output for easy hosting (GitHub Pages, Cloudflare Pages, etc.).

## Project Files

- `questions.json`: Source question bank.
- `app.template.html`: HTML template (references `__QUESTIONS__` placeholder).
- `update_questions.py`: Builds the final HTML by embedding questions.
- `docs/index.html`: Generated output used for deployment.

## How to Update Questions

1) Edit `questions.json`.
2) Regenerate the site:

```bash
python3 update_questions.py
```

This writes the updated HTML to `docs/index.html`.

## Local Preview

Open the generated file directly in a browser:

```bash
open docs/index.html
```

Or use any static server of your choice.
