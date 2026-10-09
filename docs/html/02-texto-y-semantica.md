---
icon: lucide/type
title: "HTML 02 - Texto y semántica de contenido"
description: "Jerarquía de encabezados h1-h6, párrafos y separadores, listas (ul, ol, dl), elementos en línea semánticos (strong, em, mark, del/ins, abbr, time…), agrupaciones de texto y esquema de una página."
modulo: "LMH (0373) / DIW (0615) / DI (0488)"
unidad: 1
fecha: "2026-09-29"
---

# HTML 02 — Texto y semántica de contenido

Una página "bonita" con texto plano sigue sin significado. Aquí trabajamos los elementos que dan **jerarquía** al contenido (encabezados), lo estructuran en bloques (párrafos y listas) y marcan **la función** de cada fragmento de texto (énfasis, fechas, citas, código). La anatomía del documento se vio en el [capítulo 01](01-introduccion-html5.md).

!!! note "Conocimientos previos"

    - Montar el documento básico: `head`, `body`, `lang` y `charset` ([capítulo 01](01-introduccion-html5.md)).
    - Diferenciar elementos de bloque de elementos de línea.
    - Probar ejemplos en VS Code con la extensión `.html`.

## 1. Jerarquía de encabezados `h1`-`h6`

### 1.1 Orden, no tamaño

Los encabezados no se eligen por el tamaño que quieras dar, sino por su **posición en la jerarquía**. Dos reglas: **un solo `<h1>` por página** (el tema principal) y ==sin saltos de nivel== (`h1` → `h2` → `h3`, nunca `h2` → `h4`).

```html title="encabezados.html" hl_lines="2 4"
<!-- CORRECTO: un h1 y niveles encadenados -->
<h1>Horario de 1.º DAW · 2.º trimestre</h1> <!-- (1)! -->
<h2>Lunes</h2>
<h3>Mañana</h3>
<p>Programación, de 8:00 a 10:00.</p>

<!-- INCORRECTO: dos h1 y salto de h2 a h4 -->
<h1>Horario</h1>
<h1>Lunes</h1>
<h4>Programación</h4> <!-- (2)! -->
```

1.  Un único `<h1>` y niveles encadenados: ese es el esquema que leerá una máquina.
2.  Aquí hay dos `<h1>` y se salta de `h2` a `h4`: el esquema queda roto.

El texto del encabezado debe **resumir** lo que viene después ("Tipos de listas", no "Otra cosa más"). `h5` y `h6` casi nunca se usan en una web real, y el tamaño lo decide CSS, no el nivel.

### 1.2 Por qué importa: lectores de pantalla y SEO

- Los **lectores de pantalla** construyen un índice con los encabezados y permiten saltar de un bloque a otro sin leerlo todo: un esquema roto hace la página inutilizable.
- Los **buscadores** usan los niveles para entender la estructura y el peso de cada sección.
- En clase de interfaces, la primera revisión de cualquier maquetación es comprobar el esquema de encabezados; se explica en la sección 7.

!!! quote "WCAG 2.1 — Criterio 1.3.1 Información y relaciones (nivel A)"

    «La información, estructura y relaciones comunicadas a través de la presentación pueden ser determinadas por software o están disponibles como texto» (Traducción española oficial de las WCAG por el W3C).

## 2. Párrafos y separadores

### 2.1 El elemento `<p>`

Cada `<p>` es **una idea**. No admite elementos de bloque en su interior (una lista o un `<h2>` dentro de un párrafo es HTML inválido) y, por defecto, el navegador le añade margen superior e inferior (modelo de caja en [../css/03-modelo-de-caja.md](../css/03-modelo-de-caja.md)).

### 2.2 `<br>`: salto de línea literal

Su uso es **raro**: solo cuando el salto forma parte del texto (direcciones, poemas, versos de canciones). **Nunca** para "bajar una línea" o separar párrafos: eso es trabajo de CSS.

### 2.3 `<hr>`: separador temático

Marca un ==cambio de tema== dentro del contenido (fin de una sección, transición a un asunto nuevo). No es un adorno horizontal: si quieres una línea decorativa, va en CSS.

