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

---

## 9. Ejemplo práctico: artículo editorial con multicolumna, imagen flotada con BFC y tabla de datos

El siguiente ejemplo demuestra los casos de uso legítimos de los sistemas clásicos y especializados de CSS en la web moderna: flujo de texto periodístico con `columns` y `column-span: all`, una figura flotada con contención limpia mediante `display: flow-root`, y una tabla de datos estadísticos optimizada con `table-layout: fixed`.

```html title="editorial.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CSS Editorial · Maquetación Periodística</title>
  <link rel="stylesheet" href="css/editorial.css">
</head>
<body>
  <article class="publicacion">
    <header class="publicacion__cabecera">
      <span class="categoria">Reportaje Tecnológico</span>
      <h1>La Revolución del Hardware Abierto en Europa</h1>
      <p class="entradilla">
        Universidades y centros de investigación impulsan procesadores con arquitectura RISC-V para garantizar la soberanía digital del continente.
      </p>
    </header>

    <!-- Contenedor con Multi-column Layout -->
    <div class="cuerpo-editorial">
      <p>
        Durante décadas, la industria de los semiconductores ha dependido de licencias propietarias cerradas. Sin embargo, un consorcio de instituciones europeas ha comenzado la fabricación en serie de los primeros chips basados íntegramente en estándares abiertos.
      </p>

      <!-- Bloque con float y BFC -->
      <figure class="figura-flotada">
        <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=400&q=80" 
             alt="Oblea de silicio con microchips grabados"
             width="280" height="200">
        <figcaption>Oblea de silicio en sala limpia.</figcaption>
      </figure>

      <p>
        El diseño colaborativo permite auditar cada línea de código Verilog, verificando que no existan puertas traseras que comprometan la seguridad de infraestructuras críticas como redes eléctricas o centros de cálculo estatales.
      </p>

      <!-- Titular que rompe y cruza todas las columnas -->
      <h2 class="subtitulo-cruzado">Comparativa de Adopción por Países</h2>

      <p>
        Los planes de transición tecnológica contemplan una inversión inicial de más de 3.000 millones de euros distribuidos en los presupuestos comunitarios de la próxima década.
      </p>

      <!-- Tabla de datos con table-layout: fixed -->
      <table class="tabla-estadistica">
        <caption>Inversión pública en microelectrónica abierta (2025-2026)</caption>
        <thead>
          <tr>
            <th scope="col">País</th>
            <th scope="col">Proyectos</th>
            <th scope="col">Presupuesto</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">Alemania</th>
            <td>14</td>
            <td>850 M€</td>
          </tr>
          <tr>
            <th scope="row">España</th>
            <td>9</td>
            <td>420 M€</td>
          </tr>
          <tr>
            <th scope="row">Francia</th>
            <td>12</td>
            <td>710 M€</td>
          </tr>
        </tbody>
      </table>

      <p>
        Los expertos concluyen que, aunque el desafío de manufactura física sigue siendo gigantesco, el impulso de la propiedad intelectual abierta es ya imparable en todo el territorio.
      </p>
    </div>
  </article>
</body>
</html>
```

