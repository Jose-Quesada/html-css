---
icon: lucide/pencil
title: "HTML 09 - Ejercicios"
description: "42 ejercicios prácticos de HTML5: 10 retos globales y 32 por unidad, con enunciado, código inicial y pista."
modulo: "LMH (0373) / DIW (0615) / DI (0488)"
unidad: 9
fecha: "2026-09-29"
---

# HTML 09 — Ejercicios prácticos

Diez retos globales de semántica, tablas, formularios HTML5, multimedia y accesibilidad, más **cuatro retos por unidad** (del 1 al 8) al final del capítulo. Resuélvelos en orden y compara después tu trabajo con [Ver soluciones](10-ejercicios-soluciones.md).

!!! note "Cómo trabajar"

    - **Intenta antes de mirar**: entrega una versión tuya de cada ejercicio y solo después consulta la solución.
    - **Valida siempre** en <https://validator.w3.org/>: que el navegador lo muestre no significa que esté bien.
    - **Pruébalo con teclado y lector de pantalla** donde aplique (menús, tablas, formularios, avisos).
    - **No toques el CSS salvo que el enunciado lo pida**: si el aspecto visual cambia sin que se indique, es que has roto la estructura.

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
    <p>Por Juan Pérez - 10 de junio de 2026</p>
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
- **Un solo `h1`** y sin saltos de encabezado (evita `h1` → `h3`).

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
    <p>Publicado por Laura García - 5 de junio de 2026</p>
    <img src="conferencia.jpg" alt="Sala llena durante la conferencia">
    <p>Sevilla acogerá la Conferencia Internacional de Inteligencia Artificial.
    "La tecnología debe estar al servicio de las personas", afirmó la directora.
    Cuenta con el apoyo de la agencia andaluza de innovación (ANDA).</p>
    <h3>Datos del evento</h3>
    <p>Del 16 al 18 de junio de 2026 · 48 ponencias · 1200 asistentes.</p>
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

- Los tres `<div>` internos pasan a `<section>` con `h3`; el contenedor, a `<section id="perfil">` con `<header>`.
- Crea un `<form>` con ==`<fieldset>`==/`<legend>` y `label for/id` en todos los campos (nombre, `email`, `tel`).
- En "Actividad Reciente", usa una `<ol>` con `<time datetime="...">` en cada entrada.
- En "Preferencias", añade otro `<form>` con `checkbox` y `<select>`, todos con ==etiqueta==.
- Convierte `div.lateral` en `<aside>` con `<h3>` y lista de enlaces.
- **Un solo `h1`** visible y los `h2` sin saltos de nivel.

**Pista:** si al hacer clic en el texto el foco salta a su campo, el `for` está bien.

## Ejercicio 6 — Procesamiento de vídeo con canvas

**Nivel:** avanzado · **Capítulo:** [04 — Multimedia](04-multimedia.md) · también [08 — APIs y funcionalidades nativas](08-apis-html5.md)

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
    <h1>IES F3</h1>
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
    <p>Bienvenido al IES F3.</p>
    <div id="avisos">No hay avisos nuevos.</div>
  </div>
  <div class="pie"><p>&copy; 2026 IES F3</p></div>
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
    - [ ] El **texto visible** no ha cambiado** respecto al código inicial y ningún `<div>` sobra.
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

## Ejercicios por unidad

Además de los diez retos globales, cada capítulo tiene su propio banco: **4 retos por unidad** (básico → avanzado) con enunciado, código inicial, tarea y pista. Repasa primero la teoría de la unidad y compara después tu trabajo con las [soluciones por unidad](10-ejercicios-soluciones.md).

### Unidad 1 — Introducción a HTML5 {: #ej-u1 }

Antes de maquetar nada hay que dominar el esqueleto del [capítulo 01](01-introduccion-html5.md): estos cuatro retos van de la ==plantilla completa== al HTML heredado que el navegador "arregla" a tu espalda sin que te enteres.

#### U1.1 — La plantilla del ciclo desde cero

**Nivel:** básico · **Tema:** [01 — Introducción a HTML5](01-introduccion-html5.md)

**Enunciado**

El ciclo DAM/DAW del IES F3 quiere estrenar web y todavía no existe ni un fichero. Crea desde cero la página de inicio con la estructura mínima bien formada, sin copiar el ejemplo resuelto del capítulo.

**Tarea:**

- Primera línea: ==`<!DOCTYPE html>`==, que es una **declaración** y no una etiqueta; después la raíz `<html lang="es">`.
- `<head>` con el ==trío clave==: `<meta charset="UTF-8">` como primer elemento, `<meta name="viewport">` y un `<title>` único y descriptivo.
- `<body>` con `header`, un único `main` y `footer`; dentro del `main`, un `h1` con el nombre del ciclo y dos párrafos (matrícula y ubicación).
- Añade dos comentarios: uno que explique el contenido del `head` y otro que marque el inicio del contenido visible.
- Escribe todas las etiquetas y nombres de atributos en minúsculas y cierra los elementos en orden inverso.
- Valida en <https://validator.w3.org/> pegando el código: **0 errores**.

**Pista:** el esqueleto de la sección 2.1 del capítulo cabe en menos de veinte líneas.

#### U1.2 — El `head` roto: cuatro fallos silenciosos

**Nivel:** básico · **Tema:** [01 — Introducción a HTML5](01-introduccion-html5.md)

**Enunciado**

La página se ve bien en el PC de clase, pero en el móvil se dibuja como si fuera un escritorio de 980 px, la pestaña dice "Página principal" (igual que otras diez) y en secretaría aparecen caracteres raros. Los fallos están todos en la cabecera del documento.

**Código inicial**

```html title="u1-2-inicial.html"
<html>
<head>
  <link rel="stylesheet" href="css/estilos.css">
  <meta name="description" content="Página del ciclo de DAM y DAW del IES F3.">
  <title>Página principal</title>
  <meta charset="iso-8859-1">
</head>
<body>
  <h1>Ciclos DAM y DAW</h1>
  <p>Matrícula abierta del 1 al 30 de septiembre de 2026.</p>
</body>
</html>
```

**Tarea:**

- Añade `<!DOCTYPE html>` en la primera línea y `lang="es"` a la raíz: sin `lang`, el lector de pantalla lee "añadir" con fonética inglesa.
- Cambia la codificación a `UTF-8` y ==muévela al principio== del `<head>`: debe quedar dentro de los primeros 1024 bytes.
- Completa la cabecera con el `<meta name="viewport">` que exige el diseño responsivo.
- Sustituye el título de plantilla por uno único e informativo de esta página.
- Deja un comentario sobre cada una de las cuatro correcciones explicando el fallo que resuelve.
- Valida en <https://validator.w3.org/> y repite hasta 0 errores.

**Pista:** los cuatro fallos son silenciosos: solo se ven como `Ã±`, en una pantalla estrecha o en la pestaña del navegador.

#### U1.3 — Entidades y booleanos de la chuleta

**Nivel:** medio · **Tema:** [01 — Introducción a HTML5](01-introduccion-html5.md)

**Enunciado**

La chuleta de HTML5 del ciclo se genera a mano y el resultado ya se ve en el navegador: la etiqueta de ejemplo no aparece, el enunciado del examen se parte en dos líneas y los campos no se comportan como promete el texto. El fichero está en UTF-8, así que los acentos van directos.

**Código inicial**

```html title="u1-3-inicial.html"
<body>
  <h1>Chuleta de HTML5 del ciclo</h1>
  <p>Para enlazar el CSS escribe: <link rel="stylesheet" href="estilos.css"></p>
  <p>HTML & CSS, más JavaScript. © 2026 IES F3</p>
  <p>El examen es el 15 de mayo a las 9:30 h.</p>
  <form action="/acceso" method="post">
    <p>Usuario: <input type="text" name="usuario" required="true"></p>
    <p><input type="checkbox" name="recordar" checked="false"> Recordarme</p>
    <p>Matrícula: <input type="text" name="matricula" value="2026-DAW-0142" disabled="no"></p>
  </form>
</body>
```

**Tarea:**

