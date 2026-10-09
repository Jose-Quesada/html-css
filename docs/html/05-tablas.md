---
icon: lucide/table
title: "HTML 05 - Tablas"
description: "Tablas semánticas en HTML: estructura con caption, thead/tbody/tfoot, combinación de celdas con colspan y rowspan, accesibilidad con th y scope y tablas responsivas con scroll horizontal."
modulo: "LMH (0373) / DIW (0615) / DI (0488)"
unidad: 5
fecha: "2026-09-29"
---

# HTML 05 — Tablas de datos

Una tabla es el **único** elemento de HTML pensado para relacionar datos que se cruzan en dos dimensiones: horarios, notas, precios... Aquí vemos su estructura semántica completa, cómo combinar celdas sin romper la cuadrícula y cómo dejarla accesible y usable en móvil.

!!! note "Conocimientos previos"

    - Estructura básica de un documento HTML y etiquetas de contenido.
    - Modelo de caja (`overflow`, `width`) para entender el scroll horizontal (→ [../css/03-modelo-de-caja.md](../css/03-modelo-de-caja.md)).
    - Accesibilidad y WCAG de la clase de interfaces (→ [07-estructura-semantica-y-aria.md](07-estructura-semantica-y-aria.md)).
    - Si hay que recoger datos del usuario, eso es trabajo de [06-formularios-html5.md](06-formularios-html5.md).

## 1. Cuándo SÍ y cuándo NO usar una tabla

### 1.1 Sí: cuando hay dos ejes de datos independientes

Condiciones que deben cumplirse **todas**:

- Hay **filas y columnas** con categoría propia (cada columna, un atributo; cada fila, una entidad).
- Las celdas contienen **datos atómicos** (una nota, un precio), no bloques de texto.
- La lectura **fila → columna** es natural y ninguna celda rompe la cuadrícula.

Casos típicos: horario, acta de notas, precios de productos o comparativa de módulos.

**Test rápido:** *"para cada fila X, el valor del atributo Y"* → tabla. *"Dentro de esta columna hay un menú o tarjetas con imagen"* → no lo es.

### 1.2 No: nunca para maquetar la página

> **Regla de oro:** una tabla **no** es una herramienta de diseño. Maquetar con `<table>` obliga a anidar tablas e inventar `rowspan` absurdos, rompe el responsive y vuelve ilegible el HTML.

!!! failure "Anti-patrón: maquetar con tablas"

    - Cabecera con el logo a la izquierda y el menú a la derecha hecha con una fila de `<td>`.
    - Tarjetas de producto **anidadas** en dos o tres tablas, con celdas vacías de relleno.
    - `rowspan`/`colspan` usados **solo para cuadrar el diseño**: cuando cambie el texto, se rompe.

    Resultado: HTML ilegible, **estilo acoplado al marcado** y una tabla que el lector de pantalla anuncia como datos que no existen.

Para distribuir bloques usa **Flexbox** (una dimensión) → [../css/05-flexbox.md](../css/05-flexbox.md) y **CSS Grid** (dos dimensiones) → [../css/06-grid.md](../css/06-grid.md): menos etiquetas, más accesible y estilo separado en CSS.

| Necesito... | Solución |
|---|---|
| Precios de productos con su IVA o datos que se cruzan fila × columna | ✅ `<table>` |
| Poner el logo a la izquierda y el menú a la derecha | ❌ Flexbox |
| Portada en 3 columnas de tarjetas | ❌ CSS Grid |
| Campos de formulario alineados | ❌ `fieldset` (→ [06-formularios-html5.md](06-formularios-html5.md)) |

## 2. Estructura semántica completa

### 2.1 Elementos que forman una tabla

| Etiqueta | Función |
|---|---|
| `<table>` | Contenedor principal. Solo datos tabulares dentro. |
| `<caption>` | **Título de la tabla**. Siempre el primer hijo de `<table>`. |
| `<thead>` | Agrupa la fila (o filas) de encabezados. |
| `<tbody>` | Agrupa los datos. Puede haber varios. |
| `<tfoot>` | Agrupa el pie: totales, medias, notas al pie. |
| `<tr>` | *Table Row*: una fila. |
| `<th>` | *Table Header*: celda de encabezado (negrita y centrada por defecto). Atributos `scope` y `abbr`. |
| `<td>` | *Table Data*: celda de datos normal. |

