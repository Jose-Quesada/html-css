with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.startswith('=== "CSS"'):
        print(f"Line {i+1}: {line.strip()}")
        for j in range(i+1, min(len(lines), i+6)):
            print(f"  Line {j+1}: repr={repr(lines[j][:20])}")
