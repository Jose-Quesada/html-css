---
icon: lucide/check-square
title: "HTML 12 - Soluciones de Prácticas"
description: "Soluciones completas a las prácticas globales de HTML5."
modulo: "LMH (0373) / DIW (0615) / DI (0488)"
unidad: 12
fecha: "2026-10-07"
---

# HTML 12 — Soluciones a Prácticas Globales

En este documento encontrarás el código resuelto para las prácticas globales planteadas en la unidad 11, junto con explicaciones sobre las decisiones de maquetación semántica.

## Solución: Práctica Global 1 (Blog Técnico)

A continuación tienes el código HTML5 que resuelve la práctica, garantizando 0 errores en la validación de la W3C y aplicando la semántica correcta para lectores de pantalla y motores de búsqueda.

```html title="articulo-solucion.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Introducción a la Arquitectura Limpia en Aplicaciones Multiplataforma</title>
  
  <!-- Resource Hints -->
  <link rel="preload" href="/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
  
  <!-- Sindicación RSS -->
  <link rel="alternate" type="application/rss+xml" title="Feed RSS del Blog" href="/blog/feed.xml">
  
  <!-- Open Graph -->
  <meta property="og:title" content="Introducción a la Arquitectura Limpia en Aplicaciones Multiplataforma">
  <meta property="og:type" content="article">
  <meta property="og:image" content="https://tudominio.es/img/portada-arquitectura.jpg">
  
  <!-- JSON-LD Schema.org -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "Introducción a la Arquitectura Limpia en Aplicaciones Multiplataforma",
    "author": {
      "@type": "Person",
      "name": "María López"
    }
  }
  </script>
</head>
<body>

  <h1>Introducción a la Arquitectura Limpia en Aplicaciones Multiplataforma</h1>
  <p>Publicado el <time datetime="2026-10-15">15 de octubre de 2026</time>.</p>

  <h2>¿Qué es la Arquitectura Limpia?</h2>
  <p>El concepto central es separar el código por responsabilidades. Cuando diseñamos una <dfn><abbr title="Interfaz de Programación de Aplicaciones">API</abbr></dfn>, su lógica debe ser independiente de la <dfn><abbr title="Interfaz de Usuario">UI</abbr></dfn>. Esto evita que un cambio en la base de datos rompa el aspecto visual.</p>

  <h3>Principios Fundamentales</h3>
  <blockquote cite="https://blog.cleancoder.com/">
    <p>Como dijo Robert C. Martin en su libro "Clean Architecture": <q>La arquitectura es sobre la intención, no sobre el framework.</q></p>
    <cite>Robert C. Martin</cite>
  </blockquote>
  <p>Siguiendo esta idea, nuestro código debe gritar su propósito.</p>

  <h2>Guía de Configuración Inicial</h2>
  <p>Para empezar tu primer proyecto, sigue estos pasos:</p>
  <ol>
    <li>Instala el entorno. Asegúrate de tener instalado el CLI de tu lenguaje.</li>
    <li>Clona el repositorio base. Ejecuta en tu terminal el comando: <code>git clone url-del-repo</code>. Si el sistema se bloquea, pulsa <kbd>Ctrl</kbd> + <kbd>C</kbd> para cancelar.</li>
    <li>
      Instala las dependencias. Esto descargará e instalará paquetes fundamentales como:
      <ul>
        <li>Motor de base de datos</li>
        <li>Librería de testing</li>
        <li>Linter de código</li>
      </ul>
    </li>
    <li>Ejecuta el servidor.</li>
  </ol>

  <h2>Cambios de versión</h2>
  <p>El año pasado usábamos el archivo <code>config.xml</code> para esto, pero ahora ha sido <del>deprecado</del> y lo hemos sustituido por <ins><code>settings.json</code></ins>. Fíjate en que si intentas escribir la etiqueta <code>&lt;config&gt;</code>, el compilador te lanzará un error.</p>

  <hr>

  <address>
    <strong>Autora:</strong> María López, Ingeniera de Software.<br>
    Email: <a href="mailto:maria@iesf3.es">maria@iesf3.es</a><br>
    Edificio Tecnológico, Aula 12.
  </address>

</body>
</html>
```

