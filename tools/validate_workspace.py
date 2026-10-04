"""Read-only structural checks for StudyNest. Python 3.9+, no packages."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import os
import re
import sys

REQUIRED = (
    "AGENTS.md", "CLAUDE.md", "START_HERE.md", "VERSION",
    "context/STUDENT_PROFILE.md", "context/DASHBOARD.md",
    "context/MEMORY.md", "context/HANDOFF.md",
    "courses/README.md", "docs/INSTALLATION.md", "docs/PROMPTS.md",
    "workflows/ONBOARDING.md", "workflows/SOURCE_INTAKE.md",
    "workflows/STUDY.md", "workflows/EXAMS.md",
    "workflows/ASSIGNMENTS.md", "workflows/PROGRESS.md",
    "modules/HEALTHCARE.md", "templates/course/README.md",
    "templates/exam/Priority Map.md", "templates/assignment/README.md",
)
STARTUP = (
    "AGENTS.md", "CLAUDE.md", "START_HERE.md",
    "context/STUDENT_PROFILE.md", "context/DASHBOARD.md",
    "context/MEMORY.md", "context/HANDOFF.md",
)
def headings(body):
    anchors, counts = set(), {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", body, re.M):
        slug = re.sub(r"[^\w\s-]", "", heading.lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        anchors.add(slug if count == 0 else f"{slug}-{count}")
    return anchors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--blank", action="store_true",
                        help="Also require no live courses, source files, or inbox uploads.")
    args = parser.parse_args()
    root = args.root.resolve()
    errors, warnings = [], []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"Missing required file: {name}")
    texts = {}
    skip = {".git", "sources", "outputs", "workfiles", "archive",
            "node_modules", ".venv", "__pycache__"}
    for folder, dirs, names in os.walk(root):
        dirs[:] = [d for d in dirs if d not in skip]
        for name in names:
            if name.endswith(".md"):
                path = Path(folder) / name
                try:
                    texts[path.resolve()] = path.read_text(encoding="utf-8")
                except (OSError, UnicodeError) as exc:
                    errors.append(f"Unreadable Markdown: {path.relative_to(root)} ({exc})")
    checked = 0
    fence = chr(96) * 3
    for path, body in texts.items():
        prose = re.sub("^" + fence + r"[^\n]*\n.*?^" + fence + r"\s*$",
                       "", body, flags=re.M | re.S)
        for raw in re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", prose):
            target = raw.strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("//"):
                continue
            checked += 1
            local = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not local.is_relative_to(root):
                errors.append(f"Link leaves workspace: {path.relative_to(root)} -> {target}")
            elif not local.exists():
                errors.append(f"Broken link: {path.relative_to(root)} -> {target}")
            elif parsed.fragment and local.suffix == ".md":
                if unquote(parsed.fragment) not in headings(texts.get(local, "")):
                    errors.append(f"Missing heading: {path.relative_to(root)} -> {target}")
    if (root / "CLAUDE.md").exists():
        if "@AGENTS.md" not in (root / "CLAUDE.md").read_text(encoding="utf-8"):
            errors.append("CLAUDE.md must import the shared AGENTS.md.")
    if args.blank:
        live = root / "courses"
        extras = sorted(p.name for p in live.iterdir() if p.name != "README.md") if live.exists() else []
        if extras:
            errors.append("Live courses present in blank template: " + ", ".join(extras))
        for folder in (root / "inbox", *root.glob("**/sources")):
            if folder.is_dir():
                extras = [p.name for p in folder.iterdir() if p.name != "README.md"]
                if extras:
                    errors.append(f"Nonblank upload/source folder: {folder.relative_to(root)}")
        profile = root / "context/STUDENT_PROFILE.md"
        if profile.exists() and "Setup status: not started" not in profile.read_text(encoding="utf-8"):
            errors.append("Blank template profile is already personalized.")
    total_words = total_bytes = 0
    for name in STARTUP:
        path = root / name
        if path.exists():
            body = path.read_text(encoding="utf-8")
            words = len(body.split())
            total_words += words
            total_bytes += len(body.encode("utf-8"))
            print(f"Startup: {name}: {words} words")
            if words > 600:
                warnings.append(f"Startup file is getting long: {name}")
    print(f"Startup total: {total_words} words, {total_bytes} UTF-8 bytes.")
    print("Word/byte counts are not provider token measurements.")
    print(f"Checked {len(texts)} Markdown files and {checked} local links.")
    for warning in warnings:
        print("WARNING:", warning)
    for error in errors:
        print("ERROR:", error)
    print("PASS: structural checks." if not errors else "FAIL: structural checks.")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
