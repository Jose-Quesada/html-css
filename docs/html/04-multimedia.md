---
icon: lucide/film
title: "HTML 04 - Multimedia en HTML5"
description: "Vídeo y audio nativos: atributos de video y audio, formatos y compatibilidad, subtítulos con track y ficheros VTT, incrustación externa y accesibilidad."
modulo: "LMH (0373) / DIW (0615) / DI (0488)"
unidad: 4
fecha: "2026-09-29"
---

# HTML 04 — Multimedia en HTML5

Antes de HTML5 la reproducción dependía de plugins externos (el difunto Adobe Flash); hoy el navegador gestiona el contenido multimedia de forma **nativa**. En esta unidad vemos `<video>` y `<audio>` con todos sus atributos, los formatos reales que puedes servir, los subtítulos accesibles con `<track>` y los ficheros `.vtt`, e incrustación de vídeo externo.

!!! note "Conocimientos previos"

    - Estructura del documento HTML y uso de atributos (`src`, `controls`, `width`, `height`).
    - Resolver rutas relativas y absolutas para localizar ficheros dentro del proyecto.
    - Diferenciar contenido informativo de contenido decorativo (idea básica de accesibilidad).

## 1. De los plugins a la reproducción nativa

### 1.1 El problema de los plugins

Flash, Silverlight o QuickTime exigían instalar un componente aparte, actualizaciones constantes y **vulnerabilidades conocidas**; no funcionaban en los iPhone y los buscadores **no podían leer ni indexar** nada de lo que mostraban. Además consumían mucha batería y el desarrollador **no controlaba** ni el reproductor ni la accesibilidad. Hoy esa tarea la asume la ==reproducción nativa== del navegador.

### 1.2 Ventajas de HTML5

- **Sin instalaciones**: `<video>` y `<audio>` se reproducen en cualquier navegador moderno y en móvil.
- **Semántica y accesibilidad**: son elementos del documento, se pueden enfocar con teclado, llevar subtítulos (`<track>`) y describir con ARIA.
- **SEO y rendimiento**: el navegador descarga solo lo necesario (`preload`) y los buscadores entienden el contexto del contenido.
- **Coste cero**: no hay licencias de reproductor; el control lo da el navegador o un *skin* en CSS/JS.
- **Fallback declarativo**: si el navegador no entiende el elemento, se muestra contenido de respaldo dentro de la etiqueta.

!!! info "Antes y después de HTML5"

    Los plugins eran **cajas negras**: nada legible para buscadores ni para lectores de pantalla. Con `<video>` y `<audio>` el contenido pasa a ser **parte del documento**, con foco, subtítulos y estilos propios.

## 2. El elemento `<video>`

### 2.1 Atributos principales

| Atributo | Descripción |
|---|---|
| `controls` | Muestra la barra de reproducción (play, tiempo, volumen, pantalla completa). |
| `src` | Ruta directa al fichero; atajo cuando solo sirves un formato. |
| `poster` | Imagen que se ve mientras carga el vídeo o hasta que se pulsa play. |
| `width` / `height` | Reservan el espacio en píxeles y evitan saltos de diseño (CLS). |
| `preload` | `none` (no descarga nada), `metadata` (duración y pistas), `auto` (todo el fichero). |
| `autoplay` | Inicia solo; los navegadores **solo lo permiten con `muted`**. |
| `loop` | Reinicia el vídeo al finalizar. |
| `muted` | Silencia el audio por defecto. |
| `playsinline` | En iOS reproduce dentro de la página en vez de a pantalla completa. |

!!! info "El atributo imprescindible: controls"

    Un `<video>` sin ==controls== es **solo una caja**: no hay barra, ni atajos de teclado, ni control de volumen. Es lo primero que se revisa en examen (y el error más frecuente).

### 2.2 `src` frente a `<source>` múltiple y contenido de respaldo

