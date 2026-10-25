#!/usr/bin/env python3
"""Turn a raw (RFC 822) order email into readable text, and extract PDF attachments.

Use when an order email's plain-text part omits the item list (only the HTML
part has it), or when the receipt is a PDF attachment. Accepts:
  - a .eml file,
  - a JSON file with a base64url "raw" field (Gmail API messages.get format=RAW),
  - a JSON file wrapping either under "content".

Prints subject, date and a de-tagged text rendering (URLs removed). With
--pdf-dir, saves PDF attachments there and prints their text if `pdftotext`
is installed.

Usage:
    python decode_raw_email.py message.json [--max 6000] [--pdf-dir pdfs/]
"""
import argparse
import base64
import email
import html
import json
import re
import shutil
import subprocess
from email import policy
from pathlib import Path


def load_bytes(path):
    data = Path(path).read_bytes()
    try:
        obj = json.loads(data)
    except (ValueError, UnicodeDecodeError):
        return data
    if isinstance(obj, dict) and isinstance(obj.get("content"), str):
        inner = obj["content"]
        try:
            obj = json.loads(inner)
        except ValueError:
            return base64.urlsafe_b64decode(inner + "===")
    raw = obj.get("raw") if isinstance(obj, dict) else None
    if not raw:
        raise SystemExit("no 'raw' field found")
    return base64.urlsafe_b64decode(raw + "===")


def to_text(markup):
    markup = re.sub(r"(?is)<(style|script|head).*?</\1>", " ", markup)
    markup = re.sub(r"(?i)<br\s*/?>|</(p|div|tr|li|h\d)>", "\n", markup)
    text = html.unescape(re.sub(r"<[^>]+>", " ", markup))
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[ \t ͏‌​]+", " ", text)
    return re.sub(r"\n\s*\n+", "\n", text).strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--max", type=int, default=6000)
    ap.add_argument("--pdf-dir")
    a = ap.parse_args()

    msg = email.message_from_bytes(load_bytes(a.path), policy=policy.default)
    print("Subject:", msg.get("subject"))
    print("Date:", msg.get("date"))
    print("-" * 60)
    plain, htmls = [], []
    for part in msg.walk():
        ctype = part.get_content_type()
        if ctype == "text/plain":
            plain.append(part.get_content())
        elif ctype == "text/html":
            htmls.append(to_text(part.get_content()))
        elif ctype == "application/pdf" and a.pdf_dir:
            out = Path(a.pdf_dir)
            out.mkdir(parents=True, exist_ok=True)
            f = out / (part.get_filename() or "attachment.pdf")
            f.write_bytes(part.get_payload(decode=True))
            print(f"[saved PDF] {f}")
            if shutil.which("pdftotext"):
                print(subprocess.run(["pdftotext", "-layout", str(f), "-"], capture_output=True, text=True).stdout[: a.max])
    body = "\n".join(htmls) if htmls else "\n".join(plain)
    print(body[: a.max])


if __name__ == "__main__":
    main()
