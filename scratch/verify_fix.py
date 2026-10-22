with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    text = f.read()

assert 'overflow: hidden; /* Corta esquinas' not in text, "old overflow still present"
assert 'border-top-left-radius: calc(var(--radius-md) - 1px);' in text, "border-top-left-radius not in master"
assert 'overflow: hidden' in text, "overflow: hidden not in warning"
assert 'z-index' in text, "z-index not in warning"

with open('docs/css/practicas-posicionamiento-flexbox-grid-canvas.md', 'r', encoding='utf-8') as f:
    c_text = f.read()

assert 'overflow: hidden;' in c_text, "overflow: hidden not in canvas file"
assert 'border-top-left-radius' in c_text, "border-top-left-radius not in canvas file"

print("All assertions passed cleanly in python!")
