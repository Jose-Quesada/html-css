## Ejericios básicos
### Recomendaciones iniciales

- No te preocupes por el diseño visual todavía: El objetivo principal de estos ejercicios es la estructura semántica. El CSS vendrá después para dar estilo.
- Utiliza las herramientas de desarrollo del navegador: Puedes inspeccionar los elementos HTML en el navegador (clic derecho > "Inspeccionar" o "Inspect Element") para ver la estructura que has creado.
- Investiga: Si no estás seguro de qué etiqueta usar, consulta la documentación de MDN Web Docs sobre HTML semántico.
- Practica, practica, practica: La mejor manera de dominar el HTML semántico es aplicándolo constantemente.
### 1. Desmontando el "divitis"

- **Objetivo**: Identificar y reemplazar `<div>` s genéricos por etiquetas semánticas básicas.
- **Escenario**: Tienes un pequeño fragmento de HTML que "funciona" pero no tiene ningún significado estructural.

Código inicial:
```html
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
        <p>&copy; 2025 Mi Web</p>
    </div>
</body>
</html>
```

Tarea:

   1. Abre el archivo index.html en tu editor de código.

   2. Analiza los `<div>`  y sus contenidos.

   3. Reemplaza los `<div>`  con las etiquetas semánticas HTML5 más apropiadas para cada sección:
      - div#cabecera
      - div.menu
      - div#contenido-principal
      - div#pie-de-pagina
   4. Mantén el contenido (los `<h1>` , `<ul>` , `<li>` , `<p>` , etc.) intacto dentro de las nuevas etiquetas.
   5. Abre el archivo modificado en tu navegador para verificar que el contenido se muestra correctamente (el aspecto visual puede no cambiar, lo cual es normal).

### 2. Estructurando un artículo 
- **Objetivo**: Aplicar etiquetas semánticas para organizar el contenido de un artículo o entrada de blog.
- **Escenario**: Vas a crear la estructura de una entrada de blog sobre "El Aceite de Oliva en Andalucía".

Código inicial :

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Artículo: El Aceite de Oliva</title>
</head>
<body>
    <div>
        <h1>El Oro Líquido de Andalucía</h1>
        <p>Por Juan Pérez - 10 de Junio de 2025</p>
    </div>
    <div>
        <p>Andalucía es la cuna del aceite de oliva, un producto esencial en la dieta mediterránea.</p>
        <p>La historia del cultivo del olivo en nuestra región se remonta a miles de años.</p>
        <h2>Variedades Principales</h2>
        <ul>
            <li>Picual</li>
            <li>Hojiblanca</li>
            <li>Arbequina</li>
        </ul>
        <p>Cada variedad aporta matices únicos a nuestro aceite.</p>
    </div>
    <div>
        <h3>Recetas Populares</h3>
        <ul>
            <li>Salmorejo cordobés</li>
            <li>Gazpacho andaluz</li>
            <li>Tostadas con tomate y aceite</li>
        </ul>
    </div>
    <div>
        <p>Más información en nuestra web.</p>
    </div>
