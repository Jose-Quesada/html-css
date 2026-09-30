---
icon: lucide/move-horizontal
title: "Unidad 05 — Flexbox"
description: "Modelo de flexión completo: ejes, propiedades del contenedor y de los items, shorthand flex, el problema de min-width:auto, centrado seguro y layouts típicos."
modulo: "LMH (0373) / DIW (0615)"
unidad: 5
fecha: "2026-09-06"
---

# Unidad 05 · Flexbox

**Flexbox es un modelo de distribución en UNA dimensión**: una fila O una columna. Es la herramienta ideal para distribuir espacio entre items y alinearlos dentro de un contenedor (navbars, toolbars, cards en fila, centrado, «espacio entre»).

Para dos dimensiones a la vez → **Grid** (unidad 06). La regla práctica:

- ¿Distribuyo contenido en una línea que puede envolver? → **Flex**.
- ¿Diseño la página/sección como cuadrícula (filas Y columnas)? → **Grid**.

!!! note "Conocimientos previos"

    - Modelo de caja y límites `min-*`/`max-*` (→ [03-modelo-de-caja.md](03-modelo-de-caja.md)).
    - Datos tabulares frente a maquetación (→ [../html/05-tablas.md](../html/05-tablas.md)).

## 1. Activación y anatomía

```css title="activacion-flex.css"
.contenedor { display: flex; }        /* o inline-flex */
```

Al activarse:

- El contenedor se convierte en **flex container**; sus hijos directos, en **flex items** (aunque sean inline, floats… dejan de comportarse como tales).
- Aparecen dos ejes:
  - **Main axis** (eje principal): dirección del flujo (`flex-direction`).
  - **Cross axis** (eje transversal): perpendicular al principal.

```text
row (default):          column:
→ main axis             ↓ main axis
↓ cross axis            → cross axis
```

El ==main axis== **reparte** el espacio; el transversal **alinea**.

`display: inline-flex` crea un contenedor flex que fluye como inline (útil para widgets embebidos en texto).

## 2. Propiedades del contenedor


| Propiedad | Valores habituales | Efecto |
|---|---|---|
| ==flex-direction== | `row` (def), `row-reverse`, `column`, `column-reverse` | Orienta el eje principal. |
| `flex-wrap` | `nowrap` (def), `wrap`, `wrap-reverse` | Permite saltar a líneas nuevas. |
| `flex-flow` | atajo de las dos anteriores: `row wrap`. |
| `justify-content` | Distribución **sobre el eje principal** (ver tabla abajo). |
| `align-items` | Alineación **sobre el eje transversal** de todos los items: `stretch` (def), `flex-start`, `flex-end`, `center`, `baseline`. |
| `align-content` | Alinea **las líneas** entre sí cuando hay `wrap`: `stretch`, `flex-start`, `center`, `space-between`, `space-around`, `space-evenly`. |
| ==`gap`== | Espacio entre items (y entre líneas si hay wrap). Soporte universal moderno. |

!!! info "Justify o align: dos reglas fijas"

    - `justify-content` → **eje principal** (el que define `flex-direction`).
    - `align-items` → **eje transversal** de todos los items.
    - `align-content` solo actúa con **varias líneas** (`wrap`).

### 2.1. `justify-content` desgranado

| Valor | Comportamiento |
|---|---|
| `flex-start` | Empaqueta al inicio del eje (default). |
| `flex-end` | Al final. |
| `center` | Centrado. |
| `space-between` | Espacios **iguales** entre items; primero y último pegados a los bordes. |
| `space-around` | Espacio igual alrededor; los bordes miden la mitad que el intermedio. |
| `space-evenly` | Espacio idéntico en todas partes (bordes incluidos). |
| `start` / `end` | Equivalentes lógicos (respetan `direction`) — preferirlos por i18n. |


### 2.2. Alineación «segura» (safe alignment)

Problema histórico: con `justify-content: center` + `overflow`, el contenido desbordado se corta **por el principio** (inaaccesible). Solución moderna:

```css title="alineacion-segura.css" hl_lines="2 3"
.contenedor {
  justify-content: safe center;   /* si no cabe, alinea al start */
  align-items: safe center;
}
```


## 3. Propiedades de los items

