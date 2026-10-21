import re

with open('docs/css/practicas-posicionamiento-flexbox-grid-canvas.md', 'r', encoding='utf-8') as f:
    text = f.read()

pats = re.findall(r'## Práctica \d', text)
print('Practices found in canvas file:', pats)

canvases = re.findall(r'<canvas id="([^"]+)"', text)
print('Canvases found:', canvases)

canva_tags = re.findall(r'<canva id="([^"]+)"', text)
print('Canva tags found:', canva_tags)

css_tabs = re.findall(r'=== "CSS"', text)
print('CSS solution tabs in canvas file:', len(css_tabs))

with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    orig = f.read()
orig_pats = re.findall(r'## Práctica \d', orig)
print('Practices in original master file:', orig_pats)
orig_css = re.findall(r'=== "CSS"', orig)
print('CSS solution tabs in original master file:', len(orig_css))