### Explicación de la Solución

1. **Cabecera Avanzada:** Se incluyen `<link rel="preload">`, `<meta property="og:...">` y un bloque `<script type="application/ld+json">` garantizando que el documento esté optimizado tanto para carga web como para indexadores sociales y de búsqueda. Ninguna etiqueta vacía usa la barra final `/`.
2. **Jerarquía (H1, H2, H3):** Sólo hay un `<h1>`. La sección "¿Qué es la Arquitectura Limpia?" es un `<h2>`, y su dependencia lógica "Principios Fundamentales" baja un peldaño hasta `<h3>`. Luego se vuelve a subir a `<h2>` para el tutorial.
3. **Acoplamiento de Listas:** El elemento `<ol>` contiene 4 etiquetas `<li>`. Dentro del tercer `<li>`, justo después del texto introductorio, se abre y cierra el `<ul>`. Esto garantiza que la semántica estructural no se rompa al crear sub-niveles.
4. **Semántica de Código:** Las palabras clave técnicas (archivos o comandos de consola) están envueltas en `<code>`. Los botones físicos del teclado usan `<kbd>`. Las etiquetas de ejemplo (`&lt;config&gt;`) usan las entidades HTML correctas para evitar que el navegador crea que son etiquetas reales.
5. **Citas Rigurosas:** El bloque completo de Robert C. Martin está dentro de un `<blockquote>`. En su interior, un párrafo contiene la frase donde la mención exacta está rodeada de `<q>` (que añadirá las comillas visualmente). Se cierra atribuyendo el autor con `<cite>`.

## Solución: Práctica Global 2 (Portafolio Profesional Multimedia)

El siguiente código muestra cómo integrar enlaces de acción, atributos de seguridad en recursos externos, imágenes responsivas por resolución y un iframe accesible, manteniendo el núcleo semántico perfecto.

```html title="sobre-mi-solucion.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Portfolio de [Tu Nombre] - Desarrollador Web</title>
  <meta name="description" content="Portfolio profesional especializado en accesibilidad y desarrollo web.">
</head>
<body>

  <nav aria-label="Menú rápido">
    <ul>
      <li><a href="#experiencia">Ir a Experiencia</a></li>
      <li><a href="#contacto">Ir a Contacto</a></li>
    </ul>
  </nav>

  <h1>Portfolio de [Tu Nombre]</h1>
  <p>Desarrollador web especializado en accesibilidad.</p>

  <h2 id="experiencia">Experiencia</h2>
  <p>He trabajado creando interfaces de usuario (<abbr title="Interfaz de Usuario">UI</abbr>) desde el año <time datetime="2024">2024</time>.</p>
  
  <blockquote cite="https://www.w3.org/">
    <p>Mi lema de trabajo lo saqué del <abbr title="World Wide Web Consortium">W3C</abbr>: <q>El poder de la Web está en su universalidad</q>.</p>
  </blockquote>

  <figure>
    <img src="https://dummyimage.com/800x600/ccc/000.png&text=proyecto.jpg" 
         srcset="https://dummyimage.com/800x600/ccc/000.png&text=proyecto-movil.jpg 400w, https://dummyimage.com/800x600/ccc/000.png&text=proyecto.jpg 800w" 
         sizes="(max-width: 600px) 400px, 800px" 
         alt="Dos monitores mostrando código de programación y un editor de texto" 
         width="800" height="450" 
         loading="lazy">
    <figcaption>Mi entorno de desarrollo</figcaption>
  </figure>

  <h2 id="contacto">Contacto</h2>
  <ul>
    <li>Puedes ver mi código fuente en mi perfil de <a href="https://github.com/" target="_blank" rel="noopener">GitHub</a>.</li>
    <li>Escríbeme a: <a href="mailto:correo@ejemplo.com">correo@ejemplo.com</a>.</li>
  </ul>

  <p>Trabajo desde la zona tecnológica de Málaga.</p>
  
  <iframe 
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3198.058348616147!2d-4.4214!3d36.7213!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd72f7c000000001%3A0x1c00000000000000!2sM%C3%A1laga!5e0!3m2!1ses!2ses!4v1700000000000!5m2!1ses!2ses" 
    width="600" 
    height="450" 
    style="border:0;" 
    allowfullscreen="" 
    loading="lazy" 
    referrerpolicy="no-referrer-when-downgrade"
    title="Mapa de la zona tecnológica de Málaga">
  </iframe>

</body>
</html>
```