```html title="separadores.html"
<p>La matrícula abre el 1 de junio y cierra el 30 de septiembre.</p>

<!-- br: el salto forma parte del texto -->
<p>Instituto Cervantes<br>Calle Mayor, 12<br>28013 Madrid</p>

<!-- hr: cambio de tema, no decoración -->
<p>Este es el resumen del curso anterior.</p>
<hr>
<h2>Nuevo curso disponible</h2>
```

## 3. Listas

### 3.1 `<ul>` y `<ol>`

`<ul>` cuando el **orden no importa** (menús, características) y `<ol>` cuando **sí importa** (pasos, ranking). Los hijos siempre son ==`<li>`==; meter cualquier otro elemento directo es inválido.

```html title="listas.html"
<!-- ol: atributos start y reversed cambian la numeración -->
<ol start="4" reversed> <!-- (1)! -->
    <li>Revisar el enunciado</li>
    <li>Maquetar con HTML semántico</li>
    <li>Validar en el W3C</li>
</ol>

<!-- ul: orden irrelevante -->
<ul>
    <li>Accesibilidad</li>
    <li>Rendimiento</li>
</ul>
```

1.  `start` fija el primer número y `reversed` lo cuenta hacia atrás: aquí la lista empezaría en 4 y terminaría en 2.

!!! question "Autoevaluación: ¿ul u ol?"

    Quieres listar los pasos para matricularse **en orden obligatorio** y que la numeración arranque en el 4. ¿Qué etiqueta y qué atributo usas?

    ??? success "Respuesta"

        **`<ol start="4">`**: el orden importa, así que lista ordenada; `start` cambia el primer número y `reversed` invierte la cuenta.

### 3.2 Listas anidadas

Una lista dentro de un `<li>` (nunca dentro de la `<ul>` madre). Cada nivel se anida con sangría y puede alternar `ul` y `ol`.

```html title="listas-anidadas.html"
<ul>
    <li>Preparar el entorno
        <ul>
            <li>Instalar VS Code</li>
            <li>Crear la carpeta del proyecto</li>
        </ul>
    </li>
    <li>Publicar la web
        <ol>
            <li>Subir los archivos por FTP</li>
            <li>Comprobar las rutas</li>
        </ol>
    </li>
</ul>
```

### 3.3 `<dl>`, `<dt>` y `<dd>`

Lista de **descripciones**: `<dt>` es el término y `<dd>` su descripción (puede haber varias por término). Ideal para glosarios y fichas de datos.

```html title="glosario.html"
<dl>
    <dt>HTML</dt>
    <dd>Estructura y contenido de la página.</dd>
    <dt>CSS</dt>
    <dd>Presentación visual.</dd>
    <dt>JavaScript</dt>
    <dd>Comportamiento e interacción.</dd>
</dl>
```

### 3.4 Listas de enlaces

Los menús son listas de enlaces: `<nav>` + `<ul>` + `<li>` + `<a>`, tal como se detalla en [03-enlaces-y-recursos.md](03-enlaces-y-recursos.md). Si los datos tienen dos ejes (filas y columnas), no es una lista sino una tabla: van en [05-tablas.md](05-tablas.md).

## 4. Texto en línea semántico

### 4.1 `strong` y `em`: significado, no apariencia

==`<strong>`== marca **importancia** (advertencias, avisos críticos) y `<em>` marca **énfasis** (la palabra que se pronunciaría con fuerza). Ambos son **semánticos**: el navegador los pinta en negrita y cursiva, pero su valor real está en que lector de pantalla y buscadores lo interpretan como "esto importa". ==La negrita visual se consigue con CSS==, no eligiendo etiquetas.

### 4.2 Explicación detallada de los elementos en línea semánticos

Para un alumno principiante, la regla de oro es: **nunca elijas una etiqueta HTML por cómo se ve en pantalla**, sino por **qué significa su contenido**. La apariencia visual siempre es responsabilidad de CSS.

A continuación se detalla la función real de cada etiqueta semántica en línea:

#### 1. `<time>` y el atributo `datetime`: Fechas legibles por máquinas
Un humano comprende expresiones como *"ayer"*, *"el próximo viernes"* o *"12/04/2026"*. Sin embargo, un motor de búsqueda, un calendario o un lector de pantalla se confunden (por ejemplo, ¿`12/04` es el 12 de abril o el 4 de diciembre?).