- Escapa la etiqueta de ejemplo con ==`&lt;` y `&gt;`== y envuélvela en `<code>`: hoy el navegador la interpreta y la hace desaparecer.
- Convierte el `&` suelto de "HTML & CSS" en `&amp;` y escribe el copyright con `&copy;`.
- Une con `&nbsp;` las partes de la fecha que no deben partirse: "15 de mayo" y "9:30 h".
- Deja los ==atributos booleanos== sin valor (`required`, `checked`, `disabled`): hoy `checked="false"` sigue marcado porque el atributo existe.
- Añade un comentario que explique por qué el campo de matrícula se muestra inactivo.
- Valida en <https://validator.w3.org/>: ya no debe aparecer el aviso del `link` dentro del `p`.

**Pista:** si un booleano lleva valor, has perdido: su presencia basta para activarlo.

#### U1.4 — HTML heredado: cierres en cruz y en MAYÚSCULAS

**Nivel:** avanzado · **Tema:** [01 — Introducción a HTML5](01-introduccion-html5.md)

**Enunciado**

Heredas el código de un curso anterior: el navegador lo muestra, pero el árbol que construye no es el que diseñó quien lo escribió y el validador se queja. Arréglalo sin cambiar una sola letra del texto visible.

**Código inicial**

```html title="u1-4-inicial.html"
<BODY>
  <H1 CLASS="titulo">Taller de iniciación a HTML</H1>
  <DIV>
    <P>Este taller enseña <STRONG>HTML semántico.</P>
  </STRONG>
  <P>Se imparte en el <EM>IES F3</EM>.</P>
  </DIV>
  <UL>
    <LI>Semana 1: estructura del documento</LI>
    <LI>Semana 2: texto y semántica</LI>
  </UL>
  <P><A HREF="matricula.html">Matricularme</A></P>
</BODY>
```

**Tarea:**

- Pasa todas las etiquetas y nombres de atributos a ==minúsculas==: HTML no distingue mayúsculas, pero es la convención y mañana el fichero podría servirse como XHTML.
- Corrige los cierres cruzados con la regla de oro: ==lo que se abre de último, se cierra de primero==.
- Envuelve el documento en la plantilla completa: `<!DOCTYPE>`, `lang`, `charset`, `viewport` y `title`.
- Abre el fichero y comprueba en la pestaña *Elements* (`F12`) que el árbol del navegador coincide con el que tú esperabas.
- Valida en <https://validator.w3.org/> hasta dejar 0 errores.

**Pista:** el navegador tolera el cruce y lo repara a su manera: por eso el fallo solo se ve en el árbol DOM y en el validador.

### Unidad 2 — Texto y semántica de contenido {: #ej-u2 }

El [capítulo 02](02-texto-y-semantica.md) convierte texto plano en ==esquema== y significado legibles por máquina: jerarquía de encabezados, listas, énfasis y citas, aplicados aquí a cuatro piezas reales del centro.

#### U2.1 — Esquema de encabezados a contracorriente

**Nivel:** básico · **Tema:** [02 — Texto y semántica de contenido](02-texto-y-semantica.md)

**Enunciado**

El folleto del ciclo en línea tiene dos `h1`, salta de `h1` a `h4` y vuelve a empezar por `h1` a mitad de página: quien navegue por encabezados con lector de pantalla se pierde desde el primer salto. Rehace el esquema sin tocar el texto.

**Código inicial**

```html title="u2-1-inicial.html"
<body>
  <h1>Ciclo DAM · IES F3</h1>
  <h4>Qué es DAM</h4>
  <p>Desarrollo de Aplicaciones Multiplataforma: 2.000 horas en dos cursos.</p>
  <h2>Módulos destacados</h2>
  <p>Programación, bases de datos y lenguajes de marcado.</p>
  <h1>Salidas profesionales</h1>
  <p>Desarrollo de escritorio, soporte técnico y testing.</p>
  <h3>Feria del Software Andaluz</h3>
  <p>Del 12 al 14 de noviembre en Sevilla.</p>
</body>
```

**Tarea:**

- Deja ==un solo `h1`== para toda la página y que elija el tema real del folleto.
- Reencadena los niveles ==sin saltos==: `h1` → `h2` → `h3`; "Qué es DAM" no puede ser un `h4` inmediatamente después del `h1`.
- Comprueba que cada encabezado **resume** lo que viene después ("Módulos destacados", no "Otra cosa más").
- Conserva intactos los cinco párrafos: no añadas ni quites texto visible.
- Extrae el esquema final en texto plano y compáralo con la lista de encabezados de la pestaña *Elements*.
- Valida en <https://validator.w3.org/>: 0 errores.

**Pista:** piensa en el índice que leerá un lector de pantalla: si un nivel se salta, el índice se rompe ahí.

#### U2.2 — La guía de matrícula en cuatro listas

**Nivel:** básico/medio · **Tema:** [02 — Texto y semántica de contenido](02-texto-y-semantica.md)

**Enunciado**

Secretaría publica la guía de matrícula y todo son párrafos de prosa: los pasos hay que contarlos a mano, la cuenta atrás no se aprecia, el material parece una enumeración perdida y el glosario no existe como tal. Conviértela en listas bien tipadas.

**Código inicial**

```html title="u2-2-inicial.html"
<body>
  <h1>Guía de matrícula de DAW</h1>
  <p>Pasos pendientes (los dos primeros ya los diste en la tutoría): 3) Entregar la hoja firmada en secretaría, 4) Pagar las tasas y 5) Guardar el justificante.</p>
  <p>Cuenta atrás para el cierre, en días restantes (de 5 a 1): publicar el aviso en la web, segundo aviso a los pendientes, última llamada de secretaría, cierre del plazo a las 23:59 y lista definitiva de admitidos.</p>
  <p>Necesitas: DNI en vigor, certificado digital, foto tipo carnet y la hoja de matrícula descargada.</p>
  <p>Glosario: DAW es Desarrollo de Aplicaciones Web. SMR es Mantenimiento de Sistemas Microinformáticos. FP es Formación Profesional.</p>
</body>
```

**Tarea:**

- Los pasos van en una `<ol>` con ==`start="3"`==: el primer `li` debe numerarse 3.
- La cuenta atrás va en otra `<ol>` con `start="5"` y `reversed`, numera 5, 4, 3, 2, 1 y borra del texto los números y el "(de 5 a 1)".
- El bloque "Necesitas" pasa a `<ul>`: ahí el orden no importa.
- El glosario pasa a `<dl>`: cada sigla es un `<dt>` y su expansión un `<dd>`.
- Comprueba que el único hijo directo de `ul`/`ol` es `<li>` (y de `dl`, `dt`/`dd`): ningún párrafo dentro de la lista.
- Valida en <https://validator.w3.org/>: 0 errores.

**Pista:** el número visible lo pinta la lista, no el texto: si siguen apareciendo "3)" escritos, sobran.

#### U2.3 — Avisos: importancia, énfasis y separadores

**Nivel:** medio · **Tema:** [02 — Texto y semántica de contenido](02-texto-y-semantica.md)

**Enunciado**

Como la web del centro muestra esos rótulos en negrita, quien la escribió envolvió todo en `<strong>` y separó las ideas con `<br>`. El resultado se ve igual, pero el lector de pantalla lo lee todo con la misma urgencia y no hay ni un cambio de tema real.

**Código inicial**

```html title="u2-3-inicial.html"
<body>
  <h1>Avisos del centro</h1>
  <p><strong>Secretaría</strong> abre de 8:00 a 14:00.
  <br>IES F3<br>Calle Rioja, 12<br>29018 Málaga<br>secretaria@F3.es</p>
  <p><strong>Convocatoria</strong> extraordinaria de Lenguajes de Marcado: el <em>22 de julio</em>.</p>
  <p><strong>Matrícula</strong> del curso 2026/2027: del 1 al 30 de septiembre.
  <br><strong>Importante:</strong> no se aceptarán matrículas fuera de plazo.</p>
  <p><strong>Exámenes</strong> del primer trimestre: del 12 al 23 de enero.</p>
</body>
```

**Tarea:**

