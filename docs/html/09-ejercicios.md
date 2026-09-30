---
icon: lucide/pencil
title: "HTML 09 - Ejercicios"
description: "10 ejercicios prácticos de HTML5 por niveles, con enunciado y pista."
modulo: "LMH (0373) / DIW (0615) / DI (0488)"
unidad: 9
fecha: "2026-09-29"
---

# HTML 09 — Ejercicios prácticos

Diez retos de semántica, tablas, formularios HTML5, multimedia y accesibilidad. Resuélvelos en orden y compara después tu trabajo con [Ver soluciones](10-ejercicios-soluciones.md).

!!! note "Cómo trabajar"

    - **Intenta antes de mirar**: entrega una versión tuya de cada ejercicio y solo después consulta la solución.
    - **Valida siempre** en <https://validator.w3.org/>: que el navegador lo muestre no significa que esté bien.
    - **Pruébalo con teclado y lector de pantalla** donde aplique (menús, tablas, formularios, avisos).
    - **No toques el CSS**: si el aspecto visual cambia, es que has roto la estructura.

!!! info "Cómo están organizados los ejercicios"

    Cada ejercicio indica su **nivel** y el **capítulo** del que parte: empieza por los **básicos** y sube de nivel cuando los valides sin errores. Si alguno te bloquea, repasa antes la teoría de ese capítulo y vuelve a intentarlo.

## Ejercicio 1 — Desmontando la "divitis"

**Nivel:** básico · **Capítulo:** [07 — Estructura semántica y ARIA](07-estructura-semantica-y-aria.md)

**Enunciado**

La página se ve bien, pero todo son `<div>`: nadie sabe qué es cabecera, menú o pie. Dale significado sin cambiar una sola palabra.

**Código inicial**

```html title="ejercicio-1-inicial.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi Página Simple</title>
</head>
<body>
  <div id="cabecera">
    <h1>Bienvenido a mi Web</h1>
    <div class="menu">
      <ul>
        <li><a href="#">Inicio</a></li>
        <li><a href="#">Sobre Nosotros</a></li>
        <li><a href="#">Contacto</a></li>
      </ul>
    </div>
  </div>
  <div id="contenido-principal">
    <p>Este es el contenido principal de la página.</p>
    <p>Aquí podríamos hablar de muchos temas interesantes.</p>
  </div>
  <div id="pie-de-pagina">
    <p>&copy; 2026 Mi Web</p>
  </div>
</body>
</html>
```

**Tarea:**

- Sustituye `div#cabecera` por la cabecera de página y `div.menu` por un `<nav>`.
- Sustituye `div#contenido-principal` por el contenido principal y `div#pie-de-pagina` por el pie.
- Conserva el `<h1>`, la `<ul>` y los `<p>` intactos: **solo cambian los contenedores**.
- Verifica en las herramientas de desarrollo que la ==jerarquía== es correcta y el texto no varía.

**Pista:** son cuatro etiquetas de bloque de HTML5 y ninguna necesita atributos.

## Ejercicio 2 — Artículo semántico

**Nivel:** básico · **Capítulo:** [02 — Texto y semántica](02-texto-y-semantica.md)

**Enunciado**

Una entrada de blog está en `<div>` planos y la fecha es texto suelto. Conviértela en un artículo con secciones internas y fecha legible también para la máquina.

**Código inicial**

```html title="ejercicio-2-inicial.html"
<body>
  <div>
    <h1>El Oro Líquido de Andalucía</h1>
    <p>Por Juan Pérez - 10 de Junio de 2026</p>
  </div>
  <div>
    <p>Andalucía es la cuna del aceite de oliva, un producto esencial en la dieta mediterránea.</p>
    <h2>Variedades Principales</h2>
    <ul>
      <li>Picual</li>
      <li>Hojiblanca</li>
      <li>Arbequina</li>
    </ul>
  </div>
  <div>
    <h3>Recetas Populares</h3>
    <ul>
      <li>Salmorejo cordobés</li>
      <li>Gazpacho andaluz</li>
    </ul>
  </div>
  <div>
    <p>Más información en nuestra web.</p>
  </div>
</body>
```

**Tarea:**

- Envuelve todo en un `<article>` con `<header>` interno para título y autor.
- Marca la fecha con `<time datetime="2026-06-10">` (==formato ISO== en el atributo).
- Agrupa "Variedades" y "Recetas" en dos `<section>`, cada una con su encabezado.
- Cierra el artículo con un `<footer>` para "Más información...".
- **Un solo `h1`** y sin saltos de encabezado (`h1` → `h3`).

