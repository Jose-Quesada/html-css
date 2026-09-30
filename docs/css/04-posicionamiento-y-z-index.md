---
icon: lucide/move
title: "Unidad 04 — Posicionamiento y z-index"
description: "Propiedad position en todos sus valores, bloques contenedores, offsets, contexto de apilamiento y z-index explicados a fondo, position: sticky y patrones prácticos."
modulo: "LMH (0373) / DIW (0615)"
unidad: 4
fecha: "2026-09-06"
---

# Unidad 04 · Posicionamiento y z-index

`position` decide **cómo se sitúa** la caja respecto al flujo normal del documento. Junto con el concepto de *contexto de apilamiento*, es uno de los temas con más «magia negra» aparente… hasta que se entiende.

!!! note "Conocimientos previos"

    - Flujo normal y modelo de caja (→ [03-modelo-de-caja.md](03-modelo-de-caja.md)).
    - `float` y `display`, que aquí interaccionan (→ [07-flujo-multicolumna-tablas-display.md](07-flujo-multicolumna-tablas-display.md)).

## 1. Los cinco valores de `position`


| Valor | Comportamiento | Sale del flujo? |
|---|---|---|
| `static` (default) | Flujo normal; ignora `top/right/bottom/left`. | No |
| `relative` | Flujo normal + desplazamiento **visual** desde su posición original (el espacio reservado se mantiene). | No |
| ==`absolute`== | Se posiciona respecto a su **bloque contenedor**; el espacio original desaparece. | Sí |
| `fixed` | Como `absolute`, pero respecto al **viewport** (no se mueve al hacer scroll). | Sí |
| ==`sticky`== | Híbrido: se comporta como `relative` hasta alcanzar un umbral, luego «se pega» como `fixed` dentro de su contenedor. | No |

## 2. Bloque contenedor (containing block)

El elemento de referencia para `absolute`/`fixed` y para porcentajes de offsets:

1. Para `position: absolute`: el **ancestro más cercano** con `position` ≠ `static` (o `transform`, `filter`, `perspective`, `contain: layout`… ver abajo). Si no existe, el *initial containing block* (≈ viewport).
2. Para `position: fixed`: el **viewport**, salvo que un ancestro tenga `transform`, `perspective`, `filter`, `backdrop-filter`, `contain: paint/layout` o `will-change` de esas propiedades → entonces ese ancestro se convierte en su bloque contenedor (bug clásico de modales que «saltan»).
3. Para `position: sticky`: el **contenedor padre directo** (solo puede moverse dentro de él).

!!! info "Los porcentajes se miden aquí"

    `top: 50%` se calcula sobre el **alto del bloque contenedor**, no sobre la ventana.

> **Claves para el examen**: «¿Respecto a qué se posiciona un elemento absoluto?» → el ancestro positioned más cercano. Y saber que `transform` en un abuelo rompe el `fixed` de un nieto.

## 3. Offsets: `top`, `right`, `bottom`, `left` y `inset`

```css title="offsets-y-inset.css" hl_lines="2 5"
.capa {
  position: absolute; /* (1)! */
  top: 1rem; right: 1rem;
  /* atajo moderno: */
  inset: 0;              /* rellena todo el bloque contenedor */
  inset: 1rem 2rem;      /* vertical horizontal */
}
```

1.  Sin `position` ≠ `static`, los offsets de debajo se ignoran.

Reglas de interacción (para `absolute`):

- Con `top`+`bottom` definidos y `height: auto` → la altura se resuelve entre ambos.
- Con `left`+`right` y `width: auto` → idem en horizontal.
- Con los cuatro y dimensiones fijas → **se ignora el valor según la dirección** (`direction: ltr` ignora `right`; `rtl` ignora `left`).
- En `relative`, los offsets son **desplazamientos** (pueden ser negativos).

Atajo moderno: ==`inset`== resume los cuatro offsets en una sola línea.

## 4. `z-index` y contexto de apilamiento ⚠️

### 4.1. Qué es un contexto de apilamiento (stacking context)

Es una «capa aislada»: dentro de ella, los ==`z-index`== se comparan **entre sí**; fuera, solo cuenta el `z-index` del propio contexto. Un elemento **crea** contexto de apilamiento cuando, entre otros casos:

- Tiene `position` ≠ `static` **y** `z-index` ≠ `auto` (incluido `z-index: 0`).
- Es flex/grid item con `z-index` ≠ `auto`.
- Tiene `opacity < 1`.
- Tiene `transform`, `perspective`, `filter`, `backdrop-filter` ≠ `none`.
- Tiene `will-change` con alguna de esas propiedades.
- Tiene `contain: paint` (o `strict`/`content`).
- Tiene `isolation: isolate` (la **forma explícita y recomendada**).
- Elementos con `mix-blend-mode` ≠ `normal`.
- `<iframe>`, elementos SVG con `isolation`, etc.

