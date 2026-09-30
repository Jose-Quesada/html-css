---
title: "Unidad 03 — Modelo de caja"
description: "Box model completo: content/padding/border/margin, box-sizing, dimensiones y límites, colapso de márgenes, overflow, tamaño intrínseco, aspect-ratio y patrones prácticos."
modulo: "LMH (0373) / DIW (0615)"
unidad: 3
fecha: "2026-09-06"
---

# Unidad 03 · Modelo de caja

Todo elemento renderizado es una **caja rectangular** en el flujo del documento. Entender exactamente cómo se calcula su tamaño es la base de toda maquetación.

## 1. Anatomía de la caja

```text
┌──────────────────────────────────────────────┐ ← margen (margin)
│ ┌──────────────────────────────────────────┐ │
│ │ ┌──────────────────────────────────────┐ │ │ ← borde (border)
│ │ │ ┌──────────────────────────────────┐ │ │ │ ← padding
│ │ │ │                                  │ │ │ │
│ │ │ │        CONTENIDO (content)       │ │ │ │
│ │ │ │                                  │ │ │ │
│ │ │ └──────────────────────────────────┘ │ │ │
│ │ └──────────────────────────────────────┘ │ │
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘
```

| Capa | Propiedades | Notas |
|---|---|---|
| Contenido | `width`, `height` | Tamaño del contenido (no de la caja completa). |
| Padding | `padding`, `padding-top/right/bottom/left`, `padding-inline/block` | Espacio interior; admite `%` (sobre el ancho del contenedor padre). |
| Borde | `border-width/style/color`, `border-*-radius` | El `style` es obligatorio para que el borde se pinte. |
| Margen | `margin`, `margin-*`, `margin-inline/block` | Espacio exterior; puede ser negativo. |

Propiedades de atajo: `box-shadow` (fuera de la caja pero dentro del «área de pintura»), `outline` (no ocupa espacio, se dibuja fuera del borde).

## 2. `box-sizing`: el cambio que lo cambia todo

### 2.1. `content-box` (default histórico)

`width` define solo el contenido:

```text
ancho total = width + padding-left + padding-right + border-left + border-right
```

### 2.2. `border-box` (el estándar de facto moderno)

`width` define la caja **incluyendo** padding y borde:

```text
ancho total = width   (ya incluye padding y border)
```

```css
/* Reset universal recomendado */
*, *::before, *::after {
  box-sizing: border-box;
}
```

> **Claves para el examen**: con `border-box`, si declaras `width: 300px; padding: 20px; border: 5px solid`, la caja mide 300 px en total. Con `content-box`, mediría 350 px. Pregunta típica: calcular el ancho resultante en ambos modos.

### 2.3. ¿Por qué `border-box`?

- Los cálculos a mano coinciden con lo que ves.
- Evita sorpresas al añadir padding a elementos de ancho fijo.
- Es la premisa de casi todos los frameworks y design systems.

## 3. Dimensiones: `width` y `height`

### 3.1. Valores

- **Longitudes**: `px`, `rem`, `%`, `vw/vh`, `ch`, `clamp()`…
- **`auto`** (default):
  - En bloque horizontal: llena el contenedor (menos padding/borde propios).
  - En vertical: crece con el contenido.
- **Palabras clave intrínsecas** (solo `width`/`height` en ciertos contextos):
  - `min-content`: el más estrecho posible sin romper contenido.
  - `max-content`: el más ancho posible en una línea.
  - `fit-content`: `min(max(min-content, disponible), max-content)` → «lo justo».

```css
.etiqueta { width: fit-content; }      /* se ajusta al texto */
.tabla-col { width: min-content; }     /* columna mínima legible */
```

### 3.2. Límites: `min-*` y `max-*`

```css
input {
  width: 100%;
  min-width: 12rem;    /* nunca por debajo */
  max-width: 24rem;    /* nunca por encima */
}
```

Reglas importantes:

- `min-width`/`min-height` **ganan** ante `width`/`height` cuando entran en conflicto.
- `max-width: 100%` en imágenes/media evita desbordes clásicos.
- En flex/grid, `min-width: auto` impide que un item se encoga menos que su contenido (ver unidad 05, problema clásico).

