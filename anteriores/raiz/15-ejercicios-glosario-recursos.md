---
title: "Unidad 15 — Ejercicios, glosario y recursos"
description: "Banco de ejercicios por niveles con soluciones, glosario técnico español-inglés y listado de fuentes oficiales para continuar estudiando."
modulo: "LMH (0373) / DIW (0615)"
unidad: 15
fecha: "2026-09-06"
---

# Unidad 15 · Ejercicios, glosario y recursos

## PARTE A · EJERCICIOS

Consejo: resuelve primero en papel/código y compara después. Los enunciados están marcados por la unidad que evalúan.

### Nivel medio

**E1 (U01/U02).** Calcula la especificidad de estos selectores y ordena de menor a mayor:

```text
a) #nav ul li a:hover
b) .card .card__titulo
c) article :is(h2, h3) p
d) :where(.a, .b) > span
e) #main .post:not(.borrador)
```

<details><summary>Solución</summary>

- d) `:where()` = 0 + `span` tipo → **0-0-1**
- b) dos clases → **0-2-0**
- c) `:is(h2,h3)` toma el máximo (tipo) + `p` tipo → **0-0-2**
- a) ID + 3 tipos + pseudo-clase → **1-1-3**
- e) ID + 2 clases (`:not` cuenta su argumento) → **1-2-0**

Orden: d < c < b < e < a.
</details>

**E2 (U03).** Con `box-sizing: content-box`, un elemento tiene `width: 300px; padding: 16px; border: 4px solid`. ¿Cuánto mide la caja? ¿Y si cambias a `border-box`? Si además hay dos hermanos con `margin: 20px 0`, ¿cuánto espacio hay entre ellos?

<details><summary>Solución</summary>

- `content-box`: 300 + 16·2 + 4·2 = **340 px**.
- `border-box`: **300 px** (padding y borde incluidos).
- Márgenes colapsan: el espacio entre hermanos es **20 px** (el máximo), no 40.
</details>

**E3 (U04).** Un modal con `position: fixed` se desplaza cuando abres un carrusel con `transform: translateX()`. Explica por qué y da dos soluciones.

<details><summary>Solución</summary>

El `transform` del carrusel (o de un ancestro del modal) convierte ese ancestro en **bloque contenedor** del `fixed`, que deja de referirse al viewport. Soluciones: (1) montar el modal directamente bajo `<body>` (portal); (2) eliminar el `transform` de la cadena de ancestros del modal (usar `translate` solo en el carrusel interno sin que el modal esté dentro).
</details>

**E4 (U05).** Escribe el CSS de una navbar: logo a la izquierda, enlaces a la derecha, todo verticalmente centrado, con envoltura en móvil.

<details><summary>Solución</summary>

```css
.nav { display: flex; flex-wrap: wrap; align-items: center; gap: 1rem; }
.nav .logo { margin-inline-end: auto; }
.nav ul { display: flex; flex-wrap: wrap; gap: .5rem; list-style: none; margin: 0; padding: 0; }
```
</details>

**E5 (U06).** Una galería debe mostrar 4 columnas de mínimo 220 px en desktop, 2 en tablet y 1 en móvil, sin media queries. Escríbelo y explica `auto-fit` vs `auto-fill`.

<details><summary>Solución</summary>

```css
.galeria {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(220px, 100%), 1fr));
  gap: 1rem;
}
```
`auto-fit` colapsa las columnas vacías estirando las ocupadas (look elástico); `auto-fill` mantiene los «slots» vacíos visibles. El `min(220px, 100%)` evita desborde en contenedores más estrechos que 220 px.
</details>

**E6 (U08).** Define una escala tipográfica fluida: `h1` de 2 rem en 360 px hasta 3.5 rem en 1200 px usando `clamp()`. Muestra el cálculo aproximado.

<details><summary>Solución</summary>

Método de interpolación lineal entre dos puntos (tamaño en función del ancho del viewport):

