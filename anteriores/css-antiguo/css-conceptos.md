
## La Herencia en CSS

La **herencia** es uno de los tres pilares fundamentales de CSS (junto con la Cascada y la Especificidad). Entenderla es la diferencia entre escribir 1.000 líneas de código repetitivo o escribir 100 líneas elegantes y fáciles de mantener.


### 1. ¿Qué es la Herencia?

La herencia es el mecanismo por el cual ciertas propiedades CSS se pasan de un elemento padre a sus elementos hijos.

Si aplicas un color de texto al `<body>`, no necesitas aplicárselo a cada `<p>`, `<h1>` o `<span>` individualmente; ellos lo "heredan" automáticamente. Esto se basa en la estructura del **DOM (Document Object Model)**.

---

### 2. ¿Qué propiedades se heredan y cuáles no?

No todas las propiedades se heredan. Imagina que el `border` se heredara: si le pones un borde a un `div`, ¡todos sus párrafos, enlaces y negritas tendrían también un borde individual! Sería un caos visual.

#### A. Propiedades que SÍ se heredan (Relacionadas con el texto)

Generalmente, todo lo que tiene que ver con la tipografía y el color del contenido:

* `color`
* `font-family`, `font-size`, `font-weight`
* `line-height`
* `text-align`
* `letter-spacing`, `word-spacing`
* `list-style`

**Ejemplo de código:**

```html
<div style="color: darkgreen; font-family: Arial;">
    <h1>Título Verde</h1>
    <p>Este párrafo también es verde porque hereda del div.</p>
    <ul>
        <li>Incluso los items de la lista son verdes.</li>
    </ul>
</div>

```

#### B. Propiedades que NO se heredan (Relacionadas con la caja/layout)

Todo lo que define la forma, posición y espacio del contenedor:

* `margin`, `padding`
* `border`, `outline`
* `width`, `height`
* `background` (color, imagen)
* `position`, `top`, `left`, etc.
* `display`

**Ejemplo de código:**

```css
.contenedor-padre {
    border: 2px solid red;
    padding: 20px;
    background-color: lightblue;
}

/* El párrafo de abajo NO tendrá borde rojo, ni fondo azul, ni padding, 
   aunque esté dentro del div padre. */

```

---

### 3. Forzando la Herencia: La palabra clave `inherit`

A veces queremos que una propiedad que **no** se hereda por defecto, lo haga. O queremos que un elemento hijo recupere el valor de su padre.

**Caso de uso típico: Los Enlaces**
Por defecto, los navegadores dan a los enlaces (`<a>`) un color azul, ignorando la herencia del padre. Podemos forzarlo:

```css
.seccion-oscura {
    color: white;
}

.seccion-oscura a {
    /* Forzamos al enlace a ser blanco como su padre, 
       en lugar del azul por defecto del navegador */
    color: inherit; 
}

```

---

### 4. Otros valores de control: `initial`, `unset` y `revert`

Para tener un control total sobre la herencia, CSS ofrece estas palabras clave:

1. **`initial`**: Cambia el valor de la propiedad al valor por defecto que dicta el estándar de CSS (no el del navegador).
* *Ejemplo:* `color: initial;` pondrá el texto en negro, independientemente de lo que diga el padre.


2. **`unset`**: Es inteligente. Si la propiedad es heredable, se comporta como `inherit`. Si no lo es, se comporta como `initial`.
3. **`revert`**: Vuelve al estilo que tenía el elemento según la hoja de estilo por defecto del navegador (*User Agent Stylesheet*).

---

### 5. Herencia vs. Especificidad

Es muy importante entender que **la herencia es la fuerza más débil**.

Si un elemento hijo tiene un selector directo que le aplica un estilo, ese estilo **siempre** ganará al valor heredado, sin importar lo específica que sea la regla del padre.

**Ejemplo:**

```html
<style>
    #padre-muy-importante { color: red; } /* Selector de ID (muy fuerte) */
    p { color: blue; }                   /* Selector de etiqueta (débil) */
</style>

<div id="padre-muy-importante">
    <p>¿De qué color soy?</p> 
    </div>

```

---

### Resumen

| Situación | Comportamiento |
| --- | --- |
| **Propiedad tipográfica** | Se hereda automáticamente (color, fuentes). |
| **Propiedad de caja** | No se hereda (bordes, márgenes, fondos). |
| **Uso de `inherit**` | Obliga al hijo a copiar el valor del padre. |
| **Conflicto** | Cualquier estilo directo al hijo anula lo heredado. |

