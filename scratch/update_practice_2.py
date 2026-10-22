# Script to update Practice 2 across both files
import re

new_p2_requirements = """### 1. Escenario y Requerimientos

Maquetarás la vista de lectura y documentación de una academia online:

1. **Cabecera Adhesiva (`sticky-header`):**
    * La barra superior `.sticky-header` debe permanecer visible pegada al borde superior de la pantalla durante todo el desplazamiento (`position: sticky; top: 0;`) con `z-index: 100` y fondo oscuro (`#0f172a`).
    * Contiene el logotipo corporativo (`⚡ DominIA Academy`), un menú de navegación principal con los enlaces `Inicio`, `Artículos`, `Lecciones` y `Recursos`, y un botón de notificaciones con icono de campana `🔔` e insignia numérica roja (`.notification-badge`) superpuesta en la esquina superior derecha (`position: absolute; top: 0; right: 0;`).
2. **Cuerpo del Artículo y Cuadrícula Comparativa:**
    * Encabezado con título principal `Guía Maestra: Sticky vs Fixed en CSS` y subtítulo explicativo.
    * Una cuadrícula `.cards-grid` con dos tarjetas comparativas:
        * `.concept-card--sticky`: Título azul `1. Comportamiento Sticky`, explicación y badge `position: sticky; top: 0;`.
        * `.concept-card--fixed`: Título naranja `2. Comportamiento Fixed`, explicación y badge `position: fixed; bottom: 0;`.
    * Párrafos de lectura complementarios para garantizar suficiente recorrido de desplazamiento vertical en el navegador.
3. **Botón Volver Arriba (`fixed`):**
    * Un botón circular flotante `.btn-scroll-top` en la esquina inferior derecha con `position: fixed; bottom: 5rem; right: 1.5rem; z-index: 90;` y flecha `↑`.
4. **Banner de Consentimiento Fijo Inferior (`fixed`):**
    * Una barra fija inferior `.cookie-banner` que ocupa el 100% del ancho con `position: fixed; bottom: 0; left: 0; right: 0; z-index: 95;`.
    * Contiene el texto `🍪 Utilizamos cookies técnicas para garantizar el funcionamiento del aula.` y el botón `Aceptar todas`.
    * El elemento `body` debe reservar un margen inferior (`padding-bottom: 6rem;`) para que el banner fijo no tape el final del artículo."""

new_p2_html = """<!DOCTYPE html>
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
        <a href="#inicio" class="nav-link active">Inicio</a>
        <a href="#articulos" class="nav-link">Artículos</a>
        <a href="#lecciones" class="nav-link">Lecciones</a>
        <a href="#recursos" class="nav-link">Recursos</a>
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

new_p2_css = """/* ==========================================================================
   Práctica 2: Posicionamiento Sticky vs Fixed
   ========================================================================== */

:root {
  --color-primary: #2563eb;
  --color-primary-hover: #1d4ed8;
  --color-header-bg: #0f172a;
  --color-header-text: #f1f5f9;
  --color-accent-blue: #38bdf8;
  --color-accent-orange: #ea580c;
  --color-success: #10b981;
  --color-danger: #ef4444;
  --color-bg: #f8fafc;
  --color-card-bg: #ffffff;
  --color-text-main: #0f172a;
  --color-text-muted: #64748b;
  --color-border: #e2e8f0;
  
  --radius-md: 10px;
  --radius-sm: 6px;
  --shadow-card: 0 4px 12px rgba(0, 0, 0, 0.05);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: system-ui, -apple-system, sans-serif;
  background-color: var(--color-bg);
  color: var(--color-text-main);
  line-height: 1.6;
  /* PREVENCIÓN CRÍTICA: Espacio inferior para que el banner fijo no oculte el último párrafo */
  padding-bottom: 6rem;
}

/* 1. CABECERA ADHESIVA CON POSITION: STICKY */
.sticky-header {
  position: sticky;
  top: 0; /* Umbral exacto donde se congela al hacer scroll */
  z-index: 100; /* Asegura que flote sobre todo el contenido del artículo */
  background-color: var(--color-header-bg);
  border-bottom: 1px solid #1e293b;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.header-content {
  max-width: 900px;
  margin: 0 auto;
  padding: 0.75rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
}

/* Logotipo */
.logo {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  text-decoration: none;
  font-weight: 800;
  font-size: 1.05rem;
  color: var(--color-accent-blue);
}

.logo-icon {
  font-size: 1.15rem;
}

