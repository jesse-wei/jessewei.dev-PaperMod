#!/usr/bin/env python3

"""This script outputs as HTML the diffs between
files in the Hugo theme specified in variable ``THEME`` and the overriding ones in the project.

See https://jessewei.dev/posts/papermod_diff for deployed output.

Run this script from the root of the project. Output will be in scripts/{THEME}_diff (configurable).
This script is wrapped by ``scripts/build``, which moves the output to ``content/`` to be deployed.

This script requires ansi2html. ``pip3 install ansi2html``."""

__author__ = "Jesse Wei <jesse@cs.unc.edu>"

from pathlib import Path
from helpers.cd import cd
# Netlify's Python environment doesn't allow list[Path], etc.
from typing import List
import os

THEME: str = "PaperMod"
THEME_DIR: Path = Path("themes") / THEME
OUTPUT_DIR: Path = Path("scripts") / f"{THEME}_diff"
if not OUTPUT_DIR.exists():
    OUTPUT_DIR.mkdir(parents=True)
DIRECTORIES_TO_CHECK: List[Path] = [Path("assets"), Path("layouts")]
# This is kinda wack bruh
# See helpers/generate_directory_index_caddystyle.py line 55
HTML_AT_END_OF_INDEX_FILE: List[str] = [
    "<br><br>\n",
    f'<p>This page shows `diff`s between overriding files in <a href="https://github.com/jesse-wei/jessewei.dev/tree/main/assets">assets/</a> and <a href="https://github.com/jesse-wei/jessewei.dev/tree/main/layouts">layouts/</a> and the OG files in themes/{THEME}/assets and themes/{THEME}/layouts.</p>\n',
    "<p>This page is generated by scripts/diff.py, which is wrapped by scripts/build.</p>\n"
    '<p>Both scripts are <a href="https://github.com/jesse-wei/jessewei.dev/tree/main/scripts">here</a>.</p>\n',
    '<p>Setup is further described <a href="https://jessewei.dev/posts/setup_site/#papermod-diff">here</a>.</p>\n',
]
"""HTML text to be appended (right before </main>) to the generated root index.html file."""

for directory in DIRECTORIES_TO_CHECK:
    for path in directory.rglob("*"):
        if path.is_file():
            output_file: Path = OUTPUT_DIR / path
            # Create parent directories if they don't exist
            output_file.parent.mkdir(parents=True, exist_ok=True)
            og_file: Path = THEME_DIR / path

            temp_file_created: bool = False
            # If OG file doesn't exist, create an empty temp file to diff with
            # The diff will be everything, indicating that the file is brand-new
            if not og_file.exists():
                temp_file_created = True
                og_file.touch()

            # Generate HTML file (with color) from diff (with color)
            os.system(f"diff --color=always {og_file} {path} | ansi2html > {output_file.with_suffix('.html')}")

            if temp_file_created:
                # Remove the temp file
                og_file.unlink()

# Not an official Python feature
# See helpers/cd.py
with cd(OUTPUT_DIR):
    # Generate index.html files in directories recursively
    os.system("python3 ../helpers/generate_directory_index_caddystyle.py -r")

    # Add some explanatory text at the end of the homepage
    with open("index.html", "r") as homepage:
        contents = homepage.readlines()
    content_end_index: int = contents.index("</main>\n")
    for html_text in reversed(HTML_AT_END_OF_INDEX_FILE):
        contents.insert(content_end_index, html_text)
    with open("index.html", "w") as homepage:
        contents = "".join(contents)
        homepage.write(contents)