!!! info "Qué es una tabla de datos"

    Un `<table>` es una **matriz con dos ejes**: las filas son entidades, las columnas son atributos y cada celda guarda **un único valor**. Todo lo que no encaje en esa idea (menús, portadas, rejillas de tarjetas) no es una tabla de datos.

Dos detalles que conviene memorizar:

- ==`caption`== va **dentro** de `<table>` y **al principio**; no es un `h1` suelto.
- Si escribes `<tr>` directamente dentro de `<table>`, el navegador **crea un `<tbody>` implícito**; por eso en CSS se selecciona `tbody > tr`, no `table > tr`. Y `<th>` no es "negrita y ya": es la celda que **define** a las demás.

### 2.2 Ejemplo mínimo anotado

```html title="precios.html" hl_lines="2 6"
<table>
  <caption>Taller El Olivo — precios con IVA de la tienda online</caption>
  <!-- caption SIEMPRE es el primer hijo de table: es el título accesible -->

  <thead>
    <tr>
      <th scope="col">Producto</th>
      <!-- scope="col": este th encabeza la COLUMNA de productos -->
      <th scope="col">Formato</th>
      <th scope="col" abbr="Euros">Precio (euros)</th>
      <!-- abbr: forma corta que el lector de pantalla anuncia en cada celda -->
    </tr>
  </thead>

  <tbody>
    <tr>
      <th scope="row">Aceite de oliva virgen extra</th>
      <!-- scope="row": este th encabeza la FILA (el producto) -->
      <td>Botella 1 L</td>
      <td>9,50 €</td>
    </tr>
    <tr>
      <th scope="row">Vinagre de Jerez</th>
      <td>Botella 500 ml</td>
      <td>4,25 €</td>
    </tr>
  </tbody>
</table>
```

## 3. Combinación de celdas: `colspan` y `rowspan`

### 3.1 Reglas de uso

- **`colspan="n"`**: la celda ocupa `n` columnas **en su propia fila** (se extiende a la derecha).
- **`rowspan="n"`**: la celda ocupa `n` filas **en sus propias columnas** (se extiende hacia abajo).
- Las celdas "cubiertas" por un `rowspan` **no se escriben**: si las escribes, la fila se desborda y el navegador empuja el resto hacia la derecha, desalineando toda la tabla.
- El `rowspan` se declara siempre en la **primera fila** del bloque que cubre.

### 3.2 Ejemplo: horario de clase

```html title="horario.html"
<table>
  <caption>Horario semanal — 1.º DAW A, 1.er trimestre</caption>
  <thead>
    <tr>
      <th scope="col">Hora</th>
      <th scope="col">Lunes</th>
      <th scope="col">Martes</th>
      <th scope="col">Miércoles</th>
      <th scope="col">Jueves</th>
      <th scope="col">Viernes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">08:00–10:00</th>
      <td>Programación</td>
      <td rowspan="2">Bases de datos</td> <!-- (1)! -->
      <!-- Esta celda ocupa también la franja de 10:00 a 12:00 -->
      <td>Programación</td>
      <td rowspan="2">Sistemas de gestión empresarial</td>
      <td>Programación</td>
    </tr>
    <tr>
      <th scope="row">10:00–12:00</th>
      <!-- OJO: NO escribo las celdas de Bases de datos ni Sistemas:
           ya las cubre el rowspan de la fila anterior -->
      <td>Lenguajes de marcas</td>
      <td>Entornos de desarrollo</td>
      <td>Desarrollo web en cliente</td>
    </tr>
    <tr>
      <th scope="row">12:00–14:00</th>
      <td colspan="5">Tutoría y trabajo autónomo (de lunes a viernes)</td> <!-- (2)! -->
      <!-- colspan="5": una sola celda para las 5 columnas de días -->
    </tr>
  </tbody>
</table>
```

1.  Una sola celda ocupa **dos franjas horarias**: la fila de abajo **no repite** esas `<td>`.

2.  `colspan="5"` extiende la celda **lo ancho de los cinco días**, así que el resto de la fila ya está completa.

### 3.3 Comprobación manual de la aritmética

Antes de dar una tabla por buena, comprueba el recuento **a mano**, fila a fila:

1. **Cuenta las columnas totales (T)** en la cabecera, sin contar `colspan` (aquí: `Hora` + 5 días = **T = 6**).
2. **Para cada fila**, suma `1` por cada celda + los adicionales de su `colspan` + los heredados de los `rowspan` de filas anteriores.
3. Si el total **no es exactamente T**, la tabla está rota, aunque el navegador intente "repararla".

