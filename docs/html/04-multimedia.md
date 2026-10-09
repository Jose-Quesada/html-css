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

### 2.1 Atributos principales explicados en detalle

Para un alumno que aprende HTML5, la etiqueta `<video>` se controla mediante una combinación de atributos booleanos y de configuración que determinan la interfaz y el comportamiento de red:

| Atributo | Tipo | Función y Comportamiento |
|---|---|---|
| `controls` | Booleano | **Indispensable.** Muestra los controles nativos del navegador (botón play/pausa, barra de progreso, volumen, selector de pistas y pantalla completa). Sin él, el vídeo es solo un fotograma estático sin interactividad. |
| `src` | URL | Ruta directa al archivo multimedia. Solo se utiliza cuando se ofrece un único formato garantizado (atajo rápido). |
| `poster` | URL | Imagen que se muestra antes de reproducir el vídeo o mientras se descarga el primer fotograma. Debe coincidir con la relación de aspecto del vídeo para evitar saltos visuales. |
| `width` / `height` | Píxeles | Reservan el espacio físico en la cuadrícula de maquetación, evitando el salto de página (**CLS - Cumulative Layout Shift**). |
| `preload` | Enumerado | Controla la política de descarga previa: `none`, `metadata` o `auto`. |
| `autoplay` | Booleano | Inicia la reproducción de forma automática. **Los navegadores lo bloquean por seguridad si no va acompañado de `muted`**. |
| `muted` | Booleano | Inicia el vídeo con el volumen silenciado (audio en cero). Requisito para permitir `autoplay`. |
| `loop` | Booleano | Reinicia la reproducción continuamente desde el segundo cero al llegar al final. |
| `playsinline` | Booleano | En navegadores móviles (especialmente Safari en iOS), fuerza la reproducción dentro del flujo del diseño web, impidiendo que el sistema operativo lo abra a pantalla completa obligatoria. |

#### ¿Qué valor elegir en `preload`?
- **`preload="none"`:** El navegador **no descarga ni un solo byte** del archivo de vídeo hasta que el usuario pulsa deliberadamente el botón de reproducción. Es la opción obligatoria cuando una página contiene múltiples vídeos o episodios de podcast, evitando colapsar el ancho de banda del usuario.
- **`preload="metadata"`:** El navegador descarga únicamente la cabecera del archivo: duración total, dimensiones en píxeles y pistas de subtítulos disponibles, pero sin precargar el flujo de vídeo. Es el **equilibrio perfecto** para la mayoría de webs, permitiendo que la barra de tiempo se dibuje correctamente sin consumir datos excesivos.
- **`preload="auto"`:** Indica al navegador que descargue el vídeo completo de forma anticipada tan pronto como se cargue la página web, asumiendo que el usuario lo verá con certeza. Debe evitarse en móviles.

!!! info "El atributo imprescindible: controls"

    Un `<video>` sin ==controls== es **solo una caja muda**: no hay botón de play, ni barra de desplazamiento, ni teclado (barra espaciadora para pausar, flechas para avanzar/retroceder), ni control de volumen. Es lo primero que se revisa en un examen técnico y el fallo más habitual de los principiantes.

### 2.2 `src` frente a `<source>` múltiple y contenido de respaldo

```html title="video-multipista.html"
<video controls
       poster="https://dummyimage.com/800x600/ccc/000.png&text=noticia-portada.jpg"
       width="640" height="360"
       preload="metadata"
       playsinline>
  <!-- El navegador recorre los <source> de arriba abajo y carga el primero que entienda -->
  <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4" type="video/mp4"> <!-- (1)! -->
  <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.webm" type="video/webm">
  <source src="https://www.w3schools.com/html/mov_bbb.ogg" type="video/ogg">
  <!-- Fallback interno: solo se ve si el navegador no reconoce <video> -->
  <p>Tu navegador no reproduce vídeo HTML5. <!-- (2)! -->
     <a href="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4">Descarga el clip (MP4)</a>.</p>
</video>

<!-- Atajo con src directo: un único formato, sin <source> -->
<video controls src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"
       poster="https://dummyimage.com/800x600/ccc/000.png&text=noticia-portada.jpg" width="640" height="360"></video>
```

1.  El orden importa: el navegador se queda con el **primer `type` que entiende**.
2.  El texto de respaldo se ve **solo si el navegador no reconoce** el elemento `<video>`.

Cuando usas varios `<source>`, **no** repitas la ruta en `src` del `<video>`: el navegador tendría dos declaraciones del mismo recurso. El texto de respaldo va siempre **dentro**, después de las pistas.

