import re

with open('docs/css/practicas-posicionamiento-flexbox-grid-canvas.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix title in frontmatter
text = re.sub(
    r'title:\s*"CSS — Prácticas de Layout \(Vista del Alumno con Lienzo <canvas>\)"',
    'title: "CSS — Prácticas de Layout (Vista del Alumno - Lienzo Canvas)"',
    text
)

# 2. Fix tab titles: remove <canvas> from tab headers
text = text.replace('=== "Lienzo Visual <canvas>"', '=== "Lienzo Visual"')

# 3. Fix math formula
text = text.replace(
    '$\\text{grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));}$',
    '`grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));`'
)
# Also check if original has it
text = text.replace(
    r'$\(\text{grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));}\)$',
    '`grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));`'
)

with open('docs/css/practicas-posicionamiento-flexbox-grid-canvas.md', 'w', encoding='utf-8') as f:
    f.write(text)

# Also fix the math formula in docs/css/practicas-posicionamiento-flexbox-grid.md
with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    master_text = f.read()

master_text = master_text.replace(
    '$\\text{grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));}$',
    '`grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));`'
)
with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'w', encoding='utf-8') as f:
    f.write(master_text)

print('Updated files!')
