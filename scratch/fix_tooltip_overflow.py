import re

# 1. Update docs/css/practicas-posicionamiento-flexbox-grid.md
with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Update requirements
old_req1 = """1. **Bloque Contenedor:**
    * El elemento `.card-product` debe tener ancho acotado (`max-width: 320px`), fondo blanco, borde y esquinas redondeadas.
    * El contenedor de la imagen `.product-media` debe declarar **`position: relative;`** para actuar como sistema de coordenadas de sus elementos hijos absolutos."""

new_req1 = """1. **Bloque Contenedor:**
    * El elemento `.card-product` debe tener ancho acotado (`max-width: 320px`), fondo blanco, borde y esquinas redondeadas. **No debes usar `overflow: hidden;` en `.card-product`**, ya que recortaría físicamente cualquier elemento hijo que sobresalga (como el *tooltip* superior), sin importar su nivel de `z-index`.
    * El contenedor de la imagen `.product-media` debe declarar **`position: relative;`** para actuar como sistema de coordenadas de sus elementos hijos absolutos, y aplicar `border-top-left-radius` y `border-top-right-radius` para adaptarse al borde redondeado superior de la tarjeta."""

text = text.replace(old_req1, new_req1)

# Update CSS
old_css_card = """    .card-product {
      background-color: var(--color-card-bg);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-card);
      max-width: 320px;
      width: 100%;
      overflow: hidden; /* Corta esquinas de la imagen según el radio */
    }

    /* 1. ZONA MULTIMEDIA: Contexto de referencia con position: relative */
    .product-media {
      position: relative; /* CLAVE!: Sistema de coordenadas para sus hijos absolutos */
      background: linear-gradient(135deg, #e0f2fe 0%, #dbeafe 100%);
      height: 220px;
      display: grid;
      place-items: center;
    }"""

new_css_card = """    .card-product {
      background-color: var(--color-card-bg);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-card);
      max-width: 320px;
      width: 100%;
      /* ¡IMPORTANTE!: No usar overflow: hidden aquí.
         overflow: hidden recorta físicamente los elementos que sobresalen de la caja
         (como el tooltip flotante superior), ignorando por completo el z-index. */
    }

    /* 1. ZONA MULTIMEDIA: Contexto de referencia con position: relative */
    .product-media {
      position: relative; /* CLAVE!: Sistema de coordenadas para sus hijos absolutos */
      background: linear-gradient(135deg, #e0f2fe 0%, #dbeafe 100%);
      height: 220px;
      display: grid;
      place-items: center;
      /* Redondeo explícito de esquinas superiores para respetar el borde de la tarjeta sin overflow: hidden */
      border-top-left-radius: calc(var(--radius-md) - 1px);
      border-top-right-radius: calc(var(--radius-md) - 1px);
    }"""

text = text.replace(old_css_card, new_css_card)

# Update section 3
old_sec3 = """### 3. Puntos Críticos y Rúbrica de la Práctica 1

!!! tip "¿Qué ocurre si eliminas `position: relative` de `.product-media`?"
    Si comentas la regla `position: relative;` del contenedor multimedia, el navegador buscará hacia arriba en el árbol DOM hasta el elemento raíz `<html>`. Como consecuencia, la insignia `-25%` y el botón de favoritos volarán a la esquina superior de la ventana del navegador, saliéndose por completo de la tarjeta.

!!! success "Rúbrica de verificación (Práctica 1)"
    - [ ] **Referencia espacial:** `.product-media` tiene `position: relative;` y sirve de origen de coordenadas `(0,0)`.
    - [ ] **Insignia fija en esquina:** `.badge-discount` usa `position: absolute; top: 0.75rem; left: 0.75rem;`.
    - [ ] **Botón en esquina:** `.btn-favorite` usa `position: absolute; top: 0.75rem; right: 0.75rem;`.
    - [ ] **Tooltip flotante:** El mensaje explicativo descansa encima del botón con `bottom: calc(100% + 8px); left: 50%; transform: translateX(-50%);` y solo se muestra en `:hover` o `:focus-visible`."""

