---
icon: lucide/list-checks
title: "Unidad 15 — Ejercicios, glosario y recursos"
description: "Banco exhaustivo de 100 ejercicios prácticos de CSS de dificultad incremental organizados por unidades (U01 a U10), glosario técnico bilingüe y recursos oficiales."
modulo: "LMH (0373) / DIW (0615)"
unidad: 15
fecha: "2026-10-09"
---

# Unidad 15 · Ejercicios, glosario y recursos

Este tema recoge el banco central de ejercicios prácticos de CSS para los módulos de Lenguajes de Marcas (0373) y Diseño de Interfaces Web (0615). Está estructurado en tres bloques:

1. **Parte A · Banco de Ejercicios por Unidad (U01 – U10):** 100 ejercicios de dificultad incremental (10 retos por unidad, desde nivel básico hasta avanzado/experto), donde cada unidad introduce sus conceptos específicos y puede integrar técnicas de los temas anteriores.
2. **Parte B · Glosario Técnico (Español – Inglés):** Definiciones precisas de los términos más recurrentes en exámenes técnicos y especificaciones del W3C.
3. **Parte C · Recursos Oficiales y Fuentes de Profundización:** Especificaciones, herramientas de validación, plataformas de auditoría y guías de referencia.

> [!TIP]
> Todas las soluciones comentadas con código completo, explicaciones técnicas y errores habituales están disponibles en la unidad complementaria: **[15. Ejercicios: soluciones](15-ejercicios-soluciones.md)**.
> Se recomienda encarecidamente intentar resolver cada reto en código propio antes de consultar la solución.

---

## PARTE A · BANCO DE EJERCICIOS POR UNIDAD (U01 – U10)

### Unidad 01 — Fundamentos de CSS

Conceptos evaluados: sintaxis canónica, reglas y declaraciones, inclusión de estilos (`<link>`, `<style>`, `style=""`), `@import`, normalización y reseteo, orden de declaración, herencia de propiedades (`inherit`, `initial`, `unset`, `revert`), uso adecuado de la cascada y hojas alternativas.

#### U01.01 — Anatomía canónica y vinculación externa
* **Nivel:** Básico
* **Enunciado:** Dispones de un documento HTML básico que carece de estilos. Debes crear una hoja de estilos externa denominada `estilos.css` y vincularla correctamente mediante la etiqueta estándar `<link>`.
* **Código inicial:**
  ```html title="index.html"
  <!DOCTYPE html>
  <html lang="es">
  <head>
    <meta charset="UTF-8">
    <title>Fundamentos CSS</title>
  </head>
  <body>
    <h1>Titular Principal</h1>
    <p>Párrafo introductorio de prueba.</p>
  </body>
  </html>
  ```
* **Tarea:**
  1. Enlaza `estilos.css` en el `<head>` usando la relación adecuada y codificación estándar.
  2. En `estilos.css`, redacta una regla para `h1` que defina el color del texto en azul marino (`#003366`) y tipografía del sistema sin serifa.
  3. Identifica y comenta en el archivo CSS cada una de las partes de la regla: selector, bloque de declaraciones, propiedad, valor y declaración completa.
* **Pista:** La vinculación externa se realiza con `<link rel="stylesheet" href="...">`.

---

#### U01.02 — Refactorización y desacoplamiento de estilos
* **Nivel:** Básico
* **Enunciado:** Un desarrollador novato ha mezclado estilos en línea (`style=""`) y etiquetas `<style>` dentro del cuerpo del documento.
* **Código inicial:**
  ```html title="sucio.html"
  <body>
    <h2 style="color: red; font-size: 24px;">Ofertas del mes</h2>
    <style>
      p { color: gray; }
    </style>
    <p style="color: black; font-weight: bold;">Condiciones de compra aplicadas.</p>
  </body>
  ```
* **Tarea:**
  1. Elimina todos los atributos `style` en línea y la etiqueta `<style>` interna dentro del cuerpo.
  2. Crea una estructura desacoplada con clases semánticas (`.titulo-ofertas`, `.texto-condiciones`).
  3. Traslada todas las declaraciones a una hoja CSS externa limpia.
* **Pista:** El principio de separación de responsabilidades (SoC) exige mantener la estructura en el HTML y la presentación visual en el CSS.

---

#### U01.03 — Comentarios y legibilidad profesional
* **Nivel:** Básico
* **Enunciado:** Un fichero de estilos contiene comentarios en formatos erróneos importados de otros lenguajes de programación, lo que provoca que el analizador sintáctico de CSS ignore reglas legítimas.
* **Código inicial:**
  ```css title="errores-comentarios.css"
  // Estilos de la cabecera principal
  header {
    background-color: #f0f0f0;
    // padding interior
    padding: 20px;
  }
  # Cabecera secundaria
  h2 { color: #333; }
  ```
* **Tarea:**
  1. Corrige todos los comentarios para utilizar exclusivamente la sintaxis válida de CSS.
  2. Organiza el archivo creando secciones visuales comentadas según buenas prácticas (Bloque General, Bloque de Componentes).
* **Pista:** CSS solo admite comentarios de bloque delimitados por `/*` y `*/`.

---

#### U01.04 — Micro-reset universal moderno
* **Nivel:** Medio
* **Enunciado:** Los navegadores aplican por defecto márgenes y modelos de caja divergentes en elementos de bloque como `body`, `h1-h6`, `p` y `ul`.
* **Tarea:**
  1. Construye una regla con el selector universal `*` y sus pseudo-elementos (`*::before, *::after`) que establezca el modelo de caja universal en `box-sizing: border-box`.
  2. Elimina los márgenes por defecto de `body`, títulos (`h1`, `h2`, `h3`) y listas (`ul`, `ol`).
  3. Aplica al `body` una altura mínima de pantalla (`min-height: 100vh`) y un suavizado tipográfico adecuado.
* **Pista:** Resetear márgenes y fijar `box-sizing: border-box` previene desbordamientos horizontales inesperados.

---

#### U01.05 — Rendimiento de `@import` frente a `<link>`
* **Nivel:** Medio
* **Enunciado:** Una aplicación web enlaza un único archivo `main.css`, pero dentro de él se encadenan cuatro directivas `@import` para importar tipografías y módulos, generando un cuello de botella en la cascada de peticiones HTTP (efecto cascada síncrona).
* **Tarea:**
  1. Muestra la sintaxis canónica de `@import url(...)` dentro de un archivo CSS.
  2. Explica técnicamente por qué el navegador bloquea el renderizado al resolver `@import` anidados secuencialmente.
  3. Reescribe la carga en el `<head>` del HTML utilizando etiquetas `<link rel="stylesheet">` paralelas y optimizadas.
* **Pista:** Los navegadores descargan múltiples etiquetas `<link>` en paralelo, mientras que `@import` requiere descargar y parsear el archivo padre antes de iniciar la descarga del hijo.

---

#### U01.06 — Herencia natural frente a `inherit` explícito
* **Nivel:** Medio
* **Enunciado:** Se desea que los campos de formulario (`input`, `button`, `select`, `textarea`) utilicen la misma tipografía (`font-family`) y color de texto que el resto del contenedor padre, pero por defecto los navegadores les asignan estilos de interfaz del sistema operativo (User Agent Stylesheet).
* **Tarea:**
  1. Identifica qué propiedades CSS se heredan de padres a hijos por defecto (ej. tipografía, color) y cuáles no (ej. bordes, márgenes, paddings).
  2. Escribe una regla CSS que fuerce a todos los controles de formulario a heredar explícitamente `font-family`, `font-size` y `color` del contenedor mediante el valor `inherit`.
* **Pista:** `font-family: inherit` y `color: inherit` neutralizan los estilos nativos del agente de usuario.

---

#### U01.07 — Palabras clave universales: `inherit`, `initial`, `unset` y `revert`
* **Nivel:** Medio
* **Enunciado:** Tienes una tarjeta con un botón que ha recibido estilos globales indeseados. Debes demostrar la diferencia práctica entre las cuatro palabras clave globales de valor en CSS aplicadas sobre una propiedad como `color` o `border`.
* **Tarea:**
  1. Redacta cuatro clases (`.btn-inherit`, `.btn-initial`, `.btn-unset`, `.btn-revert`).
  2. Explica qué valor adopta cada una y qué diferencia existe entre `initial` (valor de la especificación W3C) y `revert` (valor de la hoja del navegador o cascada previa).
* **Pista:** Para propiedades heredadas, `unset` equivale a `inherit`; para no heredadas, equivale a `initial`.

---

#### U01.08 — Resolución de conflictos por orden de declaración
* **Nivel:** Medio
* **Enunciado:** Dos reglas con exactamente la misma especificidad colisionan sobre el mismo elemento `p.destacado`.
* **Código inicial:**
  ```css title="conflicto.css"
  p.destacado {
    color: green;
    font-size: 18px;
  }
  p.destacado {
    color: orange;
  }
  ```
* **Tarea:**
  1. Determina cuál será el color final del texto y cuál el tamaño de fuente.
  2. Justifica el resultado basándote en las fases del algoritmo de la Cascada de CSS.
  3. Demuestra qué ocurre si los estilos provienen de dos archivos `<link>` externos distintos cargados en distinto orden en el `<head>`.
* **Pista:** A igualdad de especificidad y origen, la regla que se procesa en último lugar en el flujo de lectura es la que prevalece.

---

#### U01.09 — Desactivación de `!important` y reestructuración limpia
* **Nivel:** Avanzado
* **Enunciado:** En un proyecto legacy, un desarrollador utilizó `color: red !important;` en un selector genérico, impidiendo que los botones secundarios puedan cambiar de color en sus estados.
* **Código inicial:**
  ```css title="legacy-important.css"
  .btn {
    background-color: blue !important;
    color: white !important;
  }
  .btn-secundario {
    background-color: gray;
    color: black;
  }
  ```
* **Tarea:**
  1. Explica técnicamente cómo altera `!important` la fase de origen e importancia de la cascada.
  2. Refactoriza el código eliminando por completo todas las directivas `!important`.
  3. Asegura que `.btn-secundario` sobrescriba a `.btn` mediante especificidad limpia o composición de clases semánticas.
* **Pista:** El uso de `!important` rompe el flujo natural de la cascada y crea deuda técnica. Debe sustituirse por selectores de mayor especificidad o mejor arquitectura.

---

#### U01.10 — Hojas de estilo alternativas para accesibilidad
* **Nivel:** Avanzado
* **Enunciado:** Para cumplir con normativas de accesibilidad en entornos educativos, una página web debe ofrecer una hoja de estilo estándar y una hoja de estilo alternativa de "Alto Contraste" que el usuario pueda alternar en su navegador.
* **Tarea:**
  1. Configura el `<head>` del HTML con una hoja preferida y una hoja alternativa utilizando los atributos `rel="alternate stylesheet"` y `title`.
  2. Implementa en la hoja alternativa (`alto-contraste.css`) un esquema de fondo negro puro (`#000000`), textos en amarillo brillante (`#ffff00`) y enlaces subrayados en blanco (`#ffffff`).
* **Pista:** La especificación HTML permite declarar hojas alternativas con `title="Alto Contraste"` que navegadores y herramientas de apoyo pueden activar.

---

### Unidad 02 — Selectores y especificidad

Conceptos evaluados: selectores básicos y universales, combinadores de descendencia, hijo (`>`), hermano adyacente (`+`) y hermano general (`~`), selectores de atributos, pseudo-clases de interacción y estructurales, pseudo-elementos (`::before`, `::after`), cálculo riguroso de especificidad `(I, A, B, C)`, pseudo-clases lógicas (`:is()`, `:where()`, `:not()`) y selector relacional (`:has()`). Integra conceptos de U01.

#### U02.01 — Selectores básicos y ámbito de aplicación
* **Nivel:** Básico
* **Enunciado:** En un portal de noticias, se requiere aplicar estilos diferenciados al título del sitio (único), a las cabeceras de los artículos (múltiples) y a los párrafos de entradilla.
* **Tarea:**
  1. Utiliza un selector de ID para el logotipo/título principal de la web.
  2. Utiliza un selector de clase para todas las tarjetas de noticia (`.noticia`).
  3. Utiliza un selector de tipo combinado con clase para resaltar únicamente los párrafos de resumen (`p.resumen`).
* **Pista:** Los IDs son únicos por documento; las clases son reutilizables y componibles.

---

