---
title: "Apuntes de HTML y CSS — DAW/DAM"
description: "Material de estudio de HTML5 y CSS como apoyo a los módulos LMH (0373), DIW (0615) y DI (0488) de los ciclos de Desarrollo de Aplicaciones Web y de Aplicaciones Multiplataforma en Andalucía."
modulo: "LMH (0373) / DIW (0615) / DI (0488)"
ciclo: "DAW — Técnico Superior en Desarrollo de Aplicaciones Web · DAM — Técnico Superior en Desarrollo de Aplicaciones Multiplataforma"
nivel: "medio-avanzado"
fecha: "2026-09-29"
idioma: "es"
licencia: "CC BY-SA 4.0"
---

# Apuntes de HTML y CSS · DAW/DAM (Andalucía)

Material de estudio de **HTML5** y **CSS**, elaborado como **apoyo a las clases** de los módulos de interfaces del ciclo de **DAW** y de **DAM** en Andalucía. Primero se cubre todo lo referente a **HTML** (sección HTML5, con ejemplos prácticos y ejercicios) y después el material de **CSS** completo.

| Módulo | Código | Horas | Relación con estos apuntes |
|---|---|---|---|
| Lenguajes de marcas y sistemas de gestión de información | **0373** (LMH) | 128 h | HTML5 completo (RA 3: *creación de documentos*); CSS: *ventajas y aplicación de hojas de estilo*. |
| Diseño de interfaces web | **0615** (DIW) | 80 h | RA 1 (planificación de interfaz), RA 2 (estilos), RA 5 (accesibilidad/WCAG) y RA 6 (usabilidad). |
| Desarrollo de interfaces | **0488** (DI) | 140 h | Repaso de HTML5/CSS como base previa al desarrollo con frameworks. |

> **Normativa de referencia** (detallada en [docs/css/00-normativa-y-marco-curricular.md](docs/css/00-normativa-y-marco-curricular.md)):
> - Real Decreto 686/2010, de 20 de mayo (BOE): título y enseñanzas mínimas.
> - Orden de 16 de junio de 2011 (BOJA n.º 149, de 1 de agosto de 2011): desarrollo del currículo en Andalucía.
> - W3C: especificaciones HTML5 y CSS, WCAG 2.1/2.2 (accesibilidad).

## Estructura del repositorio

- `docs/html/` — **10 capítulos de HTML5** (teoría, ejemplos y ejercicios con solución).
- `docs/css/` — **16 unidades de CSS** (de la 00 a la 15, con ejercicios y glosario).
- `docs/index.md` — portada del sitio.
- `anteriores/` — material original conservado íntegro (`html/` originales HTML, `css-antiguo/` versiones previas de CSS, `raiz/` copias y plantillas). **No se ha borrado nada**: se ha reorganizado.
- `zensical.toml` — configuración del sitio (navegación por secciones HTML5/CSS).

## Cómo usar este material

1. **Orden**: HTML primero (capítulos 01→10) y después CSS (00→15); cada unidad es autocontenida pero asume la anterior.
2. **Práctica obligatoria**: todos los capítulos incluyen ejemplos comentados. La sección HTML termina con [10 ejercicios](docs/html/09-ejercicios.md) por niveles con criterios de evaluación y [sus soluciones](docs/html/10-ejercicios-soluciones.md); CSS agrega los suyos en la unidad [15](docs/css/15-ejercicios-glosario-recursos.md).
3. **Para el examen**: busca los recuadros **«Claves para el examen»** (final de cada capítulo) y **«Error común»** (incrustados); recogen los conceptos que más se evalúan.
4. **Validación**: comprueba tu código en <https://validator.w3.org> y la accesibilidad con el árbol de accesibilidad de las DevTools.

## Índice — HTML5 (docs/html)

| # | Archivo | Contenido |
|---|---|---|
| 01 | [Introducción a HTML5](docs/html/01-introduccion-html5.md) | HTML frente a CSS/JS, historia y HTML5, boilerplate comentado, elementos y atributos, entidades, validación W3C |
| 02 | [Texto y semántica](docs/html/02-texto-y-semantica.md) | Jerarquía de encabezados, listas, elementos en línea semánticos (`strong`, `mark`, `time`…), `figure`, artículo de ejemplo |
| 03 | [Enlaces y recursos](docs/html/03-enlaces-y-recursos.md) | Rutas relativas, tipos de destino, accesibilidad de enlaces, `img` con `alt`, `srcset`/`picture`, `iframe` |
| 04 | [Multimedia](docs/html/04-multimedia.md) | `video`/`audio`, formatos y compatibilidad, `track` con WebVTT, WCAG 1.2.x, incrustación externa |
| 05 | [Tablas de datos](docs/html/05-tablas.md) | `caption`, `th` con `scope`, `colspan`/`rowspan`, accesibilidad, tablas responsivas |
| 06 | [Formularios HTML5](docs/html/06-formularios-html5.md) | Tabla de tipos de `input`, atributos de validación, `label`/`fieldset`, validación nativa y Constraint API, ejemplo de matrícula |
| 07 | [Estructura semántica y ARIA](docs/html/07-estructura-semantica-y-aria.md) | Landmarks (`main`, `nav`…), skip link, regla de oro de ARIA, `aria-label`, `aria-live`, DevTools |
| 08 | [APIs y funcionalidades nativas](docs/html/08-apis-html5.md) | `data-*`, `localStorage`, Constraint API, geolocalización, drag & drop, canvas, Fetch |
| 09 | [Ejercicios](docs/html/09-ejercicios.md) | 10 retos por niveles con enunciado, código inicial, tarea y rúbrica de evaluación |
| 10 | [Ejercicios: soluciones](docs/html/10-ejercicios-soluciones.md) | Código completo comentado, puntos clave y errores frecuentes de cada ejercicio |