### 2.3 Reproducción automática: `autoplay`, `muted`, `loop` y `playsinline`

```html title="autoplay.html" hl_lines="2"
<!-- Cabecera decorativa: autoplay SOLO es aceptado con el sonido silenciado -->
<video autoplay muted loop playsinline
       src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.webm"
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
  <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3" type="audio/mpeg">
  <source src="https://www.w3schools.com/html/horse.ogg" type="audio/ogg">
  <p>Tu navegador no soporta el elemento de audio.
     <a href="https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3">Descarga el episodio</a>.</p>
</audio>

<!-- Atajo con src directo -->
<audio controls src="https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3"></audio>
```

`<audio>` admite los mismos atributos de reproducción que `<video>` (`controls`, `autoplay`, `loop`, `muted`, `preload`), pero no tiene `poster` ni `playsinline`. El atributo ==preload== es el que decide **cuánto se descarga** antes de pulsar play: con `none` el navegador no baja nada hasta que se pulsa play, lo recomendable si tienes **varios audios** en la misma página.

### 4.2 Listas de reproducción (playlists)

`<audio>` reproduce **un solo fichero**: no existe un atributo que apunte a varias pistas. Una *playlist* se construye con JavaScript, cambiando el valor de `src` (o del `<source>`) y llamando a `play()`, por ejemplo al pulsar el botón "Siguiente". Conviene usar **`<button>`** para esos controles y mantener siempre disponible un enlace de descarga, por si el script no carga.

## 5. Accesibilidad: subtítulos, descripciones y transcripción

### 5.1 El elemento `<track>`: Subtítulos y pistas de accesibilidad

HTML5 incorpora el elemento hijo `<track>` para asociar pistas de texto temporizadas (*timed text tracks*) a un reproductor de `<video>` o `<audio>`. Su uso es un **requisito legal vinculante en España y Europa** (Directiva 2016/2102 y Real Decreto 1112/2018 para el sector público y Ley 11/2023 para el sector privado).

```html title="subtitulos.html" hl_lines="5 7"
<video controls 
       poster="https://dummyimage.com/800x600/ccc/000.png&text=noticia-portada.jpg" 
       width="640" height="360" 
       preload="metadata"
       crossorigin="anonymous">
  <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4" type="video/mp4">
  <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.webm" type="video/webm">
  
  <!-- 1. Subtítulos para sordos en español (activados al iniciar) -->
  <track kind="captions" src="https://interactive-examples.mdn.mozilla.net/media/examples/friday.vtt" 
         srclang="es" label="Español (CC)" default> <!-- (1)! -->
         
  <!-- 2. Subtítulos traducidos al inglés (opcionales) -->
  <track kind="subtitles" src="https://interactive-examples.mdn.mozilla.net/media/examples/friday.vtt" 
         srclang="en" label="English">
         
  <!-- 3. Audiodescripción hablada para personas con baja visión -->
  <track kind="descriptions" src="https://interactive-examples.mdn.mozilla.net/media/examples/friday.vtt" 
         srclang="es" label="Descripción de audio">
         
  <p>Tu navegador no reproduce vídeo HTML5.</p>
</video>
```

1.  `default`: Activa automáticamente esta pista al iniciar el reproductor sin que el usuario tenga que seleccionarla a mano en el menú de subtítulos.

#### Los 5 tipos de pista (`kind`): ¿Cuándo se usa cada uno?

| Valor de `kind` | Qué contiene | Público destinatario | Ejemplo de contenido |
|---|---|---|---|
| `captions` | **Diálogo íntegro + efectos sonoros relevantes** (*Closed Captions / CC*) | Personas sordas, con hipoacusia o usuarios en entornos sin sonido (oficinas, transporte) | `[Música de suspense]`, `[Pasos aproximándose]`, `¡Cuidado!` |
| `subtitles` | **Traducción del diálogo hablado** | Personas que no dominan el idioma original del vídeo | Traduce una conversación en inglés al español. No incluye efectos sonoros. |
| `descriptions` | **Descripción textual de lo que ocurre visualmente en pantalla** | Personas ciegas o con baja visión | El sintetizador de voz lee lo que pasa en silencios: *"El profesor abre la consola de Linux y escribe el comando."* |
| `chapters` | **Marcas de tiempo de navegación por capítulos** | Todos los usuarios | Permite al reproductor dibujar marcas en la barra de tiempo (*"00:00 Introducción", "04:15 Demostración"*). |
| `metadata` | **Datos estructurados invisibles para el usuario** | Scripts de JavaScript | Coordenadas, información de productos que aparecen en pantalla para tiendas interactivas. |

