## Multimedia en HTML5

Antes de HTML5, dependíamos de plugins externos (como el difunto Adobe Flash). Ahora, el navegador gestiona el contenido multimedia de forma nativa, lo que mejora el rendimiento, la seguridad y el SEO.

### Accesibilidad: El atributo `alt`

No es una etiqueta multimedia en sí, pero es el pilar de la accesibilidad para imágenes (`<img>`) y elementos de mapa.

- **Propósito**: Ofrecer una descripción textual si la imagen no carga o para que los lectores de pantalla la narren a personas con discapacidad visual.

- **Buenas prácticas**:

    - **Descriptivo**: `alt="Logotipo de la Junta de Andalucía"` en lugar de `alt="logo"`.

    - **Imágenes decorativas**: Si la imagen no aporta información, usa `alt=""` (vacío) para que el lector de pantalla la ignore.

    - **Evitar redundancias**: No empieces con "Imagen de..." o "Foto de...".

### El elemento `<video>`
Permite reproducir clips de vídeo sin necesidad de reproductores externos.

| **Atributo** | **Descripción** |
| :--- | :--- |
| `src`	| Ruta del archivo de vídeo. |
| `controls`	| Muestra la barra de reproducción (play, volumen, etc.). |
| `autoplay`	| Inicia el vídeo automáticamente (Nota: la mayoría de navegadores exigen que esté muted). |
| `loop`	| Reinicia el vídeo al finalizar. |
| `muted`	| Silencia el audio por defecto. |
| `poster`	| URL de una imagen que se muestra mientras el vídeo carga o hasta que se pulsa play. |
| `preload`	| Sugiere al navegador cuánto cargar (none, metadata, auto). |
| `width / height`	| Dimensiones en píxeles. |

**Ejemplo de código**

```html
<video controls poster="miniatura.jpg" width="640">
  <source src="video-promocional.mp4" type="video/mp4">
  <source src="video-promocional.webm" type="video/webm">
  Tu navegador no soporta el formato de vídeo.
</video>
```

### El elemento `<audio>`

Al igual que el vídeo, el elemento `<audio>` permite reproducir archivos de sonido de forma nativa. Es ideal para podcasts, música de fondo o efectos sonoros en aplicaciones web.

| **Atributo** | **Descripción** |
| :--- | :--- |
| `src`	| Ruta del archivo de vídeo. |
| `controls`	| Imprescindible para que el usuario vea el reproductor (play, volumen, tiempo). |
| `autoplay`	| Inicia el audio automáticamente al cargar (usar con precaución por la UX). |
| `loop`	| Hace que el audio se repita infinitamente. |
| `muted`	| El audio comienza silenciado por defecto. |
| `preload`	| Sugiere al navegador cuánto cargar (none, metadata, auto). |


**Ejemplo de código**

```html
<audio controls>
  <source src="audio/podcast-clase.mp3" type="audio/mpeg">
  <source src="audio/podcast-clase.ogg" type="audio/ogg">
  
  Tu navegador no soporta el elemento de audio.
</audio>
```

### El Elemento `<canvas>`

A diferencia de las imágenes o vídeos, el `<canvas>` es un lienzo en blanco. No contiene nada por sí mismo; es un contenedor de gráficos que se dibujan en tiempo real mediante **JavaScript**.

**Conceptos Clave**
- **Mapa de bits**: A diferencia de SVG (que es vectorial), Canvas trabaja con píxeles. Si lo escalas mucho mediante CSS, se pixelará.

- **Contexto**: Para dibujar, necesitamos definir un "contexto" en JavaScript (normalmente '2d').

- **Atributos de dimensión**: Es fundamental definir width y height directamente en la etiqueta HTML. Si se hace por CSS, el navegador "estirará" el dibujo original, deformándolo.

**Sistema de Coordenadas**
En el lienzo de Canvas, el punto (0,0) se encuentra en la **esquina superior izquierda**. El eje X aumenta hacia la derecha y el eje Y aumenta hacia abajo.

**Ejemplo de implementación básica**

=== "HTML"

    ```html
    <canvas id="lienzoInterfaces" width="400" height="200" style="border: 2px solid #333;">
        Contenido de respaldo: Tu navegador no es compatible con Canvas.
    </canvas>
    ```

=== "JavaScript"

    ```javascript
    // 1. Seleccionamos el elemento
    const canvas = document.getElementById('lienzoInterfaces');

    // 2. Obtenemos el contexto de dibujo
    const ctx = canvas.getContext('2d');

    // 3. Dibujamos: Un rectángulo azul
    ctx.fillStyle = "blue";
    ctx.fillRect(50, 50, 150, 100); // (x, y, ancho, alto)

    // 4. Dibujamos: Una línea roja
    ctx.strokeStyle = "red";
    ctx.lineWidth = 5;
    ctx.beginPath();
    ctx.moveTo(0, 0); // Inicio
    ctx.lineTo(400, 200); // Fin
    ctx.stroke();
    ```

