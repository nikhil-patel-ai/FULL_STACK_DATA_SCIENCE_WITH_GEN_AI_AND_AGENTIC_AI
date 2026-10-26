"""
Images

Goal: Explore the files in this subfolder and understand how they support the Machine Learning syllabus.

Run from this folder with:
    python "Images_practice.py"

This is a learning example. Review the code and dependencies before using it in production.
"""

from pathlib import Path

folder = Path.cwd()
print("Current folder:", folder)
files = sorted(p for p in folder.iterdir() if p.is_file())
folders = sorted(p for p in folder.iterdir() if p.is_dir())

print("\nFiles:")
for item in files:
    print(f"- {item.name} ({item.stat().st_size:,} bytes)")
print("\nSubfolders:")
for item in folders:
    print(f"- {item.name}")

# Open data or documents only after checking their file type and contents.
