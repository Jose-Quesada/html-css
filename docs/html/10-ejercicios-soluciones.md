---
icon: lucide/check-check
title: "HTML 10 - Ejercicios: soluciones"
description: "Soluciones comentadas de los 10 ejercicios de HTML 09: código completo, puntos clave y errores frecuentes."
modulo: "LMH (0373) / DIW (0615) / DI (0488)"
unidad: 10
fecha: "2026-09-29"
---

# HTML 10 — Ejercicios: soluciones

Soluciones comentadas de los diez retos de [HTML 09 — Ejercicios prácticos](09-ejercicios.md). Cada bloque es **código completo y funcional**: compáralo con tu versión **en lugar de copiarlo**.

## Solución 1 — Desmontando la "divitis"

```html title="solucion-1.html" hl_lines="2 4"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi Página Simple</title>
</head>
<body>
  <!-- header: presentación de la página -->
  <header>
    <h1>Bienvenido a mi Web</h1>
    <!-- nav: solo enlaces de navegación -->
    <nav>
      <ul><li><a href="#">Inicio</a></li><li><a href="#">Sobre Nosotros</a></li><li><a href="#">Contacto</a></li></ul>
    </nav>
  </header>
  <!-- main: contenido único y principal (uno por página) -->
  <main>
    <p>Este es el contenido principal de la página.</p>
    <p>Aquí podríamos hablar de muchos temas interesantes.</p>
  </main>
  <footer>
    <p>&copy; 2026 Mi Web</p>
  </footer>
</body>
</html>
```

**Puntos clave:**

- Solo cambian los ==contenedores==: **el texto no varía**, así que el aspecto tampoco.
- `nav` se anida en `header` cuando la navegación forma **parte de la cabecera**.

**Error frecuente:** repetir `<main>` o dejar el menú como `<div class="menu">`.

## Solución 2 — Artículo semántico

```html title="solucion-2.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Artículo: El Aceite de Oliva</title>
</head>
<body>
  <!-- article: pieza independiente que se entiende por sí sola -->
  <article>
    <header>
      <h1>El Oro Líquido de Andalucía</h1>
      <!-- datetime en formato ISO: la fecha la entienden las máquinas -->
      <p>Por Juan Pérez - <time datetime="2026-06-10">10 de Junio de 2026</time></p>
    </header>
    <p>Andalucía es la cuna del aceite de oliva, un producto esencial en la dieta mediterránea.</p>
    <!-- section: bloque temático con encabezado propio -->
    <section>
      <h2>Variedades Principales</h2>
      <ul><li>Picual</li><li>Hojiblanca</li><li>Arbequina</li></ul>
      <p>Cada variedad aporta matices únicos a nuestro aceite.</p>
    </section>
    <section>
      <h2>Recetas Populares</h2>
      <ul><li>Salmorejo cordobés</li><li>Gazpacho andaluz</li></ul>
    </section>
    <footer>
      <p>Más información en nuestra web.</p>
    </footer>
  </article>
</body>
</html>
```

**Puntos clave:**

- "Recetas" pasa de `h3` a `h2`: cada ==`section`== lleva su **encabezado** y no hay saltos.
- `header` y `footer` internos pertenecen al **artículo**, no a la página.

**Error frecuente:** dos `h1` por página o un `h3` inmediatamente después del `h1`.

## Solución 3 — Portafolio semántico