- Aplica la regla: ==`<strong>` solo para importancia real==; el único que se queda es el aviso de plazo cerrado.
- Los rótulos decorativos (Secretaría, Convocatoria, Matrícula, Exámenes) pasan a `<span class="destacado">` con un comentario que diga que el aspecto lo pondrá CSS.
- Conserva en `<em>` la fecha que se enfatiza al pronunciarla y no lo uses para decorar.
- Mantén solo los `<br>` que forman parte del texto (la dirección); el que separa ideas se sustituye por dos párrafos.
- Separa el cambio de tema entre el bloque de matrícula y el de exámenes con un `<hr>`.
- Mete dirección y correo en un `<address>` y valida en <https://validator.w3.org/> sin errores.

**Pista:** `<strong>` se anuncia con más fuerza en el lector de pantalla: si no es importante, sobra.

#### U2.4 — Ficha de la ruta del Caminito del Rey

**Nivel:** avanzado · **Tema:** [02 — Texto y semántica de contenido](02-texto-y-semantica.md)

**Enunciado**

El grupo excursionista de la FP publica la salida al Caminito con la fecha en texto suelto, la foto pegada con su pie en otro párrafo y la cita del ingeniero entre comillas escritas a mano. Dale el formato semántico completo.

**Código inicial**

```html title="u2-4-inicial.html"
<body>
  <h1>Caminito del Rey: salida de este sábado</h1>
  <p>Salida el sábado 14 de marzo de 2026 a las 8:30 desde el parking de Ardales.</p>
  <p>La ruta tiene 7,7 km y el billete cuesta 10 €.</p>
  <img src="caminito.jpg" alt="Pasarela metálica anclada a la pared del desfiladero">
  <p>Foto: tramo central sobre el desfiladero de los Gaitanes.</p>
  <p>"Es la obra civil más temeraria de su tiempo", dijo el ingeniero en 1905.</p>
  <p>El lema de la excursión: "miedo arriba, no mires abajo".</p>
  <p>Más información en caminitodelrey.info</p>
</body>
```

**Tarea:**

- Marca la salida con `<time datetime="2026-03-14T08:30">` usando ==formato ISO== con hora; el texto visible no cambia.
- Envuelve la imagen en `<figure>` con un `<figcaption>` que aporte algo distinto del `alt`.
- Convierte la frase del ingeniero en `<blockquote>` con `<p>` dentro, el atributo `cite` con la URL de origen y la atribución visible en `<cite>`.
- Cambia las comillas literales del lema por `<q>`: el navegador pone las comillas.
- Responde por escrito: ¿qué ocurre si `figcaption` y `alt` dicen exactamente lo mismo? ¿Y qué guarda el atributo `cite` del `blockquote`?
- Valida en <https://validator.w3.org/>: 0 errores.

**Pista:** `cite` del bloque guarda la URL para las máquinas y no se muestra en pantalla; si quieres que se vea la fuente, va como texto dentro.

### Unidad 3 — Enlaces y recursos {: #ej-u3 }

Cuatro retos para dominar los destinos de un enlace —rutas, anclas y protocolos especiales— y los recursos que los acompañan: imágenes y marcos incrustados. Recuerda que una ==ruta relativa== depende de la página desde la que se escribe.

#### U3.1 — Rutas relativas en la tienda

**Nivel:** básico · **Tema:** [03 — Enlaces y recursos](03-enlaces-y-recursos.md)

**Enunciado**

La tienda tiene esta estructura de carpetas y la ficha de producto enlaza a todo con rutas escritas "a ojo" desde la raíz. Recorre el árbol, sitúate en la página que enlaza y corrige cada destino.

**Código inicial**

```text title="arbol.txt"
tienda-ufro/                 <- raíz del sitio
├── index.html
├── producto/
│   ├── zapatillas.html
│   └── mochila.html
├── img/
│   ├── logo.svg
│   └── producto/zapatillas-1200w.jpg
├── css/estilos.css
└── documentos/garantia-2-anios.pdf
```

```html title="u3-1-inicial.html"
<!-- Rutas escritas desde producto/zapatillas.html -->
<link rel="stylesheet" href="estilos.css">
<body>
  <header>
    <img src="logo.svg" alt="Logotipo de la tienda">
    <a href="index.html">Volver a la portada</a>
  </header>
  <main>
    <h1>Zapatillas Run 300</h1>
    <a href="mochila.html">Ver también la mochila Trail 25 L</a>
    <a href="garantia-2-anios.pdf">Consultar la garantía de 2 años</a>
    <a href="/documentos/garantia-2-anios.pdf">La misma garantía por raíz</a>
  </main>
</body>
```

**Tarea:**

- Sitúate en `producto/zapatillas.html`: la ruta se calcula **desde la página que enlazas**, no desde el explorador.
- Corrige CSS, logotipo y portada: desde la subcarpeta hay que ==subir== un nivel con `../` antes de bajar a `css/`, `img/` o a la raíz.
- "Ver también la mochila" ya es correcta: es un fichero hermano en la misma carpeta; déjala tal cual.
- Corrige "Consultar la garantía" con ruta relativa y comprueba que la versión de ==raíz== (`/documentos/garantia-2-anios.pdf`) apunta al mismo fichero.
- Añade un enlace nuevo a `img/producto/zapatillas-1200w.jpg` con la ruta relativa completa desde la ficha.
- Abre la página en el navegador: ni un solo 404 en estilos, imágenes ni enlaces.

**Pista:** cuenta niveles desde la carpeta de la página: `../` sube uno, `carpeta/archivo` baja y `/ruta` arranca en la raíz del sitio.

#### U3.2 — Índice con anclas y skip link

**Nivel:** básico/medio · **Tema:** [03 — Enlaces y recursos](03-enlaces-y-recursos.md)

**Enunciado**

Un reglamento largo en una sola página se navega a golpe de scroll. Convierte el índice en saltos internos de verdad y añade el enlace de salto accesible para quien navega con teclado.

**Código inicial**

```html title="u3-2-inicial.html"
<body>
  <a class="skip-link" href="#">Saltar al contenido</a>
  <header>
    <h1>Reglamento de evaluación</h1>
    <nav aria-label="Índice">
      <ul>
        <li><a href="#">Matriculación</a></li>
        <li><a href="#">Asistencia</a></li>
        <li><a href="#">Evaluación</a></li>
        <li><a href="#">Reconsideraciones</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <section><h2>Matriculación</h2><p>El plazo se abre el 1 de septiembre.</p></section>
    <section><h2>Asistencia</h2><p>La justificación se presenta en 48 horas.</p></section>
    <section><h2>Evaluación</h2><p>Cada trimestre se publican las notas.</p></section>
    <section><h2>Reconsideraciones</h2><p>Plazo de cinco días hábiles.</p></section>
  </main>
</body>
```

**Tarea:**

- Asigna un `id` único a cada `<section>` del `<main>` y conecta los cuatro enlaces del índice con su ==fragmento== (`#matriculacion`, `#asistencia`, `#evaluacion`, `#reconsideraciones`).
- Corrige el skip link: debe apuntar al `id` del `<main>` y ser el **primer elemento** del `<body>`.
- Añade al pie un enlace "Volver al principio" que apunte al `id` del encabezado: vuelve arriba sin recargar.
- Respeta la jerarquía: un `h1` visible y un `h2` por sección, sin saltos de nivel.
- Recorre la página solo con Tab: el primer salto debe ir al contenido y cada `#…` debe llevar al título de su sección.

**Pista:** un enlace `#id` no recarga la página: busca en el documento un elemento con ese `id` y, si no existe, el salto no ocurre.

#### U3.3 — Enlaces con destinos especiales y descargas

**Nivel:** medio · **Tema:** [03 — Enlaces y recursos](03-enlaces-y-recursos.md)

**Enunciado**

La página de recursos del centro mezcla "haz clic aquí", un enlace externo que debería abrirse aparte y descargas sin indicar qué se lleva. Reescribe destinos y textos.

**Código inicial**

```html title="u3-3-inicial.html"
<main>
  <h1>Recursos para familias</h1>
  <p>Consulta <a href="horarios.pdf">haz clic aquí</a> y también
     <a href="matricula.pdf">este otro</a>.</p>
  <p><a href="https://www.juntadeandalucia.es/">Más información</a></p>
  <p>Contacta: <a href="#">correo</a> o <a href="#">teléfono</a>.</p>
  <p><a href="calendario.pdf">Descargar</a></p>
</main>
```

**Tarea:**