- El texto entre las etiquetas es lo que lee el usuario humano: `<time datetime="2026-10-15">15 de octubre</time>`.
- El atributo obligatorio `datetime` proporciona la fecha exacta en formato estándar internacional **ISO 8601**:
    - Solo fecha: `datetime="2026-10-15"` (`AAAA-MM-DD`).
    - Fecha y hora: `datetime="2026-10-15T09:30"` (`AAAA-MM-DDTHH:MM`).
    - Solo año: `datetime="2026"`.
- **Beneficio real:** Permite que los móviles sugieran automáticamente "Añadir a Google Calendar" al tocar la fecha y que Google muestre la fecha exacta en los resultados de búsqueda.

#### 2. `<abbr>`: Abreviaturas y siglas accesibles
Identifica una sigla o acrónimo y proporciona su significado expandido mediante el atributo `title`:
```html
<p>El ciclo de <abbr title="Desarrollo de Aplicaciones Web">DAW</abbr> tiene alta empleabilidad.</p>
```

- **Comportamiento:** En navegadores visuales suele mostrar un suave subrayado punteado y un recuadro de ayuda (*tooltip*) al pasar el cursor del ratón.
- **Accesibilidad:** Los lectores de pantalla anuncian la expansión completa a personas que no conocen la terminología técnica.

#### 3. `<del>` e `<ins>`: Historial de cambios y precios de oferta
Representan ediciones en un documento legal o en una tienda online:

- `<del>`: Texto **eliminado o tachado** que ya no está vigente (*deleted*).
- `<ins>`: Texto **insertado o añadido** que lo sustituye (*inserted*).
```html
<p>Precio de matrícula: <del>150 €</del> <ins>95 €</ins> (oferta de lanzamiento).</p>
```
Semánticamente indican a los motores de indexación que hubo una modificación editorial, y los lectores de pantalla leen expresamente *"Eliminado: 150 euros. Insertado: 95 euros"*.

#### 4. `<mark>`: Texto resaltado contextualmente
Representa un fragmento de texto marcado o resaltado por su **relevancia contextual en ese momento**, exactamente igual que un rotulador fluorescente amarillo.

- **Caso de uso típico:** Cuando un usuario busca una palabra en una web y el buscador devuelve la lista de resultados resaltando en amarillo el término coincidente.
- **Diferencia con `<strong>`:** `<strong>` marca algo que es intrínsecamente importante por sí mismo (como una advertencia de peligro); `<mark>` solo señala que es relevante para la acción actual del usuario.

#### 5. `<sub>` y `<sup>`: Subíndices y superíndices
- `<sub>` (*Subscript*): Texto desplazado hacia abajo en tamaño reducido. Indispensable para fórmulas químicas: `H<sub>2</sub>O`.
- `<sup>` (*Superscript*): Texto desplazado hacia arriba. Se utiliza para potencias matemáticas (`x<sup>2</sup>`), notas al pie (`documento<sup>[1]</sup>`) o abreviaturas ordinales (`1.<sup>er</sup> curso`).

#### 6. `<dfn>`: Definición de términos
Envuelve el **término exacto que se está definiendo por primera vez** en un texto técnico:
```html
<p>Un <dfn>algoritmo</dfn> es un conjunto ordenado y finito de instrucciones para resolver un problema.</p>
```
Los navegadores y robots de indexación asocian la definición de todo el párrafo directamente al término envuelto en `<dfn>`.

#### 7. Citas: `<q>` vs `<blockquote>` vs `<cite>` (El gran dilema de examen)
HTML distingue con precisión matemática entre la cita y su autoría:

- `<q>`: Para citas cortas integradas **en línea dentro de un párrafo**. El navegador añade automáticamente las comillas tipográficas adecuadas según el atributo `lang` del documento (en español usará comillas latinas `« »` o inglesas `" "`). **Nunca debes escribir las comillas a mano si usas `<q>`**, o saldrán duplicadas.
- `<blockquote>`: Para citas extensas de **bloque** (ocupan su propio espacio separado, con márgenes).
- El atributo `cite="..."`: Es un atributo HTML opcional que se coloca dentro de `<blockquote>` o `<q>`. Contiene la **URL de origen digital de la cita** para las máquinas (es invisible en pantalla).
- La etiqueta `<cite>`: Es un elemento HTML en línea que sirve para nombrar el **título de la obra citada** (un libro, una película, un artículo de investigación) o la autoría humana visible:
```html
<blockquote cite="https://es.wikipedia.org/wiki/Tim_Berners-Lee">
  <p>El poder de la Web está en su universalidad. El acceso para todos, independientemente de la discapacidad, es un aspecto esencial.</p>
</blockquote>
<p>— <cite>Tim Berners-Lee</cite>, creador de la World Wide Web.</p>
```