```html title="solucion-3.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Portafolio de [Tu Nombre]</title>
</head>
<body>
  <header>
    <h1>Portafolio de [Tu Nombre]</h1>
    <nav aria-label="Principal">
      <ul><li><a href="#inicio">Inicio</a></li><li><a href="#proyectos">Proyectos</a></li><li><a href="#contacto">Contacto</a></li></ul>
    </nav>
  </header>
  <main>
    <section id="inicio">
      <h2>¡Hola! Soy [Tu Nombre], desarrollador de interfaces.</h2>
      <p>Creo experiencias web intuitivas y accesibles.</p>
    </section>
    <section id="proyectos">
      <h2>Mis Proyectos</h2>
      <!-- article: cada proyecto es una pieza independiente -->
      <article>
        <h3>Proyecto 1: Tienda Online</h3>
        <p>Interfaz de usuario para productos locales, con foco en móvil.</p>
        <img src="tienda.png" alt="Portada de la tienda en un móvil" width="320" height="200"> <a href="#">Ver proyecto</a>
      </article>
      <article>
        <h3>Proyecto 2: Gestión de Olivos</h3>
        <p>Panel de control con datos en tiempo real.</p>
        <img src="olivos.png" alt="Gráficas de humedad del olivar" width="320" height="200"> <a href="#">Ver proyecto</a>
      </article>
      <article>
        <h3>Proyecto 3: Blog de Gastronomía</h3>
        <p>Blog responsivo de recetas andaluzas.</p>
        <img src="blog.png" alt="Lista de recetas con fotografías" width="320" height="200"> <a href="#">Ver proyecto</a>
      </article>
    </section>
  </main>
  <aside>
    <h3>Contacto</h3>
    <p>Email: <a href="mailto:tu.email@example.com">tu.email@example.com</a></p>
    <p><a href="https://github.com/tuusuario" target="_blank" rel="noopener">GitHub</a></p>
    <figure>
      <img src="avatar.png" alt="Retrato de [Tu Nombre]" width="150" height="150">
      <figcaption>Mi avatar profesional</figcaption>
    </figure>
  </aside>
  <footer>
    <p>&copy; 2026 [Tu Nombre]. Todos los derechos reservados.</p>
  </footer>
</body>
</html>
```

**Puntos clave:**

- Los `id` de las secciones coinciden con los **fragmentos del menú** y hay un único `<main>`.
- `alt` describe la imagen y `figcaption` la contextualiza: no deben ser ==el mismo texto==.

**Error frecuente:** `target="_blank"` sin `rel="noopener"` e imágenes sin `width`/`height`.

## Solución 4 — Noticia completa con detalles

```html title="solucion-4.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Conferencia de IA en Sevilla - Andalucía Tech Hub</title>
</head>
<body>
  <header>
    <h1>Andalucía Tech Hub</h1>
    <nav aria-label="Principal">
      <ul><li><a href="#">Eventos</a></li><li><a href="#">Noticias</a></li><li><a href="#">Recursos</a></li></ul>
    </nav>
  </header>
  <main>
    <article>
      <header>
        <h2>Conferencia Internacional de IA en Sevilla</h2>
        <p>Publicado por Laura García - <time datetime="2026-06-05">5 de Junio de 2026</time></p>
      </header>
      <figure>
        <img src="conferencia.jpg" alt="Auditorio lleno durante la ponencia" width="600" height="300">
        <figcaption>Panorámica del auditorio en la ponencia inaugural.</figcaption>
      </figure>
      <section>
        <h3>Innovación en Andalucía</h3>
        <!-- abbr desarrolla la sigla o abreviatura en el atributo title -->
        <p>Sevilla acogerá la <abbr title="Inteligencia Artificial">Conferencia Internacional de IA</abbr>, que reunirá a expertos de toda Europa.</p>
        <blockquote><p>La tecnología debe estar al servicio de las personas.</p>
          <cite>Laura Méndez, directora del congreso</cite></blockquote>
        <p>Cuenta con el apoyo de la agencia andaluza de innovación (<abbr title="Agencia Andaluza de Innovación">ANDA</abbr>).</p>
      </section>
      <section>
        <h3>Datos del evento</h3>
        <p>Del <time datetime="2026-06-16">16</time> al <time datetime="2026-06-18">18 de Junio de 2026</time>.</p>
        <table>
          <caption>Resumen de la Conferencia IA Sevilla 2026</caption>
          <thead>
            <tr><th scope="col">Concepto</th><th scope="col">Valor</th></tr>
          </thead>
          <tbody>
            <tr><th scope="row">Ponencias</th><td>48</td></tr>
            <tr><th scope="row">Asistentes</th><td>1200</td></tr>
          </tbody>
          <tfoot>
            <tr><th scope="row">Duración</th><td>3 días</td></tr>
          </tfoot>
        </table>
      </section>
      <footer>
        <p>Comparte este evento: #IASevilla2026</p>
      </footer>
    </article>
  </main>
  <footer>
    <p>&copy; 2026 Andalucía Tech Hub</p>
  </footer>
</body>
</html>
```

