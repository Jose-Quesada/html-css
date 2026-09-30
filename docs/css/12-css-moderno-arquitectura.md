---
icon: lucide/blocks
title: "Unidad 12 — CSS moderno y arquitectura"
description: "Custom properties, @property, anidación nativa, @layer, @supports, @scope, propiedades lógicas e i18n, patrones de arquitectura (BEM, ITCSS), preprocesadores, PostCSS y design tokens."
modulo: "LMH (0373) / DIW (0615)"
unidad: 12
fecha: "2026-09-06"
---

# Unidad 12 · CSS moderno y arquitectura

Esta unidad reúne las características estructurales del CSS actual (variables, capas, anidación, alcance) y los patrones de organización de código que se esperan en el mercado (RA 1 «guía de estilo» y RA 2 «interfaces homogéneos»).

!!! note "Conocimientos previos"

    - Cascada, especificidad y herencia (unidades 01–02).
    - Selectores y pseudo-clases (unidad 02).
    - Nombres de clase consistentes y guía de estilo (RA 1).

## PARTE A · CARACTERÍSTICAS ESTRUCTURALES MODERNAS

### 1. Custom properties (variables CSS)

Las ==custom properties== son la **única variable nativa** de CSS: se declaran con `--nombre` y se consumen con `var(--nombre)`.

```css title="tokens.css"
:root {
  --color-marca: oklch(60% 0.2 260);
  --espacio-base: 1rem;
  --radio: .5rem;
}
.boton {
  background: var(--color-marca);
  padding: calc(var(--espacio-base) * .75);
  border-radius: var(--radio);
  color: var(--texto, #111);   /* fallback si no existe */
}
```

Reglas que hay que dominar:

- **Se heredan** como cualquier propiedad heredable: definidas en `:root` alcanzan todo; redefinibles por subárbol (componente, tema).
- **Scope dinámico**: su valor se resuelve donde se **usa**, no donde se define → permiten theming local sin cascada extra.
- No validan su valor al declararse (cualquier token es válido); la validación ocurre al usarlas → un typo en `var()` invalida la declaración completa (por eso el **fallback**).
- Accesibles desde JS: `getComputedStyle(el).getPropertyValue('--x')`, `el.style.setProperty('--x', v)`.
- **No** son responsive por sí solas: combínalas con `@media`/`@container` o `clamp()`.

Patrones típicos:

```css title="patrones.css"
/* Tema por atributo */
:root[data-tema="oscuro"] {
  --bg: #111; --texto: #eee;
}
/* Escala derivada */
:root {
  --s-1: .25rem; --s-2: .5rem; --s-3: 1rem; --s-4: 2rem;
}
/* Estado interactivo */
.boton:hover { --elevacion: 2; }
```

!!! example "Theming local en dos líneas"

    ```css title="tema.css"
    .tarjeta       { --bg: #ffffff; background: var(--bg); }
    .modo-oscuro .tarjeta { --bg: #111111; }
    ```

    El componente **no sabe** nada del tema: consume su variable, redefinida por el ancestro.

### 2. `@property`: variables tipadas y animables

Con ==`@property`== el navegador **conoce el tipo** de la variable: eso habilita la **animación**.

```css title="propiedad.css" hl_lines="8"
@property --angulo {
  syntax: "<angle>";             /* (1)! */
  inherits: false;
  initial-value: 0deg;
}
.giro {
  transform: rotate(var(--angulo));
  transition: --angulo 1s;   /* ¡ahora transiciona! */
}
.giro:hover { --angulo: 180deg; }
```

1.  **`<angle>`** es el contrato: `transition` y `transform` ya saben qué tratan.

- Registra la variable con **tipo** (`<color>`, `<length>`, `<number>`, `<angle>`…), herencia y valor inicial.
- Permite **transicionar/animar custom properties** (antes solo saltaban) y usarlas en contextos que exigen tipo concreto (p. ej., `background: var(--grad)` donde `--grad` es `<image>`).
- Soporte: Chrome 85+, Safari 16.4+, Firefox 128+.

### 3. Anidación nativa (Nesting L1)