#### U02.02 — Combinador hijo directo (`>`) frente a descendiente (` `)
* **Nivel:** Básico
* **Enunciado:** Un menú de navegación multinivel con submenús desplegables sufre un problema: al estilizar los elementos de lista del menú principal, los estilos se heredan en cascada indeseadamente a los submenús anidados.
* **Código inicial:**
  ```html title="menu.html"
  <nav class="menu-principal">
    <ul>
      <li><a href="#">Inicio</a></li>
      <li>
        <a href="#">Cursos</a>
        <ul class="submenu">
          <li><a href="#">DAW</a></li>
          <li><a href="#">DAM</a></li>
        </ul>
      </li>
    </ul>
  </nav>
  ```
* **Tarea:**
  1. Utiliza el combinador hijo directo (`>`) para aplicar un borde inferior y tamaño de letra grande solo a los enlaces de primer nivel.
  2. Asegúrate de que los enlaces dentro de `.submenu` mantengan un tamaño más pequeño y sin borde.
* **Pista:** `nav > ul > li > a` solo selecciona los hijos directos inmediatos, ignorando las profundidades inferiores.

---

#### U02.03 — Combinadores de hermanos: adyacente (`+`) y general (`~`)
* **Nivel:** Medio
* **Enunciado:** En un artículo de blog se desea que:
  a) El primer párrafo que aparece inmediatamente después de un `h2` tenga una tipografía más grande (párrafo líder).
  b) Si un formulario muestra un mensaje de advertencia con la clase `.alerta-error`, todos los inputs siguientes queden marcados con un borde rojo.
* **Tarea:**
  1. Resuelve el caso (a) mediante el combinador de hermano adyacente (`+`).
  2. Resuelve el caso (b) mediante el combinador de hermano general (`~`).
* **Pista:** `A + B` selecciona a B si es inmediatamente consecutivo a A; `A ~ B` selecciona a todos los hermanos B que sigan a A aunque no sean inmediatamente adyacentes.

---

#### U02.04 — Selectores de atributos avanzados
* **Nivel:** Medio
* **Enunciado:** En una intranet universitaria existen enlaces a páginas internas, enlaces externos seguros, documentos PDF descargables y archivos comprimidos ZIP.
* **Tarea:**
  1. Selecciona todos los enlaces con `target="_blank"` y añade un indicador visual.
  2. Selecciona todos los enlaces cuyo `href` comience por `https://` (`[href^="https://"]`).
  3. Selecciona todos los enlaces que terminen en `.pdf` (`[href$=".pdf"]`) y muéstrales un icono representativo mediante CSS.
  4. Selecciona enlaces cuyo texto de destino contenga la palabra `examen` en cualquier parte del atributo (`[href*="examen"]`).
* **Pista:** Los operadores `^=`, `$=` y `*=` evalúan el inicio, fin y subcadena de cualquier atributo HTML.

---

#### U02.05 — Estados dinámicos de interfaz y foco accesible
* **Nivel:** Medio
* **Enunciado:** Diseña los estilos de un botón interactivo y accesible que responda a los estados de puntero y teclado: reposo, `:hover`, `:focus-visible`, `:active` y `:disabled`.
* **Tarea:**
  1. Define los colores de fondo para reposo, hover y active.
  2. Configura un contorno claro de enfoque accesible mediante `:focus-visible` (evitando que aparezca en clics de ratón pero manteniéndolo para navegación con tabulador).
  3. Estila el estado `:disabled` reduciendo la opacidad y aplicando `cursor: not-allowed`.
* **Pista:** Jamás utilices `outline: none` sin proporcionar una alternativa visible e inequívoca mediante `:focus` o `:focus-visible`.

---

#### U02.06 — Pseudo-clases estructurales y fórmulas `nth-child`
* **Nivel:** Medio
* **Enunciado:** En un catálogo de productos con 12 artículos, se necesita aplicar estilos específicos a posiciones clave de la rejilla.
* **Tarea:**
  1. Estila el primer elemento con `:first-child` y el último con `:last-child`.
  2. Aplica un fondo gris alterno a las filas pares mediante `:nth-child(even)` o fórmula matemática.
  3. Destaca cada tercer elemento de la serie mediante la expresión `:nth-child(3n)`.
  4. Explica la diferencia práctica entre `:nth-child(2)` y `:nth-of-type(2)` cuando se intercalan etiquetas `<h3>` y `<p>`.
* **Pista:** `:nth-child` cuenta elementos hermanos absolutos; `:nth-of-type` cuenta únicamente hermanos que comparten la misma etiqueta HTML.

---

#### U02.07 — Generación de contenido decorativo con `::before` y `::after`
* **Nivel:** Medio
* **Enunciado:** Se desea maquetar un bloque de cita (`<blockquote>`) con comillas tipográficas gigantes decorativas y una etiqueta "Nuevo" flotante en tarjetas sin agregar texto innecesario en el marcado HTML.
* **Tarea:**
  1. Añade comillas de apertura antes de la cita utilizando `blockquote::before` y la propiedad `content`.
  2. Aplica a un elemento `.badge-nuevo` un punto indicador animado o texto con `::after`.
  3. Asegura que los lectores de pantalla no interpreten el contenido puramente decorativo o protégelo semánticamente.
* **Pista:** Para que un pseudo-elemento `::before` o `::after` se dibuje en pantalla, la propiedad `content` es estrictamente obligatoria (incluso como cadena vacía `content: ""`).

---

#### U02.08 — Matriz de cálculo y ordenación de especificidad
* **Nivel:** Avanzado
* **Enunciado:** Dados los siguientes 5 selectores, calcula su puntuación exacta en el formato de 4 columnas `(Inline, ID, Clase/Atributo/Pseudo-clase, Elemento/Pseudo-elemento)` y ordénalos de menor a mayor prioridad en la cascada:
  * Selector A: `header nav.principal ul li a:hover`
  * Selector B: `#usuario-perfil .datos > span`
  * Selector C: `body main article p`
  * Selector D: `button[type="submit"]:not(:disabled)`
  * Selector E: `#alerta`
* **Tarea:**
  1. Desglosa los puntos de cada selector en su tupla numérica.
  2. Determina el orden estricto de precedencia.
  3. Explica por qué una regla con un único ID vence a una regla con 15 clases encadenadas.
* **Pista:** La especificidad no usa base decimal: un ID (columna B) jamás puede ser superado por acumulación de clases (columna C).

---

#### U02.09 — Pseudo-clases lógicas: `:is()`, `:where()` y `:not()`
* **Nivel:** Avanzado
* **Enunciado:** Simplifica un selector largo de cabeceras en diferentes secciones y demuestra el impacto en la especificidad al usar `:where()` frente a `:is()`.
* **Código inicial:**
  ```css title="largo.css"
  article h1, article h2, article h3,
  section h1, section h2, section h3,
  aside h1, aside h2, aside h3 {
    color: #1a1a1a;
  }
  ```
* **Tarea:**
  1. Reescribe el selector completo en una única línea compacta usando `:is()`.
  2. Reescribe la misma regla utilizando `:where()`.
  3. Calcula la especificidad de ambas versiones y explica por qué `:where()` es ideal para estilos base o resets de librerías.
* **Pista:** `:is()` adopta la especificidad del selector más pesado de su lista de argumentos; `:where()` tiene siempre especificidad cero `(0, 0, 0, 0)`.

---

#### U02.10 — El selector relacional padre `:has()`
* **Nivel:** Avanzado
* **Enunciado:** Utiliza CSS moderno sin JavaScript para:
  a) Aplicar un borde destacado y sombra a una tarjeta `.tarjeta` solo cuando contenga una imagen destacada `.tarjeta-img`.
  b) Cambiar el fondo de un formulario cuando alguno de sus checkboxes obligatorios esté marcado (`:checked`).
* **Tarea:**
  1. Implementa `.tarjeta:has(.tarjeta-img)` con estilos específicos.
  2. Implementa `form:has(input[type="checkbox"]:checked)`.
  3. Explica por qué `:has()` resolvió una limitación histórica de más de 20 años en CSS ("el selector de padre").
* **Pista:** `:has()` permite comprobar la presencia o estado de elementos descendientes o hermanos para condicionar el estilo del elemento seleccionado.

---

### Unidad 03 — Modelo de caja (Box Model)

Conceptos evaluados: componentes del modelo de caja (content, padding, border, margin), `box-sizing: content-box` vs `border-box`, colapso de márgenes verticales (hermanos, padre-hijo, elementos vacíos), márgenes automáticos y negativos, `outline` vs `border`, `box-shadow` (múltiple, inset) y control de desbordamiento (`overflow`). Integra conceptos de U01 y U02.

#### U03.01 — Cálculo analítico de dimensiones en `content-box`
* **Nivel:** Básico
* **Enunciado:** Un bloque tiene las siguientes declaraciones: `width: 320px`, `padding: 24px`, `border: 6px solid #333`, `margin: 30px`.
* **Tarea:**
  1. Calcula el ancho total real que ocupa la caja en pantalla en modo estándar `box-sizing: content-box`.
  2. Calcula el espacio total que reserva respecto a sus elementos vecinos teniendo en cuenta los márgenes.
  3. Comprueba el resultado mediante una fórmula matemática paso a paso.
* **Pista:** En `content-box`, el ancho total renderizado es `width + padding_izq + padding_der + border_izq + border_der`.

---

#### U03.02 — Prevención de rotura de layout con `border-box`
* **Nivel:** Básico
* **Enunciado:** Dos columnas colocadas una al lado de la otra tienen `width: 50%`. Al agregar `padding: 20px` y `border: 2px solid`, la segunda columna cae a la siguiente línea rompiendo el diseño.
* **Tarea:**
  1. Explica técnicamente por qué se produce el salto de línea con `content-box`.
  2. Resuelve el problema aplicando `box-sizing: border-box`.
  3. Demuestra cuánto mide el área de contenido interna disponible para el texto en cada columna.
* **Pista:** Con `border-box`, el `width` declarado representa el límite exterior del borde; el padding y el borde se descuentan del espacio interior.

---

#### U03.03 — Shorthand de padding y comportamiento en elementos en línea
* **Nivel:** Básico
* **Enunciado:** Se aplican márgenes y rellenos a un elemento `<span>` de texto para destacarlo como una etiqueta. Sin embargo, los márgenes verticales no desplazan a los párrafos vecinos y el fondo se solapa con las líneas superior e inferior.
* **Tarea:**
  1. Explica por qué los elementos de flujo en línea (`display: inline`) no respetan márgenes verticales ni alteran la altura de línea de la caja padre.
  2. Transforma el elemento a `display: inline-block`.
  3. Aplica un padding con la sintaxis shorthand de dos valores (`padding: vertical horizontal`) y márgenes laterales adecuados.
* **Pista:** Las cajas puramente inline generan rectángulos de línea que no empujan verticalmente a los bloques adyacentes.

---

#### U03.04 — Colapso de márgenes entre hermanos adyacentes
* **Nivel:** Medio
* **Enunciado:** Un titular `h2` tiene `margin-bottom: 30px` y el párrafo siguiente `p` tiene `margin-top: 20px`.
* **Tarea:**
  1. Calcula el espacio vertical exacto en píxeles que separará ambos elementos en la pantalla.
  2. Explica qué ocurriría si el párrafo tuviera `margin-top: 30px`, o si uno de los márgenes fuera negativo (`-10px`).
  3. Enuncia la regla universal del colapso de márgenes entre hermanos adyacentes en el flujo normal.
* **Pista:** Cuando dos márgenes verticales positivos colapsan, prevalece el valor mayor, no su suma. Si hay uno negativo, se resta del positivo mayor.

---

#### U03.05 — Colapso de margen padre-hijo y soluciones modernas
* **Nivel:** Medio
* **Enunciado:** Un contenedor `<div>` sin borde ni padding contiene como primer elemento un `<h1>` con `margin-top: 40px`. Al renderizar la página, el margen "escapa" del contenedor padre y desplaza a todo el `<div>` respecto a la parte superior de la página, en lugar de separar el título del borde superior del contenedor.
* **Tarea:**
  1. Explica las condiciones bajo las cuales colapsan los márgenes entre un contenedor padre y su primer/último hijo.
  2. Demuestra tres formas distintas de evitar este colapso (usando padding, borde o creando un contexto BFC con `display: flow-root`).
  3. Justifica por qué `display: flow-root` es la solución más limpia y semántica.
* **Pista:** `display: flow-root` crea un nuevo Block Formatting Context (BFC) sin efectos colaterales.

---