**Puntos clave:**

- `blockquote` + `cite` marcan **la cita y su fuente**; `abbr` evita repetir la forma completa.
- Tabla con `caption`, `thead` (`scope="col"`), ==cabeceras de fila== (`scope="row"`) y `tfoot`.

**Error frecuente:** tabla de puras `<td>` y `figcaption` idéntico al `alt`.

## Solución 5 — Perfil de usuario con múltiples secciones

```html title="solucion-5.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi Perfil - Mi Plataforma Andalucía</title>
</head>
<body>
  <header>
    <h1>Mi Plataforma Andalucía</h1>
    <nav aria-label="Principal">
      <ul><li><a href="#">Dashboard</a></li><li><a href="#perfil">Mi Perfil</a></li><li><a href="#">Mensajes</a></li></ul>
    </nav>
  </header>
  <main>
    <section id="perfil">
      <header>
        <h2>Mi Perfil de Usuario</h2>
      </header>
      <section>
        <h3>Datos Personales</h3>
        <form action="/update-profile" method="post">
          <!-- fieldset + legend: grupo con título accesible -->
          <fieldset>
            <legend>Información de contacto</legend>
            <p><label for="nombre">Nombre</label> <input type="text" id="nombre" name="nombre" required autocomplete="name"></p>
            <p><label for="email">Correo electrónico</label> <input type="email" id="email" name="email" required></p>
            <p><label for="telefono">Teléfono</label> <input type="tel" id="telefono" name="telefono"></p>
          </fieldset>
          <button type="submit">Guardar cambios</button>
        </form>
      </section>
      <section>
        <h3>Actividad Reciente</h3>
        <ol>
          <li>Mensaje a Soporte Técnico - <time datetime="2026-09-28T14:30">ayer, 14:30</time></li>
          <li>Proyecto visitado - <time datetime="2026-09-27T10:15">27 de Septiembre, 10:15</time></li>
        </ol>
      </section>
      <section>
        <h3>Preferencias de la Cuenta</h3>
        <form action="/update-preferences" method="post">
          <fieldset>
            <legend>Notificaciones y opciones</legend>
            <p><input type="checkbox" id="notif-email" name="notif-email" checked> <label for="notif-email">Avisos por email</label></p>
            <p><input type="checkbox" id="notif-sms" name="notif-sms"> <label for="notif-sms">Avisos por SMS</label></p>
            <p><label for="idioma">Idioma preferido</label> <select id="idioma" name="idioma"><option value="es" selected>Español</option><option value="en">English</option></select></p>
          </fieldset>
          <button type="submit">Actualizar preferencias</button>
        </form>
      </section>
    </section>
  </main>
  <aside>
    <h3>Acciones rápidas</h3>
    <ul><li><a href="#">Cambiar contraseña</a></li><li><a href="#">Gestionar suscripciones</a></li></ul>
  </aside>
  <footer>
    <p>&copy; 2026 Mi Plataforma Andalucía</p>
  </footer>
</body>
</html>
```

**Puntos clave:**

- **Jerarquía de títulos** coherente: `h2` global del perfil y `h3` por bloque.
- Cada `label` apunta con `for` al `id` de su campo: pulsar el texto lleva el ==foco== al control.

**Error frecuente:** `label` sin `for` y casillas sin etiqueta asociada.

## Solución 6 — Procesamiento de vídeo con canvas

**Respuestas al quiz:**

- **¿Por qué el canvas está vacío al cargar?** `<canvas>` es un contenedor sin fuente: dibuja cuando JavaScript ejecuta el primer `drawImage` al empezar la reproducción.
- **¿Por qué de 4 en 4?** `ImageData.data` guarda RGBA: cuatro posiciones por píxel (rojo, verde, azul y alfa).
- **`setInterval` en vez de `requestAnimationFrame`:** pierde fluidez: `rAF` se sincroniza con el refresco y se pausa en pestañas ocultas; `setInterval` corre "a ciegas".
- **`gris = canal verde`:** sigue en blanco y negro, pero cambia la luminosidad: los rojos salen negros y los verdes, muy brillantes.