### Explicación de la Solución

1. **Enlaces e Identificadores (Anclas):** Los enlaces del `<nav>` (`href="#experiencia"`) coinciden de forma exacta con el atributo `id` de las etiquetas `<h2>`. Esto permite el salto interno sin recargar la página.
2. **Seguridad en enlaces externos:** Al enlazar a GitHub usando `target="_blank"` para abrir una nueva pestaña, es absolutamente obligatorio acompañarlo de `rel="noopener"` para evitar vulnerabilidades de seguridad (*tabnabbing*).
3. **Enlaces de Acción:** Se usa el protocolo `mailto:` en el atributo `href` para abrir el gestor de correo predeterminado del usuario.
4. **Imagen Responsiva (`srcset` y `sizes`):** 
    - `srcset` informa al navegador de las imágenes disponibles y sus anchos reales (`400w` y `800w`).
    - `sizes` le dice al navegador qué espacio ocupará la imagen en pantalla. Con esta información, el navegador decide inteligentemente cuál descargar para ahorrar ancho de banda. 
    - Los atributos `width` y `height` previenen el *Layout Shift* (salto de la página) al reservar el espacio, y `loading="lazy"` retrasa su descarga hasta que el usuario hace scroll hacia ella.
5. **Iframes Accesibles:** Al integrar el mapa se ha añadido el atributo `title`, que es vital para que un lector de pantalla pueda anunciar qué contiene la ventana flotante sin tener que entrar en ella a ciegas. También se marca con `loading="lazy"` por cuestiones de rendimiento.

## Solución: Práctica Global 3 (Plataforma de Videoeducación)

Esta solución muestra cómo orquestar múltiples etiquetas multimedia para construir un entorno de aprendizaje inclusivo.

```html title="leccion-solucion.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lección 4: Introducción a la Lógica de Programación</title>
  <meta name="description" content="Aprende los fundamentos de los algoritmos y bucles en esta lección interactiva.">
</head>
<body>

  <header>
    <nav aria-label="Navegación del curso">
      <a href="/cursos">Volver a cursos</a>
    </nav>
  </header>

  <main>
    <h1>Lección 4: Introducción a la Lógica de Programación</h1>

    <section aria-labelledby="video-title">
      <h2 id="video-title">Vídeo de la Lección</h2>
      <!-- Reproductor principal con múltiples fuentes y subtítulos -->
      <video controls poster="poster-leccion4.jpg" preload="metadata" width="800" height="450">
        <source src="leccion4.webm" type="video/webm">
        <source src="leccion4.mp4" type="video/mp4">
        
        <!-- Subtítulos e información de accesibilidad -->
        <track src="subs-es.vtt" kind="subtitles" srclang="es" label="Español" default>
        <track src="desc-es.vtt" kind="descriptions" srclang="es" label="Descripción de Audio (Español)">
        
        <p>Tu navegador no soporta vídeo HTML5. <a href="leccion4.mp4">Descargar el vídeo</a>.</p>
      </video>
    </section>

    <section aria-labelledby="audio-title">
      <h2 id="audio-title">Audio Alternativo</h2>
      <p>Escucha esta lección en formato podcast:</p>
      <audio controls>
        <source src="podcast-leccion4.mp3" type="audio/mpeg">
        <p>Tu navegador no soporta el elemento de audio.</p>
      </audio>
    </section>

    <section aria-labelledby="glosario-title">
      <h2 id="glosario-title">Glosario de la lección</h2>
      <!-- Lista descriptiva para pares de término/definición -->
      <dl>
        <dt><dfn>Algoritmo</dfn></dt>
        <dd>Conjunto ordenado de operaciones sistemáticas que permite hacer un cálculo.</dd>
        
        <dt><dfn>Bucle</dfn></dt>
        <dd>Secuencia que ejecuta repetidas veces un trozo de código.</dd>
      </dl>
    </section>

    <section aria-labelledby="relacionados-title">
      <h2 id="relacionados-title">Cursos Recomendados</h2>
      <article>
        <!-- Imágenes responsivas con formatos modernos -->
        <picture>
          <source srcset="curso-avanzado.avif" type="image/avif">
          <img src="curso-avanzado.jpg" alt="Estudiantes programando frente a un monitor" loading="lazy" width="400" height="250">
        </picture>
        <p><a href="https://externo.ejemplo.com/curso" target="_blank" rel="noopener noreferrer">Ver curso avanzado de JavaScript</a></p>
      </article>
    </section>
  </main>

</body>
</html>
```