#### Atributos indispensables de `<track>`:
- **`src`:** URL al archivo con extensión `.vtt`.
- **`srclang`:** Código de idioma en formato BCP 47 (ej. `es`, `en`, `fr`). **Obligatorio** si `kind="subtitles"`.
- **`label`:** Título legible que aparece en el menú desplegable del reproductor (ej. *"Español"*, *"Inglés con subtítulos"*).
- **`default`:** Booleano. Solo puede haber **un único `<track>` con `default`** en todo el elemento `<video>`.
- **Atención a la seguridad (CORS):** El archivo `.vtt` debe estar alojado en el mismo dominio que la página web. Si está en un servidor externo, el servidor debe emitir la cabecera HTTP `Access-Control-Allow-Origin: *` y el `<video>` debe incluir el atributo `crossorigin="anonymous"`; si no se cumple, el navegador **bloqueará en silencio los subtítulos** y el botón de subtítulos no aparecerá.

---

### 5.2 Estructura del fichero WebVTT (`.vtt`)

WebVTT (*Web Video Text Tracks*) es el estándar oficial del W3C para subtítulos en la web. Es un **fichero de texto plano** con codificación **UTF-8**:

```vtt title="noticia-es.vtt"
WEBVTT

1
00:00:00.000 --> 00:00:04.500
Hoy se publica la nueva convocatoria de becas de formación.

2
00:00:04.500 --> 00:00:09.200
[Música institucional de fondo]
El plazo de solicitud permanece abierto hasta el 30 de octubre.

3
00:00:09.500 --> 00:00:14.000
<v Consejera>Animamos a todo el alumnado de FP a participar.</v>
```

#### Reglas de sintaxis de WebVTT:
1. **La primera línea debe ser siempre `WEBVTT`**: Si hay un espacio, un salto de línea previo o un carácter extraño antes de `WEBVTT`, el archivo será rechazado por el navegador.
2. **Identificador del bloque (*Cue identifier*):** Un número o etiqueta opcional (ej. `1`, `2`).
3. **Línea de tiempo (*Cue timings*):** Formato estricto `HH:MM:SS.mmm --> HH:MM:SS.mmm` (horas, minutos, segundos y milisegundos separados por un punto). La flecha debe ser exactamente `-->` con un espacio a cada lado.
4. **Voz o personaje con `<v Nombre>`:** Permite indicar quién habla en ese subtítulo, lo cual puede estilizarse con CSS mediante la pseudoclase `::cue`.

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
        <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4" type="video/mp4">
        <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.webm" type="video/webm">
        <track kind="subtitles" src="https://interactive-examples.mdn.mozilla.net/media/examples/friday.vtt" srclang="es" label="Español" default>
        <p>Tu navegador no reproduce vídeo HTML5.
           <a href="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4">Descarga el clip</a>.</p>
      </video>
      <p><a href="https://interactive-examples.mdn.mozilla.net/media/examples/friday.vtt">Descargar los subtítulos (VTT)</a></p>
    </article>

    <article>
      <h2>Podcast: la beca en 5 minutos</h2>
      <audio controls preload="none">
        <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3" type="audio/mpeg">
        <source src="https://www.w3schools.com/html/horse.ogg" type="audio/ogg">
        <p>Tu navegador no reproduce audio.
           <a href="https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3">Descarga el episodio</a>.</p>
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

---

### 7.1 Explicación detallada: ¿Por qué se usa cada etiqueta y para qué sirve?

A continuación se profundiza en las razones técnicas, de diseño y de accesibilidad universal que motivan la elección de cada elemento multimedia y sus atributos en `noticia-completa.html`:

#### 1. `<video>` — El reproductor de vídeo nativo HTML5
- **¿Para qué sirve?** Incrusta un flujo de vídeo directamente en el navegador sin necesitar complementos externos de terceros (como el antiguo Flash Player).
- **Desglose de sus atributos esenciales:**
    - **`controls`:** Habilita la interfaz nativa de reproducción del navegador (barra de progreso, botón de reproducción/pausa, control de volumen, selector de pistas y botón de pantalla completa). Sin este atributo booleano, el vídeo parecería una imagen estática congelada a menos que se programen botones personalizados en JavaScript. Además, los controles nativos garantizan navegación accesible por teclado mediante <kbd>Espacio</kbd> y flechas de dirección.
    - **`poster="..."`:** Imagen fija que se muestra en el reproductor antes de que el usuario pulse "Play" o mientras el vídeo se descarga. Evita un rectángulo negro vacío en el diseño visual de la web y comunica visualmente de qué trata el clip.
    - **`width="640"` y `height="360"`:** Fijan la relación de aspecto espacial (16:9). El navegador reserva el hueco exacto en el diseño antes de cargar el primer fotograma del archivo multimedia, previniendo el desplazamiento no deseado del contenido (*Cumulative Layout Shift - CLS*).
    - **`preload="metadata"`:** Optimización crítica de rendimiento y ahorro de datos. Indica al navegador que **solo descargue la cabecera del archivo** (duración total, dimensiones y pistas disponibles), sin descargar los megabytes del vídeo hasta que el usuario decida reproducirlo voluntariamente.

