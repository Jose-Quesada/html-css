with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    text = f.read()

pos_p2 = text.find('## Práctica 2:')
pos_p3 = text.find('## Práctica 3:')
p2_block = text[pos_p2:pos_p3]

pos_html = p2_block.find('=== "HTML"')
print(repr(p2_block[pos_html:pos_html+400]))