#### U03.06 — Centrado horizontal con márgenes automáticos
* **Nivel:** Medio
* **Enunciado:** Se requiere centrar horizontalmente en la pantalla un contenedor de contenido principal con un ancho máximo de 1000 píxeles.
* **Tarea:**
  1. Escribe la regla para `.contenedor` utilizando `max-width: 1000px` y las propiedades lógicas modernas de margen (`margin-inline: auto`).
  2. Explica qué ocurre cuando la ventana del navegador mide menos de 1000 píxeles.
  3. Añade un relleno lateral (`padding-inline`) para evitar que el texto toque los bordes físicos de la pantalla en dispositivos móviles.
* **Pista:** `margin-inline: auto` distribuye equitativamente el espacio sobrante disponible a izquierda y derecha.

---

#### U03.07 — Estilos de bordes y radios asimétricos
* **Nivel:** Medio
* **Enunciado:** Diseña una tarjeta de llamada a la acción (*callout*) que posea un borde izquierdo grueso de color corporativo (4px solid), bordes superior/derecho/inferior transparentes o tenues, y esquinas redondeadas asimétricas (solo la esquina superior-derecha e inferior-derecha redondeadas a 12px).
* **Tarea:**
  1. Utiliza propiedades específicas de borde o sintaxis shorthand para cada lado.
  2. Aplica `border-radius` utilizando la sintaxis de 4 valores en sentido de las agujas del reloj.
  3. Agrega estilos de contraste que armonicen con un fondo tenue.
* **Pista:** `border-radius: top-left top-right bottom-right bottom-left`.

---

#### U03.08 — `outline` frente a `border` en focos accesibles
* **Nivel:** Medio
* **Enunciado:** Al aplicar un borde de 3 píxeles en el estado `:hover` o `:focus` de un botón, toda la barra de herramientas "tiembla" o da un salto de 3 píxeles porque el borde altera el modelo de caja física.
* **Tarea:**
  1. Explica técnicamente por qué `border` altera la geometría del documento mientras que `outline` no afecta al flujo.
  2. Sustituye el borde de enfoque por `outline: 3px solid var(--color-focus)` junto con `outline-offset: 2px`.
  3. Explica las ventajas de `outline-offset` para personas con baja visión.
* **Pista:** El `outline` se dibuja fuera del modelo de caja sin alterar el tamaño del elemento ni empujar a sus hermanos.

---

#### U03.09 — Sistema de sombras multicapa con `box-shadow`
* **Nivel:** Avanzado
* **Enunciado:** Las sombras simples de CSS con un único valor suelen verse artificiales y toscas. Los sistemas de diseño modernos construyen sombras realistas y suaves superponiendo varias capas y utilizando valores pequeños de desenfoque.
* **Tarea:**
  1. Crea una tarjeta elevada con una sombra suave compuesta por 3 capas en la misma declaración `box-shadow`.
  2. Crea una tarjeta de formulario hundida utilizando una sombra interior (`inset`).
  3. Detalla el significado de los 5 parámetros de `box-shadow: x y blur spread color`.
* **Pista:** Se pueden declarar múltiples sombras separadas por comas dentro de una única propiedad `box-shadow`.

---

#### U03.10 — Gestión de desbordamiento (`overflow`) y prevención de scrollbars parásitas
* **Nivel:** Avanzado
* **Enunciado:** Un panel de notificaciones contiene texto largo o nombres de usuario sin espacios que desbordan el ancho asignado, generando una barra de desplazamiento horizontal no deseada en toda la página web.
* **Tarea:**
  1. Configura el panel con `overflow-x: hidden` y `overflow-y: auto` para permitir únicamente el scroll vertical cuando el contenido supere una altura máxima (`max-height: 300px`).
  2. Aplica la propiedad CSS para forzar la división de palabras largas que no contienen guiones (`overflow-wrap: break-word` o `word-break: break-all`).
  3. Personaliza el comportamiento de desplazamiento fluido con `overscroll-behavior: contain`.
* **Pista:** `overscroll-behavior: contain` evita que el scroll del panel secundario continúe desplazando la página principal al llegar al tope.

---

### Unidad 04 — Posicionamiento y z-index

Conceptos evaluados: flujo normal (`static`), posicionamiento relativo (`relative`), absoluto (`absolute`), fijo (`fixed`), adhesivo (`sticky`), propiedades lógicas (`inset`), orden de apilamiento, contextos de apilamiento (*stacking contexts*), regla de `z-index`, trampas de `transform`/`filter` y encapsulación con `isolation: isolate`. Integra U01–U03.

#### U04.01 — Posicionamiento relativo y conservación del espacio físico
* **Nivel:** Básico
* **Enunciado:** Se desea desplazar un icono 8 píxeles hacia abajo y 4 hacia la derecha para alinearlo visualmente con un texto, sin alterar la posición de ningún elemento circundante.
* **Tarea:**
  1. Aplica `position: relative` junto con `top` y `left`.
  2. Demuestra que el espacio original que ocupaba el elemento en el flujo del documento se mantiene intacto.
  3. Explica la diferencia entre desplazar un elemento con `position: relative` frente a desplazarlo con `margin`.
* **Pista:** Un elemento con `position: relative` se desplaza visualmente respecto a su propia posición natural en el flujo sin mover a sus hermanos.

---

#### U04.02 — Posicionamiento absoluto y búsqueda del bloque contenedor
* **Nivel:** Básico
* **Enunciado:** Un botón de cierre con forma de "X" debe posicionarse en la esquina superior derecha de una tarjeta de alerta. Al aplicar `position: absolute; top: 10px; right: 10px;`, el botón vuela a la esquina superior derecha de la ventana del navegador.
* **Tarea:**
  1. Explica el algoritmo que sigue el navegador para encontrar el bloque contenedor (*containing block*) de un elemento absoluto.
  2. Corrige el problema aplicando `position: relative` a la tarjeta `.alerta`.
  3. Posiciona la "X" de forma exacta en la esquina interior de la tarjeta.
* **Pista:** Si ningún ancestro tiene una posición distinta de `static`, el bloque contenedor es el viewport inicial del documento (Initial Containing Block).

---

#### U04.03 — Tarjeta de comercio electrónico con badge flotante
* **Nivel:** Medio
* **Enunciado:** Construye una tarjeta de producto que contenga una imagen, título, precio y un badge de "Oferta -20%" que flote sobre la imagen en la esquina superior izquierda, sobresaliendo ligeramente de la tarjeta.
* **Tarea:**
  1. Estructura el marcado HTML semántico de la tarjeta.
  2. Aplica posicionamiento absoluto al badge con coordenadas negativas controladas (`top: -8px; left: -8px;`).
  3. Añade una pequeña sombra para conferir profundidad al badge sobre la imagen.
* **Pista:** Las coordenadas negativas permiten hacer sobresalir elementos fuera de los bordes del bloque contenedor.

---

#### U04.04 — Cabecera fija persistente con compensación de espacio
* **Nivel:** Medio
* **Enunciado:** Se requiere una barra de navegación superior que permanezca siempre visible al hacer scroll por la página (`position: fixed`). Al aplicarla, la cabecera tapa los primeros párrafos de contenido del sitio.
* **Tarea:**
  1. Declara la cabecera con `position: fixed; top: 0; left: 0; width: 100%;` (o usando `inset`).
  2. Explica por qué el contenido de la página queda oculto debajo de la cabecera al pasar a `fixed`.
  3. Resuelve el problema aplicando un `padding-top` compensatorio al elemento `<body>` o `<main>`.
* **Pista:** Los elementos con `position: fixed` salen por completo del flujo normal, por lo que el resto de elementos ocupan su lugar físico original.

---

#### U04.05 — Cabeceras adhesivas con `position: sticky`
* **Nivel:** Medio
* **Enunciado:** En una guía telefónica o lista de contactos agrupados alfabéticamente ("A", "B", "C"...), cada letra de encabezado debe hacer scroll normal hasta llegar al borde superior de la pantalla y permanecer fijada mientras el usuario lee los contactos de dicha letra, soltándose cuando entra la siguiente letra.
* **Tarea:**
  1. Aplica `position: sticky; top: 0;` a los encabezados de grupo.
  2. Detalla los 3 requisitos estrictos para que `sticky` funcione correctamente (ancestro sin `overflow: hidden`, altura del contenedor padre superior al elemento sticky, y coordenada de activación declarada).
* **Pista:** Un elemento `sticky` solo se fija dentro de los límites físicos de su elemento contenedor padre directo.

---

#### U04.06 — Propiedades lógicas de posicionamiento con `inset`
* **Nivel:** Medio
* **Enunciado:** Un modal a pantalla completa o superposición de fondo (*backdrop*) debe cubrir todo el viewport. En lugar de escribir cuatro declaraciones individuales (`top: 0; right: 0; bottom: 0; left: 0;`), refactoriza utilizando la propiedad moderna `inset`.
* **Tarea:**
  1. Escribe la regla de overlay usando `position: fixed; inset: 0;`.
  2. Demuestra el uso de `inset-block` e `inset-inline` para controlar márgenes en sistemas bidireccionales (LTR / RTL).
* **Pista:** `inset: 0` es la abreviatura canónica de `top: 0; right: 0; bottom: 0; left: 0;`.

---

#### U04.07 — Orden natural de apilamiento sin `z-index`
* **Nivel:** Medio
* **Enunciado:** Tres cajas coloreadas se superponen ligeramente mediante márgenes negativos. Ninguna de ellas tiene declarada la propiedad `z-index`.
* **Tarea:**
  1. Determina cuál de las cajas se dibuja por encima de las demás si todas tienen `position: static`.
  2. Determina qué ocurre si la primera caja tiene `position: relative` y las otras dos `position: static`.
  3. Enuncia la jerarquía de las 7 capas del orden de apilamiento de la especificación CSS2/CSS3.
* **Pista:** Cualquier elemento posicionado (distinto de static) se dibuja automáticamente por encima de los elementos no posicionados, con independencia del orden del DOM.

---

#### U04.08 — Diagnóstico de bugs de `z-index` y Stacking Context
* **Nivel:** Avanzado
* **Enunciado:** Un menú desplegable (*dropdown*) dentro de una cabecera tiene `z-index: 9999`, pero queda visualmente tapado por una imagen dentro de un banner principal que solo tiene `z-index: 2`.
* **Código inicial:**
  ```html title="dropdown-bug.html"
  <header class="cabecera">
    <nav class="dropdown">Menú desplegable (z-index: 9999)</nav>
  </header>
  <main class="hero">
    <img src="banner.jpg" class="imagen-hero" alt="Hero (z-index: 2)">
  </main>
  ```
  ```css title="dropdown-bug.css"
  .cabecera { position: relative; z-index: 1; }
  .dropdown { position: absolute; z-index: 9999; }
  .hero { position: relative; z-index: 2; }
  .imagen-hero { position: relative; z-index: 2; }
  ```
* **Tarea:**
  1. Explica técnicamente por qué el valor 9999 no puede ganar al valor 2 en este escenario (concepto de contextos de apilamiento padres).
  2. Corrige el fallo modificando los niveles de apilamiento de los contenedores raíz sin utilizar números mágicos.
* **Pista:** Los `z-index` de hijos pertenecientes a contextos de apilamiento diferentes se comparan a través de sus padres; si el padre A tiene menor z-index que el padre B, ningún hijo de A podrá superar a los hijos de B.

---

#### U04.09 — Efecto colateral de `transform` sobre elementos `fixed`
* **Nivel:** Avanzado
* **Enunciado:** Un diálogo modal con `position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;` se introduce dentro de una tarjeta que tiene una animación con `transform: scale(1.05)`. El modal deja de ocupar la pantalla completa y queda confinado dentro de los límites de la pequeña tarjeta.
* **Tarea:**
  1. Explica por qué propiedades como `transform`, `filter` o `perspective` convierten al elemento en bloque contenedor de los elementos hijos con `position: fixed`.
  2. Propón dos soluciones arquitectónicas (patrón Portal al `body` o extracción de la transformación fuera del contenedor del modal).
* **Pista:** La especificación de CSS Transforms estipula que cualquier elemento con `transform` distinto de `none` actúa como bloque contenedor de descendientes `fixed` y `absolute`.

---