```html title="video-multipista.html"
<video controls
       poster="https://dummyimage.com/800x600/ccc/000.png&text=noticia-portada.jpg"
       width="640" height="360"
       preload="metadata"
       playsinline>
  <!-- El navegador recorre los <source> de arriba abajo y carga el primero que entienda -->
  <source src="video/noticia.mp4" type="video/mp4"> <!-- (1)! -->
  <source src="video/noticia.webm" type="video/webm">
  <source src="video/noticia.ogv" type="video/ogg">
  <!-- Fallback interno: solo se ve si el navegador no reconoce <video> -->
  <p>Tu navegador no reproduce vídeo HTML5. <!-- (2)! -->
     <a href="video/noticia.mp4">Descarga el clip (MP4)</a>.</p>
</video>

<!-- Atajo con src directo: un único formato, sin <source> -->
<video controls src="video/noticia.mp4"
       poster="https://dummyimage.com/800x600/ccc/000.png&text=noticia-portada.jpg" width="640" height="360"></video>
```

1.  El orden importa: el navegador se queda con el **primer `type` que entiende**.
2.  El texto de respaldo se ve **solo si el navegador no reconoce** el elemento `<video>`.

Cuando usas varios `<source>`, **no** repitas la ruta en `src` del `<video>`: el navegador tendría dos declaraciones del mismo recurso. El texto de respaldo va siempre **dentro**, después de las pistas.

### 2.3 Reproducción automática: `autoplay`, `muted`, `loop` y `playsinline`

```html title="autoplay.html" hl_lines="2"
<!-- Cabecera decorativa: autoplay SOLO es aceptado con el sonido silenciado -->
<video autoplay muted loop playsinline
       src="video/banner-tienda.webm"
       width="960" height="400"
       aria-hidden="true"></video>
```

Los navegadores bloquean el `autoplay` con sonido porque molesta al usuario y consume datos sin permiso. La **fórmula válida** es `autoplay muted playsinline`; si además quieres sonido, debe activarlo la persona usuaria con su interacción. Un vídeo decorativo como este se oculta a los lectores de pantalla con `aria-hidden="true"` (más detalle en [07-estructura-semantica-y-aria.md](07-estructura-semantica-y-aria.md)).

## 3. Formatos y compatibilidad

| Contenido | Formato | Códec | Comentario |
|---|---|---|---|
| Vídeo | **MP4** | H.264 + AAC | El más compatible: todos los navegadores y móviles. |
| Vídeo | **WebM** | VP9 o AV1 + Opus | Abierto, ligero y muy soportado; ideal como segunda pista. |
| Vídeo | **Ogg** | Theora + Vorbis | Respaldo antiguo, hoy apenas necesario. |
| Audio | **MP3** | MPEG-1 Layer 3 | Universal en cualquier navegador y reproductor. |
| Audio | **MP4 / M4A** | AAC | Calidad superior al MP3, muy soportado. |
| Audio | **WebM / Ogg** | Opus | Mejor relación calidad/tamaño; estándar abierto. |

Nota: la compatibilidad cambia con cada versión de navegador, así que **verifica en `caniuse.com`** el soporte real de `video/mp4`, `video/webm` o `audio/ogg` antes de publicar. La regla práctica es servir **siempre dos formatos** con `<source>`: el códec universal primero y el abierto como alternativa. Sirve siempre ==MP4== y, como segunda pista, WebM.

=== "MP4"

    Códec H.264 + AAC: lo reproduce **cualquier navegador y móvil**; va primero en el listado de `<source>`.

=== "WebM"

    Códec VP9 o AV1 + Opus: estándar **abierto y ligero**; va después como segunda pista.

## 4. El elemento `<audio>`

### 4.1 Atributos y ejemplo con `<source>`

