with open('docs/css/practicas-posicionamiento-flexbox-grid-canvas.md', 'r', encoding='utf-8') as f:
    text = f.read()

pos_p2 = text.find('## Práctica 2:')
pos_html = text.find('=== "Código HTML Base"', pos_p2)
print(repr(text[pos_html:pos_html+400]))