**Filtro de escala de grises (`script.js`):**

```javascript title="script.js" hl_lines="2 4"
const video = document.getElementById('videoOriginal');
const canvas = document.getElementById('canvasFiltrado');
// willReadFrequently optimiza el getImageData repetido cada fotograma
const ctx = canvas.getContext('2d', { willReadFrequently: true });

function procesarFrame() {
  if (video.paused || video.ended) return;

  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
  const frame = ctx.getImageData(0, 0, canvas.width, canvas.height);
  const data = frame.data;

  // Avanzamos de 4 en 4: R, G, B y A de cada píxel
  for (let i = 0; i < data.length; i += 4) {
    const gris = 0.2126 * data[i] + 0.7152 * data[i + 1] + 0.0722 * data[i + 2];
    data[i] = gris;
    data[i + 1] = gris;
    data[i + 2] = gris;
    // data[i + 3] es el alfa: no se toca
  }

  ctx.putImageData(frame, 0, 0);
  requestAnimationFrame(procesarFrame);
}

video.addEventListener('play', procesarFrame);
```

**Marcado asociado:**

```html title="solucion-6.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Taller Multimedia - Interfaces</title>
</head>
<body>
  <header>
    <h1>Procesamiento de Vídeo en Tiempo Real</h1>
    <p>Módulo: Diseño de Interfaces Web (DAW)</p>
  </header>
  <main>
    <figure>
      <!-- Sin crossorigin, getImageData lanza un error de seguridad -->
      <video id="videoOriginal" crossorigin="anonymous" controls autoplay muted loop>
        <source src="video_jaen.mp4" type="video/mp4">
        Tu navegador no soporta vídeo.
      </video>
      <figcaption>Entrada: Vídeo Original</figcaption>
    </figure>
    <figure>
      <canvas id="canvasFiltrado" width="400" height="225">Tu navegador no soporta canvas.</canvas>
      <figcaption>Salida: Filtro Escala de Grises</figcaption>
    </figure>
  </main>
  <script src="script.js"></script>
</body>
</html>
```

**Puntos clave:**

- El bucle arranca en el evento `play` y se corta solo cuando el vídeo está ==en pausa==.
- El canal alfa (`i + 3`) **no se modifica**: tocarlo volvería transparente el lienzo.

**Error frecuente:** olvidar `crossorigin` o recorrer el array de 1 en 1 desalineando los píxeles.

## Solución 7 — Formulario de matrícula

```html title="solucion-7.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Formulario de matrícula</title>
</head>
<body>
  <main>
    <h1>Matrícula del próximo curso</h1>
    <form action="/matricula" method="post">
      <fieldset>
        <legend>Datos del estudiante</legend>
        <p><label for="nombre">Nombre y apellidos</label> <input type="text" id="nombre" name="nombre" required></p>
        <p><label for="email">Correo electrónico</label> <input type="email" id="email" name="email" required></p>
        <!-- date muestra el selector nativo y valida el formato -->
        <p><label for="nacimiento">Fecha de nacimiento</label> <input type="date" id="nacimiento" name="nacimiento" required></p>
        <p><label for="edad">Edad</label> <input type="number" id="edad" name="edad" min="16" max="99" required></p>
        <!-- pattern valida una expresión regular; title explica el error -->
        <p><label for="nif">NIF</label> <input type="text" id="nif" name="nif" pattern="[0-9]{8}[A-Za-z]" title="Ocho dígitos y una letra, p. ej. 12345678Z" required> <!-- (1)! --></p>
      </fieldset>
      <fieldset>
        <legend>Datos académicos</legend>
        <!-- datalist sugiere valores sin impedir escribir otro -->
        <p><label for="ciclo">Ciclo formativo</label> <input type="text" id="ciclo" name="ciclo" list="ciclos" required>
          <datalist id="ciclos"><option value="DAM"></option><option value="DAW"></option><option value="SMR"></option><option value="IFCT-videojuegos"></option></datalist> <!-- (2)! -->
        </p>
        <p><label for="observaciones">Observaciones</label> <textarea id="observaciones" name="observaciones" rows="4"></textarea></p>
      </fieldset>
      <button type="submit">Enviar matrícula</button>
    </form>
  </main>
</body>
</html>
```