## El elemento `<iframe>` (Inline Frame)

1. ¿Qué es un `<iframe>`?
Es una etiqueta que permite incrustar un documento HTML completo dentro de otro documento HTML. Actúa como una "ventana" a otro sitio web o a otra página de tu propio servidor.

2. Atributos Esenciales

| **Atributo** | **Descripción** |
| :--- | :--- |
| `src`	| Dirección de la página a incrustar. |
| `title`	| **Obligatorio** para accesibilidad (ej. "Mapa de ubicación"). |
| `sandbox`	| Aumenta la seguridad restringiendo acciones del contenido incrustado. |
| `loading="lazy"`	| Optimiza la carga de la página. |

```html
<iframe 
  src="https://www.google.com/maps/embed?..." 
  title="Mapa de la oficina en Sevilla"
  width="400" 
  height="300" 
  loading="lazy">
</iframe>
```



Las tablas han pasado por un largo camino. En los años 90 se usaban para *todo* el diseño (un pecado semántico hoy en día), pero ahora su propósito es único y sagrado: **mostrar datos tabulares**.

Aquí tienes el material completo sobre tablas en HTML, estructurado para tus clases en formato Markdown.

---

## Tablas en HTML: Estructura, Semántica y Datos

### 1. Introducción

Las tablas se utilizan para organizar datos en filas y columnas. Una tabla bien construida debe ser fácil de leer tanto para humanos como para máquinas (lectores de pantalla y buscadores).

> **Regla de oro:** ¡No uses tablas para maquetar el diseño de tu web! Para eso existen Flexbox y CSS Grid.

---

### 2. Estructura Básica

Toda tabla se compone de cuatro etiquetas fundamentales:

* **`<table>`**: El contenedor principal.
* **`<tr>`** (Table Row): Define una fila.
* **`<th>`** (Table Header): Define una celda de encabezado (por defecto es negrita y centrada).
* **`<td>`** (Table Data): Define una celda de datos estándar.

#### Ejemplo simple:

```html
<table>
  <tr>
    <th>Producto</th>
    <th>Precio</th>
  </tr>
  <tr>
    <td>Aceite de Oliva</td>
    <td>9,50€</td>
  </tr>
</table>

```

---

### 3. Estructura Semántica Avanzada

Para tablas complejas o extensas, HTML5 nos da etiquetas para dividir la tabla en secciones lógicas. Esto ayuda a los navegadores a manejar el scroll y a las impresoras a repetir los encabezados en cada página.

* **`<caption>`**: El título de la tabla. Debe ser la primera etiqueta dentro de `<table>`.
* **`<thead>`**: Agrupa el contenido del encabezado.
* **`<tbody>`**: Agrupa el cuerpo de los datos.
* **`<tfoot>`**: Agrupa el pie de la tabla (útil para sumas totales).

```html
<table>
  <caption>Ventas Mensuales - Almería</caption>
  <thead>
    <tr>
      <th>Mes</th>
      <th>Ventas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Enero</td>
      <td>12.000€</td>
    </tr>
    <tr>
      <td>Febrero</td>
      <td>15.400€</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Total</td>
      <td>27.400€</td>
    </tr>
  </tfoot>
</table>

```

---

### 4. Combinación de Celdas (Spanning)

A veces una celda debe ocupar el espacio de varias columnas o filas. Para esto usamos:

* **`colspan`**: Expande una celda horizontalmente (columnas).
* **`rowspan`**: Expande una celda verticalmente (filas).

#### Ejemplo de combinación:

```html
<tr>
  <td rowspan="2">Servicios</td>
  <td>Diseño Web</td>
</tr>
<tr>
  <td>Mantenimiento</td>
</tr>
<tr>
  <td colspan="2">Nota: Precios sin IVA</td>
</tr>

```

---

### 5. Gestión de Columnas (`<colgroup>`)

Si quieres aplicar estilos (como el ancho o el color de fondo) a una columna entera sin tener que repetir el CSS en cada celda, usamos el grupo de columnas.

```html
<table>
  <colgroup>
    <col style="background-color: #e0e0e0; width: 100px;">
    <col style="background-color: #ffffff; width: 200px;">
  </colgroup>
  <tr>
    <td>ID</td>
    <td>Nombre del Alumno</td>
  </tr>
</table>

```

---

### 6. Accesibilidad en Tablas

Para que un lector de pantalla explique correctamente la relación entre los encabezados y los datos, usamos el atributo **`scope`**.

