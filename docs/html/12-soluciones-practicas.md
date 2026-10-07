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
