---
title: "Unidad 01 — Fundamentos de CSS"
description: "Historia del lenguaje, sintaxis, formas de incluir estilos, cascada, especificidad, herencia e importancia. Base sobre la que se construye todo el resto de los apuntes."
modulo: "LMH (0373) / DIW (0615)"
unidad: 1
fecha: "2026-09-06"
---

# Unidad 01 · Fundamentos de CSS

## 1. ¿Qué es CSS y por qué existe?

**CSS (Cascading Style Sheets)** es un lenguaje de hojas de estilo que describe **cómo se presenta** un documento estructurado (HTML, XML/SVG…). Su función es separar la **presentación** de la **estructura**:

```text
HTML  → estructura y semántica (QUÉ hay en la página)
CSS   → presentación (CÓMO se ve)
JS    → comportamiento (CÓMO actúa)
```

### Ventajas de usar hojas de estilo (CE 2.g del módulo 0373)

| Ventaja | Explicación |
|---|---|
| **Separación de preocupaciones** | El contenido vive en HTML; el aspecto en CSS. Cambiar el diseño no toca el contenido. |
| **Mantenibilidad** | Un cambio en una regla afecta a todos los elementos seleccionados. Sin CSS habría que editar cada etiqueta. |
| **Consistencia** | Una clase `.boton` garantiza el mismo aspecto en toda la aplicación (RA 2 del 0615: «interfaces homogéneas»). |
| **Menor peso de transferencia** | Un único archivo CSS se descarga y cachea una vez; el HTML queda más ligero. |
| **Accesibilidad** | Permite adaptar el diseño a las necesidades del usuario (tamaño de texto, contraste, movimiento reducido) sin tocar el contenido. |
| **Impresión y otros medios** | Con `@media` el mismo documento puede verse bien en pantalla, imprimirse o leerse. |
| **Reutilización** | La misma hoja sirve a varios documentos; varias hojas pueden combinarse. |

> **Error común**: usar atributos presentacionales obsoletos (`<font>`, `<center>`, `align="..."`) o estilos en línea para todo. El currículo (RA 2, CE b–c) distingue explícitamente *estilos directos* de *hojas externas*: los directos son la excepción (personalización puntual, email marketing), no la norma.

## 2. Breve historia (contexto suficiente para examen)

| Año | Hito |
|---|---|
| 1994 | Hakon Wim Lie propone «Style Sheets» como alternativa a las etiquetas presentacionales de HTML. |
| 1996 | **CSS1** (W3C Recommendation). Browsers: solo parcial. |
| 1998 | **CSS2**. Aparecen posicionamiento absoluto/fijo, floats, media types. |
| 2003–2010 | Era de las «workarounds»: hacks de IE, DHTML, table layouts. Nace el movimiento del *web standards* (W3C, WHATWG). |
| 2011 | **CSS2.1** REC (consolidación). Empieza la **modularización de CSS3**. |
| 2009–2015 | Llegan Flexbox, Grid, variables custom, transformaciones 3D, animaciones. |
| 2018–hoy | CSS moderno: `:has()`, subgrid, container queries, nesting nativo, `@layer`, scroll-driven animations… |

> **Claves para el examen**: CSS nació para **liberar a HTML de la maquetación**. La modularización (módulos con niveles L1/L2/…) sustituyó al mito de «CSS3 vs CSS4».

## 3. Sintaxis

### 3.1. Anatomía de una regla

```css
selector {
  propiedad: valor;
  otra-propiedad: valor2 !important;
}
```

- **Selector**: qué elementos se ven afectados (unidad 02 completa).
- **Bloque de declaraciones**: entre llaves `{ }`.
- **Declaración**: par `propiedad: valor` terminado por **punto y coma** `;`.
- **Comentario**: `/* así */` (no existe comentario de línea).
- **At-rule**: reglas que empiezan por `@` (`@media`, `@import`, `@keyframes`, `@font-face`, `@layer`…). Tienen dos formas:
  - *con bloque* (`@media (min-width: 600px) { … }`)
  - *con prefijo/sufijo* (`@import url("otro.css");`)

### 3.2. Errores de sintaxis y su efecto