| Fila | Celdas escritas | Huecos declarados | Heredados (`rowspan`) | Total |
|---|---|---|---|---|
| Encabezado | 6 `<th>` | 6 | 0 | **6 ✓** |
| 08:00–10:00 | 6 | 6 | 0 | **6 ✓** |
| 10:00–12:00 | 4 | 4 | 2 (Martes y Jueves) | **6 ✓** |
| 12:00–14:00 | 2 | 6 | 0 | **6 ✓** |

!!! success "Comprueba que la tabla está bien formada"

    - [ ] Todas las filas suman **el mismo total de columnas** que la cabecera.
    - [ ] Cada `rowspan` tiene su **hueco reservado** en la fila siguiente y esa celda no se vuelve a escribir.
    - [ ] Ninguna fila termina con **más celdas** de las que admite la cabecera.
    - [ ] El recuento se ha hecho **fila a fila, a mano**, no "a ojo".

**Truco:** dibuja la tabla, tacha las celdas cubiertas por ==`rowspan`== y comprueba que no queda ningún hueco sobrante.

!!! warning "Error común"

    El fallo clásico con `rowspan` es escribir la fila inferior **completa**, como si la celda superior no existiera: las columnas se desplazan y toda la tabla queda escalonada. Recuerda: **las celdas cubiertas se eliminan, no se dejan vacías** (una `<td></td>` vacía sigue ocupando su hueco).

## 4. `colgroup` y `col`: columnas enteras

`<colgroup>` va justo después de `<caption>` y agrupa columnas con `<col>` para aplicar estilo o ancho **a la columna entera** sin repetirlo celda a celda:

```html title="matricula.html" hl_lines="4 6"
<table>
  <caption>Matrícula del ciclo formativo</caption>
  <colgroup>
    <col span="1" style="width: 12rem; background-color: #f2f2f2;">
    <!-- 1.ª columna (Alumno) más ancha y con fondo gris -->
    <col span="3" style="background-color: #ffffff;">
  </colgroup>
  <thead>
    <tr>
      <th scope="col">Alumno/a</th>
      <th scope="col">Grupo</th>
      <th scope="col">Módulo</th>
      <th scope="col">Nota</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Ana Torres</th>
      <td>1.º DAW A</td>
      <td>Lenguajes de marcas</td>
      <td>8,5</td>
    </tr>
  </tbody>
</table>
```

- `span="n"` en `<col>` aplica la definición a `n` columnas seguidas.
- `<col>` es una etiqueta vacía que **solo admite atributos presentacionales** (`width`, `background-color`, `border`, `visibility`...); nunca lleva contenido.

**Ojo con el ancho:** el `width` de `<col>` (y el antiguo de `<td>`) es solo una **sugerencia**: el navegador puede ignorarlo si el contenido no cabe, porque el algoritmo de tablas prima el contenido. Para fijar anchos usa CSS (`tbody th { width: 12rem; }`) o `table-layout: fixed`.

??? note "Para saber más: por qué el navegador puede ignorar el ancho"

    El algoritmo de tabla calcula **primero** lo que necesita cada celda y **después** reparte el sobrante, así que `width` es solo una petición. Con `table-layout: fixed` se invierte el proceso: el navegador respeta **exactamente** los anchos de la primera fila (o los de `<col>`), pero entonces el contenido que no quepa se recorta o desborda.

## 5. Accesibilidad de las tablas

### 5.1 `th` + `scope` + `caption`: la tríada imprescindible

Para un lector de pantalla una tabla sin semántica es una lista de números sueltos; con la tríada puede anunciar *"Fila 3, Precio (euros), 9,50 €"*:

- **`caption`**: nombre de la tabla; se anuncia al entrar.
- **`th`**: identifica qué celda "define" a las demás.
- ==`scope`== marca la **dirección** del encabezado (`col` o `row`), para vincular cada dato con su fila y su columna.
    - scope="col" (Columna): Le indica a la tecnología asistencial que ese encabezado rige y da significado a todas las celdas que se encuentran verticalmente debajo de él.  
    - scope="row" (Fila): Le especifica que ese encabezado  define el contexto de todas las celdas que están horizontalmente a su derecha en esa misma fila.  
- **`abbr`**: abreviatura para no deletrear frases largas repetidas en cada celda.

No es opcional: se exige en **WCAG 1.3.1 (Información y relaciones)** y **4.1.2 (Nombre, rol, valor)**, de la clase de interfaces (→ [07-estructura-semantica-y-aria.md](07-estructura-semantica-y-aria.md)).