**Pista:** `<section>` siempre lleva ==encabezado==; si no lo lleva, no es una sección.

## Ejercicio 3 — Portafolio semántico

**Nivel:** básico/medio · **Capítulo:** [07 — Estructura semántica y ARIA](07-estructura-semantica-y-aria.md)

**Enunciado**

Monta tu portafolio: cabecera con menú, zona principal con proyectos, barra lateral de contacto y pie. Partes de este esqueleto casi vacío.

**Código inicial**

```html title="ejercicio-3-inicial.html" hl_lines="2 4"
<body>
  <header>
    <h1>Portafolio de [Tu Nombre]</h1>
    <nav><!-- menú: Inicio, Proyectos, Contacto --></nav>
  </header>
  <main>
    <section id="inicio"><!-- presentación --></section>
    <section id="proyectos"><!-- proyectos --></section>
  </main>
  <aside><!-- contacto --></aside>
  <footer><!-- derechos de autor --></footer>
</body>
```

**Tarea:**

- Completa el `<nav>` con una `<ul>` de tres enlaces a ==fragmentos== (`#inicio`, `#proyectos`, `#contacto`).
- Crea tres `<article>` de proyecto con `h3`, párrafo y enlace "Ver proyecto".
- Añade a cada proyecto una imagen con `src`, **`alt` descriptivo** y `width`/`height`.
- En el `<aside>`, pon `<h3>Contacto</h3>`, un `mailto:` y dos enlaces con `target="_blank" rel="noopener"`.
- Envuelve el avatar en `<figure>` con `<figcaption>`.
- Debe haber **un solo `<main>`** y todos los `id` referenciados deben existir.

**Pista:** un enlace `#proyectos` no recarga: apunta al `id` de la sección.

## Ejercicio 4 — Noticia completa con detalles

**Nivel:** medio · **Capítulo:** [02 — Texto y semántica](02-texto-y-semantica.md)

**Enunciado**

La noticia de la conferencia de IA en Sevilla no distingue abreviaturas, no marca citas, no legenda la imagen y mete los datos duros en un párrafo. Enriquecéla.

**Código inicial**

```html title="ejercicio-4-inicial.html" hl_lines="2 4"
<main>
  <article>
    <h2>Conferencia Internacional de IA en Sevilla</h2>
    <p>Publicado por Laura García - 5 de Junio de 2026</p>
    <img src="conferencia.jpg" alt="Sala llena durante la conferencia">
    <p>Sevilla acogerá la Conferencia Internacional de Inteligencia Artificial.
    "La tecnología debe estar al servicio de las personas", afirmó la directora.
    Cuenta con el apoyo de la agencia andaluza de innovación (ANDA).</p>
    <h3>Datos del evento</h3>
    <p>Del 16 al 18 de Junio de 2026 · 48 ponencias · 1200 asistentes.</p>
    <footer><p>Comparte este evento: #IASevilla2026</p></footer>
  </article>
</main>
```

**Tarea:**

- Añade un `<header>` interno con el `h2`, el autor y la fecha en `<time datetime="2026-06-05">`.
- Convierte la imagen en `<figure>` con un `<figcaption>` **distinto del `alt`**.
- Marca "IA" con `<abbr title="Inteligencia Artificial">` y "ANDA" con su sigla completa.
- Extrae la frase de la directora a un `<blockquote>` con `<cite>`.
- Pasa "Datos del evento" a `<table>` con `<caption>`, `<th scope="col">` y fila en `<tfoot>`.
- Usa dos `<time>` con ==fecha ISO== para el rango del 16 al 18 de junio.

**Pista:** ==`scope`== es lo que permite anunciar de qué columna habla cada celda.

## Ejercicio 5 — Perfil de usuario con múltiples secciones

**Nivel:** medio · **Capítulo:** [07 — Estructura semántica y ARIA](07-estructura-semantica-y-aria.md)

**Enunciado**

En "Mi Perfil" conviven datos editables, actividad reciente, preferencias y una zona lateral de acciones. Deben quedar bien jerarquizados para saltar de sección en sección.

**Código inicial**

```html title="ejercicio-5-inicial.html"
<body>
  <header>
    <h1>Mi Plataforma Andalucía</h1>
    <nav><!-- Dashboard, Mi Perfil, Mensajes, Cerrar Sesión --></nav>
  </header>
  <main>
    <div class="perfil">
      <h1>Mi Perfil de Usuario</h1>
      <div class="datos"><!-- datos personales --></div>
      <div class="actividad"><!-- actividad reciente --></div>
      <div class="preferencias"><!-- preferencias --></div>
    </div>
  </main>
  <div class="lateral"><!-- acciones rápidas --></div>
  <footer><p>&copy; 2026 Mi Plataforma Andalucía</p></footer>
</body>
```