new_sec3 = """### 3. Puntos Críticos y Rúbrica de la Práctica 1

!!! warning "La Trampa de `overflow: hidden` frente a `z-index`: ¿Por qué se cortaba el Tooltip?"
    Un error clásico al maquetar tarjetas con elementos flotantes es añadir `overflow: hidden;` a `.card-product` para recortar automáticamente la imagen superior.
    
    * **¿Por qué falla el tooltip aunque tenga `z-index: 10`?**
      `overflow: hidden` crea una frontera física de recorte (*clipping path*). Aunque apliques `z-index: 10`, `z-index: 999` o `z-index: 999999`, **`z-index` únicamente define el orden de apilamiento en el eje perpendicular (profundidad Z), pero jamás puede anular ni atravesar el recorte geométrico de un contenedor ancestro con `overflow: hidden`**.
    * **La solución arquitectónica correcta:**
      1. Quitar `overflow: hidden;` de la tarjeta padre `.card-product`.
      2. Aplicar `border-top-left-radius` y `border-top-right-radius` directamente a `.product-media` para mantener el acabado visual limpio sin amputar los elementos flotantes.

!!! tip "¿Qué ocurre si eliminas `position: relative` de `.product-media`?"
    Si comentas la regla `position: relative;` del contenedor multimedia, el navegador buscará hacia arriba en el árbol DOM hasta el elemento raíz `<html>`. Como consecuencia, la insignia `-25%` y el botón de favoritos volarán a la esquina superior de la ventana del navegador, saliéndose por completo de la tarjeta.

!!! success "Rúbrica de verificación (Práctica 1)"
    - [ ] **Referencia espacial:** `.product-media` tiene `position: relative;` y sirve de origen de coordenadas `(0,0)`.
    - [ ] **Sin recorte de desbordamiento:** `.card-product` no tiene `overflow: hidden;`, permitiendo que el `.tooltip` sobresalga y se lea al completo sin amputarse.
    - [ ] **Insignia fija en esquina:** `.badge-discount` usa `position: absolute; top: 0.75rem; left: 0.75rem;`.
    - [ ] **Botón en esquina:** `.btn-favorite` usa `position: absolute; top: 0.75rem; right: 0.75rem;`.
    - [ ] **Tooltip flotante:** El mensaje explicativo descansa encima del botón con `bottom: calc(100% + 8px); left: 50%; transform: translateX(-50%);` y solo se muestra en `:hover` o `:focus-visible`."""

text = text.replace(old_sec3, new_sec3)

with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated master practice file!')

# 2. Update docs/css/practicas-posicionamiento-flexbox-grid-canvas.md
with open('docs/css/practicas-posicionamiento-flexbox-grid-canvas.md', 'r', encoding='utf-8') as f:
    c_text = f.read()

c_text = c_text.replace(old_req1, new_req1)

# In canvas file, ensure Section 3 is present for Practice 1
# Find end of Practice 1 HTML tab and check if section 3 is there
p1_end_html = 'Añadir a la Cesta</button>\n          </div>\n\n        </article>\n      </main>\n\n    </body>\n    </html>\n    ```'
if p1_end_html in c_text:
    target_split = p1_end_html + '\n\n---\n\n\n\n---\n\n## Práctica 2:'
    target_clean = p1_end_html + '\n\n---\n\n' + new_sec3 + '\n\n---\n\n## Práctica 2:'
    if target_split in c_text:
        c_text = c_text.replace(target_split, target_clean)
        print('Injected Section 3 into canvas file (clean replacement)')
    else:
        # try more flexible replacement
        p1_pos = c_text.find('practica-01-tarjeta-posicionamiento.html')
        p2_pos = c_text.find('## Práctica 2:')
        code_end_pos = c_text.find('```', p1_pos + 50) + 3
        # replace between code_end_pos and p2_pos
        c_text = c_text[:code_end_pos] + '\n\n---\n\n' + new_sec3 + '\n\n---\n\n' + c_text[p2_pos:]
        print('Injected Section 3 into canvas file (slice replacement)')

with open('docs/css/practicas-posicionamiento-flexbox-grid-canvas.md', 'w', encoding='utf-8') as f:
    f.write(c_text)

print('Updated student canvas practice file!')
