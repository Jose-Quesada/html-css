with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    text = f.read()

pos_p1 = text.find('## Práctica 1:')
pos_html = text.find('=== "HTML"', pos_p1)
print(repr(text[pos_html:pos_html+400]))