#### 2. `<source>` — Negociación de códecs y formatos en vídeo
- **¿Para qué sirve?** Ofrece fuentes alternativas del mismo contenido multimedia para que el navegador escoja la primera que sea compatible con su motor interno de decodificación.
- **¿Por qué se ponen en este orden (`mp4` y luego `webm`)?**
    - `type="video/mp4"`: Contenedor universalmente compatible con todos los sistemas operativos y dispositivos móviles (códec H.264 / AAC).
    - `type="video/webm"`: Formato abierto y libre de derechos impulsado para la web con alta compresión (códec VP8/VP9 o AV1).
    - El atributo `type` es vital porque le ahorra al navegador tener que hacer una petición de red a ciegas: lee el tipo MIME y, si no lo soporta, pasa inmediatamente al siguiente `<source>` sin malgastar conexiones HTTP.

#### 3. `<track>` — Accesibilidad auditiva mediante pistas de texto (WebVTT)
- **¿Para qué sirve?** Sincroniza pistas de texto temporalizadas con la línea de tiempo del vídeo o audio.
- **Desglose de sus atributos clave:**
    - **`kind="subtitles"`:** Especifica que el archivo contiene la traducción o transcripción del diálogo hablado. Otros valores posibles son `captions` (incluye efectos sonoros como *«música épica»* para personas sordas), `descriptions` (audiodescripción) o `chapters` (capítulos de navegación).
    - **`src="..."`:** Ruta al archivo estandarizado con formato **WebVTT** (`.vtt`), que contiene las marcas de tiempo (`00:00:01.000 --> 00:00:04.000`) y el texto correspondiente.
    - **`srclang="es"`:** Código de idioma internacional (BCP 47) de los subtítulos (español).
    - **`label="Español"`:** Nombre amigable y legible que aparecerá en el menú de selección de idiomas del reproductor visual.
    - **`default`:** Indica al navegador que active esta pista automáticamente por defecto si las preferencias de accesibilidad del usuario no especifican otro idioma preferente.

#### 4. Texto de fallback dentro de `<video>` y `<audio>`
- **¿Para qué sirve?** El texto y los enlaces situados al final de `<video>` y `<audio>` son ignorados por los navegadores modernos, pero **se muestran si el navegador es muy antiguo o tiene deshabilitada la reproducción multimedia**.
- **Buena práctica:** Incluir un enlace directo de descarga del archivo (`<a href="...">Descarga el clip</a>`) asegura que cualquier usuario pueda consumir la información en un reproductor de escritorio externo si su navegador presenta incompatibilidades.

#### 5. `<audio controls preload="none">` — El reproductor de sonido
- **¿Para qué sirve?** Incrusta sonido o podcasts directamente en la página web.
- **`controls`:** Muestra la botonera básica de sonido accesible por teclado.
- **`preload="none"`:** Como se trata de un podcast complementario situado al final de la página, esta directiva indica al navegador que **no gaste ni un solo byte de conexión a internet** en este archivo de audio hasta que el usuario decida expresamente hacer clic en el botón de reproducción.

#### 6. `<details>` y `<summary>` — Transcripción textual accesible (Criterio WCAG 1.2.1)
- **¿Para qué sirven?** Crean un componente interactivo desplegable nativo sin necesidad de escribir ni una sola línea de JavaScript ni CSS.
    - `<summary>`: Representa el encabezado o etiqueta visible del desplegable (*«Transcripción completa del episodio»*).
    - El contenido interior de `<details>` permanece oculto por defecto y se despliega limpiamente al hacer clic sobre el `<summary>`.
- **Importancia fundamental en Accesibilidad (WCAG Nivel A):** El criterio de conformidad WCAG 1.2.1 exige que todo contenido exclusivamente sonoro (un podcast, un discurso) disponga de una **alternativa basada en texto completa**. Las personas con discapacidad auditiva o aquellos usuarios que navegan en entornos ruidosos o en una biblioteca sin auriculares pueden pulsar sobre el desplegable y leer íntegramente la conversación sin perderse nada.

---

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
