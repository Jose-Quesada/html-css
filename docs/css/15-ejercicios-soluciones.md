---
icon: lucide/check-check
title: "Unidad 15 — Ejercicios: soluciones"
description: "Soluciones completas, comentadas y explicadas técnicamente para los 100 ejercicios de CSS (Unidades 01 a 10) de la Unidad 15."
modulo: "LMH (0373) / DIW (0615)"
unidad: 15
fecha: "2026-10-09"
---

# Unidad 15 · Ejercicios: soluciones completas (U01 – U10)

Este documento recoge las **soluciones oficiales comentadas** a los [100 ejercicios prácticos de CSS de la Unidad 15](15-ejercicios-glosario-recursos.md). Cada solución proporciona el código fuente completo, el análisis técnico del funcionamiento de la regla y la advertencia de los errores comunes más frecuentes entre el alumnado.

---

## Soluciones: Unidad 01 — Fundamentos de CSS

### Solución U01.01 — Anatomía canónica y vinculación externa

=== "HTML"
```html title="index.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fundamentos CSS</title>
  <!-- Vinculación canónica de la hoja de estilos externa -->
  <link rel="stylesheet" href="estilos.css">
</head>
<body>
  <h1>Titular Principal</h1>
  <p>Párrafo introductorio de prueba.</p>
</body>
</html>
```

=== "CSS"
```css title="estilos.css"
/*
  ANATOMÍA DE LA REGLA:
  - Selector: h1 (apunta a todos los encabezados h1 del DOM)
  - Bloque de declaraciones: todo lo encerrado entre las llaves { ... }
  - Propiedad 1: color | Valor 1: #003366 | Declaración 1: color: #003366;
  - Propiedad 2: font-family | Valor 2: system-ui, sans-serif | Declaración 2: font-family: system-ui, sans-serif;
*/
h1 {
  color: #003366;
  font-family: system-ui, sans-serif;
}
```

* **Puntos clave:** La etiqueta `<link>` debe residir en el `<head>` y contar con `rel="stylesheet"`. Omitir `type="text/css"` es la buena práctica recomendada en HTML5 por ser redundante.
* **Error frecuente:** Usar una ruta errónea en `href` o cerrar la etiqueta `<link>` con `</link>` (es un elemento vacío/autocerrado en HTML).

---

### Solución U01.02 — Refactorización y desacoplamiento de estilos

=== "HTML"
```html title="limpio.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Separación de Responsabilidades</title>
  <link rel="stylesheet" href="ofertas.css">
</head>
<body>
  <h2 class="titulo-ofertas">Ofertas del mes</h2>
  <p class="texto-condiciones">Condiciones de compra aplicadas.</p>
</body>
</html>
```

=== "CSS"
```css title="ofertas.css"
.titulo-ofertas {
  color: #d32f2f;
  font-size: 1.5rem;
}

.texto-condiciones {
  color: #111111;
  font-weight: bold;
}
```

* **Puntos clave:** Se respeta la Separación de Responsabilidades (SoC). Las clases semánticas identifican el rol del elemento y no su apariencia directa (evitar nombres como `.texto-rojo-24px`).
* **Error frecuente:** Dejar estilos en línea en el HTML argumentando que "solo afectaban a un elemento". Los estilos en línea tienen especificidad (1,0,0,0) y complican el mantenimiento.

---

### Solución U01.03 — Comentarios y legibilidad profesional

```css title="estilos-limpios.css"
/* ==========================================================================
   1. SECCIÓN DE CABECERA Y NAVEGACIÓN
   ========================================================================== */

/* Contenedor principal del encabezado del sitio */
header {
  background-color: #f0f0f0;
  padding: 20px;
}

/* ==========================================================================
   2. TIPOGRAFÍA Y ENCABEZADOS
   ========================================================================== */

/* Subtítulos secundarios de sección */
h2 {
  color: #333333;
}
```

* **Puntos clave:** CSS estándar no admite comentarios de una sola línea con `//` ni numerales `#`. Un comentario mal cerrado anula silenciosamente todas las reglas siguientes hasta el próximo `*/`.
* **Error frecuente:** Usar comentarios estilo JavaScript o C++ (`//`). El analizador de CSS descarta la propiedad o la regla completa por error sintáctico.

---

### Solución U01.04 — Micro-reset universal moderno

```css title="reset.css"
/* 1. Modelo de caja consistente en todo el árbol */
*,
*::before,
*::after {
  box-sizing: border-box;
}

/* 2. Eliminación de márgenes predeterminados del navegador */
body,
h1, h2, h3, h4, h5, h6,
p,
ul, ol,
figure,
blockquote {
  margin: 0;
  padding: 0;
}

/* 3. Base del documento y altura mínima */
body {
  min-height: 100vh;
  line-height: 1.5;
  font-family: system-ui, -apple-system, sans-serif;
  -webkit-font-smoothing: antialiased;
}

/* 4. Listas sin viñetas por defecto cuando se usan en maquetación */
ul, ol {
  list-style: none;
}
```

* **Puntos clave:** El reseteo de `box-sizing: border-box` en `*, *::before, *::after` garantiza que paddings y bordes no desborden los anchos declarados.
* **Error frecuente:** Usar `* { margin: 0; }` indiscriminadamente sin resetear los pseudo-elementos, o no restablecer un `line-height` legible.

---

### Solución U01.05 — Rendimiento de `@import` frente a `<link>`

=== "HTML"
```html title="paralelo.html"
<!-- Carga en paralelo: el navegador inicia las tres peticiones simultáneamente -->
<link rel="stylesheet" href="fonts.css">
<link rel="stylesheet" href="layout.css">
<link rel="stylesheet" href="componentes.css">
```

=== "CSS"
```css title="antipatron.css"
/* ANTIPATRÓN: Bloquea el hilo de renderizado por cascada secuencial */
@import url("fonts.css");
@import url("layout.css");
@import url("componentes.css");
```

* **Puntos clave:** Con `@import`, el navegador no puede descubrir ni solicitar `layout.css` hasta que ha descargado y parseado completamente el archivo CSS inicial. Con múltiples `<link>` en HTML, el navegador ejecuta peticiones HTTP concurrentes.
* **Error frecuente:** Emplear `@import` dentro de CSS para importar librerías pesadas creyendo que modulariza el código sin coste de red.

---

### Solución U01.06 — Herencia natural frente a `inherit` explícito

```css title="herencia.css"
/*
  Propiedades tipográficas (font-family, color, font-size) se heredan naturalmente
  en la mayoría de elementos, pero inputs y botones tienen estilos nativos del SO.
*/
button,
input,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  color: inherit;
  line-height: inherit;
}
```

* **Puntos clave:** Los elementos de formulario son una excepción histórica de los navegadores y no heredan la tipografía del `body`. El valor `inherit` obliga al control a tomar el valor computado de su ancestro directo.
* **Error frecuente:** Redefinir manualmente la fuente en cada botón (`font-family: Arial`) en lugar de usar `inherit`, lo que obliga a modificar múltiples reglas si cambia la tipografía global.

---

### Solución U01.07 — Palabras clave universales: `inherit`, `initial`, `unset` y `revert`

```css title="keywords.css"
/* Hereda el color computado del contenedor padre */
.btn-inherit {
  color: inherit;
}

/* Restablece al valor inicial de la especificación CSS oficial (negro para color) */
.btn-initial {
  color: initial;
}

/* Para propiedades heredadas actúa como inherit; para no heredadas como initial */
.btn-unset {
  color: unset;
}

/* Revierte el estilo al valor que tendría por la hoja del agente de usuario (navegador) */
.btn-revert {
  color: revert;
}
```

* **Puntos clave:** `initial` ignora la herencia y devuelve la propiedad al valor teórico marcado por el W3C; `revert` retrocede en la cascada respetando los estilos por defecto del navegador.
* **Error frecuente:** Creer que `initial` equivale a "los estilos por defecto del navegador". `initial` en `display` siempre es `inline` (incluso para un `<div>`).

---

### Solución U01.08 — Resolución de conflictos por orden de declaración

```css title="orden.css"
p.destacado {
  color: green;
  font-size: 18px;
}

p.destacado {
  color: orange; /* Prevalece esta declaración para 'color' por estar escrita después */
}
```

* **Puntos clave:** El selector `p.destacado` tiene una especificidad de (0, 0, 1, 1) en ambas reglas. A igual especificidad y mismo origen, la regla que se define en último lugar sobreescribe a las anteriores. El tamaño de fuente (`font-size: 18px`) se mantiene intacto porque la segunda regla no lo redefine.
* **Error frecuente:** Pensar que la segunda regla anula todas las propiedades de la primera; solo anula aquellas propiedades que coinciden y colisionan.

---

### Solución U01.09 — Desactivación de `!important` y reestructuración limpia

```css title="limpio-important.css"
/* Clase base con especificidad normal (0, 1, 0) */
.btn {
  background-color: #0056b3;
  color: #ffffff;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
}

/* Modificador con mayor especificidad por encadenamiento o cascada limpia */
.btn.btn-secundario {
  background-color: #6c757d;
  color: #ffffff;
}
```

* **Puntos clave:** Al eliminar `!important`, la cascada vuelve a regirse por la especificidad y el orden. Encadenar `.btn.btn-secundario` otorga especificidad (0, 2, 0), garantizando que sobrescriba a `.btn` (0, 1, 0) sin ensuciar el código.
* **Error frecuente:** Tratar de vencer a un `!important` añadiendo otro selector con `!important`. Eso desencadena una escalada que imposibilita modificar estilos dinámicamente.

---

### Solución U01.10 — Hojas de estilo alternativas para accesibilidad

=== "HTML"
```html title="accesible.html"
<head>
  <meta charset="UTF-8">
  <title>Portal Accesible</title>
  <!-- Hoja de estilos estándar preferida -->
  <link rel="stylesheet" href="estandar.css" title="Estándar">
  <!-- Hoja de estilos alternativa de alto contraste -->
  <link rel="alternate stylesheet" href="alto-contraste.css" title="Alto Contraste">
</head>
```

=== "CSS"
```css title="alto-contraste.css"
/* alto-contraste.css */
body {
  background-color: #000000 !important;
  color: #ffff00 !important;
  font-size: 1.25rem !important;
}

a {
  color: #ffffff !important;
  text-decoration: underline !important;
  font-weight: bold;
}
```

* **Puntos clave:** `rel="alternate stylesheet"` junto con el atributo `title` permite a los navegadores (como Firefox mediante el menú Ver > Estilo de página) y lectores de pantalla conmutar entre estilos oficiales sin necesidad obligatoria de scripts.
* **Error frecuente:** Omitir el atributo `title` en una hoja alternativa, lo que provoca que los navegadores no la reconozcan como estilo seleccionable.

---

## Soluciones: Unidad 02 — Selectores y especificidad

### Solución U02.01 — Selectores básicos y ámbito de aplicación

```css title="selectores-basicos.css"
/* 1. Selector de ID: Único en todo el documento */
#logo-portal {
  font-size: 2rem;
  font-weight: 900;
  color: #1a365d;
}

/* 2. Selector de clase: Reutilizable en múltiples elementos */
.noticia {
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 1rem;
}

/* 3. Selector de tipo combinado con clase */
p.resumen {
  font-size: 1.125rem;
  color: #4a5568;
  line-height: 1.6;
}
```

* **Puntos clave:** `p.resumen` solo selecciona párrafos que tengan la clase `.resumen`, ignorando elementos `div.resumen` o párrafos ordinarios.
* **Error frecuente:** Utilizar IDs para estilizar componentes repetibles como tarjetas o botones, impidiendo su reutilización limpia.

---

### Solución U02.02 — Combinador hijo directo (`>`) frente a descendiente (` `)

```css title="menu.css"
/* Afecta ÚNICAMENTE a los enlaces del primer nivel del menú */
.menu-principal > ul > li > a {
  font-size: 1.25rem;
  font-weight: bold;
  border-bottom: 2px solid #0056b3;
  padding-bottom: 4px;
}

/* Los enlaces de submenús anidados no heredan esas declaraciones */
.submenu a {
  font-size: 0.95rem;
  font-weight: normal;
  border-bottom: none;
}
```