#### U04.10 — Aislamiento de capas con `isolation: isolate`
* **Nivel:** Avanzado
* **Enunciado:** Un componente de interfaz complejo (ej. tarjeta interactiva con tooltip flotante) utiliza varios niveles de `z-index` locales (`1`, `2`, `5`). Se desea garantizar que ningún estilo interno de la tarjeta pueda interferir o desbordar la escala de capas global de la aplicación.
* **Tarea:**
  1. Aplica la propiedad moderna `isolation: isolate` al contenedor raíz del componente.
  2. Explica qué significa crear un nuevo contexto de apilamiento sin necesidad de usar `position` ni `z-index`.
  3. Define una escala de tokens de `z-index` en variables CSS globales (`--z-base`, `--z-header`, `--z-modal`, `--z-toast`).
* **Pista:** `isolation: isolate` crea un nuevo Stacking Context local de manera segura y atómica.

---

### Unidad 05 — Flexbox

Conceptos evaluados: contenedor flex y ejes (principal y cruzado), `flex-direction`, `flex-wrap`, alineaciones (`justify-content`, `align-items`, `align-content`, `align-self`), propiedades de los ítems (`flex-grow`, `flex-shrink`, `flex-basis`, shorthand `flex`), `order`, espaciado con `gap`, patrones: barra de navegación con espaciador automático, centrado absoluto, sticky footer y tarjetas de altura uniforme. Integra U01–U04.

#### U05.01 — Contenedor flex y anatomía de ejes
* **Nivel:** Básico
* **Enunciado:** Dispones de una lista desordenada `<ul>` con 4 elementos `<li>`. Por defecto se muestran apilados verticalmente como elementos de bloque.
* **Tarea:**
  1. Convierte la lista en un contenedor flex en fila horizontal.
  2. Identifica cuál es el eje principal (*main axis*) y cuál el eje cruzado (*cross axis*) en este estado.
  3. Cambia la dirección a columnas inversas (`flex-direction: column-reverse`) y explica cómo se reorientan los ejes.
* **Pista:** Con `flex-direction: row`, el eje principal es horizontal (izquierda a derecha en LTR); con `column`, pasa a ser vertical.

---

#### U05.02 — Distribución en el eje principal con `justify-content`
* **Nivel:** Básico
* **Enunciado:** Una barra de acciones secundarias contiene tres botones. Se debe mostrar cómo cambia su distribución utilizando los diferentes valores de `justify-content`.
* **Tarea:**
  1. Crea ejemplos visuales de `flex-start`, `center`, `flex-end`, `space-between`, `space-around` y `space-evenly`.
  2. Explica la diferencia matemática exacta de distribución de espacio entre `space-between` (extremos pegados a bordes), `space-around` (medio espacio en extremos) y `space-evenly` (espacio idéntico en todos los huecos).
* **Pista:** `justify-content` reparte el espacio libre sobrante a lo largo del eje principal.

---

#### U05.03 — Alineación en el eje cruzado con `align-items`
* **Nivel:** Básico
* **Enunciado:** Una fila de elementos contiene un avatar circular de 40px, un bloque de texto de varias líneas y un botón de acción. Sus alturas son distintas.
* **Tarea:**
  1. Aplica `align-items: center` para centrar verticalmente todos los elementos de la fila.
  2. Demuestra el efecto de `align-items: stretch` (comportamiento por defecto) y de `align-items: baseline` (alineación de las líneas base tipográficas).
  3. Utiliza `gap: 16px` para separar los elementos sin recurrir a márgenes laterales individuales.
* **Pista:** `gap` en Flexbox simplifica el espaciado entre hijos directos sin generar márgenes sobrantes en el primer o último elemento.

---

#### U05.04 — El centrado perfecto bidimensional
* **Nivel:** Básico
* **Enunciado:** Centra una tarjeta de inicio de sesión de 350px tanto horizontal como verticalmente en el centro exacto de la pantalla del usuario.
* **Tarea:**
  1. Configura el contenedor padre (`body` o `.wrapper`) con `display: flex; justify-content: center; align-items: center; min-height: 100vh;`.
  2. Muestra la alternativa de centrado automático mediante `display: flex;` en el padre y `margin: auto;` en la tarjeta hija.
  3. Explica por qué `margin: auto` absorbe todo el espacio libre en ambos ejes dentro de un contenedor flex.
* **Pista:** En Flexbox, `margin: auto` en un flex item absorbe el espacio disponible tanto vertical como horizontalmente.

---

#### U05.05 — Barra de navegación con espaciador automático
* **Nivel:** Medio
* **Enunciado:** Diseña una barra de navegación que contenga a la izquierda el logotipo y tres enlaces de sección, y a la extrema derecha los botones de "Iniciar Sesión" y "Registro".
* **Código inicial:**
  ```html title="navbar.html"
  <nav class="navbar">
    <a href="#" class="logo">MiEmpresa</a>
    <a href="#">Productos</a>
    <a href="#">Servicios</a>
    <a href="#">Contacto</a>
    <a href="#" class="login">Entrar</a>
    <a href="#" class="registro">Registro</a>
  </nav>
  ```
* **Tarea:**
  1. Aplica `display: flex; align-items: center; gap: 1rem;`.
  2. Empuja el bloque de login y registro a la derecha sin usar `float`, sin `position: absolute` y sin wrappers adicionales, aplicando `margin-inline-start: auto` (o `margin-left: auto`) en el enlace `.login`.
* **Pista:** Un margen automático en un ítem flex consume todo el espacio libre disponible en esa dirección sobre el eje principal.

---

#### U05.06 — Envoltura elástica y separación multilínea con `flex-wrap`
* **Nivel:** Medio
* **Enunciado:** Un listado de 20 etiquetas de categorías (*tags*) de diferentes longitudes debe mostrarse horizontalmente, pero cuando la pantalla no tenga suficiente ancho, las etiquetas deben pasar ordenadamente a la siguiente línea sin desbordar la pantalla.
* **Tarea:**
  1. Configura el contenedor con `flex-wrap: wrap` y define `gap: 8px 12px` (separación vertical y horizontal).
  2. Aplica a cada etiqueta estilos de botón redondeado con relleno accesible.
  3. Explica la diferencia entre `align-items` (alineación de ítems dentro de su propia línea) y `align-content` (distribución de las múltiples líneas de la cuadrícula flex).
* **Pista:** `align-content` solo tiene efecto cuando hay múltiples líneas (`flex-wrap: wrap`) y sobra espacio vertical en el contenedor.

---

#### U05.07 — El trío `flex-grow`, `flex-shrink` y `flex-basis`
* **Nivel:** Medio
* **Enunciado:** Se tienen tres columnas en un panel de control: una barra lateral, un área de contenido y un panel de widgets.
* **Tarea:**
  1. Define la barra lateral con tamaño fijo base de 240px que no deba encogerse ni crecer (`flex: 0 0 240px`).
  2. Define el área de contenido para que ocupe todo el espacio sobrante disponible (`flex: 1 1 0%` o `flex: 1`).
  3. Define el panel de widgets con base de 300px que pueda encogerse si el espacio disminuye pero no crecer más allá de su base (`flex: 0 1 300px`).
  4. Detalla la diferencia entre `flex-basis: 0` y `flex-basis: auto`.
* **Pista:** `flex: 1` expande el elemento repartiendo el espacio disponible a partir de una base cero; `flex: auto` reparte el espacio considerando el contenido previo.

---

#### U05.08 — Patrón de pie de página pegajoso (*Sticky Footer*)
* **Nivel:** Medio
* **Enunciado:** En páginas web con muy poco contenido de texto, el pie de página (`footer`) sube visualmente hasta la mitad de la pantalla, dejando un antiestético hueco en blanco debajo.
* **Tarea:**
  1. Configura `body` con `min-height: 100vh; display: flex; flex-direction: column;`.
  2. Aplica `flex: 1;` al elemento `<main>` para que crezca y empuje el `<footer>` al fondo de la ventana, independientemente de la cantidad de texto que contenga.
  3. Asegura que cuando la página tenga mucho contenido, el pie se desplace de forma natural al final del scroll.
* **Pista:** Con `flex-grow: 1` en el contenedor principal vertical, este absorbe cualquier espacio vertical remanente del viewport.

---

#### U05.09 — Reordenación visual con `order` y accesibilidad
* **Nivel:** Avanzado
* **Enunciado:** En una vista de escritorio, una barra lateral de filtros aparece visualmente a la izquierda y el listado de resultados a la derecha. Sin embargo, en el DOM y para lectores de pantalla, el listado de resultados debe leerse antes que los filtros.
* **Tarea:**
  1. Estructura el HTML colocando primero `<main>` y después `<aside>`.
  2. Utiliza la propiedad `order` de Flexbox para colocar visualmente el `<aside>` en primer lugar (`order: -1`).
  3. Explica los riesgos de accesibilidad cuando el orden visual difiere del orden de foco del tabulador (criterio WCAG 1.3.2 y 2.4.3).
* **Pista:** `order` solo cambia el dibujo visual en pantalla; la navegación por teclado y los lectores de pantalla siguen el orden del marcado HTML.

---

#### U05.10 — Tarjetas de contenido con botones alineados al fondo
* **Nivel:** Avanzado
* **Enunciado:** En una fila de 3 tarjetas de producto, cada tarjeta contiene un título, un párrafo de descripción de longitud muy variable y un botón "Comprar". Debido a los diferentes textos, los botones "Comprar" quedan a diferentes alturas desalineados, produciendo un aspecto descuidado.
* **Tarea:**
  1. Convierte cada tarjeta en un contenedor flex vertical (`display: flex; flex-direction: column;`).
  2. Aplica `margin-top: auto` al botón final de cada tarjeta (o `flex-grow: 1` a la descripción).
  3. Demuestra cómo todos los botones quedan milimétricamente alineados en la base de la fila de tarjetas sin importar cuántas líneas tenga cada párrafo.
* **Pista:** En un flex container vertical, `margin-top: auto` en el último hijo absorbe el espacio vertical sobrante de la tarjeta empujándolo al borde inferior.

---

### Unidad 06 — CSS Grid

Conceptos evaluados: contenedor bidimensional, pistas (`grid-template-columns`, `grid-template-rows`), unidad fraccionaria `fr`, funciones `repeat()` y `minmax()`, patrones elásticos (`auto-fit` vs `auto-fill`), `grid-template-areas`, colocación por líneas numéricas y spans, alineaciones bidimensionales, Bento Grid y `subgrid`. Integra U01–U05.

#### U06.01 — Cuadrícula básica bidimensional
* **Nivel:** Básico
* **Enunciado:** Se desea crear una cuadrícula simple de 3 columnas de 200px cada una y 2 filas de 150px para mostrar 6 tarjetas de iconos.
* **Tarea:**
  1. Aplica `display: grid` al contenedor.
  2. Define las columnas con `grid-template-columns: 200px 200px 200px;` y las filas con `grid-template-rows: 150px 150px;`.
  3. Añade un espacio de 16px entre celdas mediante la propiedad `gap`.
* **Pista:** CSS Grid controla de forma simultánea tanto las filas como las columnas (bidimensional), a diferencia de Flexbox que es unidimensional.

---

#### U06.02 — La unidad fraccionaria `fr` y `repeat()`
* **Nivel:** Básico
* **Enunciado:** Refactoriza una cuadrícula de 4 columnas iguales para que ocupe el 100% del ancho disponible sin importar el tamaño de la ventana y sin usar porcentajes rígidos.
* **Tarea:**
  1. Utiliza la unidad fraccionaria `fr` junto con la función `repeat()` (`repeat(4, 1fr)`).
  2. Explica qué representa exactamente una fracción `fr` del espacio sobrante disponible.
  3. Modifica una de las columnas para que mida `2fr` y comprueba cómo se reparte el espacio (1fr, 2fr, 1fr, 1fr).
* **Pista:** La unidad `fr` distribuye el espacio libre disponible una vez descontados los anchos fijos y los gaps.

---

#### U06.03 — Posicionamiento explícito por líneas numéricas
* **Nivel:** Medio
* **Enunciado:** En una cuadrícula de 3 columnas y 3 filas, una noticia destacada debe ocupar las dos primeras columnas y las dos primeras filas, mientras que el resto de noticias ocupan celdas individuales.
* **Tarea:**
  1. Escribe la regla para `.noticia-destacada` usando `grid-column-start: 1; grid-column-end: 3;` y `grid-row-start: 1; grid-row-end: 3;`.
  2. Simplifica las declaraciones usando los shorthands `grid-column: 1 / 3;` y `grid-row: 1 / 3;` (o con `span 2`).
  3. Comprende que las coordenadas de Grid hacen referencia a las líneas divisorias de la cuadrícula (1, 2, 3, 4), no a los números de celda.