/* Menú de navegación */
.main-nav {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.nav-link {
  color: #cbd5e1;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  transition: color 0.15s ease;
}

.nav-link:hover,
.nav-link.active {
  color: #ffffff;
}

/* Botón de notificaciones con insignia absoluta */
.header-actions {
  display: flex;
  align-items: center;
}

.btn-notifications {
  position: relative; /* Contexto de coordenadas para la insignia absoluta */
  background: transparent;
  border: none;
  color: #ffffff;
  cursor: pointer;
  padding: 0.35rem;
  display: grid;
  place-items: center;
  font-size: 1.2rem;
}

.notification-badge {
  position: absolute;
  top: 0;
  right: 0;
  background-color: var(--color-danger);
  color: #ffffff;
  font-size: 0.65rem;
  font-weight: 800;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  border: 2px solid var(--color-header-bg);
}

/* 2. CONTENIDO PRINCIPAL Y ARTÍCULO */
.article-container {
  max-width: 900px;
  margin: 2rem auto;
  padding: 0 1.5rem;
}

.article-intro {
  margin-bottom: 2rem;
}

.article-title {
  font-size: 2rem;
  font-weight: 800;
  color: var(--color-text-main);
  letter-spacing: -0.02em;
  margin-bottom: 0.5rem;
}

.article-lead {
  font-size: 1.1rem;
  color: var(--color-text-muted);
}

/* Cuadrícula de Tarjetas Comparativas */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2.5rem;
}

.concept-card {
  background-color: var(--color-card-bg);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  box-shadow: var(--shadow-card);
  display: flex;
  flex-direction: column;
}

.concept-card--sticky {
  border-top: 4px solid var(--color-primary);
}

.concept-card--fixed {
  border-top: 4px solid var(--color-accent-orange);
}

.card-title {
  font-size: 1.15rem;
  font-weight: 700;
  margin-bottom: 0.75rem;
}

.concept-card--sticky .card-title {
  color: var(--color-primary);
}

.concept-card--fixed .card-title {
  color: var(--color-accent-orange);
}

.card-desc {
  font-size: 0.95rem;
  color: var(--color-text-muted);
  line-height: 1.6;
  margin-bottom: 1.25rem;
  flex-grow: 1;
}

.card-footer {
  margin-top: auto;
}

.badge {
  display: inline-block;
  font-family: monospace;
  font-size: 0.8rem;
  font-weight: 700;
  padding: 0.35rem 0.65rem;
  border-radius: var(--radius-sm);
}

.badge--sticky {
  background-color: #dbeafe;
  color: #1e40af;
}

.badge--fixed {
  background-color: #ffedd5;
  color: #9a3412;
}

/* Bloques de texto informativos para scroll */
.text-block {
  background-color: var(--color-card-bg);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  margin-bottom: 1.5rem;
}

.text-block h2 {
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: var(--color-text-main);
}

.text-block p {
  color: #334155;
  margin-bottom: 0.75rem;
}

.text-block p:last-child {
  margin-bottom: 0;
}

/* 3. BOTÓN FLOTANTE FIJO (POSITION: FIXED) */
.btn-scroll-top {
  position: fixed;
  bottom: 5rem;
  right: 1.5rem;
  z-index: 90;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background-color: var(--color-primary);
  color: #ffffff;
  display: grid;
  place-items: center;
  font-size: 1.25rem;
  font-weight: 700;
  text-decoration: none;
  box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
  transition: transform 0.15s ease, background-color 0.15s ease;
}

.btn-scroll-top:hover {
  transform: translateY(-3px);
  background-color: var(--color-primary-hover);
}

/* 4. BANNER DE CONSENTIMIENTO FIJO INFERIOR (POSITION: FIXED) */
.cookie-banner {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  width: 100%;
  z-index: 95;
  background-color: #1e293b;
  border-top: 1px solid #334155;
  box-shadow: 0 -4px 16px rgba(0, 0, 0, 0.2);
}