---

#### Actividad : "El Árbol Genealógico"

Crea un `div` con un `section` dentro, y un `p` dentro del `section`.

1. Poner un tipo de letra en el `div` y ver cómo llega al `p`.
2. Intentar poner un `border` en el `div` y ver que el `p` no lo tiene.
3. Finalmente, usar `inherit` en el `p` para "robarle" el borde al `div`.


---

##  La Cascada en CSS

### 1. ¿Qué es exactamente la Cascada?

La "C" de CSS significa *Cascading* (Cascada). Imagina el código CSS como un río que fluye desde arriba hacia abajo. A medida que el agua baja, las reglas que están más abajo o que tienen más "fuerza" arrastran y sobrescriben a las anteriores.

Cuando hay un conflicto (ejemplo: una regla dice que el botón es rojo y otra dice que es azul), el navegador usa **tres criterios** en este orden exacto para decidir al ganador:

1. **Importancia** (El comodín)
2. **Especificidad** (El peso del selector)
3. **Orden de origen** (El último en llegar)

---

### Criterio 1: La Importancia (`!important`)

Es la regla nuclear. Si una declaración lleva la etiqueta `!important`, gana automáticamente, ignorando la especificidad y el orden.

```css
.boton-peligro {
    background-color: red !important; /* Esto ganará SIEMPRE */
}

#boton-unico {
    background-color: blue; /* Pierde, aunque el ID sea más específico */
}

```

>  **Advertencia:** ¡No uses `!important` para arreglar problemas de código! Rompe el flujo natural de la Cascada y hace que el CSS sea imposible de mantener. Solo debe usarse en casos muy extremos (como sobrescribir estilos de una librería externa que no puedes modificar).

---

### Criterio 2: La Especificidad (El Sistema de Puntos)

Si no hay `!important`, el navegador mira la **especificidad**. Cuanto más específico sea un selector, más "peso" o "puntos" tiene.

Podemos imaginarlo como una puntuación de tres cifras: **(ID, Clases, Etiquetas)**.

| Tipo de Selector | Ejemplo | Puntuación aproximada |
| --- | --- | --- |
| **Estilos en línea** | `style="..."` en HTML | **1000 puntos** (Gana a todo menos a `!important`) |
| **Identificadores (ID)** | `#cabecera` | **100 puntos** |
| **Clases, Atributos y Pseudo-clases** | `.btn`, `[type="text"]`, `:hover` | **10 puntos** |
| **Etiquetas y Pseudo-elementos** | `h1`, `div`, `::before` | **1 punto** |
| **Selector Universal** | `*` | **0 puntos** |

### Ejemplo de Combate (Especificidad en acción):

Imagina este HTML: `<p class="texto-destacado" id="intro">Hola</p>`

```css
/* Batalla por el color del texto: */

p { 
    color: green; 
    /* Puntos: 1 (Etiqueta). */
}

.texto-destacado { 
    color: blue; 
    /* Puntos: 10 (Clase). Gana al verde. */
}

#intro { 
    color: red; 
    /* Puntos: 100 (ID). Gana al azul. El texto será ROJO. */
}

```

### Sumando puntos en selectores complejos:

Si combinas selectores, los puntos se suman:

* `nav ul li` ➔ 3 etiquetas = **3 puntos**.
* `.menu li` ➔ 1 clase + 1 etiqueta = **11 puntos**.
* `#header .logo img` ➔ 1 ID + 1 clase + 1 etiqueta = **111 puntos**.

---

### Criterio 3: El Orden de Origen (La regla del más "fresco")

¿Qué pasa si dos selectores tienen exactamente **los mismos puntos** de especificidad? Aquí entra la regla más sencilla de todas: **el último que se declara en el código, gana**.

El navegador lee de arriba a abajo. La última instrucción sobrescribe a las anteriores.

```css
/* Ambos tienen la misma especificidad (10 puntos por ser clases) */

.caja {
    background-color: yellow;
}

.caja {
    background-color: purple; /* ESTA GANA porque está más abajo */
}

```

Esto también se aplica al orden en que llamas a tus archivos CSS en el HTML:

```html
<link rel="stylesheet" href="estilos-base.css">
<link rel="stylesheet" href="tema-oscuro.css">

```

---

## Resumen del Algoritmo

Para interiorizar cómo piensa el navegador ante un elemento, responde a las preguntas en orden:

1. ¿Hay alguna regla con `!important`? (Si sí, fin del debate).
2. Si no, ¿qué regla tiene el selector con la puntuación de **Especificidad** más alta? (IDs > Clases > Etiquetas).
3. Si hay un empate de puntos, ¿cuál está escrita **más abajo** en el archivo CSS?

---

¿Te gustaría que preparemos un **"Juego de la Calculadora de Especificidad"**? Les doy 5 o 6 selectores complejos y tienen que calcular los puntos y decirme qué color ganaría en una pelea a tres bandas. Es una dinámica súper efectiva en clase.


## Selectores Avanzados en CSS

### 1. Combinadores (Relaciones en el DOM)

Los combinadores definen cómo se relacionan dos selectores basándose en su ubicación en el árbol de etiquetas.

| Combinador | Nombre | Selección |
| --- | --- | --- |
| `A B` | **Descendiente** | Cualquier `B` que esté dentro de `A` (sin importar el nivel). |
| `A > B` | **Hijo directo** | Solo los `B` que son hijos inmediatos de `A`. |
| `A + B` | **Hermano adyacente** | El elemento `B` que va justo después de `A`. |
| `A ~ B` | **Hermano general** | Todos los elementos `B` que sigan a `A`, siempre que compartan padre. |

#### Ejemplo de Código:

```css
/* Selecciona todos los <p> dentro de un <article> */
article p { color: gray; }

/* Selecciona solo los <li> que son hijos directos de un <ul> */
ul > li { list-style: square; }

/* El párrafo que va justo después de un h2 tendrá más margen arriba */
h2 + p { margin-top: 30px; }

/* Todos los párrafos que sigan a una imagen (dentro del mismo contenedor) */
img ~ p { font-style: italic; }

```

---

### 2. Selectores de Atributo

Permiten seleccionar elementos basándose en la presencia o el valor de sus atributos HTML. Son extremadamente potentes para interfaces dinámicas.

* **`[attr]`**: Tiene el atributo (da igual el valor).
* **`[attr="val"]`**: El valor es exactamente "val".
* **`[attr^="val"]`**: El valor **empieza** por "val".
* **`[attr$="val"]`**: El valor **termina** por "val".
* **`[attr*="val"]`**: El valor **contiene** "val" en cualquier parte.

#### Ejemplo de Código (Casos Reales):

```css
/* Pone un icono de candado a los enlaces seguros */
a[href^="https"] { color: green; }

/* Estiliza todos los inputs de tipo "submit" y "button" */
input[type="submit"] { cursor: pointer; }

/* Selecciona enlaces a archivos PDF (terminan en .pdf) */
a[href$=".pdf"]::after { content: " (PDF)"; color: red; }

/* Selecciona elementos que contienen la palabra "error" en su clase */
[class*="error"] { border: 2px dashed red; }

```

---

### 3. Pseudo-clases Estructurales

Permiten seleccionar elementos según su posición en el documento sin añadir clases extra como `.first` o `.last`.

* **`:first-child` / `:last-child**`: El primer o último hijo de su padre.
* **`:nth-child(n)`**: El hijo número `n`.
* **`:nth-of-type(n)`**: El elemento número `n` de ese tipo específico.
* **`:not(selector)`**: Selecciona todo lo que **no** coincida con el selector.

#### Ejemplo de Código:

```css
/* Cebra en una tabla: filas pares */
tr:nth-child(even) { background-color: #f2f2f2; }

/* Primera letra de una lista de nombres */
li:first-child { font-weight: bold; }

/* Todos los párrafos EXCEPTO los que tengan la clase .intro */
p:not(.intro) { font-size: 0.9em; }

/* El tercer párrafo dentro de un div (útil para maquetación editorial) */
p:nth-of-type(3) { color: darkblue; }

```

---

### 4. Pseudo-elementos

A diferencia de las pseudo-clases (que seleccionan estados), los pseudo-elementos seleccionan o crean **partes** específicas de un elemento.

* **`::before` / `::after**`: Crea contenido "falso" antes o después del contenido del elemento. **Requiere la propiedad `content**`.
* **`::first-line` / `::first-letter**`: Estiliza la primera línea o letra de un bloque.
* **`::selection`**: Estiliza el texto cuando el usuario lo subraya con el ratón.

#### Ejemplo de Código:

```css
/* Añade una comilla decorativa antes de cada cita */
blockquote::before {
    content: "“";
    font-size: 4em;
    color: #ccc;
}

/* Letra capital (estilo periódico) */
p::first-letter {
    font-size: 3em;
    float: left;
    margin-right: 8px;
}

/* Cambiar el color de resaltado al seleccionar texto */
::selection {
    background: #007f5f;
    color: white;
}

```

