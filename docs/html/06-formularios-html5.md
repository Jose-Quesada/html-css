---
icon: lucide/clipboard-list
title: "HTML 06 - Formularios HTML5"
description: "Formularios en HTML5: elemento form con GET y POST, label y fieldset, tipos de input, atributos de validación nativa, Constraint Validation API y accesibilidad de los campos."
modulo: "LMH (0373) / DIW (0615) / DI (0488)"
unidad: 6
fecha: "2026-09-29"
---

# HTML 06 — Formularios HTML5

Un formulario es la **puerta de entrada de datos** hacia el servidor: sin `label`, sin `name` o con `method` equivocado, el dato se pierde o el usuario no puede escribir. Aquí vemos `form`, los tipos de `input` con su validación nativa, los atributos de control y la accesibilidad.

!!! note "Conocimientos previos"

    - Estructura de un documento HTML.
    - Accesibilidad y ARIA de la clase de interfaces (→ [07-estructura-semantica-y-aria.md](07-estructura-semantica-y-aria.md)).
    - Constraint Validation y otras APIs → [08-apis-html5.md](08-apis-html5.md); práctica → [09-ejercicios.md](09-ejercicios.md).

## 1. El elemento `form`

### 1.1 `action` y `method`: GET vs POST

`<form>` envía los campos a la URL de **`action`** con el verbo de **`method`**.

| | **GET** | **POST** |
|---|---|---|
| Dónde van los datos | En la **URL**: `buscar?nota=8` | En el **cuerpo** de la petición |
| En la URL | Sí: historial, caché, *logs* | No |
| Longitud | Limitada (~2.000-8.000 caracteres) | Sin límite práctico |
| Efecto | Consulta, repetible | Escritura, crea o modifica |

**Regla:** datos **sensibles o largos** → `POST`: una contraseña con `GET` queda en la barra de dirección, en el historial y en los *logs*. Cada campo viaja como `clave=valor` con como clave su atributo `name`.

=== "GET"

    ```html title="busqueda.html"
    <form action="/buscar" method="get" role="search">
      <input type="search" id="q" name="q" placeholder="Lenguajes de marcas">
      <button type="submit">Buscar</button>
    </form>
    ```

=== "POST"

    ```html title="login.html"
    <form action="/login" method="post">
      <label for="usuario">Usuario</label>
      <input type="text" id="usuario" name="usuario" autocomplete="username" required>
      <label for="clave">Contraseña</label>
      <input type="password" id="clave" name="clave" autocomplete="current-password" required>
      <button type="submit">Entrar</button>
    </form>
    ```

!!! danger "Datos sensibles enviados con `GET`"

    El valor queda en la **barra de dirección**, en el **historial**, en **marcadores** y en los **logs** de proxy y servidor: cualquiera con acceso a esos registros lo lee sin esfuerzo. Credenciales, DNI y tarjetas → **`POST` siempre**.

### 1.2 `enctype`, `name`/`id` y `novalidate`

- **`enctype`**: por defecto `application/x-www-form-urlencoded` y, con `type="file"`, es obligatorio `multipart/form-data`.
- **`name`** es la clave de envío y **`id`** el identificador que enlaza el `<label>`: **sin `name` el dato no se envía**, aunque el campo esté relleno.
- **`novalidate`**: desactiva la validación nativa para validar con JavaScript.

!!! info "Qué viaja en el cuerpo de la petición"

    Con `application/x-www-form-urlencoded` los campos se serializan como `clave=valor&...` (el mismo formato que usan las URLs). Con `multipart/form-data` se abre un **límite por parte** y el navegador añade cabeceras `Content-Disposition`: por eso es **obligatorio** al subir ficheros con `type="file"`.

### 1.3 HTML no programa: el control llega con TypeScript

HTML declara los campos, pero no calcula ni muestra mensajes propios: eso es JavaScript. En la clase de interfaces verás que en **Angular** el `<form>` se controla con TypeScript (*Reactive Forms*, `ngSubmit`) y el envío va con `HttpClient`.

## 2. `label`: la pieza obligatoria

### 2.1 `for` / `id` y área de clic

```html title="nombre.html"
<label for="nombre">Nombre y apellidos</label>
<input type="text" id="nombre" name="nombre">
```