```html title="podcast.html" hl_lines="2"
<!-- Podcast: varios formatos y descarga de respaldo -->
<audio controls preload="none">
  <source src="audio/podcast-clase.mp3" type="audio/mpeg">
  <source src="audio/podcast-clase.ogg" type="audio/ogg">
  <p>Tu navegador no soporta el elemento de audio.
     <a href="audio/podcast-clase.mp3">Descarga el episodio</a>.</p>
</audio>

<!-- Atajo con src directo -->
<audio controls src="audio/podcast-clase.mp3"></audio>
```

`<audio>` admite los mismos atributos de reproducción que `<video>` (`controls`, `autoplay`, `loop`, `muted`, `preload`), pero no tiene `poster` ni `playsinline`. El atributo ==preload== es el que decide **cuánto se descarga** antes de pulsar play: con `none` el navegador no baja nada hasta que se pulsa play, lo recomendable si tienes **varios audios** en la misma página.

### 4.2 Listas de reproducción (playlists)

`<audio>` reproduce **un solo fichero**: no existe un atributo que apunte a varias pistas. Una *playlist* se construye con JavaScript, cambiando el valor de `src` (o del `<source>`) y llamando a `play()`, por ejemplo al pulsar el botón "Siguiente". Conviene usar **`<button>`** para esos controles y mantener siempre disponible un enlace de descarga, por si el script no carga.

## 5. Accesibilidad: subtítulos, descripciones y transcripción

### 5.1 El elemento `<track>`

```html title="subtitulos.html" hl_lines="5"
<video controls poster="https://dummyimage.com/800x600/ccc/000.png&text=noticia-portada.jpg" width="640" height="360" preload="metadata">
  <source src="video/noticia.mp4" type="video/mp4">
  <source src="video/noticia.webm" type="video/webm">
  <!-- Subtítulos en español, activados por defecto -->
  <track kind="subtitles" src="video/noticia-es.vtt" srclang="es" label="Español" default> <!-- (1)! -->
  <!-- Descripción hablada de lo que ocurre en pantalla -->
  <track kind="descriptions" src="video/noticia-es-desc.vtt" srclang="es" label="Descripción de audio">
  <p>Tu navegador no reproduce vídeo HTML5.</p>
</video>
```

1.  `default` deja esa pista **activada al empezar**, sin que nadie abra el menú.

| `kind` | Qué muestra | Para quién |
|---|---|---|
| `subtitles` | Diálogo traducido o en otro idioma | Personas que no hablan el idioma del vídeo |
| `captions` | Diálogo + efectos sonoros ((pasos), música) | Personas sordas o sin sonido |
| `descriptions` | Descripción hablada de la acción en pantalla | Personas con baja visión |
| `chapters` | Puntos de navegación por secciones | Navegación rápida |
| `metadata` | Datos para scripts | Procesado con JavaScript |

Toda pista se declara con ==\<track\>== **dentro** de `<video>` o `<audio>`. Obligatorio en toda pista: `srclang` (idioma) y `label` (nombre visible en el menú de subtítulos); `default` marca la pista activada al empezar. Las pistas deben subirse al **mismo origen** que la página (o con cabeceras CORS correctas).

!!! question "Autoevaluación: ¿qué tipo de pista?"

    Un vídeo muda en el que solo se oyen pasos, música y ruido de fondo, dirigido a **personas sordas**. ¿Qué `kind` eliges y por qué no basta `subtitles`?

    ??? success "Respuesta"

        `kind="captions"`: recoge **diálogo y efectos sonoros** ((pasos), música). `subtitles` solo **traduce la habla**; el sonido ambiente quedaría fuera.

### 5.2 Fichero `.vtt` de ejemplo

```vtt title="noticia-es.vtt"
WEBVTT

1
00:00:00.000 --> 00:00:04.500
Hoy se publica la nueva convocatoria de becas.

2
00:00:04.500 --> 00:00:09.200
El plazo de solicitud permanece abierto hasta el 30 de octubre.
```