* **Puntos clave:** Si se hubiera usado `.menu-principal a` (combinador descendiente), todos los enlaces de cualquier nivel habrían recibido el borde y tamaño grande.
* **Error frecuente:** Confundir el espacio en blanco (cualquier nivel de profundidad) con el signo mayor que `>` (hijo biológico inmediato).

---

### Solución U02.03 — Combinadores de hermanos: adyacente (`+`) y general (`~`)

```css title="hermanos.css"
/* a) Hermano adyacente (+): Solo el primer párrafo que sigue inmediatamente a un h2 */
h2 + p {
  font-size: 1.2rem;
  color: #2d3748;
  font-weight: 500;
}

/* b) Hermano general (~): Todos los inputs hermanos que aparezcan después de la alerta */
.alerta-error ~ .form-group input {
  border-color: #e53e3e;
  background-color: #fff5f5;
}
```

* **Puntos clave:** `A + B` exige adyacencia inmediata. Si entre el `h2` y el `p` hubiera una imagen, el selector `h2 + p` no coincidiría. `A ~ B` coincide con todos los B que compartan el mismo padre y vengan después de A.
* **Error frecuente:** Intentar usar combinadores de hermanos para seleccionar elementos precedentes (hacia atrás). En CSS el flujo de selección va siempre hacia adelante.

---

### Solución U02.04 — Selectores de atributos avanzados

```css title="atributos.css"
/* Enlaces que abren en nueva pestaña */
a[target="_blank"]::after {
  content: " ↗";
  font-size: 0.85em;
}

/* Enlaces externos seguros (comienzan por https://) */
a[href^="https://"] {
  color: #0b69a3;
}

/* Documentos descargables PDF (terminan en .pdf) */
a[href$=".pdf"] {
  padding-inline-start: 1.5rem;
  background: url("icono-pdf.svg") no-repeat left center;
  background-size: 1rem;
}

/* Enlaces cuya URL contiene la palabra "examen" en cualquier posición */
a[href*="examen"] {
  font-weight: bold;
  color: #c53030;
}
```

* **Puntos clave:** `^=` (empieza por), `$=` (termina en), `*=` (contiene). Proporcionan retroalimentación visual accesible al usuario antes de hacer clic.
* **Error frecuente:** Olvidar que las mayúsculas/minúsculas importan en los atributos salvo que se añada el modificador insensible `i` (ej. `[href$=".pdf" i]`).

---

### Solución U02.05 — Estados dinámicos de interfaz y foco accesible

```css title="boton-estados.css"
.btn-accion {
  display: inline-flex;
  align-items: center;
  padding: 10px 20px;
  background-color: #2563eb;
  color: #ffffff;
  border: 2px solid transparent;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

/* Hover: Puntero del ratón sobre el botón */
.btn-accion:hover {
  background-color: #1d4ed8;
}

/* Active: Momento exacto de pulsación */
.btn-accion:active {
  background-color: #1e40af;
  transform: translateY(1px);
}

/* Foco accesible: Solo visible con teclado (Tab) */
.btn-accion:focus-visible {
  outline: 3px solid #60a5fa;
  outline-offset: 3px;
}

/* Deshabilitado: Inaccesible para interacción */
.btn-accion:disabled {
  background-color: #94a3b8;
  cursor: not-allowed;
  opacity: 0.7;
}
```

* **Puntos clave:** `:focus-visible` activa el anillo de enfoque solo para usuarios que navegan con teclado, eliminando la molesta caja de foco para usuarios de ratón sin perjudicar la accesibilidad.
* **Error frecuente:** Desactivar el foco con `outline: none` sin proveer un indicador visual alternativo, vulnerando el criterio WCAG 2.4.7.

---

### Solución U02.06 — Pseudo-clases estructurales y fórmulas `nth-child`

```css title="nth-child.css"
/* Primer y último producto de la lista */
.producto:first-child {
  border-top-width: 4px;
}
.producto:last-child {
  border-bottom-width: 4px;
}

/* Filas alternas (zebra) */
.producto:nth-child(even) {
  background-color: #f8fafc;
}

/* Cada tercer elemento (3, 6, 9, 12...) */
.producto:nth-child(3n) {
  border-inline-end: 3px solid #3b82f6;
}

/* Segundo párrafo independientemente de si hay encabezados interpuestos */
p:nth-of-type(2) {
  font-style: italic;
}
```

* **Puntos clave:** Si la estructura es `<h1>`, `<p>`, `<p>`, el selector `p:nth-child(2)` selecciona el primer párrafo porque es el segundo hijo absoluto. En cambio, `p:nth-of-type(2)` selecciona el segundo párrafo real.
* **Error frecuente:** Usar `:nth-child` creyendo que filtra por tipo de etiqueta; filtra por posición global entre hermanos.

---

### Solución U02.07 — Generación de contenido decorativo con `::before` y `::after`

```css title="pseudoelementos.css"
/* Comillas decorativas antes de una cita */
blockquote.cita {
  position: relative;
  padding-left: 2.5rem;
  font-style: italic;
}

blockquote.cita::before {
  content: "“";
  position: absolute;
  left: 0;
  top: -0.5rem;
  font-size: 4rem;
  color: #93c5fd;
  font-family: serif;
  line-height: 1;
}

/* Badge con punto indicador en tarjeta */
.badge-nuevo::after {
  content: "";
  display: inline-block;
  width: 8px;
  height: 8px;
  background-color: #ef4444;
  border-radius: 50%;
  margin-left: 6px;
}
```

* **Puntos clave:** La propiedad `content` es obligatoria para generar la caja visual del pseudo-elemento. Si es decorativo, `content: ""` permite dibujar formas geométricas o fondos con CSS.
* **Error frecuente:** Insertar texto informativo vital únicamente en `content: "Texto"`, ya que algunos lectores de pantalla antiguos pueden ignorarlo o traducirlo incorrectamente.

---

### Solución U02.08 — Matriz de cálculo y ordenación de especificidad

Desglose de la puntuación en la tupla `(Inline, ID, Clase/Attr/Pseudo-clase, Elemento/Pseudo-elem)`:

* **Selector A:** `header nav.principal ul li a:hover` $\rightarrow$ `(0, 0, 2, 4)`
  *(0 IDs, 2 clases/pseudo `[.principal, :hover]`, 4 elementos `[header, nav, ul, li, a]`)*
* **Selector B:** `#usuario-perfil .datos > span` $\rightarrow$ `(0, 1, 1, 1)`
  *(1 ID `[#usuario-perfil]`, 1 clase `[.datos]`, 1 elemento `[span]`)*
* **Selector C:** `body main article p` $\rightarrow$ `(0, 0, 0, 4)`
  *(0 IDs, 0 clases, 4 elementos `[body, main, article, p]`)*
* **Selector D:** `button[type="submit"]:not(:disabled)` $\rightarrow$ `(0, 0, 2, 1)`
  *(0 IDs, 2 attr/pseudo `[[type=submit], :disabled - :not no suma pero sí su argumento]`, 1 elemento `[button]`)*
* **Selector E:** `#alerta` $\rightarrow$ `(0, 1, 0, 0)`
  *(1 ID `[#alerta]`, 0 clases, 0 elementos)*

**Ordenación de menor a mayor prioridad en la cascada:**
$$\text{C (0,0,0,4)} < \text{D (0,0,2,1)} < \text{A (0,0,2,4)} < \text{E (0,1,0,0)} < \text{B (0,1,1,1)}$$

* **Puntos clave:** Un solo ID en la columna B (ej. Selector E) supera a cualquier número de clases en la columna C (como el Selector A con 2 clases y 4 elementos).
* **Error frecuente:** Sumar los números en un único valor decimal (ej. pensar que 2 clases y 4 elementos = "24 puntos" y 1 ID = "10 puntos"). No hay base decimal en la especificidad.

---

### Solución U02.09 — Pseudo-clases lógicas: `:is()`, `:where()` y `:not()`

```css title="logicas.css"
/* Versión compacta con :is() -> Especificidad (0, 0, 0, 2) [el argumento más alto: article h1] */
:is(article, section, aside) :is(h1, h2, h3) {
  color: #1a1a1a;
}

/* Versión con :where() -> Especificidad EXACTA (0, 0, 0, 0) */
:where(article, section, aside) :where(h1, h2, h3) {
  color: #1a1a1a;
}
```

* **Puntos clave:** `:where()` establece la especificidad a cero absoluto. Esto la convierte en la herramienta perfecta para resets y hojas base de componentes, ya que cualquier regla de usuario la sobrescribirá con facilidad sin guerras de especificidad.
* **Error frecuente:** Usar `:is()` creyendo que tiene especificidad cero; `:is()` asume la especificidad del selector más pesado de su lista de opciones.

---

### Solución U02.10 — El selector relacional padre `:has()`

```css title="has.css"
/* a) Estilar la tarjeta cuando contiene una imagen */
.tarjeta:has(.tarjeta-img) {
  border: 2px solid #3b82f6;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

/* b) Cambiar el fondo del formulario cuando un checkbox obligatorio está marcado */
form:has(input[type="checkbox"]:required:checked) {
  background-color: #f0fdf4;
  border-color: #22c55e;
}
```

* **Puntos clave:** `:has()` actúa como un selector de padre y hermano relacional en CSS puro, evaluando el estado o presencia de descendientes sin requerir eventos JavaScript.
* **Error frecuente:** Intentar anidar un `:has()` dentro de otro `:has()` (está prohibido por especificación para evitar bucles de rendimiento infinitos).

---

## Soluciones: Unidad 03 — Modelo de caja

### Solución U03.01 — Cálculo analítico de dimensiones en `content-box`

* **Datos de la caja:** `width: 320px`, `padding: 24px`, `border: 6px`, `margin: 30px`.
* **Fórmula de ancho total renderizado (visual):**
  $$\text{Ancho Visual} = \text{width} + \text{padding-left} + \text{padding-right} + \text{border-left} + \text{border-right}$$
  $$\text{Ancho Visual} = 320 + 24 + 24 + 6 + 6 = \mathbf{380\text{ px}}$$
* **Fórmula de ocupación total en el flujo (con márgenes):**
  $$\text{Espacio Total} = \text{Ancho Visual} + \text{margin-left} + \text{margin-right} = 380 + 30 + 30 = \mathbf{440\text{ px}}$$
* **Puntos clave:** En `content-box` (valor inicial de CSS), la propiedad `width` solo delimita el área interior del contenido; todo padding y borde se suma por fuera.
* **Error frecuente:** Creer que un elemento con `width: 320px` y `padding: 24px` medirá 320px en la pantalla.

---

### Solución U03.02 — Prevención de rotura de layout con `border-box`

=== "HTML"
```html title="columnas.html"
<div class="fila">
  <div class="columna">Columna 1</div>
  <div class="columna">Columna 2</div>
</div>
```

=== "CSS"
```css title="columnas.css"
.fila {
  display: flex; /* o ancho contenedor */
  width: 100%;
}

.columna {
  box-sizing: border-box; /* Imprescindible para evitar el desbordamiento */
  width: 50%;
  padding: 20px;
  border: 2px solid #cbd5e1;
}
```

* **Puntos clave:** Con `border-box`, el 50% abarca el ancho total exterior de la columna (incluyendo sus 40px de padding horizontal y 4px de borde). Las dos columnas suman exactamente el 100% y encajan sin caer a la línea siguiente.
* **Error frecuente:** Mantener `content-box` y forzar un `width: 48%` aproximado para que "quepa", lo que genera layouts frágiles que se rompen al cambiar el zoom.

---

### Solución U03.03 — Shorthand de padding y comportamiento en elementos en línea

```css title="inline-block.css"
/* span convertido a inline-block */
.etiqueta-destacada {
  display: inline-block;
  padding: 6px 14px; /* Shorthand: 6px arriba/abajo, 14px izquierda/derecha */
  margin: 4px 8px;
  background-color: #e0e7ff;
  color: #3730a3;
  border-radius: 4px;
}
```

