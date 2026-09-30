---
title: "Unidad 08 — Unidades, tipografía y colores"
description: "Todas las unidades CSS con criterios de uso, sistema tipográfico completo (@font-face, fuentes variables, OpenType) y modelos de color modernos (oklch, color-mix, light-dark) con accesibilidad."
modulo: "LMH (0373) / DIW (0615)"
unidad: 8
fecha: "2026-09-06"
---

# Unidad 08 · Unidades, tipografía y colores

El RA 1 del módulo 0615 exige «analizar y seleccionar los **colores y tipografías** adecuados para su visualización en pantalla». Esta unidad da el bagaje técnico para hacerlo con criterio profesional.

## PARTE A · UNIDADES

### 1. Clasificación general

| Familia | Ejemplos | Uso típico |
|---|---|---|
| Absolutas (físicas) | `px`, `cm`, `mm`, `in`, `pt`, `pc`, `Q` | `px` es la referencia práctica de pantalla. |
| Relativas a tipografía | `em`, `rem`, `ex`, `ch` | Tipografía y espaciado rítmico. |
| Relativas al viewport | `vw`, `vh`, `vmin`, `vmax`, `svh/dvh/lvh` | Layouts a pantalla completa, hero. |
| De contenedor | `cqw`, `cqh`, `cqi`, `cqb`, `cqmin`, `cqmax` | Componentes responsivos (container queries, U10). |
| Porcentaje | `%` | Respecto a una propiedad del padre (ver matices). |
| Fracción | `fr` | Solo en grid. |
| Tiempo | `s`, `ms` | Transiciones/animaciones. |
| Ángulo | `deg`, `rad`, `grad`, `turn` | `rotate()`, degradados. |
| Resolución | `dpi`, `dpcm`, `dppx` | Media queries de resolución. |
| Frecuencia | `Hz`, `kHz` | (raro) |

Referencias fijas: `1in = 96px`, `1pt = 1/72in`, `1pc = 12pt`, `1cm ≈ 37.8px`. En pantalla solo `px` importa realmente.

### 2. `px` vs `rem` vs `em` (el debate eterno)

| Unidad | Referencia | Cuándo usarla |
|---|---|---|
| `px` | Pixel CSS (1/96 in) | Bordes finos (1–2 px), detalles donde no quieres escalar. |
| `rem` | `font-size` de `:root` | **Tipografía y espaciado global**: respeta la preferencia de tamaño de texto del usuario (accesibilidad). |
| `em` | `font-size` del propio elemento | Escalado relativo dentro de un componente (iconos `1em`, padding proporcional al tipo). |

Reglas prácticas:

- Define `html { font-size: 100% }` (16 px por defecto) y trabaja en `rem`.
- El usuario que sube el texto a 200% (WCAG 1.4.4) escala todo lo en `rem` → tu layout debe aguantarlo (pruébalo).
- Cuidado con `em` anidados: se multiplican (`1.2em` dentro de `1.2em` = 1.44×). Con `rem` no hay sorpresa.
- `ch` = ancho de la cifra «0» → medidas tipográficas perfectas (`width: 20ch` para un input numérico; `max-width: 68ch` para prosa).
- `ex` ≈ altura de la x (poco usado).

### 3. Viewport units y sus variantes dinámicas

| Unidad | Base |
|---|---|
| `vw` / `vh` | 1% del ancho/alto del viewport **inicial**. |
| `vmin` / `vmax` | El menor/mayor de los dos anteriores. |
| `svh` / `dvh` / `lvh` | **small / dynamic / large** viewport height: resuelven el problema de la barra de navegador móvil que aparece/desaparece. |

```css
.hero { min-height: 100dvh; }   /* llena la pantalla real en móvil */
/* svh: cuando la barra está visible (mínimo)
   lvh: cuando está oculta (máximo)
   dvh: dinámica (reacciona) ← la recomendada hoy */
```

> **Claves para el examen**: explicar el problema del `100vh` en móviles (sobra o falta según la URL bar) y la solución `dvh`.

### 4. Porcentajes: ¿respecto a qué?

Depende de la propiedad:

