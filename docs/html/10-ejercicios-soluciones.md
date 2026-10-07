---
icon: lucide/check-check
title: "HTML 10 - Ejercicios: soluciones"
description: "Soluciones comentadas de los 42 ejercicios de HTML 09 (10 globales + 32 por unidad): código completo, puntos clave y errores frecuentes."
modulo: "LMH (0373) / DIW (0615) / DI (0488)"
unidad: 10
fecha: "2026-09-29"
---

# HTML 10 — Ejercicios: soluciones

Soluciones comentadas de los **42 retos** de [HTML 09 — Ejercicios prácticos](09-ejercicios.md): los diez globales y los treinta y dos por unidad (`U1.1` … `U8.4`). Cada bloque es **código completo y funcional**: compáralo con tu versión **en lugar de copiarlo**.

## Solución 1 — Desmontando la "divitis"

```html title="solucion-1.html" hl_lines="10 13 18 22"
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
      <p>Por Juan Pérez - <time datetime="2026-06-10">10 de junio de 2026</time></p>
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
        <img src="https://dummyimage.com/800x600/ccc/000.png&text=tienda.png" alt="Portada de la tienda en un móvil" width="320" height="200"> <a href="#">Ver proyecto</a>
      </article>
      <article>
        <h3>Proyecto 2: Gestión de Olivos</h3>
        <p>Panel de control con datos en tiempo real.</p>
        <img src="https://dummyimage.com/800x600/ccc/000.png&text=olivos.png" alt="Gráficas de humedad del olivar" width="320" height="200"> <a href="#">Ver proyecto</a>
      </article>
      <article>
        <h3>Proyecto 3: Blog de Gastronomía</h3>
        <p>Blog responsivo de recetas andaluzas.</p>
        <img src="https://dummyimage.com/800x600/ccc/000.png&text=blog.png" alt="Lista de recetas con fotografías" width="320" height="200"> <a href="#">Ver proyecto</a>
      </article>
    </section>
  </main>
  <aside id="contacto">
    <h3>Contacto</h3>
    <p>Email: <a href="mailto:tu.email@example.com">tu.email@example.com</a></p>
    <p><a href="https://github.com/tuusuario" target="_blank" rel="noopener">GitHub</a></p>
    <p><a href="https://www.linkedin.com/in/tuusuario" target="_blank" rel="noopener">LinkedIn</a></p>
    <figure>
      <img src="https://dummyimage.com/200x200/ccc/000.png&text=avatar.png" alt="Retrato de [Tu Nombre]" width="150" height="150">
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

- Los tres `id` del menú (`inicio`, `proyectos`, `contacto`) existen todos en la página y hay un único `<main>`.
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
        <p>Publicado por Laura García - <time datetime="2026-06-05">5 de junio de 2026</time></p>
      </header>
      <figure>
        <img src="https://dummyimage.com/800x600/ccc/000.png&text=conferencia.jpg" alt="Auditorio lleno durante la ponencia" width="600" height="300">
        <figcaption>Panorámica del auditorio en la ponencia inaugural.</figcaption>
      </figure>
      <section>
        <h3>Innovación en Andalucía</h3>
        <!-- abbr desarrolla la sigla o abreviatura en el atributo title -->
        <p>Sevilla acogerá la Conferencia Internacional de <abbr title="Inteligencia Artificial">IA</abbr>, que reunirá a expertos de toda Europa.</p>
        <blockquote><p>La tecnología debe estar al servicio de las personas.</p>
          <cite>Laura Méndez, directora del congreso</cite></blockquote>
        <p>Cuenta con el apoyo de la agencia andaluza de innovación (<abbr title="Agencia Andaluza de Innovación">ANDA</abbr>).</p>
      </section>
      <section>
        <h3>Datos del evento</h3>
        <p>Del <time datetime="2026-06-16">16</time> al <time datetime="2026-06-18">18 de junio de 2026</time>.</p>
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
          <li>Mensaje a Soporte Técnico - <time datetime="2026-09-28T14:30">28 de septiembre, 14:30</time></li>
          <li>Proyecto visitado - <time datetime="2026-09-27T10:15">27 de septiembre, 10:15</time></li>
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

// Mini reto: alterna entre el filtro y el fotograma original sin recargar
let grisActivo = true;
document.getElementById('btn-filtro').addEventListener('click', (evento) => {
  grisActivo = !grisActivo;
  evento.currentTarget.textContent = grisActivo ? 'Mostrar original' : 'Mostrar escala de grises';
});

function procesarFrame() {
  if (video.paused || video.ended) return;

  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

  // El fotograma se dibuja siempre; la luminancia solo si el filtro está activo
  if (grisActivo) {
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
  }

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
      <!-- Mini reto: alterna entre el filtro y el fotograma original -->
      <p><button id="btn-filtro" type="button">Mostrar original</button></p>
    </figure>
  </main>
  <script src="script.js"></script>
</body>
</html>
```

**Puntos clave:**

- El bucle arranca en el evento `play` y se corta solo cuando el vídeo está ==en pausa==.
- El canal alfa (`i + 3`) **no se modifica**: tocarlo volvería transparente el lienzo.
- El **mini reto** solo envuelve la luminancia en `if (grisActivo)`: el fotograma se dibuja en todo caso y el botón actualiza su texto con `textContent`.

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
        <p><label for="nacimiento">Fecha de nacimiento</label> <input type="date" id="nacimiento" name="nacimiento"></p>
        <p><label for="edad">Edad</label> <input type="number" id="edad" name="edad" min="16" max="99"></p>
        <!-- pattern valida una expresión regular; title explica el error -->
        <p><label for="nif">NIF</label> <input type="text" id="nif" name="nif" pattern="[0-9]{8}[A-Za-z]" title="Ocho dígitos y una letra, p. ej. 12345678Z"> <!-- (1)! --></p>
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
          <tr><th scope="row">Total</th><td colspan="3">7 horas semanales lectivas</td></tr>
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
      <img src="https://dummyimage.com/800x600/ccc/000.png&text=taller-800.jpg"
           srcset="https://dummyimage.com/400x300/ccc/000.png&text=taller-400.jpg 400w, https://dummyimage.com/800x600/ccc/000.png&text=taller-800.jpg 800w, https://dummyimage.com/800x600/ccc/000.png&text=taller-1600.jpg 1600w" <!-- (1)! -->
           sizes="(max-width: 600px) 100vw, 50vw"
           width="800" height="533"
           alt="Alumnos soldando placas en el taller de electrónica">
      <figcaption>Alumnos en el taller de electrónica.</figcaption>
    </figure>
    <p><a href="taller-1600.jpg" download="taller-1600.jpg">Descargar la foto en alta (JPG, 1,2 MB)</a></p>
    <figure>
      <!-- poster: imagen de portada; track: subtítulos accesibles -->
      <video controls poster="https://dummyimage.com/800x600/ccc/000.png&text=promo-poster.jpg" width="640" height="360">
        <source src="promo.mp4" type="video/mp4">
        <track kind="subtitles" src="promo-es.vtt" srclang="es" label="Español" default> <!-- (2)! -->
        <track kind="subtitles" src="promo-en.vtt" srclang="en" label="English">
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

```html title="solucion-10.html" hl_lines="11 15 26"
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
    <section id="ciclos">
      <h2>Ciclos</h2>
      <p>DAM, DAW y SMR.</p>
    </section>
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


## Soluciones por unidad

Soluciones completas de los **32 ejercicios por unidad** de [HTML 09 — Ejercicios prácticos](09-ejercicios.md). Mismo orden y numeración (U1.1 … U8.4) que los enunciados.

### Unidad 1 — Introducción a HTML5 {: #sol-u1 }

#### U1.1 — La plantilla del ciclo desde cero

```html title="u1-1.html"
<!DOCTYPE html> <!-- Declaración HTML5: activa el modo estándar, no es una etiqueta -->
<html lang="es"> <!-- Raíz del documento; lang = idioma del contenido -->
<head>
  <!-- Trío clave del head: charset, viewport y title -->
  <meta charset="UTF-8"> <!-- ñ, tildes y €: dentro de los primeros 1024 bytes -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Web del ciclo de DAM y DAW del IES Maya.">
  <title>Ciclos DAM y DAW · IES Maya</title> <!-- Título único de la pestaña -->
</head>
<body>
  <!-- Empieza aquí TODO el contenido visible -->
  <header>
    <h1>Ciclos DAM y DAW · IES Maya</h1>
  </header>
  <main>
    <!-- main: contenido único y principal de esta página (solo uno por página) -->
    <h2>Bienvenidos</h2>
    <p>Impartimos Desarrollo de Aplicaciones Multiplataforma y Web en Málaga.</p>
    <p>Matrícula abierta del 1 al 30 de septiembre de 2026.</p>
  </main>
  <footer>
    <p>&copy; 2026 IES Maya</p>
  </footer>
</body>
</html>
```

**Puntos clave:**

- ==`<!DOCTYPE html>`== es la declaración que activa el modo estándar; sin ella caerías en *quirks mode*.
- El ==trío clave== va al principio del `<head>` y `lang="es"` en la raíz: sin ellos aparecen `Ãñ` y un lector con acento inglés.
- Un solo `<main>`, etiquetas en minúsculas y cierres en orden inverso.

**Error frecuente:** olvidar `lang="es"` o dejar el `charset` fuera del `<head>`: el validador lo tilda, el navegador lo disimula.

#### U1.2 — El `head` roto: cuatro fallos silenciosos

```html title="u1-2.html"
<!DOCTYPE html>
<html lang="es"> <!-- 1) Declaración + idioma de la raíz -->
<head>
  <meta charset="UTF-8"> <!-- 2) UTF-8 y el PRIMER elemento del head -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- 3) Responsivo -->
  <meta name="description" content="Página del ciclo de DAM y DAW del IES Maya.">
  <title>Ciclos DAM y DAW · IES Maya</title> <!-- 4) Título único, no el de plantilla -->
  <link rel="stylesheet" href="css/estilos.css">