* **Puntos clave:** Los elementos puramente `inline` (como `<span>` por defecto) pintan el fondo del padding pero este se superpone visualmente sobre las líneas adyacentes sin empujarlas. Al aplicar `display: inline-block`, la caja genera un rectángulo que respeta márgenes y alturas completas.
* **Error frecuente:** Intentar separar verticalmente párrafos aplicando `margin-top` o `margin-bottom` a un `<span>` en línea.

---

### Solución U03.04 — Colapso de márgenes entre hermanos adyacentes

* **Caso 1:** `h2` (`margin-bottom: 30px`) y `p` (`margin-top: 20px`).
  * En el colapso vertical, prevalece el margen positivo mayor:
  $$\text{Espacio resultante} = \max(30\text{px}, 20\text{px}) = \mathbf{30\text{ px}}$$
* **Caso 2:** Si ambos tuvieran 30px, el espacio sigue siendo $\max(30, 30) = \mathbf{30\text{ px}}$.
* **Caso 3:** Si el párrafo tuviera `margin-top: -10px`:
  $$\text{Espacio resultante} = 30\text{px} + (-10\text{px}) = \mathbf{20\text{ px}}$$
* **Puntos clave:** El colapso solo ocurre en el eje vertical (bloque) entre hermanos en el flujo normal; los márgenes horizontales jamás colapsan (siempre se suman).
* **Error frecuente:** Sumar 30 + 20 y esperar 50px de separación entre títulos y párrafos.

---

### Solución U03.05 — Colapso de margen padre-hijo y soluciones modernas

```css title="colapso-padre.css"
/* Solución recomendada: Crear un nuevo BFC sin efectos secundarios */
.contenedor-tarjeta {
  display: flow-root;
  background-color: #f1f5f9;
}

.contenedor-tarjeta h1 {
  margin-top: 40px; /* Ahora el margen se queda DENTRO del contenedor */
}
```

* **Puntos clave:** Si un padre no tiene padding superior, ni borde superior, ni nada que lo separe de su primer hijo, los márgenes de ambos se fusionan y escapan al exterior. `display: flow-root` crea un Block Formatting Context (BFC) nativo que retiene todos los márgenes internos.
* **Error frecuente:** Usar `overflow: hidden` para contener márgenes, con el riesgo de recortar tooltips o menús desplegables que sobresalgan de la tarjeta.

---

### Solución U03.06 — Centrado horizontal con márgenes automáticos

```css title="centrado-bloque.css"
.contenedor-principal {
  max-width: 1000px;
  margin-inline: auto; /* Equivalente moderno a: margin-left: auto; margin-right: auto; */
  padding-inline: 1.5rem; /* Evita que el texto toque los bordes físicos en móviles */
}
```

* **Puntos clave:** Los márgenes automáticos horizontales dividen equitativamente el espacio restante entre la izquierda y la derecha de la caja. Si la ventana mide menos de 1000px, `max-width` permite que la caja se reduzca fluidamente al 100%.
* **Error frecuente:** Usar `width: 1000px` fijo en lugar de `max-width`, provocando barras de desplazamiento horizontal destructivas en pantallas móviles.

---

### Solución U03.07 — Estilos de bordes y radios asimétricos

```css title="callout.css"
.callout-destacado {
  background-color: #eff6ff;
  border: 1px solid #bfdbfe;
  border-left: 6px solid #2563eb; /* Borde izquierdo dominante */
  /* Sintaxis 4 valores: top-left top-right bottom-right bottom-left */
  border-radius: 0 12px 12px 0;
  padding: 1rem 1.5rem;
}
```

* **Puntos clave:** Las esquinas izquierdas quedan rectas (0) para coincidir con la línea sólida del borde decorativo, mientras que las esquinas derechas quedan suavemente redondeadas a 12px.
* **Error frecuente:** Confundir el orden de las esquinas en `border-radius`. Sigue siempre las agujas del reloj: arriba-izquierda, arriba-derecha, abajo-derecha, abajo-izquierda.

---

### Solución U03.08 — `outline` frente a `border` en focos accesibles

```css title="foco-accesible.css"
.btn-accesible {
  background-color: #0f172a;
  color: #ffffff;
  padding: 10px 24px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

/* Foco con outline: no altera el layout ni produce temblores en la pantalla */
.btn-accesible:focus-visible {
  outline: 3px solid #38bdf8;
  outline-offset: 3px; /* Separa el anillo del borde físico del botón */
}
```

* **Puntos clave:** `border` forma parte del modelo de caja; añadir 3px de borde en `:focus` añade 6px al tamaño total empujando a los elementos contiguos. `outline` se dibuja fuera del cálculo de geometría en una capa superior.
* **Error frecuente:** Añadir `border: 3px solid` dinámicamente en hover/focus sin prever el salto visual resultante.

---

### Solución U03.09 — Sistema de sombras multicapa con `box-shadow`

```css title="sombras.css"
/* Tarjeta elevada con sombra multicapa suave y realista */
.tarjeta-elevada {
  background-color: #ffffff;
  border-radius: 12px;
  padding: 2rem;
  box-shadow:
    0 1px 2px rgba(0, 0, 0, 0.05),
    0 4px 6px -1px rgba(0, 0, 0, 0.08),
    0 12px 18px -4px rgba(0, 0, 0, 0.12);
}

/* Campo de formulario con efecto hundido interior */
.campo-hundido {
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  padding: 8px 12px;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.06);
}
```

* **Puntos clave:** La combinación de una sombra corta y oscura para el contacto y otra más amplia y difuminada para la luz ambiental emula la física de la iluminación natural.
* **Error frecuente:** Usar una sola sombra con gran dispersión y opacidad alta (`box-shadow: 0 10px 20px #000`), lo que genera un aspecto tosco y sucio.

---

### Solución U03.10 — Gestión de desbordamiento (`overflow`) y scrollbars parásitas

```css title="overflow.css"
.panel-notificaciones {
  max-height: 320px;
  overflow-x: hidden; /* Bloquea cualquier desbordamiento horizontal */
  overflow-y: auto;   /* Scroll vertical solo cuando el contenido lo requiera */
  overscroll-behavior: contain; /* Evita que el scroll encadene al body */
  overflow-wrap: break-word;    /* Parte cadenas de texto excesivamente largas */
  padding: 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
}
```

* **Puntos clave:** `overflow-wrap: break-word` fuerza a palabras largas (como URLs o hashes) a saltar de línea sin estirar el contenedor. `overscroll-behavior: contain` aísla el desplazamiento dentro del panel.
* **Error frecuente:** Usar `overflow: scroll`, lo que dibuja barras de desplazamiento permanentes e inactivas en Windows aunque el contenido no las necesite.

---

## Soluciones: Unidad 04 — Posicionamiento y z-index

### Solución U04.01 — Posicionamiento relativo y conservación del espacio físico

```css title="relative.css"
.icono-ajustado {
  position: relative;
  top: 8px;  /* Desplaza visualmente 8px hacia abajo */
  left: 4px; /* Desplaza visualmente 4px hacia la derecha */
}
```

* **Puntos clave:** El hueco original de 24x24px del icono se conserva exactamente igual en el flujo del documento; los párrafos y textos adyacentes no se reajustan ni se mueven.
* **Error frecuente:** Usar `position: relative` creyendo que saca al elemento del flujo. Solo altera la posición del dibujo visual.

---

### Solución U04.02 — Posicionamiento absoluto y búsqueda del bloque contenedor

=== "HTML"
```html title="alerta.html"
<div class="tarjeta-alerta">
  <h3>Aviso importante</h3>
  <p>La sesión caducará en 5 minutos.</p>
  <button class="btn-cerrar" aria-label="Cerrar">×</button>
</div>
```

=== "CSS"
```css title="alerta.css"
.tarjeta-alerta {
  position: relative; /* Bloque contenedor de referencia para los hijos absolutos */
  padding: 1.5rem;
  background-color: #fef2f2;
  border: 1px solid #fecaca;
  border-radius: 8px;
}

.btn-cerrar {
  position: absolute;
  top: 12px;
  right: 12px;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
}
```

* **Puntos clave:** Sin `position: relative` en `.tarjeta-alerta`, el botón subiría por el árbol DOM buscando un ancestro posicionado hasta anclarse en la ventana del navegador.
* **Error frecuente:** Olvidar añadir `position: relative` al contenedor padre.

---

### Solución U04.03 — Tarjeta de comercio electrónico con badge flotante

```css title="badge-producto.css"
.tarjeta-producto {
  position: relative;
  width: 280px;
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  overflow: visible; /* Debe ser visible para permitir que el badge sobresalga */
}

.badge-oferta {
  position: absolute;
  top: -8px;
  left: -8px;
  background-color: #dc2626;
  color: #ffffff;
  font-size: 0.8rem;
  font-weight: bold;
  padding: 4px 10px;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}
```

* **Puntos clave:** Las coordenadas negativas (`top: -8px; left: -8px`) sitúan al elemento fuera del perímetro de la tarjeta. Es vital no tener `overflow: hidden` en el padre o el badge quedaría cercenado.
* **Error frecuente:** Poner `overflow: hidden` en la tarjeta para redondear imágenes y preguntarse por qué el badge desaparece.

---

### Solución U04.04 — Cabecera fija persistente con compensación de espacio

```css title="header-fixed.css"
/* 1. Cabecera fija al viewport */
.header-fijo {
  position: fixed;
  inset-block-start: 0;
  inset-inline: 0; /* Ocupa el 100% del ancho horizontal */
  height: 64px;
  background-color: #ffffff;
  border-bottom: 1px solid #e2e8f0;
  z-index: 100;
}

/* 2. Compensación en el cuerpo del documento */
body {
  padding-top: 64px; /* Idéntico a la altura de la cabecera fija */
}
```

* **Puntos clave:** Los elementos `position: fixed` salen del flujo normal. El primer elemento del `body` subirá a la coordenada `top: 0` quedando tapado si no se añade un relleno compensatorio.
* **Error frecuente:** No añadir `z-index` a la cabecera fija, provocando que elementos con posición relativa de la página se pinten por encima de ella al hacer scroll.

---

### Solución U04.05 — Cabeceras adhesivas con `position: sticky`

```css title="sticky.css"
.directorio-grupo {
  margin-bottom: 2rem;
}

/* Cabecera alfabética adhesiva */
.letra-encabezado {
  position: sticky;
  top: 0; /* Umbral donde comienza a fijarse */
  background-color: #f8fafc;
  padding: 8px 16px;
  font-weight: bold;
  border-bottom: 2px solid #cbd5e1;
  z-index: 10;
}
```

* **Puntos clave:** Un elemento `sticky` solo se fija mientras su elemento padre directo siga visible en la pantalla. Al acabarse el grupo `.directorio-grupo`, la cabecera adhesiva es empujada fuera de la pantalla por el siguiente grupo.
* **Error frecuente:** Colocar `overflow: hidden` en un ancestro, lo que desactiva por completo el mecanismo de `position: sticky`.

---

### Solución U04.06 — Propiedades lógicas de posicionamiento con `inset`

```css title="modal-backdrop.css"
/* Superposición a pantalla completa */
.modal-backdrop {
  position: fixed;
  inset: 0; /* Reemplaza a: top: 0; right: 0; bottom: 0; left: 0; */
  background-color: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
  z-index: 999;
}
```

* **Puntos clave:** `inset: 0` es más limpio y legible. En sistemas internacionales, `inset-inline-start` se adapta automáticamente a idiomas de derecha a izquierda (RTL) como el árabe o hebreo.
* **Error frecuente:** Declarar `width: 100%; height: 100%;` junto con `top: 0; left: 0;`, lo que resulta innecesariamente verboso frente a `inset: 0`.

---

### Solución U04.07 — Orden natural de apilamiento sin `z-index`

* **Orden oficial de dibujo (de abajo hacia arriba):**
  1. Fondo y bordes del elemento raíz (`html`).
  2. Elementos no posicionados (`position: static`) en orden del DOM.
  3. Elementos posicionados (`relative`, `absolute`, `fixed`, `sticky`) en orden del DOM.