```css title="anidacion.css" hl_lines="4 11"
.tarjeta {
  padding: 1rem;

  &:hover { box-shadow: 0 8px 24px rgb(0 0 0 / .15); }   /* (1)! */

  &__titulo {
    font-size: 1.25rem;
    margin-block-end: .5rem;
  }

  & > ul { list-style: none; }

  @media (min-width: 40em) {
    display: grid;
    grid-template-columns: auto 1fr;
  }
}
```

1.  `&` se sustituye por el selector padre: `&:hover` → `.tarjeta:hover`.

Reglas:

- `&` = selector padre (puede ir en cualquier posición compuesta: `&__x`, `&:hover`, `.otro &`).
- Solo se permite anidar **reglas de estilo** y at-rules condicionales (`@media`, `@supports`, `@container`) dentro de reglas; NO anidar selectores a secuelas fuera de regla.
- El selector resultante es el padre + combinador implícito descendiente salvo que uses `>`/`+`/`~`.
- Limitaciones frente a Sass: sin mixins, sin bucles, sin operaciones complejas (eso sigue siendo terreno de preprocesadores/PostCSS).
- Soporte: Chrome 120+, Firefox 117+, Safari 17.2+.

> **Claves para el examen**: diferenciar anidación nativa (limitada, estándar) de Sass (lenguaje completo). Y saber que `&` no existe en CSS plano histórico.

### 4. `@layer`: ordenar la cascada arquitectónicamente

Problema que resuelve: controlar **qué gana** sin depender del orden físico de archivos ni de `!important`; con ==@layer== ese orden lo decides tú.

```css title="capas.css" hl_lines="2 4"
/* Declarar capas (orden de prioridad creciente) */
@layer reset, tokens, base, components, utilities;   /* (1)! */

@layer reset {
  *, *::before, *::after { box-sizing: border-box; margin: 0; }
}
@layer base {
  body { line-height: 1.6; }
}
@layer components {
  .boton { padding: .5rem 1rem; }
}
@layer utilities {
  .mt-4 { margin-top: 1rem; }   /* (2)! */
}
```

1.  La declaración fija el **orden de prioridad** de todas las capas; lo que no aparece aquí se añade al final.
2.  Última capa declarada = **mayor prioridad**: `utilities` pisa a `components`.

Reglas:

- Capas **declaradas** tienen MENOR prioridad que el CSS **no capado** (el no capado gana siempre).
- Entre capas: gana la **última** declarada (_utilities_ pisa a _components_, etc.).
- Capas **anidadas**: `@layer base.typography { … }` → ruta `base.typography`; el orden lo define la primera mención de cada segmento.
- Añadir capas después: `@layer newlayer { }` sin declarar antes → se añade al final (máxima prioridad entre capadas).
- Combinado con ==`revert-layer`== (unidad 01): una utilidad puede «ceder» a la capa anterior.
- Soporte: Chrome 99+, Firefox 97+, Safari 15.4+.

!!! info "Qué gana qué, en orden"

    De **menor a mayor**: estilos de agente → **capas declaradas** → CSS **sin capa** → `!important` (orden invertido, unidad 01).

Arquitectura típica con layers:

```text title="orden-capas.txt"
reset → tokens(base) → elements → components → utilities
        (lo más específico/derecho gana)
```

!!! question "Orden de capas en examen"

    Declara `@layer a, b;` y escribe los bloques al revés: `b` primero, `a` después. ¿Qué regla gana?

    ??? success "Respuesta"

        Gana **`b`**: la prioridad la fija la **primera declaración** (última capa declarada = mayor prioridad), no el orden físico de los bloques. Por eso se declaran todas las capas **al principio**.

### 5. `@supports`: detección de características

```css title="soporte.css"
/* Propiedad */
@supports (display: grid) { .layout { display: grid; } }

/* Valor */
@supports (gap: 1rem) { .flex { gap: 1rem; } }

/* Función */
@supports (background: paint(mifondo)) { … }

/* Negación y lógica */
@supports not (backdrop-filter: blur(4px)) { .vidrio { background: #fff; } }
@supports (selector(:has(*))) or (selector(* => *)) { … }

/* Custom property registrada */
@supports (animation-timeline: scroll()) {
  .progreso { animation-timeline: scroll(root); }
}
```