!!! question "¿Qué se pierde sin `scope`?"

    Una tabla de notas declara `<th>DIW</th>` en la primera columna, pero **ningún `th` lleva `scope`**. ¿Qué anuncia entonces el lector de pantalla?

    ??? success "Respuesta"

        Anuncia el texto **suelto y huérfano**: no puede decir si "DIW" es el nombre de la fila o de la columna, y el dato `7,5` pierde su contexto. Solución: **`scope="row"`** en el `th` de cada fila y **`scope="col"`** en los de cabecera.

### 5.2 Antes / después

**Antes (inaccesible):** encabezados pintados a mano con `<b>` y sin relación declarada.

```html title="inaccesible.html"
<table>
  <tr><td><b>Módulo</b></td><td><b>Nota</b></td></tr>
  <tr><td>DIW</td><td>7,5</td></tr>
</table>
<!-- Anuncia suelto: "Módulo Nota DIW 7,5", sin vínculo -->
```

**Después (semántico):** misma apariencia visual, relación declarada.

```html title="accesible.html" hl_lines="2 4"
<table>
  <caption>Notas de 1.º DAW A</caption>
  <thead>
    <tr><th scope="col">Módulo</th><th scope="col">Nota</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">DIW</th><td>7,5</td></tr>
  </tbody>
</table>
<!-- Anuncia: "Notas de 1.º DAW A. Encabezado Módulo, DIW. Nota, 7,5" -->
```

### 5.3 Tablas decorativas: `role="presentation"`

Si una tabla **no representa datos** (heredada de una plantilla de correo o de un widget que solo coloca elementos), decláralo para que el lector no anounce filas ni columnas:

```html title="configuracion.html"
<table role="presentation">
  <!-- Sin th y sin caption: se trata como una caja simple, como un div -->
  <tr>
    <td><img src="https://dummyimage.com/200x200/ccc/000.png&text=icono.png" alt="Ajustes"></td>
    <td>Configuración de la cuenta</td>
  </tr>
</table>
```

`role="presentation"` (o `role="none"`) **elimina la semántica de tabla**: no se navega por celdas y cada `<td>` deja de tener significado. Úsalo solo cuando la tabla **no aporta información relacional**; si tiene datos, la solución es semántica, no quitar roles.

## 6. Tablas responsivas: scroll en móvil

Una tabla ancha no cabe en una pantalla de 360 px. La solución estándar es **mantener la tabla y desplazar solo ella**, nunca romper la maquetación con `<table>`.

### 6.1 Contenedor con `overflow-x`

```html title="scroll-movil.html"
<!-- tabindex="0" permite desplazar con el teclado; role + aria-labelledby
     convierten la zona en una región nombrada por el caption -->
<figure class="tabla-scroll" tabindex="0" role="region" aria-labelledby="cap-horario"> <!-- (1)! -->
  <table>
    <caption id="cap-horario">Horario semanal — 1.º DAW A</caption>
    <!-- ... filas de la tabla ... -->
  </table>
</figure>
```

1.  `role="region"` + `aria-labelledby` convierten el contenedor en una **región con nombre** (el del `caption`), y `tabindex="0"` permite **enfocarla y desplazarla con las flechas**.

```css title="tabla-scroll.css"
.tabla-scroll {
  overflow-x: auto;            /* scroll horizontal SOLO en la tabla */
}

.tabla-scroll table {
  width: 100%;
  min-width: 44rem;            /* ancho mínimo: así aparece la barra en móvil */
  border-collapse: collapse;
  font-size: 0.875rem;
}
```

### 6.2 Qué consigues así

- **`overflow-x: auto`** (modelo de caja → [../css/03-modelo-de-caja.md](../css/03-modelo-de-caja.md)): la barra solo aparece si el contenido desborda; en escritorio no se ve.
- ==`tabindex="0"`== es **imprescindible**: el desplazamiento con teclado solo funciona si el contenedor recibe foco (WCAG 2.1.1).
- **`min-width` + fuente reducida**: caben más columnas sin que el texto quede ilegible[^1].

**Nunca** uses `overflow: hidden` para "arreglar" el desbordamiento: ocultas datos sin posibilidad de recuperarlos, y un contenedor de scroll **sin `tabindex="0"`** deja la tabla inalcanzable para quien navega con teclado o lector de pantalla.

## 7. Ejemplo práctico: acta de notas con `tfoot`