* **Resolución del ejercicio:**
  * Si las tres cajas son `static`, la última en el DOM se dibuja sobre las anteriores.
  * Si la caja 1 tiene `position: relative` y las cajas 2 y 3 son `static`, la **caja 1 se dibuja por encima** de las otras dos, sin importar que esté escrita antes en el HTML.
* **Puntos clave:** La simple presencia de `position` distinto de `static` promociona al elemento por encima de todos los elementos no posicionados del flujo normal.
* **Error frecuente:** Llenar el código de `z-index: 1`, `z-index: 2` cuando bastaba con comprender el orden natural de apilamiento.

---

### Solución U04.08 — Diagnóstico de bugs de `z-index` y Stacking Context

```css title="solucion-stacking.css"
/* Corrección: Asignar un z-index superior al contenedor padre de la cabecera */
.cabecera {
  position: relative;
  z-index: 10; /* Gana al z-index: 2 del hero */
}

.dropdown {
  position: absolute;
  z-index: 1; /* Valor sensato, ya no necesita 9999 */
}

.hero {
  position: relative;
  z-index: 2;
}
```

* **Puntos clave:** Como `.cabecera` (z-index: 1) y `.hero` (z-index: 2) formaban contextos de apilamiento independientes, sus contenidos se comparaban exclusivamente a través de sus padres. Ningún elemento hijo de la cabecera podía sobrepasar al hero. Elevando el padre a `z-index: 10` se soluciona limpiamente.
* **Error frecuente:** Subir el z-index del hijo a `999999` sin entender que está atrapado en el contexto de apilamiento de su padre.

---

### Solución U04.09 — Efecto colateral de `transform` sobre elementos `fixed`

```css title="fix-transform.css"
/* OPCIÓN 1: Extraer el modal para que sea hijo directo de <body> (Patrón Portal) */
body > .modal {
  position: fixed;
  inset: 0;
  z-index: 1000;
}

/* OPCIÓN 2: Aplicar la transformación solo a la imagen interior, no al contenedor */
.tarjeta:hover .tarjeta-img {
  transform: scale(1.05); /* El ancestro del modal ya no tiene transform */
}
```

* **Puntos clave:** Por especificación del W3C, cualquier elemento con `transform`, `filter`, `perspective` o `contain` distinto de `none` pasa a actuar como bloque contenedor para todos sus descendientes `fixed`, haciendo que `100vw/100vh` se mida respecto a la tarjeta y no a la pantalla.
* **Error frecuente:** Volverse loco buscando por qué un modal `fixed` se queda encerrado dentro de una tarjeta animada.

---

### Solución U04.10 — Aislamiento de capas con `isolation: isolate`

```css title="isolation.css"
:root {
  --z-base: 1;
  --z-header: 100;
  --z-dropdown: 200;
  --z-modal: 500;
  --z-toast: 1000;
}

/* El componente queda aislado en su propio contexto de apilamiento */
.tarjeta-componente {
  isolation: isolate;
}

.tarjeta-componente .tooltip-local {
  position: absolute;
  z-index: 10; /* Este 10 nunca interferirá con la escala global del sitio */
}
```

* **Puntos clave:** `isolation: isolate` crea un nuevo Stacking Context de forma segura sin requerir declarar `position: relative` ni números mágicos de `z-index`.
* **Error frecuente:** Usar números aleatorios como `z-index: 2147483647` en lugar de una escala tipificada de tokens.

---

## Soluciones: Unidad 05 — Flexbox

### Solución U05.01 — Contenedor flex y anatomía de ejes

```css title="flex-ejes.css"
.lista-flex {
  display: flex;
  list-style: none;
  padding: 0;
  gap: 1rem;
}

/* Dirección en columna invertida */
.lista-flex-invertida {
  display: flex;
  flex-direction: column-reverse;
}
```

* **Puntos clave:** Con `flex-direction: row`, el eje principal discurre horizontalmente y el eje cruzado verticalmente. Con `flex-direction: column-reverse`, el eje principal pasa a ser vertical (empezando por abajo y subiendo hacia arriba).
* **Error frecuente:** Creer que `justify-content` siempre alinea en horizontal; `justify-content` alinea siempre a lo largo del eje principal, que es vertical cuando `flex-direction: column`.

---

### Solución U05.02 — Distribución en el eje principal con `justify-content`

```css title="justify.css"
.fila-botones {
  display: flex;
  background-color: #f1f5f9;
  padding: 1rem;
}

/* Variantes de distribución */
.fila-start    { justify-content: flex-start; }
.fila-center   { justify-content: center; }
.fila-end      { justify-content: flex-end; }
.fila-between  { justify-content: space-between; } /* Pegados a los bordes */
.fila-around   { justify-content: space-around; }  /* Extremos tienen medio espacio */
.fila-evenly   { justify-content: space-evenly; }  /* Espacio idéntico en todos los huecos */
```

* **Puntos clave:** `space-between` no deja margen en los extremos; `space-around` asigna la mitad de espacio en los bordes que entre elementos; `space-evenly` distribuye espacios exactamente idénticos en todos los intervalos.
* **Error frecuente:** Usar márgenes calculados manualmente con porcentajes cuando `space-between` o `gap` resuelven la distribución de forma nativa.

---

### Solución U05.03 — Alineación en el eje cruzado con `align-items`

```css title="align-items.css"
.barra-usuario {
  display: flex;
  align-items: center; /* Centrado vertical en el eje cruzado */
  gap: 16px;           /* Separación limpia entre avatar, texto y botón */
  padding: 12px;
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
}
```

* **Puntos clave:** El valor por defecto de `align-items` es `stretch` (estira todos los elementos a la altura del más alto). Al cambiar a `center`, cada elemento adopta su altura intrínseca y se centra verticalmente.
* **Error frecuente:** Usar `line-height` igual a la altura de la caja o tablas de display para centrar elementos verticales dispares.

---

### Solución U05.04 — El centrado perfecto bidimensional

```css title="centrado-flex.css"
.contenedor-login {
  display: flex;
  justify-content: center; /* Centrado horizontal */
  align-items: center;     /* Centrado vertical */
  min-height: 100vh;
  background-color: #f8fafc;
}

.tarjeta-login {
  width: 100%;
  max-width: 380px;
  padding: 2rem;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}
```

* **Puntos clave:** Alternativamente, `display: flex` en el contenedor y `margin: auto` en la `.tarjeta-login` produce exactamente el mismo centrado perfecto en ambos ejes.
* **Error frecuente:** Usar `top: 50%; left: 50%; transform: translate(-50%, -50%);` en lugar del centrado nativo limpio de Flexbox.

---

### Solución U05.05 — Barra de navegación con espaciador automático

=== "HTML"
```html title="navbar-auto.html"
<nav class="navbar">
  <a href="#" class="logo">MiEmpresa</a>
  <a href="#">Productos</a>
  <a href="#">Servicios</a>
  <a href="#">Contacto</a>
  <a href="#" class="btn-login">Entrar</a>
  <a href="#" class="btn-registro">Registro</a>
</nav>
```

=== "CSS"
```css title="navbar-auto.css"
.navbar {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  padding: 1rem 2rem;
  background-color: #ffffff;
  border-bottom: 1px solid #e2e8f0;
}

/* Empuja este elemento y a todos los que le siguen al extremo derecho */
.btn-login {
  margin-inline-start: auto; /* o margin-left: auto */
}
```

* **Puntos clave:** En Flexbox, `margin-left: auto` consume todo el espacio sobrante en el eje principal. Elimina la necesidad de envolver los botones en un `<div>` secundario con `justify-content: space-between`.
* **Error frecuente:** Usar `float: right` dentro de un contenedor flex (el float es completamente ignorado en flex items).

---

### Solución U05.06 — Envoltura elástica y separación multilínea con `flex-wrap`

```css title="tags-wrap.css"
.contenedor-tags {
  display: flex;
  flex-wrap: wrap;       /* Permite saltar a la siguiente fila al llenarse */
  gap: 8px 12px;         /* 8px vertical entre filas, 12px horizontal entre tags */
  padding: 1rem;
}

.tag-item {
  padding: 6px 14px;
  background-color: #e2e8f0;
  color: #334155;
  border-radius: 9999px; /* Forma de píldora */
  font-size: 0.875rem;
}
```

* **Puntos clave:** Sin `flex-wrap: wrap`, los elementos flex intentarán encogerse agresivamente o desbordarán horizontalmente la pantalla en resoluciones móviles.
* **Error frecuente:** Añadir márgenes a cada tag y luego tener que restar márgenes negativos en el contenedor padre; `gap` resuelve la separación sin efectos colaterales.

---

### Solución U05.07 — El trío `flex-grow`, `flex-shrink` y `flex-basis`

```css title="tres-columnas.css"
.layout-dashboard {
  display: flex;
  gap: 1.5rem;
}

/* 1. Barra lateral: Fija en 240px, no crece ni se encoge */
.sidebar {
  flex: 0 0 240px; /* grow: 0, shrink: 0, basis: 240px */
}

/* 2. Área principal: Absorbe todo el espacio sobrante */
.contenido-principal {
  flex: 1 1 0%;    /* Crece todo lo posible a partir de una base cero */
}

/* 3. Panel de widgets: Base 300px, puede encogerse pero no crecer */
.panel-widgets {
  flex: 0 1 300px; /* grow: 0, shrink: 1, basis: 300px */
}
```

* **Puntos clave:** `flex: 1` es el atajo recomendado para `flex: 1 1 0%`. Garantiza un reparto equitativo del espacio sin verse distorsionado por el contenido previo de los elementos.
* **Error frecuente:** Usar `flex-basis: auto` creyendo que reparte el espacio equitativamente; `auto` tiene en cuenta el tamaño del contenido interno antes de repartir el sobrante.

---

### Solución U05.08 — Patrón de pie de página pegajoso (*Sticky Footer*)

```css title="sticky-footer.css"
body {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  margin: 0;
}

/* El elemento main crece absorbiendo cualquier hueco vertical disponible */
main {
  flex: 1 0 auto;
}

footer {
  flex-shrink: 0;
  background-color: #0f172a;
  color: #ffffff;
  padding: 2rem;
}
```

* **Puntos clave:** Al tener `min-height: 100vh` en el `body`, si la página tiene poco contenido el `<main>` se estira obligando al `<footer>` a asentarse en la base. Si la página tiene mucho texto, el scroll funciona de manera 100% natural.
* **Error frecuente:** Usar `position: fixed` en el footer para fijarlo abajo, haciendo que tape el contenido de la página al hacer scroll.

---

### Solución U05.09 — Reordenación visual con `order` y accesibilidad

=== "HTML"
```html title="order-a11y.html"
<!-- En el DOM, el contenido principal va primero por accesibilidad -->
<div class="contenedor-vista">
  <main class="resultados">Lista de resultados (Leído primero por Screen Reader)</main>
  <aside class="filtros">Filtros de búsqueda</aside>
</div>
```

=== "CSS"
```css title="order-a11y.css"
.contenedor-vista {
  display: flex;
}

/* Se mueve visualmente a la izquierda sin romper el orden semántico */
.filtros {
  order: -1;
  width: 260px;
}

.resultados {
  flex: 1;
}
```

* **Puntos clave:** El valor por defecto de `order` es 0. Cualquier valor negativo (`-1`) desplaza el elemento al inicio visual. Sin embargo, no debe alterarse de forma drástica respecto a la navegación por tabulador para evitar confusión cognitiva.
* **Error frecuente:** Utilizar `order` para resolver desastres de estructura HTML en lugar de maquetar con semántica correcta.

---

### Solución U05.10 — Tarjetas de contenido con botones alineados al fondo

```css title="tarjeta-boton-fondo.css"
.grid-tarjetas {
  display: flex;
  gap: 1.5rem;
}

.tarjeta {
  display: flex;
  flex-direction: column; /* Flujo vertical interno */
  flex: 1;
  padding: 1.5rem;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
}

.tarjeta-descripcion {
  color: #475569;
  line-height: 1.5;
}

/* Empuja el botón al fondo de la tarjeta */
.tarjeta-btn {
  margin-top: auto; /* Absorbe el espacio vertical sobrante de la tarjeta */
  padding: 10px;
  background-color: #2563eb;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  text-align: center;
}
```