</body>
</html>
```

Tarea:

1. Abre el archivo articulo.html .
2. Identifica las diferentes secciones lógicas dentro del contenido.
3. Reestructura el contenido usando las siguientes etiquetas semánticas:
    - `<article>` : Para encerrar todo el contenido del artículo.
    - `<header>` : Para el título del artículo y la información del autor/fecha.
    - `<section>` : Para agrupar las "Variedades Principales" y "Recetas Populares" como secciones temáticas dentro del artículo.
    - `<footer>` : Para la información final del artículo (por ejemplo, "Más información...").
    - `<time>` : Para la fecha de publicación del artículo.
    - Considera si algún `<h2>` o `<h3>` debería estar dentro de una sección con una etiqueta semántica más descriptiva.
4. Verifica el resultado en el navegador.


### 3. Maquetación de un portafolio Semántico
- **Objetivo**: Crear la estructura semántica de una página de portafolio, incorporando múltiples elementos semánticos y una sección lateral.
- **Escenario**: Estás construyendo la página de portafolio de un desarrollador de interfaces. Necesitas una cabecera, navegación principal, una sección principal con proyectos y una barra lateral con información de contacto o enlaces relacionados.

Tarea:

1. Crea un nuevo archivo portafolio.html con la estructura básica de HTML.
2. Define las siguientes secciones semánticas principales:

    - Un `<header>` que contenga un `<h1>` con el nombre del
    desarrollador ("Portafolio de [Tu Nombre]") y un `<nav>` para el menú principal ( Inicio , Proyectos , Contacto ).
    - Un `<main>` que encapsule el contenido principal de la página.
    - Dentro del `<main>` , crea una `<section>` dedicada a los "Proyectos". Dentro de esta sección, cada proyecto debe ser un `<article>` independiente. Cada article de proyecto debería tener:
        - Un `<h2>` para el título del proyecto.
        - Un párrafo `<p>` con una descripción breve.
        - Un enlace `<a>` a "Ver Proyecto".
    - Un `<aside>` que contenga una sección lateral. Dentro de la aside , añade un `<h3>` "Contacto" y un `<ul>` con tu email y redes sociales. Podrías incluir también una figure con una img y su figcaption si quisieras añadir un avatar.
    - Un `<footer>` al final de la página con información de derechos de autor.
3. Añade contenido de relleno (textos y enlaces ficticios) para cada una de estas secciones.
4. Asegúrate de que cada elemento HTML cumple su rol semántico apropiado.
Ejemplo de estructura esperada (sin todo el contenido de relleno):

```html
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
        <nav>
        </nav>
    </header>
    <main>
        <section>
            <h2>Mis Proyectos</h2>
            <article>
                <h3>Proyecto 1: [Nombre del Proyecto]</h3>
            </article>
            <article>
                <h3>Proyecto 2: [Nombre del Proyecto]</h3>
            </article>
        </section>
    </main>
    <aside>
        <h3>Contacto</h3>
    </aside>
    <footer>
    </footer>