1. Pendiente: `m = Δtamaño / Δancho = (3.5 − 2) rem / (1200 − 360) px = 1.5/840 ≈ 0.001786 rem/px`.
2. Pasamos a `vw` (como `100vw = W px`): `m_vw = 0.001786 × 100 ≈ 0.1786vw`.
3. Término independiente: `b = tamaño_min − m_vw × ancho_min(en vw) = 2rem − 0.1786 × 3.6 ≈ 1.357rem`.

Comprobación: a 360 px → 1.357 + 0.1786·3.6 = **2 rem** ✓ · a 1200 px → 1.357 + 0.1786·12 = **3.5 rem** ✓

```css
h1 { font-size: clamp(2rem, 1.357rem + 0.179vw, 3.5rem); }
```
(Las calculadoras de tipografía fluida hacen exactamente este cálculo; lo importante es dominar el método.)
</details>

**E7 (U10).** Un widget debe mostrarse en horizontal (imagen izquierda) si su contenedor supera 320 px, sea en sidebar o en main. Escríbelo con container queries y unidades de contenedor.

<details><summary>Solución</summary>

```css
.widget-wrap { container-type: inline-size; container-name: widget; }
@container widget (min-width: 320px) {
  .widget { display: grid; grid-template-columns: 30cqw 1fr; gap: 1rem; }
}
/* Base (vertical): */
.widget { display: grid; gap: .5rem; }
```
</details>

### Nivel avanzado

**E8 (U02/U12).** Sin JavaScript, construye un acordeón accesible-básico con `:has()` y `details/summary` estilizado, explicando cada selector.

<details><summary>Solución</summary>

```html
<details class="acordeon">
  <summary>Pregunta 1</summary>
  <div class="acordeon__cuerpo"><p>Respuesta…</p></div>
</details>
```

```css
.acordeon summary { cursor: pointer; padding: 1rem; }
.acordeon summary::marker { content: "+ "; }
.acordeon[open] summary::marker { content: "− "; }
.acordeon .acordeon__cuerpo {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .3s ease-out;
}
.acordeon[open] .acordeon__cuerpo { grid-template-rows: 1fr; }
.acordeon__cuerpo > * { overflow: hidden; }
/* :has() para estilizar el grupo cuando alguno está abierto: */
.lista:has(details[open]) .acordeon:not([open]) summary { opacity: .6; }
```
La animación usa el truco `grid-template-rows: 0fr → 1fr` (transicionable). `<details>` ya gestiona estado y teclado sin JS.
</details>

**E9 (U04/U11).** Diseña un sistema de capas (z-index) documentado para una app con: fondo decorativo, contenido, header sticky, dropdown, modal, toast y tooltip. Justifica cada decisión y muestra cómo aislarías un componente que contiene elementos positioned internos.

<details><summary>Solución</summary>

```css
:root {
  --z-fondo: 0;      /* decoraciones */
  --z-contenido: 1;
  --z-header: 100;
  --z-dropdown: 200;
  --z-modal: 300;    /* + backdrop 299 */
  --z-toast: 400;
  --z-tooltip: 500;
}
.header  { position: sticky; z-index: var(--z-header); }
.modal-root { isolation: isolate; z-index: var(--z-modal); }
/* Dentro de .modal-root los z-index locales (1, 2…) no contaminan la escala global */
```
`isolation: isolate` crea contexto propio: dentro del modal puedes usar `z-index: 1/2` sin tocar la escala global. Nunca uses 9999: si surge un conflicto, subes el token, no el número mágico.
</details>

**E10 (U11).** Implementa una barra de progreso de lectura con scroll-driven animations y fallback completo (sin soporte: nada; con soporte parcial: verificar). Muestra el `@supports`.

<details><summary>Solución</summary>

```css
.progreso {
  position: fixed; inset: 0 0 auto 0; height: 3px;
  background: var(--color-marca);
  transform: scaleX(0);
  transform-origin: 0 50%;
}
@supports (animation-timeline: scroll()) {
  .progreso {
    animation: crecer-progreso linear both;
    animation-timeline: scroll(root block);
  }
  @keyframes crecer-progreso { to { transform: scaleX(1); } }
}
@media (prefers-reduced-motion: reduce) {
  .progreso { display: none; }  /* es puramente decorativa */
}
```
Sin soporte, la barra queda invisible funcionalmente (`scaleX(0)`) o se oculta; nunca rompe el layout.
</details>