* **Puntos clave:** En un contenedor flex vertical, `margin-top: auto` en el último hijo actúa como un muelle que empuja al botón contra el borde inferior de la tarjeta, alineando todos los botones de la fila.
* **Error frecuente:** Forzar alturas fijas en píxeles a las tarjetas o descripciones para que coincidan, lo que provoca desbordamientos de texto cuando el usuario amplía la fuente.

---

## Soluciones: Unidad 06 — CSS Grid

### Solución U06.01 — Cuadrícula básica bidimensional

```css title="grid-basico.css"
.grid-iconos {
  display: grid;
  grid-template-columns: 200px 200px 200px; /* 3 columnas fijas */
  grid-template-rows: 150px 150px;           /* 2 filas fijas */
  gap: 16px;                                 /* Separación bidimensional */
}
```

* **Puntos clave:** `grid-template-columns` y `grid-template-rows` definen explícitamente las dimensiones de las pistas. El `gap` separa las celdas tanto horizontal como verticalmente sin requerir márgenes perimetrales.
* **Error frecuente:** Usar Flexbox con cálculos manuales de porcentaje para forzar una rejilla rígida de 3 columnas y 2 filas.

---

### Solución U06.02 — La unidad fraccionaria `fr` y `repeat()`

```css title="grid-fr.css"
/* Cuadrícula de 4 columnas iguales */
.grid-cuatro-columnas {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}

/* Modificación: segunda columna al doble de ancho (1fr, 2fr, 1fr, 1fr) */
.grid-asimetrico {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr 1fr;
  gap: 1.5rem;
}
```

* **Puntos clave:** Una unidad `fr` no es un porcentaje fijo; representa una parte proporcional del espacio libre sobrante disponible tras descontar anchos fijos y gaps.
* **Error frecuente:** Usar `25%` en lugar de `1fr`, lo que genera desbordamiento cuando se añade un `gap: 20px`.

---

### Solución U06.03 — Posicionamiento explícito por líneas numéricas

```css title="grid-lineas.css"
.grid-noticias {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, auto);
  gap: 1rem;
}

/* Noticia destacada: ocupa 2 columnas y 2 filas */
.noticia-destacada {
  grid-column: 1 / 3; /* Desde la línea 1 hasta la línea 3 (equivale a span 2) */
  grid-row: 1 / 3;    /* Desde la línea vertical 1 hasta la 3 */
}
```

* **Puntos clave:** En una cuadrícula de 3 columnas existen 4 líneas divisorias verticales numeradas del 1 al 4. La sintaxis `1 / 3` abarca las celdas comprendidas entre la línea 1 y la línea 3.
* **Error frecuente:** Confundir líneas con celdas y escribir `1 / 2` esperando que ocupe dos columnas.

---

### Solución U06.04 — Expansión a ancho completo con `grid-column: 1 / -1`

```css title="grid-fullwidth.css"
.banner-publicidad {
  grid-column: 1 / -1; /* Desde la primera línea hasta la última línea explícita */
  background-color: #fef08a;
  padding: 1.5rem;
  text-align: center;
}
```

* **Puntos clave:** El índice negativo `-1` hace referencia a la última línea de la cuadrícula explícita. Permite que el elemento abarque todo el ancho independientemente de si la cuadrícula tiene 3, 4 o 12 columnas.
* **Error frecuente:** Usar `-1` en cuadrículas implícitas generadas automáticamente por contenido dinámico sin columnas explícitas declaradas.

---

### Solución U06.05 — Maquetación semántica con `grid-template-areas`

```css title="holy-grail.css"
.app-layout {
  display: grid;
  grid-template-columns: 240px 1fr;
  grid-template-rows: 64px 1fr 60px;
  grid-template-areas:
    "header  header"
    "nav     main"
    "footer  footer";
  min-height: 100vh;
}

.app-header { grid-area: header; }
.app-nav    { grid-area: nav; }
.app-main   { grid-area: main; }
.app-footer { grid-area: footer; }
```

* **Puntos clave:** Proporciona un mapa visual directo de la página. Para dejar una celda vacía se utiliza un punto `.` en la matriz de cadenas (ej. `"nav ."`).
* **Error frecuente:** No tener el mismo número de palabras/celdas en cada fila de texto, lo que invalida toda la propiedad `grid-template-areas`.

---

### Solución U06.06 — Rejilla responsiva elástica con `auto-fit` y `minmax()`

```css title="grid-elastico.css"
.galeria-responsiva {
  display: grid;
  /* El patrón canónico responsivo sin media queries */
  grid-template-columns: repeat(auto-fit, minmax(min(260px, 100%), 1fr));
  gap: 1.5rem;
}
```

* **Puntos clave:** `auto-fit` calcula cuántas columnas de al menos 260px caben en el ancho actual; si sobra espacio, estira las columnas con `1fr`. La función `min(260px, 100%)` previene el desbordamiento horizontal en móviles estrechos de 240px.
* **Error frecuente:** Escribir decenas de media queries rígidas (`@media (min-width: 600px)`, `@media (min-width: 900px)`) para adaptar un catálogo de tarjetas cuando una sola línea de Grid lo resuelve de forma continua.

---

### Solución U06.07 — Comparativa práctica: `auto-fit` frente a `auto-fill`

```css title="autofit-vs-autofill.css"
/* auto-fill: Mantiene los slots vacíos reservados a la derecha */
.galeria-autofill {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}

/* auto-fit: Colapsa los slots vacíos a cero y estira las tarjetas existentes */
.galeria-autofit {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}
```

* **Puntos clave:** Si solo hay 2 elementos en una pantalla donde cabrían 5, `auto-fill` mantiene las 2 tarjetas midiendo 200px y deja 3 huecos vacíos a la derecha; `auto-fit` estira las 2 tarjetas para que ocupen el 50% de la pantalla cada una.
* **Error frecuente:** Usar `auto-fill` esperando que las tarjetas llenen toda la fila cuando hay pocos resultados de búsqueda.

---

### Solución U06.08 — Alineación bidimensional integral en Grid

```css title="grid-alineacion.css"
.panel-grid {
  display: grid;
  grid-template-columns: repeat(2, 250px);
  grid-template-rows: repeat(2, 180px);
  width: 800px;
  height: 600px;
  
  /* Alinea la cuadrícula de 500x360 dentro del contenedor de 800x600 */
  justify-content: center; /* Eje horizontal */
  align-content: center;   /* Eje vertical */
  
  /* Alinea el contenido de todos los elementos dentro de sus celdas de 250x180 */
  justify-items: center;
  align-items: center;
  gap: 1rem;
}

/* Widget individual que sobrescribe su alineación en su celda */
.widget-especial {
  justify-self: end;
  align-self: end;
}
```

* **Puntos clave:** Las propiedades con sufijo `-content` alinean el conjunto de pistas en el contenedor; las propiedades con `-items` o `-self` alinean elementos dentro de las celdas.
* **Error frecuente:** Confundir `justify-content` (mueve las columnas enteras) con `justify-items` (mueve el contenido dentro de la columna).

---

### Solución U06.09 — Cuadrícula asimétrica estilo "Bento Grid"

```css title="bento-grid.css"
.bento-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 180px;
  grid-auto-flow: dense; /* Empaquetado compacto: rellena huecos automáticamente */
  gap: 1rem;
}

/* Tarjeta principal dominante */
.bento-principal {
  grid-column: span 2;
  grid-row: span 2;
  background-color: #1e293b;
  color: #ffffff;
}

/* Tarjeta secundaria alargada */
.bento-alargada {
  grid-column: span 2;
  background-color: #f1f5f9;
}

/* Tarjetas estándar ocupan 1 celda por defecto */
.bento-item {
  border-radius: 12px;
  padding: 1.5rem;
}
```

* **Puntos clave:** `grid-auto-flow: dense` analiza el orden del DOM y, si un elemento grande deja un hueco libre en filas anteriores, coloca un elemento posterior más pequeño para aprovechar el espacio.
* **Error frecuente:** No usar `dense` y ver huecos en blanco vacíos e inexplicables en el layout.

---

### Solución U06.10 — Alineación de componentes hijos con `subgrid`

```css title="subgrid.css"
.grid-tarjetas {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.tarjeta {
  display: grid;
  grid-row: span 3;              /* La tarjeta abarca 3 filas del grid padre */
  grid-template-rows: subgrid;   /* Hereda las pistas de fila del padre */
  border: 1px solid #e2e8f0;
  padding: 1.5rem;
  border-radius: 8px;
}
```

* **Puntos clave:** Gracias a `subgrid`, las 3 cabeceras de las 3 tarjetas comparten la fila 1, los 3 cuerpos de texto comparten la fila 2 y los 3 botones comparten la fila 3, logrando una alineación perfecta sin importar las diferencias de longitud de texto.
* **Error frecuente:** Intentar anidar grids ordinarios creyendo que pueden coordinar sus alturas de fila con hermanos de otros contenedores sin `subgrid`.

---

## Soluciones: Unidad 07 — Flujo normal, multicolumna, tablas y display

### Solución U07.01 — Comportamiento y diferencias de `block`, `inline` e `inline-block`

```css title="displays.css"
/* 1. Block: Ocupa todo el ancho, inicia nueva línea, admite width, height y márgenes */
.caja-block {
  display: block;
  width: 250px;
  height: 80px;
  margin: 20px 0;
  background-color: #fee2e2;
}

/* 2. Inline: Fluye en la línea, ignora width, height y márgenes verticales */
.caja-inline {
  display: inline;
  width: 500px;  /* IGNORADO */
  height: 500px; /* IGNORADO */
  margin: 30px;  /* Solo se aplican margin-left y margin-right */
  background-color: #fef3c7;
}

/* 3. Inline-block: Fluye en la línea pero respeta width, height y todos los márgenes */
.caja-inline-block {
  display: inline-block;
  width: 140px;
  height: 60px;
  margin: 10px;
  background-color: #dcfce7;
}
```

* **Puntos clave:** `inline-block` ofrece lo mejor de ambos mundos para elementos como botones, avatares o badges en línea que requieren dimensiones y espaciado predecible.
* **Error frecuente:** Aplicar `height` y `margin-top` a un enlace `<a>` sin cambiar su display a `inline-block` o `flex`.

---

### Solución U07.02 — Ocultación visual y accesibilidad: `none` vs `hidden` vs `.sr-only`

```css title="a11y-ocultar.css"
/* 1. display: none -> Eliminado de la vista Y del lector de pantalla (No accesible) */
.oculto-total {
  display: none;
}

/* 2. visibility: hidden -> Invisible pero conserva su espacio en blanco en el layout */
.invisible-con-hueco {
  visibility: hidden;
}

/* 3. .sr-only -> Invisible para los ojos pero LEÍDO por tecnologías de asistencia */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

* **Puntos clave:** Para añadir textos explicativos accesibles (ej. etiquetas de iconos de lupa o cerrar), `.sr-only` es el estándar indiscutible de la industria recomendado por la W3C.
* **Error frecuente:** Usar `display: none` para ocultar etiquetas de formulario, dejando a personas ciegas sin información contextual del campo.

---

### Solución U07.03 — Desenvoltura estructural con `display: contents`

```css title="contents.css"
/* El formulario no genera caja propia; sus campos participan en el grid exterior */
.formulario-integrado {
  display: contents;
}
```

* **Puntos clave:** Al aplicar `display: contents`, el elemento contenedor no genera caja de renderizado (se ignoran sus paddings, bordes o fondos propios) y sus hijos directos pasan a comportarse como hijos directos del contenedor abuelo.
* **Error frecuente:** Aplicar `display: contents` en listas `<ul>` o `<ol>` en navegadores sin soporte completo, lo que provocaba que los lectores de pantalla dejaran de anunciar la lista semántica.

---

### Solución U07.04 — Creación de BFC con `display: flow-root`

```css title="flow-root.css"
/* Contenedor padre que encierra elementos flotantes sin hacks */
.articulo-con-float {
  display: flow-root; /* Crea un Block Formatting Context nativo */
  background-color: #f8fafc;
  padding: 1.5rem;
  border-radius: 8px;
}

