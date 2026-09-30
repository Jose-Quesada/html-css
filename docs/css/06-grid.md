---
icon: lucide/layout-grid
title: "Unidad 06 — CSS Grid"
description: "Sistema de cuadrícula bidimensional: pistas, líneas, áreas, unidades fraccionarias, minmax(), auto-fill/auto-fit, flujo denso, subgrid y patrones responsivos sin media queries."
modulo: "LMH (0373) / DIW (0615)"
unidad: 6
fecha: "2026-09-06"
---

# Unidad 06 · CSS Grid

**Grid es un sistema de maquetación bidimensional**: controlas filas Y columnas a la vez. Es *layout-first*: primero defines la estructura (pistas) y luego colocas el contenido en ella. Es la herramienta por defecto para diseñar páginas, secciones y dashboards.

!!! note "Conocimientos previos"

    - Flexbox y su lógica de ejes (→ [05-flexbox.md](05-flexbox.md)).
    - Modelo de caja, `min-width: 0` y `box-sizing` (→ [03-modelo-de-caja.md](03-modelo-de-caja.md)).

## 1. Activación y vocabulario

```css title="activacion-grid.css"
.galeria { display: grid; }
```

| Término | Significado |
|---|---|
| **Grid container** | El elemento con `display: grid`. |
| **Grid item** | Hijos directos del contenedor. |
| **Track (pista)** | Una fila o una columna. |
| **Line (línea)** | Borde de una pista; se numeran desde 1. |
| **Cell (celda)** | Intersección de una fila y una columna. |
| **Area (área)** | Rectángulo formado por 4 líneas. |

```text
      línea1   línea2   línea3   línea4
        ┌────────┬────────┬────────┐
  fila1 │  celda │  celda │  celda │
        ├────────┼────────┼────────┤
  fila2 │  celda │  celda │  celda │
        └────────┴────────┴────────┘
```


## 2. Definir la cuadrícula explícita

### 2.1. `grid-template-columns` / `grid-template-rows`

```css title="plantilla-explicita.css"
.g {
  grid-template-columns: 200px 1fr 1fr;   /* 3 columnas */
  grid-template-rows: auto 100px;         /* 2 filas */
}
```

Funciones útiles dentro:

| Función | Descripción |
|---|---|
| `repeat(n, …)` | Repite: `repeat(3, 1fr)` = `1fr 1fr 1fr`. |
| `minmax(min, max)` | Pista flexible entre dos límites: `minmax(250px, 1fr)`. |
| `fit-content(len)` | Se ajusta al contenido hasta `len`. |
| `auto` | Tamaño según el contenido de sus items. |

### 2.2. La unidad `fr`

`fr` = **fracción del espacio libre** tras repartir las pistas no fraccionarias.

```css
grid-template-columns: 1fr 2fr;
/* De 900px libres: col1 = 300px, col2 = 600px */
```

Reglas que hay que dominar:

- `1fr 1fr 1fr` ≠ «un tercio cada uno» si hay márgenes/gaps: el gap se resta antes.
- `fr` + `minmax`: `minmax(0, 1fr)` evita que el contenido mínimo inflé la pista (equivalente práctico a `min-width: 0` en flex).
- Mezclar: `250px 1fr 2fr` → fijo + reparto 1:2 del resto.

!!! info "Qué es realmente `fr`"

    `fr` mide el **espacio que sobra**: pistas fijas primero, `gap` después y lo demás se reparte. Si no queda nada, `1fr` se resuelve a **0**.

### 2.3. Gaps

```css title="gaps.css"
gap: 1rem;            /* row-gap + column-gap */
row-gap: 1rem; column-gap: 2rem;
```

El gap **no** cuenta como pista ni como línea; existe entre pistas.

## 3. Cuadrícula implícita y `auto-*`

Si hay más items que celdas explícitas, Grid crea **pistas implícitas** automáticamente:

```css title="auto-rows-y-auto-flow.css"
.g {
  grid-template-columns: repeat(3, 1fr); /* (1)! */
  grid-auto-rows: 120px;          /* altura de las filas implícitas */
  grid-auto-flow: row;            /* row | column | row dense | column dense */
}
```

1.  Lo que declares con `grid-template-*` es la cuadrícula **explícita**; lo que aparece después, la **implícita**.

- `grid-auto-flow: dense`: rellana huecos anteriores si cabe un item posterior (**packing denso**); cambia el orden visual respecto al DOM (accesibilidad: documentar).
- `grid-auto-columns`: ancho de columnas implícitas (cuando `auto-flow: column`).

## 4. Colocar items

### 4.1. Por líneas

```css title="colocar-items-por-lineas.css"
.item {
  grid-column: 1 / 3;      /* de la línea 1 a la 3 → ocupa 2 columnas */
  grid-row: 2;             /* una sola línea → fila 2 */
  /* atajo: */
  grid-area: 2 / 1 / span 2 / span 3;  /* fila / col / filas / cols */
}
```

Notas:

- `span 2`: avanza 2 pistas.
- Líneas negativas cuentan desde el final: `grid-column: -1 / 1`.
- `grid-column: 1 / -1` → **toda la anchura** (truco omnipresente).
- Si omites un lado (`grid-row-start` solo), el otro se calcula con `auto` (1 pista, o según `auto-flow`).

### 4.2. Líneas nombradas

```css
.g {
  grid-template-columns:
    [sidebar] 250px [sidebar-fin contenido] 1fr [contenido-fin];
}
.item { grid-column: sidebar / contenido; }
```

Permite nombres repetidos (útil con `repeat`): `repeat(3, [col-start] 1fr [col-end])`.

### 4.3. `grid-template-areas` (el favorito para layouts de página)

```css title="pagina-con-grid-template-areas.css" hl_lines="3 4"
.pagina {
  display: grid;
  grid-template-areas:
    "cabecera cabecera cabecera"
    "nav      main     aside"
    "pie      pie      pie";
  grid-template-columns: 200px 1fr 250px;
  grid-template-rows: auto 1fr auto;
}
.cabecera { grid-area: cabecera; }
.nav      { grid-area: nav; }
.main     { grid-area: main; }
.aside    { grid-area: aside; }
.pie      { grid-area: pie; }
```

Ventajas: legible, fácil de reordenar cambiando solo la «imagen de texto» con ==grid-template-areas==, y permite responsive trivial:

```css title="grid-areas-responsivo.css"
@media (max-width: 700px) {
  .pagina {
    grid-template-areas:
      "cabecera"
      "main"
      "nav"
      "aside"
      "pie";
    grid-template-columns: 1fr;
  }
}
```

## 5. Alineación dentro de la celda

| Propiedad | Alinea |
|---|---|
| `justify-items` | Items sobre el **eje inline** (horizontal en LTR) dentro de su celda: `start`, `end`, `center`, `stretch` (def). |
| `align-items` | Sobre el **bloque** (vertical). |
| `place-items` | Atajo de ambas: `place-items: center` centra en los dos ejes. |
| `justify-content` / `align-content` / `place-content` | Alinean **el conjunto de pistas** dentro del contenedor (cuando las pistas no llenan todo). |
| `justify-self` / `align-self` / `place-self` | Anulación por item. |

Valores adicionales de content: `space-between`, `space-around`, `space-evenly`, `start/end`.

!!! info "¿`items` o `content`?"

    - `place-items` → el **contenido en su celda**; `place-content` → **las pistas** (solo si no lo llenan).
    - ==`place-items`== `: center` centra en los dos ejes en una línea.

## 6. Responsivo SIN media queries: `auto-fit` vs `auto-fit`… ¡y `auto-fill`!

El patrón de galería fluida más usado del mundo:

```css title="galeria-fluida.css" hl_lines="3"
.galeria {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
}
```

¿Qué hace? Crea tantas columnas de «mínimo 240px» como quepan; el sobrante se reparte (`1fr`).