```css title="css/editorial.css"
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Georgia, Cambria, "Times New Roman", serif;
  background-color: #fafaf9;
  color: #1c1917;
  line-height: 1.7;
  padding: 2.5rem 1rem;
}

.publicacion {
  max-width: 58rem;
  margin-inline: auto;
  background-color: #ffffff;
  padding: 3rem 2.5rem;
  border: 1px solid #e7e5e4;
  box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);
}

.publicacion__cabecera {
  margin-block-end: 2rem;
  border-bottom: 2px solid #1c1917;
  padding-bottom: 1.5rem;
}

.categoria {
  font-family: system-ui, sans-serif;
  text-transform: uppercase;
  font-size: 0.75rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  color: #b91c1c;
}

.publicacion__cabecera h1 {
  font-size: 2.5rem;
  line-height: 1.15;
  margin-block: 0.5rem 1rem;
}

.entradilla {
  font-size: 1.25rem;
  line-height: 1.45;
  color: #44403c;
  font-style: italic;
}

/* 1. Multicolumna fluida con regla separadora */
.cuerpo-editorial {
  /* columns: 2 18rem => genera 2 columnas si caben (mínimo 18rem cada una) */
  columns: 2 18rem;
  column-gap: 2.5rem;
  column-rule: 1px solid #d6d3d1; /* Línea de separación clásica de periódico */
  text-align: justify; /* Justificado editorial */
}

.cuerpo-editorial p {
  margin-block-end: 1.25rem;
}

/* 2. Titular intermedio que cruza todas las columnas */
.subtitulo-cruzado {
  column-span: all; /* Atraviesa todas las columnas de la página */
  font-family: system-ui, sans-serif;
  font-size: 1.5rem;
  margin-block: 2rem 1.5rem;
  padding-block: 0.5rem;
  border-top: 1px solid #e7e5e4;
  border-bottom: 1px solid #e7e5e4;
  text-align: left;
}

/* 3. Imagen flotada con contención BFC */
.figura-flotada {
  float: left; /* Flota la caja a la izquierda permitiendo que el texto la envuelva */
  margin-inline-end: 1.5rem;
  margin-block-end: 1rem;
  max-width: 14rem;
  break-inside: avoid; /* Impide que la figura se fracture entre dos columnas */
}

.figura-flotada img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 0.25rem;
}

.figura-flotada figcaption {
  font-family: system-ui, sans-serif;
  font-size: 0.75rem;
  color: #78716c;
  margin-top: 0.35rem;
}

/* 4. Tabla de datos optimizada */
.tabla-estadistica {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed; /* Rendimiento: el navegador no espera a leer todos los datos */
  margin-block: 1.5rem;
  font-family: system-ui, sans-serif;
  font-size: 0.85rem;
  break-inside: avoid; /* No partir la tabla entre columnas */
}

.tabla-estadistica caption {
  font-weight: 700;
  text-align: left;
  margin-bottom: 0.5rem;
  color: #44403c;
}

.tabla-estadistica th,
.tabla-estadistica td {
  padding: 0.6rem 0.75rem;
  border-bottom: 1px solid #e7e5e4;
  text-align: left;
}

.tabla-estadistica th {
  background-color: #f5f5f4;
  color: #1c1917;
}

.tabla-estadistica td:last-child,
.tabla-estadistica th:last-child {
  text-align: right; /* Alineación numérica a la derecha */
}
```

---

### 9.1 Explicación detallada: ¿Por qué se usa cada propiedad y para qué sirve?

A continuación se detalla la función de las propiedades de maquetación avanzada empleadas en este diseño editorial:

#### 1. Atajo `columns: 2 18rem` y `column-gap`
- **¿Cómo funciona?** Combina `column-count: 2` y `column-width: 18rem`.
- **Comportamiento adaptativo:** En pantallas amplias de escritorio, el texto fluye en dos columnas paralelas. Si la ventana se reduce por debajo de aproximadamente 38 rem (móviles o tablets estrechas), el navegador desactiva la segunda columna y muestra una sola columna fluida, resolviendo la adaptabilidad sin media queries.
- **`column-rule: 1px solid #d6d3d1`:** Dibuja un filete vertical divisorio entre columnas sin ocupar ancho de maquetación ni alterar los márgenes.

#### 2. `column-span: all`
- **¿Para qué sirve?** Hace que el encabezado `.subtitulo-cruzado` cruce transversalmente todas las columnas de la página.
- **Efecto visual:** Interrumpe el flujo multicolumna, divide el texto superior, coloca el título a todo lo ancho de la caja, y reinicia el flujo de dos columnas inmediatamente debajo.

#### 3. `break-inside: avoid` en figuras y tablas
- **El problema de la partición indeseada:** Por defecto, el motor de multicolumna puede cortar un elemento a la mitad para encajar la primera parte al final de la columna 1 y la segunda parte arriba de la columna 2.
- **La solución técnica:** Aplicar `break-inside: avoid` a `<figure>` y `<table>` prohíbe tajantemente la fractura, forzando a que la imagen o la tabla se muestren completas como un bloque indivisible.

#### 4. `float: left` para flujo de texto envolvente
- **¿Cuándo es correcto usar `float` hoy?** Envolver una imagen con párrafos de texto continuo es el **único caso de uso legítimo de `float` en la actualidad**.
- **Por qué no usar flex ni grid para esto:** Ni Flexbox ni Grid permiten que un texto comience a la derecha de una foto y continúe después debajo de ella ocupando todo el ancho. El algoritmo de flotación de CSS es el único capacitado para realizar esta envoltura orgánica.

#### 5. `table-layout: fixed`
- **¿Para qué sirve?** Cambia el algoritmo de cálculo del ancho de las celdas de la tabla.
- **Ventaja de rendimiento:** En el modo estándar (`table-layout: auto`), el navegador debe descargar e inspeccionar **todas y cada una de las celdas de la tabla** para saber cuál contiene el texto más largo antes de decidir el ancho de las columnas. Con `fixed`, el navegador calcula las anchuras inmediatamente leyendo solo la primera fila (`<thead>`), acelerando drásticamente el renderizado inicial de tablas extensas.

---

## 10. Autoevaluación rápida

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