### 3.3. `aspect-ratio`

Mantiene proporción entre anchura y altura:

```css
.thumb {
  width: 100%;
  aspect-ratio: 16 / 9;   /* o 1.777 */
}
.avatar { aspect-ratio: 1; }  /* cuadrado */
```

- Funciona con `width` o `height` definidos (o `auto` en reemplazos como `<img>`).
- Se combina con `object-fit` para controlar el relleno de media (unidad 09).
- Permite **reservas de espacio** anti CLS: el contenedor reserva la proporción antes de cargar la imagen (unidad 14).

## 4. Márgenes

### 4.1. Valores y atajos

```css
.margen {
  margin: 1rem 2rem;          /* vertical horizontal */
  margin: 1rem 2rem 3rem 4rem;/* arriba derecha abajo izquierda */
  margin-block: 2rem;         /* logical: arriba+abajo */
  margin-inline-start: 1rem;  /* logical: lado de inicio (i18n) */
}
```

### 4.2. Colapso de márgenes (margin collapsing) ⚠️

Es uno de los conceptos **más examinados** del CSS clásico.

**Regla**: cuando dos márgenes verticales de bloques en el mismo BFC se tocan, **no se suman**: se colapsan en uno solo, cuyo valor es el **máximo** (en valor absoluto) de los implicados.

Casos:

1. **Entre hermanos consecutivos**:

```css
p { margin: 1rem 0; }
/* <p>A</p><p>B</p> → el espacio entre A y B es 1rem, no 2rem */
```

2. **Padre-hijo (sin separación)**: si el padre no tiene padding/borde superior ni `overflow` distinto de visible, el margen superior del hijo «sale» del padre:

```css
section { }            /* sin padding-top ni border-top */
section > p:first-child { margin-top: 2rem; }
/* El section entero baja 2rem: el margen «escapa» */
```

3. **Vacío**: dos elementos vacíos con margen colapsan igualmente.
4. **Márgenes opuestos signos**: `1rem` + `-2rem` → colapsan a `-1rem`.

**No colapsan** cuando:

- Hay algo que separe: padding, borde, `inline-content`, clearance.
- El elemento crea un **nuevo BFC** (`overflow: hidden/auto/scroll`, `display: flow-root/flex/grid/table-caption…`).
- Posicionamiento distinto de `static` (absoluto/fijo no colapsan con nada).
- En flex/grid containers, los márgenes de items **nunca** colapsan.
- Márgenes horizontales **nunca** colapsan (solo verticales de bloques).

**Soluciones habituales**:

```css
/* 1. flow-root: convierte al bloque en BFC (la más limpia) */
article { display: flow-root; }

/* 2. overflow (cuidado: recorta) */
.card { overflow: hidden; }

/* 3. padding/borde en el padre */
section { padding-top: 1px; } /* truco feo, evitar */

/* 4. :first-child / :last-child para anular márgenes internos */
.section > :first-child { margin-top: 0; }
.section > :last-child  { margin-bottom: 0; }
```

> **Claves para el examen**: explicar QUÉ colapsa, CUÁNDO no colapsa, y dar dos soluciones distintas. El «hijo que empuja al padre» es el caso favorito de los exámenes.

### 4.3. Márgenes negativos

```css
.full-bleed {
  margin-inline: calc(50% - 50vw);  /* rompe el contenedor a ancho total */
}
.overlap { margin-top: -2rem; }     /* superpone con el anterior */
```

Útiles para: full-bleed, solapamientos, corregir spacing de librerías. Cuidado con accesibilidad (contenido tapado) y mantenimiento.

## 5. `overflow`

Controla qué pasa cuando el contenido supera la caja:

| Valor | Comportamiento |
|---|---|
| `visible` (default) | Se desborda pintándose fuera. |
| `hidden` | Se recorta; **no** hay barras. |
| `scroll` | Barras siempre visibles. |
| `auto` | Barras solo si hace falta (el más usado). |
| `clip` | Como `hidden` pero **sin** crear contenedor de scroll (mejor rendimiento, no focusable). |