---

### 5. Pseudo-clases de Estado (Interacción)

Fundamentales en el **Diseño de Interfaces** para dar feedback al usuario.

* **`:hover`**: Ratón encima.
* **`:focus`**: Elemento seleccionado (teclado o clic en input).
* **`:disabled`**: Elementos de formulario desactivados.
* **`:checked`**: Checkbox o radio seleccionado.

#### Ejemplo de Código:

```css
/* Efecto de foco en inputs para accesibilidad */
input:focus {
    outline: 2px solid #007f5f;
    background-color: #eefdf9;
}

/* Cambiar el estilo de un label cuando su checkbox está marcado */
input:checked + label {
    font-weight: bold;
    text-decoration: underline;
}

```

---

### Resumen de "Buenas Prácticas"

1. **No abuses de los selectores descendientes (`A B`)**: Si la estructura es muy profunda, el navegador tarda más en procesarla. Intenta ser específico.
2. **Usa `::before` y `::after` para decoración**: No ensucies el HTML con `<span>` vacíos solo para poner iconos o adornos.
3. **La accesibilidad es clave**: Usa siempre `:focus` junto a `:hover`. Si un usuario navega con el teclado, necesita saber dónde está.

---

## Posicionamiento clásico en CSS

Antes de mover cajas por la pantalla, debemos entender una regla fundamental de HTML: **El Flujo Normal del Documento**.
Por defecto, el navegador lee el HTML de arriba a abajo. Los elementos de bloque (como `<div>` o `<p>`) se apilan uno debajo del otro, y los elementos en línea (como `<span>` o `<a>`) se colocan uno al lado del otro.

La propiedad `position` de CSS nos permite alterar este flujo. Para mover los elementos, usamos las coordenadas: `top`, `bottom`, `left` y `right`.

---

### 1. `position: static` (comportamiento por defecto)

Todos los elementos en HTML son `static` por defecto.

* **Cómo funciona:** El elemento sigue el flujo normal del documento.
* **Limitación clave:** Las propiedades `top`, `right`, `bottom`, `left` y `z-index` **NO tienen ningún efecto** sobre un elemento estático.

**Ejemplo de código:**

```css
.caja-normal {
    position: static;
    top: 50px; /*El navegador ignorará esto por completo */
    background-color: lightgray;
}

```

---

## 2. `position: relative` (El pariente tranquilo)

Aquí empieza la magia. Un elemento relativo sigue en el flujo normal, pero **se puede mover respecto a su posición original**.

* **La clave para el alumno:** Cuando mueves un elemento relativo, este deja un "fantasma" o espacio vacío donde originalmente estaba. Los elementos que lo rodean no se inmutan; no ocupan su lugar.
* **Uso principal:** Para pequeños ajustes visuales o, más importante aún, para servir de ancla a los elementos absolutos (lo veremos en el siguiente punto).

**Ejemplo de código:**

```html
<style>
    .caja-relativa {
        position: relative;
        top: 20px;  /* Baja 20px desde donde DEBERÍA estar */
        left: 30px; /* Se mueve 30px a la derecha */
        background-color: #3498db;
        color: white;
    }
</style>

<div>Caja 1 (Estática)</div>
<div class="caja-relativa">Caja 2 (Se mueve, pero su hueco original sigue ahí)</div>
<div>Caja 3 (Estática, no sube a ocupar el hueco de la Caja 2)</div>

```

---

## 3. `position: absolute` (El rebelde sin causa)

Este es el concepto que más cuesta asimilar. Un elemento absoluto **es arrancado del flujo normal del documento**.

* **La clave para el alumno:** Al ser arrancado, no deja ningún "fantasma". Es como si desapareciera para los demás elementos, que subirán a ocupar su lugar.
* **¿Respecto a qué se mueve?** Se mueve (con `top`, `left`, etc.) respecto a su **ancestro posicionado más cercano**. Si no encuentra ninguno, se moverá respecto al `<body>` (la ventana completa).

### La Regla de Oro: "Padre Relativo, Hijo Absoluto"

Para controlar un elemento absoluto y que no se escape volando por toda la pantalla, debemos "encerrarlo". Para ello, le damos al contenedor padre un `position: relative`.

**Ejemplo de código (Creando una etiqueta de "Oferta" en una tarjeta):**