* **Pista:** Una cuadrícula de 3 columnas tiene 4 líneas divisorias verticales.

---

#### U06.04 — Expansión a ancho completo con `grid-column: 1 / -1`
* **Nivel:** Medio
* **Enunciado:** En una cuadrícula donde el número de columnas puede variar según la resolución de pantalla, se necesita que un banner publicitario o separador ocupe siempre el 100% del ancho de la rejilla (desde la primera hasta la última columna disponible).
* **Tarea:**
  1. Declara en el banner `grid-column: 1 / -1;`.
  2. Explica qué significa el índice negativo `-1` en la numeración de líneas de CSS Grid.
  3. Señala en qué casos el índice `-1` no funciona (cuadrículas implícitas generadas automáticamente).
* **Pista:** `-1` hace referencia a la última línea explícita de la cuadrícula.

---

#### U06.05 — Maquetación semántica con `grid-template-areas`
* **Nivel:** Medio
* **Enunciado:** Diseña la estructura global de una página web (*Holy Grail Layout*) compuesta por: cabecera superior, barra lateral de navegación, contenido principal y pie de página inferior.
* **Código inicial:**
  ```html title="layout.html"
  <div class="app-layout">
    <header class="app-header">Cabecera</header>
    <nav class="app-nav">Navegación</nav>
    <main class="app-main">Contenido Principal</main>
    <footer class="app-footer">Pie</footer>
  </div>
  ```
* **Tarea:**
  1. Define en el contenedor `.app-layout` una plantilla visual con `grid-template-areas` de 2 columnas y 3 filas.
  2. Asigna cada elemento a su área correspondiente usando la propiedad `grid-area`.
  3. Utiliza la notación de punto `.` para dejar una celda vacía deliberadamente.
* **Pista:** La matriz textual en `grid-template-areas` debe tener el mismo número de celdas en cada fila para ser sintácticamente válida.

---

#### U06.06 — Rejilla responsiva elástica con `auto-fit` y `minmax()`
* **Nivel:** Medio
* **Enunciado:** Construye una galería de tarjetas que se adapte automáticamente a cualquier tamaño de pantalla: en pantallas grandes mostrará 4 o 5 columnas, en tablet 2 o 3, y en móvil 1 sola columna, sin escribir ninguna media query.
* **Tarea:**
  1. Implementa la regla: `grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));`.
  2. Añade `gap: 1.5rem;`.
  3. Añade la protección `min(260px, 100%)` para evitar desbordamientos en pantallas móviles con anchos inferiores a 260px.
* **Pista:** El patrón `repeat(auto-fit, minmax(min(260px, 100%), 1fr))` es el estándar de oro del diseño responsivo en CSS Grid.

---

#### U06.07 — Comparativa práctica: `auto-fit` frente a `auto-fill`
* **Nivel:** Medio
* **Enunciado:** En una pantalla ancha con espacio para 5 columnas de 200px, el usuario solo tiene 2 tarjetas cargadas en la base de datos.
* **Tarea:**
  1. Modela el comportamiento visual con `repeat(auto-fill, minmax(200px, 1fr))` y explica cómo reserva los huecos vacíos restantes.
  2. Modela el comportamiento con `repeat(auto-fit, minmax(200px, 1fr))` y explica cómo colapsa las pistas vacías a cero píxeles estirando las 2 tarjetas existentes para ocupar todo el ancho.
  3. Concluye cuál de las dos opciones es preferible según el tipo de componente.
* **Pista:** `auto-fill` mantiene los "slots" vacíos; `auto-fit` colapsa las pistas vacías permitiendo que los elementos existentes crezcan.

---

#### U06.08 — Alineación bidimensional integral en Grid
* **Nivel:** Avanzado
* **Enunciado:** Un panel de widgets de 800px x 600px contiene una cuadrícula de 2x2. Los widgets no ocupan todo el espacio asignado a sus celdas.
* **Tarea:**
  1. Alinea la cuadrícula entera en el centro del contenedor con `justify-content: center` y `align-content: center`.
  2. Alinea el contenido de todos los elementos dentro de sus celdas con `justify-items: center` y `align-items: center`.
  3. Modifica un widget individual para que se alinee a la esquina inferior derecha de su celda con `justify-self: end` y `align-self: end`.
* **Pista:** Las propiedades terminadas en `-content` alinean el conjunto de pistas en el contenedor; las terminadas en `-items` o `-self` alinean elementos dentro de sus celdas.

---

#### U06.09 — Cuadrícula asimétrica estilo "Bento Grid"
* **Nivel:** Avanzado
* **Enunciado:** Diseña una interfaz moderna tipo Bento Box de 4 columnas inspirada en dashboards de producto, con tarjetas de diferentes jerarquías:
  * Tarjeta principal: ocupa 2 columnas y 2 filas (`span 2 / span 2`).
  * Tarjeta secundaria alargada: ocupa 2 columnas y 1 fila (`span 2 / span 1`).
  * Dos tarjetas pequeñas cuadradas: ocupan 1 columna y 1 fila cada una.
* **Tarea:**
  1. Define la cuadrícula base con `grid-template-columns: repeat(4, 1fr)` y `grid-auto-rows: 180px`.
  2. Utiliza `grid-auto-flow: dense` para que el navegador rellene automáticamente cualquier hueco vacío con tarjetas posteriores.
  3. Estila las tarjetas con bordes suaves, fondo superficial y relleno interno.
* **Pista:** `grid-auto-flow: dense` optimiza el empaquetado del layout rellenando huecos vacíos.

---

#### U06.10 — Alineación de componentes hijos con `subgrid`
* **Nivel:** Avanzado
* **Enunciado:** Tienes una fila de 3 tarjetas en Grid. Cada tarjeta tiene una cabecera con título, un cuerpo de texto de tamaño variable y un pie con botones. En CSS normal, los títulos y pies de distintas tarjetas quedan desalineados entre sí porque cada tarjeta tiene su propio flujo independiente.
* **Tarea:**
  1. Configura el grid principal para que cada tarjeta ocupe 3 filas (`grid-row: span 3`).
  2. Declara en la tarjeta `.tarjeta`: `display: grid; grid-template-rows: subgrid;`.
  3. Comprueba cómo los 3 títulos, los 3 cuerpos y los 3 botones comparten exactamente las mismas líneas del grid padre quedando perfectamente alineados entre sí.
* **Pista:** `subgrid` permite que los elementos hijos hereden las pistas de su contenedor padre directo.

---

### Unidad 07 — Flujo normal, multicolumna, tablas y display

Conceptos evaluados: valores de `display` (`inline`, `block`, `inline-block`, `none`, `contents`), visibilidad y accesibilidad (`visibility: hidden` vs `.sr-only`), contexto de formato de bloque (BFC) con `flow-root`, columnas de texto editorial (`column-count`, `column-width`, `column-gap`, `column-rule`, `column-span`, `break-inside`), estilización accesible de tablas de datos (`border-collapse`, `caption-side`, `table-layout: fixed`, `font-variant-numeric: tabular-nums`). Integra U01–U06.

#### U07.01 — Comportamiento y diferencias de `block`, `inline` e `inline-block`
* **Nivel:** Básico
* **Enunciado:** Demuestra de forma práctica en un mismo archivo las tres diferencias fundamentales entre `display: block`, `display: inline` y `display: inline-block`.
* **Tarea:**
  1. Aplica ancho (`width`), alto (`height`), `margin-top` y `padding` a un elemento de cada tipo.
  2. Explica qué propiedades se aplican y cuáles se ignoran en cada valor de `display`.
  3. Resume en qué casos prácticos se debe usar `inline-block` frente a `inline`.
* **Pista:** `inline` no admite width/height ni márgenes verticales; `inline-block` admite dimensiones completas pero fluye en la misma línea de texto.

---

#### U07.02 — Ocultación visual y accesibilidad: `none` vs `hidden` vs `.sr-only`
* **Nivel:** Básico
* **Enunciado:** En un formulario accesible, un icono de lupa acompaña al campo de búsqueda, pero se requiere un texto descriptivo "Buscar en el catálogo" que no debe verse visualmente en pantalla pero sí debe ser leído por los lectores de pantalla.
* **Tarea:**
  1. Explica qué ocurre si aplicas `display: none;` (eliminado del árbol de accesibilidad y del layout).
  2. Explica qué ocurre si aplicas `visibility: hidden;` (oculto pero reservando su espacio en blanco).
  3. Implementa la clase utilitaria accesible `.sr-only` (*screen reader only*) utilizando la técnica canónica del clip rect y dimensiones de 1px.
* **Pista:** `display: none` oculta el elemento tanto para usuarios videntes como para tecnologías de asistencia.

---

#### U07.03 — Desenvoltura estructural con `display: contents`
* **Nivel:** Medio
* **Enunciado:** En un componente React o plantilla de servidor, una etiqueta intermedia `<div>` o `<form>` envuelve a un grupo de elementos, impidiendo que participen directamente como flex-items o grid-items de un contenedor exterior.
* **Tarea:**
  1. Aplica `display: contents` al elemento contenedor intermedio.
  2. Demuestra cómo el navegador ignora visualmente la caja intermedia y promociona a sus hijos directos para interactuar con el contenedor padre.
  3. Precaución: advierte sobre bugs históricos de accesibilidad en navegadores antiguos al aplicar `contents` sobre listas semánticas.
* **Pista:** `display: contents` hace desaparecer la caja generadora del elemento, manteniendo intactos a sus hijos en el árbol del DOM.

---

#### U07.04 — Creación de BFC con `display: flow-root`
* **Nivel:** Medio
* **Enunciado:** Un artículo contiene una imagen flotante (`float: left; width: 200px;`). El texto siguiente es tan corto que la imagen desborda por debajo de la tarjeta padre, haciendo que el pie de página suba y colisione con la imagen flotante (fallo clásico de desbordamiento de float).
* **Tarea:**
  1. Aplica `display: flow-root` al contenedor padre del artículo.
  2. Explica qué es un Block Formatting Context (BFC) y por qué contiene automáticamente a los elementos flotantes interiores.
  3. Compara `display: flow-root` con los antiguos hacks de clearfix (`::after { clear: both; }`) o `overflow: hidden`.
* **Pista:** `flow-root` crea un BFC nativo sin riesgo de recortar sombras o tooltips como ocurría con `overflow: hidden`.

---

#### U07.05 — Texto periodístico con multicolumna CSS
* **Nivel:** Medio
* **Enunciado:** Un artículo de opinión largo debe distribuirse en 3 columnas de lectura en escritorio, pero en pantallas pequeñas las columnas no deben estrecharse a menos de 250px cada una.
* **Tarea:**
  1. Utiliza la propiedad shorthand `columns: 3 250px;` (equivalente a `column-count: 3` y `column-width: 250px`).
  2. Explica cómo el navegador decide dinámicamente si mostrar 1, 2 o 3 columnas en función del ancho disponible sin necesidad de media queries.
* **Pista:** La propiedad `columns` combina un número máximo de columnas con un ancho mínimo deseado.

---

#### U07.06 — Personalización de separadores y gutters en multicolumna
* **Nivel:** Medio
* **Enunciado:** Mejora la presentación del artículo multicolumna añadiendo aireación y separación editorial visual entre los bloques de texto.
* **Tarea:**
  1. Ajusta la separación entre columnas con `column-gap: 2rem;`.
  2. Dibuja una línea vertical divisoria elegante con `column-rule: 1px solid var(--color-border);`.
  3. Muestra cómo se desglosa `column-rule` en ancho, estilo y color.
* **Pista:** `column-rule` se comporta como un borde, pero no ocupa espacio físico en el ancho total de las columnas.

---

#### U07.07 — Titulares transversales y control de cortes de párrafo
* **Nivel:** Avanzado
* **Enunciado:** Dentro del artículo multicolumna se introduce una cita destacada que debe cruzar a lo ancho de todas las columnas. Además, se detecta que las tarjetas con imágenes se parten feamente por la mitad entre la base de una columna y la parte superior de la siguiente.
* **Tarea:**
  1. Aplica `column-span: all;` a la cita para que interrumpa el flujo de columnas y ocupe el ancho completo.
  2. Aplica `break-inside: avoid;` a las tarjetas ilustradas para evitar que se fracturen entre dos columnas.
* **Pista:** `break-inside: avoid` garantiza la integridad visual de bloques dentro de sistemas multicolumna y modos de impresión.

---

