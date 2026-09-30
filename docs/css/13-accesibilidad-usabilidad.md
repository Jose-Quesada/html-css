---
icon: lucide/accessibility
title: "Unidad 13 — Accesibilidad y usabilidad"
description: "WCAG aplicada a CSS: contraste, foco, movimiento reducido, forced-colors, técnicas de ocultación accesible, reflow y espaciado; principios de usabilidad y herramientas de verificación."
modulo: "DIW (0615) — RA 5 y RA 6"
unidad: 13
fecha: "2026-09-06"
---

# Unidad 13 · Accesibilidad y usabilidad

El módulo 0615 dedica dos resultados de aprendizaje enteros a esto (RA 5 «interfaces accesibles» y RA 6 «interfaces amigables»). No es un extra: es **requisito de titulación** y, además, obligación legal en muchos contextos (Directiva europea de accesibilidad, Ley General de Derechos de las Personas con Discapacidad, contratos públicos).

!!! note "Conocimientos previos"

    - HTML semántico y `label` (unidades 02 y 06 de HTML).
    - Cascada y pseudo-clases (unidades 01–02 de CSS).
    - Tokens y guía de estilo (unidad 12).

## 1. Marco: WCAG

Los cuatro principios se recuerdan por sus siglas: ==POUR==.

**WCAG (Web Content Accessibility Guidelines)**, W3C, versiones 2.0/2.1/2.2. Se organiza en:

- **4 principios (POUR)**:
  1. **P**erceptible (Perceivable)
  2. **O**perable (Operable)
  3. **C**omprensible (Understandable)
  4. **R**obusto (Robust)
- **Nivel de conformidad**: A (mínimo) → AA (objetivo habitual profesional y contractual) → AAA (máximo, no siempre viable).
- Cada **criterio de éxito** tiene número (p. ej., 1.4.3) y nivel.

Los criterios que **CSS implementa directamente** son los que trabajamos aquí; el más preguntado es ==1.4.3 (contraste)==.

!!! info "Qué significa certificar AA"

    - **A** = mínimo viable; **AA** es el nivel que piden contratos y prácticas.
    - **AAA** no se exige en todo el sitio: se aplica a apartados concretos.
    - Cada criterio es **verificable** y numerado: el de contraste es el **1.4.3**.

!!! quote "Por qué importa"

    «The power of the Web is in its universality. Access by everyone regardless of disability is an essential aspect.»

    — Tim Berners-Lee (W3C), citado por la WAI: <https://www.w3.org/WAI/>

## 2. Criterios WCAG aplicados a CSS

### 2.1. 1.4.3 Contraste de texto (AA): 4.5:1

- Texto normal: mínimo **4.5 : 1**.
- Texto grande (≥ 24 px, o ≥ 18.66 px en negrita): mínimo **3 : 1**.
- AAA: 7:1 / 4.5:1.

Cómo calcularse: relación entre luminancias relativas `(L1 + 0.05) / (L2 + 0.05)`. En la práctica: herramientas (Stark, Contrast, WebAIM Contrast Checker, DevTools panel Accessibility muestra el ratio).

```css title="contraste.css" hl_lines="4"
/* Bien */
:root { --texto: #1f2937; --fondo: #ffffff; }        /* 14.7:1 */
/* Mal */
.aviso { color: #9ca3af; background: #f3f4f6; }      /* ~1.9:1 → falla AA */
```

Reglas prácticas:

- El contraste se calcula sobre el **fondo efectivo** (si hay imagen detrás, usa el peor caso o una capa opaca).
- `opacity` sobre texto reduce el contraste real: médelo, no lo supongas.
- Textos decorativos gigantes (logotipos tipográficos) están exentos, pero el contenido no.
- En modo oscuro aplica igual (no asumas que «oscuro = más contraste»).

!!! danger "Contraste AA incumplido"

    El par `#9ca3af` sobre `#f3f4f6` rinde **≈1.9:1**: lejos de los **4.5:1** del 1.4.3. Si ese gris es texto real, la página **no puede declararse AA**.

### 2.2. 1.4.11 Contraste no textual (AA): 3:1

Para **componentes de UI** y gráficos necesarios para entender el contenido:

- Bordes de inputs, botones, iconos funcionales, indicadores de estado, thumbs de carrusel.
- Solución típica: bordes de 2px con color suficiente, o `outline`, o sombra que sume contraste.

```css title="ui.css"
input { border: 2px solid #6b7280; }   /* sobre blanco: 4.8:1 ✓ */
```

### 2.3. 1.4.1 Uso del color (A)

El color **no puede ser la única información**:

```html title="error.html"
<!-- Mal: solo el rojo indica error -->
<span style="color:red">Error</span>   <!-- (1)! -->
<!-- Bien -->
<span class="error"><svg aria-hidden="true">✕</svg> Error: falta el email</span>
```

