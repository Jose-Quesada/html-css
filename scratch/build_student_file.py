import re

with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    text = f.read()

with open('scratch/render_all_canvases.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

# Canvas dimensions per practice
canvas_dims = {
    1: 460,
    2: 500,
    3: 480,
    4: 490,
    5: 540,
    6: 550,
    7: 550
}

# Split intro and practices
intro_part = text[:text.find('## Práctica 1:')]

# Adjust frontmatter and intro
intro_part = intro_part.replace(
    'title: "CSS — Prácticas Integrales de Layout: Posicionamiento, Flexbox y Grid"',
    'title: "CSS — Prácticas de Layout (Vista del Alumno con Lienzo <canvas>)"'
)
intro_part = intro_part.replace(
    'description: "Itinerario formativo completo y secuencial de maquetación web moderna: desde los fundamentos de coordenadas espaciales (Posicionamiento), pasando por la alineación unidimensional (Flexbox), hasta la retícula bidimensional (CSS Grid) y proyectos de página completa."',
    'description: "Itinerario práctico de maquetación web con HTML5 y CSS3 sin soluciones CSS expuestas. El alumnado debe codificar las hojas de estilo hasta replicar con exactitud el objetivo visual renderizado en cada lienzo <canvas>."'
)

# Add student notice right after intro badges
notice = """
<div class="admonition tip">
<p class="admonition-title">Metodología de Trabajo: Reto de Maquetación con Lienzo Visual (&lt;canvas&gt;)</p>
<p>
Para desarrollar tu intuición espacial y rigor técnico como desarrollador frontend, <strong>este documento no incluye soluciones CSS para copiar y pegar</strong>. En cada práctica dispones de:
</p>
<ol>
  <li><strong>Lienzo Visual <code>&lt;canvas&gt;</code></strong>: Una representación gráfica pixel-perfect del objetivo a replicar (renderizada en mapa de bits en el navegador, sin estilos CSS en el DOM inspeccionable).</li>
  <li><strong>Código HTML Base</strong>: El marcado semántico limpio con las clases que debes estilizar en tu propio fichero <code>.css</code>.</li>
  <li><strong>Requerimientos Técnicos y Rúbrica</strong>: Los criterios de modelo de caja, posicionamiento, flexbox o grid requeridos.</li>
</ol>
</div>
"""
intro_part = intro_part.replace('</div>\n\nEn el desarrollo web profesional', '</div>\n' + notice + '\nEn el desarrollo web profesional')

# Extract each practice
pattern = r'(## Práctica (\d).*?)(?=\n## Práctica |\n## Comparativa|\Z)'
practices = list(re.finditer(pattern, text, re.DOTALL))

transformed_practices = []

for match in practices:
    p_text = match.group(1)
    p_num = int(match.group(2))
    h_dim = canvas_dims.get(p_num, 480)
    
    # Extract parts before === "HTML"
    html_tab_pos = p_text.find('=== "HTML"')
    if html_tab_pos == -1:
        transformed_practices.append(p_text)
        continue
    
    header_and_reqs = p_text[:html_tab_pos].strip()
    
    # Extract HTML code block
    html_match = re.search(r'=== "HTML"\s+(```html.*?\n\s+```)', p_text, re.DOTALL)
    if not html_match:
        html_code = '<!-- No HTML found -->'
    else:
        html_code = html_match.group(1)
    
    # Extract Checklist/Rubric after CSS
    # Find ### 3 or ### 4 or Lista de Verificación
    check_match = re.search(r'(### \d\. Lista de Verificación.*?)(?=\n## Práctica |\n## Comparativa|\Z)', p_text, re.DOTALL)
    if check_match:
        checklist = check_match.group(1).strip()
    else:
        checklist = ''
        
    canvas_block = f"""=== "Lienzo Visual <canvas>"

    !!! tip "Objetivo visual a replicar"
        Observa con detenimiento las coordenadas, alineaciones y proporciones en el siguiente lienzo gráfico. Debes conseguir este resultado visual exacto escribiendo tu propia hoja de estilos CSS. **El código CSS no está expuesto en el código fuente de la página.**

    <div class="browser-preview">
      <div class="browser-preview-bar">
        <span class="browser-preview-dot red"></span>
        <span class="browser-preview-dot yellow"></span>
        <span class="browser-preview-dot green"></span>
        <span style="font-family: monospace; font-size: 0.75rem; color: #64748b; margin-left: 0.5rem;">canvas://practica-0{p_num}-objetivo-visual</span>
      </div>
      <div class="browser-preview-body" style="background: #0f172a; text-align: center; padding: 1.5rem 0.5rem; overflow-x: auto;">
        <canva id="canva-practica-{p_num}" style="display:none;"></canva>
        <canvas id="canvas-practica-{p_num}" width="760" height="{h_dim}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.4);" aria-label="Lienzo gráfico con la visualización esperada de la Práctica {p_num}">
          Tu navegador no soporta el elemento canvas de HTML5.
        </canvas>
      </div>
    </div>

=== "Código HTML Base"

    {html_code}"""

    transformed_p = f"{header_and_reqs}\n\n### 2. Lienzo Gráfico y Código HTML Base\n\n{canvas_block}\n\n---\n\n{checklist}"
    transformed_practices.append(transformed_p)

# Extract comparativa if exists
comp_pos = text.find('## Comparativa y Guía de Decisión Arquitectónica')
if comp_pos != -1:
    comparativa = text[comp_pos:]
else:
    comparativa = ''

script_block = f"""

<!-- Motor de renderizado en cliente para los 7 lienzos <canvas> -->
<script>
{js_code}
</script>
"""

full_content = intro_part + "\n\n" + "\n\n---\n\n".join(transformed_practices) + "\n\n---\n\n" + comparativa + script_block

output_path = 'docs/css/practicas-posicionamiento-flexbox-grid-canvas.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(full_content)

print(f"Generated successfully: {output_path} ({len(full_content)} chars)")