1.  `pattern` se compara con **todo el valor** del campo y `title` es el texto que el navegador muestra cuando la expresión no coincide.

2.  `datalist` sugiere los ciclos **sin impedir** escribir otro: se asocia al input con `list="ciclos"` ↔ `id="ciclos"`.

**Puntos clave:**

- La validación es **nativa**: `required`, `email`, `date`, `min`/`max` y `pattern` funcionan **sin JavaScript**.
- `datalist` (`list="ciclos"` ↔ `id="ciclos"`) sugiere ==sin cerrar la opción==; para cerrarla se usa `<select>`.

!!! warning "Error común"

    `label` sin `for`, `pattern` sin `title` y campos obligatorios sin `required`.

## Solución 8 — Horario de clase accesible

```html title="solucion-8.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Horario de 1º DAM</title>
</head>
<body>
  <main>
    <h1>Horario semanal</h1>
    <figure>
      <table>
        <!-- caption: título accesible de la tabla -->
        <caption>Horario del grupo 1º DAM - Curso 2026/2027</caption>
        <colgroup><col style="width: 120px"></colgroup>
        <thead>
          <tr><th scope="col">Hora</th><th scope="col">Lunes</th><th scope="col">Miércoles</th><th scope="col">Viernes</th></tr>
        </thead>
        <tbody>
          <tr><th scope="row">08:00-09:00</th><td>LMH</td><td>DIW</td><td>DI</td></tr>
          <!-- colspan cubre el hueco de esa hora -->
          <tr><th scope="row">09:00-10:00</th><td>LMH</td><td colspan="2">Hora de patrocinio</td></tr>
          <tr><th scope="row">10:00-11:00</th><td colspan="2">Proyecto</td><td>DIW</td></tr>
        </tbody>
        <tfoot>
          <tr><th scope="row">Total</th><td colspan="3">12 horas semanales lectivas</td></tr>
        </tfoot>
      </table>
      <figcaption>Los huecos indican grupos desdoblados.</figcaption>
    </figure>
  </main>
</body>
</html>
```

**Puntos clave:**

- ==`scope`== declara si un `th` describe columna o fila: así el lector anuncia "Lunes, LMH".
- Todas las filas suman **4 celdas** contando `colspan`.

!!! warning "Error común"

    `th` sin `scope`, encabezados como `<td>` en negrita y `colspan` que desalinea la tabla.

## Solución 9 — Galería accesible

```html title="solucion-9.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Galería del ciclo</title>
</head>
<body>
  <main id="galeria">
    <h1>Galería del ciclo</h1>
    <figure>
      <!-- srcset: versiones disponibles; sizes: ancho previsto en cada caso -->
      <img src="taller-800.jpg"
           srcset="taller-400.jpg 400w, taller-800.jpg 800w, taller-1600.jpg 1600w" <!-- (1)! -->
           sizes="(max-width: 600px) 100vw, 50vw"
           width="800" height="533"
           alt="Alumnos soldando placas en el taller de electrónica">
      <figcaption>Alumnos en el taller de electrónica.</figcaption>
    </figure>
    <p><a href="taller-1600.jpg" download="taller-1600.jpg">Descargar la foto en alta (JPG, 1,2 MB)</a></p>
    <figure>
      <!-- poster: imagen de portada; track: subtítulos accesibles -->
      <video controls poster="promo-poster.jpg" width="640" height="360">
        <source src="promo.mp4" type="video/mp4">
        <track kind="subtitles" src="promo-es.vtt" srclang="es" label="Español" default> <!-- (2)! -->
        <track kind="captions" src="promo-en.vtt" srclang="en" label="English">
        Tu navegador no soporta la reproducción de vídeo.
      </video>
      <figcaption>Vídeo promocional del ciclo.</figcaption>
    </figure>
  </main>
  <footer>
    <p>&copy; 2026 IES Maya</p>
  </footer>
</body>
</html>
```