**E11 (U12).** Migra este CSS legacy a una arquitectura moderna (layers + tokens + nesting + lógicas):

```css
.container { max-width: 1100px; margin-left: auto; margin-right: auto; padding-left: 1rem; padding-right: 1rem; }
.btn { background: #2563eb; color: white; padding: 10px 20px; border-radius: 6px; border: 0; }
.btn:hover { background: #1d4ed8; }
.btn-red { background: #dc2626; }
.btn-red:hover { background: #b91c1c; }
```

<details><summary>Solución</summary>

```css
@layer tokens, components;

@layer tokens {
  :root {
    --color-brand: oklch(55% 0.2 260);
    --color-brand-hover: color-mix(in oklab, var(--color-brand) 85%, black);
    --color-danger: oklch(55% 0.2 25);
    --color-danger-hover: color-mix(in oklab, var(--color-danger) 85%, black);
    --space-2: .5rem; --space-3: .75rem; --space-4: 1rem;
    --radius-sm: .375rem;
    --contenedor-max: 68.75rem;
  }
}

@layer components {
  .contenedor {
    max-inline-size: var(--contenedor-max);
    margin-inline: auto;
    padding-inline: var(--space-4);
  }
  .boton {
    border: 0;
    padding: var(--space-2) var(--space-4);
    border-radius: var(--radius-sm);
    background: var(--color-brand);
    color: white;
    &:hover { background: var(--color-brand-hover); }
    &--peligro {
      background: var(--color-danger);
      &:hover { background: var(--color-danger-hover); }
    }
  }
}
```
Ganancias: tokens únicos, hover derivado con `color-mix`, propiedades lógicas (RTL-ready), BEM en modificador, capas que evitan guerras de especificidad.
</details>

**E12 (U13).** Audita este fragmento y lista TODOS los problemas de accesibilidad con su criterio WCAG:

```css
.link { color: #aaa; text-decoration: none; }
.link:focus { outline: none; }
.alerta-error { color: red; }
.modal { position: fixed; top: 0; left: 0; width: 100%; height: 100vh; background: white; }
.animacion { animation: parpadeo 1s infinite; }
@keyframes parpadeo { 50% { opacity: .3; } }
```

<details><summary>Solución</summary>

1. `.link` `#aaa` sobre blanco ≈ 2.3:1 → falla **1.4.3** (AA 4.5:1). Además quita subrayado: enlace distinguible solo por color → riesgo **1.4.1**; restaurar `text-decoration`.
2. `outline: none` sin alternativa → falla **2.4.7** (foco visible).
3. `.alerta-error` solo color → falla **1.4.1** (añadir icono/texto).
4. `.modal` con `height: 100vh` fijo → problemas en móvil (barra URL) y posible corte a zoom 200% (**1.4.4**); usar `100dvh` + `max-height` + scroll interno.
5. Animación infinita automática parpadeando (~1 Hz, pero opacidad oscilante continua) → incómoda; viola la espíritu de **2.3.3** y **2.2.2** si no es pausable; respetar `prefers-reduced-motion` y hacerla pausable/dismissible.
</details>

**E13 (U14).** Tu página tiene LCP de 4.8 s en móvil. El hero es una imagen de 2200 px servida siempre a todos los clientes, hay 3 hojas CSS (una de 380 KB) y la fuente del titular carga con `font-display: optional` tras 2 s. Propón un plan de mejora ordenado por impacto.

<details><summary>Solución</summary>

1. **Imagen LCP**: servir `srcset`/`sizes` (≈800–1000 px en móvil), AVIF/WebP, `fetchpriority="high"` y preload; dimensiones explícitas. (Mayor impacto directo en LCP.)
2. **CSS**: identificar la hoja de 380 KB → purgar (Coverage/PurgeCSS), minificar, extraer CSS crítico inline y defer el resto con preload+swap.
3. **Fuente**: cambiar a `font-display: swap` + preload de WOFF2 subconjunto latino; evitar `optional` para el titular (no pintaría con la fuente correcta casi nunca).
4. Verificar con Lighthouse mobile y re-medir LCP/CLS antes/después.
</details>

