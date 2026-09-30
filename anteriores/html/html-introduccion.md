## ¿Qué es HTML y su rol en la Web?

### El Origen
La World Wide Web (WWW) nació de la necesidad de compartir información de manera accesible. A principios de los años 90, Tim Berners-Lee desarrolló HTML (HyperText Markup Language) en el CERN con la idea de crear un lenguaje simple para estructurar documentos y navegar entre ellos usando hipervínculos.

### Definición
HTML no es un lenguaje de programación, sino un lenguaje de marcado de hipertexto. Es la base de la web y su propósito es dar estructura y contenido a los documentos web.

- HTML se encarga de la estructura y el contenido (el "qué es" de la página). En la construcción de una casa: el HTML son los cimientos, las paredes y los ladrillos (la estructura), mientras que el CSS es la pintura, la decoración y la distribución de los muebles (la apariencia visual).
El rol del HTML (El "Qué") El HTML (Lenguaje de Marcado de Hipertexto) se encarga de dar estructura y contenido a la página. 

    - Le dice al navegador qué es cada elemento: "esto es un título", "esto es un párrafo", "esto es una imagen". 

    - No está diseñado para controlar el aspecto visual, sino el significado y el orden de los elementos.

!!! Recurso 
    [Guía de referencia](https://developer.mozilla.org/es/docs/Web/HTML/Reference/Elements) 


## Estructura en HTML
### Estructura básica de un documento
Si escribimos solo HTML, el navegador aplicará sus estilos por defecto (fondo blanco, texto negro, letras de distinto tamaño según su importancia).

``` html
<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi primera página web</title>
    </head>
    <body>
        <h1>Hola mundo</h1>
    </body>
</html>
```

??? info "Atajos disponibles en VSCode"
    
    - `!` 
    - `HTML:5`

En este código puro, cada etiqueta cumple una función específica e indispensable para la estructura del documento:

`<!DOCTYPE html>:` Es lo primero que debes escribir. Sirve para indicar y declarar al navegador que el documento está escrito siguiendo el estándar de HTML5.

`<html>` y `</html>:` Es la etiqueta inicial y final que envuelve absolutamente todo el documento. Es fundamental no olvidar cerrarla al final.

`<head>:` Es la "parte privada" del documento. No se muestra directamente en la página, sino que sirve como un espacio de comunicación entre el sitio web y el navegador. En su interior encontramos:

- `<meta>:` Añade información sobre la página, como la codificación en la que está escrita (charset="UTF-8") para que reconozca tildes y caracteres especiales.
- `<title>:` Define el título de la página, que es el texto que el usuario visualizará en la pestaña de su navegador.

`<body>:` Encierra el contenido visible o propiamente dicho del sitio. Todo lo que pongas aquí (como la etiqueta de encabezado principal `<h1>` con el texto "Hola mundo") es lo que el usuario verá renderizado en la pantalla.


### Elementos en HTML
Es fundamental entender la estructura de objetos html.

#### Etiquetas de Apertura y Cierre

La mayoría de los elementos funcionan como contenedores:

- Etiqueta de apertura: `<etiqueta>` (Indica dónde empieza el efecto o el contenido).

- Contenido: El texto o los elementos que van dentro.

- Etiqueta de cierre: `</etiqueta>` (Lleva una barra inclinada / y es obligatoria para evitar errores de renderizado).

Excepción importante: Etiquetas ***"Self-closing"***
No todas las etiquetas se cierran. Algunas son "huérfanas" porque no contienen texto, sino que insertan algo. Ejemplos: `<img>` (imagen), `<br>` (salto de línea) o `<input>` (campo de formulario).

#### Atributos: Los "Adjetivos" de las Etiquetas

Los atributos proporcionan información adicional sobre el elemento. Siempre se escriben en la etiqueta de apertura.

Estructura de un atributo:

- **nombre="valor"**
- **id:** Un identificador único para ese elemento (como un DNI).
- **class:** Una categoría para aplicar estilos (pueden compartirla varios elementos).
- **src:** La fuente o ruta (usado en imágenes).
- **href:** El destino de un enlace (usado en la etiqueta `<a>`).

#### El concepto de "Anidamiento" (Nesting)
HTML es jerárquico. Las etiquetas se comportan como cajas dentro de otras cajas. La regla de oro: "Lo que se abre de último, se cierra de primero".

Ejemplo correcto:
```html
<p>Este es un texto <strong>en negrita</strong></p>
```

Ejemplo incorrecto (error común):
```html
<p>Este es un texto <strong>en negrita</p></strong>
```

### Etiquetas básicas
#### Etiquetas de Estructura Básica y Organización

Estas son el "esqueleto" de cualquier documento.

- `<div>`: Contenedor genérico de bloque. Es la "caja" básica para agrupar elementos.

- `<span>`: Contenedor genérico en línea. Se usa para aplicar estilos a fragmentos de texto dentro de un párrafo.

- `<h1>` a `<h6>`: Encabezados. Es vital explicar que no se usan por su tamaño, sino por su jerarquía e importancia para el SEO.

- `<p>`: Párrafos de texto.

- `<ul>` y `<ol>`: Listas no ordenadas (puntos) y ordenadas (números). Siempre acompañadas de `<li>` (elementos de la lista).


#### Etiquetas de Contenido y Multimedia
Son las que aportan riqueza visual y conectividad:

- `<a>`: Enlaces. Imprescindible controlar el atributo href y target="_blank".

- `<img>`: Imágenes. Necesario src y, sobre todo, alt por accesibilidad.

- `<table>`: Tablas. Aunque hoy no se usan para maquetar, siguen siendo necesarias para datos. Necesarios `<tr>` (fila) y `<td>` (celda).

#### Etiquetas de Formulario
Fundamentales para la interacción con el usuario:

- `<form>`: El contenedor del formulario.

- `<label>`: La etiqueta de texto para cada campo (siempre asociada a un input).

- `<input>`: El campo de entrada. Es clave que conozcan los tipos de HTML5: text, password, email, number, date.

- `<textarea>`: Para textos largos.

- `<select>` y `<option>`: Listas desplegables.

- `<button>`: Botón de envío o acción.

#### Etiquetas Semánticas de HTML5
Esta es la parte más importante para el desarrollo moderno. HTML5 introdujo etiquetas que le dicen al navegador y a Google qué es cada parte, no solo cómo se ve. Estas son las que deben controlar para maquetar una web actual:

- `<header>`: Cabecera de la página o de una sección.

- `<nav>`: Contenedor de los enlaces de navegación (menús).

- `<main>`: El contenido principal y único de la página.

- `<section>`: Agrupa contenido temático relacionado.

- `<article>`: Contenido independiente y autónomo (como un post de un blog o una noticia).

- `<aside>`: Contenido tangencial o relacionado (barras laterales, publicidad).

- `<footer>`: Pie de página con información de contacto, redes o copyright.

!!! Recursos 
    [Ejemplos HTML semántico](https://es.semrush.com/blog/html-semantico/)
    
    [Elementos HTML semántico explicados](https://www.freecodecamp.org/espanol/news/elementos-semanticos-html5-explicados/)


#### Nuevas Etiquetas Multimedia en HTML5
Antes se necesitaba Flash; ahora es nativo:

- `<video>`: Para insertar vídeos con el atributo controls.

- `<audio>`: Para música o podcasts.

- `<canvas>`: Para gráficos y dibujos dinámicos mediante JavaScript.

#### Ejemplo de código
``` html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estructura de Mi Web</title>
</head>
<body>

    <header>
        <h1>Mi Portal de Desarrollo</h1>
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
            <h2>Bienvenida</h2>
            <p>Hola, este es un ejemplo de cómo organizar etiquetas de <strong>bloque</strong> y de <strong>línea</strong>.</p>
        </section>

        <section id="proyectos">
            <h2>Mis Proyectos</h2>
            
            <article>
                <h3>Proyecto 1: El Bazar Digital</h3>
                <p>Una tienda online creada con <span>Angular</span> y TypeScript.</p>
                <div class="tags">
                    <span>#Web</span> | <span>#Frontend</span>
                </div>
            </article>

            <article>
                <h3>Proyecto 2: Registro Espacial</h3>
                <p>Formulario reactivo para nuevos astronautas.</p>
            </article>
        </section>

        <aside>
            <h4>Enlaces de interés</h4>
            <p>Consulta la documentación oficial en MDN.</p>
        </aside>
    </main>

    <footer>
        <p>&copy; 2026 - Creado por un futuro Desarrollador</p>
    </footer>

</body>
</html>
```
### Etiquetas básicas

CSS (Hojas de Estilo en Cascada) se encarga de la apariencia, el diseño visual y el estilo (el "cómo se ve")
.
Buena práctica: Menciónales que, idealmente, siempre deben mantener el contenido (HTML) separado del estilo (CSS) en archivos distintos
.