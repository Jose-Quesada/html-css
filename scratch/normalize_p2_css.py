with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    content = f.read()

pos_tab = content.find('=== "CSS"', content.find('## Práctica 2:'))
pos_code_start = content.find('```css title="practica-02-sticky-vs-fixed.css"', pos_tab)
# backtrack to beginning of line
pos_line_start = content.rfind('\n', 0, pos_code_start) + 1
pos_code_end = content.find('```', pos_code_start + 45) + 3

css_block = content[pos_line_start:pos_code_end]
lines = css_block.split('\n')

normalized_lines = []
for line in lines:
    stripped = line.strip()
    if stripped:
        normalized_lines.append('    ' + stripped)
    else:
        normalized_lines.append('')

new_block = '\n'.join(normalized_lines)
content = content[:pos_line_start] + new_block + content[pos_code_end:]

with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Normalized indentation to exactly 4 spaces!")
