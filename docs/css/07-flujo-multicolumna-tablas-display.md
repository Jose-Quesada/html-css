---
icon: lucide/columns-3
title: "Unidad 07 — Flujo, display, multicolumna y tablas"
description: "Valores de display y sus contextos de formato, BFC, float y clear (herencia técnica), shape-outside, layout multicolumna y sistema de tablas."
modulo: "LMH (0373) / DIW (0615)"
unidad: 7
fecha: "2026-09-06"
---

# Unidad 07 · Flujo, `display`, multicolumna y tablas

Esta unidad cubre el **flujo normal del documento** y los sistemas de ordenación «clásicos». El RA 1 del módulo 0615 cita literalmente *marcos, tablas y capas* como elementos de ordenación: aquí se explica esa evolución histórica y su estado actual.

!!! note "Conocimientos previos"

    - Modelo de caja, `overflow` y colapso de márgenes (→ [03-modelo-de-caja.md](03-modelo-de-caja.md)).
    - Tablas semánticas de HTML (→ [../html/05-tablas.md](../html/05-tablas.md)).

## 1. Evolución histórica de la maquetación (contexto curricular)

| Era | Técnica | Problema |
|---|---|---|
| ~1996–2000 | **Marcos** (`<frameset>`, `<frame>`) | Cada frame = documento independiente; sin SEO, sin impresión, sin accesibilidad. **Obsoleto en HTML5**. |
| ~2000–2009 | **Tablas** para layout | Mezcla estructura y presentación; pesada; lenta; imposible de adaptar. |
| ~2005–hoy | **Capas** (`<div>` + CSS) con floats → flex/grid | Separación correcta. Los floats siguen vivos solo para imágenes flotadas. |

> **Claves para el examen**: si preguntan por «marcos», la respuesta es que están obsoletos y se sustituyen por layouts CSS (grid/flex) o, en casos muy concretos de embebidos, por `<iframe>` (que NO es un frame de layout).

## 2. `display`: el valor que define el formato

### 2.1. Valores principales

El valor ==display== decide **qué caja** genera un elemento y qué propiedades le corresponden.

| Valor | Genera | Comportamiento |
|---|---|---|
| `block` | Caja de bloque | Ocupa línea completa; acepta width/height/márgenes completos. |
| `inline` | Caja inline | Fluye con el texto; ignora width/height; márgenes solo horizontales. |
| `inline-block` | Caja inline-bloque | Fluye como inline pero acepta dimensiones y box completo. |
| `none` | Nada | No genera caja; el elemento desaparece del render (y del árbol de accesibilidad). |
| `contents` | Ninguna propia | El elemento no genera caja; **sus hijos** participan directamente en el formato del abuelo. |
| `flex` / `inline-flex` | Flex container | Ver unidad 05. |
| `grid` / `inline-grid` | Grid container | Ver unidad 06. |
| `table`, `table-row`, `table-cell`… | Tabla | Ver sección 5. |
| `flow-root` | Bloque que crea BFC | La «píldora» anti colapso de márgenes (unidad 03). |
| `run-in` | Definido en spec | **No implementado** en navegadores (no usar). |

El único «de mentira» es `run-in`: está en la spec, pero **ningún navegador lo implementa**.

!!! info "Block, inline o inline-block"

    - **block**: ocupa la línea entera y acepta `width`, `height` y márgenes.
    - **inline**: como texto: **ignora** `width`/`height` y solo admite márgenes horizontales.

### 2.2. Cambiar `display` rompe cosas

Cada valor de display cambia qué propiedades tienen sentido:

- `display: none` → el elemento ni existe para render ni para lectores de pantalla. Para «ocultar visualmente pero mantener en a11y» usa técnicas distintas (unidad 13).
- `display: contents` → el propio elemento deja de existir como caja: pierde estilos de caja, `position`, eventos al hover sobre «su área» (los hijos quedan expuestos). Cuidado con accesibilidad: algunos lectores pierden el nombre del contenedor (p. ej., un `<fieldset display:contents>` pierde su leyenda asociada en ciertos casos).
- `float` + `position` positioned → el float se ignora.
- Elementos con `display: table-cell` dentro de un div normal → el navegador les aplica *anonymous table wrappers* (comportamiento impredecible): usa siempre el contenedor `display: table`.

### 2.3. Valores externos vs internos (tablas)

En tablas hay valores de dos niveles:

```css title="display-de-tabla.css" hl_lines="2"
.tabla { display: table; }          /* externo */
.fila  { display: table-row; }      /* interno */
.celda { display: table-cell; }     /* interno */
```

El navegador envuelve automáticamente lo necesario («anonymous boxes»), pero declarar todo explícitamente evita sorpresas.

## 3. Block Formatting Context (BFC)

Un **BFC** es un ámbito de render independiente: lo que pasa dentro no afecta fuera (y viceversa). Se crea cuando un elemento cumple, entre otros:

- `display: flow-root` (la forma moderna y limpia).
- `overflow` ≠ `visible` (hidden/auto/scroll/clip).
- `position: absolute/fixed/sticky`.
- `display: inline-block/table-cell/flex/grid` (el elemento en sí).
- Floats y elementos con `float` crean su propio contexto parcial.

**Para qué sirve saberlo**:

1. **Evitar colapso de márgenes** (unidad 03): `display: flow-root` en el padre.
2. **Contener floats**: el clásico clearfix:

```css title="clearfix.css"
.clearfix::after {
  content: "";
  display: block;   /* hoy: display: flow-root en el padre es mejor */
  clear: both;
}
/* Versión moderna: .contenedor { display: flow-root; } */
```

3. **Evitar solapamiento con floats**: un bloque con BFC no se pinta bajo un float (genera *clearance* o se ajusta).
4. **Isolar animaciones/redimensiones** (rendimiento, unidad 14).

La forma moderna de crear un BFC es ==`flow-root`==: no recorta nada y resuelve el colapso de márgenes.

!!! warning "Error común"

    Usar `overflow: hidden` «porque hace BFC» **recorta** tooltips y sombras: crea el contexto con `flow-root`.

## 4. `float` y `clear` (herencia técnica imprescindible)

Aunque grid/flex dominan, el float sigue siendo **la forma correcta de flotar imágenes** en texto (como en prensa digital).

### 4.1. Mecánica

```css title="imagen-flotada.css"
.figura { float: left; margin: 0 1rem 1rem 0; }
```

- El float se extrae del flujo y se desplaza a izquierda/derecha hasta que su borde toca el borde del contenedor o otro float.
- El **texto inline** fluye alrededor; las cajas de bloque siguientes pueden solaparlo (de ahí los BFC y `clear`).
- El contenedor padre **no ve** la altura del float → necesita clearfix/BFC.


### 4.2. `clear`

| Valor | Efecto |
|---|---|
| `none` | Default; permite floats a ambos lados. |
| `left` / `right` | No permite float por ese lado (baja hasta debajo). |
| `both` | No permite floats a ningún lado. |
| `inline-start` / `inline-end` | Variantes lógicas (i18n). |

### 4.3. `shape-outside` (text wrap avanzado)

Define la **forma** alrededor de la cual fluye el texto, no solo el rectángulo:

```css title="shape-outside.css" hl_lines="3"
.figura-circular {
  float: right;
  shape-outside: circle(50%);
  margin: 0 1.5rem 1rem 1.5rem;
}
.shape-poligono {
  float: left;
  clip-path: polygon(0 0, 100% 0, 80% 100%, 0 100%);
  shape-outside: polygon(0 0, 100% 0, 80% 100%, 0 100%); /* debe coincidir */
}
```

1.  ==`shape-outside`== solo actúa sobre elementos **flotados**: sin `float`, el texto no tiene forma que rodear.

- `shape-margin` añade margen alrededor de la forma.
- Soporte bueno en Chrome/Safari/Firefox (formas básicas); `path()` solo en Chrome.

> **Claves para el examen**: diferenciar *float para layout* (antiguo, mal) de *float para imagen en texto* (válido hoy). Y saber que elclearfix moderno es `display: flow-root`.

## 5. Layout de tablas (CSS Tables)

Las tablas HTML son semánticamente **datos tabulares**; CSS las estiliza. Nunca uses tablas HTML para maquetar páginas (ver sección 1).

### 5.1. Propiedades clave

| Propiedad | Valores | Efecto |
|---|---|---|
| `table-layout` | `auto` (def) / `fixed` | `fixed`: anchos según primera fila/`<col>`; más rápido y predecible. |
| `border-collapse` | `separate` (def) / `collapse` | Bordes compartidos (estilo «grid» clásico). |
| `border-spacing` | longitud / x y | Espacio entre celdas (solo `separate`). |
| `caption-side` | `top` / `bottom` / `inline-start/end` | Posición del `<caption>`. |
| `empty-cells` | `show` / `hide` | Mostrar bordes de celdas vacías. |

El par que más se pregunta: con ==`table-layout`== `: fixed` los anchos salen de la **primera fila** (o de `<col>`), lo que hace el cálculo **rápido y predecible**; con `auto` manda el contenido.

### 5.2. Patrón: tabla responsive simple

```css title="tabla-responsive.css" hl_lines="2"
.tabla-wrap { overflow-x: auto; }   /* scroll horizontal en móvil */
table { border-collapse: collapse; min-width: 600px; }
th, td { padding: .5rem .75rem; text-align: start; }
```

Alternativas avanzadas: transformar filas en «tarjetas» con `display: block` + `data-label` en `::before` (patrón conocido; cuidado con accesibilidad: mantén la semántica de tabla o usa listas).

!!! example "Tabla que se convierte en tarjetas en móvil"

    ```css
    @media (max-width: 600px) {
      .tabla tr, .tabla td { display: block; }
      .tabla th[scope="row"] { display: none; } /* (1)! */
      .tabla td { display: flex; justify-content: space-between; }
      .tabla td::before { content: attr(data-label); }
    }
    ```

    1.  Cada `td` muestra su **etiqueta** con `attr(data-label)` sin perder semántica (→ [../html/05-tablas.md](../html/05-tablas.md)).