- Convierte "correo" en `mailto:secretaria@centro.es?subject=Consulta%20sobre%20matrícula` y "teléfono" en `tel:+34955000000`.
- El sitio de la Junta se abre en pestaña nueva: `target="_blank"` con ==`rel="noopener noreferrer"`== y un texto que avise de la pestaña.
- "Descargar" pasa a `download="Calendario_2026.pdf"` con texto que indique formato y peso; el horario **no** lleva `download` (debe abrirse en el navegador).
- Sustituye los textos genéricos por ==enlaces descriptivos== que se entiendan solos en la lista de enlaces del lector de pantalla.
- Ningún texto de enlace se repite dentro de la página.

**Pista:** lee solo los textos de los enlaces, uno por línea: si no sabes a dónde lleva cada uno sin leer el párrafo, reescríbelo.

#### U3.4 — Imágenes accesibles y marco incrustado

**Nivel:** avanzado · **Tema:** [03 — Enlaces y recursos](03-enlaces-y-recursos.md)

**Enunciado**

La ficha de un alojamiento anuncia un patrón decorativo que nadie necesita oír, muestra imágenes que hacen saltar la página al cargar y termina con un mapa sin descripción. Déjalo todo limpio y accesible.

**Código inicial**

```html title="u3-4-inicial.html"
<main>
  <h1>Casa del Olivar · Jaén</h1>
  <img src="img/patron.jpg">
  <img src="img/patio-800.jpg" alt="Patio">
  <img src="img/habitacion-800.jpg" alt="Habitación doble con vistas al valle">
  <p>Fotos: <a href="#">ver más</a></p>
  <iframe src="https://www.openstreetmap.org/export/embed.html?bbox=-3.80,37.77,-3.78,37.79"></iframe>
</main>
```

**Tarea:**

- `img/patron.jpg` es decorativa: usa ==`alt=""`== (vacío) para que el lector de pantalla la salte.
- "Patio" e "Habitación" son informativas: `alt` de una línea que aporte lo que el texto no dice, sin repetir el `figcaption`.
- Añade `width` y `height` a las tres imágenes para ==reservar el espacio== y evitar saltos de diseño (CLS).
- La habitación queda fuera del pliegue (`loading="lazy"`); banner y patio, sobre el texto, van con `loading="eager"`.
- Envuelve banner y patio en `<picture>` con `<source>` `image/avif` y `image/webp`, dejando el `<img>` como respaldo con su `alt`.
- Al `<iframe>` del mapa: `title` que describa el lugar, `width`/`height`, `loading="lazy"` y `sandbox` con los permisos mínimos.

**Pista:** el `<img>` final de un `<picture>` es a la vez el respaldo obligatorio y el único que lleva `alt`, `width` y `height`.

### Unidad 4 — Multimedia en HTML5 {: #ej-u4 }

Cuatro retos de reproducción nativa: formatos y póster, subtítulos con un `.vtt` de verdad, audio con transcripción e incrustación externa accesible, a partir de [04 — Multimedia en HTML5](04-multimedia.md).

#### U4.1 — Vídeo informativo con póster y formatos

**Nivel:** básico · **Tema:** [04 — Multimedia](04-multimedia.md)

**Enunciado**

El clip de la jornada de puertas abiertas se sirve en MP4 y WebM, pero la página no muestra barra de reproducción, la ruta del fichero se declara una sola vez y el marco salta al aparecer.

**Código inicial**

```html title="u4-1-inicial.html"
<main>
  <h1>Jornada de puertas abiertas</h1>
  <video src="video/jornada.mp4" poster="img/jornada-portada.jpg"></video>
  <p>Grabación completa de la visita al centro.</p>
</main>
```

**Tarea:**

- Añade ==`controls`==: sin él el vídeo es "solo una caja", sin barra ni atajos de teclado.
- Declara los dos formatos con `<source>` y `type` (MP4 primero, WebM después) y **retira** `src` del `<video>`.
- Mantén el `poster` y añade `width="640" height="360"` para ==reservar el espacio==.
- Usa `preload="metadata"`: duración y pistas sin descargar el fichero entero.
- Cierra con un texto de respaldo **dentro** del `<video>` que ofrezca descargar el MP4.
- Comprueba en las herramientas de desarrollo que el navegador pide solo el `type` que entiende.

**Pista:** el navegador recorre los `<source>` de arriba abajo y se queda con el primero cuyo `type` comprende.

#### U4.2 — Subtítulos con un .vtt real

**Nivel:** medio · **Tema:** [04 — Multimedia](04-multimedia.md)

**Enunciado**

El vídeo de las normas del taller necesita subtítulos en español para quien es sordo o ve con el sonido apagado. Adjunta el fichero `.vtt`, actívalo por defecto y añade una segunda pista en inglés.

**Código inicial**

```html title="u4-2-inicial.html"
<video controls poster="img/normas-portada.jpg" width="640" height="360" preload="metadata">
  <source src="video/normas.mp4" type="video/mp4">
  <source src="video/normas.webm" type="video/webm">
  <p>No puedes reproducir este vídeo.
     <a href="video/normas.mp4">Descárgalo (MP4)</a>.</p>
</video>
```

```vtt title="normas-es.vtt"
WEBVTT

1
00:00:00.000 --> 00:00:03.500
Bienvenidos al taller de electrónica.

2
00:00:03.500 --> 00:00:07.800
(texto pendiente)
```

**Tarea:**

- Añade un `<track>` con `kind="captions"` (diálogo **y** efectos sonoros), `srclang="es"`, `label="Español"` y ==`default`==.
- Completa `normas-es.vtt`: termina el cue 2 y añade dos bloques más con cabecera `WEBVTT` y tiempos `HH:MM:SS.mmm --> HH:MM:SS.mmm`.
- Incluye al menos un efecto sonoro, por ejemplo `((pasos))`, en su propio bloque de texto.
- Añade un segundo `<track>` en inglés (`kind="subtitles"`, `srclang="en"`, `label="English"`) **sin** `default`.
- El `src` de cada `<track>` debe apuntar a su `.vtt` con la ruta correcta desde la página.
- El texto de respaldo va **después** de las pistas, dentro del `<video>`; activa los subtítulos y verifica que "Español" aparece marcado.

**Pista:** `captions` recoge diálogo y efectos sonoros; `subtitles` solo traduce la habla.

#### U4.3 — Podcast con transcripción

**Nivel:** medio · **Tema:** [04 — Multimedia](04-multimedia.md)

**Enunciado**

El podcast del ciclo se sirve en un solo formato, descarga el fichero antes de que nadie pulse play y no ofrece alternativa textual. Déjalo listo sin depender de JavaScript.

**Código inicial**

```html title="u4-3-inicial.html"
<main>
  <h1>Podcast: la FP en 5 minutos</h1>
  <h2>Episodio 7: los ciclos de Artes Gráficas</h2>
  <audio src="audio/ep07.mp3" controls></audio>
  <p>Episodio 7: qué se estudia y qué salidas tiene.</p>
</main>
```

**Tarea:**

- Declara dos formatos con `<source>` y `type` (`audio/mpeg` primero, `audio/ogg` después) y retira `src` del `<audio>`.
- Usa `preload="none"`: con varios episodios en la página nada se descarga hasta pulsar play.
- Añade texto de respaldo **dentro** del `<audio>` con enlace de descarga al MP3.
- Publica la transcripción en un `<details>` con `<summary>`: al menos tres entradas con marca de tiempo.
- Junto al reproductor, añade un enlace de ==descarga directa== que indique formato y peso.
- Responde por escrito: ¿cumple la transcripción la WCAG 1.2.1 o la 1.2.2? ¿Qué cambiaría si el episodio tuviera vídeo?

**Pista:** la transcripción es texto visible en la propia página, no un fichero adjunto aparte.

#### U4.4 — Banner automático e incrustación externa

**Nivel:** avanzado · **Tema:** [04 — Multimedia](04-multimedia.md)

**Enunciado**

La portada quiere un vídeo decorativo que arranque solo sin molestar y, más abajo, una clase grabada alojada en YouTube. Ambos tienen que funcionar con teclado y lector de pantalla.

**Código inicial**