### Explicación de la Solución 3
1. **Vídeo Robusto:** La etiqueta `<video>` declara un tamaño base para evitar saltos (`width/height`), muestra una miniatura (`poster`) y delega al navegador descargar solo los metadatos al inicio (`preload`). Usa `<source>` en orden de compresión (WebM primero, luego MP4).
2. **Accesibilidad Multimedia (`<track>`):** Fundamental para usuarios con discapacidad visual o auditiva. Un `<track>` de tipo `subtitles` ofrece texto en pantalla (por defecto activado), y otro de tipo `descriptions` es usado por lectores de pantalla para narrar la acción visual en los silencios.
3. **Semántica de Glosario:** La lista `<dl>`, junto con `<dt>` (término) y `<dd>` (descripción), es la única forma semántica correcta de listar vocabularios, por encima de las listas desordenadas convencionales.

## Solución: Práctica Global 4 (Panel de Control Financiero)

Esta práctica pone a prueba la capacidad de trazar el eje X e Y de una tabla compleja para que un lector de pantalla pueda cruzar datos sin perder el contexto.

```html title="dashboard-solucion.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Informe Financiero Q3</title>
</head>
<body>

  <header>
    <h1>Informe Financiero Q3</h1>
    <!-- Vídeo corporativo decorativo: autoplay, silenciado y en bucle -->
    <video src="bg-finance.mp4" autoplay loop muted playsinline aria-hidden="true" width="100%"></video>
  </header>

  <main>
    <section>
      <h2>Resumen de Ingresos y Gastos</h2>
      
      <table>
        <caption>Resultados financieros consolidados por región (Q3)</caption>
        
        <thead>
          <!-- Fila 1 de cabecera: Agrupaciones principales -->
          <tr>
            <td></td> <!-- Celda vacía en la esquina superior izquierda -->
            <th scope="col" colspan="2">Ingresos</th>
            <th scope="col" colspan="2">Gastos</th>
          </tr>
          <!-- Fila 2 de cabecera: Sub-regiones -->
          <tr>
            <td></td> <!-- Celda vacía para alinear con la primera columna de encabezados de fila -->
            <th scope="col">Norteamérica</th>
            <th scope="col">Europa</th>
            <th scope="col">Norteamérica</th>
            <th scope="col">Europa</th>
          </tr>
        </thead>
        
        <tbody>
          <!-- Fila de Software -->
          <tr>
            <th scope="row">Software</th>
            <td>$50k</td>
            <td>$40k</td>
            <td>$10k</td>
            <td>$12k</td>
          </tr>
          <!-- Fila de Hardware -->
          <tr>
            <th scope="row">Hardware</th>
            <td>$30k</td>
            <td>$20k</td>
            <td>$15k</td>
            <td>$10k</td>
          </tr>
        </tbody>
        
        <tfoot>
          <!-- Fila de Totales (Pie de tabla) -->
          <tr>
            <th scope="row">Totales</th>
            <td>$80k</td>
            <td>$60k</td>
            <td>$25k</td>
            <td>$22k</td>
          </tr>
        </tfoot>
      </table>

    </section>
  </main>

</body>
</html>
```