```html title="acta.html"
<table>
  <caption>Notas de evaluación — 1.º DAW A, 1.er trimestre</caption>
  <thead>
    <tr>
      <th scope="col">Módulo</th>
      <th scope="col">1.ª eval.</th>
      <th scope="col">2.ª eval.</th>
      <th scope="col">Proyecto</th>
      <th scope="col" abbr="Final">Nota final</th> <!-- (1)! -->
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Lenguajes de marcas</th>
      <td>7,0</td>
      <td>8,5</td>
      <td>9,0</td>
      <td>8,4</td>
    </tr>
    <tr>
      <th scope="row">Bases de datos</th>
      <td>5,5</td>
      <td>6,5</td>
      <td>7,5</td>
      <td>6,7</td>
    </tr>
  </tbody>
  <tfoot> <!-- (2)! -->
    <tr>
      <th scope="row">Media del grupo</th>
      <td>6,3</td>
      <td>7,3</td>
      <td>8,2</td>
      <td>7,5</td>
    </tr>
  </tfoot>
</table>
```

1.  `abbr="Final"` deja la **forma corta** que el lector anuncia en cada celda de esa columna, sin deletrear "Nota final" una y otra vez.

2.  `tfoot` agrupa la **fila de totales**: se coloca al final de la tabla y resume las dos evaluaciones con la media del grupo.

Todo lo visto junto: `caption`, `scope` en las dos dimensiones, `abbr` en la cabecera larga y `tfoot` con la media.

---

### 7.1 Explicación detallada: ¿Por qué se usa cada etiqueta y para qué sirve?

A continuación se realiza una disección técnica de cada etiqueta y atributo de la tabla `acta.html`, explicando su función en la estructura de datos tabulares y su impacto directo en la navegación accesible para personas con discapacidad visual:

#### 1. `<table>` — El contenedor semántico de datos tabulares
- **¿Para qué sirve?** Define un bloque estructurado para organizar datos en filas y columnas bidimensionales.
- **¿Por qué se usa aquí y cuál es la regla de oro?**
    - Se usa exclusivamente porque la información que mostramos es **genuinamente tabular** (una matriz relacional de notas por asignatura y evaluación).
    - **Regla estricta:** Está terminantemente prohibido utilizar `<table>` para maquetar el diseño de una interfaz (crear columnas de texto, menús o tarjetas). Las tablas solo deben contener datos; el diseño visual se construye con CSS (Flexbox y Grid).

#### 2. `<caption>` — El título accesible obligatorio de la tabla
- **¿Para qué sirve?** Representa el título formal y la descripción sucinta de la tabla (*«Notas de evaluación — 1.º DAW A, 1.er trimestre»*). Debe ser siempre el **primer hijo directo** de la etiqueta `<table>`.
- **Importancia crítica en Accesibilidad (WCAG 1.3.1):**
    - Cuando un usuario con lector de pantalla aterriza en una tabla, el software anuncia inmediatamente el contenido de `<caption>` junto con las dimensiones de la tabla (*"Tabla: Notas de evaluación, 5 columnas, 4 filas"*).
    - Esto permite al estudiante ciego decidir en menos de un segundo si la tabla le interesa o si prefiere saltarla con una tecla, sin tener que escuchar obligatoriamente las decenas de números de cada celda.

#### 3. `<thead>`, `<tbody>` y `<tfoot>` — División estructural en tres zonas
- **`<thead>` (Cabecera):** Agrupa las filas (`<tr>`) que contienen las etiquetas de cabecera de las columnas (`<th>`).
- **`<tbody>` (Cuerpo de datos):** Contiene el grueso de filas con los datos reales de los módulos profesionales.
- **`<tfoot>` (Pie o totales):** Agrupa las filas de resumen, estadísticas, totales o medias.
- **Ventajas de esta separación:**
    - **Impresión en papel (*Print CSS*):** Si la tabla tiene 200 filas y se imprime en varias páginas, el navegador repite automáticamente el bloque `<thead>` en la parte superior de cada folio y el `<tfoot>` en la inferior.
    - **Tablas con scroll vertical:** Permite fijar la cabecera arriba con CSS (`position: sticky`) mientras los datos de `<tbody>` se desplazan libremente.

#### 4. `<tr>` — Fila de tabla (*Table Row*)
- **¿Para qué sirve?** Delimita cada una de las líneas horizontales de la cuadrícula. No puede contener texto directamente; solo puede albergar celdas `<th>` o `<td>`.