- Es la herramienta de **mejora progresiva**: escribe el fallback primero y mejora dentro de `@supports`.
- `selector()` permite detectar pseudo-clases nuevas sin romper navegadores viejos (que descartarían toda la regla si vieran `:has()` inválido… en realidad descartarían la regla; `selector()` evita eso).

### 6. `@scope`: alcance limitado (componentes)

==`@scope`== acota las reglas a un **árbol concreto** sin prefijos ni clases extra:

```css title="alcance.css"
.widget {
  /* todo lo de aquí solo aplica DENTRO de .widget */
  :scope h3 { margin: 0; }
  a { color: inherit; }
}
/* equivalente explícito: */
@scope (.widget) {
  h3 { margin: 0; }
  a  { color: inherit; }
}
```

- Evita que estilos «escapen» del componente sin necesidad de prefijarlo todo (reduce la **especificidad inflada**).
- Complemento natural de Web Components y de anidación.
- Soporte: Chrome 118+, Firefox 146+, Safari 26.4+ (reciente; verificar en caniuse[^1] antes de usar en producción).

### 7. Propiedades lógicas e internacionalización

Las propiedades físicas (`margin-left`, `top`…) asumen LTR. Las **lógicas** se basan en el **flujo de escritura** (`direction`, `writing-mode`):

| Física | Lógica | Significado |
|---|---|---|
| `margin-left/right` | `margin-inline-start/end` | Lado de inicio/fin de línea. |
| `margin-top/bottom` | `margin-block-start/end` | Inicio/fin de bloque. |
| `padding-left…` | `padding-inline/block(-start/-end)` | Ídem. |
| `width` / `height` | `inline-size` / `block-size` | Tamaños por eje. |
| `min/max-width` | `min/max-inline-size` | Límites por eje. |
| `left/top/right/bottom` | `inset-inline-start`… / `inset-block-*` | Offsets posicionados. |
| `border-top-left-radius` | `border-start-start-radius` | Esquina inicio-inicio. |
| `float: left` | `float: inline-start` | Flotado lógico. |
| `clear: left` | `clear: inline-start` | Ídem. |

```css title="propiedades-logicas.css"
.caja {
  margin-inline: 1rem;      /* izquierda+derecha según dirección */
  padding-block: 2rem;
  inset-inline-start: 0;
}
html[dir="rtl"] { direction: rtl; }   /* árabe, hebreo, persa… */
```

!!! question "De físico a lógico"

    Traduce a propiedades lógicas: `top: 0; right: 0; width: 10rem; margin-bottom: 1rem; text-align: left;`

    ??? success "Respuesta"

        `inset-block-start: 0;` · `inset-inline-end: 0;` · `inline-size: 10rem;` · `margin-block-end: 1rem;` · `text-align: start;`.

!!! warning "Error común"

    - Llamar a la variable `var(color-marca)` **sin los dos guiones**: no es una custom property y la declaración se invalida **en silencio**.
    - Mezclar mayúsculas: `--ColorMarca` y `--colormarca` son **dos variables distintas**.
    - Esperar el error al definir `--x`: el fallo de `var()` aparece **al usarla**, no donde la declaras.

> **Claves para el examen**: «¿Por qué usar propiedades lógicas?» → un solo código sirve para LTR y RTL (y vertical CJK) sin duplicar reglas. Pregunta típica: traducir `margin: 1rem 2rem; text-align: left` a lógicas.

## PARTE B · ARQUITECTURA DE CSS

### 8. Por qué importa la arquitectura

En proyectos reales (decenas de componentes, varios desarrolladores) el CSS sin estructura genera: **especificidades impredecibles**, **código duplicado**, imposible borrar lo muerto. La ==guía de estilo== (RA 1) es el documento vivo que fija: tokens, nomenclatura, espaciado, tipografía, componentes y convenciones.

### 9. Patrones de nomenclatura

#### BEM (Block Element Modifier) — el más enseñado