**Tarea:**

- Los tres `<div>` internos pasan a `<section>` con `h2`; el contenedor, a `<section id="perfil">` con `<header>`.
- Crea un `<form>` con ==`<fieldset>`==/`<legend>` y `label for/id` en todos los campos (nombre, `email`, `tel`).
- En "Actividad Reciente", usa una `<ol>` con `<time datetime="...">` en cada entrada.
- En "Preferencias", añade otro `<form>` con `checkbox` y `<select>`, todos con ==etiqueta==.
- Convierte `div.lateral` en `<aside>` con `<h3>` y lista de enlaces.
- **Un solo `h1`** visible y los `h2` sin saltos de nivel.

**Pista:** si al hacer clic en el texto el foco salta a su campo, el `for` está bien.

## Ejercicio 6 — Procesamiento de vídeo con canvas

**Nivel:** avanzado · **Capítulo:** [04 — Multimedia](04-multimedia.md)

**Enunciado**

El `<video>` será la fuente de píxeles y el `<canvas>` un render paralelo: muestra el clip de un olivar en Jaén junto a su versión en escala de grises, fotograma a fotograma.

**Código inicial**

```html title="ejercicio-6-inicial.html"
<main class="contenedor-multimedia">
  <figure>
    <!-- Vídeo con source mp4, controls, muted, loop y crossorigin -->
    <figcaption>Entrada: Vídeo Original</figcaption>
  </figure>
  <figure>
    <canvas id="canvasFiltrado" width="400" height="225"></canvas>
    <figcaption>Salida: Filtro Escala de Grises</figcaption>
  </figure>
</main>
<script src="script.js"></script>
```

**Tarea:**

- Completa el `<video>` con `<source src="video_jaen.mp4" type="video/mp4">`, ==texto de respaldo== y `controls`, `muted`, `loop`, `autoplay`, `crossorigin="anonymous"`.
- Con `getContext('2d', { willReadFrequently: true })` obtén el contexto de dibujo.
- Escribe `procesarFrame()`: `drawImage` → `getImageData` → luminancia `0.2126*R + 0.7152*G + 0.0722*B` recorriendo el array **de 4 en 4** → `putImageData` → `requestAnimationFrame`.
- Lanza el bucle en el evento `play` y no trabajes con el vídeo ==en pausa==.
- Responde por escrito:
    1. ¿Por qué el `<canvas>` está vacío al cargar la página?
    2. ¿Por qué el bucle avanza de 4 en 4?
    3. ¿Qué pierdes al cambiar `requestAnimationFrame` por `setInterval(fn, 16)`?
    4. Si usas solo el canal verde como gris, ¿qué objetos se verán negros?
- **Mini reto:** un botón que alterne entre escala de grises y el fotograma original sin recargar.

**Pista:** si `getImageData` lanza un error de seguridad, revisa `crossorigin` del vídeo.

## Ejercicio 7 — Formulario de matrícula

**Nivel:** medio · **Capítulo:** [06 — Formularios HTML5](06-formularios-html5.md)

**Enunciado**

El formulario de matrícula es texto plano sin validar: se envían correos vacíos y fechas imposibles. Aprovecha la validación nativa de HTML5 para no depender de JavaScript.

**Código inicial**

```html title="ejercicio-7-inicial.html"
<form action="/matricula" method="post">
  <p>Nombre: <input type="text" name="nombre"></p>
  <p>Correo: <input type="text" name="email"></p>
  <p>Fecha de nacimiento: <input type="text" name="nacimiento"></p>
  <p>Edad: <input type="text" name="edad"></p>
  <p>NIF: <input type="text" name="nif"></p>
  <p>Ciclo: <input type="text" name="ciclo"></p>
  <input type="submit" value="Enviar matrícula">
</form>
```

**Tarea:**

- Agrupa los campos en dos `<fieldset>` con `<legend>`: "Datos del estudiante" y "Datos académicos".
- Asocia cada campo con `<label for>`: **ningún input sin etiqueta visible**.
- Cambia los tipos a `email`, `date` y `number` con `min="16"` y `max="99"`; el NIF sigue en `text`.
- Marca `required` los ==obligatorios== (nombre, correo, ciclo) y añade `autocomplete`.
- Restringe el NIF con `pattern="[0-9]{8}[A-Za-z]"` y explica el formato en el `title`.
- Crea ==`<datalist id="ciclos">`== con `DAM`, `DAW`, `SMR` y `IFCT-videojuegos` y asócialo con `list`.
- Añade un `<textarea rows="4">` para observaciones y un `<button type="submit">`.