El formato WebVTT es **texto plano**: empieza con la cabecera **`WEBVTT`**, después se numeran los bloques con sus tiempos en `HH:MM:SS.mmm --> HH:MM:SS.mmm` y el texto del subtítulo. Se guarda con extensión `.vtt` y se enlaza desde `<track>`.

### 5.3 Transcripción en la página y WCAG

La transcripción completa del audio o del diálogo se publica como texto dentro de la propia página (por ejemplo, en un `<details>` o en una sección con su `<h2>`). Además de cumplir las pautas de accesibilidad, aporta texto indexable para buscadores y permite leer el contenido sin consumir datos ni sonido. En una frase: una ==transcripción== en página cumple la **WCAG 1.2.1**, que exige una alternativa para el contenido exclusivamente audio o vídeo, y la **WCAG 1.2.2** exige subtítulos sincronizados en todo el contenido pregrabado con audio. La estructura semántica de esas secciones está en [07-estructura-semantica-y-aria.md](07-estructura-semantica-y-aria.md).

!!! quote "Criterios WCAG 1.2.1 y 1.2.2 (nivel A)"

    **1.2.1 — Alternativas para audio y vídeo:** toda información presentada solo en audio o vídeo debe tener una **alternativa textual equivalente**, salvo que sea un medio de reemplazo y el contenido ya esté descrito.

    **1.2.2 — Solo texto (subtítulos):** todo contenido de audio pregrabado **sincronizado** necesita una alternativa basada en texto, salvo que el audio sea un medio de reemplazo para el texto de la página.

!!! success "Comprueba que tu vídeo es accesible"

    - [ ] Todo contenido con audio tiene pista de **subtítulos** (`subtitles` o `captions`).
    - [ ] Cada `<track>` lleva **`srclang`** y **`label`** (y `default` si va activada).
    - [ ] El fichero `.vtt` empieza por **`WEBVTT`** y usa tiempos `HH:MM:SS.mmm --> HH:MM:SS.mmm`.
    - [ ] Hay **transcripción completa** en texto dentro de la propia página.
    - [ ] Revisa los criterios WCAG 1.2.1 y 1.2.2 antes de publicar.

## 6. Incrustar vídeo externo con `<iframe>`

```html title="youtube-incrustado.html"
<iframe
  width="560" height="315"
  src="https://www.youtube-nocookie.com/embed/AbC123XyZ"
  title="Vídeo: presentación del ciclo de Desarrollo de Aplicaciones Web"
  loading="lazy"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture"
  allowfullscreen>
</iframe>
```

`title` es **obligatorio** para accesibilidad, `loading="lazy"` evita cargar el reproductor hasta que aparece en pantalla y `allowfullscreen` habilita el botón de pantalla completa (en los navegadores actuales basta con `allow="fullscreen"`). YouTube y Vimeo ofrecen además versiones sin cookies (`youtube-nocookie.com`) que respetan mejor la privacidad.

El nativo es preferible **si controlas los ficheros**: `<video>` no arrastra cookies ni scripts de terceros, es más ligero, permite tus propios subtítulos `<track>`, tu marca y tus controles, y no muestra vídeos recomendados de la competencia. Usa el `<iframe>` solo cuando el contenido vive en una plataforma externa (clase grabada, conferencia publicada en YouTube): el ==iframe== es la vía de la **incrustación externa**.

## 7. Ejemplo práctico: noticia con vídeo y podcast con transcripción