- `for` debe coincidir **exactamente** con el `id`.
- Da **área de clic**: al pulsar el texto se enfoca (o se marca si es `radio`/`checkbox`), con objetivo cómodo en táctil.
- También vale envolver el campo dentro del label, pero con varios campos juntos `for`/`id` es más claro.

### 2.2 `placeholder` ≠ `label`

| | `<label>` | `placeholder` |
|---|---|---|
| ¿Qué es? | Etiqueta permanente | Ayuda **temporal** dentro del campo |
| ¿Se ve tras escribir? | Siempre | No: desaparece al escribir |
| ¿Lo anuncia el lector? | Sí: es el **nombre** del campo | No, o de forma poco fiable |
| ¿Sirve para el formato? | Junto a un texto de ayuda | Como pista, nunca como única info |

El ==`label`== **es obligatorio**; el `placeholder` es opcional y se borra al escribir.

### 2.3 `fieldset` y `legend`: agrupar opciones

Los campos que el usuario percibe como **un mismo bloque** se envuelven en ==`fieldset`==, y `legend` aporta su título accesible:

```html title="turno.html"
<fieldset>
  <legend>Turno de matrícula</legend>
  <input type="radio" id="manana" name="turno" value="manana">
  <label for="manana">Mañana</label>
  <input type="radio" id="tarde" name="turno" value="tarde">
  <label for="tarde">Tarde</label>
</fieldset>
```

- `<legend>` es el **título accesible** del grupo: el lector lo anuncia antes de cada opción.
- Los `radio` de un grupo comparten **el mismo `name`** (solo se marca uno); cada control lleva su `id`/`label`.
- Los `checkbox` son independientes: cada uno con su `name`.

!!! example "Qué oye el lector de pantalla"

    Al enfocar cada opción del bloque anterior se anuncia *"Turno de matrícula, Mañana, 1 de 2, botón de opción"*.

    Sin `fieldset`/`legend`, el mismo campo suena **solo** *"Mañana, 1 de 2"*: **se pierde el grupo** al que pertenece.

## 3. Tipos de `input`: tabla completa

El `type` decide **qué acepta** el navegador y **qué teclado** aparece en móvil: validación + teclado.

| `type` | Validación nativa | Teclado móvil | Ejemplo |
|---|---|---|---|
| `text` | Ninguna (solo `maxlength`) | Alfanumérico | DNI |
| `password` | Ninguna (oculta la entrada) | Alfanumérico | Contraseña |
| `email` | Formato `algo@dominio.tld` | `@` y `.es` | Correo |
| `url` | Exige `http(s)://` | `/` y `.com` | Página personal |
| `tel` | Ninguna (validar en servidor) | Numérico con `+` | Teléfono |
| `search` | Ninguna (botón de borrado) | Alfanumérico | Buscador |
| `number` | Números con `min`/`max`/`step` | Numérico `+ -` | Nota, edad |
| `range` | Dentro de `min`/`max` | Deslizador | Satisfacción |
| `date` | Fecha del calendario | Selector de fecha | Nacimiento |
| `time` | Hora válida | Selector de hora | Tutoría |
| `datetime-local` | Fecha y hora juntas | Fecha y hora | Cita previa |
| `month` | Mes y año válidos | Mes/año | Caducidad |
| `week` | Semana ISO válida | Selector de semana | Entrega semanal |
| `color` | Solo `#rrggbb` | Paleta de color | Color corporativo |
| `file` | Extensión según `accept` | Selector de archivos | Subir currículum |
| `checkbox` | Marcado o no | Casilla grande | Aceptar condiciones |
| `radio` | **Uno** del grupo marcado | Casilla redonda | Turno, pago |
| `hidden` | Oculto, no editable, **sí se envía** | — | ID del curso |

**Importante:** `email`, `url` o `date` solo garantizan **forma correcta**, no que el dato sea **verdadero**. La validación definitiva es del servidor.

## 4. Atributos de validación y control

### 4.1 `required`, `readonly` y `disabled`

```html title="estados.html" hl_lines="2 3"
<input type="text" id="dni" name="dni" required>
<input type="text" id="curso" name="curso" value="2026-2027" readonly>
<input type="text" id="codigo" name="codigo" value="DAW-A" disabled>
```

El ==`required`== **bloquea el envío** hasta que el campo tenga valor; `readonly` **se envía** (visible y tabulable); `disabled` **no** (gris, sin foco). El primero deja un valor calculado en el formulario; el segundo apaga un control hasta que corresponda.