1.  Un color **solo** no comunica la causa: añade texto, icono o patrón.

CSS: añade icono, texto, subrayado (`text-decoration`) o patrón. Prueba siempre con simulador de daltonismo (deuteranopía es la más frecuente).

### 2.4. 2.4.7 Foco visible (AA) y 2.4.11 Foco no oculto (AAA)

- Nunca ==`outline: none`== sin alternativa equivalente o mejor.
- `:focus-visible` estilizado con contraste ≥ 3:1 contra el fondo adyacente:

```css title="foco.css"
:focus-visible {
  outline: 3px solid var(--color-enfoque);   /* (1)! */
  outline-offset: 2px;
}
/* Si el elemento ya tiene borde fuerte, la outline basta con 2px */
```

1.  El indicador debe verse **contra cualquier fondo**: por eso el color sale de un token.

- 2.4.11: el elemento enfocado no debe quedar tapado por headers fijos u overlays (usa `scroll-margin-top`):

```css title="scroll.css" hl_lines="1"
section[id] { scroll-margin-top: 5rem; }  /* respeta header sticky al hacer foco/ancla */
```

!!! warning "Error común"

    - Borrar el foco con `outline: none` y «luego lo decoro»: sin indicador **no hay 2.4.7**.
    - Poner `outline-offset` negativo o `overflow: hidden` padre: el anillo queda **tapado**.
    - Confundir `opacity: 0` con «oculto»: sigue **focalizable**.

### 2.5. 1.4.4 Redimensionar texto (AA): 200%

El texto debe escalarse a 200% **sin pérdida de contenido ni funcionalidad**:

- Trabaja en `rem` (unidad 08).
- Evita alturas fijas que recorten texto (`height` + `overflow: hidden` en párrafos).
- Prueba con zoom del navegador al 200%: ¿algo se corta? ¿Se solapa? ¿El menú sigue usable?
- Alternativa admitida: ofrecer zoom propio equivalente.

### 2.6. 1.4.10 Reflow (AA): 320 csspx

A 320px de ancho (≈ móvil pequeño con zoom 400%) no debe haber scroll en **dos dimensiones**:

- Layouts de una columna a ese ancho (tu breakpoint más bajo suele cubrirlo).
- Tablas anchas: permiten scroll horizontal **interno** (el wrapper), no la página.
- Elementos con `white-space: nowrap` largos: revisarlos.

### 2.7. 1.4.12 Espaciado del texto (AA)

Al modificar `line-height` (mín. 1.5×), `paragraph spacing` (mín. 2× font-size), `letter-spacing` (mín. 0.12em) y `word-spacing` (0.16em), **no debe perderse contenido**:

- Implica evitar cajas con altura fija y `overflow: hidden` en bloques de texto.
- Los usuarios pueden forzar estos valores desde su perfil: tu CSS no debe romperlo.

### 2.8. 1.4.13 Contenido en hover o foco (AA)

La información mostrada al hover/foco debe:

- **Dismissible**: cerrable con `Escape` (o dejar de hoverear).
- **Hoverable**: posible mantenerla con el puntero (no desaparecer al moverse hacia ella).
- **Persistent**: fijable con otra interacción (click) si es crítica.

Aplica a tooltips, menús desplegables y popovers: diseña zonas «muertas» generosas y transiciones de salida cortas.

### 2.9. 2.3.3 Animaciones a partir de interacciones (AA)

Las animaciones disparadas por interacción deben poder **desactivarse** si duran > 4 s cada una, son paralelas, o son automátas… y en la práctica: respetar ==`prefers-reduced-motion`== (ver [unidad 11](11-transiciones-animaciones.md), sección 7). Además, nada que parpadee entre 2 y 3 Hz (2.3.1, nivel A).

### 2.10. 2.4.4 Propósito de enlaces (A) — lado CSS/HTML

El texto del enlace debe tener propósito («Ver precios», no «clic aquí»). CSS ayuda: estilizar enlaces distinguibles sin depender solo del color (subrayado por defecto es buena idea).

## 3. Ocultar contenido: las cuatro formas y sus efectos

| Técnica | Render | Árbol de accesibilidad | Cuándo |
|---|---|---|---|
| `display: none` | No se pinta | **No existe** | Ocultar de verdad (menú cerrado, tab inactivo). |
| `visibility: hidden` | Reserva espacio | No existe (pero el espacio sí) | Raro; mantiene layout. |
| `opacity: 0` | Invisible pero ocupa | **Sigue presente** (focalizable ¡problema!) | Solo junto a `pointer-events: none` y cuidado con foco. |
| Clase ==visually-hidden== (clip) | No visible | **Presente y legible** | Texto solo para lectores de pantalla («Saltar al contenido», contexto de iconos). |