```html title="u4-4-inicial.html"
<body>
  <header>
    <h1>Instituto F3</h1>
    <!-- vídeo decorativo de fondo -->
  </header>
  <main>
    <h2>Clase grabada: accesibilidad</h2>
    <!-- aquí va el vídeo de YouTube -->
    <p>Duración: 45 minutos.</p>
  </main>
</body>
```

**Tarea:**

- El banner debe arrancar solo: ==`autoplay muted playsinline`== más `loop`; al ser decorativo va sin `controls` y con `aria-hidden="true"`.
- Dále `width`, `height` y `preload="none"`: el fondo no debe consumir datos hasta que haga falta.
- Incrusta la clase con `<iframe>` de `youtube-nocookie.com`, `title` descriptivo, `loading="lazy"`, `width="560" height="315"` y pantalla completa habilitada.
- Añade debajo un enlace al vídeo original en YouTube con texto descriptivo, por si el marco no carga.
- Responde por escrito: ¿qué `preload` usarías en la ficha de un vídeo largo (`none`, `metadata` o `auto`) y por qué?

**Pista:** los navegadores solo aceptan el arranque automático con el sonido silenciado; si quieres sonido, lo activa la persona usuaria.

### Unidad 5 — Tablas de datos {: #ej-u5 }

Cuatro retos sobre la estructura completa de `<table>`: secciones semánticas, celdas combinadas, columnas enteras y un scroll horizontal que no deje a nadie fuera. Si algo te bloquea, repasa antes la teoría de [05 — Tablas de datos](05-tablas.md) y vuelve a intentarlo.

#### U5.1 — Clasificación de la liga

**Nivel:** básico · **Tema:** [05 — Tablas de datos](05-tablas.md)

**Enunciado**

La clasificación del torneo local es una tira plana de `<td>`: no se distingue la fila de encabezados, nadie sabe qué columna contiene qué y falta el resumen del grupo.

**Código inicial**

```html title="u5-1-inicial.html"
<table>
  <tr>
    <td>Equipo</td><td>PJ</td><td>G</td><td>E</td><td>P</td><td>Pts</td>
  </tr>
  <tr>
    <td>Real Betis</td><td>8</td><td>6</td><td>1</td><td>1</td><td>19</td>
  </tr>
  <tr>
    <td>Sevilla FC</td><td>8</td><td>5</td><td>2</td><td>1</td><td>17</td>
  </tr>
  <tr>
    <td>CD Málaga</td><td>8</td><td>4</td><td>2</td><td>2</td><td>14</td>
  </tr>
</table>
```

**Tarea:**

- Envuelve la fila de cabecera en `<thead>` y convierte sus `<td>` en `<th scope="col">`.
- Mueve los tres equipos a `<tbody>` y haz que la primera celda de cada fila sea un `<th scope="row">`.
- Añade `<tfoot>` con la fila "Media del grupo": 8, 5, 1,7, 1,3 y 16,7, también encabezada con `th scope="row"`.
- Comprueba fila a fila que todas suman seis celdas y que ==`scope`== distingue columna de fila.
- Valida y recorre la tabla con el lector de pantalla: cada dato debe anunciar su equipo y su columna.

**Pista:** `thead` encabeza las columnas, `tbody` guarda los datos y `tfoot` resume al final.

#### U5.2 — Turnos con celdas unidas

**Nivel:** medio · **Tema:** [05 — Tablas de datos](05-tablas.md)

**Enunciado**

En la tabla de turnos de la panadería "Lunes" aparece dos veces seguidas y el descanso se fragmenta en celdas sueltas. Une las celdas para que cada día y cada bloque ocupen exactamente el espacio que les corresponde.

**Código inicial**

```html title="u5-2-inicial.html"
<table>
  <caption>Turnos de la semana — Panadería El Trigal</caption>
  <thead>
    <tr><th scope="col">Día</th><th scope="col">Sección</th><th scope="col">Mañana</th><th scope="col">Tarde</th></tr>
  </thead>
  <tbody>
    <tr><td>Lunes</td><td>Horno</td><td>Ana</td><td>Luis</td></tr>
    <tr><td>Lunes</td><td>Venta</td><td>Marta</td><td>Carlos</td></tr>
    <tr><td>Martes</td><td>Horno</td><td>Ana</td><td>Luis</td></tr>
    <tr><td>Martes</td><td>Venta</td><td>Marta</td><td>Carlos</td></tr>
  </tbody>
</table>
```

**Tarea:**

- Convierte el `<td>` de "Lunes" en `<th scope="row" rowspan="2">` y **borra** el `<td>` repetido de la fila de Venta: la celda cubierta no se escribe.
- Haz lo mismo con "Martes".
- Añade al final del `<tbody>` una fila de descanso con una única celda `<td colspan="4">`.
- Recuenta cada fila: cabecera, datos y descanso deben sumar cuatro columnas, contando los huecos heredados por ==`rowspan`==.
- Valida el resultado: el navegador repara en silencio las tablas rotas, así que un documento válido no garantiza una cuadrícula correcta.

**Pista:** dibuja la tabla en papel y tacha las celdas que cubre cada `rowspan`; si queda un hueco sobrante, sobra una `<td>`.

#### U5.3 — Precios con colgroup y abbr

**Nivel:** medio · **Tema:** [05 — Tablas de datos](05-tablas.md)

**Enunciado**

El catálogo de la tienda necesita que la columna de producto sea más ancha que las demás sin repetir el ancho celda a celda, y que el lector de pantalla no deletree "Precio con IVA incluido" en cada fila.

**Código inicial**

```html title="u5-3-inicial.html"
<table>
  <caption>Taller El Olivo — precios con IVA</caption>
  <thead>
    <tr>
      <th scope="col">Producto</th>
      <th scope="col">Formato</th>
      <th scope="col">Precio con IVA incluido</th>
    </tr>
  </thead>
  <tbody>
    <tr><th scope="row">Aceite de oliva virgen extra</th><td>Botella 1 L</td><td>9,50 €</td></tr>
    <tr><th scope="row">Vinagre de Jerez</th><td>Botella 500 ml</td><td>4,25 €</td></tr>
    <tr><th scope="row">Sal marina en escamas</th><td>Bolsa 1 kg</td><td>2,10 €</td></tr>
  </tbody>
</table>
```

**Tarea:**

- Inserta un `<colgroup>` con dos `<col>`: el primero con `style="width: 16rem"` y el segundo con `span="2"` para formato y precio.
- Respeta el orden de los hijos de `<table>`: `caption` → ==`colgroup`== → `thead` → `tbody`.
- Añade al `<th>` largo un `abbr="Precio (IVA)"` con la forma corta que el lector anuncie en cada celda.
- Recuerda que `<col>` es una etiqueta vacía y solo admite atributos presentacionales (`width`, `background-color`...).
- Valida y comprueba que el texto visible de la cabecera no ha cambiado.

**Pista:** el `width` de `<col>` es solo una sugerencia: si necesitas un ancho fiable, fíjalo en CSS.

#### U5.4 — Calendario de exámenes accesible en móvil

**Nivel:** medio/avanzado · **Tema:** [05 — Tablas de datos](05-tablas.md)

**Enunciado**

El calendario de exámenes tiene seis columnas y en una pantalla de 360 px se sale de golpe. Mantén la tabla intacta y haz que su scroll horizontal sea alcanzable también con el teclado.

**Código inicial**

```html title="u5-4-inicial.html"
<figure>
  <table>
    <caption>Semana de exámenes finales — 1.º DAW A</caption>
    <thead>
      <tr><th scope="col">Módulo</th><th scope="col">Lun 15</th><th scope="col">Mar 16</th><th scope="col">Mié 17</th><th scope="col">Jue 18</th><th scope="col">Vie 19</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">Lenguajes de marcas</th><td>09:00</td><td></td><td></td><td></td><td></td></tr>
      <tr><th scope="row">Bases de datos</th><td></td><td>11:30</td><td></td><td></td><td></td></tr>
      <tr><th scope="row">Desarrollo web en cliente</th><td></td><td></td><td>09:00</td><td></td><td></td></tr>
      <tr><th scope="row">Sistemas de gestión empresarial</th><td></td><td></td><td></td><td>12:00</td><td></td></tr>
      <tr><th scope="row">Entornos de desarrollo</th><td></td><td></td><td></td><td></td><td>10:00</td></tr>
    </tbody>
  </table>
</figure>
```