Detalles:

- Si uno de los ejes es `visible` y el otro no, el `visible` se convierte en `auto` (comportamiento contraintuitivo a recordar).
- `overflow-x` / `overflow-y` independientes.
- `overscroll-behavior` controla el «rubber-band»/propagación de scroll en móviles.
- **Crear `overflow` ≠ visible genera nuevo BFC** → corta colapso de márgenes (ver 4.2).
- `text-overflow: ellipsis` requiere `overflow: hidden` + `white-space: nowrap`.

## 6. Contención (`contain`)

Indica al navegador que ciertas partes del render son **independientes**, permitiendo optimizaciones:

| Valor | Aísla |
|---|---|
| `contain: layout` | Lo que pasa dentro no afecta al layout exterior (y viceversa). |
| `contain: paint` | El contenido no se pinta fuera de la caja (equivale a `overflow: clip` visualmente). |
| `contain: style` | Las `@counter`/`@font-face` internos no escapan. |
| `contain: strict` | layout + paint + size. |
| `contain: content` | layout + paint. |

```css
.lista-virtual .item { contain: content; }
```

Advertencia: `contain: size` hace que el elemento ignore el tamaño de su contenido (peligroso sin `contain-intrinsic-size`). Se profundiza en rendimiento (unidad 14).

## 7. `resize` y `cursor`

```css
.editable {
  resize: both;      /* both | horizontal | vertical | none */
  overflow: auto;    /* necesario para que funcione */
}
```

Permite al usuario redimensionar cajas (útil en paneles, widgets).

## 8. Patrones prácticos de caja

### 8.1. Centrado perfecto (bloques)

```css
/* Horizontal */
.centrado { margin-inline: auto; max-width: 60rem; }

/* Vertical + horizontal en un contenedor fijo */
.modal {
  position: absolute; inset: 0;
  margin: auto;
  width: fit-content; height: fit-content;
}
/* (Alternativas con flex/grid en unidades 05–06) */
```

### 8.2. Full-bleed dentro de contenedor centrado

```css
.contenido { max-width: 65rem; margin-inline: auto; padding-inline: 1rem; }
.banner {
  margin-inline: calc(50% - 50vw);
  padding-inline: calc(50vw - 50% + 1rem); /* compensa el padding del padre */
}
```

### 8.3. Caja con ratio fijo y contenido fluido

```css
.video-frame {
  position: relative;
  width: 100%;
  aspect-ratio: 16/9;
}
.video-frame iframe {
  position: absolute; inset: 0;
  width: 100%; height: 100%; border: 0;
}
```

### 8.4. Limitar reflow de columnas de texto largo

```css
.prosa {
  max-width: 68ch;   /* ~68 caracteres por línea: legibilidad óptima */
}
```

## 9. Errores comunes (repaso)

| Error | Síntoma | Causa/solución |
|---|---|---|
| No usar `border-box` | Cajas que «crecen» al añadir padding | Reset global `box-sizing: border-box`. |
| Sorpresa de colapso | El container «baja» solo | Nuevo BFC (`flow-root`) o `:first-child { margin-top: 0 }`. |
| `overflow: hidden` «mágico» | Recorta tooltips/dropdowns | Usar `clip` con cuidado o repensar el layout. |
| Imagen que rompe el layout | Desborde horizontal | `max-width: 100%; height: auto; display: block;`. |
| Altura fantasma bajo inline | Hueco bajo imágenes/frases | `vertical-align: middle` o `display: block` en el media. |

## 10. Autoevaluación rápida

1. Con `content-box`: `width: 200px; padding: 10px; border: 2px`. ¿Cuánto mide la caja? ¿Y con `border-box`?
2. Dos párrafos con `margin: 2rem 0` seguidos: ¿cuánto espacio hay entre ellos? ¿Cómo harías que fueran 4 rem?
3. Un `div` vacío con `margin-top: 3rem` dentro de una sección sin padding: ¿qué pasa? ¿Tres formas de evitarlo?
4. ¿Qué valor de `overflow` usarías para recortar sin crear scroll ni foco?
5. Explica `fit-content` con la fórmula `min(max(...))`.