</head>
<body>
  <h1>Ciclos DAM y DAW</h1>
  <p>Matrícula abierta del 1 al 30 de septiembre de 2026.</p>
</body>
</html>
```

**Puntos clave:**

- El ==`charset`== va primero en el `<head>`: si aparece tarde, los 1024 bytes iniciales ya se han interpretado con la codificación equivocada.
- `viewport` es obligatorio en responsivo: sin él el móvil renderiza a ~980 px.
- `title` es obligatorio y único por página: es lo que se ve en la pestaña y en el resultado de búsqueda.

**Error frecuente:** cambiar el texto a UTF-8 y olvidar la etiqueta (o dejar `iso-8859-1`): el fichero ya no es lo que el navegador cree que es.

#### U1.3 — Entidades y booleanos de la chuleta

```html title="u1-3.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chuleta de HTML5 del ciclo</title>
</head>
<body>
  <h1>Chuleta de HTML5 del ciclo</h1>
  <!-- &lt; y &gt; muestran la etiqueta como texto; sin ellas el link se "come" el párrafo -->
  <p>Para enlazar el CSS escribe: <code>&lt;link rel="stylesheet" href="estilos.css"&gt;</code></p>
  <!-- El & de texto plano siempre como entidad -->
  <p>HTML &amp; CSS, más JavaScript. &copy; 2026 IES Maya</p>
  <!-- &nbsp; impide que se parta la fecha y la hora -->
  <p>El examen es el 15&nbsp;de&nbsp;mayo a las 9:30&nbsp;h.</p>
  <form action="/acceso" method="post">
    <!-- Booleanos: su presencia basta, nunca llevan valor -->
    <p>Usuario: <input type="text" name="usuario" required></p>
    <p><input type="checkbox" name="recordar" checked> Recordarme</p>
    <p>Matrícula: <input type="text" name="matricula" value="2026-DAW-0142" disabled></p>
  </form>
</body>
</html>
```

**Puntos clave:**

- ==Entidades== obligatorias para `<`, `>` y `&`; con UTF-8 los acentos y la ñ van directos.
- `&nbsp;` une lo que no debe saltar de línea, pero no sirve para "empujar" el diseño (eso es CSS).
- ==Atributos booleanos== sin valor: `required="true"` es redundante y `checked="false"` sigue marcado.

**Error frecuente:** creer que `disabled="no"` desactiva el atributo: al contrario, lo activa, porque existe.

#### U1.4 — HTML heredado: cierres en cruz y en MAYÚSCULAS

```html title="u1-4.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Taller de iniciación a HTML</title>
</head>
<body>
  <!-- Todo en minúsculas: convención de MDN y W3C (y requisito si se sirve como XHTML) -->
  <h1 class="titulo">Taller de iniciación a HTML</h1>
  <div>
    <!-- Cierres en orden inverso: primero </strong>, después </p> -->
    <p>Este taller enseña <strong>HTML semántico.</strong></p>
    <p>Se imparte en el <em>IES Maya</em>.</p>
  </div>
  <ul>
    <li>Semana 1: estructura del documento</li>
    <li>Semana 2: texto y semántica</li>
  </ul>
  <p><a href="matricula.html">Matricularme</a></p>
</body>
</html>
```

**Puntos clave:**

- ==Anidamiento== correcto: `</strong>` se cierra dentro del `<p>`; el texto visible no ha cambiado ni una letra.
- HTML no distingue mayúsculas, pero se escriben en ==minúsculas== por convención y por compatibilidad futura con XHTML/XML.
- La plantilla completa (`<!DOCTYPE>`, `lang`, `charset`, `viewport`, `title`) es obligatoria también en un fragmento heredado.

**Error frecuente:** fiarse de que "el navegador lo arregla": el árbol DOM resultante no es el que diseñaste y CSS, JavaScript y lectores de pantalla trabajan con ese otro árbol.

#### U1.5 — Auditoría y reparación integral del esqueleto corporativo

```html title="u1-5-solucion.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Landing Page Oficial | IES F3</title>
  
  <!-- Soporte PWA y visualización -->
  <meta name="theme-color" content="#1e40af">
  <link rel="manifest" href="/manifest.json">
  <link rel="apple-touch-icon" href="/icon-192.png">
  
  <!-- Resource Hints (Aceleradores de rendimiento) -->
  <link rel="preconnect" href="https://cdn.iesf3.es">
  <link rel="preload" href="/fonts/roboto.woff2" as="font" type="font/woff2" crossorigin>
  
  <!-- Sindicación -->
  <link rel="alternate" type="application/rss+xml" title="Noticias IES F3" href="/feed.xml">
  
  <!-- Datos Estructurados (Schema.org) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "EducationalOrganization",
    "name": "IES F3",
    "description": "Formación Profesional de Alto Rendimiento en Informática"
  }
  </script>
</head>
<body>
  <h1 class="titulo_principal">Bienvenido al IES F3</h1>
  <div>
    <p>Formación Profesional de <strong>Alto Rendimiento.</strong></p>
  </div>
  <form action="/contacto" method="post">
    <p>Acepto las condiciones: <input type="checkbox" name="terminos" checked></p>
    <p><button type="submit" disabled>Enviar</button></p>
  </form>
</body>
</html>
```

**Puntos clave:**

- **HTML5 nativo y puro:** Eliminación absoluta de `xmlns` y `xml:lang` en favor de un simple `<html lang="es">`.
- **Atributos booleanos modernos:** En HTML5, los atributos booleanos (`checked`, `disabled`, `required`) no necesitan valor; basta con su simple existencia.
- **Rendimiento e Integración PWA:** Incorporación de `<link rel="preload">` y `<link rel="preconnect">` junto a metadatos PWA esenciales, elevando un marcado anticuado a los estándares web del 2026.
- **Schema.org y SEO Semántico:** El uso de JSON-LD proporciona contexto claro y determinista para los motores de búsqueda, superando cualquier etiqueta meta antigua.

**Error frecuente:** Conservar el cierre de las etiquetas vacías estilo XHTML (`/>`) o mantener el viejo charset de ISO-8859-1 que puede corromper caracteres españoles en un servidor moderno que sirva todo como UTF-8 por defecto.

### Unidad 2 — Texto y semántica de contenido {: #sol-u2 }

#### U2.1 — Esquema de encabezados a contracorriente

```html title="u2-1.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ciclo DAM · IES Maya</title>
</head>
<body>
  <!-- Un solo h1: el tema de toda la página -->
  <h1>Ciclo DAM · IES Maya</h1>
  <h2>Qué es DAM</h2>
  <p>Desarrollo de Aplicaciones Multiplataforma: 2.000 horas en dos cursos.</p>
  <h2>Módulos destacados</h2>
  <p>Programación, bases de datos y lenguajes de marcado.</p>
  <h2>Salidas profesionales</h2>
  <p>Desarrollo de escritorio, soporte técnico y testing.</p>
  <!-- h3 sí: es subsección de "Salidas profesionales" -->
  <h3>Feria del Software Andaluz</h3>
  <p>Del 12 al 14 de noviembre en Sevilla.</p>
</body>
</html>
```

**Puntos clave:**

- Esquema final `h1 → h2 → h2 → h2 → h3`: ==un solo `h1`== y ningún nivel saltado.
- El segundo `h1` ("Salidas profesionales") baja a `h2`: los encabezados se eligen por **jerarquía**, no por tamaño.
- El texto de cada encabezado resume su bloque, que es lo que leen lectores de pantalla y buscadores.

**Error frecuente:** repetir `h1` a mitad de página y usar `h4` "para que salga más pequeño": el tamaño lo decide CSS, no el nivel.

#### U2.2 — La guía de matrícula en cuatro listas

```html title="u2-2.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Guía de matrícula de DAW</title>
</head>
<body>
  <h1>Guía de matrícula de DAW</h1>
  <h2>Pasos pendientes</h2>
  <!-- start fija el primer número: los dos primeros pasos ya se dieron en la tutoría -->
  <ol start="3">
    <li>Entregar la hoja firmada en secretaría</li>
    <li>Pagar las tasas</li>
    <li>Guardar el justificante</li>
  </ol>
  <h2>Cuenta atrás para el cierre</h2>
  <!-- start + reversed: numera 5, 4, 3, 2, 1 sin escribir el número en el texto -->
  <ol start="5" reversed>
    <li>Publicar el aviso en la web y por correo</li>
    <li>Segundo aviso a los pendientes</li>
    <li>Última llamada de secretaría</li>
    <li>Cierre del plazo a las 23:59</li>
    <li>Lista definitiva de admitidos</li>
  </ol>
  <h2>Qué necesitas</h2>
  <!-- ul: el orden no importa -->
  <ul>
    <li>DNI en vigor</li>
    <li>Certificado digital</li>
    <li>Foto tipo carnet</li>
    <li>Hoja de matrícula descargada</li>
  </ul>
  <h2>Glosario</h2>
  <!-- dl: término (dt) y descripción (dd) -->
  <dl>
    <dt>DAW</dt>
    <dd>Desarrollo de Aplicaciones Web.</dd>
    <dt>SMR</dt>
    <dd>Mantenimiento de Sistemas Microinformáticos.</dd>
    <dt>FP</dt>
    <dd>Formación Profesional.</dd>
  </dl>
