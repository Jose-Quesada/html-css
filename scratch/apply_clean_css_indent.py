from update_practice_2 import new_p2_css

indented_css_lines = []
indented_css_lines.append('    ```css title="practica-02-sticky-vs-fixed.css"')
for line in new_p2_css.split('\n'):
    if line.strip():
        indented_css_lines.append('    ' + line)
    else:
        indented_css_lines.append('')
indented_css_lines.append('    ```')

final_css_block = '\n'.join(indented_css_lines)

with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    text = f.read()

pos_p2 = text.find('## Práctica 2:')
pos_tab = text.find('=== "CSS"', pos_p2)
pos_block_start = text.find('```css title="practica-02-sticky-vs-fixed.css"', pos_tab)
pos_line_start = text.rfind('\n', 0, pos_block_start) + 1
pos_block_end = text.find('```', pos_block_start + 45) + 3

text = text[:pos_line_start] + final_css_block + text[pos_block_end:]

with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied perfectly indented CSS to Practice 2 in master file!")