!!! question "¿Qué llega al servidor?"

    Los tres campos de arriba se cumplimentan y se pulsa el botón de envío. ¿Qué recibe el servidor y qué no?

    ??? success "Respuesta"

        - `dni` (`required`): se envía si tiene valor; **vacío, el navegador ni siquiera deja enviar**.
        - `curso` (`readonly`): **sí se envía**, porque el campo sigue visible, enfocable y con nombre.
        - `codigo` (`disabled`): **no se envía**, como si no existiera en el formulario.

### 4.2 `min`, `max`, `step`, `minlength`, `maxlength`

- `min`/`max` y `step` en `number` (`min="0" max="10" step="0.5"`), en `range` y en `date` (`min="2026-10-01"`): delimitan el intervalo.
- En `number`, `step` por defecto es `1`: `step="0.5"` admite 7,5 pero no 7,3.
- `minlength`/`maxlength` miden **caracteres**; `maxlength` además corta la escritura.

### 4.3 `pattern`: validar un formato exacto

```html title="nif.html"
<label for="nif">NIF</label>
<input type="text" id="nif" name="nif" pattern="[0-9]{8}[A-Za-z]"
       title="8 dígitos y una letra, ej.: 12345678Z" required>
```

- ==`pattern`== recibe una **expresión regular** que cubre **todo** el valor (el navegador añade `^` y `$`). Otro caso: `pattern="[A-Z]{3}-[0-9]{2}"` → `LMH-05`.
- `title` alimenta el mensaje de error y describe el formato al lector.
- Sensible a mayúsculas: `[a-z]` no admite `A`.

### 4.4 `placeholder`, `value` y `autocomplete`

- **`placeholder`**: pista de formato; se borra al escribir y nunca sustituye al label (§ 2.2).
- **`value`**: valor inicial o fijo; en los botones, el texto visible.
- **`autocomplete`**: qué autocompleta el navegador (`name`, `email`, `tel`, `postal-code`, `current-password`, `cc-number`...); criterio **WCAG 1.3.5**.

### 4.5 `multiple`, `accept`, `list` y `datalist`

```html title="adjuntos.html"
<input type="file" id="docs" name="docs" accept=".pdf,.jpg" multiple> <!-- (1)! -->

<input type="text" id="modulo" name="modulo" list="modulos"> <!-- (2)! -->
<datalist id="modulos">
  <option value="Lenguajes de marcas">
</datalist>
```

1.  `multiple` permite adjuntar **varios ficheros** en un solo campo y `accept` filtra las extensiones que ofrece el selector.

2.  `list` enlaza el campo con el `datalist` de debajo: el navegador muestra las **sugerencias** mientras se escribe.

`datalist` ofrece **sugerencias** pero **no obliga** a elegir: no sustituye a un `<select>`, donde solo se escoge entre las opciones.

### 4.6 `autofocus`, `spellcheck` e `inputmode`

- **`autofocus`**: enfoca al cargar; evítalo con varios campos: interrumpe a quien usa lector de pantalla.
- **`spellcheck="false"`**: apaga el corrector (códigos, usuario, contraseñas).
- **`inputmode`**: teclado virtual (`numeric`, `decimal`, `email`, `tel`) **sin cambiar el `type`**; ideal para DNI o CP, donde `type="number"` admite `e` y `+`.

## 5. El resto de controles

### 5.1 `select`, `optgroup` y `selected`

```html title="ciclo.html"
<label for="ciclo">Ciclo formativo</label>
<select id="ciclo" name="ciclo" required>
  <optgroup label="Grado medio">
    <option value="smr">Sistemas microinformáticos y redes</option>
  </optgroup>
  <optgroup label="Grado superior">
    <option value="daw" selected>Desarrollo de aplicaciones web</option>
  </optgroup>
</select>
```

- Lo que se envía es **`value`**; sin `value`, se envía el texto.
- **`selected`** precarga y **`optgroup`** agrupa con un subtítulo.
- `required` exige elegir: por eso se añade `<option value="" disabled selected>Elige una opción</option>`.

### 5.2 `textarea`

```html title="observaciones.html"
<label for="obs">Observaciones</label>
<textarea id="obs" name="obs" rows="4" cols="60" maxlength="500"
          placeholder="Necesito adaptación de horario..."></textarea>
```