</body>
</html>
```

**Puntos clave:**

- El número visible lo pinta la lista: ==`start`== fija el primero y `reversed` cuenta hacia atrás.
- `<ul>`/`<ol>` solo aceptan `<li>` como hijo directo; para términos y definiciones existe ==`<dl>`== (`dt` + `dd`).
- El orden decide la etiqueta: pasos en `ol`, material en `ul`, nunca al revés.

**Error frecuente:** numeración escrita a mano en el texto ("3) entregar…") y párrafos sueltos dentro de la lista.

#### U2.3 — Avisos: importancia, énfasis y separadores

```html title="u2-3.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Avisos del centro · IES Maya</title>
</head>
<body>
  <h1>Avisos del centro</h1>
  <!-- Rótulo decorativo: no es importancia; el aspecto lo pondrá CSS -->
  <p><span class="destacado">Secretaría</span> abre de 8:00 a 14:00.</p>
  <!-- br solo cuando el salto forma parte del texto (dirección) -->
  <address>
    IES Maya<br>
    Calle Rioja, 12<br>
    29018 Málaga<br>
    <a href="mailto:secretaria@iesmaya.es">secretaria@iesmaya.es</a>
  </address>
  <p><span class="destacado">Convocatoria</span> extraordinaria de Lenguajes de Marcado: el <em>22 de julio</em>.</p>
  <p><span class="destacado">Matrícula</span> del curso 2026/2027: del 1 al 30 de septiembre.</p>
  <!-- strong: importancia real, el lector lo anuncia con más fuerza -->
  <p><strong>Importante:</strong> no se aceptarán matrículas fuera de plazo.</p>
  <!-- hr: cambio de tema, no adorno horizontal -->
  <hr>
  <p><span class="destacado">Exámenes</span> del primer trimestre: del 12 al 23 de enero.</p>
</body>
</html>
```

**Puntos clave:**

- ==`<strong>`== queda solo donde hay importancia real; lo demás era negrita decorativa y va en `<span>` con clase.
- `<em>` marca énfasis de pronunciación (la fecha), no "texto que quería que se viera distinto".
- `<br>` solo dentro de la dirección, `<hr>` marca el ==cambio de tema== y `<address>` agrupa el contacto del centro.

**Error frecuente:** `<strong>` por estética y `<br>` para fabricar párrafos: se ve igual, pero no hay estructura que lea nadie.

#### U2.4 — Ficha de la ruta del Caminito del Rey

```html title="u2-4.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Caminito del Rey: salida de este sábado</title>
</head>
<body>
  <h1>Caminito del Rey: salida de este sábado</h1>
  <!-- datetime en ISO con hora: la fecha la entienden las máquinas -->
  <p>Salida el <time datetime="2026-03-14T08:30">sábado 14 de marzo de 2026 a las 8:30</time> desde el parking de Ardales.</p>
  <p>La ruta tiene 7,7 km y el billete cuesta 10 €.</p>
  <figure>
    <img src="https://dummyimage.com/800x600/ccc/000.png&text=caminito.jpg" alt="Pasarela metálica anclada a la pared del desfiladero" width="800" height="533">
    <!-- figcaption contextualiza; no repite el alt -->
    <figcaption>Tramo central sobre el desfiladero de los Gaitanes, a 100 m de altura.</figcaption>
  </figure>
  <!-- cite (atributo) guarda la URL de origen; no se muestra en pantalla -->
  <blockquote cite="https://www.caminitodelrey.info/historia">
    <p>«Es la obra civil más temeraria de su tiempo».</p>
    <cite>Informe del ingeniero Eduardo Torroja, 1905</cite>
  </blockquote>
  <p>El lema de la excursión: <q>miedo arriba, no mires abajo</q>.</p>
  <p>Más información en caminitodelrey.info</p>
</body>
</html>
```

**Puntos clave:**

- ==`datetime`== con formato ISO (`2026-03-14T08:30`) hace la fecha legible para máquinas sin tocar el texto visible.
- `figcaption` **contextualiza** y `alt` **describe**: si dicen lo mismo, una de las dos sobra.
- El atributo `cite` guarda la URL para las máquinas y `<cite>` es la fuente visible dentro del bloque; `<q>` pone las comillas el navegador.

**Error frecuente:** cita entre comillas escritas a mano y sin fuente, o `figcaption` calcado del `alt`.

#### U2.5 — Maquetación semántica de un artículo científico-técnico

```html title="u2-5-solucion.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Análisis de la FP Informática</title>
</head>
<body>
  <h1>Análisis de la FP Informática</h1>
  <p>Publicado el <time datetime="2026-09-25">25 de septiembre de 2026</time>.</p>
  
  <h2>Requisitos de acceso y matriculación</h2>
  <p>El proceso consta de varias fases clave.</p>
  <ol>
    <li>Solicitar plaza en la secretaría virtual.</li>
    <li>
      Aportar documentación oficial. Dentro de esta fase, es imprescindible entregar:
      <ul>
        <li>Fotocopia del DNI</li>
        <li>Fotografía tamaño carnet</li>
        <li>Certificado de notas</li>
      </ul>
    </li>
    <li>Formalizar matrícula presencial.</li>
  </ol>
  
  <h2>El módulo de Desarrollo de Interfaces</h2>
  <p>El objetivo principal es aprender a diseñar interfaces <dfn><abbr title="Interfaz de Usuario">UI</abbr>/<abbr title="Experiencia de Usuario">UX</abbr></dfn>.</p>
  
  <h3>Evaluación y proyectos</h3>
  <blockquote cite="https://www.w3.org/Press/1997/WAI-launch.html">
    <p>Como dijo Tim Berners-Lee: <q>La Web es para todos</q>, y lo dijo en <time datetime="1997">1997</time>.</p>
    <cite>Tim Berners-Lee</cite>
  </blockquote>
  <p>Basado en ese principio, los proyectos deben ser accesibles.</p>
  
  <h3>Herramientas de línea de comandos</h3>
  <p>En clase usamos <code>git</code>. Para descargar un repositorio debes escribir <code>git clone</code> seguido de la URL. Si te equivocas, pulsa <kbd>Ctrl</kbd> + <kbd>C</kbd> para cancelar.</p>
  
  <hr>
  
  <p>El antiguo temario enseñaba <del>Flash</del>, pero ya ha sido sustituido por <ins>HTML5 y CSS</ins>.</p>
</body>
</html>
```

**Puntos clave:**

- **Semántica pura sin CSS:** El uso de etiquetas como `<time>`, `<abbr>`, `<dfn>`, `<code>`, `<kbd>`, `<del>` e `<ins>` aporta una enorme riqueza de significado procesable para lectores de pantalla e indexadores, aunque en pantalla los cambios visuales parezcan sutiles.
- **Anidamiento correcto de listas:** El `<ul>` hijo se encierra **dentro** del `<li>` de la fase 2. Es un error crítico colocar el `<ul>` entre dos etiquetas `<li>`, ya que el único hijo válido de `<ol>` o `<ul>` es un `<li>`.
- **Citas ricas:** `<blockquote>` encapsula el párrafo y su bloque contextual, mientras que `<q>` se usa para la cita directa en línea (el navegador pondrá las comillas automáticas). `<cite>` referencia de manera visible al autor.

**Error frecuente:** Asignar encabezados (como `<h4>`) simplemente para dar un tamaño visual menor, rompiendo la estructura del árbol (`h1 -> h2 -> h3`), y dejar listas desordenadas "flotando" fuera del `<li>` que las origina.

### Unidad 3 — Enlaces y recursos {: #sol-u3 }

#### U3.1 — Rutas relativas en la tienda

```html title="u3-1.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Zapatillas Run 300 · Tienda UFRO</title>
  <!-- Desde producto/ subo un nivel y bajo a css/ -->
  <link rel="stylesheet" href="../css/estilos.css">
</head>
<body>
  <header>
    <!-- Misma regla para el logotipo: subo y bajo a img/ -->
    <img src="https://dummyimage.com/200x200/ccc/000.png&text=logo.svg" alt="Logotipo de la tienda" width="120" height="40">
    <a href="../index.html">Volver a la portada</a>
  </header>
  <main>
    <h1>Zapatillas Run 300</h1>
    <!-- Hermano: misma carpeta, sin ../ -->
    <a href="mochila.html">Ver también la mochila Trail 25 L</a>
    <!-- Ruta relativa: subo hasta la raíz y bajo a documentos/ -->
    <a href="../documentos/garantia-2-anios.pdf" download>Consultar la garantía de 2 años (PDF)</a>
    <!-- Mismo destino por raíz: no depende de la carpeta de la página -->
    <a href="/documentos/garantia-2-anios.pdf">La misma garantía por raíz</a>
    <!-- Ruta relativa completa: subo, bajo a img/ y entro en producto/ -->
    <a href="../img/producto/zapatillas-1200w.jpg">Ver la foto en alta resolución</a>
  </main>
  <footer>
    <p>&copy; 2026 Tienda UFRO</p>
  </footer>