.articulo-con-float img {
  float: left;
  margin-right: 1.5rem;
  margin-bottom: 0.5rem;
}
```

* **Puntos clave:** `display: flow-root` erradica la necesidad del viejo hack `clearfix` (`::after { content: ""; display: table; clear: both; }`) y contiene limpiamente los floats y colapsos de márgenes.
* **Error frecuente:** Usar `overflow: auto` o `overflow: hidden` como sustituto de BFC cuando `flow-root` fue creado expresamente para este propósito.

---

### Solución U07.05 — Texto periodístico con multicolumna CSS

```css title="multicolumna.css"
.texto-editorial {
  /* shorthand: column-count: 3; column-width: 250px; */
  columns: 3 250px;
  line-height: 1.6;
  text-align: justify;
}
```

* **Puntos clave:** Si la pantalla tiene más de 750px de ancho, se dibujarán 3 columnas; si el ancho se reduce por debajo de 500px, el navegador bajará automáticamente a 2 o 1 columna para asegurar que ninguna mida menos de 250px.
* **Error frecuente:** Declarar únicamente `column-count: 3`, lo que en pantallas móviles de 320px genera 3 columnas estrechas ilegibles con 2 palabras por línea.

---

### Solución U07.06 — Personalización de separadores y gutters en multicolumna

```css title="column-rule.css"
.articulo-separado {
  columns: 3 260px;
  column-gap: 2.5rem; /* Separación horizontal entre columnas */
  column-rule: 1px solid #cbd5e1; /* Línea divisoria elegante */
}
```

* **Puntos clave:** `column-rule` no ocupa espacio físico en el ancho total de las columnas; se dibuja en el centro del espacio reservado por `column-gap`.
* **Error frecuente:** Intentar añadir bordes laterales a párrafos (`p { border-right: 1px solid }`) para simular columnas, lo que produce líneas duplicadas y rotas.

---

### Solución U07.07 — Titulares transversales y control de cortes de párrafo

```css title="column-span.css"
/* Título que atraviesa todas las columnas de la página */
.titular-transversal {
  column-span: all;
  margin-block: 2rem;
  font-size: 2rem;
  text-align: center;
}

/* Tarjeta o imagen que no debe partirse entre dos columnas */
.tarjeta-destacada {
  break-inside: avoid; /* Previene cortes visuales a mitad de tarjeta */
  margin-bottom: 1.5rem;
  background-color: #f1f5f9;
  padding: 1rem;
}
```

* **Puntos clave:** `column-span: all` interrumpe el flujo multicolumna, divide el texto anterior y posterior en dos bloques y ocupa el 100% del ancho. `break-inside: avoid` es crucial también para optimizar estilos de impresión (`@media print`).
* **Error frecuente:** Olvidar `break-inside: avoid` y ver la mitad de una foto en la base de una columna y la otra mitad en la parte superior de la siguiente.

---

### Solución U07.08 — Estilizado accesible de tablas de datos

```css title="tabla-accesible.css"
.tabla-datos {
  width: 100%;
  border-collapse: collapse; /* Une los bordes adyacentes */
  font-family: system-ui, sans-serif;
}

.tabla-datos caption {
  caption-side: top;
  font-size: 1.25rem;
  font-weight: bold;
  text-align: left;
  padding-bottom: 0.75rem;
}

.tabla-datos th,
.tabla-datos td {
  padding: 12px 16px;
  border-bottom: 1px solid #e2e8f0;
}

.tabla-datos th {
  background-color: #f8fafc;
  font-weight: 600;
  text-align: left;
}
```

* **Puntos clave:** El elemento `<caption>` es obligatorio para accesibilidad WCAG y debe estilizarse con `caption-side`. `border-collapse: collapse` previene las líneas dobles antiguas de HTML4.
* **Error frecuente:** Quitar `<caption>` y colocar un simple `<h3>` encima de la tabla; los lectores de pantalla pierden la asociación del título con la estructura de datos.

---

### Solución U07.09 — Optimización de tablas con `table-layout: fixed`

```css title="tabla-fixed.css"
.tabla-optimizada {
  width: 100%;
  table-layout: fixed; /* El navegador no necesita esperar a descargar todas las filas */
  border-collapse: collapse;
}

/* Las columnas toman el ancho declarado en la primera fila */
.tabla-optimizada th:nth-child(1) { width: 120px; }
.tabla-optimizada th:nth-child(2) { width: 40%; }
.tabla-optimizada th:nth-child(3) { width: auto; }

/* Truncado limpio de texto en celdas fijas */
.tabla-optimizada td {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding: 10px;
}
```

* **Puntos clave:** Con `table-layout: fixed`, el motor de renderizado calcula la geometría examinando únicamente la cabecera `<thead>`, pintando la tabla de forma casi instantánea. Permite además aplicar `text-overflow: ellipsis`.
* **Error frecuente:** Usar `table-layout: auto` en tablas de miles de registros, provocando latencia de renderizado y saltos continuos mientras se descargan datos asíncronos.

---

### Solución U07.10 — Bandas cebradas, cabecera adhesiva y cifras numéricas tabulares

```css title="tabla-financiera.css"
.tabla-financiera {
  width: 100%;
  border-collapse: collapse;
}

/* Bandas cebradas para facilitar el seguimiento visual de filas largas */
.tabla-financiera tbody tr:nth-child(even) {
  background-color: #f8fafc;
}

/* Cabecera pegajosa en el scroll */
.tabla-financiera thead th {
  position: sticky;
  top: 0;
  background-color: #0f172a;
  color: #ffffff;
  z-index: 1;
}

/* Cifras numéricas monoespaciadas y alineadas a la derecha */
.col-moneda {
  text-align: right;
  font-variant-numeric: tabular-nums; /* Dígitos con idéntico ancho */
}
```

* **Puntos clave:** `font-variant-numeric: tabular-nums` garantiza que los dígitos '1' ocupen exactamente el mismo ancho horizontal que los '8', manteniendo comas y decimales en perfecta alineación vertical.
* **Error frecuente:** Centrar columnas de números en lugar de alinearlas a la derecha con cifras tabulares.

---

## Soluciones: Unidad 08 — Unidades, tipografía y colores

### Solución U08.01 — Configuración base de `rem` y espaciado proporcional

```css title="rem-escala.css"
/* Respetar el 100% de la configuración de accesibilidad del navegador */
html {
  font-size: 100%; /* Equivalente habitual a 16px */
}

/* Escala tipográfica basada en rem */
.texto-sm   { font-size: 0.875rem; } /* 14px */
.texto-base { font-size: 1rem; }     /* 16px */
.texto-lg   { font-size: 1.25rem; }  /* 20px */
.texto-xl   { font-size: 1.5rem; }   /* 24px */
.texto-2xl  { font-size: 2rem; }     /* 32px */
```

* **Puntos clave:** Fijar `html { font-size: 10px; }` (el viejo truco del 62.5% mal implementado) rompe el escalado si un usuario con baja visión tiene configurado su navegador a 24px base.
* **Error frecuente:** Utilizar píxeles fijos `px` en tipografías, ignorando las preferencias del sistema operativo.

---

### Solución U08.02 — El efecto compuesto del `em` vs la consistencia del `rem`

```css title="em-vs-rem.css"
/* Corrección: listas anidadas con rem para tamaño constante */
ul li {
  font-size: 1rem; /* 16px constante en todos los niveles de profundidad */
}

/* Uso virtuoso de em: padding de botón que escala con el tamaño de su fuente */
.btn-escalable {
  font-size: 1rem;
  padding: 0.5em 1em; /* Se recalcula si una clase secundaria cambia el font-size */
}

.btn-grande {
  font-size: 1.5rem; /* El padding crece automáticamente a 0.75rem / 1.5rem */
}
```

* **Puntos clave:** Con `font-size: 1.2em`, el nivel 1 mide 19.2px, el nivel 2 mide 23.04px y el nivel 3 mide 27.65px (efecto compuesto). En cambio, para paddings en botones o márgenes de encabezados, `em` es ideal para lograr proporcionalidad intrínseca.
* **Error frecuente:** Usar `em` para tamaños de fuente en componentes anidados profundos.

---

### Solución U08.03 — Unidades de viewport dinámicas en móviles: `dvh`, `svh` y `lvh`

```css title="viewport-dvh.css"
.hero-pantalla-completa {
  /* Fallback para navegadores antiguos */
  min-height: 100vh;
  /* Altura dinámica exacta adaptada a la barra de direcciones del móvil */
  min-height: 100dvh;
  display: flex;
  align-items: center;
  justify-content: center;
}
```

* **Puntos clave:** `100svh` toma como base la pantalla con la barra de navegación del navegador abierta; `100lvh` asume la barra contraída; `100dvh` se recalcula dinámicamente cuando el usuario desliza el dedo y la barra colapsa.
* **Error frecuente:** Usar únicamente `100vh` en móviles y ver que el botón inferior del formulario queda tapado por la barra de Chrome o Safari.

---

### Solución U08.04 — Funciones matemáticas: `calc()`, `min()` y `max()`

```css title="calc-math.css"
.contenedor-restringido {
  /* 100% menos 40px de márgenes, pero entre 300px y 1200px */
  width: min(max(calc(100% - 40px), 300px), 1200px);
  margin-inline: auto;
}

/* Sintaxis equivalente y más limpia usando clamp: */
.contenedor-clamp {
  width: clamp(300px, calc(100% - 40px), 1200px);
  margin-inline: auto;
}
```

* **Puntos clave:** Los operadores `+` y `-` en `calc()` requieren obligatoriamente espacios a ambos lados (`calc(100% - 40px)`). De lo contrario, el analizador lo interpreta como un valor negativo erróneo.
* **Error frecuente:** Escribir `calc(100%-40px)` sin espacios, haciendo que la declaración sea ignorada por el navegador.

---

### Solución U08.05 — Tipografía fluida continua con `clamp()`

```css title="clamp-fluido.css"
h1.titular-fluido {
  /*
    - Mínimo: 2rem (32px a 360px de viewport)
    - Valor preferido fluido: 1.14rem + 3.8vw
    - Máximo: 4rem (64px a 1200px de viewport)
  */
  font-size: clamp(2rem, 1.14rem + 3.8vw, 4rem);
  line-height: 1.15;
}
```

* **Puntos clave:** `clamp(MIN, PREFERRED, MAX)` escala la fuente de forma continua con la pantalla sin necesidad de saltos bruscos provocados por Media Queries.
* **Error frecuente:** Usar solo unidades `vw` directas (ej. `font-size: 5vw;`) sin límites, lo que hace el texto microscópico en relojes inteligentes o ridículamente gigante en televisores 4K.

---

### Solución U08.06 — Carga optimizada de tipografías con `@font-face` y `font-display`

```css title="font-face.css"
@font-face {
  font-family: "OpenSans";
  src: url("/fonts/OpenSans-Variable.woff2") format("woff2");
  font-weight: 300 800; /* Fuente variable con rango de pesos */
  font-style: normal;
  font-display: swap;   /* Muestra la fuente fallback hasta que termine la descarga */
}

body {
  font-family: "OpenSans", system-ui, -apple-system, sans-serif;
}
```

* **Puntos clave:** `font-display: swap` erradica el Flash of Invisible Text (FOIT), permitiendo al usuario empezar a leer el contenido inmediatamente con una tipografía del sistema. El formato WOFF2 ofrece la mejor compresión web.
* **Error frecuente:** Omitir la pila tipográfica de respaldo (*fallback*), dejando que el navegador elija fuentes serif imprevistas si la conexión de red falla.

---

### Solución U08.07 — Legibilidad avanzada: `line-height` relativo y `text-wrap`

```css title="text-wrap.css"
body {
  line-height: 1.6; /* Sin unidades: los hijos recalculan 1.6 x su propio font-size */
}