**Pista:** `pattern` valida una expresión regular sobre todo el valor; el `title` explica el error.

## Ejercicio 8 — Horario de clase accesible

**Nivel:** medio · **Capítulo:** [05 — Tablas](05-tablas.md)

**Enunciado**

El horario semanal se lee mal con lector de pantalla: no hay pie de tabla, las celdas de encabezado no están declaradas, los huecos obligan a contar columnas a ciegas y falta el total de horas.

**Código inicial**

```html title="ejercicio-8-inicial.html"
<table>
  <tr>
    <td>Hora</td>
    <td>Lunes</td>
    <td>Miércoles</td>
    <td>Viernes</td>
  </tr>
  <tr>
    <td>08:00-09:00</td>
    <td>LMH</td>
    <td>DIW</td>
    <td>DI</td>
  </tr>
  <tr>
    <td>09:00-10:00</td>
    <td>LMH</td>
    <td colspan="2">Hora de patrocinio</td>
  </tr>
</table>
```

**Tarea:**

- Envuelve la tabla en un `<figure>` y añade un `<caption>` visible con el título del horario.
- Pasa la primera fila a `<thead>` con `<th scope="col">` y la primera columna de cada fila a `<th scope="row">`.
- Separa el cuerpo en `<tbody>` y añade un `<tfoot>` con el total de horas semanales.
- Revisa los huecos: contando `colspan`, todas las filas deben tener ==el mismo número de celdas==.
- Usa `<colgroup>`/`<col>` para dar ancho fijo a la columna de horas.
- Valida y comprueba con el lector de pantalla que **cada celda anuncia columna y fila**.

**Pista:** en `<td>` va el dato; en `<th scope>` va lo que *describe* ==fila o columna==.

## Ejercicio 9 — Galería accesible

**Nivel:** medio · **Capítulo:** [03 — Enlaces y recursos](03-enlaces-y-recursos.md) · también [04 — Multimedia](04-multimedia.md)

**Enunciado**

La galería del ciclo tiene enlaces "ver imagen" sueltos, imágenes sin `alt` útil, ninguna versión adaptativa y un vídeo sin subtítulos ni portada. Hazla apta para conexiones lentas y lector de pantalla.

**Código inicial**

```html title="ejercicio-9-inicial.html"
<main id="galeria">
  <h1>Galería del ciclo</h1>
  <div>
    <img src="taller-800.jpg">
    <p>Alumnos en el taller de electrónica</p>
    <a href="ver-imagen.html">Ver imagen</a>
  </div>
  <div>
    <video src="promo.mp4" controls></video>
    <p>Vídeo promocional del ciclo</p>
  </div>
</main>
```

**Tarea:**

- Convierte cada bloque en `<figure>` con `<figcaption>` y elimina los enlaces redundantes "ver imagen".
- Añade `alt` descriptivo distinto de la leyenda: el `alt` describe la imagen, la leyenda la contextualiza.
- Implementa `srcset` + `sizes` con ==versiones== de 400, 800 y 1600 px, e incluye `width` y `height`.
- Añade un enlace de descarga con `download` que indique formato y peso.
- Completa el `<video>` con `poster="promo-poster.jpg"` y dos `<track>`: `kind="subtitles" srclang="es" label="Español" default` y otro ==en inglés==.
- Recorre la galería solo con `Tab`: el foco debe ser siempre visible.
- Valida y comprueba que **no queda ninguna imagen sin `alt`**.

**Pista:** `srcset` dice *qué* imágenes hay y `sizes` dice *dónde* se mostrarán.

## Ejercicio 10 — Mini web con landmarks y skip link

**Nivel:** avanzado · **Capítulo:** [07 — Estructura semántica y ARIA](07-estructura-semantica-y-aria.md)

**Enunciado**

Esqueleto de una web de centro educativo con tres requisitos exigidos en la rúbrica: enlace de salto al contenido, menú que declare su estado y aviso dinámico que se anuncie. Sin librerías.

**Código inicial**