### 5.3. Alinear contenido de celdas

```css
td { vertical-align: middle; }        /* top | middle | bottom | baseline */
th { text-align: end; }               /* números a la derecha, habitual */
```

## 6. Multicolumna (CSS Multi-column Layout)

Para **contenido editorial** (catálogos, revistas, menús largos), no para layout de página:

```css title="multicolumna-editorial.css"
.multicolumna {
  columns: 3 250px;        /* column-count + column-width */
  column-gap: 2rem;
  column-rule: 1px solid #ddd;
}
```

1.  `columns` es un atajo: si pones las dos medidas, `column-width` actúa como **mínimo**.

| Propiedad | Descripción |
|---|---|
| `column-count` | Número entero de columnas. |
| `column-width` | Ancho ideal; el navegador calcula cuántas caben. |
| `columns` | Atajo de ambas (si ambas, `column-width` actúa como mínimo). |
| `column-gap` | Espacio entre columnas. |
| `column-rule-*` | Línea separadora. |
| `column-fill` | `auto` (con altura fija reparte) / `balance` (def, equilibra alturas). |
| `break-before/after/inside` | Control de saltos: `avoid`, `column`, `page`, `recto`, `verso`. |
| `span` | `all`: el elemento cruza todas las columnas (p. ej., subtítulos). |

Ejemplo editorial:

```css
.glosario { columns: 2; column-gap: 3rem; }
.glosario dt { break-after: avoid; font-weight: 600; }
.glosario dd { break-inside: avoid; margin-inline: 0; }
```

Limitaciones: el contenido fluye **verticalmente** dentro de cada columna (primero rellena la 1, luego la 2…). No sirve para «distribuir tarjetas» (eso es grid `auto-fit`).

!!! info "Multicolumna no es grid"

    - Las columnas de `columns` las **crea el texto**: no colocas nada en «la columna 2».
    - Tarjetas y galerías → `grid` con `auto-fit`; prosa larga → `columns`.

!!! question "Dos medidas, dos comportamientos"

    En 800 px, ¿en qué se diferencian `column-count: 3` y `column-width: 250px`?

    ??? success "Respuesta"

        `column-count: 3` → **exactamente 3** de ~266 px (manda el número). `column-width: 250px` → **tantas de 250 px o más** como quepan, sin fijar el número.

## 7. `writing-mode` y orientación del texto

Relevante para i18n (japonés, chino, árabe…) y diseños editoriales:

```css
.titulo-vertical { writing-mode: vertical-rl; }  /* vertical, líneas derecha→izquierda */
```

Valores: `horizontal-tb` (def), `vertical-rl`, `vertical-lr`. Afecta a ejes lógicos (ver propiedades lógicas, unidad 12).

## 8. Resumen comparativo de sistemas de ordenación

| Sistema | Dimensión | Caso de uso actual | Estado |
|---|---|---|---|
| Frames | — | Ninguno | Obsoleto |
| Tablas (layout) | 2D (rígida) | Solo datos tabulares | Válido para datos |
| Float | 1D + wrap de texto | Imágenes flotadas en prosa | Válido (uso específico) |
| Multicolumna | Columnas de flujo | Contenido editorial denso | Válido |
| Flexbox | 1D | Componentes, distribución | Estándar principal |
| Grid | 2D | Páginas, secciones, dashboards | Estándar principal |


## 9. Autoevaluación rápida

1. ¿Por qué `display: contents` puede ser peligroso para accesibilidad?
2. Nombra tres formas de crear un BFC y una utilidad de cada una.
3. ¿Cuándo es legítimo usar `float` hoy? ¿Y `clear: both`?
4. Diferencia entre `column-count: 3` y `column-width: 250px` cuando el contenedor mide 800px.
5. ¿Qué hace `table-layout: fixed` y por qué mejora el rendimiento?
6. Explica por qué las tablas HTML no deben usarse para maquetar una web.

!!! success "Checklist antes de dar la maquetación por buena"

    - [ ] La estructura sale de **flex/grid**, no de tablas ni floats.
    - [ ] Si necesito un BFC uso **`display: flow-root`**.
    - [ ] Los floats llevan clearfix/BFC y el texto **fluye** alrededor.
!!! tip "Claves para el examen"

    - `display`: `block` ocupa línea, `inline` ignora `width/height`, `inline-block` une lo mejor de ambos.
    - `display: none` **borra** el elemento (y para lectores de pantalla); `display: contents` deja **sin caja** y expone a los hijos.
    - ==`flow-root`== crea un BFC **sin efectos secundarios**; `overflow` ≠ `visible`, pero recorta.
    - `float` hoy: **solo imágenes en texto** (el clearfix moderno es `display: flow-root` en el padre); `shape-outside` da forma al texto que lo rodea.

*[BFC]: Block Formatting Context, ámbito de render independiente
*[a11y]: accesibilidad (del inglés *accessibility*)