| Propiedad | Descripción |
|---|---|
| `order` | Orden visual (no afecta al DOM ni al foco). Default 0. Negativos válidos. |
| `flex-grow` | Factor de reparto del **espacio libre** positivo. Default 0. |
| `flex-shrink` | Factor de compresión ante **espacio negativo**. Default 1. |
| `flex-basis` | Tamaño inicial antes de repartir. Default `auto` (usa `width`/contenido). |
| `flex` | Atajo: `flex: grow shrink basis`. |
| `align-self` | Anula `align-items` para un item: `auto`, `stretch`, `flex-start`, `flex-end`, `center`, `baseline`. |

### 3.1. El atajo `flex` a fondo

| Declaración | Equivale a | Uso típico |
|---|---|---|
| `flex: initial` | `0 1 auto` | Default real de los items. |
| `flex: auto` | `1 1 auto` | Crece y se encoge desde su tamaño natural. |
| `flex: none` | `0 0 auto` | Rígido: ni crece ni encoge. |
| `flex: 1` | `1 1 0%` | **Reparte por igual** ignorando el contenido (el más usado). |
| `flex: 2 1 0%` | Doble peso de crecimiento que `flex: 1`. |

Regla de oro: ==`flex: 1`== en varios items = **anchuras proporcionales** a sus factores.

!!! info "`flex: 1` no es `flex: auto`"

    - `flex: 1` = **`1 1 0%`**: base cero, el contenido **no cuenta**.
    - `flex: auto` = **`1 1 auto`**: base el tamaño natural, que **sigue influyendo**.

### 3.2. Cómo se calcula el tamaño final (resumen)

1. Se fija `flex-basis` (o `auto` → `width`/contenido).
2. Si sobra espacio: se reparte según `flex-grow` (proporcionalmente).
3. Si falta: se quita según `flex-shrink × flex-basis` (no solo shrink: pesa también la base).
4. Los límites `min-width`/`max-width` aplican **al final** (aquí vive la trampa clásica).

## 4. La trampa: `min-width: auto`

Los flex items tienen por defecto `min-width: auto` (= su *min-content*). Consecuencia: **un item con mucho contenido no se encoge** y rompe el layout.

```css title="trampa-min-width-auto.css" hl_lines="2"
.item { flex: 1; overflow: hidden; }  /* solución 1: permite encoger */
.item { min-width: 0; }               /* solución 2: explícita */
```

Casos donde muerde: textos largos sin espacios (URLs), tablas dentro de flex, inputs largos.

> **Claves para el examen**: «mi flex no se encoge y desborda» → ==`min-width: 0`== (o `overflow` distinto de visible) en el item.

!!! question "Mi flex no se encoge"

    Una tarjeta con una URL larguísima rompe la fila. ¿Diagnóstico y arreglo?

    ??? success "Respuesta"

        Conserva `min-width: auto` y no baja de su **min-content**: `min-width: 0` **en ese item**.

!!! warning "Error común"

    Olvidar cada eje: `justify-content` va por el **principal** y `align-items` por el transversal; con ==flex-direction== `: column`, «centrar en horizontal» deja de ser `justify-content: center`.

## 5. Layouts canónicos

### 5.1. Navbar clásico

```css title="navbar-clasica.css" hl_lines="6"
.nav {
  display: flex;
  align-items: center;
  gap: 1rem;
}
.nav .logo { margin-inline-end: auto; }  /* empuja el resto a la derecha */
.nav ul { display: flex; gap: .5rem; list-style: none; }
```

Truco: `margin-inline-end: auto` en un item absorbe todo el espacio libre → efecto «push».


### 5.2. Centrado total

```css title="centrado-total.css"
.centro {
  display: flex; /* (1)! */
  justify-content: center;   /* main */
  align-items: center;       /* cross */
  min-height: 100dvh;
}
/* o el atajo moderno: */
.centro { display: grid; place-items: center; }
```

1.  Sin `min-height` no hay altura donde **centrar** en el eje transversal.

### 5.3. Fila de cards iguales que envuelven

```css
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
.card { flex: 1 1 250px; }   /* base 250px, crecen por igual */
```

### 5.4. Toolbar con grupos