| Propiedad | Referencia del % |
|---|---|
| `width` / `height` | Contenedor padre (content box). |
| `margin-*` / `padding-*` | **Ancho** del contenedor padre (¡también los verticales!). |
| `top/left/right/bottom` (positioned) | Bloque contenedor. |
| `font-size` | `font-size` del padre. |
| `background-position` | Diferencia entre tamaño del fondo y del área. |
| `border-radius` | Radio horizontal respecto al ancho, vertical al alto. |

Trampa clásica: `padding-bottom: 100%` sobre un elemento de 300px de ancho crea 300px de padding (base = ancho, no alto). De ahí el truco antiguo de *aspect ratio* con padding (hoy sustituido por `aspect-ratio`).

### 5. Funciones de valor

```css
calc(100% - 2rem);            /* aritmética mixta */
min(100%, 60rem);             /* el menor */
max(100%, 400px);             /* el mayor */
clamp(1rem, 2.5vw, 2rem);     /* min, ideal, max → fluido */
round(nearest 8px, 100%);     /* redondeo a múltiplos (nuevo) */
```

`clamp(min, val, max)` es LA herramienta del diseño fluido: un solo valor que crece/decrece con límites (unidad 10).

## PARTE B · TIPOGRAFÍA

### 6. El stack tipográfico

```css
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
.titulo {
  font-family: "Fraunces", Georgia, "Times New Roman", serif;
}
.codigo {
  font-family: ui-monospace, "Cascadia Code", "JetBrains Mono", Consolas, monospace;
}
```

Buenas prácticas:

- **Máximo 2 familias** (display + texto) por proyecto; las variantes pesan.
- Siempre **fallback genérico** final (`sans-serif`, `serif`, `monospace`, `system-ui`, `ui-sans-serif`…).
- Nombres con espacios → comillas.
- `font-display` y carga: ver sección 8.

### 7. Propiedades de fuente completas

| Propiedad | Valores/notas |
|---|---|
| `font-family` | Lista con fallback. |
| `font-size` | Longitud; `smaller/larger` (evitar: opacos). |
| `font-weight` | 100–900 (variable fonts: cualquier valor del rango); keywords `normal`=400, `bold`=700. |
| `font-style` | `normal`, `italic`, `oblique [ángulo]`. |
| `font-stretch` | `50%`–`200%` o keywords (`condensed`, `expanded`) — solo si la fuente lo soporta. |
| `font-variant` | Atajo histórico; mejor las específicas: |
| `font-variant-caps` | `small-caps`, `all-small-caps`, `titling-caps`… |
| `font-variant-numeric` | `tabular-nums` (cifras alineadas: tablas, relojes), `oldstyle-nums`, `lining-nums`, `ordinal`, `slashed-zero`. |
| `font-variant-east-asian` | Para CJK. |
| `font-variation-settings` | Ejes de fuentes variables: `"wght" 650, "wdth" 110`. |
| `font-feature-settings` | Características OpenType: `"liga"`, `"tnum"`, `"smcp"`… (crudo; preferible `font-variant-*` cuando exista). |
| `font-kerning` | `normal` / `none`. |
| `font-optical-sizing` | `auto`: la fuente elige corte según tamaño (Display/Text). |
| `line-height` | **Adimensional preferido** (`1.5`): escala con el tipo. `px` solo en casos muy concretos. |
| `letter-spacing` | `em` pequeños (`0.02em`); negativo en display grandes (`-0.02em`). |
| `word-spacing` | Espaciado entre palabras. |
| `text-transform` | `uppercase`, `lowercase`, `capitalize`. |
| `text-indent` | Sangría primera línea (editorial). |
| `text-align` | `start/end` (lógicos) > `left/right` (i18n). |
| `text-align-last` | Alineación de la última línea (`justify` cuidado). |
| `text-justify` | `inter-word` / `inter-character`. |
| `hyphens` | `manual` / `auto` (requiere `lang` correcto). |
| `overflow-wrap` | `break-word` / `anywhere`: evita desbordes de palabras largas. |
| `word-break` | `normal` / `break-all` (CJK). |
| `white-space` | `normal`, `nowrap`, `pre`, `pre-wrap`, `pre-line`, `break-spaces`. |
| `text-shadow` | `x y blur color` (varias capas). |
| `text-decoration-*` | `line`, `color`, `style`, `thickness`, `skip-ink`, `underline-position`. |
| `text-wrap` | `balance` (titulares: líneas parejitas), `pretty` (evita viudas/orfanas). |
| `text-orientation` | Con `writing-mode` vertical. |
| `text-combine-upright` | Combinar caracteres (unidades: ㎡). |
| `font-size-adjust` | Compensa la x-height del fallback (nuevo, soporte parcial). |