## Índice — CSS (docs/css)

| # | Archivo | Contenido | Módulos |
|---|---|---|---|
| 00 | [Normativa y marco curricular](docs/css/00-normativa-y-marco-curricular.md) | Marco legal estatal y andaluz, resultados de aprendizaje aplicables, papel del W3C | LMH + DIW |
| 01 | [Fundamentos de CSS](docs/css/01-fundamentos-de-css.md) | Historia, sintaxis, formas de inclusión, cascada, especificidad, herencia, `!important` | LMH + DIW |
| 02 | [Selectores](docs/css/02-selectores.md) | Todos los tipos de selectores, combinadores, pseudo-clases y pseudo-elementos, cálculo de especificidad | LMH + DIW |
| 03 | [Modelo de caja](docs/css/03-modelo-de-caja.md) | Box model, `box-sizing`, dimensiones, colapso de márgenes, `overflow`, tamaño intrínseco | LMH + DIW |
| 04 | [Posicionamiento y z-index](docs/css/04-posicionamiento-y-z-index.md) | `position`, bloques contenedores, contexto de apilamiento, `sticky`, patrones prácticos | LMH + DIW |
| 05 | [Flexbox](docs/css/05-flexbox.md) | Modelo de flexión completo: contenedor, elementos, problemas clásicos y layouts | LMH + DIW |
| 06 | [Grid](docs/css/06-grid.md) | Cuadrícula 2D: pistas, líneas, áreas, `fr`, `minmax()`, `auto-fit/auto-fill`, subgrid | LMH + DIW |
| 07 | [Flujo, multicolumna, tablas y display](docs/css/07-flujo-multicolumna-tablas-display.md) | Valores de `display`, BFC, `float` (herencia técnica), columnas, layout de tabla | LMH + DIW |
| 08 | [Unidades, tipografía y colores](docs/css/08-unidades-tipografia-colores.md) | Todas las unidades, sistema tipográfico completo, modelos de color modernos, `color-mix()`, `light-dark()` | LMH + DIW |
| 09 | [Fondos, imágenes y decoración](docs/css/09-fondos-imagenes-decoracion.md) | `background`, degradados, formatos de imagen, bordes, sombras, filtros, blend modes, máscaras, `clip-path` | LMH + DIW |
| 10 | [Diseño responsivo](docs/css/10-diseno-responsivo.md) | Mobile-first, media queries, `clamp()`, unidades fluidas, container queries | LMH + DIW |
| 11 | [Transiciones y animaciones](docs/css/11-transiciones-animaciones.md) | Transiciones, `@keyframes`, `transform`, scroll-driven animations, view transitions, `prefers-reduced-motion` | LMH + DIW |
| 12 | [CSS moderno y arquitectura](docs/css/12-css-moderno-arquitectura.md) | Custom properties, `@property`, nesting nativo, `@layer`, `@supports`, `@scope`, propiedades lógicas, BEM/ITCSS, preprocesadores, PostCSS | LMH + DIW |
| 13 | [Accesibilidad y usabilidad](docs/css/13-accesibilidad-usabilidad.md) | WCAG aplicada a CSS, contraste, foco, movimiento reducido, `forced-colors`, usabilidad, herramientas de verificación | DIW (RA 5 y 6) |
| 14 | [Rendimiento y buenas prácticas](docs/css/14-rendimiento-buenas-practicas.md) | Critical rendering path, render-blocking, containment, `will-change`, Core Web Vitals, DevTools, calidad de código | LMH + DIW |
| 15 | [Ejercicios, glosario y recursos](docs/css/15-ejercicios-glosario-recursos.md) | Ejercicios por niveles con soluciones, glosario ES/EN, fuentes oficiales | LMH + DIW |

## Convenciones del material

- **Sintaxis**: los ejemplos usan HTML5 y CSS sin prefijos salvo cuando se indica expresamente el prefijo necesario (`-webkit-`, `-moz-`).
- **Soporte de navegadores**: cuando una característica es reciente se indica su estado (estable/experimental) y las versiones mínimas aproximadas, tomadas de MDN/browser-compat-data. Verifica siempre en <https://caniuse.com>.
- **Notación**: `propiedad`, `valor` y etiquetas en monoespaciado; **negrita** para términos clave.

## Fuentes principales consultadas

- **MDN Web Docs** (Mozilla): referencia HTML y CSS — <https://developer.mozilla.org/es/docs/Web/HTML> · <https://developer.mozilla.org/es/docs/Web/CSS>
- **W3C**: especificaciones HTML Living Standard y CSS (Selectors L4, Color L5, Grid L2, Nesting L1…), WCAG 2.1/2.2 — <https://www.w3.org/TR/html52/> · <https://www.w3.org/Style/CSS/>
- **web.dev** (Google): rendimiento y Core Web Vitals — <https://web.dev>
- **Orden de 16 de junio de 2011** (BOJA): currículo DAW/DAM en Andalucía — <https://www.juntadeandalucia.es/boja/2011/149/23>
