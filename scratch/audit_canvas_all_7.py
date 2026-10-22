with open('docs/css/practicas-posicionamiento-flexbox-grid-canvas.md', 'r', encoding='utf-8') as f:
    text = f.read()

import re

practices = re.findall(r'## Práctica \d.*?:.*?(?=\n## Práctica |\n## Comparativa|\Z)', text, re.DOTALL)

for p in practices:
    p_title = p.split('\n')[0]
    pos_html = p.find('=== "Código HTML Base"')
    if pos_html != -1:
        snippet = p[pos_html:pos_html+200]
        pos_fence = snippet.find('```html')
        after_fence = snippet[pos_fence:].split('\n')[1] if pos_fence != -1 else ''
        html_indented = after_fence.startswith('    ')
    else:
        html_indented = False
        
    print(f"{p_title[:50]}: HTML_indented={html_indented}")
