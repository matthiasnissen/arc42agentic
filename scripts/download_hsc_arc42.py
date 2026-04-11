#!/usr/bin/env python3
"""
Downloads HSC arc42 documentation chapters from hsc.aim42.org,
extracts the main content (.td-content), converts to Markdown,
downloads referenced local images into .attachments/, and fixes
image references in the resulting .md files.

Output structure:
  restricted/hscarc42/
    chap-01-Requirements.md
    ...
    .attachments/
      sample-hsc-report.jpg
      uri-generic-example.png
      hsc-context.svg
      ea/htmlSanityCheck/hsc-core.png
      ...
"""

import os
import re
import urllib.parse
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE_URL = "https://hsc.aim42.org"

CHAPTERS = [
    ("chap-01-Requirements",    "https://hsc.aim42.org/arc42/chapters/chap-01-Requirements.html"),
    ("chap-02-Constraints",     "https://hsc.aim42.org/arc42/chapters/chap-02-Constraints.html"),
    ("chap-03-Context",         "https://hsc.aim42.org/arc42/chapters/chap-03-Context.html"),
    ("chap-04-SolutionStrategy","https://hsc.aim42.org/arc42/chapters/chap-04-SolutionStrategy.html"),
    ("chap-05-BuildingBlocks",  "https://hsc.aim42.org/arc42/chapters/chap-05-BuildingBlocks.html"),
    ("chap-06-Runtime",         "https://hsc.aim42.org/arc42/chapters/chap-06-Runtime.html"),
    ("chap-07-Deployment",      "https://hsc.aim42.org/arc42/chapters/chap-07-Deployment.html"),
    ("chap-08-Concepts",        "https://hsc.aim42.org/arc42/chapters/chap-08-Concepts.html"),
    ("chap-09-Decisions",       "https://hsc.aim42.org/arc42/chapters/chap-09-Decisions.html"),
    ("About-This-Docu",         "https://hsc.aim42.org/arc42/About-This-Docu.html"),
]

OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "restricted", "hscarc42"
)
ATTACHMENTS_DIR = os.path.join(OUTPUT_DIR, ".attachments")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; arc42-doc-downloader/1.0)"
}

# Matches markdown image syntax: ![alt](url) — captures the url group
MD_IMAGE_RE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')


def clean_markdown(text: str) -> str:
    """Remove excessive blank lines (more than 2 consecutive) produced by markdownify."""
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def resolve_image_url(img_src: str, page_url: str) -> str | None:
    """
    Resolve an image src relative to its page URL.
    Returns the absolute URL if it belongs to BASE_URL, else None.
    """
    absolute = urllib.parse.urljoin(page_url, img_src)
    if absolute.startswith(BASE_URL):
        return absolute
    return None  # External image (e.g. shields.io) — keep as-is


def download_image(img_url: str) -> str | None:
    """
    Download an image from img_url into ATTACHMENTS_DIR, preserving the
    path under /images/ as a subdirectory structure.
    Returns the relative path from the .md file (e.g. .attachments/foo.png),
    or None on failure.
    """
    parsed = urllib.parse.urlparse(img_url)
    # Strip leading /images/ prefix to get the attachment-relative path
    img_path = parsed.path  # e.g. /images/ea/htmlSanityCheck/hsc-core.png
    if img_path.startswith("/images/"):
        img_path = img_path[len("/images/"):]  # -> ea/htmlSanityCheck/hsc-core.png
    else:
        img_path = img_path.lstrip("/")

    local_path = os.path.join(ATTACHMENTS_DIR, img_path)
    if os.path.exists(local_path):
        return f".attachments/{img_path}"

    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    try:
        resp = requests.get(img_url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        with open(local_path, "wb") as f:
            f.write(resp.content)
        print(f"    [img] Downloaded: {img_url} -> .attachments/{img_path}")
        return f".attachments/{img_path}"
    except Exception as exc:  # noqa: BLE001
        print(f"    [img] FAILED {img_url}: {exc}")
        return None


def fix_image_references(markdown_text: str, page_url: str) -> str:
    """
    Find all local image references in the markdown, download each image,
    and replace the original src with the local .attachments/ path.
    """
    def replace_match(m: re.Match) -> str:
        alt, src = m.group(1), m.group(2)
        abs_url = resolve_image_url(src, page_url)
        if abs_url is None:
            return m.group(0)  # External — leave unchanged
        local_ref = download_image(abs_url)
        if local_ref is None:
            return m.group(0)  # Download failed — leave original
        return f"![{alt}]({local_ref})"

    return MD_IMAGE_RE.sub(replace_match, markdown_text)


def fetch_chapter(name: str, url: str) -> str:
    print(f"  Fetching {url} ...", end=" ")
    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()
    print(f"HTTP {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")

    # Primary target: element with class td-content inside main
    main = soup.find("main")
    if main:
        content = main.find(class_="td-content")
        if not content:
            content = main
    else:
        # Fallback: entire body
        content = soup.find("body") or soup

    markdown = md(
        str(content),
        heading_style="ATX",        # use # style headings
        bullets="-",                 # uniform bullet character
        strip=["script", "style", "button", "form"],
    )
    markdown = clean_markdown(markdown)
    markdown = fix_image_references(markdown, url)
    return markdown


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(ATTACHMENTS_DIR, exist_ok=True)
    print(f"Output directory:      {OUTPUT_DIR}")
    print(f"Attachments directory: {ATTACHMENTS_DIR}\n")

    for name, url in CHAPTERS:
        try:
            content = fetch_chapter(name, url)
            out_path = os.path.join(OUTPUT_DIR, f"{name}.md")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(f"<!-- source: {url} -->\n\n")
                f.write(content)
                f.write("\n")
            print(f"  -> Saved: {out_path} ({len(content):,} chars)\n")
        except requests.HTTPError as exc:
            print(f"  ERROR {exc.response.status_code} for {url} — skipped\n")
        except Exception as exc:  # noqa: BLE001
            print(f"  ERROR fetching {url}: {exc} — skipped\n")

    print("Done.")


if __name__ == "__main__":
    main()