Diferencia clave (pregunta de examen):

| Valor | Comportamiento cuando sobra espacio |
|---|---|
| `auto-fill` | Mantiene **columnas vacías** (reserva huecos). Útil si vas a añadir items después o quieres «slots». |
| `auto-fit` | **Colapsa** las columnas vacías y estira las ocupadas. El look «galería elástica» clásico. |

Variante con límite superior: `repeat(auto-fit, minmax(min(240px, 100%), 1fr))` → evita desbordes en pantras muy estrechas (el `min()` protege el mínimo).

!!! warning "Error común"

    Cálculo mal hecho: ==`auto-fit`== obedece a **`min·n + gap·(n − 1) ≤ ancho`**. Si te saltas los `gap` (o el `min()`) aparecen **columnas fantasma** o desbordes.

!!! question "¿Cuántas columnas caben?"

    Con `grid-template-columns: repeat(auto-fit, minmax(200px, 1fr))` y `gap: 20px`, ¿cuántas columnas se crean en un contenedor de 1000 px?

    ??? success "Respuesta"

        `200·n + 20·(n − 1) ≤ 1000` → `220·n ≤ 1020` → **n = 4**. El sobrante lo reparte `1fr`.

## 7. Subgrid

Permite a un item **heredar la definición de pistas** de la cuadrícula padre, alineando internamente con la retícula global:

```css title="tarjetas-con-subgrid.css"
.tarjetas {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}
.tarjeta {
  display: grid;
  grid-template-rows: subgrid;   /* hereda filas del padre */
  grid-row: span 3;              /* ocupa 3 filas del padre */
}
.tarjeta img    { grid-row: 1; }
.tarjeta h3     { grid-row: 2; }
.tarjeta p      { grid-row: 3; }
```

Resultado: títulos de todas las tarjetas quedan alineados aunque el texto varíe (imposible sin subgrid sin hacks de altura fija). Soporte: Chrome 117+, Firefox 71+, Safari 16+.


> **Claves para el examen**: definir qué problema resuelve ==subgrid== (alineación de subcomponentes sobre la retícula padre) y que requiere que el item sea también grid container con `subgrid` en el eje heredado.

## 8. Superposición y densidad

- Dos items en la misma celda **se superponen** (a diferencia de tablas). Controla el orden con `z-index`/DOM.
- `grid-auto-flow: dense` + items de varios tamaños = mosaico tipo masonry «aproximado» (no es masonry real, que depende de alturas desconocidas).

## 9. Patrones completos

### 9.1. Dashboard

```css title="dashboard.css"
.dash {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-auto-rows: minmax(100px, auto);
  gap: 1rem;
}
.kpi   { grid-column: span 3; }
.grafica-grande { grid-column: span 8; grid-row: span 2; }
.tabla { grid-column: span 12; }
```

### 9.2. Holy grail moderno

```css title="holy-grail-grid.css"
body {
  display: grid;
  grid-template-rows: auto 1fr auto;
  grid-template-areas: "header" "main" "footer";
  min-height: 100dvh; /* (1)! */
}
header { grid-area: header; }
main   { grid-area: main; display: grid; grid-template-columns: 220px 1fr; }
footer { grid-area: footer; }
```

1.  Sin `min-height` la fila central se colapsa al tamaño del contenido y la página deja de ocupar la ventana.

### 9.3. Formulario label+input en dos columnas

```css
.form {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: .75rem 1rem;
  align-items: center;
}
.form .full { grid-column: 1 / -1; }
```

### 9.4. Centrado absoluto

```css
.stage { display: grid; place-items: center; min-height: 100dvh; }
```

### 9.5. Columna pegada (sticky) dentro de grid

```css
.layout { display: grid; grid-template-columns: 1fr 320px; }
.sidebar > .inner { position: sticky; top: 1rem; }
```