#### 8. `<small>`: Texto accesorio o descargos legales
No significa simplemente "letra de tamaño pequeño" (eso es CSS `font-size: 0.8rem`). Semánticamente se reserva para la "letra pequeña" legal: avisos de derechos de autor (*copyright*), descargos de responsabilidad o condiciones de privacidad.

---

### 4.3 Código técnico: `code`, `pre`, `kbd`, `samp`, `var`

Cuando escribimos documentación de software, tutoriales o apuntes informáticos, HTML proporciona cinco etiquetas especializadas que los navegadores renderizan por defecto con tipografía monoespaciada:

| Etiqueta | Función conceptual | Ejemplo de uso |
|---|---|---|
| `<code>` | Fragmento de código o sintaxis de programación **en línea** | Para declarar variables en JS usa <code>const</code> o <code>let</code>. |
| `<pre>` | Bloque con **espacios en blanco y saltos de línea preservados** | Bloques de código fuente completos (siempre debe envolver a un `<code>` en su interior). |
| `<kbd>` | Tecla física o atajo de teclado que debe pulsar el usuario | Pulsa <kbd>Ctrl</kbd> + <kbd>C</kbd> para copiar. |
| `<samp>` | Salida o respuesta que devuelve un programa o terminal | El servidor respondió: <samp>200 OK</samp>. |
| `<var>` | Variable matemática o parámetro formal en programación | Si la variable <var>x</var> es mayor que 10... |

```html title="codigo-tecnico.html"
<p>Para formatear el disco duro, escribe el comando <code>format C:</code> en la consola y presiona la tecla <kbd>Enter</kbd>.</p>
<p>Salida esperada en la terminal: <samp>Operación completada con éxito</samp>.</p>
<p>El área de un círculo se calcula como: Área = π × <var>r</var><sup>2</sup>.</p>

<!-- Bloque completo de código: pre preserva tabulaciones y saltos de línea -->
<pre><code>function saludar(nombre) {
    console.log("Hola, " + nombre);
}</code></pre>
```

!!! warning "Error común"

    Usar `<strong>` o `<em>` **solo porque el diseño pide negrita o cursiva**: eso es CSS (`font-weight`, `font-style`). Si no hay importancia o énfasis real, usa un `<span>` con clase y dale estilos en tu archivo CSS.

## 5. Elementos de agrupación de texto

### 5.1 `<address>`

Agrupa los **datos de contacto** del autor, la organización o la sección (no es cualquier texto pequeño): dentro puede haber enlaces y párrafos.

### 5.2 `<figure>` y `<figcaption>`

Figura = contenido autocontenido (imagen, código, gráfico) con su pie ==`<figcaption>`==, que es obligatorio como hermano único dentro de `<figure>`. El ancho de la imagen y sus márgenes se ajustan con el modelo de caja ([../css/03-modelo-de-caja.md](../css/03-modelo-de-caja.md)) y las variantes `srcset`/`picture` se ven en [03-enlaces-y-recursos.md](03-enlaces-y-recursos.md).

### 5.3 `<blockquote>` con `cite`

Cita de bloque; el atributo `cite` guarda la **URL de origen** (no la muestra). Un `<blockquote>` suele llevar un `<p>` dentro.

!!! info "Qué hace `cite`"

    - Guarda la **fuente** como URL **para las máquinas**: los navegadores no muestran ni aplican nada por sí solos.
    - Si quieres que la fuente se vea, añade un enlace dentro del bloque; el atributo no lo sustituye.

```html title="agrupaciones.html"
<address>
    Escuela: IES Ejemplo · <a href="mailto:daw@ies.example.es">daw@ies.example.es</a>
</address>

<figure>
    <img src="https://dummyimage.com/800x600/ccc/000.png&text=entrega-proyectos.jpg" alt="Alumnado entregando los proyectos de fin de curso">
    <figcaption>Entrega de proyectos, junio de 2026.</figcaption> <!-- (1)! -->
</figure>

<blockquote cite="https://developer.mozilla.org/es/docs/Web/HTML"> <!-- (2)! -->
    <p>HTML describe la estructura y el contenido de un documento.</p>
</blockquote>
```