#### U07.08 — Estilizado accesible de tablas de datos
* **Nivel:** Avanzado
* **Enunciado:** Maqueta una tabla de calificaciones académicas o catálogo de precios cumpliendo criterios rigurosos de accesibilidad y diseño limpio.
* **Tarea:**
  1. Aplica `border-collapse: collapse;` en el elemento `table`.
  2. Coloca y estila el elemento `<caption>` con `caption-side: top;` y tipografía destacada.
  3. Diferencia visualmente las celdas de cabecera `th` (con `scope="col"` y `scope="row"`) de las celdas de datos `td`.
  4. Añade un relleno (*padding*) generoso y bordes sutiles.
* **Pista:** `border-collapse: collapse` fusiona los bordes adyacentes de las celdas en un único borde limpio.

---

#### U07.09 — Optimización de tablas con `table-layout: fixed`
* **Nivel:** Avanzado
* **Enunciado:** Una tabla contiene miles de registros. En modo automático (`table-layout: auto`), el navegador debe descargar e inspeccionar el contenido de todas las celdas antes de poder calcular el ancho de las columnas, bloqueando el renderizado de la página.
* **Tarea:**
  1. Aplica `table-layout: fixed; width: 100%;` a la tabla.
  2. Define anchos fijos o porcentuales en las celdas de cabecera del `<thead>`.
  3. Añade `white-space: nowrap; overflow: hidden; text-overflow: ellipsis;` a las celdas de texto largo para truncar nombres de archivo sin desbordar.
  4. Explica por qué `table-layout: fixed` rinde infinitamente mejor en tablas grandes.
* **Pista:** Con `table-layout: fixed`, el navegador dibuja la tabla inmediatamente leyendo únicamente la primera fila de cabeceras.

---

#### U07.10 — Bandas cebradas, cabecera adhesiva y alineación numérica tabular
* **Nivel:** Avanzado
* **Enunciado:** Diseña una tabla financiera profesional con filas alternas sombreadas, cabecera que permanece fija al hacer scroll vertical en el contenedor y números perfectamente alineados por sus comas decimales.
* **Tarea:**
  1. Aplica bandas cebradas con `tbody tr:nth-child(even) { background-color: #f8f9fa; }`.
  2. Configura la cabecera adhesiva con `thead th { position: sticky; top: 0; background-color: ...; z-index: 1; }`.
  3. Alinea las columnas numéricas a la derecha y utiliza la propiedad tipográfica `font-variant-numeric: tabular-nums` para que todos los dígitos tengan idéntico ancho monoespaciado.
* **Pista:** `font-variant-numeric: tabular-nums` evita el baile visual de cifras con anchos proporcionales en tablas contables.

---

### Unidad 08 — Unidades, tipografía y colores

Conceptos evaluados: unidades absolutas (`px`) vs relativas (`rem`, `em`, `%`), unidades de viewport (`vw`, `vh`, `dvh`, `svh`), funciones matemáticas (`calc()`, `min()`, `max()`, `clamp()`), tipografía fluida, carga con `@font-face` y `font-display`, propiedades tipográficas modernas (`line-height` sin unidades, `text-wrap: balance`), modelos de color (RGB, HSL, OKLCH), mezcla dinámica con `color-mix()`, y sistema de tokens con contraste WCAG. Integra U01–U07.

#### U08.01 — Configuración base de `rem` y espaciado proporcional
* **Nivel:** Básico
* **Enunciado:** Establece un sistema escalable donde todos los tamaños tipográficos y espaciados dependan de la raíz del documento.
* **Tarea:**
  1. Declara el tamaño base en `html` (manteniendo el estándar del navegador al 100% o 16px para respetar las preferencias de accesibilidad del usuario).
  2. Escribe una escala de clases tipográficas (`.texto-sm: 0.875rem`, `.texto-base: 1rem`, `.texto-lg: 1.25rem`, `.texto-xl: 1.5rem`).
  3. Explica por qué fijar `html { font-size: 10px; }` viola las buenas prácticas de accesibilidad para personas con problemas de visión.
* **Pista:** Modificar el tamaño base del `html` en píxeles fijos anula la configuración que el usuario haya establecido en su sistema operativo.

---

#### U08.02 — El efecto compuesto del `em` vs la consistencia del `rem`
* **Nivel:** Básico
* **Enunciado:** Una lista anidada de tres niveles (`ul > li > ul > li > ul > li`) tiene declarado `font-size: 1.2em`. El texto de los subniveles se vuelve gigantesco de forma descontrolada.
* **Tarea:**
  1. Explica matemáticamente el efecto compuesto (*compounding effect*) de las unidades `em` en propiedades heredadas.
  2. Corrige el problema sustituyendo por unidades `rem`.
  3. Muestra un ejemplo donde el uso de `em` es la mejor opción técnica (el padding interno de un botón que escala proporcionalmente si cambia su font-size).
* **Pista:** `1rem` siempre se refiere a la raíz (`html`); `1em` se refiere al tamaño de fuente del propio elemento o de su padre directo.

---

#### U08.03 — Unidades de viewport dinámicas en móviles: `dvh`, `svh` y `lvh`
* **Nivel:** Medio
* **Enunciado:** Una pantalla de bienvenida a toda altura tiene `height: 100vh;`. En dispositivos móviles (Chrome Android / Safari iOS), al hacer scroll aparece y desaparece la barra de direcciones del navegador, provocando que la parte inferior de la pantalla quede oculta o dé tirones visuales bruscos.
* **Tarea:**
  1. Explica la diferencia entre `100svh` (Small Viewport Height), `100lvh` (Large Viewport Height) y `100dvh` (Dynamic Viewport Height).
  2. Implementa una sección de bienvenida utilizando `min-height: 100dvh;` con fallback a `100vh` para navegadores antiguos.
* **Pista:** `dvh` recalcula la altura dinámicamente cuando la barra de navegación del navegador móvil se expande o colapsa.

---

#### U08.04 — Funciones matemáticas: `calc()`, `min()` y `max()`
* **Nivel:** Medio
* **Enunciado:** Se necesita maquetar un contenedor que mida el 100% del ancho de la ventana menos 40 píxeles de márgenes exteriores, pero que nunca sea más ancho de 1200px ni más estrecho de 300px.
* **Tarea:**
  1. Combina `calc()`, `min()` y `max()` en una o dos declaraciones de ancho.
  2. Demuestra el uso de operaciones matemáticas con unidades mixtas (`calc(100% - 2rem)`).
  3. Recuerda la regla obligatoria de espaciado alrededor de los operadores matemáticos `+` y `-` en `calc()`.
* **Pista:** En `calc()`, los operadores `+` y `-` deben llevar siempre un espacio antes y después (ej. `calc(100% - 40px)`).

---

#### U08.05 — Tipografía fluida continua con `clamp()`
* **Nivel:** Medio
* **Enunciado:** Diseña un titular `h1` responsivo fluido que mida exactamente 2rem (32px) en pantallas móviles de 360px de ancho, y que escale progresiva y suavemente hasta 4rem (64px) en pantallas de escritorio de 1200px, sin usar ninguna media query.
* **Tarea:**
  1. Aplica la función `clamp(min, preferred, max)`.
  2. Calcula o aproxima el valor preferido combinando un valor base en `rem` y una proporción en unidades `vw` (ej. `clamp(2rem, 1.14rem + 3.8vw, 4rem)`).
  3. Verifica que en pantallas inferiores a 360px nunca baje de 2rem y en pantallas superiores a 1200px nunca supere 4rem.
* **Pista:** `clamp(MIN, VALOR_FLUIDO, MAX)` mantiene el valor dentro del rango acotado en cualquier resolución.

---

#### U08.06 — Carga optimizada de tipografías con `@font-face` y `font-display`
* **Nivel:** Medio
* **Enunciado:** La fuente corporativa "OpenSans-Variable.woff2" tarda 1.5 segundos en descargarse en redes móviles lentas. Durante ese tiempo, la página muestra un espacio en blanco invisible (Flash of Invisible Text - FOIT), degradando la experiencia y la métrica Core Web Vital LCP.
* **Tarea:**
  1. Redacta la regla `@font-face` completa con `font-family`, ruta `url()` en formato WOFF2 y rango de pesos.
  2. Añade la directiva `font-display: swap;` para mostrar inmediatamente una fuente del sistema de respaldo y sustituirla cuando la fuente web termine de cargar.
  3. Define una pila tipográfica (*font stack*) robusta con fuentes sans-serif del sistema como fallback.
* **Pista:** `font-display: swap` erradica el texto invisible mostrando una fuente del sistema hasta que se complete la descarga.

---

#### U08.07 — Legibilidad avanzada: `line-height` relativo y `text-wrap`
* **Nivel:** Medio
* **Enunciado:** Mejora la calidad tipográfica y la legibilidad editorial de un portal de noticias.
* **Tarea:**
  1. Explica por qué `line-height` debe declararse como un número sin unidades (ej. `line-height: 1.5;`) en lugar de píxeles (`24px`) o porcentajes (`150%`).
  2. Aplica `text-wrap: balance;` a los titulares `h1`, `h2` para equilibrar armónicamente la longitud de sus líneas.
  3. Aplica `text-wrap: pretty;` a los párrafos de texto para evitar palabras huérfanas en la última línea.
* **Pista:** Un `line-height` sin unidades se recalcula de forma relativa al `font-size` de cada elemento hijo cuando se hereda.

---

#### U08.08 — El espacio de color moderno OKLCH frente a HEX/RGB/HSL
* **Nivel:** Avanzado
* **Enunciado:** En el modelo HSL tradicional, un color amarillo con luminosidad 50% (`hsl(60, 100%, 50%)`) se percibe visualmente muchísimo más brillante y claro para el ojo humano que un azul con luminosidad 50% (`hsl(240, 100%, 50%)`), provocando fallos en escalas de contraste automáticas.
* **Tarea:**
  1. Explica por qué el espacio `oklch(L C H)` es perceptualmente uniforme.
  2. Define tres colores corporativos usando la sintaxis moderna `oklch(luminosidad croma matiz)`: primario, éxito y peligro.
  3. Comprueba el soporte del navegador y añade un fallback en HSL/RGB mediante `@supports`.
* **Pista:** En OKLCH, dos colores con la misma luminosidad (L) tienen el mismo brillo aparente para el sistema visual humano en todo el espectro cromático.

---

#### U08.09 — Variantes automáticas con `color-mix()`
* **Nivel:** Avanzado
* **Enunciado:** En lugar de declarar a mano códigos de color hexadecimales independientes para los estados `:hover` y `:active` de cada botón, genera automáticamente las variantes más oscuras o claras mezclando dinámicamente el color base en CSS.
* **Tarea:**
  1. Define una variable `--color-marca: #2563eb;`.
  2. Crea la variante de hover mezclando un 85% de la marca con un 15% de negro en el espacio `oklab`: `color-mix(in oklab, var(--color-marca) 85%, black)`.
  3. Crea un fondo de alerta semitransparente mezclando un 10% del color marca con un 90% de blanco o transparente.
* **Pista:** `color-mix(in espacio, color1 porcentaje, color2)` interpola dos colores nativamente en el navegador.

---

#### U08.10 — Sistema de Tokens con modo claro/oscuro y contraste WCAG
* **Nivel:** Avanzado
* **Enunciado:** Construye un sistema de variables semánticas que conmute automáticamente entre tema claro y tema oscuro respetando las preferencias del sistema operativo del usuario (`@media (prefers-color-scheme: dark)` o la función `light-dark()`), asegurando un ratio de contraste mínimo de 4.5:1 (WCAG Nivel AA).
* **Tarea:**
  1. Declara en `:root` tokens de superficie (`--bg-surface`, `--bg-canvas`), texto (`--text-main`, `--text-muted`) y borde (`--border-color`).
  2. Implementa la variante oscura mediante `@media (prefers-color-scheme: dark)`.
  3. Comprueba que el texto principal sobre el fondo de superficie cumple la relación de contraste 4.5:1 exigida por el criterio WCAG 1.4.3.
* **Pista:** La función moderna `color: light-dark(#111, #eee);` permite declarar ambos valores simultáneamente si se activa `color-scheme: light dark;`.

---

### Unidad 09 — Fondos, imágenes y decoración

Conceptos evaluados: propiedades de fondo (`background-image`, `size`, `position`, `repeat`), degradados (`linear-gradient`, `radial-gradient`, `conic-gradient`), fondos múltiples por capas, control de elementos reemplazados (`object-fit`, `object-position`, `aspect-ratio`), bordes elípticos y asimétricos, recorte con `clip-path`, cristal esmerilado con `backdrop-filter` y filtros visuales (`filter: drop-shadow()` vs `box-shadow`). Integra U01–U08.