```html
<style>
    /* 1. El contenedor actúa como ancla (Relative) */
    .tarjeta-producto {
        position: relative; 
        width: 200px;
        height: 300px;
        background-color: #ecf0f1;
        border: 1px solid #bdc3c7;
    }

    /* 2. El hijo se mueve libremente DENTRO de la tarjeta (Absolute) */
    .etiqueta-oferta {
        position: absolute;
        top: 10px;  /* A 10px del borde superior de la tarjeta */
        right: -10px; /* Sobresale un poco por la derecha */
        background-color: #e74c3c;
        color: white;
        padding: 5px 10px;
    }
</style>

<div class="tarjeta-producto">
    <div class="etiqueta-oferta">-50%</div>
    <h3>Zapatillas Nike</h3>
    <p>Precio: 50€</p>
</div>

```

---

## 4. `position: fixed` (El vigilante inamovible)

Muy similar al absoluto (también es arrancado del flujo y no deja hueco), pero con una diferencia radical: **siempre se posiciona respecto a la ventana del navegador (viewport)**.

* **La clave para el alumno:** Aunque el usuario haga scroll infinito hacia abajo, el elemento `fixed` se quedará clavado en la misma posición de la pantalla.
* **Uso principal:** Menús de navegación superiores que te persiguen, botones de "Volver arriba" o iconos de chat flotantes.

**Ejemplo de código (Botón flotante de ayuda):**

```html
<style>
    .boton-chat {
        position: fixed;
        bottom: 20px; /* Clavado a 20px del final de la pantalla */
        right: 20px;  /* Clavado a 20px de la derecha */
        background-color: #2ecc71;
        color: white;
        padding: 15px;
        border-radius: 50%;
        cursor: pointer;
    }
</style>

<div class="boton-chat">💬</div>

```

---

## 5. `position: sticky` (El híbrido moderno)

Es una mezcla mágica entre `relative` y `fixed`. El elemento se comporta como relativo (fluye normalmente) **hasta que haces scroll y llegas a su posición**. En ese momento, se "pega" a la pantalla y empieza a comportarse como `fixed`.

* **Limitación:** Necesita que se le defina un umbral (ej. `top: 0;`).
* **Uso principal:** Encabezados de listas alfabéticas (como la agenda del móvil) o menús secundarios que se pegan arriba al leer un artículo.

**Ejemplo de código:**

```html
<style>
    .titulo-pegajoso {
        position: sticky;
        top: 0; /* Cuando llegue al borde superior de la pantalla, se pega */
        background-color: #f39c12;
        padding: 10px;
        font-weight: bold;
    }
</style>

<div class="contenedor-texto">
    <p>Texto introductorio...</p>
    <div class="titulo-pegajoso">Sección Importante</div>
    <p>Mucho texto aquí...</p>
    <p>Sigue haciendo scroll y verás que el título naranja te persigue 
       hasta que termine su contenedor padre.</p>
</div>

```

---

## 6. El Eje Z (`z-index`): Controlando la profundidad

Al sacar elementos del flujo normal (con relative, absolute, fixed o sticky), es inevitable que se superpongan unos con otros. ¿Quién aparece encima de quién?

Para controlarlo usamos `z-index`. Funciona con números enteros (positivos o negativos).

* **El número mayor siempre gana (se pone por encima).**
* **OJO:** El `z-index` **SOLO funciona** en elementos que tengan un `position` distinto a `static`.

```css
.modal-fondo {
    position: fixed;
    z-index: 10; /* Se pone por encima del contenido normal */
}

.modal-ventana {
    position: fixed;
    z-index: 20; /* Se pone por encima del fondo del modal */
}

```

---

### Resumen Rápido para la Pizarra

| Valor de `position` | ¿Se saca del flujo normal? | ¿Respecto a qué se mueve? |
| --- | --- | --- |
| **`static`** | NO | No se puede mover |
| **`relative`** | NO | Sí mismo (su posición original) |
| **`absolute`** | **SÍ** | El padre posicionado más cercano |
| **`fixed`** | **SÍ** | La ventana del navegador (Viewport) |
| **`sticky`** | NO (hasta hacer scroll) | Híbrido: Sí mismo ➔ Viewport |

---

¿Te gustaría que prepare un **Mini-Proyecto Clásico** antes de saltar a Flexbox? Podríamos proponerles diseñar la típica cabecera de Twitter/X: una imagen de portada, y encima (usando posicionamiento absoluto) la foto de perfil circular que se solapa entre la portada y el contenido. Es un ejercicio fantástico para afianzar "Padre Relativo, Hijo Absoluto".