1.  El pie es **hermano único** dentro de `<figure>` y va justo después de lo que describe.
2.  `cite` guarda la URL de origen, pero **no se ve en pantalla**: es metadata, no texto visible.

## 6. Ejemplo práctico: artículo de blog semántico

```html title="articulo.html" hl_lines="4 16"
<article>
    <header>
        <h1>Cómo organizar los apuntes de DAW</h1>
        <p>Por <cite>Ana Ruiz</cite> · <time datetime="2026-09-29">29 de septiembre de 2026</time></p>
    </header>

    <p>Empezar el curso con un buen método ahorra horas de repaso antes del examen.</p>

    <h2>Tres claves</h2>
    <ol>
        <li>Un fichero por tema, con su <strong>encabezado</strong> propio.</li>
        <li>Resaltar con <mark>marcador</mark> lo que se cae seguro.</li>
        <li>Repasar la semana antes de la <time datetime="2026-10-10">prueba del 10 de octubre</time>.</li>
    </ol>

    <blockquote cite="https://www.ies.example.es/blog">
        <p>Repasar es aprender dos veces.</p>
    </blockquote>

    <h3>Plantilla mínima</h3>
    <pre><code>&lt;h1&gt;Tema&lt;/h1&gt;
&lt;p&gt;Ideas principales.&lt;/p&gt;</code></pre>

    <p><small>Publicado con fines educativos; se permite su uso en clase.</small></p>

    <footer>
        <p>Etiquetas: <span>#html</span> <span>#fp</span></p>
    </footer>
</article>
```

Todo vive dentro de un ==`<article>`== autónomo, que se entiende sin el resto de la página. Fíjate en la jerarquía (`h1` → `h2` → `h3`), en que la fecha legible lleva su `datetime` y en que la cita tiene su fuente.

---

### 6.1 Explicación detallada: ¿Por qué se usa cada etiqueta y para qué sirve?

A continuación se analiza en profundidad la justificación semántica y técnica de cada etiqueta y atributo empleado en el artículo de blog `articulo.html`:

#### 1. `<article>` — El contenedor autónomo e independiente
- **¿Para qué sirve?** Representa una unidad de contenido completa, autocontenida y distribuible por sí misma (`role="article"` implícito).
- **¿Por qué se usa aquí en vez de un `<section>` o un `<div>`?**
    - Si este bloque se extrajera de la web y se publicara en un lector de RSS, en un agregador de noticias o se enviara por boletín electrónico (*newsletter*), **sigue teniendo perfecto sentido y comprensión completa** por sí mismo.
    - Un `<section>` solo divide temas genéricos dentro de un documento mayor; `<article>` indica expresamente una publicación independiente (artículo de blog, noticia, ficha de producto, post en un foro).
    - Un `<div>` no transmite ninguna información semántica a los lectores de pantalla ni a los motores de búsqueda.

#### 2. `<header>` — La cabecera del artículo
- **¿Para qué sirve?** Agrupa los elementos introductorios o metadatos de apertura de una sección o artículo.
- **¿Por qué se usa dentro del `<article>`?**
    - A diferencia del `<header>` principal del sitio (que es hijo de `<body>` y actúa como `role="banner"`), un `<header>` dentro de un `<article>` delimita específicamente la **cabecera editorial del post**, agrupando el titular, la firma del autor y la fecha de publicación antes del cuerpo del texto.

#### 3. `<h1>` — Título nuclear del artículo
- **¿Para qué sirve?** Es el titular principal del artículo (*«Cómo organizar los apuntes de DAW»*).
- **¿Por qué se usa aquí?** Proporciona la etiqueta accesible primordial para el hito del artículo. Cuando un usuario de lector de pantalla pulsa la tecla rápida <kbd>H</kbd> para navegar por encabezados, este `<h1>` le comunica de inmediato el tema central de la lectura.

#### 4. `<cite>` — Referencia a la autoría o fuente
- **¿Para qué sirve?** Representa el título o la referencia a la fuente de una obra intelectual (un libro, un ensayo, una investigación o la persona autora de la pieza).
- **¿Por qué se usa en `<cite>Ana Ruiz</cite>`?** Identifica formalmente la autoría del texto. Aunque visualmente el navegador lo renderice en cursiva por defecto, su valor radica en la semántica: permite a algoritmos de indexación identificar a la creadora del contenido.