`rows`/`cols` fijan el tamaño inicial y `maxlength` limita los caracteres; el texto va **entre las etiquetas**: no usa `value`.

### 5.3 `output`, `progress` y `meter`

- **`<output>`**: resultado **calculado** (media de las notas, total de la cesta).
- **`<progress>`**: avance de una **tarea** hacia una meta: `<progress value="3" max="4">` (sin `value` queda indeterminado); subida de archivo, paso 3 de 4.
- **`<meter>`**: medida con **umbral** que se colorea sola: `<meter value="6,7" low="5" high="8">` (nota, espacio en disco, batería).

Clave: `progress` es **cómo va** una operación; `meter` es **en qué estado** está una cantidad.

### 5.4 `<button>`: `type="submit"`, `reset` o `button`

```html title="botones.html"
<button type="submit">Enviar matrícula</button>        <!-- envía el form -->
<button type="reset">Borrar todo</button>              <!-- valores iniciales -->
<button type="button" id="vista">Vista previa</button> <!-- solo con JS -->
```

⚠ El **valor por defecto de `<button>` es `submit`, no `button`** (igual que `<input type="submit">`): un botón "Calcular media" **sin `type`** envía el formulario sin querer. **Escribe siempre `type`**.

## 6. Validación nativa de HTML5

### 6.1 Mensajes del navegador y pseudoclases

El navegador comprueba `required`, `type`, `pattern`, `min`/`max`... y muestra su mensaje (*"Introduce un correo electrónico válido"*). Es correcto, pero **no se estila con CSS**; sí lo hacen las pseudoclases:

```css title="validacion.css" hl_lines="1 3"
input:invalid:not(:placeholder-shown) { border-color: #b00020; }  /* error real */
input:valid                            { border-color: #146c2e; }
input:user-invalid                      { border-color: #b00020; }  /* tras interactuar */
```

`:user-invalid` marca el campo **solo después** de escribir o enviar, evitando que la página arranque "en rojo".

### 6.2 Constraint Validation API

Para leer el estado desde JavaScript (→ [08-apis-html5.md](08-apis-html5.md)):

- **`campo.checkValidity()`** → `true`/`false` aplicando todas las reglas.
- **`campo.validity`** → el motivo: `valueMissing`, `typeMismatch`, `patternMismatch`, `tooShort`, `rangeUnderflow`, `stepMismatch`, `customError`...
- **`campo.validationMessage`** → texto de error listo para mostrar y **`setCustomValidity("...")`** → mensaje propio (cadena vacía para limpiarlo).

### 6.3 `novalidate` y validación propia

`<form action="/matricula" method="post" novalidate>` apaga los globos nativos para mostrar errores con **nuestro diseño e idioma**. A cambio la validación pasa a JavaScript, que puede fallar: se mantienen `required`, `pattern` y `type` en el HTML y **se valida siempre también en el servidor**.

## 7. Accesibilidad de los formularios

- **`label` visible siempre**, nunca solo `placeholder` (→ [07-estructura-semantica-y-aria.md](07-estructura-semantica-y-aria.md)).
- **Errores asociados al campo**: `aria-describedby` apunta al `id` del mensaje, `role="alert"` lo anuncia al aparecer y `aria-invalid="true"` marca el campo.
- **`required` + `aria-required="true"`** cuando el estado lo gestiona el código.
- **`fieldset`/`legend`** agrupan radios y checkboxes: el `legend` es el nombre del grupo.
- **Orden de tabulación = orden del documento**: `Tab` pasa de campo en campo; evita `tabindex` positivos.

```html title="error-email.html" hl_lines="2 3"
<label for="email">Correo electrónico</label>
<input type="email" id="email" name="email" required aria-required="true"
       aria-describedby="err-email" aria-invalid="true"> <!-- (1)! -->
<p id="err-email" role="alert">Debe tener formato usuario@dominio.com</p>
```

1.  `aria-describedby` enlaza el mensaje con el campo, `aria-invalid="true"` lo declara erróneo y `role="alert"` hace que el lector **lo anuncie al aparecer**.