/* Equilibra visualmente las líneas en títulos de varias frases */
h1, h2, h3 {
  line-height: 1.2;
  text-wrap: balance;
}

/* Evita que quede una sola palabra aislada en la última línea de párrafos */
p {
  text-wrap: pretty;
}
```

* **Puntos clave:** Si se fija `line-height: 24px` en el `body`, un titular `h1` de 40px heredará una altura de línea de 24px, provocando que sus letras se aplasten y solapen. Un número sin unidad escala perfectamente.
* **Error frecuente:** Poner unidades a `line-height` en selectores generales.

---

### Solución U08.08 — El espacio de color moderno OKLCH frente a HEX/RGB/HSL

```css title="oklch.css"
:root {
  /* OKLCH: oklch(Luminosidad Croma Matiz) */
  --color-primario: oklch(55% 0.22 260); /* Azul vibrante */
  --color-exito:    oklch(65% 0.20 145); /* Verde con brillo perceptual equilibrado */
  --color-peligro:  oklch(60% 0.24 28);  /* Rojo */
}

/* Fallback con @supports para navegadores legacy */
@supports not (color: oklch(50% 0.2 0)) {
  :root {
    --color-primario: #2563eb;
    --color-exito:    #16a34a;
    --color-peligro:  #dc2626;
  }
}
```

* **Puntos clave:** En OKLCH, un 60% de luminosidad equivale al mismo brillo aparente para el ojo humano en cualquier color del círculo cromático, algo que no ocurre en HSL o RGB.
* **Error frecuente:** Confundir HSL con OKLCH y esperar que un amarillo y un azul con 50% de luminosidad en HSL tengan el mismo contraste sobre fondo blanco.

---

### Solución U08.09 — Variantes automáticas con `color-mix()`

```css title="color-mix.css"
:root {
  --color-marca: #2563eb;
}

.btn-marca {
  background-color: var(--color-marca);
  color: #ffffff;
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  cursor: pointer;
}

/* Hover: Oscurece automáticamente un 15% mezclando con negro en espacio oklab */
.btn-marca:hover {
  background-color: color-mix(in oklab, var(--color-marca) 85%, black);
}

/* Active: Oscurece un 30% */
.btn-marca:active {
  background-color: color-mix(in oklab, var(--color-marca) 70%, black);
}

/* Fondo tenue de alerta: 12% de la marca mezclado con blanco */
.alerta-info {
  background-color: color-mix(in oklab, var(--color-marca) 12%, white);
  color: var(--color-marca);
}
```

* **Puntos clave:** `color-mix()` elimina la necesidad de preprocesadores Sass para funciones como `darken()` o `lighten()`. Realiza la interpolación nativamente en el navegador.
* **Error frecuente:** Usar `srgb` como espacio de mezcla en lugar de `oklab` o `oklch`, lo que produce colores grisáceos o apagados en transiciones intermedias.

---

### Solución U08.10 — Sistema de Tokens con modo claro/oscuro y contraste WCAG

```css title="tokens-a11y.css"
:root {
  color-scheme: light dark;
  
  /* Tokens tema claro */
  --bg-canvas: #f8fafc;
  --bg-surface: #ffffff;
  --text-main: #0f172a;   /* Contraste 15.3:1 sobre superficie blanca (Supera AAA) */
  --text-muted: #475569;  /* Contraste 5.5:1 (Supera AA 4.5:1) */
  --border-color: #e2e8f0;
}

/* Conmutación automática a tema oscuro */
@media (prefers-color-scheme: dark) {
  :root {
    --bg-canvas: #090d16;
    --bg-surface: #1e293b;
    --text-main: #f8fafc;  /* Contraste 14.1:1 sobre superficie oscura */
    --text-muted: #94a3b8; /* Contraste 5.1:1 sobre superficie oscura */
    --border-color: #334155;
  }
}

body {
  background-color: var(--bg-canvas);
  color: var(--text-main);
}

.tarjeta {
  background-color: var(--bg-surface);
  border: 1px solid var(--border-color);
  padding: 1.5rem;
  border-radius: 8px;
}
```

* **Puntos clave:** El criterio WCAG 1.4.3 exige un ratio de contraste mínimo de 4.5:1 para texto normal frente a su fondo. Separar las superficies en tokens desacopla el diseño de las vistas.
* **Error frecuente:** Diseñar un modo oscuro invirtiendo ciegamente colores (`#000` fondo, `#fff` texto), produciendo fatiga visual y perdiendo jerarquía de elevación entre superficies.

---

## Soluciones: Unidad 09 — Fondos, imágenes y decoración

### Solución U09.01 — Configuración y control de imágenes de fondo

```css title="background-base.css"
.seccion-hero {
  /* Propiedades individuales: */
  background-color: #0f172a; /* Fondo de respaldo accesible si la imagen no carga */
  background-image: url("hero-bg.webp");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;

  /* Shorthand equivalente: */
  /* background: #0f172a url("hero-bg.webp") no-repeat center / cover; */
  
  color: #ffffff;
  padding: 4rem 2rem;
}
```

* **Puntos clave:** Al usar la sintaxis shorthand de `background`, el tamaño (`cover`) debe escribirse obligatoriamente precedido de una barra inclinada tras la posición: `center / cover`.
* **Error frecuente:** Olvidar declarar `background-color`, provocando que el texto blanco quede invisible sobre fondo blanco si la conexión falla o mientras la imagen se descarga.

---

### Solución U09.02 — Escala de fondo: `cover` frente a `contain`

```css title="cover-contain.css"
/* Banner hero: Debe llenar toda la caja sin dejar huecos en blanco */
.banner-hero {
  width: 400px;
  height: 300px;
  background: url("paisaje.jpg") no-repeat center;
  background-size: cover; /* Recorta márgenes sobrantes para cubrir el 100% */
}

/* Logotipo de patrocinador: Debe verse íntegro sin cortar ningún borde */
.logo-sponsor {
  width: 400px;
  height: 300px;
  background: url("logo.png") no-repeat center;
  background-size: contain; /* Ajusta la imagen dentro de la caja sin recortar */
}
```

* **Puntos clave:** `cover` garantiza cobertura visual completa sacrificando bordes de la imagen; `contain` garantiza visibilidad total de la imagen a costa de posibles espacios vacíos en los laterales.
* **Error frecuente:** Usar `background-size: 100% 100%`, lo que deforma y aplasta la relación de aspecto de la fotografía.

---

### Solución U09.03 — Degradados lineales y paradas de color (*color stops*)

```css title="linear-gradient.css"
/* Degradado suave continuo a 135 grados */
.cabecera-degradada {
  background: linear-gradient(135deg, #003366 0%, #7c3aed 40%, #ec4899 100%);
  color: #ffffff;
  padding: 3rem;
}

/* Botón con corte brusco (Hard Stops) para franjas nítidas */
.btn-bicolor {
  background: linear-gradient(to right, #2563eb 50%, #1e40af 50%);
  color: #ffffff;
  padding: 12px 24px;
  border: none;
  border-radius: 6px;
}
```

* **Puntos clave:** Cuando dos paradas de color consecutivas coinciden en el mismo porcentaje (ej. `50%` y `50%`), se genera una línea de corte nítida sin transición difuminada.
* **Error frecuente:** Omitir el ángulo o dirección en `linear-gradient` (por defecto el degradado va de arriba a abajo, `to bottom`).

---

### Solución U09.04 — Degradados radiales y cónicos

```css title="radial-conic.css"
/* Viñeta circular con foco de luz en el centro */
.fondo-vineta {
  width: 300px;
  height: 300px;
  background: radial-gradient(circle at center, #38bdf8 0%, #0f172a 75%);
}

/* Gráfico de tarta en CSS puro: 75% verde de éxito y 25% gris */
.grafico-progreso {
  width: 160px;
  height: 160px;
  border-radius: 50%;
  background: conic-gradient(#22c55e 0% 75%, #e2e8f0 75% 100%);
}
```

* **Puntos clave:** `conic-gradient()` rota los ángulos alrededor de un eje central (de 0deg a 360deg o de 0% a 100%), permitiendo crear medidores circulares de progreso sin Canvas ni SVG.
* **Error frecuente:** Confundir `radial-gradient` (expansión desde el centro hacia afuera) con `conic-gradient` (rotación circular tipo reloj).

---

### Solución U09.05 — Fondos multicapa: imagen con máscara de oscurecimiento

```css title="multicapa.css"
.hero-legible {
  /* La primera capa declarada se pinta por encima */
  background-image:
    linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.65)), /* Capa 1: Filtro oscuro */
    url("foto-concurrida.jpg");                                  /* Capa 2: Fotografía */
  background-size: auto, cover;
  background-position: center, center;
  background-repeat: no-repeat;
  color: #ffffff; /* Texto perfectamente legible */
  padding: 5rem 2rem;
}
```

* **Puntos clave:** Al colocar un degradado semitransparente como primera capa de `background-image`, se oscurece la fotografía automáticamente sin requerir pseudo-elementos adicionales (`::before`).
* **Error frecuente:** Poner la imagen en primer lugar y el degradado en segundo lugar; la imagen tapará por completo al degradado.

---

### Solución U09.06 — Control de imágenes reemplazadas con `object-fit` y `aspect-ratio`

```css title="object-fit.css"
.avatar-perfil {
  width: 140px;
  aspect-ratio: 1 / 1;      /* Fuerza relación cuadrada perfecta */
  object-fit: cover;        /* Evita que la foto se estire o deforme */
  object-position: center top; /* Prioriza enfocar la cara en el recorte */
  border-radius: 50%;
  border: 3px solid #3b82f6;
}

.tarjeta-video {
  width: 100%;
  aspect-ratio: 16 / 9;     /* Reserva el espacio antes de que el video cargue */
  object-fit: cover;
}
```

* **Puntos clave:** `aspect-ratio` reserva el espacio físico en pantalla antes de que el archivo gráfico descargue, previniendo el salto brusco de diseño medido por la métrica Core Web Vital CLS.
* **Error frecuente:** Fijar `height: 100%` en imágenes sin `object-fit`, provocando que las imágenes se aplasten horizontalmente.

---

### Solución U09.07 — Bordes elípticos y formas orgánicas complejas

```css title="border-radius-organico.css"
/* Botón en forma de píldora perfecta que se adapta a cualquier contenido */
.btn-pildora {
  border-radius: 9999px;
  padding: 10px 28px;
  background-color: #2563eb;
  color: #ffffff;
}

/* Forma orgánica asimétrica */
.forma-organica {
  width: 220px;
  height: 220px;
  background: linear-gradient(45deg, #f43f5e, #fb923c);
  /* Radios horizontales / Radios verticales */
  border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
}
```

* **Puntos clave:** La barra diagonal `/` en `border-radius` separa las curvaturas del eje X de las del eje Y para cada una de las cuatro esquinas del rectángulo.
* **Error frecuente:** Usar píxeles pequeños como `border-radius: 20px` en botones anchos, lo que no produce una píldora auténtica sino un rectángulo con esquinas redondeadas.

---

### Solución U09.08 — Recorte vectorial de elementos con `clip-path`

```css title="clip-path.css"
/* Cabecera con corte diagonal dinámico */
.cabecera-diagonal {
  background-color: #0f172a;
  color: #ffffff;
  padding: 4rem 2rem 6rem;
  /* Polígono: (X Y, X Y, X Y, X Y) */
  clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);
}

/* Insignia en forma de flecha */
.flecha-etiqueta {
  display: inline-block;
  background-color: #3b82f6;
  color: #ffffff;
  padding: 8px 24px 8px 12px;
  clip-path: polygon(0% 0%, 80% 0%, 100% 50%, 80% 100%, 0% 100%);
}
```

* **Puntos clave:** `clip-path` recorta el elemento gráficamente sin afectar al flujo del documento. Fuera del área visible recortada no se disparan eventos de ratón (`hover` o clics).
* **Error frecuente:** Usar imágenes PNG transparentes gigantes o transformaciones de rotación para crear cortes diagonales simples.

