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

### 4.2 Cuándo usar cada elemento

| Elemento | Cuándo se usa | Ejemplo |
|---|---|---|
| `strong` | Texto de importancia real | **Alerta**: plazo cerrado |
| `em` | Énfasis en la pronunciación | Esto es *fundamental* |
| `mark` | Resaltar por relevancia (búsqueda, nota) | <mark>Pendiente</mark> |
| `small` | Letra pequeña legal o lateral | <small>Oferta no acumulable</small> |
| `del` | Texto **eliminado** (precio viejo, corrección) | ~~120 €~~ |
| `ins` | Texto **insertado** (nuevo precio) | 99 € |
| `abbr` | Siglas con expansiones | `title="Diseño de Interfaces Web"` |
| `cite` | Título de una obra citada | *El paz en las palabras* |
| `q` | Cita corta **en línea** | «medir antes de cortar» |
| `blockquote` | Cita larga de bloque | ver sección 5 |
| `sub` / `sup` | Índices y notas al pie | H<sub>2</sub>O, 10<sup>2</sup> |
| `time` | Fecha u hora legible + `datetime` | <time datetime="2026-06-15">15 de junio</time> |
| `dfn` | Definición del término que se explica | *selector* |
| `code`/`pre` | Código de ordenador | ver sección 4.3 |

### 4.3 Código técnico: `code`, `pre`, `kbd`, `samp`, `var`

**`<code>`**
: texto de programación **en línea**.

**`<pre>`**
: bloque con **espaciado y saltos preservados** (envolver siempre un `<code>` dentro).

**`<kbd>`**
: tecla o combinación de teclas que teclea la persona usuaria.

**`<samp>`**
: salida de muestra de un programa.

**`<var>`**
: variable matemática o de programación.

```html title="codigo-tecnico.html"
<p>Pulsa <kbd>Ctrl</kbd> + <kbd>S</kbd> para guardar el archivo.</p>
<p>Salida esperada: <samp>Validación superada</samp></p>
<p>Si <var>n</var> es 0, el bucle no se ejecuta.</p>

<pre><code>&lt;nav&gt;
  &lt;ul&gt;
    &lt;li&gt;&lt;a href="index.html"&gt;Inicio&lt;/a&gt;&lt;/li&gt;
  &lt;/ul&gt;
&lt;/nav&gt;</code></pre>
```

También en línea: `<q>` para citas breves, `<abbr>` para siglas, `<time datetime="2026-10-10">` para fechas legibles por la máquina, `<del>`/`<ins>` para correcciones y `<sub>`/`<sup>` para índices.

!!! warning "Error común"

    - Usar `<strong>` o `<em>` **solo porque el diseño pide negrita o cursiva**: eso es CSS (`font-weight`, `font-style`). Si no hay importancia real, usa un `<span>` con clase y estílalo.

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
    <img src="entrega-proyectos.jpg" alt="Alumnado entregando los proyectos de fin de curso">
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
