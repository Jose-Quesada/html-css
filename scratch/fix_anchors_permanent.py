for fname in ['docs/css/practicas-posicionamiento-flexbox-grid.md', 'docs/css/practicas-posicionamiento-flexbox-grid-canvas.md']:
    with open(fname, 'r', encoding='utf-8') as f:
        t = f.read()
    t = t.replace('href="#inicio"', 'href="#"')
    t = t.replace('href="#articulos"', 'href="#"')
    t = t.replace('href="#lecciones"', 'href="#"')
    t = t.replace('href="#recursos"', 'href="#"')
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(t)
    print(f"Cleaned anchors in {fname}")