---

### Solución U09.09 — Efecto de cristal esmerilado con `backdrop-filter` (*Glassmorphism*)

```css title="glassmorphism.css"
.tarjeta-cristal {
  background-color: rgba(255, 255, 255, 0.25); /* Fondo blanco semitransparente */
  backdrop-filter: blur(12px) saturate(180%);   /* Desenfoca el fondo posterior */
  -webkit-backdrop-filter: blur(12px) saturate(180%); /* Safari */
  border: 1px solid rgba(255, 255, 255, 0.3);   /* Simula el bisel del cristal */
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
  color: #1e293b;
}
```

* **Puntos clave:** Si el fondo del elemento es totalmente opaco (`#ffffff`), el `backdrop-filter` no tendrá ningún efecto porque el propio fondo tapa la luz difusa que viene de atrás.
* **Error frecuente:** Confundir `filter: blur()` con `backdrop-filter: blur()`. `filter` emborrona el propio texto y contenido de la tarjeta haciéndola ilegible.

---

### Solución U09.10 — Comparativa de sombras: `box-shadow` frente a `filter: drop-shadow()`

```css title="drop-shadow.css"
/* Imagen PNG transparente o SVG de una estrella o icono */
.icono-estrella {
  /* box-shadow generaría un rectángulo cuadrado feo alrededor de la caja */
  /* drop-shadow proyecta la sombra silueteando la estrella real: */
  filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.25));
}

/* Bocadillo de diálogo con flecha creada mediante ::after */
.bocadillo-dialogo {
  position: relative;
  background-color: #ffffff;
  padding: 1rem;
  border-radius: 8px;
  /* Unifica la sombra de la caja y del triángulo ::after en una sola silueta: */
  filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.1));
}
```

* **Puntos clave:** `filter: drop-shadow()` evalúa la máscara alfa del elemento y de sus pseudo-elementos, unificando sus sombras. `box-shadow` solo conoce cajas rectangulares.
* **Error frecuente:** Intentar usar el cuarto parámetro (spread) o `inset` dentro de `drop-shadow()`; la especificación de filtros no los admite.

---

## Soluciones: Unidad 10 — Diseño responsivo y Container Queries

### Solución U10.01 — El meta viewport y el factor de escala en dispositivos móviles

```html title="viewport-head.html"
<head>
  <meta charset="UTF-8">
  <!-- Configuración estándar y accesible del viewport móvil -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Diseño Responsivo</title>
</head>
```

* **Puntos clave:** `width=device-width` hace que el viewport coincida con el ancho de la pantalla en píxeles CSS independientes del dispositivo. `initial-scale=1.0` establece una relación 1:1 entre píxeles CSS y píxeles del dispositivo.
* **Error frecuente:** Añadir `user-scalable=no` o `maximum-scale=1.0` para "fijar" la aplicación, impidiendo que usuarios con problemas de visión puedan hacer zoom, lo que viola directamente el criterio WCAG 1.4.4.

---

### Solución U10.02 — Filosofía Mobile-First con Media Queries `@media`

```css title="mobile-first.css"
/* 1. ESTILOS BASE: Móviles (pantallas pequeñas) */
.tarjeta-info {
  display: flex;
  flex-direction: column;
  text-align: center;
  padding: 1rem;
  background-color: #ffffff;
}

/* 2. MEJORA PROGRESIVA: A partir de 768px (Tablets y Escritorio) */
@media (min-width: 768px) {
  .tarjeta-info {
    flex-direction: row;
    text-align: left;
    align-items: center;
    padding: 2rem;
  }
}
```

* **Puntos clave:** En Mobile-First se redacta primero el diseño más sencillo y ligero. Las consultas `@media (min-width: ...)` añaden complejidad solo para dispositivos con pantallas más capaces, ahorrando trabajo a dispositivos móviles.
* **Error frecuente:** Trabajar en Desktop-First con `@media (max-width: ...)` y pasarse horas "deshaciendo" estilos de escritorio para que encajen en el móvil.

---

### Solución U10.03 — Sintaxis moderna de rango en Media Queries

```css title="range-syntax.css"
/* Sintaxis antigua y verbosa: */
/* @media (min-width: 600px) and (max-width: 1024px) { ... } */

/* Sintaxis moderna de rango (Media Queries Level 4): */
@media (600px <= width <= 1024px) {
  .sidebar {
    width: 280px;
  }
}

/* Consulta directa para móviles estrechos (< 768px): */
@media (width < 768px) {
  .menu-movil {
    display: block;
  }
}
```

* **Puntos clave:** La sintaxis matemática de rango (`<=`, `<`) es soportada en todos los navegadores modernos y evita el clásico problema de coincidencia límite entre `767px` y `768px`.
* **Error frecuente:** Olvidar que los operadores pueden encadenar tanto el valor mínimo como el máximo en una sola expresión.

---

### Solución U10.04 — Menú de navegación responsivo adaptable

```css title="nav-responsive.css"
/* Base: Móvil apilado */
.menu-nav {
  display: flex;
  flex-direction: column;
  width: 100%;
  padding: 0;
  margin: 0;
  list-style: none;
}

.menu-nav a {
  display: block;
  /* Área táctil mínima de 44x44px según WCAG 2.5.5 / 2.5.8 */
  min-height: 44px;
  padding: 12px 16px;
  text-decoration: none;
  color: #1e293b;
  border-bottom: 1px solid #e2e8f0;
}

/* Escritorio: Barra horizontal limpia */
@media (min-width: 768px) {
  .menu-nav {
    flex-direction: row;
    width: auto;
    gap: 1.5rem;
  }

  .menu-nav a {
    min-height: auto;
    border-bottom: none;
    padding: 8px 12px;
  }
}
```

* **Puntos clave:** Garantizar un área de pulsación de al menos 44x44px en móviles previene toques erróneos accidentales.
* **Error frecuente:** Poner enlaces diminutos en móvil que requieren que el usuario haga zoom para poder acertar con el dedo.

---

### Solución U10.05 — Cuadrícula responsiva por puntos de ruptura (*Breakpoints*)

```css title="grid-breakpoints.css"
.catalogo-grid {
  display: grid;
  grid-template-columns: 1fr; /* Móvil: 1 columna */
  gap: 12px;
}

/* Tablet vertical: 2 columnas */
@media (min-width: 576px) {
  .catalogo-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
  }
}

/* Laptop / Tablet horizontal: 3 columnas */
@media (min-width: 768px) {
  .catalogo-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
  }
}

/* Escritorio grande: 4 columnas */
@media (min-width: 1200px) {
  .catalogo-grid {
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
  }
}
```

* **Puntos clave:** La jerarquía Mobile-First escala limpiamente de menor a mayor ancho sin colisiones entre reglas.
* **Error frecuente:** Usar breakpoints arbitrarios basados en marcas de teléfonos concretos (ej. `375px`, `414px`) en vez de puntos de quiebre basados en el contenido.

---

### Solución U10.06 — Adaptación a capacidades de puntero: `@media (hover: hover)`

```css title="hover-pointer.css"
.tarjeta-interactiva {
  border: 1px solid #e2e8f0;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

/* Solo se aplica en dispositivos con puntero fino (ratón) que admiten hover real */
@media (hover: hover) and (pointer: fine) {
  .tarjeta-interactiva:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    border-color: #3b82f6;
  }
}

/* Foco siempre accesible para navegación por teclado en cualquier dispositivo */
.tarjeta-interactiva:focus-visible {
  outline: 3px solid #3b82f6;
}
```

* **Puntos clave:** En móviles táctiles, un `:hover` obliga al usuario a tocar dos veces (el primer toque dispara el hover y el segundo abre el enlace). Aislar el hover con `(hover: hover)` erradica este bug.
* **Error frecuente:** Asumir que "pantalla grande = ratón". Un iPad Pro de 12.9" tiene pantalla grande pero no tiene ratón por defecto; un portátil convertible táctil tiene ambas cosas.

---

### Solución U10.07 — Respeto a preferencias de accesibilidad: `@media (prefers-reduced-motion)`

```css title="reduced-motion.css"
.tarjeta-animada {
  transition: transform 0.3s ease, background-color 0.3s ease;
}

.tarjeta-animada:hover {
  transform: translateY(-8px);
}

/* Desactiva animaciones si el usuario lo configuró en el sistema operativo */
@media (prefers-reduced-motion: reduce) {
  .tarjeta-animada {
    transition: none; /* Sin movimiento */
  }

  .tarjeta-animada:hover {
    transform: none; /* Sin desplazamiento físico */
    background-color: #f1f5f9; /* Sustituido por cambio estático sutil */
  }
}
```

* **Puntos clave:** Personas con trastornos vestibulares pueden sufrir náuseas y mareos reales ante animaciones continuas o desplazamientos bruscos en pantalla (criterio WCAG 2.3.3).
* **Error frecuente:** Ignorar `prefers-reduced-motion` en aplicaciones con efectos parallax o transiciones pesadas.

---

### Solución U10.08 — Introducción a Container Queries: contexto de contenedor

```css title="container-query-def.css"
/* El elemento que contendrá al componente se declara como contenedor de consulta */
.envoltorio-tarjeta {
  container-type: inline-size;
  container-name: card-container;
}
```

* **Puntos clave:** `container-type: inline-size` monitoriza las dimensiones de su propio ancho en línea. No debe usarse `size` completo a menos que se fije una altura estricta, para evitar bucles infinitos donde el contenido altera la altura del contenedor y esta altera el contenido.
* **Error frecuente:** Aplicar `@container` sobre un elemento sin haber declarado previamente `container-type` en alguno de sus ancestros.

---

### Solución U10.09 — El componente modular autónomo con `@container`

```css title="tarjeta-modular.css"
.tarjeta-producto {
  display: flex;
  flex-direction: column; /* Vista vertical por defecto cuando el contenedor es estrecho */
  gap: 1rem;
  background-color: #ffffff;
  padding: 1rem;
  border-radius: 8px;
}

.tarjeta-producto .img {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}

/* Cuando el CONTENEDOR (no el viewport) mide 400px o más: */
@container card-container (min-width: 400px) {
  .tarjeta-producto {
    flex-direction: row; /* Pasa a vista horizontal automáticamente */
    align-items: center;
  }

  .tarjeta-producto .img {
    width: 40%;
    aspect-ratio: 1 / 1;
  }

  .tarjeta-producto .info {
    width: 60%;
  }
}
```

* **Puntos clave:** La misma tarjeta puede colocarse en una columna principal de 1200px (mostrándose horizontal) o en un sidebar de 300px (mostrándose vertical) simultáneamente en la misma pantalla sin requerir clases modificadoras ni media queries globales.
* **Error frecuente:** Intentar usar Media Queries para componentes modulares; las Media Queries solo conocen el viewport completo de la ventana del navegador.

---

### Solución U10.10 — Tipografía y espaciado fluido con unidades de contenedor (`cqw`)

```css title="cqw-widget.css"
.widget-clima-wrap {
  container-type: inline-size;
}

.widget-clima {
  background: linear-gradient(135deg, #0284c7, #0369a1);
  color: #ffffff;
  border-radius: clamp(8px, 2cqw, 20px);
  padding: clamp(1rem, 4cqw, 2.5rem);
}

.widget-temperatura {
  /* Escala fluidamente entre 1.5rem y 4rem en función del ANCHO DEL WIDGET */
  font-size: clamp(1.5rem, 8cqw, 4rem);
  font-weight: 800;
  line-height: 1;
}

.widget-ciudad {
  font-size: clamp(0.9rem, 3cqw, 1.5rem);
  opacity: 0.9;
}
```

* **Puntos clave:** `1cqw` equivale al 1% del ancho del contenedor más cercano con `container-type`. Si el widget se redimensiona dentro de un layout elástico de Grid, todos sus textos e iconos escalan en perfecta armonía con el espacio disponible.
* **Error frecuente:** Usar `vw` para componentes internos de una página; `vw` depende de la ventana total y provocará que el widget se vea gigantesco aunque esté confinado en una columna estrecha.