#### 5. `<time datetime="2026-09-29">` — Tiempo legible por humanos y máquinas
- **¿Para qué sirve?** Traduce una fecha u hora a un formato estándar comprensible tanto para personas como para ordenadores.
- **¿Por qué es imprescindible el atributo `datetime`?**
    - El texto visible para el usuario es *"29 de septiembre de 2026"*, un formato lingüístico agradable pero difícil de procesar por programas informáticos.
    - El atributo `datetime="2026-09-29"` codifica la fecha según la norma internacional **ISO 8601** (`AAAA-MM-DD`).
    - **Beneficios prácticos:** Permite a los navegadores ofrecer la opción de *"Añadir al calendario"* con un clic, a los motores de búsqueda saber con exactitud cuándo se publicó la noticia para ponderar su frescura en los resultados, y a los lectores de pantalla vocalizar la fecha de manera inequívoca.

#### 6. Jerarquía de encabezados: `<h2>` y `<h3>`
- **¿Para qué sirven?** Establecen el árbol de contenidos (*outline*) del documento.
- **¿Por qué se usan secuencialmente?**
    - `<h2>` abre la sección principal de recomendaciones (*«Tres claves»*).
    - `<h3>` se abre para un subapartado específico (*«Plantilla mínima»*) que depende conceptualmente del bloque anterior.
    - **Regla estricta:** Nunca se debe saltar de `<h1>` a `<h3>` directamente por motivos puramente estéticos (por querer una letra más pequeña). El tamaño de fuente es responsabilidad exclusiva de CSS; la jerarquía de etiquetas representa la lógica del contenido.

#### 7. `<ol>` y `<li>` — Lista ordenada con secuencia cronológica o prioritaria
- **¿Para qué sirve `<ol>`?** Define una **lista ordenada** (*ordered list*).
- **¿Por qué no se usa `<ul>` (lista con viñetas)?** Porque las tres claves siguen un orden lógico o enumerativo de pasos. El navegador numera automáticamente cada elemento (`1.`, `2.`, `3.`) y el lector de pantalla anuncia expresamente: *"Elemento de lista 1 de 3"*, permitiendo al estudiante comprender la secuencia y el progreso de la lectura.

#### 8. `<strong>` vs. `<mark>` — Diferenciación semántica de énfasis
- **`<strong>` (en *encabezado*):** Comunica **importancia seria o urgencia** en el contenido. Altera el tono del lector de pantalla para remarcar su gravedad conceptual.
- **`<mark>` (en *marcador*):** Representa un **resaltado de relevancia contextual** (el equivalente digital a pasar un rotulador fluorescente amarillo por encima de un texto en papel).
    - No significa que el autor original considere esa palabra más importante que las demás; significa que es relevante para la atención inmediata del lector o en una búsqueda activa.

#### 9. `<blockquote cite="...">` — Cita en bloque con procedencia
- **¿Para qué sirve `<blockquote>`?** Delimita un bloque de texto citado procedente de una fuente externa o de otro autor.
- **¿Por qué lleva el atributo `cite`?** Contiene la URL completa del documento original (`https://www.ies.example.es/blog`). Aunque este atributo no se muestra visualmente en pantalla por defecto, aporta trazabilidad legal y bibliográfica a nivel de metadatos del DOM. Dentro de la cita, el texto se estructura formalmente mediante etiquetas de párrafo `<p>`.

#### 10. `<pre>` y `<code>` — Fragmentos de código fuente
- **`<pre>` (*Preformatted text*):** Le indica al navegador que respete fielmente todos los espacios en blanco, tabulaciones y saltos de línea literales que contiene, mostrándolos en una tipografía de ancho fijo (*monospace*).
- **`<code>`:** Marca semánticamente que el texto contenido es código de programación o marcado informático.
- **¿Por qué se usan juntos `<pre><code>`?** Porque representan un bloque de código completo multilínea.
- **Escape de entidades:** Para mostrar etiquetas HTML dentro de `<code>` sin que el navegador intente ejecutarlas, los caracteres `<` y `>` se reemplazan obligatoriamente por sus entidades seguras: `&lt;` (*less than*) y `&gt;` (*greater than*).