</body>
</html>
```

**Puntos clave:**

- Toda ==ruta relativa== se resuelve desde la página que enlazas: `../` sube, `carpeta/` baja, `/` arranca en la raíz.
- `mochila.html` no lleva `../` porque comparte carpeta con la ficha de producto.
- La ruta de raíz funciona desde cualquier carpeta, pero se rompe si el sitio no está desplegado en la raíz del dominio.

**Error frecuente:** contar los niveles desde el explorador o desde la raíz: desde `producto/` siempre falta un `../` antes de alcanzar `css/`, `img/` o `documentos/`.

#### U3.2 — Índice con anclas y skip link

```html title="u3-2.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Reglamento de evaluación</title>
</head>
<body>
  <!-- Primer elemento del body: el primer Tab lo alcanza antes que al menú -->
  <a class="skip-link" href="#contenido">Saltar al contenido</a>
  <header>
    <h1 id="inicio">Reglamento de evaluación</h1>
    <nav aria-label="Índice">
      <ul>
        <li><a href="#matriculacion">Matriculación</a></li>
        <li><a href="#asistencia">Asistencia</a></li>
        <li><a href="#evaluacion">Evaluación</a></li>
        <li><a href="#reconsideraciones">Reconsideraciones</a></li>
      </ul>
    </nav>
  </header>
  <!-- El destino del skip link: un id único en el documento -->
  <main id="contenido">
    <section id="matriculacion">
      <h2>Matriculación</h2>
      <p>El plazo se abre el 1 de septiembre y cierra el 15 de octubre.</p>
    </section>
    <section id="asistencia">
      <h2>Asistencia</h2>
      <p>La justificación se presenta en las 48 horas siguientes.</p>
    </section>
    <section id="evaluacion">
      <h2>Evaluación</h2>
      <p>Cada trimestre se publican las notas en el gestor académico.</p>
    </section>
    <section id="reconsideraciones">
      <h2>Reconsideraciones</h2>
      <p>Plazo de cinco días hábiles desde la publicación de la nota.</p>
    </section>
  </main>
  <footer>
    <!-- Ancla al id de la cabecera: vuelve arriba sin recargar -->
    <p><a href="#inicio">Volver al principio</a></p>
    <p>&copy; 2026 Centro</p>
  </footer>
</body>
</html>
```

**Puntos clave:**

- Cada `href="#…"` coincide con un ==`id` único== del mismo documento; si el id no existe, el enlace no salta.
- El skip link es el **primer elemento** del `<body>` y apunta al `id` del `<main>`.
- "Volver al principio" reutiliza el `id` del encabezado: misma página, cero recargas.

**Error frecuente:** dejar los `href` en `#` o dar al skip link el id de una sección en lugar del del contenido principal.

#### U3.3 — Enlaces con destinos especiales y descargas

```html title="u3-3.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Recursos para familias</title>
</head>
<body>
  <header>
    <h1>Recursos para familias</h1>
    <nav aria-label="Principal">
      <ul>
        <li><a href="#">Inicio</a></li>
        <li><a href="#">Horarios</a></li>
        <li><a href="#">Contacto</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <!-- Texto descriptivo: se entiende sin leer el párrafo -->
    <p>Consulta el <a href="horarios.pdf">horario de clases del curso 2026/2027</a>
       y el <a href="matricula.pdf">modelo de solicitud de matrícula</a>.</p>
    <!-- Externo en pestaña nueva: el texto avisa y rel protege la ventana -->
    <p><a href="https://www.juntadeandalucia.es/"
          target="_blank" rel="noopener noreferrer">Junta de Andalucía (se abre en pestaña nueva)</a></p>
    <!-- mailto abre el gestor de correo; %20 es el espacio del asunto -->
    <p>Contacta:
      <a href="mailto:secretaria@centro.es?subject=Consulta%20sobre%20matrícula">Escribe a secretaría</a> o
      <a href="tel:+34955000000">Llama al 955 000 000</a>.</p>
    <!-- download fuerza la guardada y renombra el fichero final -->
    <p><a href="calendario.pdf" download="Calendario_2026.pdf">Descargar el calendario escolar (PDF, 180 KB)</a></p>
  </main>
  <footer>
    <p>&copy; 2026 Centro</p>
  </footer>
</body>
</html>
```

**Puntos clave:**

- ==`mailto:`== y `tel:` no abren páginas: lanzan el gestor de correo y el marcador del teléfono.
- `target="_blank"` exige ==`rel="noopener noreferrer"`== para que la pestaña nueva no acceda a tu ventana con `window.opener`.
- `download` solo actúa sobre ficheros del mismo origen y el texto del enlace informa de **formato y peso**.

**Error frecuente:** textos repetidos tipo "haz clic aquí" y `target="_blank"` sin `rel`, que el validador ni siquiera denuncia.

#### U3.4 — Imágenes accesibles y marco incrustado

```html title="u3-4.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Casa del Olivar · Jaén</title>
</head>
<body>
  <main>
    <h1>Casa del Olivar · Jaén</h1>
    <!-- Decorativa: alt vacío para que el lector la salte -->
    <img src="https://dummyimage.com/800x600/ccc/000.png&text=patron.jpg" alt="" width="1200" height="60" loading="eager">
    <figure>
      <picture>
        <!-- El navegador recorre los source de arriba abajo -->
        <source srcset="img/patio.avif" type="image/avif">
        <source srcset="https://dummyimage.com/800x600/ccc/000.png&text=patio.webp" type="image/webp">
        <img src="https://dummyimage.com/800x600/ccc/000.png&text=patio-800.jpg"
             alt="Patio interior con arco de piedra y macetas de geranios"
             width="800" height="533" loading="eager">
      </picture>
      <figcaption>Patio interior de la casa.</figcaption>
    </figure>
    <figure>
      <!-- Fuera del pliegue: carga diferida -->
      <img src="https://dummyimage.com/800x600/ccc/000.png&text=habitacion-800.jpg"
           alt="Habitación doble con ventanales abiertos al valle"
           width="800" height="533" loading="lazy" decoding="async">
      <figcaption>Habitación doble con vistas al valle.</figcaption>
    </figure>
    <p>Fotos: <a href="img/habitacion-800.jpg">Ver la habitación a tamaño completo</a></p>
    <!-- title obligatorio: describe el marco para quien no lo ve -->
    <iframe
      src="https://www.openstreetmap.org/export/embed.html?bbox=-3.80,37.77,-3.78,37.79"
      title="Mapa de situación de la Casa del Olivar en el centro de Jaén"
      width="600" height="400"
      loading="lazy"
      sandbox="allow-scripts allow-same-origin">
    </iframe>
  </main>
  <footer>
    <p>&copy; 2026 Casa del Olivar</p>
  </footer>
</body>
</html>
```

**Puntos clave:**

- ==`alt=""`== solo vale para decorativas; en informativas el `alt` es una línea que aporta lo que el texto no dice.
- `width`/`height` ==reservan el espacio== y evitan el CLS; `lazy` queda para lo que está fuera del pliegue.
- El `<img>` de un `<picture>` es el respaldo obligatorio y el único con `alt`, `width` y `height`.
- El `title` del `<iframe>` es obligatorio: describe el marco y `sandbox` suma permisos de forma acumulativa.

**Error frecuente:** `alt` con texto en la imagen decorativa (ruido para el lector) o `<iframe>` sin `title`.

### Unidad 4 — Multimedia en HTML5 {: #sol-u4 }

#### U4.1 — Vídeo informativo con póster y formatos

```html title="u4-1.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Jornada de puertas abiertas</title>
</head>
<body>
  <main>
    <h1>Jornada de puertas abiertas</h1>
    <!-- controls convierte la caja en reproductor; sin src: los source mandan -->
    <video controls
           poster="https://dummyimage.com/800x600/ccc/000.png&text=jornada-portada.jpg"
           width="640" height="360"
           preload="metadata">
      <!-- El navegador prueba los type de arriba abajo -->
      <source src="video/jornada.mp4" type="video/mp4">
      <source src="video/jornada.webm" type="video/webm">
      <!-- Respaldo: solo se ve si el navegador no reconoce <video> -->
      <p>Tu navegador no reproduce vídeo HTML5.
         <a href="video/jornada.mp4">Descarga la grabación (MP4)</a>.</p>
    </video>
    <p>Grabación completa de la visita al centro.</p>
  </main>
  <footer>
    <p>&copy; 2026 Instituto Maya</p>
  </footer>
</body>
</html>
```

**Puntos clave:**

- ==`controls`== da barra, tiempo, volumen y atajos de teclado: sin él el vídeo no se puede reproducir.
- Varios `<source>` con ==`type`== de arriba abajo; `src` en el `<video>` se retira para no declarar dos veces el recurso.
- `preload="metadata"` trae duración y pistas sin bajar el fichero y `poster` pinta la portada mientras carga.

**Error frecuente:** olvidar `controls` o combinar `src` del `<video>` con `<source>`: el navegador prioriza `src` e ignora el resto de pistas.

#### U4.2 — Subtítulos con un .vtt real

```html title="u4-2.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Normas del taller de electrónica</title>
</head>
<body>
  <main>
    <h1>Normas del taller de electrónica</h1>
    <video controls poster="https://dummyimage.com/800x600/ccc/000.png&text=normas-portada.jpg" width="640" height="360" preload="metadata">
      <source src="video/normas.mp4" type="video/mp4">
      <source src="video/normas.webm" type="video/webm">
      <!-- Captions: diálogo y efectos sonoros; default la deja activa al empezar -->
      <track kind="captions" src="normas-es.vtt" srclang="es" label="Español" default>
      <!-- Subtitles: solo traduce la habla, sin efectos -->
      <track kind="subtitles" src="normas-en.vtt" srclang="en" label="English">
      <!-- Respaldo siempre después de las pistas -->
      <p>No puedes reproducir este vídeo.
         <a href="video/normas.mp4">Descárgalo (MP4)</a>.</p>
    </video>
    <p><a href="normas-es.vtt">Descargar los subtítulos en español (VTT)</a></p>
  </main>
  <footer>
    <p>&copy; 2026 Instituto Maya</p>
  </footer>
</body>
</html>
```

