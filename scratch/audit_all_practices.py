with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Check each practice
practices = re.findall(r'## Práctica \d:.*?(?=\n## Práctica |\n## Comparativa|\Z)', text, re.DOTALL)

for p in practices:
    p_title = p.split('\n')[0]
    # Check === "HTML" and === "CSS"
    has_html_tab = '=== "HTML"' in p
    has_css_tab = '=== "CSS"' in p
    
    # Check if html code is indented
    pos_html = p.find('=== "HTML"')
    if pos_html != -1:
        snippet = p[pos_html:pos_html+200]
        # check line after ```html
        pos_fence = snippet.find('```html')
        after_fence = snippet[pos_fence:].split('\n')[1] if pos_fence != -1 else ''
        html_indented = after_fence.startswith('    ')
    else:
        html_indented = False
        
    pos_css = p.find('=== "CSS"')
    if pos_css != -1:
        snippet = p[pos_css:pos_css+200]
        pos_fence = snippet.find('```css')
        after_fence = snippet[pos_fence:].split('\n')[1] if pos_fence != -1 else ''
        css_indented = after_fence.startswith('    ')
    else:
        css_indented = False
        
    print(f"{p_title[:45]}: HTML_tab={has_html_tab} HTML_indented={html_indented} | CSS_tab={has_css_tab} CSS_indented={css_indented}")