```css
.toolbar { display: flex; flex-wrap: wrap; gap: .5rem; }
.grupo  { display: flex; gap: .25rem; }
.grupo--fin { margin-inline-start: auto; }
```

### 5.5. «Holy grail» simplificado (header/footer fijos de altura, sidebar flexible)

```css title="holy-grail-flex.css"
.layout {
  display: flex;
  min-height: 100dvh; /* (1)! */
}
.sidebar { flex: 0 0 16rem; }      /* rígida */
.main    { flex: 1; min-width: 0; } /* absorbe el resto */
```

1.  `min-height` hace que la columna ocupe **toda la pantalla** con poco contenido.

### 5.6. Etiqueta + valor alineados (patrón de formulario)

```css
.fila { display: flex; justify-content: space-between; gap: 1rem; }
```

!!! example "Navbar resuelto en dos líneas"

    ```css
    .nav { display: flex; align-items: center; gap: 1rem; }
    .nav .logo { margin-inline-end: auto; }
    ```

## 6. Flex vs Grid: decisión rápida

| Criterio | Flexbox | Grid |
|---|---|---|
| Dimensiones | 1D | 2D |
| El contenido define el layout | Sí (contenido-first) | No (layout-first: defines tracks y colocas) |
| Espaciado | `gap` + justify/align | `gap` + placement |
| Superposición de items | No (salvo tricks) | Sí (mismas líneas) |
| Casos ideales | Componentes, navbars, centrado, distribuir espacio | Páginas, dashboards, galerías, formularios complejos |

Se pueden **combinar**: grid para la página, flex dentro de cada celda.

## 7. Accesibilidad y orden

- ==order== cambia el **visual**, no el **DOM**: lectores de pantalla y Tab siguen el DOM. Si el orden visual difiere del lógico, documenta o cambia el HTML.
- No uses flex para reordenar semánticamente importantes cosas (p. ej., mover el footer visualmente antes que el main).


## 8. Errores comunes

| Error | Síntoma | Solución |
|---|---|---|
| Esperar que flex alinee «hijos de hijos» | No pasa nada | Flex solo actúa sobre hijos **directos**. |
| `height: 100%` en items de columna | Altura 0/extraña | Usar `align-items: stretch` (default) o alturas definidas en el contenedor. |
| Items que no encogen | Desborde horizontal | `min-width: 0` / `overflow: hidden`. |
| `float` dentro de flex | Float ignorado | Esperado: flex items no flotan. |
| Esperar que `justify-content` centre en vertical | No pasa nada | En `row`, el eje transversal se controla con `align-items` (o `margin-block: auto` en el item). |
| Olvidar `flex-wrap: wrap` | Items comprimidos hasta desaparecer | Añadir wrap o revisar bases. |

!!! success "Checklist antes de dar el flex por bueno"

    - [ ] Sé cuál es el **eje principal** con mi `flex-direction` actual.
    - [ ] `flex-wrap: wrap` está **donde quiero** (envolver) o se ha olvidado.
    - [ ] Los items con texto largo llevan `min-width: 0` o `overflow` distinto de `visible`.

## 9. Autoevaluación rápida

1. ¿Qué hace `flex: 1 1 0%` y por qué es distinto de `flex: auto`?
2. Explica la diferencia visual entre `space-between`, `space-around` y `space-evenly`.
3. Tu tarjeta con una URL larguísima rompe la fila. Diagnóstico y arreglo en una línea.
4. ¿Cómo harías que el tercer item ocupara el doble de espacio que el resto?
5. ¿Por qué `order` es peligroso para accesibilidad?

!!! tip "Claves para el examen"

    - Flexbox es **1D** (un eje reparte, el otro alinea); para filas Y columnas → Grid (unidad 06).
    - `justify-content` = eje principal; `align-items` = eje transversal; `align-content` solo con **varias líneas**.
    - `flex: 1` = `1 1 0%` (**ignora el contenido**); `flex: auto` = `1 1 auto` (**parte del contenido**).
    - El item nace con `min-width: auto`: si no se encoge, la solución es ==`min-width: 0`==.
    - `gap` separa items y `margin-*-auto` **empuja**; `order` cambia solo lo visual.

*[DOM]: Document Object Model, el árbol de elementos del documento
*[i18n]: internacionalización (del inglés *internationalization*)