```text title="normas-es.vtt"
WEBVTT

1
00:00:00.000 --> 00:00:03.500
Bienvenidos al taller de electrónica.

2
00:00:03.500 --> 00:00:07.800
((pasos)) Encended las fuentes de alimentación.

3
00:00:07.800 --> 00:00:12.000
Gafas de protección obligatorias antes de soldar.

4
00:00:12.000 --> 00:00:16.400
Cada puesto debe dejar la mesa limpia al terminar.
```

```text title="normas-en.vtt"
WEBVTT

1
00:00:00.000 --> 00:00:03.500
Welcome to the electronics workshop.

2
00:00:03.500 --> 00:00:07.800
((steps)) Switch on the power supplies.
```

**Puntos clave:**

- Todo `<track>` lleva ==`srclang`== y `label`; `default` marca la pista activa al cargar la página.
- `captions` recoge diálogo y efectos `((pasos))`; `subtitles` solo traduce la habla.
- El `.vtt` es texto plano: cabecera `WEBVTT`, bloques con `HH:MM:SS.mmm --> HH:MM:SS.mmm` y su texto.

**Error frecuente:** pista sin `label`/`srclang` o `.vtt` sin la cabecera `WEBVTT`: el navegador lo rechaza en silencio y no aparece el botón de subtítulos.

#### U4.3 — Podcast con transcripción

```html title="u4-3.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Podcast: la FP en 5 minutos</title>
</head>
<body>
  <main>
    <h1>Podcast: la FP en 5 minutos</h1>
    <h2>Episodio 7: los ciclos de Artes Gráficas</h2>
    <!-- preload="none": nada se descarga hasta pulsar play -->
    <audio controls preload="none">
      <source src="audio/ep07.mp3" type="audio/mpeg">
      <source src="audio/ep07.ogg" type="audio/ogg">
      <!-- Respaldo dentro del elemento, después de las pistas -->
      <p>Tu navegador no reproduce audio.
         <a href="audio/ep07.mp3">Descarga el episodio (MP3)</a>.</p>
    </audio>
    <p><a href="audio/ep07.mp3" download="fp-5-min-ep07.mp3">Descarga directa del episodio (MP3, 9,4 MB)</a></p>
    <!-- Transcripción en la propia página: texto legible sin reproducir nada -->
    <details>
      <summary>Transcripción completa del episodio</summary>
      <p><strong>00:00</strong> — Bienvenidos a «la FP en 5 minutos».</p>
      <p><strong>01:20</strong> — Qué se estudia en Artes Gráficas y qué salidas tiene.</p>
      <p><strong>03:05</strong> — Prácticas en empresas del sector y convenios firmados.</p>
      <p><strong>04:30</strong> — Cómo matricularte y fechas del próximo plazo.</p>
    </details>
  </main>
  <footer>
    <p>&copy; 2026 Instituto Maya</p>
  </footer>
</body>
</html>
```

**Puntos clave:**

- Dos `<source>` con ==`type`== y sin `src` en `<audio>`; el texto de respaldo va **dentro**, después de las pistas.
- `preload="none"` evita bajar varios episodios de golpe; la transcripción en `<details>` es la alternativa textual equivalente.
- Marca de tiempo en cada párrafo: cumple la **WCAG 1.2.1** (alternativa para audio pregrabado); la **1.2.2** exigiría además subtítulos sincronizados si el episodio tuviera vídeo.

**Error frecuente:** publicar la transcripción como PDF adjunto en lugar de texto dentro de la propia página.

#### U4.4 — Banner automático e incrustación externa

```html title="u4-4.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Instituto Maya</title>
</head>
<body>
  <header>
    <h1>Instituto Maya</h1>
    <!-- Fórmula válida de autoplay: muted + playsinline; decorativo: sin controls -->
    <video autoplay muted loop playsinline
           src="video/banner-maya.webm"
           width="960" height="400"
           preload="none"
           aria-hidden="true"></video>
  </header>
  <main>
    <h2>Clase grabada: accesibilidad</h2>
    <!-- Incrustación externa: title obligatorio y carga diferida -->
    <iframe width="560" height="315"
            src="https://www.youtube-nocookie.com/embed/AbC123XyZ"
            title="Vídeo: clase grabada de accesibilidad web (45 minutos)"
            loading="lazy"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture; fullscreen"
            allowfullscreen>
    </iframe>
    <p>Duración: 45 minutos.</p>
    <!-- Enlace de respaldo con texto descriptivo por si el marco no carga -->
    <p><a href="https://www.youtube.com/watch?v=AbC123XyZ">Ver la clase de accesibilidad en YouTube</a></p>
  </main>
  <footer>
    <p>&copy; 2026 Instituto Maya</p>
  </footer>
</body>
</html>
```

**Puntos clave:**

- ==`autoplay`== solo se acepta con `muted` y `playsinline`; al ser decorativo va sin `controls` y con `aria-hidden="true"`.
- `preload`: `none` no baja nada, `metadata` trae duración y pistas, `auto` descarga el fichero entero → banner con `none` y ficha de un vídeo largo con `metadata`.
- El `<iframe>` externo lleva `title` obligatorio, `loading="lazy"` y pantalla completa habilitada; el enlace de respaldo sigue funcionando si el marco falla.

**Error frecuente:** `autoplay` con sonido (los navegadores lo bloquean) o `<iframe>` sin `title`, que el lector de pantalla anuncia como "marco" sin decir qué contiene.

### Unidad 5 — Tablas de datos {: #sol-u5 }

#### U5.1 — Clasificación de la liga

```html title="u5-1.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Clasificación de la liga</title>
</head>
<body>
  <main>
    <h1>Clasificación del torneo local</h1>
    <table>
      <!-- thead agrupa la fila de encabezados: scope="col" declara la dirección -->
      <thead>
        <tr>
          <th scope="col">Equipo</th>
          <th scope="col">PJ</th>
          <th scope="col">G</th>
          <th scope="col">E</th>
          <th scope="col">P</th>
          <th scope="col">Pts</th>
        </tr>
      </thead>
      <!-- tbody agrupa los datos: scope="row" vincula el th con su fila -->
      <tbody>
        <tr>
          <th scope="row">Real Betis</th>
          <td>8</td><td>6</td><td>1</td><td>1</td><td>19</td>
        </tr>
        <tr>
          <th scope="row">Sevilla FC</th>
          <td>8</td><td>5</td><td>2</td><td>1</td><td>17</td>
        </tr>
        <tr>
          <th scope="row">CD Málaga</th>
          <td>8</td><td>4</td><td>2</td><td>2</td><td>14</td>
        </tr>
      </tbody>
      <!-- tfoot se escribe al final y repite la estructura: 6 celdas como las demás -->
      <tfoot>
        <tr>
          <th scope="row">Media del grupo</th>
          <td>8</td><td>5</td><td>1,7</td><td>1,3</td><td>16,7</td>
        </tr>
      </tfoot>
    </table>
  </main>
</body>
</html>
```

**Puntos clave:**

- `thead`, `tbody` y `tfoot` dividen la tabla en cabecera, datos y ==resumen==; el `tfoot` va siempre al final.
- `scope="col"` en la fila superior y `scope="row"` en cada equipo: el lector anuncia "Real Betis, Pts, 19".
- Todas las filas suman el mismo número de celdas, contando las que cubre un `colspan` o un `rowspan`.

**Error frecuente:** encabezados escritos como `<td>` "en negrita" o un `<th>` sin `scope`, que deja los datos sin contexto.

#### U5.2 — Turnos con celdas unidas

```html title="u5-2.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Turnos de la semana</title>
</head>
<body>
  <main>
    <h1>Turnos de la semana</h1>
    <table>
      <caption>Turnos de la semana — Panadería El Trigal</caption>
      <thead>
        <tr>
          <th scope="col">Día</th>
          <th scope="col">Sección</th>
          <th scope="col">Mañana</th>
          <th scope="col">Tarde</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <!-- rowspan="2": la celda del día también cubre la fila de Venta -->
          <th scope="row" rowspan="2">Lunes</th>
          <td>Horno</td><td>Ana</td><td>Luis</td>
        </tr>
        <tr>
          <!-- OJO: NO se escribe la celda del día: ya la cubre el rowspan -->
          <td>Venta</td><td>Marta</td><td>Carlos</td>
        </tr>
        <tr>
          <th scope="row" rowspan="2">Martes</th>
          <td>Horno</td><td>Ana</td><td>Luis</td>
        </tr>
        <tr>
          <td>Venta</td><td>Marta</td><td>Carlos</td>
        </tr>
        <tr>
          <!-- colspan="4": una sola celda para las cuatro columnas -->
          <td colspan="4">Descanso compartido de 14:00 a 16:00</td>
        </tr>
      </tbody>
    </table>
  </main>
</body>
</html>
```

**Puntos clave:**

- Las celdas cubiertas por un ==`rowspan`== **se eliminan**: si las escribes, la fila se desborda y toda la tabla queda escalonada.
- Recuento fila a fila: cabecera 4, cada fila de datos 4 (3 escritas + 1 heredada) y descanso 4 con su ==`colspan`==.
- El `rowspan` se declara siempre en la **primera** fila del bloque que cubre.

**Error frecuente:** repetir el `<td>` del día en la fila de abajo y dejar la cuadrícula desplazada.

#### U5.3 — Precios con colgroup y abbr