### 8. `@font-face` y carga de fuentes

```css
@font-face {
  font-family: "MiFuente";
  src: url("/fonts/mifuente-latin.woff2") format("woff2"),
       url("/fonts/mifuente-latin.woff")  format("woff");
  font-weight: 100 900;        /* rango → fuente variable */
  font-style: normal;
  font-display: swap;          /* ver abajo */
  unicode-range: U+0000-00FF;  /* subconjunto latino */
}
```

| Aspecto | Recomendación |
|---|---|
| Formato | **WOFF2** siempre (mejor compresión); WOFF como fallback histórico. |
| `font-display` | `swap` (estándar web): muestra fallback y cambia al cargar. `block` (breve espera), `fallback`, `optional` (solo si ya está cacheada), `auto`. |
| Subsets | Divide por `unicode-range` (latino, latin-ext, griego…) para no descargar lo que no se usa. |
| Preload | `<link rel="preload" href="fuente.woff2" as="font" type="font/woff2" crossorigin>` para la fuente crítica. |
| Peso | Limita pesos (400/500/700) o usa variable (un archivo, todos los pesos). |
| Self-hosting vs CDN | Self-hosting: control de privacidad (RGPD), rendimiento y disponibilidad. |

### 9. Escala tipográfica modular

Sistema clásico: ratio fijo (1.2–1.333) sobre una base:

```css
:root {
  --fs-base: 1rem;              /* 16px */
  --ratio: 1.25;                /* quinta justa */
  --fs-sm:   calc(var(--fs-base) / var(--ratio));
  --fs-md:   var(--fs-base);
  --fs-lg:   calc(var(--fs-base) * var(--ratio));
  --fs-xl:   calc(var(--fs-base) * var(--ratio) * var(--ratio));
  --fs-2xl:  calc(var(--fs-base) * pow(var(--ratio), 3));  /* pow(): nuevo */
}
h1 { font-size: var(--fs-2xl); line-height: 1.15; letter-spacing: -0.02em; }
h2 { font-size: var(--fs-xl);  line-height: 1.2; }
h3 { font-size: var(--fs-lg);  line-height: 1.3; }
p  { font-size: var(--fs-md);  line-height: 1.6; max-width: 68ch; }
```

Versión **fluida** con `clamp()` (se combina en unidad 10):

```css
h1 { font-size: clamp(2rem, 1.5rem + 2vw, 3.5rem); }
```

Métricas de legibilidad (reglas de pulgar):

- Prosa: 16–20 px, `line-height` 1.5–1.7, medida 45–75 caracteres (`68ch` óptimo).
- Títulos: `line-height` 1.05–1.25, tracking ligeramente negativo.
- Contraste mínimo AA: 4.5:1 (texto normal), 3:1 (grande ≥ 24 px o 18.66 px bold) → WCAG 1.4.3.

## PARTE C · COLORES

### 10. Formatos de color