!!! success "Comprueba que el formulario es accesible"

    - [ ] Todos los campos tienen **`label` visible**, no solo `placeholder`.
    - [ ] Cada error apunta al campo con **`aria-describedby`** y se anuncia con **`role="alert"`**.
    - [ ] Los grupos de radios van con **`fieldset` + `legend`**.
    - [ ] El orden de `Tab` **coincide con el orden visual** (sin `tabindex` positivos).

## 8. Ejemplo práctico: formulario de matrícula

```html title="matricula.html"
<form action="/matricula" method="post" enctype="multipart/form-data">
  <!-- POST: nada de URL cargada; multipart: hay un file -->
  <fieldset>
    <legend>Datos personales</legend> <!-- (1)! -->
    <label for="nombre">Nombre y apellidos</label>
    <input type="text" id="nombre" name="nombre" autocomplete="name" required>
    <!-- autocomplete cumple WCAG 1.3.5 -->
    <label for="dni">DNI/NIE</label>
    <input type="text" id="dni" name="dni" pattern="[0-9]{8}[A-Za-z]"
           title="8 dígitos y una letra, ej.: 12345678Z"
           aria-describedby="pista-dni" required>
    <span id="pista-dni">Ejemplo: 12345678Z</span>
    <!-- pista asociada al campo -->
    <label for="email">Correo electrónico</label>
    <input type="email" id="email" name="email" autocomplete="email" required>
    <label for="nacimiento">Fecha de nacimiento</label>
    <input type="date" id="nacimiento" name="nacimiento" required>
  </fieldset>
  <fieldset>
    <legend>Turno de matrícula</legend>
    <input type="radio" id="manana" name="turno" value="manana" required>
    <label for="manana">Mañana</label>
    <input type="radio" id="tarde" name="turno" value="tarde">
    <label for="tarde">Tarde</label>
    <!-- mismo name: solo uno marcado -->
  </fieldset>
  <label for="observaciones">Observaciones</label>
  <textarea id="observaciones" name="observaciones" rows="4" cols="60"
            maxlength="500" placeholder="Adaptación de horario..."></textarea>
  <label for="cv">Currículum (PDF)</label>
  <input type="file" id="cv" name="cv" accept=".pdf, application/pdf">
  <input type="checkbox" id="terminos" name="terminos" value="si" required> <!-- (2)! -->
  <label for="terminos">He leído y acepto la normativa del centro</label>
  <!-- required: sin marcarlo no se envía -->
  <button type="submit">Enviar matrícula</button>
  <button type="reset">Borrar formulario</button>
</form>
```

1.  El `legend` da **nombre accesible** al primer grupo: el lector lo anuncia antes de cada campo que lleva dentro.

2.  `required` en la casilla de normativa: **si no se marca, el navegador bloquea el envío**.

`label`+`id` y `name` en cada campo, validación nativa y `POST` para los datos personales.

## 9. Claves para el examen y errores frecuentes

!!! warning "Error común"

    Usar el **`placeholder` como si fuera el `label`**. Al escribir desaparece: el usuario ya no sabe qué campo rellena, el lector no lo toma como nombre y, si el campo viene precargado, no se ve nada. Solución: `<label for="id">` **siempre visible** y el `placeholder` solo como pista.

!!! warning "Error común"

    Enviar un login o datos sensibles con **`method="get"`**: los valores quedan en la barra de dirección, en el historial, en los marcadores y en los registros del servidor. Contraseñas, DNI y tarjetas → **`method="post"`**.

!!! tip "Claves para el examen"

    - `<form>` = `action` (dónde) + `method` (cómo): `GET` para consultas en la URL, `POST` para datos sensibles o largos.
    - `label for` ↔ `id` es obligatorio; el `placeholder` nunca sustituye a la etiqueta.
    - Sin **`name`** el dato no llega al servidor; **`readonly` sí se envía, `disabled` no**.
    - El **`type`** aporta validación y teclado móvil; se refuerzan con `required`, `pattern` y `min`/`max`/`step`.
    - `fieldset` + `legend` agrupan; los radios comparten `name` y cada control su `id`/`label`.
    - `<button>` **sin `type` equivale a `submit`**: los botones de acción propia necesitan `type="button"`.
    - Validación con pseudoclases CSS y Constraint Validation API → [08-apis-html5.md](08-apis-html5.md); práctica → [09-ejercicios.md](09-ejercicios.md).

*[HTML]: HyperText Markup Language
*[WCAG]: Web Content Accessibility Guidelines