### Explicación de la Solución 4
1. **Vídeo de Fondo (Ambiental):** Los vídeos puramente decorativos deben llevar `muted autoplay loop` (y `playsinline` para iOS). Como no aportan información, añadimos `aria-hidden="true"` para que el lector de pantalla los ignore, reduciendo el "ruido".
2. **Tabla - Estructura TR/TH/TD:** Las celdas de encabezado (`<th>`) se diferencian estrictamente de las celdas de datos (`<td>`).
3. **El superpoder de `scope`:** Es el núcleo de esta práctica. En el `<thead>`, los `<th>` tienen `scope="col"` (esta celda da título a la columna que tiene debajo). En el `<tbody>` y `<tfoot>`, la primera celda de la izquierda es un `<th>` con `scope="row"` (da título a todos los datos que tiene a su derecha). Así, si un usuario invidente está en la celda "$40k", su lector dirá: *"Software, Ingresos, Europa: $40k"*.
4. **`colspan`:** Se usa en la primera fila del `thead` para que la celda "Ingresos" se expanda horizontalmente ocupando el espacio de dos columnas secundarias (Norteamérica y Europa).

## Solución: Práctica Global 5 (Sistema de Reservas)

Esta solución implementa un formulario sólido, accesible y con validación nativa sin requerir JavaScript.

```html title="reserva-solucion.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Reserva tu Estancia - Hotel Paraíso</title>
</head>
<body>

  <main>
    <h1>Reserva tu Estancia en Hotel Paraíso</h1>

    <!-- Formulario estructurado y agrupado -->
    <form action="/procesar-reserva" method="POST">
      
      <!-- Bloque 1: Datos Personales -->
      <fieldset>
        <legend>Datos del Huésped</legend>
        
        <div>
          <label for="nombre">Nombre Completo:</label>
          <input type="text" id="nombre" name="nombre_huesped" required>
        </div>

        <div>
          <label for="email">Email de contacto:</label>
          <input type="email" id="email" name="correo" required>
        </div>

        <div>
          <label for="pais">País de procedencia:</label>
          <input type="text" id="pais" name="pais" list="lista-paises">
          <datalist id="lista-paises">
            <option value="España"></option>
            <option value="Francia"></option>
            <option value="Italia"></option>
            <option value="Portugal"></option>
          </datalist>
        </div>
        
        <div>
          <label for="cp">Código Postal (5 dígitos):</label>
          <input type="text" id="cp" name="codigo_postal" pattern="[0-9]{5}" title="Debe contener exactamente 5 números">
        </div>
      </fieldset>

      <!-- Bloque 2: Detalles de la Reserva -->
      <fieldset>
        <legend>Detalles de la Reserva</legend>
        
        <div>
          <label for="fecha-in">Fecha de Entrada:</label>
          <input type="date" id="fecha-in" name="check_in" required>
        </div>

        <div>
          <label for="fecha-out">Fecha de Salida:</label>
          <input type="date" id="fecha-out" name="check_out" required>
        </div>

        <div>
          <label for="huespedes">Número de Personas (1-5):</label>
          <input type="number" id="huespedes" name="num_personas" min="1" max="5" value="2" required>
        </div>

        <div>
          <label for="habitacion">Tipo de Habitación:</label>
          <select id="habitacion" name="tipo_habitacion" required>
            <option value="">-- Selecciona una habitación --</option>
            <optgroup label="Básicas">
              <option value="individual">Individual</option>
              <option value="doble">Doble</option>
            </optgroup>
            <optgroup label="Premium">
              <option value="suite-jr">Suite Junior</option>
              <option value="suite-presidencial">Suite Presidencial</option>
            </optgroup>
          </select>
        </div>

        <div>
          <label for="peticiones">Peticiones especiales:</label>
          <textarea id="peticiones" name="comentarios" rows="4" cols="40" placeholder="Alergias, cuna extra..."></textarea>
        </div>
      </fieldset>

      <button type="submit">Confirmar Reserva</button>
      
    </form>
  </main>

</body>
</html>
```