### Proyecto integrador (evaluación tipo examen práctico)

Construir una **landing responsive** (una página) que incluya:

1. Header sticky con nav (flex) que colapsa a menú en móvil.
2. Hero con imagen responsiva (`srcset`), título fluido (`clamp`) y CTA.
3. Sección de características en grid `auto-fit` (3→2→1 columnas).
4. Tarjetas con hover animado (`transform`/`opacity`) y estados de foco.
5. Paleta con tokens + modo oscuro con `light-dark()` o `prefers-color-scheme`.
6. Barra de progreso de lectura (scroll-driven con fallback).
7. Footer multicolumna que pasa a 1 columna.
8. Checklist: contraste AA verificado, `:focus-visible`, `prefers-reduced-motion`, sin desbordes a 320 px, Lighthouse ≥ 90 mobile.

Criterios de corrección sugeridos: estructura semántica (20%), calidad del CSS (capas/tokens/nomenclatura) (25%), responsive real (20%), accesibilidad verificada (20%), rendimiento (15%).

## PARTE B · GLOSARIO ES/EN

| Término | English | Definición breve |
|---|---|---|
| Cascada | Cascade | Proceso de resolución de conflictos entre declaraciones. |
| Especificidad | Specificity | Peso relativo de un selector. |
| Hoja de estilos | Stylesheet | Archivo/bloque de reglas CSS. |
| Modelo de caja | Box model | Estructura content/padding/border/margin. |
| Colapso de márgenes | Margin collapsing | Fusión de márgenes verticales adyacentes. |
| Contexto de formato de bloque | Block Formatting Context (BFC) | Ámbito de render independiente. |
| Contexto de apilamiento | Stacking context | Capa aislada para comparar `z-index`. |
| Bloque contenedor | Containing block | Referencia de posicionamiento absoluto/fijo. |
| Pista (grid) | Track | Fila o columna de una cuadrícula. |
| Línea (grid) | Grid line | Borde de una pista. |
| Área (grid) | Grid area | Rectángulo definido por 4 líneas. |
| Subcuadrícula | Subgrid | Herencia de pistas del grid padre. |
| Eje principal | Main axis | Dirección del flujo en flexbox. |
| Consulta de medios | Media query | Condición sobre características del dispositivo. |
| Consulta de contenedor | Container query | Condición sobre el tamaño/estilo del contenedor. |
| Propiedad personalizada | Custom property | Variable CSS (`--x`). |
| Capa (cascada) | Cascade layer | Grupo de reglas con prioridad declarada (`@layer`). |
| Anidación | Nesting | Reglas dentro de reglas (nativa o Sass). |
| Degradado | Gradient | Imagen generada por interpolación de colores. |
| Modo de mezcla | Blend mode | Algoritmo de combinación de capas de color. |
| Máscara | Mask | Recorte por alfa/luminancia. |
| Transición | Transition | Interpolación entre dos estados. |
| Fotogramas clave | Keyframes | Estados intermedios de una animación. |
| Función de temporización | Timing function | Curva de velocidad de la animación. |
| Promoción a capa | Layer promotion | Elevar elemento a compositor (`will-change`). |
| Renderizador bloqueante | Render-blocking | Recurso que retrasa la primera pintura. |
| Ruta crítica de render | Critical Rendering Path | Pipeline DOM+CSSOM→pantalla. |
| Desplazamiento acumulado | Cumulative Layout Shift (CLS) | Inestabilidad visual medida. |
| Tokens de diseño | Design tokens | Decisiones de diseño nombradas como datos. |
| Guía de estilo | Style guide | Documento de convenciones visuales y de código. |
| Mejora progresiva | Progressive enhancement | Base simple + mejoras según capacidades. |
| Reflow / Relayout | Reflow | Recálculo de geometría. |
| Repintado | Repaint | Redibujar píxeles sin recalcular layout. |
| Composición | Composite | Unión de capas en GPU. |
| Contraste | Contrast ratio | Relación de luminancias entre texto y fondo. |
| Foco visible | Visible focus | Indicador claro del elemento enfocado. |
| Movimiento reducido | Reduced motion | Preferencia del usuario para menos animación. |
| Colores forzados | Forced colors | Modo alto contraste del SO (Windows). |