**Tarea:**

- Dale `id="cap-examenes"` al `<caption>`: el contenedor apuntará a él para nombrarse.
- Convierte el `<figure>` en la región desplazable: `class="tabla-scroll"`, `tabindex="0"`, `role="region"` y `aria-labelledby="cap-examenes"`.
- Añade un bloque `<style>` con `.tabla-scroll { overflow-x: auto; }` y `.tabla-scroll table { width: 100%; min-width: 44rem; }`.
- Añade un `<tfoot>` con el total de exámenes y comprueba el orden completo: `caption` → `thead` → `tbody` → ==`tfoot`==.
- Recorre la página con `Tab`: el contenedor debe recibir el foco y las flechas deben desplazar la tabla (==WCAG 2.1.1==).
- No uses `overflow: hidden` en ningún caso: ocultaríamos datos sin forma de recuperarlos.

**Pista:** sin `tabindex="0"` la barra de scroll aparece, pero solo es alcanzable con el ratón.

### Unidad 6 — Formularios HTML5 {: #ej-u6 }

Cuatro retos de envío y validación nativa: desde un alta mínima hasta un formulario con rangos, grupos de opciones y estados bien declarados. La teoría está en [06 — Formularios HTML5](06-formularios-html5.md).

#### U6.1 — Alta en el boletín

**Nivel:** básico · **Tema:** [06 — Formularios HTML5](06-formularios-html5.md)

**Enunciado**

El boletín del centro solo pide un correo, pero llegan direcciones mal escritas y el navegador no rellena nada. Monta el formulario mínimo con validación nativa, sin una sola línea de JavaScript.

**Tarea:**

- Crea desde cero un `<form action="/boletin" method="post">` con un campo de correo y una casilla de aceptación de la política de privacidad.
- El correo debe ser `type="email"` con `id`, `name` y ==`required`==; la casilla de la política también lleva `required`.
- Asocia a cada control un `<label for>` visible: el `placeholder` puede acompañar como pista, nunca sustituirlo.
- Añade `autocomplete="email"` al campo para cumplir el criterio ==WCAG 1.3.5==.
- Cierra con `<button type="submit">Suscribirme</button>` y prueba a enviar con el campo vacío y con un correo sin `@`.

**Pista:** el navegador mostrará el error antes de que exista una sola línea de JavaScript.

#### U6.2 — Formulario de contacto

**Nivel:** básico/medio · **Tema:** [06 — Formularios HTML5](06-formularios-html5.md)

**Enunciado**

El formulario de contacto del instituto está a medias: las etiquetas no apuntan a ningún campo, ningún input declara `name` y el botón no sabe lo que hace. Déjalo listo para que el servidor reciba la consulta.

**Código inicial**

```html title="u6-2-inicial.html"
<form action="/contacto">
  <p>
    <label>Nombre <input type="text" placeholder="Tu nombre"></label>
  </p>
  <p>
    <label>Correo <input type="text" placeholder="Tu correo"></label>
  </p>
  <p>
    <label>Motivo <input type="text"></label>
  </p>
  <button>Enviar</button>
</form>
```

**Tarea:**

- Da `id` a cada campo y convierte cada etiqueta en un `<label for>` externo que apunte a él.
- Añade `name` a los tres campos: sin ==`name`== el dato no viaja al servidor aunque esté relleno.
- Cambia el correo a `type="email"` y marca `required` los tres campos.
- Declara `method="post"` y deja en un comentario del HTML la razón: aquí se crea un registro y el motivo puede ser largo, así que `GET` no encaja.
- Escribe siempre el `type` del botón: `<button type="submit">Enviar consulta</button>`.
- Comprueba en la pestaña Red que la petición lleva `nombre=...&correo=...&motivo=...`.

**Pista:** `GET` deja los valores en la barra de dirección; `POST` los manda en el cuerpo de la petición.

#### U6.3 — Encuesta con grupos de opciones

**Nivel:** medio · **Tema:** [06 — Formularios HTML5](06-formularios-html5.md)

**Enunciado**

La encuesta de final de curso tiene radios y casillas sueltos con títulos en párrafos: el lector de pantalla anuncia "Mañana, 1 de 2" sin decir de qué grupo habla, y el campo de ciclo es texto libre.

**Código inicial**

```html title="u6-3-inicial.html"
<form action="/encuesta" method="post">
  <p>Turno preferido:</p>
  <input type="radio" id="manana" name="turno" value="manana">
  <label for="manana">Mañana</label>
  <input type="radio" id="tarde" name="turno" value="tarde">
  <label for="tarde">Tarde</label>
  <p>Qué te ha parecido:</p>
  <input type="checkbox" id="contenido" name="contenido" value="si">
  <label for="contenido">El contenido</label>
  <input type="checkbox" id="practicas" name="practicas" value="si">
  <label for="practicas">Las prácticas</label>
  <p>Ciclo:</p>
  <input type="text" id="ciclo" name="ciclo">
  <button type="submit">Enviar encuesta</button>
</form>
```

**Tarea:**

- Sustituye los tres `<p>` de título por un `<fieldset>` con su ==`legend`==: el párrafo no es el nombre accesible del grupo.
- Comprueba que los dos radios comparten `name="turno"` (solo se marcará uno) y que cada casilla conserva su `name` propio.
- Cambia el campo de texto por un `<select>` con dos bloques de opciones: `Grado medio` (SMR) y `Grado superior` (DAM, DAW), cada uno en su `<optgroup>`.
- Precarga la opción vacía `<option value="" disabled selected>Elige una opción</option>` y añade `required` al `<select>`.
- Prueba con el lector: al enfocar un radio debe oírse "Turno preferido, Mañana, 1 de 2, botón de opción".

**Pista:** `legend` es el título que el lector repite antes de cada opción del grupo.

#### U6.4 — Reserva de sala: rangos, botones y estados

**Nivel:** medio/avanzado · **Tema:** [06 — Formularios HTML5](06-formularios-html5.md)

**Enunciado**

El formulario de reserva de la sala admite 500 plazas, deja escribir páginas enteras de observaciones y el botón "Ver resumen" envía el formulario sin querer. Domina rangos, límites, estados y tipos de botón.

**Código inicial**

```html title="u6-4-inicial.html"
<form action="/reserva" method="post">
  <label for="plazas">Plazas</label>
  <input type="number" id="plazas" name="plazas">
  <label for="observaciones">Observaciones</label>
  <textarea id="observaciones" name="observaciones" rows="3"></textarea>
  <label for="curso">Grupo</label>
  <input type="text" id="curso" name="curso" value="1.º DAW A">
  <label for="codigo">Código de reserva</label>
  <input type="text" id="codigo" name="codigo" value="RES-2026-014" disabled>
  <p id="resumen" hidden></p>
  <button>Ver resumen</button>
  <button>Reservar</button>
</form>
```

**Tarea:**

- En `plazas`, añade `min="1"`, `max="30"`, `step="1"` y `required`, y describe el rango permitido en el atributo `title`.
- Limita las observaciones con `maxlength="200"` y hazlas `required`; añade un `placeholder` con un ejemplo.
- Deja un comentario en cada campo de estado: ==`readonly`== en "Grupo" (visible, tabulable y **sí** se envía) y `disabled` en "Código" (sin foco y **no** se envía).
- Declara el tipo de ambos botones: "Ver resumen" pasa a ==`type="button"`== y "Reservar" a `type="submit"`; recuerda que un `<button>` sin `type` equivale a `submit`, y haz que el primero rellene el párrafo `id="resumen"` con unas líneas de JavaScript sin recargar.
- Anota en un comentario del `<form>` qué haría `novalidate`: apagaría los globos nativos para mostrar errores propios con JavaScript.
- Comprueba en la pestaña Red que llegan `plazas`, `observaciones` y `curso`, pero no `codigo`.

**Pista:** `readonly` se envía y sigue tabulándose; `disabled` ni siquiera viaja en la petición.

### Unidad 7 — Estructura semántica y ARIA {: #ej-u7 }

