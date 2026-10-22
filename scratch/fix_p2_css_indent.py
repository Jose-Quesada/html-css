with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    content = f.read()

pos_tab = content.find('=== "CSS"', content.find('## Práctica 2:'))
pos_code_start = content.find('```css title="practica-02-sticky-vs-fixed.css"', pos_tab)
pos_code_end = content.find('```', pos_code_start + 45) + 3

css_block = content[pos_code_start:pos_code_end]
lines = css_block.split('\n')

# Indent all lines by 4 spaces
indented_lines = []
for line in lines:
    if line.strip():
        # if not already indented by 4 spaces
        if not line.startswith('    '):
            indented_lines.append('    ' + line)
        else:
            indented_lines.append(line)
    else:
        indented_lines.append('')

new_css_block = '\n'.join(indented_lines)

content = content[:pos_code_start] + new_css_block + content[pos_code_end:]

with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Indented Practice 2 CSS block successfully!")