!!! example "Página completa con tres áreas"

    ```css
    .pagina { display: grid; grid-template-areas: "cabecera cabecera" "nav main" "pie pie"; min-height: 100dvh; }
    ```

    Reordenas la página entera cambiando solo la **imagen de texto** (sección 4.3).

## 10. Grid vs Flexbox (decisión)

| Situación | Elección |
|---|---|
| Navbar, toolbar, grupo de botones | Flex |
| Página completa, secciones grandes | Grid |
| Galería que envuelve | Grid (`auto-fit`) o Flex (`wrap`); Grid da control de filas |
| Alinear interior de un componente | Flex |
| Hacer coincidir alturas de tarjetas con contenido variable | Grid (filas) o subgrid |
| «Solo quiero centrar una cosa» | `display: grid; place-items: center` (o flex) |

No son rivales: lo normal es **grid fuera, flex dentro**. El mismo bloque de dos columnas:

=== "Grid"

    ```css title="dos-columnas-grid.css"
    .layout { display: grid; grid-template-columns: 1fr 320px; gap: 1rem; }
    ```

=== "Flexbox"

    ```css title="dos-columnas-flex.css"
    .layout { display: flex; gap: 1rem; }
    ```


## 11. Errores comunes

| Error | Síntoma | Solución |
|---|---|---|
| Esperar que `fr` ignore el contenido | Pista más ancha de lo esperado | `minmax(0, 1fr)` para permitir compresión total. |
| `auto-fit` vs `auto-fill` confundidos | Columnas fantasma o estiramiento inesperado | Recordar: fill reserva, fit colapsa. |
| Items que no son hijos directos | No entran en la grid | Grid solo ve hijos directos (envuelve o usa subgrid). |
| `height: 100%` en item de fila `auto` | No crece | Usar `align-self: stretch` (default) o filas definidas. |
| Olvidar `gap` y usar márgenes | Doble espaciado en bordes | Siempre `gap` en containers modernos. |
| `dense` sin pensar | Orden visual ≠ orden DOM (lectores de pantalla) | Documentar o evitar. |

!!! success "Checklist antes de dar la grid por buena"

    - [ ] Las pistas que me importan están en **explícita** (`grid-template-*`); lo demás es implícita.
    - [ ] El contenido largo no infla las pistas: uso **`minmax(0, 1fr)`** donde hace falta.
    - [ ] El spacing sale de **`gap`**, no de márgenes entre items.

## 12. Autoevaluación rápida

1. ¿Cuántas columnas crea `repeat(auto-fit, minmax(200px, 1fr))` en un contenedor de 1000px con `gap: 20px`? (Pista: 200n + 20(n−1) ≤ 1000.)
2. Diferencia entre `grid-column: 2 / 4` y `grid-column: 2 / span 2`.
3. ¿Por qué `minmax(0, 1fr)` arregla el desborde de contenido largo?
4. Explica subgrid con un ejemplo de tarjetas alineadas.
5. ¿Cuándo preferirías `auto-flow: dense` y qué coste de accesibilidad tiene?

!!! tip "Claves para el examen"

    - Grid es **2D y layout-first**: defines pistas primero y colocas después; flex es 1D y contenido-first.
    - `fr` reparte **lo que sobra** tras restar fijos y `gap`; para que no se infla con el contenido → `minmax(0, 1fr)`.
    - Colocar: `grid-column: 1 / -1` ocupa **todo el ancho**, `span n` avanza `n` pistas y las líneas negativas cuentan desde el final; ==grid-template-areas== hace el responsive **cambiando solo el mapa**.
    - ==`auto-fit`== **colapsa** columnas vacías y `auto-fill` las **reserva** (`min·n + gap·(n−1) ≤ ancho`); subgrid **hereda las pistas** del padre.
    - Regla de convivencia: **grid fuera, flex dentro**; `place-items: center` centra cualquier cosa.

*[DOM]: Document Object Model, el árbol de elementos del documento
*[masonry]: patrón de mosaico con alturas variables (del inglés *masonry*, albañilería)