* `scope="col"`: Indica que el `<th>` es el encabezado de la columna.
* `scope="row"`: Indica que el `<th>` es el encabezado de la fila.

#### Ejemplo accesible:

```html
<tr>
  <th scope="col">Nombre</th>
  <th scope="col">Especialidad</th>
</tr>
<tr>
  <th scope="row">Juan Pérez</th>
  <td>Desarrollo de Interfaces</td>
</tr>

```

---

### 7. Resumen de Opciones y Atributos

| Etiqueta/Atributo | Función |
| --- | --- |
| **`<caption>`** | Título descriptivo de la tabla. |
| **`<thead>`** | Contenedor de los encabezados. |
| **`<tfoot>`** | Resumen o notas finales de la tabla. |
| **`colspan`** | Une celdas hacia la derecha. |
| **`rowspan`** | Une celdas hacia abajo. |
| **`scope`** | Define la dirección del encabezado (accesibilidad). |

---


## La Etiqueta `<input>` en HTML

### 1. Introducción

El elemento `<input>` se usa para crear controles interactivos en formularios web con el fin de recibir datos del usuario. Es un elemento **vacío** (void element), lo que significa que no tiene etiqueta de cierre.

**Regla de Oro:** Todo `input` debe ir asociado a un `<label>` mediante el atributo `id` para garantizar la accesibilidad.

---

### 2. Atributos comunes

Antes de ver los tipos, estos son los atributos que verás casi siempre:

* **`name`**: El nombre del dato que se enviará al servidor.
* **`value`**: El valor inicial o actual del campo.
* **`placeholder`**: Texto de ayuda que desaparece al escribir.
* **`required`**: Obliga al usuario a rellenar el campo.
* **`disabled`**: Desactiva el control.
* **`readonly`**: El usuario no puede editar el valor, pero se envía al servidor.

---

### 3. Tipos de Input (Atributo `type`)

#### a. Entradas de texto y datos simples

Ideales para capturar información alfanumérica.

```html
<label for="nombre">Nombre:</label>
<input type="text" id="nombre" name="nombre" placeholder="Tu nombre">

<label for="pass">Contraseña:</label>
<input type="password" id="pass" name="password">

<label for="correo">Email:</label>
<input type="email" id="correo" name="email">

<label for="web">Web Personal:</label>
<input type="url" id="web" name="url">

<label for="tel">Teléfono:</label>
<input type="tel" id="tel" name="telefono">

<label for="buscar">Buscar:</label>
<input type="search" id="buscar" name="q">

```

#### b. Selección y Opciones

Para cuando el usuario debe elegir entre opciones predefinidas.

```html
<input type="checkbox" id="acepto" name="terminos">
<label for="acepto">Acepto los términos</label>

<p>Provincia:</p>
<input type="radio" id="sevilla" name="provincia" value="sevilla">
<label for="sevilla">Sevilla</label>
<input type="radio" id="malaga" name="provincia" value="malaga">
<label for="malaga">Málaga</label>

<label for="color">Color corporativo:</label>
<input type="color" id="color" name="color_fav" value="#007f5f">

```

#### c. Números y Rangos

Controles específicos para datos cuantitativos.

```html
<label for="edad">Edad:</label>
<input type="number" id="edad" name="edad" min="18" max="99">

<label for="volumen">Volumen:</label>
<input type="range" id="volumen" name="vol" min="0" max="100" step="10">

```

#### c. Fechas y Horas

Nativos del navegador, evitan el uso de librerías pesadas de calendario.

```html
<label for="fecha">Fecha de inicio:</label>
<input type="date" id="fecha" name="fecha_inicio">

<label for="cita">Cita médica:</label>
<input type="datetime-local" id="cita" name="cita_previa">

<label for="caducidad">Caducidad tarjeta:</label>
<input type="month" id="caducidad" name="mes_cad">

<label for="entrega">Semana de entrega:</label>
<input type="week" id="entrega" name="semana">

<label for="alarma">Hora:</label>
<input type="time" id="alarma" name="hora_alarma">

```

#### Ee. Botones y Acciones

Elementos que ejecutan acciones dentro del formulario.

```html
<input type="submit" value="Registrar usuario">

<input type="reset" value="Empezar de nuevo">

<input type="button" value="Haz clic aquí" onclick="alert('¡Hola!')">

<input type="image" src="btn-enviar.png" alt="Enviar" width="48" height="48">

```

#### f. Casos Especiales

```html
<label for="cv">Sube tu CV (PDF):</label>
<input type="file" id="cv" name="archivo" accept=".pdf">

<input type="hidden" name="user_id" value="12345">

```

---

### 4. Comparativa de Inputs de Selección

