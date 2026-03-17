#!/usr/bin/env python3
"""Helper script to create new publication .md files.

Usage:
    python scripts/add-publication.py --title "Paper Title" --authors "A, B, C" --journal "Nature" --year 2025 --url "https://..."
    python scripts/add-publication.py --title "Paper Title" --authors "A, B, C" --journal "Nature" --year 2025 --volume "16 (1), 123" --url "#"
"""

import argparse
import os
import re

def main():
    parser = argparse.ArgumentParser(description="Create a new publication markdown file")
    parser.add_argument("--title", required=True, help="Publication title")
    parser.add_argument("--authors", required=True, help="Author list")
    parser.add_argument("--journal", required=True, help="Journal name")
    parser.add_argument("--year", required=True, type=int, help="Publication year")
    parser.add_argument("--volume", default="", help="Volume/pages info")
    parser.add_argument("--url", default="#", help="URL to publication")
    args = parser.parse_args()

    slug = re.sub(r'[^a-z0-9]+', '-', args.title.lower()).strip('-')[:60]
    filename = f"{args.year}-{slug}.md"

    pub_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "publications")
    filepath = os.path.join(pub_dir, filename)

    if os.path.exists(filepath):
        print(f"Warning: {filepath} already exists!")
        return

    title = args.title.replace('"', '\\"')
    authors = args.authors.replace('"', '\\"')
    journal = args.journal.replace('"', '\\"')
    volume = args.volume.replace('"', '\\"')

    content = f'''---
title: "{title}"
authors: "{authors}"
journal: "{journal}"
volume: "{volume}"
year: {args.year}
url: "{args.url}"
---
'''

    with open(filepath, 'w') as f:
        f.write(content)

    print(f"Created: {filepath}")

if __name__ == "__main__":
    main()