```html title="u5-3.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Taller El Olivo — precios</title>
</head>
<body>
  <main>
    <h1>Precios con IVA</h1>
    <table>
      <caption>Taller El Olivo — precios con IVA</caption>
      <!-- colgroup: justo después del caption y antes del thead -->
      <colgroup>
        <!-- Primera columna (Producto) más ancha -->
        <col style="width: 16rem">
        <!-- span="2": la definición se aplica a Formato y Precio -->
        <col span="2">
      </colgroup>
      <thead>
        <tr>
          <th scope="col">Producto</th>
          <th scope="col">Formato</th>
          <!-- abbr: forma corta que el lector anuncia en cada celda -->
          <th scope="col" abbr="Precio (IVA)">Precio con IVA incluido</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">Aceite de oliva virgen extra</th>
          <td>Botella 1 L</td>
          <td>9,50 €</td>
        </tr>
        <tr>
          <th scope="row">Vinagre de Jerez</th>
          <td>Botella 500 ml</td>
          <td>4,25 €</td>
        </tr>
        <tr>
          <th scope="row">Sal marina en escamas</th>
          <td>Bolsa 1 kg</td>
          <td>2,10 €</td>
        </tr>
      </tbody>
    </table>
  </main>
</body>
</html>
```

**Puntos clave:**

- El ==`colgroup`== aplica estilo o ancho a la columna entera sin repetirlo celda a celda, y su sitio es entre `caption` y `thead`.
- `abbr` guarda la forma corta que el lector anuncia en cada celda; el texto visible de la cabecera no cambia.
- `<col>` es una etiqueta vacía que solo admite atributos presentacionales y su `width` es una sugerencia: el ancho fiable se fija en CSS.

**Error frecuente:** colocar el `<colgroup>` después de las filas o meter contenido dentro de `<col>`.

#### U5.4 — Calendario de exámenes accesible en móvil

```html title="u5-4.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Semana de exámenes finales</title>
  <style>
    /* Solo la tabla se desplaza; la barra aparece únicamente si desborda */
    .tabla-scroll {
      overflow-x: auto;
    }
    .tabla-scroll table {
      width: 100%;
      min-width: 44rem; /* ancho mínimo: así aparece la barra en móvil */
      border-collapse: collapse;
      font-size: 0.875rem;
    }
    .tabla-scroll th,
    .tabla-scroll td {
      border: 1px solid #ccc;
      padding: 0.4rem;
      text-align: left;
    }
  </style>
</head>
<body>
  <main>
    <h1>Semana de exámenes finales</h1>
    <!-- tabindex: la zona de scroll es enfocable con el teclado.
         role + aria-labelledby: región con el nombre del caption (WCAG 2.1.1) -->
    <figure class="tabla-scroll" tabindex="0" role="region" aria-labelledby="cap-examenes">
      <table>
        <!-- el id del caption es el destino del aria-labelledby -->
        <caption id="cap-examenes">Semana de exámenes finales — 1.º DAW A</caption>
        <thead>
          <tr>
            <th scope="col">Módulo</th>
            <th scope="col">Lun 15</th>
            <th scope="col">Mar 16</th>
            <th scope="col">Mié 17</th>
            <th scope="col">Jue 18</th>
            <th scope="col">Vie 19</th>
          </tr>
        </thead>
        <tbody>
          <tr><th scope="row">Lenguajes de marcas</th><td>09:00</td><td></td><td></td><td></td><td></td></tr>
          <tr><th scope="row">Bases de datos</th><td></td><td>11:30</td><td></td><td></td><td></td></tr>
          <tr><th scope="row">Desarrollo web en cliente</th><td></td><td></td><td>09:00</td><td></td><td></td></tr>
          <tr><th scope="row">Sistemas de gestión empresarial</th><td></td><td></td><td></td><td>12:00</td><td></td></tr>
          <tr><th scope="row">Entornos de desarrollo</th><td></td><td></td><td></td><td></td><td>10:00</td></tr>
        </tbody>
        <!-- tfoot el último: caption → thead → tbody → tfoot -->
        <tfoot>
          <tr>
            <th scope="row">Total de exámenes</th>
            <td colspan="5">5 pruebas, una por módulo</td>
          </tr>
        </tfoot>
      </table>
    </figure>
  </main>
</body>
</html>
```

**Puntos clave:**

- ==`tabindex="0"`== convierte la zona de scroll en un destino de teclado y `role="region"` + `aria-labelledby` le dan el nombre del `caption`.
- `overflow-x: auto` muestra la barra solo si la tabla desborda; `min-width` garantiza que aparezca en pantallas estrechas.
- El `tfoot` se escribe al final, después del `tbody`.

**Error frecuente:** contenedor de scroll sin `tabindex="0"` (inalcanzable con teclado) o `overflow: hidden`, que oculta datos sin posibilidad de recuperarlos.

### Unidad 6 — Formularios HTML5 {: #sol-u6 }

#### U6.1 — Alta en el boletín

```html title="u6-1.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Boletín del centro</title>
</head>
<body>
  <main>
    <h1>Boletín informativo</h1>
    <!-- POST: el alta escribe en el servidor -->
    <form action="/boletin" method="post">
      <p>
        <!-- label visible siempre: el placeholder solo acompaña como pista -->
        <label for="email">Correo electrónico</label>
        <input type="email" id="email" name="email" required
               autocomplete="email" placeholder="nombre@ejemplo.com">
      </p>
      <p>
        <!-- required en la casilla: sin marcarla no se envía -->
        <input type="checkbox" id="politica" name="politica" value="si" required>
        <label for="politica">He leído y acepto la política de privacidad</label>
      </p>
      <button type="submit">Suscribirme</button>
    </form>
  </main>
</body>
</html>
```

**Puntos clave:**

- `type="email"` + ==`required`== validan sin JavaScript: el navegador bloquea el envío con el campo vacío o sin `@`.
- `autocomplete="email"` declara el propósito del campo (==WCAG 1.3.5==) y `name` es la clave con la que llega el dato al servidor.

**Error frecuente:** usar el `placeholder` como etiqueta: desaparece al escribir y el lector de pantalla no tiene nombre que anunciar.

#### U6.2 — Formulario de contacto

```html title="u6-2.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contacto — IES Maya</title>
</head>
<body>
  <main>
    <h1>Formulario de contacto</h1>
    <!-- POST: el envío crea un registro y el motivo puede ser largo;
         con GET los valores acabarían en la URL, el historial y los logs -->
    <form action="/contacto" method="post">
      <p>
        <label for="nombre">Nombre y apellidos</label>
        <!-- id enlaza el label; name es la clave de envío -->
        <input type="text" id="nombre" name="nombre" autocomplete="name" required>
      </p>
      <p>
        <label for="correo">Correo electrónico</label>
        <input type="email" id="correo" name="correo" autocomplete="email" required>
      </p>
      <p>
        <label for="motivo">Motivo de la consulta</label>
        <input type="text" id="motivo" name="motivo" required>
      </p>
      <!-- sin type, este botón equivaldría a submit -->
      <button type="submit">Enviar consulta</button>
    </form>
  </main>
</body>
</html>
```

**Puntos clave:**

- Sin ==`name`== no hay envío: el `id` solo enlaza el `<label>`, la clave con la que viaja el dato es otra.
- `POST` manda los campos en el cuerpo de la petición: no quedan en la ==URL==, en el historial ni en los registros del servidor.

**Error frecuente:** `<button>` sin `type` (equivale a `submit`) y etiquetas envueltas sin `for`/`id`, que no se pueden marcar con un clic.

#### U6.3 — Encuesta con grupos de opciones

```html title="u6-3.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Encuesta de satisfacción</title>
</head>
<body>
  <main>
    <h1>Encuesta de final de curso</h1>
    <form action="/encuesta" method="post">
      <!-- fieldset + legend: nombre accesible del grupo -->
      <fieldset>
        <legend>Turno preferido</legend>
        <!-- mismo name en los radios: solo uno puede marcarse -->
        <input type="radio" id="manana" name="turno" value="manana" required>
        <label for="manana">Mañana</label>
        <input type="radio" id="tarde" name="turno" value="tarde">
        <label for="tarde">Tarde</label>
      </fieldset>
      <fieldset>
        <legend>Qué te ha parecido</legend>
        <!-- casillas independientes: cada una con su name -->
        <input type="checkbox" id="contenido" name="contenido" value="si">
        <label for="contenido">El contenido</label>
        <input type="checkbox" id="practicas" name="practicas" value="si">
        <label for="practicas">Las prácticas</label>
      </fieldset>
      <p>
        <label for="ciclo">Ciclo formativo</label>
        <select id="ciclo" name="ciclo" required>
          <!-- opción vacía: sin elegir, required bloquea el envío -->
          <option value="" disabled selected>Elige una opción</option>
          <optgroup label="Grado medio">
            <option value="smr">Sistemas microinformáticos y redes</option>
          </optgroup>
          <optgroup label="Grado superior">
            <option value="dam">Desarrollo de aplicaciones multiplataforma</option>
            <option value="daw">Desarrollo de aplicaciones web</option>
          </optgroup>
        </select>
      </p>
      <button type="submit">Enviar encuesta</button>
    </form>
  </main>
</body>
</html>
```

**Puntos clave:**

- ==`fieldset`== + `legend` dan el nombre del grupo: el lector anuncia "Turno preferido, Mañana, 1 de 2" en vez de "Mañana, 1 de 2" a secas.
- Los radios comparten `name` (uno solo) y las casillas no; el ==`optgroup`== agrupa las `option` con un subtítulo.

**Error frecuente:** título de grupo en un `<p>`, invisible para el lector, y un `<select required>` sin opción vacía que indique "Elige una opción".