#### 11. `<small>` — Letra pequeña editorial y legal
- **¿Para qué sirve?** En HTML5, `<small>` no es un simple reductor visual de tamaño tipográfico; representa comentarios secundarios, descargos de responsabilidad legal, copyright o condiciones de licencia (*"Publicado con fines educativos..."*).

#### 12. `<footer>` y `<span>` — Cierre del artículo y etiquetas temáticas
- **`<footer>` dentro del `<article>`:** Cierra el bloque editorial, acogiendo los metadatos de categorización y etiquetas (*tags*) del artículo.
- **`<span>`:** Elemento en línea genérico sin significado semántico propio. Se utiliza aquí para encapsular cada etiqueta temáticas (`#html`, `#fp`), permitiendo posteriormente aplicarles estilos visuales independientes mediante clases CSS (por ejemplo, aspecto de pastilla o *badge*) sin alterar la estructura del párrafo.

---

## 7. Cómo extraer el esquema de una página

El ==esquema== (*outline*) es la lista de encabezados con sus niveles. Para verlo de un vistazo:

1. **Pestaña *Elements*** (`F12`): despliega el árbol y filtra escribiendo `h1`, `h2`… en la barra de búsqueda de nodos.
2. **Validador del W3C** (<https://validator.w3.org/>): avisa de encabezados vacíos y de niveles que se saltan.
3. **Extensiones** como *HeadingsMap* o *W3C Web Validator* dibujan el árbol completo en un panel.

```text title="esquema.txt"
h1 Cómo organizar los apuntes de DAW
├── h2 Tres claves
└── h3 Plantilla mínima
```

!!! success "Comprueba que…"

    - [ ] Un solo `<h1>` y niveles encadenados (`h1` → `h2` → `h3`).
    - [ ] Ningún encabezado vacío ni texto genérico ("Otra cosa más").
    - [ ] El esquema refleja las secciones reales de la página, sin saltos.

Por qué nos importa en Interfaces: con ese esquema revisas en 10 segundos si la maquetación es comprensible, si la navegación por teclado tiene sentido y si el contenido se puede convertir en plantilla reutilizable.

??? note "Para saber más: el algoritmo de esquema retirado"

    HTML5 llegó a proponer un **algoritmo de esquema** que "achataba" las secciones y permitía varios `h1`. El W3C lo retiró de la especificación cuando ningún navegador lo implementó, así que sigue vigente el esquema tradicional: **un `h1` por página** y niveles sin saltos.

!!! warning "Error común"

    - **Divitis**: rodear todo de `<div>` y `<span>` "por si acaso". Si el esquema sale vacío o con los niveles saltados, el problema es de estructura, no de CSS. Practica en el [ejercicio 1 de 09-ejercicios.md](09-ejercicios.md).

## 8. Claves para el examen

!!! tip "Claves para el examen"

    - Encabezados por **jerarquía**, no por tamaño: **un `<h1>` por página** y **sin saltos** de nivel; el tamaño lo pone CSS.
    - `<strong>`/`<em>` son **semánticos** (importancia/énfasis); para negrita o cursiva visual se usa CSS.
    - `<br>` solo para saltos que forman parte del texto; `<hr>` marca cambio de tema, no decora.
    - Listas: `<ul>` sin orden, `<ol>` con orden (`start`, `reversed`), `<dl>` para términos y definiciones; siempre con `<li>` como hijo directo.
    - Fechas con `<time datetime="...">`, citas con `<blockquote cite="...">`, pie de figura con `<figcaption>` e imágenes con `alt`.
    - Errores típicos: `<strong>` usado solo por el aspecto visual y **divitis** (todo de `div`); la segunda se practica en el [ejercicio 1 de 09-ejercicios.md](09-ejercicios.md).
    - Antes de entregar: extrae el esquema de encabezados y comprueba que no hay niveles saltados ni `div` donde falta significado.


!!! success "Practica esta unidad"

    - Enunciados: [Ejercicios de la Unidad 2 — Texto y semántica de contenido](09-ejercicios.md#u41-video-informativo-con-poster-y-formatos) — cuatro retos (`U2.1` a `U2.4`) — del más básico al más avanzado.
    - Comprueba tu trabajo con [las soluciones de esta unidad](10-ejercicios-soluciones.md#sol-u2).

*[HTML]: HyperText Markup Language
*[SEO]: Search Engine Optimization
*[W3C]: World Wide Web Consortium
