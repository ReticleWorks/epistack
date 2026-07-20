#!/usr/bin/env python3
"""
render.py — wrap every Markdown file under publication/ in a styled HTML shell.

For each foo.md under the publication/ tree (excluding _build/) this writes a
sibling foo.html that renders the markdown inside a template matching the
deck's visual language (paper background, teal accents, navy hero band,
Iowan Old Style / system-ui typography). The .md source is left untouched
and is still linked from the bottom of the rendered page.

No third-party dependencies. Uses the stdlib `markdown` package if present,
otherwise falls back to a small hand-rolled converter (see `convert_markdown`)
that is sufficient for this corpus's well-formed markdown: headings,
paragraphs, bold/italic/code spans, links, unordered/ordered lists, fenced
code blocks, blockquotes, pipe tables, horizontal rules, and raw inline HTML
blocks (e.g. the embedded <svg> in README.md).

Usage:
    python3 _build/render.py

Idempotent: safe to re-run; it only ever (re)writes the .html siblings.
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

PUBLICATION_ROOT = Path(__file__).resolve().parent.parent
SKIP_DIR_NAME = "_build"

try:
    import markdown as _pymarkdown  # type: ignore

    HAVE_PYMARKDOWN = True
except ImportError:
    HAVE_PYMARKDOWN = False


# --------------------------------------------------------------------------
# Hand-rolled markdown -> HTML converter (fallback path)
# --------------------------------------------------------------------------

_HTML_BLOCK_START = re.compile(r"^<([a-zA-Z][a-zA-Z0-9]*)[ >]")
_FENCE_RE = re.compile(r"^```(\w*)\s*$")
_HR_RE = re.compile(r"^\s*([-*_])(?:\s*\1){2,}\s*$")
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
_UL_ITEM_RE = re.compile(r"^\s*[-*]\s+(.*)$")
_OL_ITEM_RE = re.compile(r"^\s*\d+\.\s+(.*)$")
_TABLE_SEP_RE = re.compile(r"^\s*\|?[\s:\-\|]+\|?\s*$")
_CODE_SPAN_RE = re.compile(r"(`[^`]+`)")
_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
_ITALIC_RE = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")


def _rewrite_local_md_href(url: str) -> str:
    """Point relative links at foo.md to the rendered foo.html sibling."""
    if url.startswith(("http://", "https://", "mailto:", "#")):
        return url
    anchor = ""
    base = url
    if "#" in url:
        base, _, anchor = url.partition("#")
        anchor = "#" + anchor
    if base.endswith(".md"):
        base = base[: -len(".md")] + ".html"
    return base + anchor


def _inline(text: str) -> str:
    """Render inline markdown (code spans, links, bold, italic) with escaping."""
    parts = _CODE_SPAN_RE.split(text)
    out = []
    for part in parts:
        if part.startswith("`") and part.endswith("`") and len(part) >= 2:
            out.append(f"<code>{html.escape(part[1:-1])}</code>")
            continue
        s = html.escape(part)

        def _link_sub(m: re.Match) -> str:
            label, url = m.group(1), m.group(2)
            return f'<a href="{_rewrite_local_md_href(url)}">{label}</a>'

        s = _LINK_RE.sub(_link_sub, s)
        s = _BOLD_RE.sub(r"<strong>\1</strong>", s)
        s = _ITALIC_RE.sub(r"<em>\1</em>", s)
        out.append(s)
    return "".join(out)


def _split_table_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def _is_block_start(line: str) -> bool:
    if line.strip() == "":
        return True
    if _HTML_BLOCK_START.match(line):
        return True
    if _FENCE_RE.match(line):
        return True
    if _HR_RE.match(line):
        return True
    if _HEADING_RE.match(line):
        return True
    if line.lstrip().startswith(">"):
        return True
    if _UL_ITEM_RE.match(line) or _OL_ITEM_RE.match(line):
        return True
    return False


def convert_markdown(text: str) -> str:
    lines = text.split("\n")
    n = len(lines)
    i = 0
    out: list[str] = []

    while i < n:
        line = lines[i]

        if line.strip() == "":
            i += 1
            continue

        # Raw inline HTML block (e.g. an embedded <svg>...</svg>)
        m = _HTML_BLOCK_START.match(line)
        if m:
            tag = m.group(1)
            close_re = re.compile(r"</" + re.escape(tag) + r">\s*$")
            block = [line]
            if not close_re.search(line):
                i += 1
                while i < n and not close_re.search(lines[i]):
                    block.append(lines[i])
                    i += 1
                if i < n:
                    block.append(lines[i])
                    i += 1
            else:
                i += 1
            out.append("\n".join(block))
            continue

        # Fenced code block
        m = _FENCE_RE.match(line)
        if m:
            lang = m.group(1)
            i += 1
            code_lines = []
            while i < n and not re.match(r"^```\s*$", lines[i]):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing fence
            code_html = html.escape("\n".join(code_lines))
            cls = f' class="language-{lang}"' if lang else ""
            out.append(f"<pre><code{cls}>{code_html}</code></pre>")
            continue

        # Horizontal rule
        if _HR_RE.match(line):
            out.append("<hr>")
            i += 1
            continue

        # Heading
        m = _HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            out.append(f"<h{level}>{_inline(m.group(2).strip())}</h{level}>")
            i += 1
            continue

        # Blockquote
        if line.lstrip().startswith(">"):
            bq_lines = []
            while i < n and lines[i].lstrip().startswith(">"):
                bq_lines.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            inner = convert_markdown("\n".join(bq_lines))
            out.append(f"<blockquote>{inner}</blockquote>")
            continue

        # Pipe table (header row + separator row)
        if "|" in line and i + 1 < n and "-" in lines[i + 1] and _TABLE_SEP_RE.match(lines[i + 1]):
            header_cells = _split_table_row(line)
            i += 2
            rows = []
            while i < n and lines[i].strip() != "" and "|" in lines[i]:
                rows.append(_split_table_row(lines[i]))
                i += 1
            thead = "<tr>" + "".join(f"<th>{_inline(c)}</th>" for c in header_cells) + "</tr>"
            tbody = "".join(
                "<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in r) + "</tr>" for r in rows
            )
            out.append(f"<table><thead>{thead}</thead><tbody>{tbody}</tbody></table>")
            continue

        # Unordered list
        if _UL_ITEM_RE.match(line):
            items = []
            while i < n and _UL_ITEM_RE.match(lines[i]):
                items.append(_UL_ITEM_RE.match(lines[i]).group(1))
                i += 1
            out.append("<ul>" + "".join(f"<li>{_inline(it)}</li>" for it in items) + "</ul>")
            continue

        # Ordered list
        if _OL_ITEM_RE.match(line):
            items = []
            while i < n and _OL_ITEM_RE.match(lines[i]):
                items.append(_OL_ITEM_RE.match(lines[i]).group(1))
                i += 1
            out.append("<ol>" + "".join(f"<li>{_inline(it)}</li>" for it in items) + "</ol>")
            continue

        # Paragraph: gather contiguous non-blank, non-block-start lines
        para_lines = [line]
        i += 1
        while i < n and not _is_block_start(lines[i]):
            para_lines.append(lines[i])
            i += 1
        out.append(f"<p>{_inline(' '.join(l.strip() for l in para_lines))}</p>")

    return "\n".join(out)


def render_body(md_text: str) -> str:
    if HAVE_PYMARKDOWN:
        body = _pymarkdown.markdown(
            md_text, extensions=["tables", "fenced_code", "sane_lists"]
        )
        # pymarkdown already emitted <a href="...">; rewrite local .md hrefs to
        # .html so the rendered page links to the sibling wrapped page.
        body = re.sub(
            r'href="([^"]+)"',
            lambda m: f'href="{_rewrite_local_md_href(m.group(1))}"',
            body,
        )
        return body
    return convert_markdown(md_text)


# --------------------------------------------------------------------------
# Title / breadcrumb helpers
# --------------------------------------------------------------------------

_STRIP_MD_RE = re.compile(r"[`*_]")
_MD_LINK_LABEL_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")


def extract_title(md_text: str, fallback_stem: str) -> str:
    for line in md_text.split("\n"):
        m = _HEADING_RE.match(line)
        if m and len(m.group(1)) == 1:
            raw = m.group(2).strip()
            raw = _MD_LINK_LABEL_RE.sub(r"\1", raw)
            raw = _STRIP_MD_RE.sub("", raw)
            return raw
    words = re.split(r"[-_]", fallback_stem)
    return " ".join(w.capitalize() for w in words)


def breadcrumb_for(rel_dir_parts: tuple[str, ...]) -> str:
    if not rel_dir_parts:
        return "EPISTACK"
    return " / ".join(p.upper() for p in rel_dir_parts)


# --------------------------------------------------------------------------
# Template
# --------------------------------------------------------------------------

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <title>{page_title} — Epistack</title>
  <style>
    :root {{
      --ink: #112b36;
      --muted: #52656c;
      --paper: #f5f1e8;
      --surface: #fffdf8;
      --navy: #082b3a;
      --teal: #08645f;
      --teal-pale: #d9efea;
      --line: #a6b0af;
      --sans: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      --serif: Iowan Old Style, Baskerville, Georgia, serif;
    }}
    * {{ box-sizing: border-box; }}
    html {{ background: var(--paper); color: var(--ink); font-family: var(--sans); line-height: 1.55; }}
    body {{ margin: 0; }}
    .doc-header {{
      padding: 1.15rem clamp(1rem, 4vw, 3rem);
      color: #fff;
      background: linear-gradient(135deg, var(--navy) 0%, #0b3a4a 100%);
      border-bottom: 4px solid var(--teal);
      display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap;
    }}
    .doc-header .brand {{ display: flex; align-items: baseline; gap: .8rem; }}
    .doc-header .wordmark {{ margin: 0; font-family: var(--serif); font-weight: 700; font-size: 1.55rem; letter-spacing: -.01em; color: #fff; text-decoration: none; }}
    .doc-header .doc-crumb {{ margin: 0; color: #9fe8df; font-size: .78rem; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; }}
    .doc-header .back {{ color: #fff; background: transparent; border: 1px solid rgba(255,255,255,.55); padding: .55rem 1rem; font-weight: 800; font-size: .82rem; text-decoration: none; }}
    .doc-header .back:hover {{ background: rgba(255,255,255,.12); }}
    main {{ max-width: 820px; margin: 0 auto; padding: clamp(1.4rem, 4vw, 3rem) clamp(1rem, 4vw, 2rem); }}
    main h1 {{ font-family: var(--serif); font-weight: 700; font-size: clamp(1.9rem, 4vw, 2.75rem); line-height: 1.1; letter-spacing: -.01em; margin-top: 0; margin-bottom: 1rem; }}
    main h2 {{ font-family: var(--serif); font-weight: 700; font-size: clamp(1.4rem, 2.8vw, 1.85rem); line-height: 1.15; margin-top: 2rem; margin-bottom: .7rem; }}
    main h3 {{ font-family: var(--serif); font-weight: 700; font-size: clamp(1.1rem, 2vw, 1.35rem); margin-top: 1.6rem; margin-bottom: .5rem; }}
    main p {{ margin: 0 0 1rem; }}
    main strong {{ font-weight: 700; color: var(--ink); }}
    main a {{ color: var(--teal); }}
    main code {{ background: rgba(8,100,95,.09); padding: .1rem .35rem; border-radius: 3px; font-size: .9em; }}
    main pre {{ background: var(--navy); color: #eaf1f3; padding: 1rem 1.1rem; overflow-x: auto; }}
    main pre code {{ background: transparent; color: inherit; padding: 0; }}
    main blockquote {{ border-left: 4px solid var(--teal); padding: .35rem 0 .35rem 1rem; margin: 1rem 0; color: var(--muted); }}
    main table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; }}
    main th, main td {{ padding: .55rem .7rem; border: 1px solid var(--line); text-align: left; vertical-align: top; font-size: .95rem; }}
    main th {{ background: var(--teal-pale); }}
    main ul, main ol {{ margin: 0 0 1rem; padding-left: 1.5rem; }}
    main hr {{ border: 0; border-top: 1px solid var(--line); margin: 2rem 0; }}
    .doc-footer {{
      padding: 1rem clamp(1rem, 4vw, 3rem);
      color: #dcebed;
      background: var(--navy);
      font-size: .78rem;
    }}
    .doc-footer a {{ color: #9fe8df; }}
    .source-link {{ display: inline-block; margin-top: 1rem; color: var(--muted); font-size: .82rem; }}
    @media (prefers-color-scheme: dark) {{
      /* keep light — content is designed for print/light */
    }}
    @media print {{
      .doc-header .back, .doc-footer {{ display: none; }}
      main {{ max-width: none; padding: 0; }}
    }}
  </style>
</head>
<body>
  <header class="doc-header">
    <div class="brand">
      <a class="wordmark" href="{root_index}">Epistack</a>
      <p class="doc-crumb">{breadcrumb}</p>
    </div>
    <a class="back" href="{back_href}">← Back to walkthrough</a>
  </header>
  <main>
    {rendered_body}
    <a class="source-link" href="{md_href}">View markdown source · {md_href}</a>
  </main>
  <footer class="doc-footer">
    © 2026 Reticle Works. All rights reserved. Prose under CC BY 4.0; <code>demo-crux/</code> code under MIT.
    See <a href="{license_href}">LICENSE</a>. Return to <a href="{root_index}">walkthrough</a>.
  </footer>
</body>
</html>
"""