#### U6.4 — Reserva de sala: rangos, botones y estados

```html title="u6-4.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Reserva de sala</title>
</head>
<body>
  <main>
    <h1>Reserva de la sala de informática</h1>
    <!-- Validación nativa activa: añadir novalidate apagaría los globos
         y obligaría a validar cada campo con JavaScript -->
    <form action="/reserva" method="post">
      <p>
        <label for="plazas">Plazas</label>
        <!-- min/max/step delimitan el intervalo; title explica el límite -->
        <input type="number" id="plazas" name="plazas"
               min="1" max="30" step="1" required
               title="Introduce un número de plazas entre 1 y 30">
      </p>
      <p>
        <label for="observaciones">Observaciones</label>
        <!-- maxlength corta la escritura en 200 caracteres -->
        <textarea id="observaciones" name="observaciones" rows="3" maxlength="200"
                  required placeholder="Necesito adaptación de horario..."></textarea>
      </p>
      <p>
        <label for="curso">Grupo</label>
        <!-- readonly: visible, tabulable y SÍ se envía -->
        <input type="text" id="curso" name="curso" value="1.º DAW A" readonly>
      </p>
      <p>
        <label for="codigo">Código de reserva</label>
        <!-- disabled: gris, sin foco y NO se envía -->
        <input type="text" id="codigo" name="codigo" value="RES-2026-014" disabled>
      </p>
      <p id="resumen" hidden></p>
      <!-- type="button" no envía; sin type equivaldría a submit -->
      <button type="button">Ver resumen</button>
      <button type="submit">Reservar</button>
    </form>
  </main>
  <script>
    // El botón de tipo "button" solo dispara JavaScript: nada se envía
    document.querySelector('button[type="button"]').addEventListener('click', () => {
      const plazas = document.getElementById('plazas').value || '0';
      const resumen = document.getElementById('resumen');
      resumen.textContent = 'Resumen: ' + plazas + ' plazas en 1.º DAW A.';
      resumen.hidden = false;
    });
  </script>
</body>
</html>
```

**Puntos clave:**

- ==`readonly`== se envía y sigue tabulándose; ==`disabled`== no viaja en la petición, como si el campo no existiera.
- Un `<button>` sin `type` equivale a `submit`: la acción propia necesita `type="button"`.
- `min`/`max`/`step` y `maxlength` validan sin JavaScript y el `title` describe el límite cuando el valor no encaja.

**Error frecuente:** poner `disabled` donde debe ir `readonly` y perder el dato en el servidor.

### Unidad 7 — Estructura semántica y ARIA {: #sol-u7 }

#### U7.1 — Encabezados sin saltos

```html title="u7-1.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fotografía Digital para Principiantes</title>
</head>
<body>
  <h1>Fotografía Digital para Principiantes</h1>
  <!-- Unidades al mismo nivel: el salto h1 → h4 desaparece -->
  <h2>La cámara</h2>
  <p>Conoce los mandos antes de disparar.</p>
  <h2>El objetivo</h2>
  <p>La distancia focal cambia la perspectiva.</p>
  <h2>Composición</h2>
  <p>La regla de los tercios ordena el encuadre.</p>
  <!-- h3: subtema dependiente de "Composición" -->
  <h3>La luz</h3>
  <!-- Segundo h1 convertido en h2: un solo h1 por página -->
  <h2>Focos y diafragma</h2>
  <p>Medir la luz es el primer hábito del fotógrafo.</p>
</body>
</html>
```

**Puntos clave:**

- Un solo ==`h1`== y niveles encadenados (`h1` → `h2` → `h3`) sin saltos: el índice del lector de pantalla vuelve a funcionar.
- El nivel lo decide la ==jerarquía==, no el tamaño: la diferencia visual entre `h2` y `h3` la pone CSS.

**Error frecuente:** elegir el encabezado por el tamaño que "queda mejor" (`h4` porque es más pequeño) y mantener dos `h1`.

#### U7.2 — Mapa de landmarks de una revista

```html title="u7-2.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Revista Alameda</title>
</head>
<body>
  <!-- header hijo directo de body => landmark banner -->
  <header>
    <h1>Revista Alameda</h1>
    <!-- nav => navigation; aria-label nombra el menú -->
    <nav aria-label="Secciones">
      <a href="index.html">Portada</a> <a href="cultura.html">Cultura</a> <a href="ciencia.html">Ciencia</a>
    </nav>
  </header>
  <!-- main => landmark main; uno solo por página -->
  <main>
    <!-- article: noticia que se entiende por sí sola -->
    <article>
      <header>
        <h2>El río que volvió a correr</h2>
        <p>La restauración de la ribera ha recuperado su cauce.</p>
      </header>
      <!-- section: bloque temático con encabezado propio -->
      <section>
        <h3>Las cifras</h3>
        <p>Se han plantado 4.000 árboles nativos.</p>
      </section>
    </article>
    <!-- aside => complementary -->
    <aside>
      <h2>También te puede interesar</h2>
      <ul><li><a href="agenda.html">Agenda del fin de semana</a></li><li><a href="letras.html">Letras de la semana</a></li></ul>
    </aside>
  </main>
  <!-- footer hijo directo de body => landmark contentinfo -->
  <footer><p>&copy; 2026 Revista Alameda</p></footer>
</body>
</html>
```

**Puntos clave:**

- El ==landmark== lo definen el elemento y su posición: `banner`/`contentinfo` solo si `header`/`footer` son hijos directos de `<body>`.
- `article` es contenido independiente, `section` exige tema con ==encabezado propio== y `aside` complementa al `main`.

**Error frecuente:** meter un segundo `<main>` para la barra lateral o dejar el `<aside>` sin encabezado.

#### U7.3 — Menú con estado y nombres accesibles

```html title="u7-3.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Novedades - Biblioteca Municipal</title>
</head>
<body>
  <header>
    <h1>Biblioteca Municipal</h1>
    <!-- aria-label: nombre accesible donde no hay título visible -->
    <nav aria-label="Principal">
      <ul>
        <li><a href="index.html">Inicio</a></li>
        <!-- aria-current="page": "estás aquí" para el lector de pantalla -->
        <li><a href="novedades.html" aria-current="page">Novedades</a></li>
        <li><a href="catalogo.html">Catálogo</a></li>
      </ul>
    </nav>
    <!-- Imagen decorativa (alt=""): el nombre del botón lo pone aria-label -->
    <button type="button" aria-label="Buscar en el catálogo">
      <img src="https://dummyimage.com/800x600/ccc/000.png&text=lupa.svg" alt="">
    </button>
  </header>
  <main>
    <h2>Novedades de septiembre</h2>
    <!-- ★ es decorativa y ya está junto al texto: no debe anunciarse -->
    <p><span aria-hidden="true">★</span> Novedad: "El nombre del viento", de Patrick Rothfuss.</p>
    <p>Reserva en el mostrador o desde tu cuenta.</p>
  </main>
</body>
</html>
```

**Puntos clave:**

- `aria-current` describe ==estado==, no estilo: el resaltado visual del enlace activo lo pone CSS.
- `aria-label` solo donde no hay texto visible (botón icono, nombre del landmark); el texto visible manda y no se duplica.

**Error frecuente:** `aria-label` redundante con el texto visible del enlace (doble anuncio) u `aria-hidden` puesto en un control enfocable.

#### U7.4 — Del div al botón nativo

```html title="u7-4.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Campaña de solidaridad</title>
</head>
<body>
  <header>
    <h1>Campaña de solidaridad</h1>
    <!-- Sin role="navigation": <nav> ya es el landmark navigation -->
    <nav>
      <a href="index.html">Inicio</a>
      <!-- Sin aria-label: el texto visible "Ayuda" ya es el nombre accesible -->
      <a href="ayuda.html">Ayuda</a>
    </nav>
  </header>
  <main>
    <h2>Firma la petición</h2>
    <!-- Nativo: teclado, foco y nombre accesible sin tabindex ni JS extra -->
    <button type="button" class="primario" onclick="this.textContent = 'Petición firmada'">Firmar ahora</button>
    <p><button type="button">Ver bases</button></p>
  </main>
</body>
</html>
```

**Puntos clave:**

- El ==botón nativo== trae gratis teclado (`Enter`/`Espacio`), foco, nombre accesible y estado `disabled`; el `div role="button"` exige reimplementarlo todo.
- Solo se añade ARIA cuando el HTML no llega: `role="navigation"` sobre `<nav>` o `aria-label` con el mismo texto visible son ==redundancias== que empeoran el anuncio.

**Error frecuente:** "arreglar" el `div` añadiendo más `tabindex` y JavaScript en vez de cambiar la etiqueta por `<button>`.

### Unidad 8 - APIs y funcionalidades nativas {: #sol-u8 }

#### U8.1 — Datos en el marcado con data-*

```html title="u8-1.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>data-* y dataset</title>
</head>
<body>
  <!-- Los datos viajan en el propio marcado, sin clases ni atributos a medida -->
  <article class="ficha" data-estado="borrador" data-id="42" data-id-unidad="7">
    <h2>Apuntes de Lenguajes de Marcas</h2>
    <p id="estado">Estado actual: —</p>
    <button type="button" class="publicar">Publicar</button>
  </article>
  <p id="salida"></p>

  <script>
    const ficha = document.querySelector('.ficha');
    const salida = document.getElementById('salida');
    const estado = document.getElementById('estado');

    // Lectura: data-estado → dataset.estado (siempre STRING)
    salida.textContent = `Estado: ${ficha.dataset.estado} · id: ${ficha.dataset.id}`;

    // data-id-unidad → dataset.idUnidad: pasa a camelCase
    // typeof imprime "string": para calcular, convierte con Number(...)
    console.log(ficha.dataset.idUnidad, typeof ficha.dataset.id, Number(ficha.dataset.id));

    // Escritura: dataset.estado = 'x' escribe data-estado="x" en el HTML
    ficha.querySelector('.publicar').addEventListener('click', () => {
      ficha.dataset.estado = 'publicado';
      estado.textContent = `Estado actual: ${ficha.dataset.estado}`;
    });
  </script>
</body>
</html>
```