</body>
</html>
```
***



## Ejericios ampliación
### 4. Creando un Evento/Noticia Completa con Detalles
- **Objetivo**: Estructurar una página de evento o noticia que incluya información detallada, fechas, ubicaciones y contenido relacionado, utilizando una variedad de etiquetas semánticas.

- **Escenario**: Quieres crear una página de un evento importante o una noticia destacada sobre una iniciativa cultural o tecnológica en Andalucía. La página debe ser rica en información y semánticamente correcta.

**Tarea:**

1. Crea un nuevo archivo evento.html con la estructura básica de HTML.

2. Define la siguiente **estructura semántica**:

    - Una `<header>` principal para la página, con un título `<h1>` del sitio web (ej. "Andalucía Tech Hub" o "Cultura Andaluza") y un `<nav>` para la navegación global (Eventos, Noticias, Recursos).

    - Un `<main>` que contenga el contenido principal de la página del evento/noticia.

    - Dentro de `<main>`, el contenido del evento/noticia en sí debe ser un `<article>`. Este article debe contener:

        - Un `<header>` interno para el título del evento/noticia (`<h2>`) y la información del autor/fecha de publicación. Utiliza `<time>` para la fecha.

        - Una `<section>` para la descripción principal del evento/noticia.

        - Otra `<section>` para "Detalles del Evento" o "Información Clave", que incluya:

            - La **fecha y hora** del evento (usa `<time>` nuevamente, si es posible con el atributo datetime para rango de fechas/horas).

            - La **ubicación** (puedes usar un `<address>` si es una dirección física).

            - Un `<details>` y `<summary>` para mostrar información adicional que se puede expandir/contraer (ej. "Programa Detallado" o "Ponentes Invitados"). Dentro de `<details>`, usa un `<ul>` con los elementos.

        - Si el evento incluye alguna imagen o video representativo con una leyenda, utiliza `<figure>` y `<figcaption>`.

        - Un `<footer>` interno para el article, con un mensaje tipo "Comparte este evento" o enlaces a recursos relacionados.

    - Una `<aside>` que contenga "Noticias Relacionadas" o "Eventos Próximos". Dentro de la aside, puedes tener una lista de enlaces a otros articles o secciones. Cada elemento de esta lista de noticias/eventos relacionados puede ser un `<li>` con un enlace.

    - Un `<footer>` global al final de la página con derechos de autor y enlaces de privacidad/términos.

3. **Añade contenido de relleno** relevante a cada una de estas secciones, simulando un evento real (por ejemplo, "Conferencia de Inteligencia Artificial en Sevilla" o "Festival de Flamenco en Granada").

4. Asegúrate de que la semántica esté correctamente anidada y utilizada.

### 5. Creando un Perfil de Usuario con Múltiples Secciones

- **Objetivo**: Construir la página de perfil de un usuario en una aplicación web, incluyendo sus datos personales, actividad reciente y preferencias, haciendo uso de elementos semánticos para estructurar la información y algunos elementos de formularios.

- **Escenario**: Eres parte del equipo de desarrollo de una plataforma online y necesitas crear la sección de "Mi Perfil" para un usuario, donde se muestren y editen sus datos.

**Tarea:**

1. Crea un nuevo archivo perfil.html con la estructura básica de HTML.

2. Define la siguiente estructura semántica:

    - Una `<header>` principal para la página, con el nombre de la plataforma (ej. "Mi Plataforma Andalucía") y un <nav> de navegación principal (Dashboard, Mi Perfil, Mensajes, Cerrar Sesión).

    - Un `<main>` que contenga todo el contenido del perfil.

    - Dentro de `<main>`, utiliza un `<section>` principal para "Mi Perfil".

    - Dentro de esta sección, crea un `<header>` con un `<h1>` "Mi Perfil de Usuario".

    - A continuación, crea varias `<section>` anidadas para organizar la información:

        - `<section>` para "Datos Personales":

            - Utiliza un `<h2>` para el título.

            - Podrías usar una `<address>` si hay una dirección física.

            - Un formulario (`<form>`) para editar datos como nombre, email, etc. Asegúrate de usar `<label>` correctamente con sus for y id.

            - Un fieldset y legend para agrupar campos relacionados (ej. "Información de Contacto").

        - `<section>` para "Actividad Reciente":

            - Un `<h2>` para el título.

            - Una `<ol>` (lista ordenada) de eventos o acciones recientes del usuario (ej. "Últimos Mensajes Enviados", "Últimos Proyectos Vistos"). Dentro de cada `<li>`, puedes usar un `<time>` para la fecha/hora de la actividad.

        - `<section>` para "Preferencias de la Cuenta":

            - Un `<h2>` para el título.

            - Otro formulario (`<form>`) para opciones como "Notificaciones por Email" (usa input type="checkbox") o "Idioma Preferido" (usa select y option).

    - Un `<aside>` con un "Panel de Acciones Rápidas" o "Enlaces Útiles del Perfil" (ej. "Cambiar Contraseña", "Ver Historial de Compras"). Contendrá una `<ul>` de enlaces.

    - Un `<footer>` global de la página con derechos de autor.

3. Añade contenido de relleno a cada sección, incluyendo campos de formulario y datos ficticios.

4. Presta especial atención a la correcta anidación y el uso de atributos como for, id, datetime.

### Ejercicio - Procesamiento de vídeo nativo

En este ejericio, aprenderemos a ir más allá de la simple reproducción multimedia. Utilizaremos el elemento `<video>` como una fuente de datos de píxeles y el elemento `<canvas>` como un motor de renderizado paralelo.

**1. El reto**
Crearemos una interfaz web donde un vídeo de entrada (un clip promocional de un olivar en Jaén, por ejemplo) se reproduce normalmente. Al mismo tiempo, replicaremos ese vídeo en un lienzo (`<canvas>`) adyacente, aplicando un filtro básico (escala de grises) en tiempo real a cada fotograma.

**Objetivo Visual**: Conseguir una disposición idéntica a la que se muestra en la siguiente imagen, donde el vídeo original está a la izquierda y el resultado del lienzo filtrado a la derecha.

**2. Requisitos previos**

- Conocimientos básicos de HTML y CSS.

- Conocimientos de JavaScript (selección de elementos, funciones y eventos).

- Archivos necesarios: Un clip de vídeo corto (ej. `video_jaen.mp4`). Nota para el alumno: Asegúrate de tener un vídeo en formato `.mp4` disponible.

**3. Guía paso a paso**

=== "HTML"

    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Taller Multimedia - Interfaces</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>

        <header>
            <h1>Procesamiento de Vídeo en Tiempo Real</h1>
            <p>Módulo: Diseño de Interfaces Web (DAW)</p>
        </header>

        <main class="contenedor-multimedia">
            <figure>
                <video id="videoOriginal" crossorigin="anonymous" controls autoplay muted loop>
                    <source src="video_jaen.mp4" type="video/mp4">
                    Tu navegador no soporta vídeo.
                </video>
                <figcaption>Entrada: Vídeo Original</figcaption>
            </figure>

            <figure>
                <canvas id="canvasFiltrado" width="400" height="225"></canvas>
                <figcaption>Salida: Filtro Escala de Grises</figcaption>
            </figure>
        </main>

        <script src="script.js"></script>
    </body>
    </html>
    ```