Cuatro retos de diagnóstico y arreglo sobre la semántica: jerarquía de encabezados, mapa de landmarks, estado del menú y el choque entre ARIA y el HTML nativo. Todos se resuelven con HTML puro y se comprueban con teclado y con el árbol de accesibilidad de DevTools.

#### U7.1 — Encabezados sin saltos

**Nivel:** básico · **Tema:** [07 — Estructura semántica y ARIA](07-estructura-semantica-y-aria.md)

**Enunciado**

La página de un curso de fotografía se lee al revés: hay dos `h1`, los títulos de unidad están en `h4` y un `h3` queda huérfano. Para el lector de pantalla el índice está roto. Reordena la jerarquía sin cambiar una sola palabra.

**Código inicial**

```html title="u7-1-inicial.html"
<body>
  <h1>Fotografía Digital para Principiantes</h1>
  <h4>La cámara</h4>
  <p>Conoce los mandos antes de disparar.</p>
  <h4>El objetivo</h4>
  <p>La distancia focal cambia la perspectiva.</p>
  <h2>Composición</h2>
  <p>La regla de los tercios ordena el encuadre.</p>
  <h3>La luz</h3>
  <h1>Focos y diafragma</h1>
  <p>Medir la luz es el primer hábito del fotógrafo.</p>
</body>
```

**Tarea:**

- Deja **un solo `<h1>`**: el título del curso; "Focos y diafragma" pasa a `h2`.
- Sube los dos `h4` a `h2`: "La cámara", "El objetivo" y "Composición" son unidades del mismo nivel.
- Conserva "La luz" como `h3` dentro de "Composición": la jerarquía debe descender ==sin saltos== de nivel.
- No toques el texto ni el tamaño visual: el estilo lo pondrá después CSS.
- Valida en <https://validator.w3.org/> y revisa en DevTools → *Elements* → *Accessibility* que los encabezados forman una lista lineal.

**Pista:** el nivel del encabezado expresa jerarquía, no tamaño; si dudas entre `h2` y `h4`, mira de qué título depende.

#### U7.2 — Mapa de landmarks de una revista

**Nivel:** básico/medio · **Tema:** [07 — Estructura semántica y ARIA](07-estructura-semantica-y-aria.md)

**Enunciado**

La portada de la revista es una pila de `div`: ningún landmark que anunciar, la noticia no se distingue de la barra lateral y el menú no tiene nombre accesible. Asigna el elemento correcto a cada bloque sin mover el contenido.

**Código inicial**

```html title="u7-2-inicial.html"
<body>
  <div class="cabecera">
    <h1>Revista Alameda</h1>
    <div class="menu"><a href="index.html">Portada</a> <a href="cultura.html">Cultura</a> <a href="ciencia.html">Ciencia</a></div>
  </div>
  <div class="principal">
    <div class="noticia">
      <h2>El río que volvió a correr</h2>
      <p>La restauración de la ribera ha recuperado su cauce.</p>
      <h3>Las cifras</h3>
      <p>Se han plantado 4.000 árboles nativos.</p>
    </div>
    <div class="lateral">
      <h2>También te puede interesar</h2>
      <ul><li><a href="agenda.html">Agenda del fin de semana</a></li><li><a href="letras.html">Letras de la semana</a></li></ul>
    </div>
  </div>
  <div class="pie"><p>&copy; 2026 Revista Alameda</p></div>
</body>
```

**Tarea:**

- `div.cabecera` pasa a `<header>` (hijo directo de `<body>`) y `div.menu` a `<nav aria-label="Secciones">`.
- `div.principal` pasa a `<main>`: en la página solo puede haber ==uno==.
- `div.noticia` pasa a `<article>` con un `<header>` interno que envuelva el `h2` y su párrafo de entrada.
- Envuelve "Las cifras" en una `<section>` con su `h3` y convierte `div.lateral` en `<aside>` conservando su `h2`.
- `div.pie` pasa a `<footer>`: solo así es landmark `contentinfo`.
- Comprueba en DevTools → *Elements* → *Accessibility* que aparecen `banner`, `navigation`, `main`, `complementary` y `contentinfo`.

**Pista:** un landmark lo definen el elemento y su posición: `header` y `footer` solo son `banner`/`contentinfo` si son hijos directos de `<body>`.

#### U7.3 — Menú con estado y nombres accesibles

**Nivel:** medio · **Tema:** [07 — Estructura semántica y ARIA](07-estructura-semantica-y-aria.md)

**Enunciado**

En la web de la biblioteca nadie sabe en qué página estás, ni siquiera el lector de pantalla; el botón de búsqueda no tiene nombre accesible y una estrella decorativa se anuncia como una palabra más. Arregla el menú y los nombres con el ARIA justo.

**Código inicial**

```html title="u7-3-inicial.html"
<body>
  <header>
    <h1>Biblioteca Municipal</h1>
    <nav>
      <ul>
        <li><a href="index.html">Inicio</a></li>
        <li><a href="novedades.html">Novedades</a></li>
        <li><a href="catalogo.html">Catálogo</a></li>
      </ul>
    </nav>
    <button type="button"><img src="lupa.svg" alt=""></button>
  </header>
  <main>
    <h2>Novedades de septiembre</h2>
    <p><span class="estrella">★</span> Novedad: "El nombre del viento", de Patrick Rothfuss.</p>
    <p>Reserva en el mostrador o desde tu cuenta.</p>
  </main>
</body>
```

**Tarea:**

- Marca el enlace "Novedades" con `aria-current="page"`: indica ==estás aquí== y el resaltado visual lo pone CSS.
- El `<nav>` no tiene título visible: nómbralo con `aria-label="Principal"`.
- El botón de búsqueda solo contiene una imagen: dale `aria-label="Buscar en el catálogo"` y deja la imagen con `alt=""`.
- La estrella acompaña a texto visible y es decorativa: añade `aria-hidden="true"` a su `<span>`.
- No pongas `aria-label` en los enlaces que ya tienen texto visible: lo ==sobrescribiría== y se anunciaría dos veces.
- Verifica cada nombre accesible en DevTools → *Elements* → *Accessibility*.

**Pista:** el orden del nombre accesible es `aria-labelledby` → `aria-label` → texto visible → `title`.

#### U7.4 — Del div al botón nativo

**Nivel:** avanzado · **Tema:** [07 — Estructura semántica y ARIA](07-estructura-semantica-y-aria.md)

**Enunciado**

En la campaña de solidaridad hay "botones" que no responden al teclado, roles que repiten lo que el HTML ya dice y un enlace cuyo nombre accesible no coincide con su texto visible. Corrígelo con la menor cantidad de ARIA posible.

**Código inicial**

```html title="u7-4-inicial.html"
<body>
  <header>
    <h1>Campaña de solidaridad</h1>
    <nav role="navigation">
      <a href="index.html">Inicio</a>
      <a href="ayuda.html" aria-label="Ir a la página de ayuda">Ayuda</a>
    </nav>
  </header>
  <main>
    <h2>Firma la petición</h2>
    <div role="button" tabindex="0" class="primario" onclick="this.textContent = 'Petición firmada'">Firmar ahora</div>
    <p><span role="button" tabindex="-1">Ver bases</span></p>
  </main>
</body>
```

**Tarea:**

- Cambia los dos `div`/`span` con `role="button"` por `<button type="button">` reales: teclado, foco y nombre accesible llegan ==gratuitos==.
- Elimina `role="navigation"` del `<nav>`: el rol ya lo aporta el propio elemento.
- Quita el `aria-label` del enlace "Ayuda": es ==redundante== con su texto visible y lo sobrescribe.
- Conserva el manejador del primer botón y comprueba con teclado que `Enter` y `Espacio` lo disparan (el `div` no lo hacía).
- Responde por escrito: qué obligaciones desaparecen al usar el nativo (`tabindex`, tecla de activación, estado de foco).
- Abre DevTools → *Elements* → *Accessibility*: los dos botones deben aparecer con rol `button` y nombre accesible igual a su texto visible.

**Pista:** la regla de oro de ARIA: no lo uses si un elemento HTML nativo ya hace ese trabajo.

### Unidad 8 — APIs y funcionalidades nativas {: #ej-u8 }

Aquí sí toca JavaScript: cuatro retos con `data-*`, almacenamiento del navegador, Constraint Validation API, arrastre y geolocalización. Cada solución lleva su `<script>` completo y comentado.