#### U09.01 — Configuración y control de imágenes de fondo
* **Nivel:** Básico
* **Enunciado:** Una sección de bienvenida requiere una imagen de fondo que no se repita en mosaico y que permanezca siempre centrada tanto horizontal como verticalmente.
* **Tarea:**
  1. Aplica las propiedades individuales: `background-image`, `background-repeat: no-repeat;`, `background-position: center center;`.
  2. Condensa las reglas en la propiedad abreviada `background`.
  3. Añade un color de fondo sólido de reserva (`background-color`) para que el texto sea legible mientras la imagen se descarga.
* **Pista:** Siempre que uses una imagen de fondo, define un `background-color` de respaldo con suficiente contraste tipográfico.

---

#### U09.02 — Escala de fondo: `cover` frente a `contain`
* **Nivel:** Básico
* **Enunciado:** Muestra la diferencia visual de comportamiento entre `background-size: cover` y `background-size: contain` en una caja fija de 400x300 píxeles.
* **Tarea:**
  1. Explica qué hace `cover` (llena todo el contenedor recortando bordes sobrantes de la imagen para preservar la proporción).
  2. Explica qué hace `contain` (muestra la imagen completa sin recortar nada, dejando posibles espacios vacíos a los lados).
  3. Señala cuál es la opción adecuada para un banner hero y cuál para el logotipo de un patrocinador.
* **Pista:** `cover` prioriza rellenar la caja; `contain` prioriza mostrar la imagen íntegra.

---

#### U09.03 — Degradados lineales y paradas de color (*color stops*)
* **Nivel:** Medio
* **Enunciado:** Diseña un fondo de cabecera con un degradado suave a 135 grados que comience en azul marino, pase por violeta intermedio al 40% y termine en rosa fucsia al 100%.
* **Tarea:**
  1. Utiliza la función `linear-gradient(135deg, ...)`.
  2. Define las paradas de color (*color stops*) con porcentajes explícitos.
  3. Crea un botón con un degradado de corte brusco (*hard stops*) para generar dos franjas de color sólidas sin transición difuminada.
* **Pista:** Si dos paradas de color consecutivas coinciden en el mismo porcentaje (ej. `#333 50%, #fff 50%`), se genera una línea de corte limpia y nítida.

---

#### U09.04 — Degradados radiales y cónicos
* **Nivel:** Medio
* **Enunciado:** Se desea crear una viñeta decorativa con degradado radial y un gráfico circular de progreso en CSS puro sin usar imágenes externas.
* **Tarea:**
  1. Implementa un `radial-gradient(circle at center, ...)` que cree un foco de luz en el centro oscureciéndose hacia los bordes.
  2. Implementa un `conic-gradient(...)` para crear un gráfico de sectores que pinte el 75% del círculo en verde y el 25% en gris claro.
* **Pista:** `conic-gradient()` rota los colores alrededor de un centro, siendo ideal para gráficos circulares (*pie charts*).

---

#### U09.05 — Fondos multicapa: imagen con máscara de oscurecimiento
* **Nivel:** Medio
* **Enunciado:** Se coloca una fotografía concurrida como fondo de un banner y un texto blanco encima. En ciertas partes de la foto el texto se vuelve ilegible por falta de contraste.
* **Tarea:**
  1. Aplica un fondo multicapa mediante la sintaxis de múltiples imágenes en `background-image` separadas por comas.
  2. Coloca en la capa superior un degradado semitransparente oscuro (`linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6))`) y en la capa inferior la imagen fotográfica.
  3. Explica el orden de apilamiento de las capas de fondo en CSS (la primera declarada es la que queda arriba).
* **Pista:** La primera capa declarada en `background-image` se dibuja en la parte superior, más cerca del usuario.

---

#### U09.06 — Control de imágenes reemplazadas con `object-fit` y `aspect-ratio`
* **Nivel:** Medio
* **Enunciado:** Los usuarios suben fotos de perfil en diversas proporciones (4:3, 16:9, fotos verticales panorámicas). Al forzar `width: 200px; height: 200px;` en la etiqueta `<img>`, las fotos se deforman y estiran horriblemente.
* **Tarea:**
  1. Aplica `object-fit: cover;` y `object-position: center top;` a la etiqueta `<img>`.
  2. Aplica la propiedad moderna `aspect-ratio: 1 / 1;` para mantener la relación cuadrada automáticamente sin alturas fijas en píxeles.
  3. Explica cómo `aspect-ratio` previene el desplazamiento acumulativo de layout (métrica CLS) reservando el espacio antes de que la imagen descargue.
* **Pista:** `object-fit` funciona exactamente igual que `background-size`, pero aplicado sobre elementos reemplazados HTML (`<img>`, `<video>`).

---

#### U09.07 — Bordes elípticos y formas orgánicas complejas
* **Nivel:** Medio
* **Enunciado:** Diseña una insignia o avatar en forma de píldora perfecta y una tarjeta decorativa con esquinas elípticas asimétricas.
* **Tarea:**
  1. Utiliza `border-radius: 9999px;` para crear un botón en forma de píldora que se adapte a cualquier ancho sin deformarse.
  2. Utiliza la sintaxis de barra inclinada `/` de `border-radius` para definir radios horizontales y verticales independientes (`border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%`).
* **Pista:** La barra diagonal `/` en `border-radius` separa los radios horizontales de los radios verticales de cada una de las esquinas.

---

#### U09.08 — Recorte vectorial de elementos con `clip-path`
* **Nivel:** Avanzado
* **Enunciado:** Una sección de cabecera debe terminar en una diagonal inclinada dinámica en su base en lugar de una línea horizontal recta. Además, una tarjeta promocional debe tener forma de hexágono o flecha.
* **Tarea:**
  1. Aplica `clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);` a la cabecera.
  2. Diseña una flecha indicadora usando la función `polygon()`.
  3. Explica por qué `clip-path` no altera el modelo de caja física ni la respuesta a eventos de puntero fuera del área recortada.
* **Pista:** `clip-path` recorta visualmente el área visible de un elemento a partir de coordenadas geométricas (círculos, elipses, polígonos).

---

#### U09.09 — Efecto de cristal esmerilado con `backdrop-filter` (*Glassmorphism*)
* **Nivel:** Avanzado
* **Enunciado:** Diseña una tarjeta flotante o barra de navegación translúcida con el moderno efecto de vidrio esmerilado que desenfoque el contenido que pasa por detrás de ella.
* **Tarea:**
  1. Aplica un fondo semitransparente utilizando un color con canal alfa (`background-color: rgba(255, 255, 255, 0.2)` o con `oklch`).
  2. Aplica la propiedad `backdrop-filter: blur(12px) saturate(180%);`.
  3. Añade un borde sutil semitransparente de 1px para simular el bisel del cristal.
  4. Explica la diferencia crítica entre `filter: blur()` (desenfoca el elemento propio) y `backdrop-filter: blur()` (desenfoca lo que está detrás).
* **Pista:** Para que `backdrop-filter` sea visible, el fondo propio del elemento debe tener cierta transparencia.

---

#### U09.10 — Comparativa de sombras: `box-shadow` frente a `filter: drop-shadow()`
* **Nivel:** Avanzado
* **Enunciado:** Tienes una imagen PNG transparente de una estrella y un bocadillo de diálogo que tiene una flecha triangular creada con un pseudo-elemento. Al aplicar `box-shadow`, la sombra se proyecta como un feo rectángulo cuadrado alrededor de la caja transparente, ignorando la forma real de la estrella y la flecha.
* **Tarea:**
  1. Sustituye `box-shadow` por `filter: drop-shadow(4px 4px 8px rgba(0,0,0,0.3));`.
  2. Demuestra cómo `drop-shadow()` sigue el contorno alfa de los píxeles visibles de la imagen PNG y unifica la flecha con el bocadillo de diálogo.
  3. Compara las capacidades de ambas propiedades (nota: `drop-shadow` no admite el parámetro spread ni sombras inset).
* **Pista:** `filter: drop-shadow()` proyecta la sombra sobre los píxeles no transparentes del elemento y de sus pseudo-elementos.

---

### Unidad 10 — Diseño responsivo y Container Queries

Conceptos evaluados: meta viewport, estrategia Mobile-First vs Desktop-First, Media Queries (`@media`), sintaxis de rango moderna, breakpoints estándar, media queries de características del dispositivo (`hover`, `pointer`), preferencias del usuario (`prefers-reduced-motion`, `prefers-color-scheme`), Container Queries (`@container`), `container-type`, y unidades de contenedor (`cqw`, `cqh`, `cqi`). Integra U01–U09.

#### U10.01 — El meta viewport y el factor de escala en dispositivos móviles
* **Nivel:** Básico
* **Enunciado:** Un sitio web se visualiza en un smartphone como si fuera una pantalla gigante de ordenador reducida y diminuta (viewport virtual de 980px), obligando al usuario a hacer doble toque y zoom para poder leer.
* **Tarea:**
  1. Escribe la etiqueta `<meta name="viewport">` estándar en el `<head>`.
  2. Explica qué significa cada uno de sus componentes: `width=device-width` e `initial-scale=1.0`.
  3. Explica por qué jamás debe configurarse `user-scalable=no` o `maximum-scale=1.0` por razones de accesibilidad (criterio WCAG 1.4.4).
* **Pista:** El meta viewport sincroniza el ancho del viewport de renderizado con los píxeles lógicos del dispositivo físico.

---

#### U10.02 — Filosofía Mobile-First con Media Queries `@media`
* **Nivel:** Básico
* **Enunciado:** Construye un diseño de tarjeta que en teléfonos móviles ocupe el 100% del ancho con texto centrado, y que a partir de 768px de ancho se muestre en dos columnas con texto alineado a la izquierda.
* **Tarea:**
  1. Escribe los estilos base fuera de cualquier media query (diseño móvil).
  2. Aplica la consulta `@media (min-width: 768px)` para introducir las modificaciones de pantalla grande.
  3. Explica por qué la aproximación Mobile-First es técnicamente superior a Desktop-First (menos sobrescrituras de código, menor consumo de datos en dispositivos limitados).
* **Pista:** Mobile-First utiliza exclusivamente consultas `@media (min-width: ...)`; Desktop-First utiliza `@media (max-width: ...)`.

---

#### U10.03 — Sintaxis moderna de rango en Media Queries
* **Nivel:** Medio
* **Enunciado:** En la especificación Media Queries Level 4 se introdujo la sintaxis de operadores de comparación matemática (`<=`, `>=`, `<`), mucho más intuitiva que las combinaciones con `and`, `min-width` y `max-width`.
* **Tarea:**
  1. Toma la regla legacy: `@media (min-width: 600px) and (max-width: 1024px) { ... }`.
  2. Reescríbela utilizando la sintaxis de rango moderna: `@media (600px <= width <= 1024px) { ... }`.
  3. Reescribe una consulta de móvil simple con `@media (width < 768px)`.
* **Pista:** La sintaxis matemática de rango está soportada en todos los navegadores modernos y previene errores con los límites exactos de píxeles.

---

#### U10.04 — Menú de navegación responsivo adaptable
* **Nivel:** Medio
* **Enunciado:** Maqueta una barra de navegación que en pantallas de escritorio (`width >= 768px`) se muestre en una sola fila horizontal con Flexbox, y que en pantallas móviles (`width < 768px`) se apile en una columna vertical con botones de ancho completo.
* **Tarea:**
  1. Diseña la estructura con Mobile-First (`display: flex; flex-direction: column; width: 100%;`).
  2. Introduce `@media (min-width: 768px)` cambiando a `flex-direction: row; justify-content: space-between;`.
  3. Asegura un área táctil mínima de 44x44 píxeles para cada enlace en la versión móvil (requisito WCAG 2.5.5 / 2.5.8).
* **Pista:** Los enlaces y botones en móvil deben tener suficiente padding para pulsar con el dedo cómodamente sin disparar enlaces contiguos.

---

#### U10.05 — Cuadrícula responsiva por puntos de ruptura (*Breakpoints*)
* **Nivel:** Medio
* **Enunciado:** Un catálogo de productos debe estructurarse mediante CSS Grid con la siguiente progresión de columnas:
  * Móvil (< 576px): 1 columna.
  * Tablet vertical (576px a 767px): 2 columnas.
  * Tablet horizontal / Laptop (768px a 1199px): 3 columnas.
  * Escritorio grande (>= 1200px): 4 columnas.