## PARTE C · RECURSOS OFICIALES Y DE PROFUNDIZACIÓN

### Especificaciones (W3C / CSS WG)

- Índice de specs CSS: <https://www.w3.org/Style/CSS/>
- Selectors Level 4: <https://www.w3.org/TR/selectors-4/>
- Color Level 5: <https://www.w3.org/TR/css-color-5/>
- Grid Level 2 (subgrid): <https://www.w3.org/TR/css-grid-2/>
- Conditional Rules Level 5 (container queries): <https://drafts.csswg.org/css-conditional-5/>
- Nesting Level 1: <https://www.w3.org/TR/css-nesting-1/>
- View Transitions Level 1: <https://www.w3.org/TR/css-view-transitions-1/>
- Cascade Level 5/6: <https://www.w3.org/TR/css-cascade-5/> / <https://www.w3.org/TR/css-cascade-6/>
- Animations Level 2 (scroll-driven): <https://www.w3.org/TR/css-animations-2/>

### Documentación de referencia

- **MDN Web Docs (ES)**: <https://developer.mozilla.org/es/docs/Web/CSS> — la biblia diaria.
- **web.dev** (Google): rendimiento, Core Web Vitals, a11y: <https://web.dev>
- **Chrome Developers**: artículos profundos del equipo Chromium: <https://developer.chrome.com/docs>
- **caniuse.com**: compatibilidad por característica (verificar antes de usar features nuevas).
- **browser-compat-data** (MDN): datos de soporte en GitHub: <https://github.com/mdn/browser-compat-data>

### Accesibilidad

- WCAG 2.2 (W3C): <https://www.w3.org/TR/WCAG22/>
- Técnicas WCAG (cómo cumplir cada criterio): <https://www.w3.org/WAI/WCAG22/Techniques/>
- The A11Y Project: <https://www.a11yproject.com>
- axe DevTools (Deque): <https://www.deque.com/axe/devtools/>
- WebAIM: contrast checker y artículos: <https://webaim.org>

### Práctica y comunidad

- **Frontend Masters / CSS Battle**: retos de CSS puro (divertido y formador): <https://cssbattle.dev>
- **Smol CSS** (Jhey Tompkins): trucos cortos bien explicados: <https://smolcss.com>
- **Every Layout** (Heydon Pickering): conceptos de layout (Holy Grail, Sidebar…): <https://every-layout.dev>
- **A List Apart**: artículos largos de calidad: <https://alistapart.com>
- **Norm (Viget)**: patrones de diseño web: <https://www.viget.com/study/norm/>

### Normativa (Andalucía / España)

- Orden de 16 de junio de 2011 (BOJA 149/2011), currículo DAW Andalucía: <https://www.juntadeandalucia.es/boja/2011/149/23>
- RD 686/2010 (BOE), título DAW: <https://www.boe.es/eli/es/rd/2010/05/20/686>
- BOJA (consultar modificaciones posteriores): <https://www.juntadeandalucia.es/eboja.html>

### Herramientas citadas en los apuntes

| Herramienta | Uso |
|---|---|
| Jigsaw CSS Validator | Validación sintáctica W3C. |
| stylelint + Prettier | Lint y formato. |
| PurgeCSS | Eliminar CSS muerto. |
| Lightning CSS / cssnano | Transform y minificación. |
| Vite | Build moderno con HMR. |
| Lighthouse / DevTools | Métricas y diagnóstico. |
| axe / WAVE / Pa11y | Auditoría de accesibilidad. |
| Stark / WebAIM | Contraste y daltonismo. |
| Storybook / Chromatic | Componentes y visual regression. |
| Fluid typography calculators | Derivar `clamp()`. |