#### U8.1 — Datos en el marcado con data-*

**Nivel:** básico · **Tema:** [08 — APIs y funcionalidades nativas](08-apis-html5.md)

**Enunciado**

El estado de una ficha de apuntes vive en una variable que se pierde al recargar. Pégalo al propio marcado con un atributo `data-*` y léelo desde JavaScript, sin selectores especiales.

**Código inicial**

```html title="u8-1-inicial.html"
<body>
  <article class="ficha" data-estado="borrador" data-id="42">
    <h2>Apuntes de Lenguajes de Marcas</h2>
    <p id="estado">Estado actual: —</p>
    <button type="button" class="publicar">Publicar</button>
  </article>
  <p id="salida"></p>
  <script>
    // TODO: al cargar, muestra data-estado y data-id en #salida con dataset
    // TODO: al pulsar .publicar, escribe dataset.estado y repinta #estado
    // TODO: añade data-id-unidad y comprueba el camelCase en consola
  </script>
</body>
```

**Tarea:**

- Al cargar, lee `data-estado` con `ficha.dataset.estado` y muéstralo en `#salida` junto a `data-id`.
- Al pulsar "Publicar", ejecuta `ficha.dataset.estado = 'publicado'` (eso actualiza el atributo HTML) y repinta `#estado`.
- Añade `data-id-unidad="7"` y comprueba en consola que se lee como `dataset.idUnidad`: pasa a ==camelCase==.
- Comprueba el tipo de dato: `dataset.id` es `"42"`, no `42`; usa `Number(...)` si necesitas calcular.
- Responde: ¿qué imprime `console.log(typeof ficha.dataset.id)` y por qué?

**Pista:** `data-*` es válido en HTML5 y se lee directamente con `elemento.dataset.clave`.

#### U8.2 — Contador de visitas con localStorage

**Nivel:** medio · **Tema:** [08 — APIs y funcionalidades nativas](08-apis-html5.md)

**Enunciado**

La tienda quiere saber cuántas veces has visitado su página y cuándo fue la última vez, con un dato que sobreviva a cerrar el navegador. Guarda un objeto en `localStorage` sin que nada se rompa en la primera visita.

**Código inicial**

```html title="u8-2-inicial.html"
<body>
  <h1>Tienda de barrio</h1>
  <p>Has visitado esta página <strong id="contador">—</strong> veces.</p>
  <p id="ultima">Sin datos todavía.</p>
  <button type="button" id="reiniciar">Reiniciar contador</button>
  <script>
    // TODO: guarda { visitas, ultima } con JSON.stringify en la clave 'visitas-tienda'
    // TODO: léelo con JSON.parse dentro de try/catch, contemplando el primer uso
    // TODO: #reiniciar → removeItem y vuelve a pintar sin recargar
  </script>
</body>
```

**Tarea:**

- Lee la clave `visitas-tienda` con `JSON.parse` dentro de `try/catch`: si está vacía o corrupta, empieza en ==0== (primer uso).
- Incrementa la visita, guarda el objeto `{ visitas, ultima }` con `JSON.stringify` y pinta ambos datos en la página.
- La fecha se guarda como texto legible con `toLocaleString('es-ES')`.
- El botón "Reiniciar" borra la clave con `removeItem` y repinta sin recargar la página.
- Variante: cambia `localStorage` por `sessionStorage` y explica en una frase qué cambia para el usuario.
- No guardes datos sensibles: el almacenamiento es texto plano que puede leer cualquier script del mismo ==origen==.

**Pista:** guardar el objeto tal cual escribe `[object Object]`: pasa siempre por `JSON.stringify`.

#### U8.3 — Validación programática con Constraint Validation API

**Nivel:** medio · **Tema:** [08 — APIs y funcionalidades nativas](08-apis-html5.md)

**Enunciado**

El formulario de inscripción ya lleva `required` y `pattern`, pero necesitas tus propios mensajes de error y saber exactamente qué campo ha fallado y por qué, todo sin recargar la página.

**Código inicial**

```html title="u8-3-inicial.html"
<form id="inscripcion" novalidate>
  <p><label for="nif">NIF</label>
     <input id="nif" name="nif" required pattern="[0-9]{8}[A-Za-z]" placeholder="12345678Z"></p>
  <p><label for="email">Correo electrónico</label>
     <input id="email" name="email" type="email" required></p>
  <button type="submit">Comprobar</button>
  <p id="error" role="alert"></p>
</form>
<script>
  // TODO: submit → e.preventDefault() y form.checkValidity() para el sí/no
  // TODO: motivo → validity.valueMissing / patternMismatch / typeMismatch
  // TODO: en input, setCustomValidity('…') para tu mensaje y ('') para borrarlo
</script>
```

**Tarea:**

- Al enviar, cancela el envío con `preventDefault()` y consulta `form.checkValidity()`; si devuelve `true`, escribe "¡Inscripción correcta!" en `#error`.
- Si falla, distingue el motivo: `nif.validity.valueMissing` → "El NIF es obligatorio"; `nif.validity.patternMismatch` → texto de `nif.validationMessage`; `email.validity.typeMismatch` → mensaje de correo mal formado.
- Mientras se escribe, si el NIF no cumple el patrón, `setCustomValidity('Debe tener 8 dígitos seguidos de una letra')`; en cuanto sea válido, `setCustomValidity('')` (==cadena vacía== = sin error propio).
- Comprueba en consola `nif.validity.valid` antes de corregir el campo y después.
- Responde: ¿por qué `novalidate` en el `<form>` si los atributos `required` y `pattern` siguen ahí?

**Pista:** `validity` no se limita a `true`/`false`: cada estado (`valueMissing`, `patternMismatch`, `typeMismatch`…) te da el ==motivo== exacto.

#### U8.4 — Entrega con arrastre y geolocalización

**Nivel:** avanzado · **Tema:** [08 — APIs y funcionalidades nativas](08-apis-html5.md)

**Enunciado**

El aula virtual admite entregar las prácticas de dos formas: arrastrando la tarea a la bandeja o pulsando su botón. Además, quien entrega "en el centro" puede enviar su posición. Todo nativo, sin librerías.

**Código inicial**

```html title="u8-4-inicial.html"
<body>
  <h1>Entrega de trabajos</h1>
  <ul id="pendientes">
    <li draggable="true" data-tarea="t1">Práctica 1: tabla <button type="button" class="entregar">Entregar</button></li>
    <li draggable="true" data-tarea="t2">Práctica 2: formulario <button type="button" class="entregar">Entregar</button></li>
  </ul>
  <div id="bandeja"><span class="vacio">Arrastra aquí tu entrega</span></div>
  <p id="aviso" role="status"></p>
  <button type="button" id="ubicacion">Estoy en el centro</button>
  <script>
    // TODO: dragstart → dataTransfer.setData y effectAllowed; drop → getData y mover el li
    // TODO: dragover en #bandeja → e.preventDefault() (obligatorio)
    // TODO: #ubicacion → getCurrentPosition traduciendo err.code 1, 2 y 3
  </script>
</body>
```

**Tarea:**

- En `dragstart` de cada `li`: `dataTransfer.setData('text/plain', li.dataset.tarea)` y `effectAllowed = 'move'`.
- En `dragover` sobre `#bandeja`: `e.preventDefault()`; sin esa línea ==drop no se dispara== nunca.
- En `drop`: lee con `getData()`, elimina el aviso `.vacio`, mueve el `li` a la bandeja y anuncia el resultado en `#aviso` (`role="status"`).
- El botón "Entregar" de cada tarea debe producir el mismo resultado para quien no puede arrastrar con el teclado.
- En `#ubicacion`: comprueba `navigator.geolocation` antes de llamar a `getCurrentPosition` y traduce `err.code`: **1** permiso denegado, **2** posición no disponible, **3** *timeout*.
- Recuerda: la geolocalización solo funciona en ==contextos seguros== (`https://` o `localhost`).

**Pista:** el orden de eventos es `dragstart` → `dragover` → `drop`; `preventDefault()` es obligatorio en `dragover` y conviene repetirlo en `drop`.

*[ARIA]: Accessible Rich Internet Applications