#### 5. `<th>` con `scope="col"` y `scope="row"` — Celdas de encabezado dimensionales
- **¿Para qué sirve `<th>`?** Define una celda de encabezado (*Table Header*). Visualmente el navegador la muestra en negrita y centrada por defecto, pero su auténtica función es semántica.
- **El atributo `scope` (Bidimensionalidad accesible):**
    - **`scope="col"` (En la fila de `<thead>`):** Indica que ese encabezado rige verticalmente para **todas las celdas de esa columna**. Por ejemplo, `<th scope="col">Proyecto</th>` indica que cualquier nota situada debajo pertenece al proyecto.
    - **`scope="row"` (En la primera celda de cada fila):** Indica que ese encabezado rige horizontalmente para **todas las celdas de esa fila**. Por ejemplo, `<th scope="row">Lenguajes de marcas</th>`.
- **La experiencia de usuario con lector de pantalla:** Gracias a `scope`, cuando una persona ciega navega por la cuadrícula con las flechas del teclado y se sitúa sobre la celda `8,5`, el lector de pantalla no se limita a decir "ocho coma cinco", sino que vocaliza el contexto completo: *"Lenguajes de marcas, 2.ª eval., 8,5"*. Sin `scope`, los números quedan completamente descontextualizados e incomprensibles.

#### 6. `abbr="Final"` en cabecera — Abreviatura para lectores de pantalla
- **¿Para qué sirve?** Proporciona una versión resumida o abreviada del texto de un encabezado largo.
- **¿Por qué se usa aquí?** En la última columna, el texto visible es *"Nota final"*. El atributo `abbr="Final"` ordena a las tecnologías de asistencia que, al recorrer las celdas inferiores de esa columna, utilicen la palabra corta *"Final"* en vez de repetir la frase larga una y otra vez, agilizando enormemente la velocidad de escucha del estudiante.

#### 7. `<td>` — Celdas de datos estándar (*Table Data*)
- **¿Para qué sirve?** Contiene los valores numéricos o informativos ordinarios del informe (las calificaciones numéricas). Cada `<td>` hereda automáticamente la asociación semántica con el `<th>` de su columna y el `<th>` de su fila.

---

## 8. Errores frecuentes y claves para el examen

!!! warning "Error común"

    Los tres fallos que más se corrigen en la práctica:
    
    - **Usar `<table>` para maquetar** (cabecera, menú, tarjetas): eso es trabajo de Flexbox y Grid → [../css/05-flexbox.md](../css/05-flexbox.md), [../css/06-grid.md](../css/06-grid.md).
    - **`<th>` sin `scope`** (o un `<th>` decorativo en negrita): el lector no vincula la celda con su fila o su columna.
    - **Olvidar `<caption>`**: la tabla queda sin título accesible y hay que adivinar su propósito leyendo celda a celda.

!!! tip "Claves para el examen"

    - `<table>` **solo** para datos tabulares; para layout, Flexbox (una dimensión) o Grid (dos dimensiones).
    - Orden dentro de `<table>`: `<caption>` → `<colgroup>` → `<thead>` / `<tbody>` → `<tfoot>`; `<caption>` es siempre el primer hijo.
    - `<th>` con **`scope="col"`** (encabeza columna) o **`scope="row"`** (encabeza fila); `abbr` guarda la versión corta.
    - `colspan` une **columnas en la misma fila**; `rowspan` une **filas hacia abajo** y las celdas cubiertas **no se escriben**: comprueba fila a fila que todas suman las mismas columnas.
    - `<col>`/`colgroup` sirve para estilo de columna entera y su `width` puede ser ignorado → ancho fiable con CSS o `table-layout: fixed`.
    - Responsivo: contenedor con `overflow-x: auto`, `tabindex="0"` y `role="region"` + `aria-labelledby` apuntando al `id` del `caption`.


!!! success "Practica esta unidad"

    - Enunciados: [Ejercicios de la Unidad 5 — Tablas de datos](09-ejercicios.md#u71-encabezados-sin-saltos) — cuatro retos (`U5.1` a `U5.4`) — del más básico al más avanzado.
    - Comprueba tu trabajo con [las soluciones de esta unidad](10-ejercicios-soluciones.md#sol-u5).

*[HTML]: HyperText Markup Language
*[WCAG]: Web Content Accessibility Guidelines

[^1]: Valores de partida usados arriba: `min-width: 44rem` (unos 704 px con fuente base de 16 px) y `font-size: 0.875rem`. Si la tabla tiene muchas columnas, sube el mínimo antes que bajar más la fuente.