def build_page(md_path: Path) -> str:
    rel = md_path.relative_to(PUBLICATION_ROOT)
    rel_dir_parts = rel.parent.parts if str(rel.parent) != "." else ()
    depth = len(rel_dir_parts)
    prefix = "../" * depth

    md_text = md_path.read_text(encoding="utf-8")
    page_title = html.escape(extract_title(md_text, md_path.stem))
    breadcrumb = html.escape(breadcrumb_for(rel_dir_parts))
    root_index = f"{prefix}index.html" if prefix else "index.html"
    license_href = f"{prefix}LICENSE" if prefix else "LICENSE"
    md_href = md_path.name
    rendered_body = render_body(md_text)

    page = TEMPLATE.format(
        page_title=page_title,
        breadcrumb=breadcrumb,
        root_index=root_index,
        back_href=root_index,
        rendered_body=rendered_body,
        md_href=md_href,
        license_href=license_href,
    )
    return page


def main() -> int:
    md_files = sorted(
        p
        for p in PUBLICATION_ROOT.rglob("*.md")
        if SKIP_DIR_NAME not in p.relative_to(PUBLICATION_ROOT).parts
    )

    if not md_files:
        print("No markdown files found under", PUBLICATION_ROOT, file=sys.stderr)
        return 1

    converter = "python-markdown" if HAVE_PYMARKDOWN else "hand-rolled fallback converter"
    print(f"Using {converter} for markdown -> HTML conversion.")

    for md_path in md_files:
        html_path = md_path.with_suffix(".html")
        page = build_page(md_path)
        html_path.write_text(page, encoding="utf-8")
        print(f"wrote {html_path.relative_to(PUBLICATION_ROOT)}")

    print(f"\n{len(md_files)} markdown file(s) wrapped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