| Formato | Ejemplo | Notas |
|---|---|---|
| Nombres | `crimson`, `rebeccapurple` | 148 nombres estándar; legibles pero limitados. |
| Hex | `#fff`, `#fffb`, `#ff0000`, `#ff000080` | 3/4/6/8 dígitos (el 4.º par = alpha). |
| `rgb()` moderno | `rgb(255 0 0 / .5)` | Espacios + `/alpha`; legacy `rgba(255,0,0,.5)` sigue válido. |
| `hsl()` moderno | `hsl(0 100% 50% / .5)` | Matiz, saturación, luz. Alpha con `/`. |
| `hwb()` | `hwb(0 100% 0%)` | Hue, white, black (intuitivo para mezclas). |
| `lab()` / `lch()` | `lch(53% 85 35)` | Perceptual CIE LCh: luz, croma, ángulo. |
| `oklab()` / `oklch()` | `oklch(70% 0.15 250)` | **Perceptualmente uniforme mejorado** (Okabe-Ito). El futuro paletas. |
| `color()` | `color(display-p3 1 0 0)` | Espacios amplios (P3, srgb…). |
| `currentColor` | — | Hereda el `color` actual (iconos SVG, bordes). |
| `transparent` | — | Negro con alpha 0 (cuidado en gradientes: crea banda gris → usa `rgb(0 0 0 / 0)` del color real). |
| System colors | `Canvas`, `Link`, `GrayText`… | Se adaptan al tema del SO (soporte irregular). |

### 11. `color-mix()` — mezclas calculadas

```css
:root { --marca: oklch(65% 0.2 250); }
.fondo-suave { background: color-mix(in oklab, var(--marca) 10%, white); }
.borde-medio { border-color: color-mix(in srgb, currentColor 30%, transparent); }
.hover      { background: color-mix(in oklab, var(--marca) 85%, black); }
```

- El espacio de mezcla (`in oklab/srgb/lab…`) afecta al resultado: **oklab** da mezclas perceptuales suaves.
- Casos de uso: generar hover/active/focus desde un único token, fondos derivados, estados de formulario. Elimina el «drenaje» de mantener 5 tonos a mano.

### 12. `light-dark()` — modo oscuro sin duplicar reglas

```css
:root {
  --bg: light-dark(#ffffff, #121212);
  --texto: light-dark(#1a1a1a, #eaeaea);
}
@media (prefers-color-scheme: dark) { /* opcional: forzar por clase */ }
:root[data-theme="dark"] { color-scheme: dark; }
```

- `color-scheme: light dark` avisa al navegador de que la página maneja ambos temas (formularios nativos, scrollbars se adaptan solos).
- Soporte: Chrome 123+, Firefox 130+, Safari 17.5+.

### 13. Construir una paleta accesible (flujo de trabajo)

1. Define **1–2 colores de marca** en `oklch` (controlas luz/croma/tono por separado).
2. Deriva escalas con `color-mix()` (50…950) o herramientas (Tailwind palette, OKLCH ramps).
3. Verifica **contraste** de cada par texto/fondo contra WCAG:
   - AA: 4.5:1 normal, 3:1 grande; AAA: 7:1 / 4.5:1.
   - No-texto (bordes, iconos funcionales, gráficos): 3:1 (WCAG 1.4.11).
4. Prueba con **daltonismo** (simuladores: Stark, Polotno, browser extensions) y nunca uses color como única información (WCAG 1.4.1): añade icono/texto/patrón.
5. Documenta la paleta como **tokens** (unidad 12).

### 14. Errores comunes de color

| Error | Consecuencia | Solución |
|---|---|---|
| `transparent` en gradientes | Banda oscura intermedia | `rgb(color / 0)` del mismo tono. |
| Hex de 3/4 dígitos mal escrito | Color inesperado | Preferir formato largo o `rgb()`. |
| Negros puros `#000`/blancos puros `#fff` | Fatiga visual, halos | Grises suaves (`#111`, `#fafafa`). |
| Paleta solo por matiz HSL | Tonos «sucios» al variar luz | Trabajar en `oklch` (croma constante). |
| Estilizar `::selection` sin contraste | Selección ilegible | Comprobar contraste también allí. |

## 15. Autoevaluación rápida

1. ¿Por qué `rem` es mejor que `em` para espaciado global? ¿Y cuándo sí conviene `em`?
2. Explica `svh/dvh/lvh` con el caso de la URL bar en iOS.
3. ¿A qué se refiere `padding-top: 50%` en un div de 400px de ancho?
4. Escribe `@font-face` con fuente variable, preload y `font-display: swap`. Justifica cada decisión.
5. Genera tres derivados (hover, fondo suave, borde) de `--marca: oklch(60% 0.2 260)` usando `color-mix()`.
6. ¿Qué es `font-variant-numeric: tabular-nums` y dónde lo aplicarías?
