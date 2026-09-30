## Ejercicio 1

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página Simple</title>
</head>
<body>
    <header> 
        <h1>Bienvenido a mi Web</h1>
        <nav> 
            <ul>
                <li><a href="#">Inicio</a></li>
                <li><a href="#">Sobre Nosotros</a></li>
                <li><a href="#">Contacto</a></li>
            </ul>
        </nav>
    </header>
    <main> 
        <p>Este es el contenido principal de la página.</p>
        <p>Aquí podríamos hablar de muchos temas interesantes.</p>
    </main>
    <footer> 
        <p>&copy; 2025 Mi Web</p>
    </footer>
</body>
</html>
```
**Justificación de los cambios**:

- `<header>` : Contiene el contenido introductorio de la página, como el título principal y la navegación.

- `<nav>` : Específicamente para enlaces de navegación principales.

- `<main>` : Representa el contenido principal y único de la página.

- `<footer>` : Contiene información de pie de página, como derechos de autor.


## Ejercicio 2

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Artículo: El Aceite de Oliva</title>
</head>
<body>
    <article> 
        <header>
            <h1>El Oro Líquido de Andalucía</h1>
            <p>Por Juan Pérez - <time datetime="2025-06-10">10 de Junio de 2025</time></p>
        </header>
        <p>Andalucía es la cuna del aceite de oliva, un producto esencial en la dieta mediterránea.</p>
        <p>La historia del cultivo del olivo en nuestra región se remonta a miles de años.</p>
        <section> 
            <h2>Variedades Principales</h2>
            <ul>
                <li>Picual</li>
                <li>Hojiblanca</li>
                <li>Arbequina</li>
            </ul>
            <p>Cada variedad aporta matices únicos a nuestro aceite.</p>
        </section>
        <section> 
            <h3>Recetas Populares</h3>
            <ul>
                <li>Salmorejo cordobés</li>
                <li>Gazpacho andaluz</li>
                <li>Tostadas con tomate y aceite</li>
            </ul>
        </section>
        <footer> 
            <p>Más información en nuestra web.</p>
        </footer>
    </article>
</body>
</html>
```

**Justificación de los cambios**:

- `<article>`: Envuelve todo el contenido que es una pieza independiente y autosuficiente de información (como un artículo de blog).

- `<header>` (dentro de `<article>`): Contiene la introducción del artículo, incluyendo el título y la metainformación.

- `<time>`: Permite a los navegadores y motores de búsqueda entender que el texto "10 de Junio de 2025" es una fecha, con un formato estándar datetime para legibilidad máquina.

- `<section>`: Se utiliza para agrupar contenido temáticamente relacionado dentro del artículo (variedades y recetas).

- `<footer>` (dentro de `<article>`): Contiene información de pie de página específica del artículo.

## Ejercicio 3

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
            <ul>
                <li><a href="#inicio">Inicio</a></li>
                <li><a href="#proyectos">Proyectos</a></li>
                <li><a href="#contacto">Contacto</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="inicio">
            <h2>¡Hola! Soy [Tu Nombre], desarrollador de interfaces en Andalucía.</h2>
            <p>Con pasión por crear experiencias web intuitivas y accesibles.</p>
        </section>

        <section id="proyectos">
            <h2>Mis Proyectos</h2>
            <article>
                <h3>Proyecto 1: Diseño de una Tienda Online</h3>
                <p>Desarrollo de la interfaz de usuario para una tienda online de productos locales andaluces, enfocándose en la usabilidad y la experiencia móvil.</p>
                <a href="#">Ver Proyecto</a>
            </article>
            <article>
                <h3>Proyecto 2: Aplicación Web para Gestión de Olivos</h3>
                <p>Creación de un panel de control interactivo para agricultores, mostrando datos en tiempo real sobre el cultivo de olivos.</p>
                <a href="#">Ver Proyecto</a>
            </article>
            <article>
                <h3>Proyecto 3: Blog de Gastronomía Andaluza</h3>
                <p>Implementación de un blog responsivo para recetas y artículos sobre la rica gastronomía de la región.</p>
                <a href="#">Ver Proyecto</a>
            </article>
        </section>
    </main>

    <aside>
        <h3>Contacto</h3>
        <p>Email: <a href="mailto:tu.email@example.com">tu.email@example.com</a></p>
        <p>LinkedIn: <a href="https://www.linkedin.com/in/tunombre" target="_blank">linkedin.com/in/tunombre</a></p>
        <p>GitHub: <a href="https://github.com/tuusuario" target="_blank">github.com/tuusuario</a></p>

        <figure>
            <img src="https://via.placeholder.com/150" alt="Avatar de [Tu Nombre]">
            <figcaption>Mi avatar profesional</figcaption>
        </figure>
    </aside>

    <footer>
        <p>&copy; 2025 [Tu Nombre]. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