.cookie-content {
  max-width: 900px;
  margin: 0 auto;
  padding: 0.85rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.cookie-text {
  color: #f1f5f9;
  font-size: 0.9rem;
}

.btn-cookie {
  background-color: var(--color-success);
  color: #ffffff;
  border: none;
  padding: 0.45rem 1.15rem;
  border-radius: var(--radius-sm);
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  transition: opacity 0.15s ease;
}

.btn-cookie:hover {
  opacity: 0.9;
}"""

new_p2_rubric = """### 3. Puntos Críticos y Rúbrica de la Práctica 2

!!! tip "Diferencia de comportamiento en el flujo: Sticky vs Fixed"
    * **`position: sticky`** mantiene su espacio en el flujo normal del documento al cargar la página; solo conmuta a comportamiento flotante cuando el scroll alcanza su coordenada umbral (`top: 0`).
    * **`position: fixed`** extrae al elemento por completo del flujo desde el primer instante; no reserva espacio en el layout y se ancla de forma inmutable respecto a la ventana física (*Viewport*).

!!! success "Rúbrica de verificación (Práctica 2)"
    - [ ] **Cabecera adhesiva (`sticky`):** `.sticky-header` tiene `position: sticky; top: 0; z-index: 100;` y se mantiene visible durante todo el scroll.
    - [ ] **Estructura de cabecera:** La cabecera incluye el logotipo `⚡ DominIA Academy`, el menú con enlaces (`Inicio`, `Artículos`, `Lecciones`, `Recursos`) y el botón con campana `🔔`.
    - [ ] **Insignia numérica absoluta:** `.notification-badge` se posiciona de forma absoluta respecto al botón de notificaciones (`position: absolute; top: 0; right: 0;`).
    - [ ] **Cuadrícula comparativa:** Las tarjetas `.concept-card--sticky` y `.concept-card--fixed` explican claramente ambos comportamientos.
    - [ ] **Botón flotante fijo:** `.btn-scroll-top` usa `position: fixed; bottom: 5rem; right: 1.5rem; z-index: 90;`.
    - [ ] **Banner fijo de cookies:** `.cookie-banner` usa `position: fixed; bottom: 0; left: 0; width: 100%; z-index: 95;`.
    - [ ] **Reserva de espacio inferior:** `body` incluye `padding-bottom: 6rem;` para evitar que el banner fijo tape el último bloque de texto."""

# Update master file
with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    master = f.read()

p2_start = master.find('## Práctica 2:')
p3_start = master.find('## Práctica 3:')
p2_block = master[p2_start:p3_start]

# Replace in master:
# From ### 1. Escenario to ### 3.
p2_code_head = '### 2. Código Fuente de la Práctica 2'
p2_before_code = p2_block[:p2_block.find(p2_code_head)]
p2_new_section1 = p2_before_code[:p2_before_code.find('### 1. Escenario y Requerimientos')] + new_p2_requirements + '\n\n---\n\n'

p2_new_code_tabs = f"""{p2_code_head}

=== "HTML"

    ```html title="practica-02-sticky-vs-fixed.html"
{new_p2_html}
    ```

=== "CSS"

    ```css title="practica-02-sticky-vs-fixed.css"
{new_p2_css}
    ```

---

{new_p2_rubric}

"""

new_p2_master = p2_new_section1 + p2_new_code_tabs
master = master[:p2_start] + new_p2_master + master[p3_start:]

with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'w', encoding='utf-8') as f:
    f.write(master)

print("Updated master file Practice 2!")

# Update student canvas file
with open('docs/css/practicas-posicionamiento-flexbox-grid-canvas.md', 'r', encoding='utf-8') as f:
    student = f.read()

sp2_start = student.find('## Práctica 2:')
sp3_start = student.find('## Práctica 3:')
sp2_block = student[sp2_start:sp3_start]

sp2_canvas_start = sp2_block.find('=== "Lienzo Visual"')
sp2_html_start = sp2_block.find('=== "Código HTML Base"')
sp2_rubric_start = sp2_block.find('### 3.')

# Extract canvas tab content
sp2_canvas_tab = sp2_block[sp2_canvas_start:sp2_html_start]

sp2_new_section1 = sp2_block[:sp2_block.find('### 1. Escenario y Requerimientos')] + new_p2_requirements + '\n\n### 2. Lienzo Gráfico y Código HTML Base\n\n'

sp2_new_student_p2 = f"""{sp2_new_section1}{sp2_canvas_tab}=== "Código HTML Base"

    ```html title="practica-02-sticky-vs-fixed.html"
{new_p2_html}
    ```

---

{new_p2_rubric}

---

"""

student = student[:sp2_start] + sp2_new_student_p2 + student[sp3_start:]

with open('docs/css/practicas-posicionamiento-flexbox-grid-canvas.md', 'w', encoding='utf-8') as f:
    f.write(student)

print("Updated student canvas file Practice 2!")