### Explicación de la Solución 5
1. **`<fieldset>` y `<legend>`:** Proporcionan un contexto semántico clave. Al navegar por el formulario, un usuario con lector de pantalla escuchará primero el título "Datos del Huésped" para orientarse y saber a qué grupo pertenecen los inputs siguientes.
2. **Conexión `<label>` a `<input>`:** Todos los campos están rígidamente enlazados. El atributo `for` de la etiqueta coincide exactamente con el atributo `id` del input. Esto no solo es vital para accesibilidad, sino que permite hacer clic en el texto de la etiqueta para enfocar el campo, mejorando enormemente la experiencia táctil.
3. **Validación Nativa:** El uso de atributos como `required`, `min`, `max` y `type="email"` bloquea el envío del formulario mediante el navegador sin necesidad de escribir JavaScript. El atributo `pattern="[0-9]{5}"` usa expresiones regulares para obligar a introducir exactamente 5 números.
4. **Agrupación en `<select>`:** El uso de `<optgroup>` permite organizar visual e internamente opciones largas, creando encabezados no seleccionables ("Básicas" y "Premium") dentro del menú desplegable.
5. **Autocompletado con `<datalist>`:** A diferencia de un `select` estricto, el combo `<input list="id_del_datalist">` junto con su `<datalist>` asociado permite sugerir opciones ("España", "Francia") pero deja total libertad al usuario para escribir texto libre si su opción no se encuentra en la lista.

## Solución: Práctica Global 6 (Plataforma de Noticias Accesible)

Esta solución demuestra un control exhaustivo de ARIA. El HTML resultante comunica un modelo de interfaz complejo (pestañas y notificaciones en vivo) a los lectores de pantalla sin depender de frameworks ni JavaScript para la capa semántica.