1.  `srcset` enumera las **versiones disponibles** y `sizes` dice en qué ancho se mostrará cada una; sin esa pareja, el navegador elige a ciegas.

2.  El `<track>` de subtítulos hace el vídeo accesible para personas sordas o con el sonido apagado; `default` marca el idioma que se muestra primero.

**Puntos clave:**

- Sin ==`sizes`==, el navegador no sabe dónde se mostrará la imagen y elige a ciegas entre las de `srcset`.
- El texto del enlace de descarga informa de **formato y peso**.

**Error frecuente:** vídeos sin `track` (inaccesibles para personas sordas) y enlaces "ver imagen" redundantes.

## Solución 10 — Mini web con landmarks y skip link

```html title="solucion-10.html" hl_lines="2 4"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IES Maya</title>
  <link rel="stylesheet" href="estilos.css">
</head>
<body>
  <!-- Primer elemento del body: ahí cae el foco inicial (en estilos.css se oculta hasta el :focus) -->
  <a class="skip-link" href="#contenido">Saltar al contenido principal</a> <!-- (1)! -->
  <header>
    <h1>IES Maya</h1>
    <nav aria-label="Principal">
      <button id="btn-menu" type="button" aria-expanded="false" aria-controls="menu-lista" aria-label="Menú principal">Menú</button>
      <ul id="menu-lista" hidden><li><a href="#inicio">Inicio</a></li><li><a href="#ciclos">Ciclos</a></li><li><a href="#contacto">Contacto</a></li></ul>
    </nav>
  </header>
  <!-- tabindex="-1" permite enfocar el main por script sin meterlo en el tabulador -->
  <main id="contenido" tabindex="-1">
    <section id="inicio">
      <h2>Inicio</h2>
      <p>Bienvenido al IES Maya.</p>
    </section>
    <!-- Región viva: los cambios de texto se anuncian solos -->
    <div id="avisos" role="status">No hay avisos nuevos.</div>
    <section id="contacto">
      <h2>Contacto</h2>
      <form id="form-contacto">
        <p><label for="motivo">Motivo de la consulta</label> <input type="text" id="motivo" name="motivo" required></p>
        <p><label for="curso">Curso</label>
          <select id="curso" name="curso" required>
            <option value="daw">DAW</option>
            <option value="dam">DAM</option>
          </select>
        </p>
        <button type="submit">Enviar consulta</button>
      </form>
    </section>
  </main>
  <aside><h2>Avisos del centro</h2><ul><li>Tutorías: martes de 16:00 a 18:00</li></ul></aside>
  <footer>
    <p>&copy; 2026 IES Maya</p>
  </footer>
  <script>
    const btn = document.getElementById('btn-menu');
    const lista = document.getElementById('menu-lista');

    // El botón alterna visibilidad y estado accesible a la vez
    btn.addEventListener('click', () => {
      const abierto = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!abierto));
      lista.hidden = abierto;
    });

    // El skip link traslada el foco real al main
    document.querySelector('.skip-link').addEventListener('click', () => document.getElementById('contenido').focus());

    const form = document.getElementById('form-contacto');
    form.addEventListener('submit', (evento) => {
      evento.preventDefault();
      document.getElementById('avisos').textContent = 'Consulta enviada. Te responderemos en 48 horas.';
      form.reset();
    });
  </script>
</body>
</html>
```

1.  Debe ser el **primer elemento** del `<body>`: así el primer `Tab` lo alcanza antes que al menú y, con el foco visible, solo se muestra al recibir foco.

**Puntos clave:**

- Orden de ==landmarks== predecible: skip link → `header` → `nav` → `main` → `aside` → `footer`, con un único `main`.
- `aria-expanded` cambia junto al estado real del menú; `role="status"` anuncia los avisos **sin robar el foco**.

!!! warning "Error común"

    Un `<div onclick>` haciendo de botón (no enfocable ni anuncia estado) o `aria-expanded` dejado en `false`.