```

**Justificación de los cambios**:

- `<header>` y `<nav>`: Como en ejercicios anteriores, para la cabecera global y la navegación principal.

- `<main>`: Encapsula el contenido principal y dinámico de la página.

- `<section id="inicio">`: Una sección temática para la introducción del portafolio.

- `<section id="proyectos">`: Una sección dedicada a agrupar los proyectos.

- `<article>` (dentro de section#proyectos): Cada proyecto individual es una pieza de contenido independiente, por lo que article es la etiqueta ideal.

- `<aside>`: Contiene contenido relacionado indirectamente con el contenido principal (información de contacto y un avatar, que podría ir en una barra lateral).

- `<figure>` y `<figcaption>` (dentro de `<aside>`): Para agrupar una imagen (`<img>`) con su leyenda (`<figcaption>`), haciéndola una unidad semántica.

- `<footer>`: Para la información de derechos de autor al final de la página.

## Ejercicio 4

```html
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
        <nav>
            <ul>
                <li><a href="#">Eventos</a></li>
                <li><a href="#">Noticias</a></li>
                <li><a href="#">Recursos</a></li>
                <li><a href="#">Contacto</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <article>
            <header>
                <h2>Conferencia Internacional de Inteligencia Artificial en Sevilla</h2>
                <p>Publicado por Laura García - <time datetime="2025-06-05">5 de Junio de 2025</time></p>
            </header>

            <figure>
                <img src="https://via.placeholder.com/600x300?text=Conferencia+IA" alt="Imagen de la Conferencia de Inteligencia Artificial">
                <figcaption>Vista aérea del Palacio de Congresos de Sevilla durante la conferencia.</figcaption>
            </figure>

            <section>
                <h3>Innovación y Futuro en el Corazón de Andalucía</h3>
                <p>Sevilla acogerá la próxima semana la Conferencia Internacional de Inteligencia Artificial, un evento que reunirá a expertos, investigadores y empresas líderes del sector. El objetivo es debatir los últimos avances, desafíos éticos y aplicaciones prácticas de la IA en diversos campos.</p>
                <p>Este encuentro es una oportunidad única para la comunidad tecnológica de Andalucía de conectar con las tendencias globales y fomentar la colaboración.</p>
            </section>

            <section>
                <h3>Detalles del Evento</h3>
                <ul>
                    <li>**Fechas:** <time datetime="2025-06-16T09:00">Lunes 16 de Junio</time> a <time datetime="2025-06-18T18:00">Miércoles 18 de Junio de 2025</time></li>
                    <li>**Horario:** 09:00h - 18:00h (GMT+2)</li>
                    <li>**Ubicación:** <address>Palacio de Congresos y Exposiciones de Sevilla (FIBES), Avda. Alcalde Luis Uruñuela 1, 41020 Sevilla</address></li>
                    <li>**Registro:** <a href="#">Inscríbete aquí</a></li>
                </ul>

                <details>
                    <summary>Programa Detallado de la Conferencia</summary>
                    <ul>
                        <li>**Día 1: IA y Sociedad**
                            <ul>
                                <li>09:30h - Conferencia Inaugural: "El Impacto de la IA en la Economía Andaluza"</li>
                                <li>11:00h - Panel de Debate: "Ética y Regulación en la IA"</li>
                            </ul>
                        </li>
                        <li>**Día 2: Aplicaciones de la IA**
                            <ul>
                                <li>10:00h - Taller Práctico: "Machine Learning con Python"</li>
                                <li>12:00h - Presentación de Casos de Éxito: "IA en la Agricultura 4.0"</li>
                            </ul>
                        </li>
                        <li>**Día 3: Futuro y Oportunidades**
                            <ul>
                                <li>09:00h - Mesa Redonda: "El Papel de Andalucía en el Ecosistema Global de IA"</li>
                                <li>17:00h - Clausura y Networking</li>
                            </ul>
                        </li>
                    </ul>
                </details>
            </section>

            <footer>
                <p>Síguenos en redes sociales para actualizaciones: #AISevilla2025</p>
                <p><small>Artículo actualizado el <time datetime="2025-06-10">10 de Junio de 2025</time>.</small></p>
            </footer>
        </article>
    </main>

    <aside>
        <h3>Noticias Relacionadas</h3>
        <ul>
            <li><a href="#">Andalucía, Referente en Desarrollo Tecnológico</a></li>
            <li><a href="#">Nuevas Ayudas para Startups de IA en Málaga</a></li>
            <li><a href="#">Éxito del Primer Hackathon de Ciberseguridad</a></li>
        </ul>
    </aside>

    <footer>
        <p>&copy; 2025 Andalucía Tech Hub. Todos los derechos reservados.</p>
        <nav>
            <ul>
                <li><a href="#">Política de Privacidad</a></li>
                <li><a href="#">Aviso Legal</a></li>
            </ul>
        </nav>
    </footer>
