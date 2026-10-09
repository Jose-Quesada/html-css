import re
from pathlib import Path

dirs = [
    Path("E:/00. Clases/Apuntes/Desarrollo_Interfaces"),
    Path("E:/00. Clases/Apuntes/Diseño interfaces")
]

media_pattern = re.compile(r'[^"\'`\s<>]+\.(?:mp4|webm|ogv|ogg|mp3|wav|vtt|m4a|aac|flac)', re.IGNORECASE)

found = []
for d in dirs:
    if not d.exists():
        print(f"Directory {d} does not exist!")
        continue
    for f in d.rglob("*.md"):
        content = f.read_text(encoding="utf-8")
        lines = content.splitlines()
        for idx, line in enumerate(lines, 1):
            if any(ext in line.lower() for ext in [".mp4", ".webm", ".ogv", ".ogg", ".mp3", ".wav", ".vtt", ".m4a", ".aac"]):
                # check if line contains an HTML tag, link, or media reference
                if ("http://" not in line and "https://" not in line):
                    found.append((f, idx, line.strip()))

print(f"Total matching lines found: {len(found)}")
for f, idx, line in found:
    print(f"{f}:{idx} -> {line[:120]}")