| Tipo | Selección | Caso de uso |
| --- | --- | --- |
| **`checkbox`** | Múltiple | "Intereses", "Aceptar condiciones". |
| **`radio`** | Única | "Género", "Método de pago". |
| **`range`** | Única (numérica) | "Nivel de satisfacción", "Presupuesto aproximado". |

---

### 5. Nota sobre Accesibilidad

Es vital recalcar que el atributo `placeholder` **no sustituye** al `<label>`. Un formulario sin labels es una pesadilla para los usuarios con lectores de pantalla y confunde a los usuarios generales cuando el campo ya está relleno.

---


¡Entendido! Vamos con la etiqueta `<a>`, la "A" de **Anchor** (Ancla), que es literalmente el pegamento que une toda la World Wide Web. Sin ella, no habría hipertexto.

Aquí tienes el material listo en Markdown, estructurado para que tus alumnos entiendan desde el enlace más simple hasta los protocolos de seguridad modernos.

---

## La Etiqueta `<a>`

### 1. Introducción

La etiqueta `<a>` define un hipervínculo que se utiliza para conectar una página con otra, ya sea en el mismo sitio web o en uno externo. Es un elemento de **línea** (inline) por defecto.

---

### 2. El Atributo Fundamental: `href`

El atributo `href` (Hypertext Reference) indica el destino del enlace. Sin él, la etiqueta no funciona como un vínculo.

#### Tipos de rutas en `href`:

* **Rutas Absolutas:** Enlazan a una URL completa en internet.
    * `href="https://www.google.com"`


* **Rutas Relativas:** Enlazan a un archivo dentro de tu propio proyecto.
    * `href="contacto.html"` (misma carpeta).
    * `href="img/foto.jpg"` (dentro de una subcarpeta).



---

### 3. Destinos Especiales

La etiqueta `<a>` no solo sirve para ir a otras webs; puede disparar acciones del sistema operativo:

* **Anclas Internas:** Salta a un punto específico de la *misma* página usando un `id`.
```html
<a href="#seccion-contacto">Ir al formulario de contacto</a>

```


* **Correo Electrónico:** Abre el gestor de correo del usuario.
```html
<a href="mailto:info@andaluciatech.com">Envíanos un email</a>

```


* **Llamadas Telefónicas:** Útil para dispositivos móviles.
```html
<a href="tel:+34600112233">Llamar ahora</a>

```



---

### 4. El Atributo `target`

Define **dónde** se abrirá el enlace.

| Valor | Resultado |
| --- | --- |
| **`_self`** | (Por defecto) Abre el enlace en la misma pestaña. |
| **`_blank`** | Abre el enlace en una **pestaña o ventana nueva**. |
| **`_parent`** | Abre el enlace en el marco padre (usado con `iframes`). |
| **`_top`** | Rompe todos los marcos y abre el enlace en la ventana completa. |

> **Nota de Seguridad:** Al usar `target="_blank"`, es una práctica recomendada añadir `rel="noopener noreferrer"` para evitar que la nueva página pueda acceder a la ventana de origen por motivos de seguridad (phishing).

---

### 5. Otros Atributos Importantes

* **`title`:** Muestra un pequeño cuadro de texto (tooltip) al pasar el ratón. Ayuda a la experiencia de usuario.
* **`download`:** En lugar de navegar al archivo, fuerza al navegador a **descargarlo**. Puedes especificar un nombre opcional para el archivo descargado.
```html
<a href="manual.pdf" download="Guia_Estudiante_Interfaces">Descargar Guía</a>

```


* **`rel` (Relationship):** Indica la relación entre la página actual y la de destino.
* `rel="nofollow"`: Dice a Google que no pase "autoridad" a ese enlace (muy usado en blogs para evitar spam).



---

### 6. Buenas Prácticas de Accesibilidad y SEO

1. **Texto de enlace descriptivo:** Evita el típico "Haz clic aquí". Es mejor usar "Descargar el catálogo de interfaces en PDF". Los lectores de pantalla y Google te lo agradecerán.
2. **Identificadores visuales:** Si un enlace abre una ventana nueva o descarga un archivo, es buena idea avisar al usuario con un icono o texto.
3. **Botones vs Enlaces:** Si la acción cambia la URL, usa `<a>`. Si la acción guarda un formulario o cambia algo internamente sin navegar, usa `<button>`.

---

### 7. Tabla de Resumen Técnica

| Opción | Ejemplo de código | Uso principal |
| --- | --- | --- |
| **Web Externa** | `<a href="https://...">` | Navegar a otro dominio. |
| **Ancla** | `<a href="#top">` | Navegación interna (ir arriba). |
| **Nueva Pestaña** | `<a target="_blank">` | Evitar que el usuario abandone tu web. |
| **Descarga** | `<a download>` | Bajar archivos (PDF, ZIP, etc). |

---