```html title="ejercicio-10-inicial.html" hl_lines="2 4"
<body>
  <div class="cabecera">
    <h1>IES Maya</h1>
    <div class="menu">
      <button>Menú</button>
      <ul hidden id="menu-lista">
        <li><a href="#inicio">Inicio</a></li>
        <li><a href="#ciclos">Ciclos</a></li>
        <li><a href="#contacto">Contacto</a></li>
      </ul>
    </div>
  </div>
  <div class="contenido">
    <h2>Inicio</h2>
    <p>Bienvenido al IES Maya.</p>
    <div id="avisos">No hay avisos nuevos.</div>
  </div>
  <div class="pie"><p>&copy; 2026 IES Maya</p></div>
</body>
```

**Tarea:**

- Sustituye los `<div>` por ==landmarks==: `<header>`, `<nav aria-label="Principal">`, `<main id="contenido">`, `<aside>` y `<footer>`.
- Añade como **primer elemento** del `<body>` el ==skip link== `<a class="skip-link" href="#contenido">Saltar al contenido principal</a>`, visible solo con foco.
- En el botón del menú, añade `aria-expanded="false"`, `aria-controls="menu-lista"` y `aria-label`, y alterna el estado con JavaScript.
- Declara los avisos como **región viva** con `role="status"` y actualiza su texto al enviar un `<form>` de contacto.
- El formulario debe tener `label`, `required` y enviar con `Intro` sin recargar.
- **Lista de comprobación con teclado:**
    1. Al cargar, el primer `Tab` marca el skip link.
    2. `Intro` lleva el foco al `<main>`.
    3. `Tab` lleva al botón del menú; `Intro` lo abre y cierra y `aria-expanded` cambia.
    4. Rellenas el formulario solo con teclado y envías con `Intro`.
    5. El lector de pantalla anuncia solo el aviso de confirmación.
- Valida el HTML final y revisa que no queda ningún `<div>` sin razón de ser.

**Pista:** `aria-expanded` solo tiene sentido en un control que despliega; si no alterna, es atributo muerto.

!!! success "Antes de entregar"

    - [ ] He validado el HTML en <https://validator.w3.org/> sin **errores**.
    - [ ] He recorrido la página solo con **teclado**: el foco siempre visible.
    - [ ] Ninguna imagen se ha quedado sin `alt` y ninguna leyenda repite su `alt`.
    - [ ] Todos los campos de formulario tienen **etiqueta visible** y tipo nativo.
    - [ ] El **texto no ha cambiado** respecto al código inicial y ningún `<div>` sobra.
    - [ ] He probado con **lector de pantalla** landmarks, tablas, formularios y avisos.

!!! question "Autoevaluación"

    Sin mirar todavía la solución: ¿qué cuatro etiquetas sustituyen a la "divitis", cuál puede haber **solo una vez** por página y qué atributo declara la dirección de un `<th>`?

    ??? success "Respuesta"

        Sustituyen a los `div` **`header`, `nav`, `main` y `footer`**; solo puede haber **un `<main>`** por página. La dirección del `<th>` la declara **`scope`** (`col` o `row`), junto con `caption` y `thead`/`tfoot`.

## Criterios de evaluación

!!! abstract "Resumen"

    Los ocho criterios de la tabla resumen el trabajo: semántica de ==bloques== y landmarks, jerarquía de encabezados, textos enriquecidos, tablas y formularios accesibles, accesibilidad con teclado y ARIA, validación y rigor del entregable. Lo que separa *Excelente* de *Suficiente* suele ser **validar sin errores** y **repasar el recorrido con teclado**.

| Criterio | Excelente | Suficiente | Insuficiente |
|---|---|---|---|
| Semántica de bloques | Todos los landmarks bien usados | Sustituye casi todos los `div` | Todo sigue siendo `div` |
| Jerarquía de encabezados | Un `h1` y niveles sin saltos | Desajustes menores | Varios `h1` o saltos |
| Textos enriquecidos | `time`, `abbr`, `blockquote`, `figure` | Etiquetas clave a medias | Fechas en texto suelto |
| Tablas accesibles | `caption`, `thead/tfoot`, `th scope`, `colspan` | Tabla con `caption` y `scope` | Tabla de puras `<td>` |
| Formularios HTML5 | Tipos nativos, `required`, `pattern`, `datalist` | Tipos correctos y etiquetas | Inputs sin etiqueta |
| Accesibilidad | Skip link, `aria-expanded`, `aria-live`, teclado | Landmarks y foco visible | Sin landmarks o sin teclado |
| Validación | Validador W3C sin errores | Avisos menores | Errores de anidamiento |
| Rigor del entregable | Código comentado y respuestas completas | Comentarios parciales | Sin comentarios |

*[ARIA]: Accessible Rich Internet Applications