**Puntos clave:**

- `data-id-unidad` se lee como `dataset.idUnidad`: los guiones pasan a ==camelCase== y el valor siempre es texto.
- Escribir sobre `dataset` actualiza el atributo HTML al momento; el mismo elemento es fuente de datos y receptor de cambios.

**Error frecuente:** comparar `ficha.dataset.id === 42` (nunca coincide: es `"42"`) u olvidar convertirlo con `Number(...)`.

#### U8.2 — Contador de visitas con localStorage

```html title="u8-2.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tienda de barrio</title>
</head>
<body>
  <h1>Tienda de barrio</h1>
  <p>Has visitado esta página <strong id="contador">0</strong> veces.</p>
  <p id="ultima">Sin datos todavía.</p>
  <button type="button" id="reiniciar">Reiniciar contador</button>

  <script>
    const CLAVE = 'visitas-tienda';
    const contador = document.getElementById('contador');
    const infoUltima = document.getElementById('ultima');

    // Lectura defensiva: clave vacía o JSON corrupto → valor inicial (primer uso)
    let datos = { visitas: 0, ultima: null };
    try {
      const guardado = JSON.parse(localStorage.getItem(CLAVE));
      if (guardado) datos = guardado;
    } catch {
      console.warn('No había JSON válido en la clave "' + CLAVE + '": empezamos de cero');
    }

    datos.visitas += 1;
    datos.ultima = new Date().toLocaleString('es-ES');

    // Escritura: SIEMPRE JSON.stringify (si no, "[object Object]")
    try {
      localStorage.setItem(CLAVE, JSON.stringify(datos));
    } catch (e) {
      // Cuota superada: la app sigue funcionando, solo no persiste
      console.warn('No se pudo guardar:', e.name);
    }

    contador.textContent = datos.visitas;
    if (datos.ultima) infoUltima.textContent = `Última visita: ${datos.ultima}`;

    // Variante con sessionStorage: mismo código, pero se borra al cerrar la pestaña
    document.getElementById('reiniciar').addEventListener('click', () => {
      localStorage.removeItem(CLAVE);   // una clave concreta, sin clear() general
      contador.textContent = '0';
      infoUltima.textContent = 'Sin datos todavía.';
    });
  </script>
</body>
</html>
```

**Puntos clave:**

- Escritura con ==`JSON.stringify`== y lectura con `JSON.parse` dentro de `try/catch`, contemplando el primer uso con la clave vacía.
- `localStorage` no caduca y no viaja al servidor; `sessionStorage` (la variante) se borra al cerrar la pestaña.

**Error frecuente:** `localStorage.setItem(CLAVE, datos)` escribe `[object Object]` y al recargar `JSON.parse` revienta.

#### U8.3 — Validación programática con Constraint Validation API

```html title="u8-3.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Inscripción - Curso de HTML5</title>
</head>
<body>
  <h1>Inscripción al curso</h1>
  <!-- novalidate: yo controlo los mensajes; checkValidity() sigue funcionando -->
  <form id="inscripcion" novalidate>
    <p><label for="nif">NIF</label>
       <input id="nif" name="nif" pattern="[0-9]{8}[A-Za-z]" placeholder="12345678Z"></p>
    <p><label for="email">Correo electrónico</label>
       <input id="email" name="email" type="email" required></p>
    <button type="submit">Comprobar</button>
    <p id="error" role="alert"></p>
  </form>

  <script>
    const form = document.getElementById('inscripcion');
    const nif = document.getElementById('nif');
    const email = document.getElementById('email');
    const error = document.getElementById('error');

    // Mensaje propio mientras se escribe
    nif.addEventListener('input', () => {
      if (nif.value && nif.validity.patternMismatch) {
        nif.setCustomValidity('Debe tener 8 dígitos seguidos de una letra');
      } else {
        nif.setCustomValidity('');   // cadena vacía = sin error propio
      }
    });

    form.addEventListener('submit', (e) => {
      e.preventDefault();   // el formulario no se envía al servidor

      if (form.checkValidity()) {          // true/false de todo el formulario
        error.textContent = '¡Inscripción correcta!';
        return;
      }
      // Cada campo falla por su motivo: validity te dice cuál
      if (nif.validity.valueMissing) {
        error.textContent = 'El NIF es obligatorio';
      } else if (nif.validity.patternMismatch) {
        error.textContent = nif.validationMessage;
      } else if (email.validity.typeMismatch) {
        error.textContent = 'El correo no tiene un formato válido';
      } else if (email.validity.valueMissing) {
        error.textContent = 'El correo es obligatorio';
      } else {
        error.textContent = 'Revisa los campos marcados';
      }
    });
  </script>
</body>
</html>
```

**Puntos clave:**

- `checkValidity()` da el sí/no y `validity.valueMissing` / `patternMismatch` / `typeMismatch` el ==motivo== exacto de cada fallo.
- `setCustomValidity('')` borra el error propio: sin esa cadena vacía, el campo se queda inválido aunque el usuario lo corrija.

**Error frecuente:** olvidar resetear `setCustomValidity('')` y creer que `novalidate` desactiva la validación (solo suspende los mensajes automáticos del envío).

#### U8.4 — Entrega con arrastre y geolocalización

```html title="u8-4.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Entrega de trabajos</title>
</head>
<body>
  <h1>Entrega de trabajos</h1>
  <h2>Pendientes</h2>
  <ul id="pendientes">
    <li draggable="true" data-tarea="t1">Práctica 1: tabla <button type="button" class="entregar">Entregar</button></li>
    <li draggable="true" data-tarea="t2">Práctica 2: formulario <button type="button" class="entregar">Entregar</button></li>
  </ul>
  <h2>Bandeja de entrega</h2>
  <div id="bandeja"><span class="vacio">Arrastra aquí tu entrega</span></div>
  <!-- Región viva: anuncia la entrega sin robar el foco -->
  <p id="aviso" role="status"></p>
  <button type="button" id="ubicacion">Estoy en el centro</button>
  <p id="coords"></p>

  <script>
    const bandeja = document.getElementById('bandeja');
    const aviso = document.getElementById('aviso');
    let origen = null;

    // Acción compartida: mover la tarea a la bandeja (la usa ratón y teclado)
    const entregar = (li) => {
      const vacio = bandeja.querySelector('.vacio');
      if (vacio) vacio.remove();
      bandeja.append(li);
      aviso.textContent = `Entregada la tarea ${li.dataset.tarea}.`;
    };

    document.querySelectorAll('#pendientes li').forEach((li) => {
      // dragstart: aquí solo se ESCRIBE en dataTransfer
      li.addEventListener('dragstart', (e) => {
        origen = li;
        e.dataTransfer.setData('text/plain', li.dataset.tarea);
        e.dataTransfer.effectAllowed = 'move';
      });

      // Alternativa accesible: mismo resultado sin arrastrar
      li.querySelector('.entregar').addEventListener('click', () => entregar(li));
    });

    // dragover: SIN preventDefault() el navegador cree que sueltas en otra
    // aplicación y drop NUNCA se dispara
    bandeja.addEventListener('dragover', (e) => e.preventDefault());

    // drop: se lee lo que se escribió en dragstart y se mueve el elemento
    bandeja.addEventListener('drop', (e) => {
      e.preventDefault();
      const tarea = e.dataTransfer.getData('text/plain');
      if (origen) {
        entregar(origen);
        origen = null;
      } else {
        aviso.textContent = `Soltado: ${tarea}`;
      }
    });

    // Geolocalización: primero se comprueba el soporte
    document.getElementById('ubicacion').addEventListener('click', () => {
      if (!navigator.geolocation) {
        aviso.textContent = 'Tu navegador no soporta geolocalización.';
        return;
      }
      navigator.geolocation.getCurrentPosition(
        (pos) => {
          const { latitude, longitude, accuracy } = pos.coords;
          document.getElementById('coords').textContent =
            `${latitude.toFixed(5)}, ${longitude.toFixed(5)} (±${Math.round(accuracy)} m)`;
        },
        (err) => {
          // err.code: 1 permiso denegado · 2 posición no disponible · 3 timeout
          const mensajes = {
            1: 'Has denegado el permiso de ubicación.',
            2: 'La posición no está disponible.',
            3: 'Se ha agotado el tiempo de espera.'
          };
          aviso.textContent = `Error ${err.code}: ${mensajes[err.code]}`;
        },
        { enableHighAccuracy: true, timeout: 8000, maximumAge: 60000 }
      );
    });
  </script>
</body>
</html>
```

**Puntos clave:**

- `dragstart` escribe en `dataTransfer`, ==`dragover`== con `preventDefault()` es lo que permite que `drop` se dispare y `drop` lee con `getData()`.
- El botón "Entregar" reutiliza la misma función `entregar()`: el arrastre nativo no funciona con teclado ni con dedo.

**Error frecuente:** olvidar `e.preventDefault()` en `dragover` (el `drop` no llega nunca) o probar la geolocalización en `http://`, donde la API no se activa.