| Error | Consecuencia |
|---|---|
| Falta `;` entre declaraciones | Se ignora el **resto del bloque** hasta el siguiente `;` válido o el `}`. |
| Propiedad desconocida | Se ignora esa declaración (el navegador descarta lo que no entiende). |
| Valor inválido | Se ignora la declaración. |
| Falta `{` o `}` | Puede invalidar varias reglas siguientes. |

El navegador aplica un principio de **tolerancia**: ignora lo que no entiende y sigue procesando. Es la base de la *progressive enhancement* (mejora progresiva): escribe CSS estándar y añade mejoras que los navegadores nuevos aplicarán.

### 3.3. At-rules frecuentes (mapa general)

| At-rule | Función | Unidad donde se profundiza |
|---|---|---|
| `@import` | Importar otra hoja | 01.5 |
| `@media` | Estilos condicionales por características del dispositivo | 10 |
| `@supports` | Estilos condicionales por soporte de propiedades | 12 |
| `@font-face` | Definir fuentes personalizadas | 08 |
| `@keyframes` | Definir animaciones | 11 |
| `@layer` | Capas de la cascada | 12 |
| `@property` | Registrar propiedades personalizadas tipadas | 12 |
| `@container` | Consultas de contenedor | 10 |
| `@scope` | Alcance limitado de reglas | 12 |
| `@page` | Márgenes y formato de impresión | 14 |
| `@charset` | Codificación de caracteres (debe ir en la primera línea) | 01 |
| `@namespace` | Espacios de nombres XML (raro en web práctica) | — |

## 4. Formas de incluir CSS

### 4.1. Estilo en línea (atributo `style`)

```html
<p style="color: crimson; font-size: 1.2rem;">Personalizado</p>
```

- **Máxima especificidad** (sin `!important` externo).
- No se puede cachear ni reutilizar; duplica código.
- Usos legítimos: personalización dinámica desde JS, plantillas con valores únicos, emails.
- El RA 2 del 0615 lo llama «definir estilos de forma directa»: se evalúa saber **cuándo NO** usarlo.

### 4.2. Hoja interna (elemento `<style>`)

```html
<head>
  <style>
    .nota { background: #fff8dc; padding: 0.5rem; }
  </style>
</head>
```

- Válido en `<head>` y también dentro de `<body>` (HTML5 lo permite para estilos locales de una sección o componente); en producción, preferir hoja externa.
- Útil para componentes autocontenidos, prototipos, islands. En producción, preferir externa.

### 4.3. Hoja externa (elemento `<link>`) — la norma

```html
<head>
  <link rel="stylesheet" href="/css/base.css">
  <link rel="stylesheet" href="/css/layout.css">
  <link rel="stylesheet" href="/css/components.css">
</head>
```

- **Cacheable**: el navegador la guarda y no vuelve a descargarla.
- Separación total de contenidos.
- Orden de aparición importa para la cascada (igual especificidad → gana la última).
- Atributos útiles:
  - `media="print"` / `media="screen and (min-width: 768px)"`: aplica solo si la consulta es cierta (evita transferir CSS innecesario).
  - `disabled="true"`: hoja desactivada (base técnica de las **hojas alternativas**, ver 4.5).
  - `rel="preload" as="style"` + intercambio: patrón anti render-blocking (unidad 14).

### 4.4. `@import`

```css
/* main.css */
@import url("reset.css");
@import url("layout.css") screen;
```

- Solo puede aparecer **al inicio** de la hoja (antes de cualquier regla, salvo `@charset`/`@layer` statement).
- Cada `@import` genera una **petición adicional** (cascada de peticiones → peor rendimiento). Preferir varios `<link>`.
- Acepta condición `media` tras la URL.

### 4.5. Hojas de estilo alternativas (CE d del RA 2, módulo 0615)

Tres mecanismos históricos/prácticos:

1. **Atributo `disabled` en `<link>`**: el autor o el usuario (menú de hojas alternativas) activa/desactiva hojas completas.
2. **`media` + JS**: cambiar el valor de `media` permite alternar variantes (p. ej., tema denso vs. cómodo).
3. **Convención moderna**: en lugar de «hojas alternativas» propiamente dichas, hoy se implementan **temas** mediante custom properties + `data-theme` o `prefers-color-scheme` (unidad 12). Es la evolución natural que espera el mercado laboral.