!!! info "Truco para adivinar contextos"

    Si el elemento **aisla** su contenido (`opacity`, `transform`, `filter`), crea **contexto de apilamiento**.

### 4.2. Orden de apilamiento DENTRO de un contexto

De atrás hacia delante:

1. Fondo y bordes del elemento que crea el contexto.
2. Hijos con `z-index` **negativo** (de mayor a menor).
3. Bloques en flujo normal (sin posición).
4. Floats.
5. Inlines en flujo.
6. Elementos positioned con `z-index: auto` o `0` (en orden de aparición en el **DOM**).
7. Elementos positioned con `z-index` **positivo** (de menor a mayor).

### 4.3. Ejemplo clásico del «z-index que no funciona»

```html title="z-index-que-no-funciona.html"
<div class="tarjeta">        <!-- sin position ni z-index --> <!-- (1)! -->
  <button>Me pisan</button>
</div>
<nav class="menu"></nav>     <!-- position: relative; z-index: 10 --> <!-- (2)! -->
```

1.  `.tarjeta` **no** crea contexto: sus hijos compiten en la escala global.
2.  El `nav` sí crea contexto con `z-index: 10`, así que gana.

Si `.tarjeta` contiene un elemento con `position: relative; z-index: 20`, **parece** que debería salir por encima del nav… pero si `.tarjeta` no crea contexto, el 20 se compara globalmente y gana. El fallo típico inverso: `.tarjeta` SÍ crea contexto (p. ej., tiene `opacity: .99`) y su `z-index` es `auto` → todo lo interno queda «atrapado» bajo el nav aunque los hijos lleven `z-index: 9999`.

**Solución**: subir el `z-index` del **contexto** (`.tarjeta { position: relative; z-index: 11 }`), no del hijo.

!!! warning "Error común"

    Posicionar sin contexto: un `absolute` **sin ancestro positioned** vuela, y el `z-index` de un hijo **no sube** si su padre no crea contexto. Arregla el **contenedor**.

> **Claves para el examen**: dibujar la jerarquía de contextos y explicar por qué `z-index` solo se compara **dentro del mismo contexto**. Pregunta estrella: «tengo z-index: 9999 y no sube, ¿por qué?».

### 4.4. Buena práctica: escala de z-index

Define una **escala documentada** (mejor, con custom properties):

```css title="escala-de-z-index.css" hl_lines="6"
:root {
  --z-bajo: 1;        /* fondos decorativos */
  --z-normal: 2;
  --z-header: 100;    /* cabecera sticky */
  --z-dropdown: 200;
  --z-modal: 300;
  --z-toast: 400;
  --z-tooltip: 500;
}
```

Evita `z-index: 9999` escalando conflictos; usa `isolation: isolate` para aislar componentes y no contaminar la escala global.

## 5. `position: sticky` en profundidad

```css title="cabecera-sticky.css" hl_lines="3"
.cabecera {
  position: sticky;
  top: 0;                 /* umbral respecto al borde superior del scroll portador */
  z-index: var(--z-header);
}
```

Características y trampas:

- Se «pega» **dentro de su contenedor directo**: cuando el contenedor termina, la cabecera se va con él.
- Necesita un **offset** (`top`/`bottom`/`left`/`right`); sin offset no hace nada.
- Un ancestro con `overflow: hidden/auto/scroll` **rompe** el sticky (ese ancestro se convierte en scroll portador). Revisa la cadena de padres.
- Los márgenes del elemento cuentan: `margin-top` desplaza el punto de enganche.
- No colapsa márgenes (no está en flujo «puro»).
- Usos: **cabeceras de tabla, TOC lateral, barras de acción**, columnas pegadas en tablas grandes.

!!! question "Mi sticky no se pega"

    He escrito `position: sticky; top: 0` y la cabecera no se mueve. ¿Dos causas?

    ??? success "Respuesta"

        1. **Falta el offset**: sin `top`/`bottom` no hay umbral y no se desplaza.
        2. Un **ancestro con `overflow`** es el scroll portador, o su contenedor ya terminó.

## 6. `position: fixed` y móvil

- Referencia al viewport: cuidado con la barra de direcciones de móviles que aparece/desaparece → las unidades `dvh/svh/lvh` (unidad 08/10) resuelven **alturas estables**.
- `env(safe-area-inset-*)` para no tapar zonas de notch/home-indicator:

```css
.barra {
  position: fixed; bottom: 0; left: 0; right: 0;
  padding-bottom: env(safe-area-inset-bottom);
}
```


## 7. Patrones prácticos

### 7.1. Overlay que cubre todo

```css title="overlay-fijo.css"
.overlay {
  position: fixed; inset: 0;
  background: rgb(0 0 0 / .5);
  z-index: var(--z-modal);
}
```

### 7.2. Modal centrado robusto

```css title="modal-centrado.css"
.modal {
  position: fixed; inset: 0;
  margin: auto;
  width: min(90vw, 32rem);
  max-height: 85dvh;
  overflow: auto;
}
```

(`inset: 0` + `margin: auto` centra sin calcular posiciones.)

### 7.3. Tooltip anclado

```css
.relativo { position: relative; }
.tooltip {
  position: absolute;
  bottom: calc(100% + .5rem);   /* justo encima */
  left: 50%;
  translate: -50% 0;            /* propiedad individual moderna */
  white-space: nowrap;
}
```

### 7.4. Parallax simple con sticky

```css
.parallax { height: 300vh; }
.parallax .escena {
  position: sticky; top: 0;
  height: 100vh;
  /* animación ligada al scroll en unidad 11 */
}
```

### 7.5. Cabecera sticky con sombra al hacer scroll

```css
header { position: sticky; top: 0; transition: box-shadow .3s; }
/* JS mínimo o :has() avanzado para detectar scroll; alternativa pura CSS con scroll-driven animations (U11) */
```

!!! example "Overlay + modal en dos reglas"

    ```css
    .overlay { position: fixed; inset: 0; z-index: var(--z-modal); }
    .modal { position: fixed; inset: 0; margin: auto; }
    ```

## 8. Interacciones con otras propiedades

| Propiedad | Efecto sobre posicionamiento |
|---|---|
| `transform` | Crea bloque contenedor para `absolute/fixed` descendientes + contexto de apilamiento. |
| `filter` / `backdrop-filter` | Idem. |
| `will-change: transform` | Idem (anticipado). |
| `contain: layout/paint` | Aísla layout/pintura; afecta a `fixed`. |
| `display: contents` | El elemento deja de generar caja: su `position` se pierde (los hijos «heredan» el contexto del abuelo). |
| `float` | Genera BFC parcial; incompatible con `position` positioned (el float se ignora). |


## 9. Errores comunes

| Error | Síntoma | Solución |
|---|---|---|
| `absolute` sin ancestro positioned | Vuela a la esquina del viewport | Añadir `position: relative` al contenedor lógico. |
| `fixed` que «salta» al abrir modal | El modal se descoloca | Eliminar `transform/filter` de ancestros del portal, o montar el modal en `<body>` (portal). |
| Sticky que no se pega | Queda quieto | Buscar `overflow` en ancestros; comprobar offset. |
| Guerra de `z-index: 9999` | Caos de capas | Escala de variables + `isolation: isolate`. |
| `top/left` con `static` | No pasa nada | Esperado: static ignora offsets. |

!!! success "Checklist de posicionamiento"

    - [ ] Los `absolute` apuntan al **contenedor lógico** correcto.
    - [ ] Ningún ancestro con `transform/filter` rompe mi `fixed`/`sticky`.
    - [ ] Los `z-index` salen de una **escala con variables**.

## 10. Autoevaluación rápida

1. Enumera cinco formas (además de `position+z-index`) de crear un contexto de apilamiento.
2. ¿Por qué un `position: fixed` dentro de un carrusel con `transform` se mueve con el carrusel?
3. Tu tooltip tiene `z-index: 9999` y sigue debajo del header. Explica dos causas posibles y su arreglo.
4. ¿Qué rompería primero un `position: sticky`: un `overflow: hidden` en el body o en el padre directo?
5. Escribe el CSS para una barra fija inferior que respete el safe-area de iOS.

!!! tip "Claves para el examen"

    - `static` **ignora** los offsets; `relative` desplaza **sin** salir del flujo; `absolute`/`fixed` **sí** salen.
    - Bloque contenedor: **ancestro positioned más cercano** en `absolute`; **viewport** en `fixed` (salvo `transform`/`filter`). Crea contexto de apilamiento `position` ≠ `static` con `z-index` ≠ `auto`, y también `opacity`, `transform`, `filter` o `isolation: isolate`.
    - **Dentro** de un contexto los `z-index` se comparan **entre sí**: «tengo 9999 y no sube» → revisa el **contenedor**.
    - `sticky` necesita **offset** y un padre **sin `overflow`**; para centrar, `inset: 0` + `margin: auto` (§7.2).

*[viewport]: área visible de la ventana del navegador (la ventana de render)
