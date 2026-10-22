raw_html_p2 = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Práctica 2: Posicionamiento — Sticky vs Fixed</title>
  <link rel="stylesheet" href="practica-02-sticky-vs-fixed.css">
</head>
<body>

  <!-- 1. CABECERA ADHESIVA (POSITION: STICKY) -->
  <header class="sticky-header">
    <div class="header-content">
      <!-- Logotipo de la academia -->
      <a href="#" class="logo">
        <span class="logo-icon">⚡</span>
        <span class="logo-text">DominIA Academy</span>
      </a>

      <!-- Menú de navegación principal -->
      <nav class="main-nav" aria-label="Navegación principal">
        <a href="#" class="nav-link active">Inicio</a>
        <a href="#" class="nav-link">Artículos</a>
        <a href="#" class="nav-link">Lecciones</a>
        <a href="#" class="nav-link">Recursos</a>
      </nav>

      <!-- Zona de acciones con campana e insignia absoluta -->
      <div class="header-actions">
        <button type="button" class="btn-notifications" aria-label="Notificaciones">
          <span class="bell-icon">🔔</span>
          <span class="notification-badge" aria-label="3 notificaciones nuevas">3</span>
        </button>
      </div>
    </div>
  </header>

  <!-- 2. CONTENIDO PRINCIPAL CON TARJETAS COMPARATIVAS Y SCROLL EXTENSO -->
  <main class="article-container">
    <header class="article-intro">
      <h1 class="article-title">Guía Maestra: Sticky vs Fixed en CSS</h1>
      <p class="article-lead">
        Aprende la diferencia operativa entre elementos anclados al flujo y fijados a la ventana.
      </p>
    </header>

    <!-- Tarjetas comparativas principales -->
    <section class="cards-grid">
      <!-- Tarjeta 1: Comportamiento Sticky -->
      <article class="concept-card concept-card--sticky">
        <h2 class="card-title">1. Comportamiento Sticky</h2>
        <p class="card-desc">
          El elemento fluye con el scroll hasta alcanzar top: 0, donde queda congelado. 
          Requiere que su contenedor padre mantenga altura en pantalla.
        </p>
        <div class="card-footer">
          <span class="badge badge--sticky">position: sticky; top: 0;</span>
        </div>
      </article>

      <!-- Tarjeta 2: Comportamiento Fixed -->
      <article class="concept-card concept-card--fixed">
        <h2 class="card-title">2. Comportamiento Fixed</h2>
        <p class="card-desc">
          Se extrae por completo del flujo y se ancla al viewport físico de la pantalla. 
          No se mueve jamás al hacer scroll, independientemente de los padres.
        </p>
        <div class="card-footer">
          <span class="badge badge--fixed">position: fixed; bottom: 0;</span>
        </div>
      </article>
    </section>

    <!-- Secciones de texto extendido para garantizar recorrido de scroll holgado -->
    <section class="text-block">
      <h2>3. Profundizando en el Mecanismo de Sticky</h2>
      <p>
        A diferencia de <code>fixed</code>, un elemento <code>sticky</code> respeta su hueco inicial en el documento. 
        No requiere compensaciones artificiales de <code>padding-top</code> en el <code>body</code>. 
        Al hacer scroll y alcanzar el umbral declarado (por ejemplo <code>top: 0</code>), conmuta su renderizado 
        a fijo relativo a la pantalla hasta que su contenedor ancestro finaliza.
      </p>
    </section>

    <section class="text-block">
      <h2>4. El Funcionamiento Inmutable de Fixed</h2>
      <p>
        Los elementos <code>fixed</code> se posicionan siempre respecto al <em>Viewport</em> (la ventana del navegador). 
        Por este motivo son la solución obligada para barras de consentimiento, botones flotantes de ayuda o retorno 
        al inicio (FAB) y ventanas modales de diálogo.
      </p>
    </section>

    <section class="text-block">
      <h2>5. La Jerarquía de Capas con z-index</h2>
      <p>
        Tanto la cabecera adhesiva (<code>z-index: 100</code>) como los elementos fijos inferiores 
        (<code>z-index: 90</code> y <code>95</code>) deben declarar niveles de apilamiento superiores al contenido 
        estándar para evitar que imágenes o bloques de código los oculten durante el desplazamiento.
      </p>
    </section>
  </main>

  <!-- 3. BOTÓN FLOTANTE FIJO (POSITION: FIXED) -->
  <a href="#" class="btn-scroll-top" title="Volver al principio" aria-label="Volver al principio">
    ↑
  </a>

  <!-- 4. BANNER DE CONSENTIMIENTO FIJO INFERIOR (POSITION: FIXED) -->
  <aside class="cookie-banner" role="region" aria-label="Aviso de privacidad">
    <div class="cookie-content">
      <p class="cookie-text">
        🍪 Utilizamos cookies técnicas para garantizar el funcionamiento del aula.
      </p>
      <div class="cookie-actions">
        <button type="button" class="btn-cookie">Aceptar todas</button>
      </div>
    </div>
  </aside>

</body>
</html>"""

# Format with exact 4-space indentation
indented_html_lines = []
indented_html_lines.append('    ```html title="practica-02-sticky-vs-fixed.html"')
for line in raw_html_p2.split('\n'):
    if line.strip():
        indented_html_lines.append('    ' + line)
    else:
        indented_html_lines.append('')
indented_html_lines.append('    ```')

formatted_html_block = '\n'.join(indented_html_lines)

# 1. Update master file
with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    master = f.read()

pos_p2 = master.find('## Práctica 2:')
pos_html_tab = master.find('=== "HTML"', pos_p2)
pos_css_tab = master.find('=== "CSS"', pos_html_tab)

# Replace between === "HTML" and === "CSS"
old_html_section = master[pos_html_tab:pos_css_tab]
new_html_section = f'=== "HTML"\n\n{formatted_html_block}\n\n'

master = master[:pos_html_tab] + new_html_section + master[pos_css_tab:]

with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'w', encoding='utf-8') as f:
    f.write(master)

print("Updated master file with indented HTML in Practice 2!")

# 2. Update student canvas file
with open('docs/css/practicas-posicionamiento-flexbox-grid-canvas.md', 'r', encoding='utf-8') as f:
    canvas_text = f.read()

c_p2 = canvas_text.find('## Práctica 2:')
c_html_tab = canvas_text.find('=== "Código HTML Base"', c_p2)
c_sec3 = canvas_text.find('### 3.', c_html_tab)
if c_sec3 == -1:
    c_sec3 = canvas_text.find('---', c_html_tab + 30)

# Replace the HTML block inside === "Código HTML Base"
c_new_html_section = f'=== "Código HTML Base"\n\n{formatted_html_block}\n\n---\n\n'
canvas_text = canvas_text[:c_html_tab] + c_new_html_section + canvas_text[c_sec3:]

with open('docs/css/practicas-posicionamiento-flexbox-grid-canvas.md', 'w', encoding='utf-8') as f:
    f.write(canvas_text)

print("Updated student canvas file with indented HTML in Practice 2!")