```css title="ocultar.css" hl_lines="6 7"
.visually-hidden {
  position: absolute !important;
  width: 1px; height: 1px;
  padding: 0; margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  white-space: nowrap;
}
```

!!! example "Texto solo para lectores de pantalla"

    ```html title="index.html"
    <a class="visually-hidden" href="#contenido">Saltar al contenido</a>
    <header>…</header>
    ```

    El enlace **existe para el lector** y desaparece al recibir foco con esta clase: sin él, la navegación por teclado se atasca en el menú.

> **Claves para el examen**: tabla comparativa de las cuatro formas. Pregunta clásica: «¿un botón con `opacity: 0` es accesible?» → No: sigue siendo focalizable y confunde.

!!! question "¿Es accesible un botón con `opacity: 0`?"

    Un botón invisible responde al Tab y activa su acción. ¿Qué falla y cómo lo arreglas?

    ??? success "Respuesta"

        Sigue en el **árbol de accesibilidad** y es **focalizable**: el usuario activa algo que no ve. Lo correcto es ocultarlo de verdad (`display: none` o `visibility: hidden`) o marcarlo `inert`; `opacity: 0` solo con `pointer-events: none` y **sin foco**.

## 4. Modos especiales del sistema operativo

### 4.1. `forced-colors` (Windows High Contrast)

```css title="forced-colors.css"
@media (forced-colors: active) {
  /* El SO pinta colores forzosos; asegura que los bordes sigan visibles */
  .boton { border: 1px solid ButtonText; }
  .icono { forced-color-adjust: none; }  /* solo si el icono ES la información */
}
```

Principio: no rompas el modo; aporta estructura (bordes) donde antes aportaba color.

### 4.2. `prefers-contrast: more`

Refuerza bordes y evita degradados sutiles como única señal.

### 4.3. Zoom y lectores de pantalla

- `display: contents` en contedores semánticos puede borrar el nombre del grupo para algunos lectores (ver unidad 07).
- Orden visual ≠ orden DOM (con `order` o grid placement) → los lectores leen el DOM: mantén coherencia.
- `aria-hidden="true"` en decoración duplicada (incluido `::before/::after` con texto relevante: mejor no poner texto en content si es ornamental).

!!! info "Ajustes del sistema que debes respetar"

    - ==forced-colors==, `prefers-contrast`, `prefers-reduced-motion` y `prefers-color-scheme`.
    - Se emulan en DevTools › Rendering, pero **pruébalos en el ajuste real del SO**.
    - El modo oscuro **del usuario** manda sobre tu CSS.

## 5. Usabilidad (RA 6)

La usabilidad estudia la **eficacia, eficiencia y satisfacción** del usuario. Referentes: ISO 9241-11 y las ==10 heurísticas de Nielsen==[^1] (las más citadas en web):

1. **Visibilidad del estado**: el sistema informa qué pasa (loading, éxito, error) → skeletons, toasts, estados de botón.
2. **Lenguaje del usuario**: etiquetas claras, sin jerga interna.
3. **Control y libertad**: salir de estados (cerrar modal con Escape/X, deshacer).
4. **Consistencia y estándares**: mismo componente = mismo comportamiento (guía de estilo).
5. **Prevención de errores**: confirmaciones en acciones destructivas, validación inline.
6. **Reconocer en vez de recordar**: contexto visible (labels siempre, no solo placeholder).
7. **Flexibilidad y eficiencia**: atajos para expertos, flujos cortos para novatos.
8. **Diseño minimalista**: menos ruido = menos carga cognitiva.
9. **Ayudar a recuperar errores**: mensajes que dicen qué pasó, dónde y cómo arreglarlo.
10. **Ayuda y documentación**: discoverable cuando se necesita.

### 5.1. Aplicado a CSS

| Heurística | Acción CSS |
|---|---|
| Visibilidad de estado | Estilos claros para `:disabled`, `.cargando`, `.error`; skeletons. |
| Consistencia | Tokens + componentes ([unidad 12](12-css-moderno-arquitectura.md)). |
| Prevención de errores | Validación visual con `:user-invalid`, mensajes asociados. |
| Control | Targets táctiles ≥ 44×44 px (WCAG 2.5.8 target size AA recomienda 24px mínimo; 44 es estándar móvil). |
| Legibilidad | Medida de línea 45–75 caracteres, jerarquía tipográfica clara. |
| Navegación predecible | Menús estables, breadcrumbs, «volver» evidente. |

### 5.2. Navegación: recordada vs redescubierta