```text title="bem.txt"
bloque __elemento --modificador
.tarjeta
.tarjeta__titulo
.tarjeta__titulo--destacado
.tarjeta--compacta
```

- Bloque: entidad autónoma. Elemento: parte del bloque (nunca anida más de un nivel semántico). Modificador: variante/estado.
- Ventajas: predecible, sin dependencias de contexto, fácil de buscar/borrar.
- Coste: nombres largos; con anidación nativa y `@scope` muchas equipos relajan ==BEM== puro.

#### Alternativas habituales

| Patrón | Idea |
|---|---|
| **ITCSS** | Capas invertidas: settings → tools → generic → elements → objects → components → utilities (de menor a mayor especificidad). Se implementa hoy con `@layer`. |
| **SMACSS** | Base / Layout / Module / State / Theme. |
| **Utility-first** (Tailwind, Tachyons) | Clases pequeñas de propósito único; composición en el HTML. Rápido, pero acopla HTML a presentación (mitigado con `@apply`/componentes). |
| **CUBE CSS** | Component, Utility, Block, Extension. |
| **CSS Modules** | Alcance local por archivo (build tool): `.btn` en `Card.css` no choca con `.btn` de otro archivo. |

!!! info "Qué patrón elijo"

    - **Producto largo**: BEM + capas + tokens (lo de aquí arriba).
    - **Prototipo o legacy**: utility-first o ITCSS con `@layer`.

### 10. Design tokens

Los ==design tokens== son **decisiones de diseño nombradas** (colores, espacios, radios, sombras, durations) almacenadas como datos y consumidas por CSS (y otras plataformas):

```json title="tokens.json"
{ "color": { "brand": { "500": { "value": "#2563eb" } } },
  "space": { "3": { "value": "1rem" } } }
```

→ generados a CSS:

```css title="tokens-generados.css"
:root { --color-brand-500: #2563eb; --space-3: 1rem; }
```

Ventajas: **fuente única de verdad**, multiplataforma (web/iOS/Android/Figma), theming trivial. Herramientas: Style Dictionary, Tokens Studio, Theme UI.

### 11. Preprocesadores (contexto profesional)

| Herramienta | Estado | Aporta sobre CSS nativo |
|---|---|---|
| **Sass/SCSS** | Estándar de facto | Variables tipadas, mixins, funciones, bucles, herencia de selectores, módulos. |
| **Less** | Legacy | Similar a Sass (historia de Bootstrap). |
| **Stylus** | Nicho | Sintaxis whitespace. |

Ejemplo SCSS:

```scss title="tarjeta.scss"
$marca: oklch(60% 0.2 260);
@mixin tarjeta($pad: 1rem) {
  padding: $pad;
  border-radius: .5rem;
  box-shadow: 0 1px 3px rgb(0 0 0 / .1);
}
.tarjeta { @include tarjeta; }
@for $i from 1 through 4 {
  .mt-#{$i} { margin-top: #{($i * 0.25)}rem; }
}
```

Tendencia 2024+: **mucho de lo que hacía Sass ya es nativo** (variables, anidación, `@layer`); los preprocesadores siguen vivos por mixins/bucles/ecosistema, y herramientas como **Lightning CSS** (Rust) hacen transform+minify rapidísimo.

### 12. PostCSS y pipeline moderno

PostCSS = procesador basado en AST con plugins:

- `autoprefixer` (prefijos según caniuse), `cssnano` (minificar), `postcss-preset-env` (habilitar sintaxis futura), `postcss-import`, `postcss-nesting` (polyfill de anidación para navegadores viejos)…

Pipeline típico hoy:

```text title="pipeline.txt"
fuentes CSS/SCSS → (Vite/esbuild/Lightning CSS) → CSS final minificado
                  └─ HMR en dev, fingerprinting en build
```

Con **Vite** (o esbuild) no necesitas configurar nada: importas CSS en JS, hace bundling, minificado y asset hashing automáticamente.

### 13. Estructura de archivos recomendada (pequeño/medio proyecto)