* **Tarea:**
  1. Implementa los estilos base y las 3 media queries con Mobile-First (`min-width: 576px`, `min-width: 768px`, `min-width: 1200px`).
  2. Emplea la propiedad `gap` ajustándola progresivamente (12px en móvil, 24px en escritorio).
* **Pista:** Utilizar variables CSS para las pistas de grid agiliza la actualización entre diferentes breakpoints.

---

#### U10.06 — Adaptación a capacidades de puntero: `@media (hover: hover)`
* **Nivel:** Medio
* **Enunciado:** En pantallas táctiles de smartphones, los efectos `:hover` provocan comportamientos extraños (se quedan pegados y requieren un segundo toque para abrir enlaces).
* **Tarea:**
  1. Envuelve los estilos interactivos de `:hover` dentro de una consulta de características: `@media (hover: hover) and (pointer: fine) { ... }`.
  2. Asegura que en dispositivos con puntero grueso o sin hover (`@media (hover: none)` o táctiles), los botones muestren su información siempre visible o mediante estados de foco limpios.
  3. Explica por qué basar la detección táctil en el ancho de la pantalla (`width < 768px`) es un error grave en la actualidad (portátiles táctiles, tablets de alta resolución).
* **Pista:** Una pantalla grande puede ser táctil (iPad Pro) y una pantalla pequeña puede tener ratón (mini-laptop); detecta la capacidad del puntero, no el ancho.

---

#### U10.07 — Respeto a preferencias de accesibilidad: `@media (prefers-reduced-motion)`
* **Nivel:** Avanzado
* **Enunciado:** Ciertas personas sufren trastornos vestibulares, mareos o epilepsia foto-sensible causados por animaciones de desplazamiento, giros y transiciones excesivas en la web.
* **Tarea:**
  1. Crea una tarjeta con una transición suave en el hover (`transform: translateY(-8px)`).
  2. Implementa la media query `@media (prefers-reduced-motion: reduce)`.
  3. Desactiva o neutraliza la animación en dicha consulta (`transition: none; transform: none;`), sustituyéndola por un cambio discreto de color de borde.
* **Pista:** Respetar `prefers-reduced-motion` es un requisito indispensable del criterio WCAG 2.3.3.

---

#### U10.08 — Introducción a Container Queries: contexto de contenedor
* **Nivel:** Avanzado
* **Enunciado:** Una tarjeta de producto se reutiliza en dos sitios distintos de la web: en el área principal de contenido (donde dispone de 800px de ancho) y en una barra lateral estrecha (donde solo dispone de 280px de ancho), ambas en la misma pantalla de escritorio de 1440px. Las media queries de viewport no pueden distinguir entre ambos casos porque el ancho del navegador es idéntico.
* **Tarea:**
  1. Define el elemento padre como contenedor de consulta: `container-type: inline-size; container-name: card-container;`.
  2. Explica qué significa `container-type: inline-size` (el contenedor mide y monitoriza su propio ancho en el eje en línea).
  3. Explica por qué no debe usarse `container-type: size` a la ligera (requiere altura fija explícita para evitar bucles infinitos de layout).
* **Pista:** Las Container Queries evalúan el tamaño del elemento contenedor directo del componente, no el tamaño de la ventana global.

---

#### U10.09 — El componente modular autónomo con `@container`
* **Nivel:** Avanzado
* **Enunciado:** Implementa el rediseño adaptativo de la tarjeta de producto dentro del contenedor definido en el ejercicio anterior.
* **Tarea:**
  1. Por defecto, estila la tarjeta en formato vertical (imagen arriba, texto abajo) para cuando el contenedor mida menos de 400px.
  2. Utiliza `@container card-container (min-width: 400px)` para transformar la tarjeta en formato horizontal (imagen a la izquierda ocupando el 40%, textos a la derecha ocupando el 60%) cuando el contenedor supere ese umbral.
  3. Comprueba cómo la tarjeta se adapta con autonomía tanto si se inserta en un sidebar estrecho como si se coloca en un área principal espaciosa.
* **Pista:** El componente se vuelve 100% autónomo y modular, listo para incrustarse en cualquier arquitectura de diseño sin depender del viewport.

---

#### U10.10 — Tipografía y espaciado fluido con unidades de contenedor (`cqw`)
* **Nivel:** Avanzado
* **Enunciado:** Diseña un widget interactivo de previsión meteorológica o cotización bursátil cuyo tamaño tipográfico, radio de bordes y rellenos escalen milimétricamente en función exacta del ancho de su propio contenedor.
* **Tarea:**
  1. Utiliza las unidades de consulta de contenedor: `1cqw` (1% del ancho del contenedor en línea) o `1cqi`.
  2. Combina unidades `cqw` dentro de una función de acotamiento: `font-size: clamp(1rem, 5cqw, 2.5rem);`.
  3. Aplica rellenos proporcionales con `padding: clamp(0.75rem, 3cqw, 2rem);`.
  4. Demuestra que si el contenedor se redimensiona en un layout flexible de CSS Grid, todo el contenido interior del widget escala armónicamente.
* **Pista:** `1cqw` equivale al 1% del ancho del contenedor más cercano que tenga declarado `container-type: inline-size`.

---

## PARTE B · GLOSARIO ES/EN

Tres términos se repiten en casi todos los exámenes: ==cascada==, ==especificidad== y contexto de apilamiento.

| Término | English | Definición breve |
|---|---|---|
| Cascada | Cascade | Proceso de resolución de conflictos entre declaraciones. |
| Especificidad | Specificity | Peso relativo de un selector. |
| Hoja de estilos | Stylesheet | Archivo/bloque de reglas CSS. |
| Modelo de caja | Box model | Estructura content/padding/border/margin. |
| Colapso de márgenes | Margin collapsing | Fusión de márgenes verticales adyacentes. |
| Contexto de formato de bloque | Block Formatting Context (BFC) | Ámbito de render independiente. |
| Contexto de apilamiento | Stacking context | Capa aislada para comparar `z-index`. |
| Bloque contenedor | Containing block | Referencia de posicionamiento absoluto/fijo. |
| Pista (grid) | Track | Fila o columna de una cuadrícula. |
| Línea (grid) | Grid line | Borde de una pista. |
| Área (grid) | Grid area | Rectángulo definido por 4 líneas. |
| Subcuadrícula | Subgrid | Herencia de pistas del grid padre. |
| Eje principal | Main axis | Dirección del flujo en flexbox. |
| Consulta de medios | Media query | Condición sobre características del dispositivo. |
| Consulta de contenedor | Container query | Condición sobre el tamaño/estilo del contenedor. |
| Propiedad personalizada | Custom property | Variable CSS (`--x`). |
| Capa (cascada) | Cascade layer | Grupo de reglas con prioridad declarada (`@layer`). |
| Anidación | Nesting | Reglas dentro de reglas (nativa o Sass). |
| Degradado | Gradient | Imagen generada por interpolación de colores. |
| Modo de mezcla | Blend mode | Algoritmo de combinación de capas de color. |
| Máscara | Mask | Recorte por alfa/luminancia. |
| Transición | Transition | Interpolación entre dos estados. |
| Fotogramas clave | Keyframes | Estados intermedios de una animación. |
| Función de temporización | Timing function | Curva de velocidad de la animación. |
| Promoción a capa | Layer promotion | Elevar elemento a compositor (`will-change`). |
| Renderizador bloqueante | Render-blocking | Recurso que retrasa la primera pintura. |
| Ruta crítica de render | Critical Rendering Path | Pipeline DOM+CSSOM→pantalla. |
| Desplazamiento acumulado | Cumulative Layout Shift (CLS) | Inestabilidad visual medida. |
| Tokens de diseño | Design tokens | Decisiones de diseño nombradas como datos. |
| Guía de estilo | Style guide | Documento de convenciones visuales y de código. |
| Mejora progresiva | Progressive enhancement | Base simple + mejoras según capacidades. |
| Reflow / Relayout | Reflow | Recálculo de geometría. |
| Repintado | Repaint | Redibujar píxeles sin recalcular layout. |
| Composición | Composite | Unión de capas en GPU. |
| Contraste | Contrast ratio | Relación de luminancias entre texto y fondo. |
| Foco visible | Visible focus | Indicador claro del elemento enfocado. |
| Movimiento reducido | Reduced motion | Preferencia del usuario para menos animación. |
| Colores forzados | Forced colors | Modo alto contraste del SO (Windows). |

!!! info "Cómo estudiar el glosario"

    - La columna **EN** es la que verás en MDN, en las specs y en las ofertas de trabajo.
    - Aprende **de dos en dos** (ES + EN) y ancla cada par a un ejemplo de código.
    - Cuidado con los gemelos: **cascade ≠ specificity**, **track ≠ line**, **repaint ≠ reflow**.

---

## PARTE C · RECURSOS OFICIALES Y DE PROFUNDIZACIÓN

Empezando por aquí: ==MDN== para dudas diarias y ==caniuse== antes de estrenar cualquier API.

### Especificaciones (W3C / CSS WG)

- Índice de specs CSS: <https://www.w3.org/Style/CSS/>
- Selectors Level 4: <https://www.w3.org/TR/selectors-4/>
- Color Level 5: <https://www.w3.org/TR/css-color-5/>
- Grid Level 2 (subgrid): <https://www.w3.org/TR/css-grid-2/>
- Conditional Rules Level 5 (container queries): <https://drafts.csswg.org/css-conditional-5/>
- Nesting Level 1: <https://www.w3.org/TR/css-nesting-1/>
- View Transitions Level 1: <https://www.w3.org/TR/css-view-transitions-1/>
- Cascade Level 5/6: <https://www.w3.org/TR/css-cascade-5/> / <https://www.w3.org/TR/css-cascade-6/>
- Animations Level 2 (scroll-driven): <https://www.w3.org/TR/css-animations-2/>

### Documentación de referencia

- **MDN Web Docs (ES)**: <https://developer.mozilla.org/es/docs/Web/CSS> — la biblia diaria.
- **web.dev** (Google): rendimiento, Core Web Vitals, a11y: <https://web.dev>
- **Chrome Developers**: artículos profundos del equipo Chromium: <https://developer.chrome.com/docs>
- **caniuse.com**: compatibilidad por característica (verificar antes de usar features nuevas).
- **browser-compat-data** (MDN): datos de soporte en GitHub: <https://github.com/mdn/browser-compat-data>

### Accesibilidad

- WCAG 2.2 (W3C): <https://www.w3.org/TR/WCAG22/>
- Técnicas WCAG (cómo cumplir cada criterio): <https://www.w3.org/WAI/WCAG22/Techniques/>
- The A11Y Project: <https://www.a11yproject.com>
- axe DevTools (Deque): <https://www.deque.com/axe/devtools/>
- WebAIM: contrast checker y artículos: <https://webaim.org>

### Práctica y comunidad

- **Frontend Masters / CSS Battle**: retos de CSS puro: <https://cssbattle.dev>
- **Smol CSS** (Jhey Tompkins): trucos cortos bien explicados: <https://smolcss.com>
- **Every Layout** (Heydon Pickering): conceptos de layout: <https://every-layout.dev>
- **A List Apart**: artículos largos de calidad: <https://alistapart.com>
- **Norm (Viget)**: patrones de diseño web: <https://www.viget.com/study/norm/>

### Normativa (Andalucía / España)

- Orden de 16 de junio de 2011 (BOJA 149/2011), currículo DAW Andalucía: <https://www.juntadeandalucia.es/boja/2011/149/23>
- RD 686/2010 (BOE), título DAW: <https://www.boe.es/eli/es/rd/2010/05/20/686>
- BOJA (consultar modificaciones posteriores): <https://www.juntadeandalucia.es/eboja.html>

### Herramientas citadas en los apuntes

| Herramienta | Uso |
|---|---|
| Jigsaw CSS Validator | Validación sintáctica W3C. |
| stylelint + Prettier | Lint y formato. |
| PurgeCSS | Eliminar CSS muerto. |
| Lightning CSS / cssnano | Transform y minificación. |
| Vite | Build moderno con HMR. |
| Lighthouse / DevTools | Métricas y diagnóstico. |
| axe / WAVE / Pa11y | Auditoría de accesibilidad. |
| Stark / WebAIM | Contraste y daltonismo. |
| Storybook / Chromatic | Componentes y visual regression. |
| Fluid typography calculators | Derivar `clamp()`. |