- **Recordada**: el usuario sabe dónde está cada cosa (consistencia de posición).
- **Redescubierta**: puede encontrarlo explorando (búsqueda, sitemap, IA).
Objetivo: que lo principal sea *recordado* (misma posición siempre) y lo secundario *redescubrible*.

## 6. Verificación: herramientas y proceso

### 6.1. Checklist manual (siempre)

!!! success "Checklist manual antes de entregar"

    - [ ] Tab por toda la página: ¿foco visible y orden lógico?
    - [ ] Zoom 200%: ¿se pierde contenido?
    - [ ] 320px: ¿scroll horizontal doble?
    - [ ] Solo teclado: ¿se completa la tarea principal?
    - [ ] Modo oscuro del SO: ¿contrastes correctos?
    - [ ] Reduced motion activado: ¿animaciones desactivadas?
    - [ ] Simulador de daltonismo: ¿el color no es la única señal?
    - [ ] Lectura con lector de pantalla (NVDA/VoiceOver) de una tarea clave.

### 6.2. Herramientas automatizadas

| Herramienta | Tipo | Notas |
|---|---|---|
| **axe DevTools** (Deque) | Extensión + librería | La más completa; integra en CI (axe-core). |
| **Lighthouse** (Chrome) | Auditoría | Incluye accesibilidad + rendimiento + SEO. |
| **WAVE** | Extensión | Visualiza errores superpuestos al DOM. |
| **Pa11y** | CLI | Para pipelines (basado en HTML_CodeSniffer). |
| **Stark / Contrast** | Color | Ratios de contraste y simulación de daltonismo. |
| **WebAIM Contrast Checker** | Web | Ratio rápido de dos colores. |
| Validador W3C (Jigsaw) | CSS/HTML | Sintaxis (no accesibilidad). |

Limitación fundamental: **lo automático detecta ~30–40% de los problemas**. La revisión manual y con usuarios es insustituible (CE f del RA 5: «verificados mediante test externos»).

### 6.3. Multi-navegador (CE g del RA 5 y RA 6)

- Chrome/Edge (Blink), Firefox (Gecko), Safari (WebKit): prueba los tres mínimos.
- Móvil real Android + iOS.
- Con y sin JavaScript (tus estilos base deben sostener la página).
- Servicios: BrowserStack / Sauce Labs para matrices grandes.

## 7. Errores comunes de accesibilidad en CSS

| Error | Impacto | Corrección |
|---|---|---|
| `outline: none` global | Foco invisible (falla 2.4.7) | `:focus-visible` con contraste. |
| Grises claros sobre blanco | Falta 1.4.3 | Medir y ajustar (tokens con ratios verificados). |
| Placeholder como único label | Desaparece al escribir; no siempre leído | `<label>` visible siempre. |
| `position: fixed` que tapa el foco | Falla 2.4.11 | `scroll-margin` / offsets. |
| Animación automática infinita | Mareo; falla 2.3.x | `prefers-reduced-motion` + parar fuera de viewport. |
| Icono sin texto ni `alt`/`aria-label` | Sin nombre para AT | Texto oculto accesible o `aria-label`. |
| Menú que desaparece al mover el ratón hacia él | Falla 1.4.13 | Zona muerta + delay de cierre. |

## 8. Autoevaluación rápida

1. Calcula (o explica cómo) el contraste de `#777777` sobre `#ffffff` y di si pasa AA para texto normal.
2. Un tooltip aparece al hover de un icono. Enumera los requisitos de 1.4.13 y cómo los cumples.
3. Diferencia entre `display:none`, `visibility:hidden`, `opacity:0` y `.visually-hidden` con un caso de uso de cada uno.
4. Tu header sticky tapa el primer campo al hacer Tab. ¿Qué CSS aplicas?
5. Lista tres heurísticas de Nielsen y su traducción a una decisión CSS concreta.
6. ¿Por qué las herramientas automáticas no bastan para declarar «web accesible»?

!!! tip "Claves para el examen"

    - **POUR** = Perceptible, Operable, Comprensible, Robusto; nivel objetivo **AA**.
    - Contraste de texto **4.5:1** (texto grande 3:1); UI y gráficos **3:1**.
    - El color **nunca** es la única señal (1.4.1).
    - ==`outline: none`== solo con sustituto: usa ==`outline`== en **`:focus-visible`**.
    - `display:none`/`visibility:hidden` = fuera del árbol; `opacity:0` **sigue focalizable**.
    - `.visually-hidden` = visible para el lector, invisible en pantalla.
    - Las automáticas cubren ~**30–40 %**: revisión manual y usuarios son obligatorios.

[^1]: Jakob Nielsen, «10 Usability Heuristics for User Interface Design» (1994).

*[WCAG]: Web Content Accessibility Guidelines
*[W3C]: World Wide Web Consortium
*[RA]: Resultado de aprendizaje