```html
<!-- Variante clásica -->
<link id="tema-a" rel="stylesheet" href="tema-clasico.css">
<link id="tema-b" rel="alternate stylesheet" title="Tema alto contraste"
      href="tema-contraste.css" disabled>
<script>
  // Alternar: document.getElementById('tema-b').disabled = false;
</script>
```

## 5. La cascada

Cuando varias declaraciones aplican a la misma propiedad de un mismo elemento, el navegador resuelve el conflicto en **tres fases** (Cascade L5/L6):

### Fase 1 — Origen e importancia

Orden de prioridad (de menor a mayor):

1. **Estilos del agente de usuario** (user-agent): defaults del navegador (p. ej., `h1` grande y negrita).
2. **Estilos del autor normales** (tu CSS).
3. **Estilos del usuario normales** (personalizaciones del visitante, p. ej., extensiones de lectura).
4. **Estilos del autor con `!important`**.
5. **Estilos del usuario con `!important`** (los más fuertes).

Regla mnemotécnica: `!important` del autor > normal del usuario > normal del autor > user-agent. Y `!important` del usuario lo aplasta todo.

### Fase 2 — Capas (`@layer`)

Las reglas dentro de `@layer` tienen **menor prioridad** que las no capadas, y entre capas gana la **última declarada**. Se estudia a fondo en la unidad 12.

### Fase 3 — Especificidad y orden

Gana la declaración con mayor especificidad; a igual especificidad, **la última en aparecer** en el código fuente.

## 6. Especificidad

### 6.1. Cálculo clásico (modelo numérico)

Se asigna una puntuación `(A, B, C, I)`:

| Componente | Cuenta |
|---|---|
| **I** | Declaración en línea (`style=""`) |
| **A** | Selectores ID (`#id`) |
| **B** | Clases (`.clase`), pseudo-clases (`:hover`) y selectores de atributo (`[href]`) |
| **C** | Tipos/etiquetas (`div`, `h1`) y pseudo-elementos (`::before`) |

Se comparan componente a componente, de izquierda a derecha: **nunca hay llevada** (100 tipos no superan a 1 ID).

### 6.2. Ejemplos trabajados

| Selector | (A,B,C) | Comentario |
|---|---|---|
| `h1` | (0,0,1) | tipo |
| `.titulo` | (0,1,0) | clase |
| `#cabecera h1` | (1,0,1) | 1 ID (`#cabecera`) + 1 tipo (`h1`) |
| `nav ul li a:hover` | (0,1,4) | 1 pseudo-clase + 4 tipos |
| `.card .card__titulo` | (0,2,0) | dos clases |
| `#app .card :is(h2, h3)` | (1,1,0) | `:is()` toma la especificidad de su argumento de mayor peso |
| `:where(.a, .b) p` | (0,0,1) | `:where()` siempre aporta **cero** |
| `article:has(> figure) h2` | (0,0,3) | `:has()` adopta la especificidad de su argumento |

> **Claves para el examen**: saber calcular la especificidad de selectores compuestos y explicar por qué `:where()` existe (aportar cero especificidad para facilitar overrides) y cómo funciona `:is()` (adopta la del argumento más específico).

### 6.3. `!important`

- Invierte la cascada: salta a la capa de importancia superior.
- **No** supera a un `!important` del usuario.
- Mal uso habitual: «para que me haga caso». Genera deuda técnica: cada override posterior necesita otro `!important`.
- Usos razonables: anular estilos de librerías de terceros que no se pueden tocar, forzar accesibilidad (p. ej., mostrar foco), emergencia en producción.

> **Error común**: pensar que `!important` «gana siempre». Pierde ante un `!important` de hoja de usuario y, dentro del mismo origen, sigue sometiéndose a especificidad y orden.

## 7. Herencia

### 7.1. Qué se hereda

Solo algunas propiedades son **heredables** (las de tipografía y texto en general): `color`, `font-*`, `line-height`, `letter-spacing`, `text-align`, `visibility`, `cursor`…

**No heredables** (típicas de caja/borde/fondo): `margin`, `padding`, `border`, `background`, `width`, `height`, `position`, `display`…

La lista completa y oficial está en MDN («Inherited» en cada referencia de propiedad).

### 7.2. Palabras clave de herencia

