"""
Reference Materials

Goal: Use this folder to locate and index reference documents without treating every PDF as an executable lesson.

Run from this folder with:
    python "Reference_Materials_practice.py"

This is a learning example. Review the code and dependencies before using it in production.
"""

from pathlib import Path

root = Path.cwd()
extensions = {".pdf", ".docx", ".pptx", ".xlsx", ".csv", ".ipynb", ".py"}
print("Reference files in the current folder and subfolders:")
for path in sorted(root.rglob("*")):
    if path.is_file() and path.suffix.lower() in extensions:
        print(f"{path.suffix.lower():7} {path.relative_to(root)}")
