with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    text = f.read()

pos1 = text.find('## Práctica 2:')
pos2 = text.find('=== "CSS"', pos1)
print(repr(text[pos2-20:pos2+350]))