| Keyword | Efecto |
|---|---|
| `initial` | Restablece la propiedad a su valor inicial definido en la spec (rompe la herencia). |
| `inherit` | Fuerza a tomar el valor del padre (útil en propiedades no heredables). |
| `unset` | Equivale a `inherit` si la propiedad es heredable, o a `initial` si no lo es. |
| `revert` | Descarta tu declaración y vuelve al valor anterior en la cascada (del usuario o user-agent). |
| `revert-layer` | Como `revert`, pero solo hasta la capa anterior (con `@layer`). |

### 7.3. Reset y normalize

- **Reset** (p. ej., *modern-normalize*, *sanitize*): anula defaults del navegador para partir de cero.
- **Normalize**: conserva los defaults razonables y corrige solo inconsistencias entre navegadores.
- Hoy, con `@layer` y `all: initial/unset`, se pueden hacer resets quirúrgicos:

```css
@layer reset {
  *, *::before, *::after { box-sizing: border-box; }
  body, h1, h2, p, figure { margin: 0; }
  img, video { max-width: 100%; display: block; }
}
```

> **Claves para el examen**: diferenciar `initial` vs `inherit` vs `unset` es pregunta clásica.

## 8. Valores universales y unidades básicas

Todo valor dimensional puede ser:

- **Número puro** (solo en propiedades adimensionales: `z-index`, `opacity`, `flex-grow`…).
- **Longitud**: `px`, `rem`, `em`, `%`, `vw/vh`, `ch`, `ex`… (unidad 08 completa).
- **Keyword** propio de cada propiedad.
- **Función**: `calc()`, `clamp()`, `var()`, `url()`, `rgb()`…

Reglas generales:

- Los valores son **case-insensitive** para keywords y funciones; los URLs y `font-family` pueden serlo según contexto.
- `calc()` permite aritmética mixta: `width: calc(100% - 2rem);`.
- `var(--mi-var, fallback)` introduce las **custom properties** (unidad 12).

## 9. Validación y depuración (CE h del RA 2)

### 9.1. Validador W3C (Jigsaw)

- <https://jigsaw.w3.org/css-validator/> : comprueba sintaxis y propiedades contra las specs.
- Limitaciones: valida CSS plano; no entiende preprocesadores (compila antes) ni todas las features muy recientes.
- En la práctica profesional se complementa con **linters**: `stylelint` (reglas configurables, integración CI).

### 9.2. DevTools del navegador

- **Panel Elements/Inspector**: estilos aplicados por selector, tachados (perdidos en la cascada), especificidad calculada.
- **Computed**: valor final resuelto.
- **Styles → View transition timeline / Layers**: inspeccionar capas de composición.
- **Rendering**: forzar repaints, mostrar layout shifts, emular `prefers-reduced-motion`.
- **Performance**: identificar problemas de layout/paint (unidad 14).

> **Claves para el examen**: el criterio «se han utilizado herramientas de validación de hojas de estilos» se cubre citando Jigsaw + stylelint + DevTools, y sabiendo qué detecta cada uno.

## 10. Resumen de la unidad

1. CSS separa **presentación** de estructura: mantenibilidad, consistencia, accesibilidad, rendimiento.
2. Sintaxis: `selector { prop: valor; }`; at-rules con `@`; el navegador **ignora** lo que no entiende (tolerancia → mejora progresiva).
3. Inclusión: en línea (excepción), `<style>` (componentes), **`<link>` externo (norma)**, `@import` (evitar por rendimiento).
4. Cascada: **origen/importancia → capas → especificidad → orden**.
5. Especificidad: `(ID, clase/pseudo-clase/atributo, tipo/pseudo-elemento)`; `:where()` = 0; `:is()` = máximo de sus argumentos; en línea y `!important` fuera de escala.
6. Herencia: solo propiedades de texto/tipo; keywords `initial/inherit/unset/revert`.
7. Valida con Jigsaw/stylelint y depura con DevTools.

## 11. Autoevaluación rápida

1. ¿Por qué `@import` es peor que varios `<link>`?
2. Calcula la especificidad de `#main article .post:not(.borrador):hover h2::first-line`.
3. ¿Qué gana: `.a { color: red }` (hoja 1) frente a `p.a { color: blue }` (hoja 2)? ¿Y si la segunda lleva `!important`?
4. ¿`initial` o `inherit` para reiniciar `margin` en un `div` dentro de otro `div` con `margin: 2rem`?
5. ¿Qué es una «hoja de estilo alternativa» y cómo se implementa hoy?