```html title="noticia-completa.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Nueva convocatoria de becas · IES Marítimo</title>
</head>
<body>
  <main>
    <article>
      <h1>Nueva convocatoria de becas 2026</h1>
      <p>La consejería abre hoy el plazo para solicitar las becas de transporte y material.</p>

      <h2>Vídeo informativo</h2>
      <video controls poster="https://dummyimage.com/800x600/ccc/000.png&text=becas-portada.jpg" width="640" height="360" preload="metadata">
        <source src="video/becas.mp4" type="video/mp4">
        <source src="video/becas.webm" type="video/webm">
        <track kind="subtitles" src="video/becas-es.vtt" srclang="es" label="Español" default>
        <p>Tu navegador no reproduce vídeo HTML5.
           <a href="video/becas.mp4">Descarga el clip</a>.</p>
      </video>
      <p><a href="video/becas-es.vtt">Descargar los subtítulos (VTT)</a></p>
    </article>

    <article>
      <h2>Podcast: la beca en 5 minutos</h2>
      <audio controls preload="none">
        <source src="audio/becas-ep07.mp3" type="audio/mpeg">
        <source src="audio/becas-ep07.ogg" type="audio/ogg">
        <p>Tu navegador no reproduce audio.
           <a href="audio/becas-ep07.mp3">Descarga el episodio</a>.</p>
      </audio>

      <details>
        <summary>Transcripción completa del episodio</summary> <!-- (1)! -->
        <p><strong>00:00</strong> — Buenas tardes, hoy explicamos los requisitos de la beca.</p>
        <p><strong>01:15</strong> — El plazo finaliza el 30 de octubre y la solicitud es en línea.</p>
        <p><strong>03:40</strong> — Dudas frecuentes: renta, convivencia y documentación.</p>
      </details>
    </article>

    <p>Amplía la práctica con [09-ejercicios.md](09-ejercicios.md).</p>
  </main>
</body>
</html>
```

1.  El `<details>` guarda la transcripción completa: **texto legible** sin reproducir nada (WCAG 1.2.1).

## 8. Errores frecuentes y claves del examen

### 8.1 Error común

!!! warning "Error común"

    - **Olvidar `controls`**: sin él no aparece ningún reproductor y el vídeo o el audio no se puede reproducir (salvo que lo manejes con JavaScript).
    - **`autoplay` con sonido**: los navegadores lo bloquean o molestan al usuario; solo se admite junto a `muted` (y en iOS además `playsinline`).
    - **`<source>` sin `type`**: el navegador no sabe qué códec probar y puede saltarse un formato que sí entendería; escribe siempre `type="video/mp4"`, `type="video/webm"`, etc.

### 8.2 Claves para el examen

!!! tip "Claves para el examen"

    - `<video>` y `<audio>` son nativos: sin plugins y con `controls` imprescindible para que el usuario pueda reproducir.
    - Varios `<source>` se comprueban de arriba abajo y se usa el primero con `type` compatible; no combines `src` en el elemento con `<source>`.
    - `preload`: `none` ahorra datos, `metadata` trae duración, `auto` descarga todo; `poster` muestra la imagen previa del vídeo.
    - `autoplay` solo con `muted` (+ `playsinline` en iOS); `loop` repite y el contenido decorativo se oculta con `aria-hidden`.
    - Formatos: MP4/H.264 el seguro, WebM el abierto; audio MP3, AAC y Opus. Sirve dos pistas y verifica en `caniuse.com`.
    - Accesibilidad: `<track>` con `kind`, `srclang`, `label` y opcional `default`, fichero `.vtt` y transcripción en la página (WCAG 1.2.1 y 1.2.2).
    - `<iframe>` externo con `title`, `loading="lazy"` y `allowfullscreen`; si tienes el fichero, el reproductor nativo es mejor.


!!! success "Practica esta unidad"

    - Enunciados: [Ejercicios de la Unidad 4 — Multimedia en HTML5](09-ejercicios.md#u61-alta-en-el-boletin) — cuatro retos (`U4.1` a `U4.4`) — del más básico al más avanzado.
    - Comprueba tu trabajo con [las soluciones de esta unidad](10-ejercicios-soluciones.md#sol-u4).

*[WCAG]: Web Content Accessibility Guidelines
*[CLS]: Cumulative Layout Shift
*[AAC]: Advanced Audio Coding