=== "Árbol de carpetas"

    ```text title="estructura.txt"
    /styles
      ├─ tokens.css          /* custom properties: color, space, type, radius */
      ├─ reset.css           /* normalización mínima */
      ├─ base.css            /* elementos globales, tipografía, foco */
      ├─ layout.css          /* contenedores, grid de página */
      ├─ components/         /* un archivo por componente */
      │    ├─ boton.css
      │    ├─ tarjeta.css
      │    └─ nav.css
      └─ utilities.css       /* clases de escape (mínimas) */
    ```

=== "Capas con `@import`"

    Con `@layer`:

    ```css title="index.css"
    @import "tokens.css" layer(tokens);
    @import "reset.css" layer(reset);
    @import "base.css" layer(base);
    @import "layout.css" layer(layout);
    @import "components/boton.css" layer(components);
    @import "utilities.css" layer(utilities);
    ```

(`@import url() layer(nombre)` combina ambas características.)

### 14. Documentación y guía de estilo

Una guía de estilo mínima debe documentar:

1. **Tokens**: paleta con usos permitidos (texto sobre fondo X), escala de espaciado, tipografías y tamaños, radios/sombras/elevaciones.
2. **Componentes**: cuándo usar cada uno, variantes, estados (hover/focus/disabled/error), ejemplos HTML+CSS.
3. **Convenciones**: nomenclatura, estructura de carpetas, cómo añadir un componente nuevo.
4. **Accesibilidad**: contraste verificado, foco visible, movimiento reducido.
5. **Responsive**: breakpoints y comportamientos por breakpoint.

Herramientas: Storybook (con addons CSS), Zeroheight, o simplemente Markdown + demos en vivo (como estos apuntes).

## 15. Errores comunes de arquitectura

| Error | Consecuencia | Solución |
|---|---|---|
| Sin capas ni orden | Guerras de especificidad | `@layer` + convención de archivos. |
| Utilidades para todo | HTML ilegible, acoplamiento | Utilidades mínimas; componentes para lo repetido. |
| Variables sin sistema | 40 azules distintos | Tokens con escala y nombres semánticos. |
| Prefijos físicos en producto i18n | Roto en RTL | Propiedades lógicas. |
| Copiar CSS de librería sin entender | Dependencias ocultas | Leer, adaptar, documentar. |

!!! success "Checklist de arquitectura"

    - [ ] Capas **declaradas una sola vez** y al principio del proyecto.
    - [ ] Variables con `--` y **nombres semánticos** (no `--azul1`).
    - [ ] Nomenclatura única (**BEM** o convención equivalente).
    - [ ] Valores repetidos 3+ veces → **token**.
    - [ ] Propiedades **lógicas** si hay RTL; guía de estilo al día.

## 16. Autoevaluación rápida

1. ¿Por qué `var(--x, fallback)` es importante? ¿Qué pasa si `--x` existe pero su valor es inválido para la propiedad?
2. Explica el orden de prioridad entre: CSS no capado, `@layer utilities`, `@layer base`, y `!important` dentro de `base`.
3. Traduce a propiedades lógicas: `position:absolute; top:0; right:0; width:10rem; margin-bottom:1rem`.
4. ¿Qué problema de theming resuelve `@property` con `syntax: "<color>"`?
5. Compara BEM vs utility-first: dos ventajas y dos inconvenientes de cada uno.
6. ¿Cuándo seguirías usando Sass aunque exista CSS nativo?

!!! tip "Claves para el examen"

    - ==custom properties==: se heredan y se resuelven **donde se usan**.
    - `var()` falla **al usarla**; por eso existe el **fallback**.
    - **`@property`** da tipo e inicial → variables **animables**.
    - **`@layer`**: orden declarado al principio; gana la **última** y el CSS **no capado**.
    - Anidación nativa = reglas y at-rules condicionales; mixins/bucles → Sass.
    - **Propiedades lógicas** → un código para LTR, RTL y escritura vertical.
    - **Tokens + guía de estilo** = fuente única de verdad (RA 1).

[^1]: Soporte navegador comprobado en <https://caniuse.com>; el porcentaje cambia en cada versión.

*[RA]: Resultado de aprendizaje
*[BEM]: Block Element Modifier
*[ITCSS]: Inverted Triangle CSS