</body>
</html>
```

**Justificación de los cambios**:

- `<article>`: El evento/noticia es el contenido principal y autosuficiente de la página.

- `<header>` (dentro de article): Para el título y metadatos del artículo.

- `<time>`: Para la fecha de publicación y las fechas/horas del evento. Se usa con datetime para formato máquina y para rangos de fechas.

- `<figure>` y `<figcaption>`: Para asociar una imagen con su leyenda, semánticamente.

- `<section>`: Para dividir el article en subsecciones lógicas (descripción, detalles del evento).

- `<address>`: Para indicar la información de contacto físico de la ubicación del evento.

- `<details>` y `<summary>`: Ideales para contenido que puede ocultarse/mostrar. En este caso, el programa detallado del evento.

- `<footer>` (dentro de article): Para información al pie del artículo, como un hashtag o fecha de actualización.

- `<aside>`: Contenido relacionado pero secundario, como otras noticias o eventos.

- `<footer>` (global): Para el pie de página general del sitio.

## Ejercicio 5

```html
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
        <nav>
            <ul>
                <li><a href="#">Dashboard</a></li>
                <li><a href="#perfil">Mi Perfil</a></li>
                <li><a href="#">Mensajes</a></li>
                <li><a href="#">Cerrar Sesión</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="perfil">
            <header>
                <h1>Mi Perfil de Usuario</h1>
            </header>

            <section>
                <h2>Datos Personales</h2>
                <form action="/update-profile" method="post">
                    <fieldset>
                        <legend>Información de Contacto</legend>
                        <p>
                            <label for="nombre">Nombre:</label>
                            <input type="text" id="nombre" name="nombre" value="Ana García" required>
                        </p>
                        <p>
                            <label for="apellidos">Apellidos:</label>
                            <input type="text" id="apellidos" name="apellidos" value="Rodríguez" required>
                        </p>
                        <p>
                            <label for="email">Email:</label>
                            <input type="email" id="email" name="email" value="ana.rodriguez@example.com" required>
                        </p>
                        <p>
                            <label for="telefono">Teléfono:</label>
                            <input type="tel" id="telefono" name="telefono" value="+34 600 123 456">
                        </p>
                    </fieldset>

                    <fieldset>
                        <legend>Dirección de Residencia</legend>
                        <address>
                            <p>Calle del Olivo, 15</p>
                            <p>29001 Málaga, Andalucía</p>
                            <p>España</p>
                        </address>
                        </fieldset>
                    <button type="submit">Guardar Cambios</button>
                </form>
            </section>

            <section>
                <h2>Actividad Reciente</h2>
                <ol>
                    <li>
                        <p>Mensaje enviado a "Soporte Técnico" - <time datetime="2025-06-09T14:30">ayer, 14:30</time></p>
                    </li>
                    <li>
                        <p>Proyecto "Plataforma de E-learning" visitado - <time datetime="2025-06-08T10:15">8 de Junio, 10:15</time></p>
                    </li>
                    <li>
                        <p>Comentario publicado en "Noticia de Evento AI" - <time datetime="2025-06-07T18:00">7 de Junio, 18:00</time></p>
                    </li>
                    <li>
                        <p>Actualización de preferencias de privacidad - <time datetime="2025-06-05T09:00">5 de Junio, 09:00</time></p>
                    </li>
                </ol>
            </section>

            <section>
                <h2>Preferencias de la Cuenta</h2>
                <form action="/update-preferences" method="post">
                    <fieldset>
                        <legend>Configuración de Notificaciones</legend>
                        <p>
                            <input type="checkbox" id="notif-email" name="notif-email" checked>
                            <label for="notif-email">Recibir notificaciones por email</label>
                        </p>
                        <p>
                            <input type="checkbox" id="notif-sms" name="notif-sms">
                            <label for="notif-sms">Recibir notificaciones por SMS</label>
                        </p>
                    </fieldset>

                    <fieldset>
                        <legend>Opciones Generales</legend>
                        <p>
                            <label for="idioma">Idioma Preferido:</label>
                            <select id="idioma" name="idioma">
                                <option value="es" selected>Español</option>
                                <option value="en">English</option>
                                <option value="fr">Français</option>
                            </select>
                        </p>
                        <p>
                            <label for="zona-horaria">Zona Horaria:</label>
                            <select id="zona-horaria" name="zona-horaria">
                                <option value="europe/madrid" selected>Europa/Madrid (CEST)</option>
                                <option value="europe/london">Europa/Londres (GMT)</option>
                                </select>
                        </p>
                    </fieldset>
                    <button type="submit">Actualizar Preferencias</button>
                </form>
            </section>
        </section>
    </main>

    <aside>
        <h3>Acciones Rápidas del Perfil</h3>
        <ul>
            <li><a href="#">Cambiar Contraseña</a></li>
            <li><a href="#">Gestionar Suscripciones</a></li>
            <li><a href="#">Ver Historial de Pedidos</a></li>
            <li><a href="#">Eliminar Cuenta</a></li>
        </ul>
    </aside>

    <footer>
        <p>&copy; 2025 Mi Plataforma Andalucía. Todos los derechos reservados.</p>
        <nav>
            <ul>
                <li><a href="#">Términos de Servicio</a></li>
            </ul>
        </nav>
    </footer>