```html title="noticias-solucion.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>A11y News - El portal de noticias accesible</title>
</head>
<body>

  <!-- Skip Link: Primer elemento interactivo del documento -->
  <a href="#contenido-principal" class="skip-link" style="position: absolute; left: -9999px;">
    Saltar al contenido principal
  </a>

  <header>
    <h1>A11y News</h1>
    
    <!-- Navegación diferenciada con aria-label -->
    <nav aria-label="Navegación principal">
      <ul>
        <li><a href="/" aria-current="page">Inicio</a></li>
        <li><a href="/politica">Política</a></li>
        <li><a href="/tecnologia">Tecnología</a></li>
      </ul>
    </nav>
    
    <!-- Formulario con rol explícito de búsqueda -->
    <form action="/buscar" role="search">
      <label for="buscar">Buscar noticias:</label>
      <input type="search" id="buscar" name="q">
      <button type="submit">Buscar</button>
    </form>
  </header>

  <main id="contenido-principal">
    <!-- Live Region: Lee automáticamente los cambios a los usuarios -->
    <section aria-labelledby="alertas-titulo" aria-live="polite" aria-atomic="true">
      <h2 id="alertas-titulo" class="sr-only">Alertas de Última Hora</h2>
      <p>Última hora: Se aprueba la nueva ley de accesibilidad web en toda la Unión Europea.</p>
    </section>

    <!-- Componente de Pestañas Avanzado (Tabs) -->
    <section aria-label="Noticias por Categoría">
      <!-- Lista de pestañas -->
      <div role="tablist" aria-label="Categorías de Noticias">
        <button role="tab" aria-selected="true" aria-controls="panel-locales" id="tab-locales">
          Noticias Locales
        </button>
        <button role="tab" aria-selected="false" aria-controls="panel-globales" id="tab-globales" tabindex="-1">
          Noticias Globales
        </button>
      </div>
      
      <!-- Panel 1 (Activo) -->
      <div id="panel-locales" role="tabpanel" tabindex="0" aria-labelledby="tab-locales">
        <h3>Titulares de la Ciudad</h3>
        <ul>
          <li><a href="/noticia1">El ayuntamiento renueva el parque tecnológico.</a></li>
        </ul>
      </div>
      
      <!-- Panel 2 (Inactivo) -->
      <div id="panel-globales" role="tabpanel" tabindex="0" aria-labelledby="tab-globales" aria-hidden="true">
        <h3>Titulares Internacionales</h3>
        <ul>
          <li><a href="/noticia2">Avances en Inteligencia Artificial.</a></li>
        </ul>
      </div>
    </section>
  </main>

  <aside aria-label="Contenido secundario">
    <h2>Suscríbete al Boletín</h2>
    <form action="/suscribir" method="POST">
      <label for="boletin-email">Tu correo electrónico:</label>
      <input type="email" id="boletin-email" required>
      <button type="submit">Suscribirme</button>
    </form>
  </aside>

  <footer>
    <nav aria-label="Navegación del pie de página">
      <ul>
        <li><a href="/legal">Aviso Legal</a></li>
        <li><a href="/contacto">Contacto</a></li>
      </ul>
    </nav>
    <p>&copy; 2026 A11y News.</p>
  </footer>

</body>
</html>
```

### Explicación de la Solución 6
1. **Skip Link Estratégico:** Situado en la primera línea del body. Aunque visualmente se ocultará con CSS (`left: -9999px;`), recibirá foco de teclado inmediatamente, permitiendo a los usuarios de navegación por tabulación saltar directamente a `<main id="contenido-principal">`, esquivando el menú repetitivo.
2. **Landmarks Nombrados (`aria-label`):** Al tener múltiples `<nav>`, un lector de pantalla se confunde. Al dotarlos de `aria-label="Navegación principal"` y `aria-label="Navegación del pie de página"`, el usuario invidente sabe exactamente qué tipo de enlaces contiene cada bloque.
3. **Pestañas WAI-ARIA Completas:**
    - El contenedor usa `role="tablist"`.
    - Los botones usan `role="tab"`. El botón inactivo lleva `aria-selected="false"` y un `tabindex="-1"` para salir del orden de tabulación nativo (en un componente real, JS gestionaría las flechas del teclado).
    - Los paneles usan `role="tabpanel"`. El panel inactivo se oculta semánticamente de los lectores usando `aria-hidden="true"`.
4. **Regiones Vivas (`aria-live="polite"`):** Si mediante JS modificamos el texto del `<section>` de alertas, el navegador interrumpirá (de forma educada, sin cortar la frase actual) al lector de pantalla para anunciar el nuevo titular de última hora al usuario en tiempo real.

## Solución: Práctica Global 7 (App de Tareas - Elementos Interactivos)

Este ejercicio demuestra cómo las APIs y los nuevos elementos interactivos de HTML5 aligeran drásticamente el peso de JavaScript, proporcionando modales, acordeones y *storage* nativo en el navegador.

