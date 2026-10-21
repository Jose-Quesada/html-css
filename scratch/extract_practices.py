import re

with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Find each practice
pattern = r'(## Práctica \d.*?)(?=\n## Práctica |\n## Comparativa|\Z)'
practices = re.findall(pattern, text, re.DOTALL)
print(f'Total practices found: {len(practices)}')

for idx, p in enumerate(practices, 1):
    title = p.split('\n')[0]
    has_html = '=== "HTML"' in p
    has_css = '=== "CSS"' in p
    print(f'Practice {idx}: {title} | HTML: {has_html} | CSS: {has_css}')