</body>
</html>
```

**Justificación de los cambios**:

- `<header>` y `<nav>` (globales): Estructura general de la página.

- `<main>`: Contiene todo el contenido principal del perfil.

- `<section id="perfil">`: Una sección principal para encapsular todo el contenido relacionado con el perfil del usuario.

- `<header>` (dentro de section#perfil): Para el título de la página de perfil.

- `<section>` (anidadas): Se utilizan para dividir lógicamente las diferentes categorías de información del perfil (Datos Personales, Actividad Reciente, Preferencias).

- `<form>`: Los datos que se pueden editar deben ir dentro de formularios.

- `<fieldset>` y `<legend>`: Fundamentales para agrupar semánticamente campos relacionados dentro de un formulario y proporcionar un título accesible para ese grupo.

- `<label>` con for y id: Imprescindible para la accesibilidad de los formularios, asociando las etiquetas con sus campos de entrada.

- `<address>`: Aunque la dirección se puede editar en un formulario, si se muestra como texto estático, address es apropiado para indicar que es información de contacto.

- `<ol>` y `<time>`: Para listar la actividad reciente de forma ordenada y dar significado semántico a las fechas de cada evento.

- `<aside>`: Para enlaces de navegación o acciones secundarias relacionadas con el perfil pero que no son parte del flujo principal de edición de datos.

- `<footer>` (global): Para el pie de página del sitio.

## Ejercicio procesamiento de video nativo

- ¿Por qué el canvas tiene un borde pero no contenido al cargar la página?

Respuesta: Porque el elemento `<canvas>` es solo un "contenedor" vacío por defecto. A diferencia de `<img>` o `<video>`, no tiene una fuente (src) de imagen propia. El contenido solo aparece cuando JavaScript ejecuta la primera instrucción de dibujo (drawImage) tras iniciarse la reproducción del vídeo.

- En el bucle de JavaScript, ¿por qué avanzamos de 4 en 4 (i += 4)?

Respuesta: Porque el array de píxeles (ImageData.data) almacena la información en formato RGBA. Cada píxel ocupa 4 posiciones consecutivas en el array: [0] para el Rojo (Red), [1] para el Verde (Green), [2] para el Azul (Blue) y [3] para el canal Alfa/Opacidad. Para pasar al siguiente píxel completo, debemos saltar esas 4 posiciones.

- Si eliminas requestAnimationFrame e intentas usar setInterval, ¿qué sucede con la fluidez?

Respuesta: Se pierde fluidez y eficiencia. requestAnimationFrame sincroniza el dibujo con la tasa de refresco del monitor (normalmente 60Hz) y se detiene si el usuario cambia de pestaña, ahorrando CPU/Batería. setInterval se ejecuta de forma "ciega", lo que puede causar tearing (desgarro de imagen) o saltos si el tiempo de ejecución del script no coincide exactamente con el refresco de la pantalla.

- Si cambiamos la fórmula del gris por gris = verde;, ¿qué efecto visual obtendrías?

Respuesta: Seguirías viendo una imagen en blanco y negro (escala de grises), pero la "luminosidad" de los objetos cambiaría. Los objetos que eran rojos puros en el vídeo original se verían negros (porque no tienen componente verde), mientras que los objetos verdes se verían muy brillantes. Es una forma de extraer el canal verde de la imagen.