```html title="app-tareas-solucion.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TaskTrack - Gestor de Proyectos</title>
</head>
<body>

  <header>
    <h1>TaskTrack</h1>
    <!-- Canvas preparado para la API de Canvas2D -->
    <canvas id="grafico-progreso" width="200" height="200" aria-label="Gráfico circular de progreso de tareas">
      <!-- Fallback en caso de que JS falle o no soporte canvas -->
      Tu navegador no soporta Canvas. Tareas completadas: 50%.
    </canvas>
  </header>

  <main>
    <section>
      <h2>Tareas Pendientes</h2>
      
      <ul id="lista-tareas">
        <!-- Tarea con atributos de datos personalizados (Dataset API) -->
        <li class="tarea-item" data-tarea-id="t1" data-estado="pendiente" data-prioridad="alta">
          <h3>Reunión de Diseño</h3>
          
          <!-- Elemento Interactivo Nativo: Acordeón -->
          <details>
            <summary>Ver notas de la reunión</summary>
            <p>Orden del día: Revisar el wireframe de la página de inicio, aprobar la paleta de colores y definir los tokens de tipografía.</p>
          </details>
          
        </li>
      </ul>
    </section>

    <section aria-label="Acciones principales">
      <button id="btn-abrir-modal">Añadir Tarea</button>
      <!-- Botón preparado para llamar a la API de Geolocalización -->
      <button id="btn-gps">Vincular GPS actual</button>
    </section>
  </main>

  <!-- Elemento Interactivo Nativo: Ventana Modal -->
  <dialog id="modal-tarea">
    <h2>Nueva Tarea</h2>
    
    <form id="form-nueva-tarea" method="dialog">
      <!-- Formulario para recolectar datos y validar nativamente -->
      <div>
        <label for="titulo-tarea">Título:</label>
        <input type="text" id="titulo-tarea" required>
      </div>
      <div>
        <label for="fecha-tarea">Fecha límite:</label>
        <input type="date" id="fecha-tarea" required>
      </div>
      
      <div>
        <!-- method="dialog" en el formulario hace que este botón de submit cierre el modal sin enviar datos al servidor -->
        <button type="submit" value="guardar">Guardar Tarea</button>
        <button type="button" id="btn-cerrar-modal">Cerrar</button>
      </div>
    </form>
  </dialog>

  <!-- Elemento Nativo: Plantilla (Inerte hasta ser clonada por JS) -->
  <template id="plantilla-tarea">
    <li class="tarea-item" data-tarea-id="" data-estado="pendiente" data-prioridad="normal">
      <h3 class="tarea-titulo"></h3>
      <button class="btn-borrar">Borrar</button>
    </li>
  </template>

</body>
</html>
```

### Explicación de la Solución 7
1. **Acordeones sin JS (`<details>` / `<summary>`):** El elemento `<details>` despliega y oculta contenido de manera 100% nativa. El `<summary>` actúa como el botón (y recibe automáticamente el foco del teclado). Es la forma más limpia y accesible de implementar "Mostrar más".
2. **Ventanas Modales (`<dialog>`):** HTML5 incluye su propio sistema de popups accesibles. Permite gestionar el "foco atrapado" (focus trap) y el fondo opaco (backdrop) desde el navegador. El atributo `method="dialog"` en su `<form>` interno permite que al pulsar el botón `submit`, los datos del formulario se validen, no se recargue la página, y se cierre la ventana modal mágicamente.
3. **Plantillas (`<template>`):** El código dentro de un `<template>` **no se renderiza en pantalla** ni ejecuta scripts/imágenes asociados en la primera carga de la página. Está diseñado para que JavaScript pueda acceder a él, clonarlo, inyectarle los datos de la nueva tarea y volcarlo al DOM de forma supereficiente.
4. **Atributos Personalizados (`data-*`):** Atributos como `data-estado` o `data-tarea-id` nos permiten incrustar metadatos directamente en las etiquetas HTML. En JavaScript se capturarán fácilmente, sirviendo de puente perfecto entre el diseño visual y la lógica de programación.
5. **Preparación para APIs:** La etiqueta `<canvas>` se reserva un bloque en memoria para que la *Canvas API* dibuje píxeles con JavaScript, incluyendo un texto alternativo dentro por accesibilidad. Botones como "Vincular GPS" dejan la estructura lista para asociar un evento de tipo `navigator.geolocation.getCurrentPosition()`.