=== "CSS"

    ```css
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f0f2f5;
        color: #1c1e21;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 0;
        padding: 20px;
    }

    header {
        text-align: center;
        margin-bottom: 40px;
    }

    .contenedor-multimedia {
        display: flex;
        gap: 30px;
        flex-wrap: wrap;
        justify-content: center;
    }

    figure {
        background: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin: 0;
    }

    figcaption {
        margin-top: 15px;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 0.9em;
        color: #555;
    }

    video, canvas {
        width: 450px;
        height: auto;
        border-radius: 4px;
        border: 1px solid #ddd;
        display: block;
    }
    ```

=== "JavaScript"

    ```javascript
    const video = document.getElementById('videoOriginal');
    const canvas = document.getElementById('canvasFiltrado');
    const ctx = canvas.getContext('2d', { willReadFrequently: true });

    function procesarFrame() {
        if (video.paused || video.ended) return;

        // 1. Dibujar el fotograma actual del vídeo en el canvas
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

        // 2. Extraer los datos de imagen (píxeles)
        const frame = ctx.getImageData(0, 0, canvas.width, canvas.height);
        const data = frame.data;

        // 3. Manipulación de píxeles (RGBA)
        for (let i = 0; i < data.length; i += 4) {
            const r = data[i];     // Rojo
            const g = data[i + 1]; // Verde
            const b = data[i + 2]; // Azul

            // Fórmula de luminancia para escala de grises
            const gris = 0.2126 * r + 0.7152 * g + 0.0722 * b;

            data[i]     = gris; // R
            data[i + 1] = gris; // G
            data[i + 2] = gris; // B
        }

        // 4. Inyectar los datos modificados de vuelta al lienzo
        ctx.putImageData(frame, 0, 0);

        // 5. Ciclo de animación optimizado
        requestAnimationFrame(procesarFrame);
    }

    // Iniciar cuando el vídeo se reproduzca
    video.addEventListener('play', procesarFrame);
    ```

**4. Preguntas**

    1. ¿Por qué el canvas tiene un borde pero no contenido al cargar la página?

    2. En el bucle de JavaScript, ¿por qué avanzamos de 4 en 4 (i += 4)?

    3. Si eliminas requestAnimationFrame e intentas usar setInterval, ¿qué sucede con la fluidez del vídeo filtrado?

    4. Si cambiamos la fórmula del gris por gris = verde;, ¿qué efecto visual obtendrías en el lienzo?