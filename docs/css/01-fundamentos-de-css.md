---
icon: lucide/lightbulb
title: "Unidad 01 — Fundamentos de CSS"
description: "Historia del lenguaje, sintaxis, formas de incluir estilos, cascada, especificidad, herencia e importancia. Base sobre la que se construye todo el resto de los apuntes."
modulo: "LMH (0373) / DIW (0615)"
unidad: 1
fecha: "2026-09-06"
---

# Unidad 01 · Fundamentos de CSS

CSS da **aspecto** al contenido, pero también impone reglas de convivencia: **cascada**, **especificidad** y **herencia** deciden qué declaración acaba viéndose. Dominar esta unidad separa un CSS mantenible de un archivo lleno de `!important`.

!!! note "Conocimientos previos"

    - Estructura básica de **HTML** y para qué sirve una hoja de estilo.
    - Haber abierto las **DevTools** del navegador y mirado la pestaña *Elements*.
    - Distinguir **estilo en línea** de **hoja externa** (visto en el módulo 0373).

## 1. ¿Qué es CSS y por qué existe?

**CSS (Cascading Style Sheets)** es un lenguaje de hojas de estilo que describe **cómo se presenta** un documento estructurado (HTML, XML/SVG…). Su función es separar la **presentación** de la **estructura**, lo que el currículo llama ==separación de preocupaciones== (CE 2.g):

```text title="capas-tecnologicas.txt"
HTML  → estructura y semántica (QUÉ hay en la página)
CSS   → presentación (CÓMO se ve)
JS    → comportamiento (CÓMO actúa)
```

### Ventajas de usar hojas de estilo (CE 2.g del módulo 0373)

| Ventaja | Explicación |
|---|---|
| **Separación de preocupaciones** | El contenido vive en HTML; el aspecto en CSS. **Cambiar el diseño no toca el contenido**. |
| **Mantenibilidad** | **Un cambio en una regla** afecta a todos los elementos seleccionados. Sin CSS habría que editar cada etiqueta. |
| **Consistencia** | Una clase `.boton` garantiza el mismo aspecto en toda la aplicación (RA 2 del 0615: «interfaces homogéneas»). |
| **Menor peso de transferencia** | Un único archivo CSS se descarga y cachea una vez; el HTML queda más ligero. |
| **Accesibilidad** | Permite adaptar el diseño a las necesidades del usuario (tamaño de texto, contraste, movimiento reducido) sin tocar el contenido. |
| **Impresión y otros medios** | Con `@media` el mismo documento puede verse bien en pantalla, imprimirse o leerse. |
| **Reutilización** | La misma hoja sirve a varios documentos; varias hojas pueden combinarse. |

### 1.1. ¿Cómo funciona CSS por debajo? (El pipeline de renderizado)

Para un estudiante que parte de cero, CSS parece a menudo «magia impredecible»: escribes una regla y a veces se aplica y a veces no. Entender qué hace el motor del navegador internamente desmitifica este proceso por completo:

1. **Construcción del DOM (Document Object Model):** El navegador lee los bytes HTML, los tokeniza y crea un árbol en memoria con cada etiqueta (`<html>`, `<body>`, `<article>`, etc.).
2. **Construcción del CSSOM (CSS Object Model):** De forma paralela, el navegador descarga y analiza las hojas de estilo (`<link>`, `<style>` y estilos de usuario/navegador). Crea otro árbol donde cada nodo tiene las reglas que le afectan.
3. **Fusión en el Árbol de Renderizado (*Render Tree*):** El navegador cruza el DOM con el CSSOM. **Cuidado:** los nodos con `display: none` o etiquetas que no se muestran (como `<head>`, `<meta>`, `<script>`) **no forman parte del Render Tree**. En cambio, elementos con `visibility: hidden` sí están en el Render Tree porque ocupan espacio visual.
4. **Cálculo de Geometría (*Layout* o *Reflow*):** El navegador determina la posición y dimensiones exactas en píxeles de cada caja en la pantalla (`width`, `height`, coordenadas relativas al viewport).
5. **Pintado (*Paint* o *Repaint*):** El motor convierte los elementos geométricos en píxeles reales dibujados en capas (colores de fondo, textos, sombras, bordes).
6. **Composición (*Composite*):** Si hay varias capas (generadas por aceleración gráfica con GPU, `transform` o `opacity`), la GPU las superpone en el orden correcto para proyectarlas en la pantalla.

!!! tip "Por qué importa a un desarrollador"

    Entender este pipeline es vital para el rendimiento: cambiar un `width` o `margin` obliga al navegador a recalcular **Layout + Paint + Composite** (costoso), mientras que animar un `transform` o `opacity` solo ejecuta **Composite** directamente en la GPU (fluido a 60/120 fps).

!!! failure "Anti-patrón: estilos directos"

    Usar atributos presentacionales obsoletos (`<font>`, `<center>`, `align="..."`) o estilos en línea para todo. El currículo (**RA 2**, CE b–c) distingue explícitamente *estilos directos* de *hojas externas*: los directos son la excepción (personalización puntual, email marketing), no la norma.

## 2. Breve historia (contexto suficiente para examen)

| Año | Hito |
|---|---|
| 1994 | Hakon Wim Lie propone «Style Sheets» como alternativa a las etiquetas presentacionales de HTML. |
| 1996 | **CSS1** (W3C Recommendation). Browsers: solo parcial. |
| 1998 | **CSS2**. Aparecen posicionamiento absoluto/fijo, floats, media types. |
| 2003–2010 | Era de las «workarounds»: hacks de IE, DHTML, table layouts. Nace el movimiento del *web standards* (W3C, WHATWG). |
| 2011 | **CSS2.1** REC (consolidación). Empieza la **modularización de CSS3**. |
| 2009–2015 | Llegan Flexbox, Grid, variables custom, transformaciones 3D, animaciones. |
| 2018–hoy | CSS moderno: `:has()`, subgrid, container queries, nesting nativo, `@layer`, scroll-driven animations… |

!!! info "¿Existe «CSS3»?"

    No hay ninguna especificación llamada «CSS3»: desde 2011 el W3C publica **módulos independientes** con su propio nivel (Selectors L4, Color L5, Grid L2…). Por eso hoy se habla de **CSS moderno** y no de «CSS4».

> **Claves para el examen**: CSS nació para **liberar a HTML de la maquetación**. La ==modularización== (**módulos con niveles** L1/L2/…) sustituyó al mito de «CSS3 vs CSS4».

## 3. Sintaxis

La ==sintaxis== es simple: **selector más bloque de declaraciones**, y el navegador hace el resto.

### 3.1. Anatomía de una regla

!!! example "Anatomía de una regla"

    ```css title="estilos.css" hl_lines="1 3"
    selector {                              /* (1)! */
      propiedad: valor;
      otra-propiedad: valor2 !important;    /* (2)! */
    }
    ```

    1.  **Selector** + bloque `{ }`: deciden **a qué elementos** llega la regla.
    2.  Cada **declaración** es un par `propiedad: valor` cerrado con **punto y coma**; `!important` altera la cascada (ver 6.3).

- **Selector**: qué elementos se ven afectados ([unidad 02 completa](02-selectores.md)).
- **Bloque de declaraciones**: entre llaves `{ }`.
- **Declaración**: par `propiedad: valor` terminado por **punto y coma** `;`.
- **Comentario**: `/* así */` (no existe comentario de línea).
- **At-rule**: reglas que empiezan por `@` (`@media`, `@import`, `@keyframes`, `@font-face`, `@layer`…). Tienen dos formas:
    - *con bloque* (`@media (min-width: 600px) { … }`)
    - *con prefijo/sufijo* (`@import url("otro.css");`)

### 3.2. Errores de sintaxis y su efecto

| Error | Consecuencia |
|---|---|
| Falta `;` entre declaraciones | Se ignora el **resto del bloque** hasta el siguiente `;` válido o el `}`. |
| Propiedad desconocida | Se ignora esa declaración (el navegador descarta lo que no entiende). |
| Valor inválido | Se ignora la declaración. |
| Falta `{` o `}` | Puede invalidar varias reglas siguientes. |

!!! info "Tolerancia del navegador"

    El navegador aplica un principio de **tolerancia**: ignora lo que no entiende y sigue procesando. Es la base de la *progressive enhancement* (**mejora progresiva**): escribe CSS estándar y añade mejoras que los navegadores nuevos aplicarán.

### 3.3. At-rules frecuentes (mapa general)

Todas empiezan por `@`; este es el mapa de las ==at-rules== que se reparten por todo el curso:

| At-rule | Función | Unidad donde se profundiza |
|---|---|---|
| `@import` | Importar otra hoja | 01.5 |
| `@media` | Estilos condicionales por características del dispositivo | 10 |
| `@supports` | Estilos condicionales por soporte de propiedades | 12 |
| `@font-face` | Definir fuentes personalizadas | 08 |
| `@keyframes` | Definir animaciones | 11 |
| `@layer` | Capas de la cascada | 12 |
| `@property` | Registrar propiedades personalizadas tipadas | 12 |
| `@container` | Consultas de contenedor | 10 |
| `@scope` | Alcance limitado de reglas | 12 |
| `@page` | Márgenes y formato de impresión | 14 |
| `@charset` | Codificación de caracteres (debe ir en la primera línea) | 01 |
| `@namespace` | Espacios de nombres XML (raro en web práctica) | — |

## 4. Formas de incluir CSS

### 4.1. Estilo en línea (atributo `style`)

```html title="index.html"
<p style="color: crimson; font-size: 1.2rem;">Personalizado</p> <!-- (1)! -->
```

1.  El atributo `style` admite declaraciones separadas por `;`: es el **origen más específico** sin `!important`.

- **Máxima especificidad** (sin `!important` externo).
- No se puede cachear ni reutilizar; duplica código.
- Usos legítimos: personalización dinámica desde JS, plantillas con valores únicos, emails.
- El RA 2 del 0615 lo llama «definir estilos de forma directa»: se evalúa saber **cuándo NO** usarlo.

### 4.2. Hoja interna (elemento `<style>`)

```html title="index.html"
<head>
  <style>
    .nota { background: #fff8dc; padding: 0.5rem; }
  </style>
</head>
```

- Válido en `<head>` y también dentro de `<body>` (HTML5 lo permite para estilos locales de una sección o componente); en producción, preferir hoja externa.
- Útil para componentes autocontenidos, prototipos, islands. En producción, preferir externa.

### 4.3. Hoja externa (elemento `<link>`) — la norma

Es la **forma recomendada**: la ==hoja externa== concentra en uno o varios ficheros todo el CSS del proyecto.

```html title="index.html" hl_lines="2"
<head>
  <link rel="stylesheet" href="/css/base.css">
  <link rel="stylesheet" href="/css/layout.css">
  <link rel="stylesheet" href="/css/components.css">
</head>
```

- **Cacheable**: el navegador la guarda y no vuelve a descargarla.
- Separación total de contenidos.
- Orden de aparición importa para la cascada (igual especificidad → gana la última).
- Atributos útiles:
    - `media="print"` / `media="screen and (min-width: 768px)"`: aplica solo si la consulta es cierta (evita transferir CSS innecesario).
    - `disabled="true"`: hoja desactivada (base técnica de las **hojas alternativas**, ver 4.5).
    - `rel="preload" as="style"` + intercambio: patrón anti render-blocking (unidad 14).

### 4.4. `@import`

```css title="main.css"
/* main.css */
@import url("reset.css");
@import url("layout.css") screen;
```

- Solo puede aparecer **al inicio** de la hoja (antes de cualquier regla, salvo `@charset`/`@layer` statement).
- Cada ==`@import`== genera una **petición adicional** (cascada de peticiones → peor rendimiento). Preferir varios `<link>`.
- Acepta condición `media` tras la URL.

### 4.5. Hojas de estilo alternativas (CE d del RA 2, módulo 0615)

Tres mecanismos históricos/prácticos:

1. **Atributo `disabled` en `<link>`**: el autor o el usuario (menú de hojas alternativas) activa/desactiva hojas completas.
2. **`media` + JS**: cambiar el valor de `media` permite alternar variantes (p. ej., tema denso vs. cómodo).
3. **Convención moderna**: en lugar de «hojas alternativas» propiamente dichas, hoy se implementan **temas** mediante custom properties + `data-theme` o `prefers-color-scheme` (unidad 12). Es la evolución natural que espera el mercado laboral.

```html title="index.html"
<!-- Variante clásica -->
<link id="tema-a" rel="stylesheet" href="tema-clasico.css">
<link id="tema-b" rel="alternate stylesheet" title="Tema alto contraste"
      href="tema-contraste.css" disabled> <!-- (1)! -->
<script>
  // Alternar: document.getElementById('tema-b').disabled = false;
</script>
```

1.  La hoja `alternate` nace **desactivada**; JavaScript la activa cambiando su atributo `disabled`.

!!! info "¿Qué forma de inclusión elijo?"

    - Proyecto real → **`<link>` externo**: cacheable y mantenible.
    - Componente autocontenido o prototipo → **`<style>`**.
    - Valor único dinámico → **estilo en línea**, solo si no se puede resolver con CSS.
    - Reglas compartidas entre hojas → `@import`, aunque por **rendimiento** conviene repetir `<link>`.

## 5. La cascada: ¿Quién gana cuando hay conflicto?

El nombre de CSS proviene precisamente de la palabra **Cascada**. En una web real, un elemento HTML (como un botón o un párrafo) puede verse afectado por decenas de reglas escritas en diferentes archivos, estilos por defecto del navegador o estilos en línea. Cuando dos o más reglas definen la **misma propiedad** (por ejemplo, `color: blue` vs `color: red`), el navegador no puede mostrar ambos: necesita un algoritmo estricto para desempatar.

Ese algoritmo procesa el conflicto en **tres fases secuenciales** (especificación *CSS Cascading and Inheritance Level 5/6*):

```text title="flujo-cascada.txt"
Conflicto de propiedades
   │
   ▼
¿Tienen distinto Origen o Importancia? ──(SÍ)──► Gana el origen más prioritario
   │ (NO)
   ▼
¿Pertenecen a distintas @layer?        ──(SÍ)──► Gana la capa con prioridad
   │ (NO)
   ▼
¿Tienen distinta Especificidad?        ──(SÍ)──► Gana el selector más específico
   │ (NO)
   ▼
Orden en el código                     ────────► Gana la última declaración leída
```

### Fase 1 — Origen e importancia

El navegador clasifica el origen del código en tres procedencias:

1. **Agente de usuario (*User-Agent*):** Son los estilos que trae Firefox, Chrome o Safari de fábrica (por ejemplo, que los enlaces sean azules y subrayados, o que `<h1>` tenga `font-size: 2em`).
2. **Usuario:** Estilos personalizados que el visitante ha configurado en su navegador o mediante extensiones (muy habitual en personas con baja visión que fuerzan tipografías legibles o alto contraste).
3. **Autor:** El código CSS que tú escribes como programador web.

El orden de victoria (de menor a mayor fuerza) es:

1. **Estilos del agente de usuario** (los más débiles; cualquier CSS tuyo los pisa).
2. **Estilos del usuario normales** (preferencias generales del visitante).
3. **Estilos del autor normales** (tu código habitual en `.css`).
4. **Estilos del autor con `!important`** (fuerza bruta en tu CSS).
5. **Estilos del usuario con `!important`** (los reyes absolutos; diseñados por el W3C para que una persona con discapacidad visual siempre pueda imponer su tamaño de letra o contraste sobre la decisión de cualquier desarrollador).

**Regla nemotécnica:** `!important` del usuario > `!important` del autor > autor normal > usuario normal > navegador por defecto.

### Fase 2 — Capas (`@layer`)

Si el origen y la importancia son idénticos, entran en juego las capas introducidas en CSS moderno (`@layer`). Las reglas dentro de capas tienen **menor prioridad** que el CSS tradicional sin capas, y entre distintas capas gana siempre la que se declaró más tarde. Esto permite importar librerías externas (como Bootstrap o Tailwind) en una capa baja y asegurarte de que tus propios estilos las sobrescriban sin pelearte con la especificidad (se detalla en la unidad 12).

### Fase 3 — Especificidad y orden

Si las declaraciones están en el mismo origen y en la misma capa, la cascada pasa a evaluar la **especificidad del selector**. Y si dos selectores tienen exactamente el mismo peso matemático, se aplica la regla más sencilla: **gana el último que aparece en el documento**.

---

## 6. Especificidad: La balanza de los selectores

La ==especificidad== es la puntuación o peso que el navegador asigna a un selector. Determina cuán "preciso" o "concreto" es el selector al apuntar a un elemento.

### 6.1. El modelo de puntuación `(I, A, B, C)`

Para evitar ambigüedades, el W3C define la especificidad como una tupla de cuatro columnas: **`(Inline, ID, Clase/Atributo/Pseudo-clase, Tipo/Pseudo-elemento)`**:

| Columna | Nombre | ¿Qué elementos puntúa? | Ejemplo |
|---|---|---|---|
| **I** | Estilo en línea | Declaraciones puestas en el HTML con el atributo `style="..."`. | `<p style="...">` |
| **A** | Identificadores (ID) | Cada selector que empiece por almohadilla `#`. | `#menu`, `#login-form` |
| **B** | Clases, atributos y pseudo-clases | Clases (`.btn`), atributos (`[type="text"]`, `[required]`) y pseudo-clases (`:hover`, `:focus`, `:nth-child()`). | `.tarjeta`, `[disabled]`, `:hover` |
| **C** | Tipos y pseudo-elementos | Nombres de etiquetas HTML (`p`, `div`, `h1`) y pseudo-elementos (`::before`, `::after`). | `h1`, `li`, `::before` |

!!! danger "La regla sagrada: ¡Nunca hay llevada matemática!"

    Muchos alumnos principiantes piensan que la especificidad es un número decimal (por ejemplo, pensar que `(0, 1, 0)` es 10 y `(0, 0, 1)` es 1). **Esto es un error crítico.** 
    
    Las columnas se comparan **de izquierda a derecha**:
    
    - Un valor mayor en la columna **I** aplasta a cualquier cantidad en **A, B o C**.
    - Un valor mayor en la columna **A** (un solo `#id`) gana a un millón de clases juntas `(0, 1000, 0)`.
    - Un valor mayor en la columna **B** (una clase) gana a cualquier cantidad de etiquetas HTML `(0, 0, 50)`.
    
    No existe la "llevada": diez selectores de etiqueta jamás equivaldrán ni superarán a una sola clase.

### 6.2. Ejemplos trabajados

| Selector | (A,B,C) | Comentario |
|---|---|---|
| `h1` | (0,0,1) | tipo |
| `.titulo` | (0,1,0) | clase |
| `#cabecera h1` | (1,0,1) | 1 ID (`#cabecera`) + 1 tipo (`h1`) |
| `nav ul li a:hover` | (0,1,4) | 1 pseudo-clase + 4 tipos |
| `.card .card__titulo` | (0,2,0) | dos clases |
| `#app .card :is(h2, h3)` | (1,1,0) | `:is()` toma la especificidad de su argumento de mayor peso |
| `:where(.a, .b) p` | (0,0,1) | `:where()` siempre aporta **cero** |
| `article:has(> figure) h2` | (0,0,3) | `:has()` adopta la especificidad de su argumento |

> **Claves para el examen**: saber calcular la especificidad de selectores compuestos y explicar por qué `:where()` existe (aportar cero especificidad para facilitar overrides) y cómo funciona `:is()` (adopta la del argumento más específico).

!!! question "Especificidad en la práctica"

    ¿Gana `#menu .enlace` o `nav ul li .enlace:hover`? ¿Y si el primero se escribe `.menu .enlace`?

    ??? success "Respuesta"

        `#menu .enlace` = **(1,1,0)** vence a **(0,2,3)**: un único **ID** supera cualquier número de clases y tipos, porque **no hay llevada**. Sin el ID, `.menu .enlace` = **(0,2,0)** y entonces gana `nav ul li .enlace:hover` por sus **tres tipos**.

### 6.3. `!important`

- **Invierte la cascada**: ==`!important`== salta a la capa de importancia superior.
- **No** supera a un `!important` del usuario.
- Mal uso habitual: «para que me haga caso». Genera **deuda técnica**: cada override posterior necesita otro `!important`.
- Usos razonables: anular estilos de librerías de terceros que no se pueden tocar, forzar accesibilidad (p. ej., mostrar foco), emergencia en producción.

!!! warning "Error común"

    Pensar que `!important` «gana siempre». Pierde ante un `!important` de **hoja de usuario** y, dentro del mismo origen, sigue sometiéndose a **especificidad** y **orden**.

## 7. Herencia: El ADN visual entre padres e hijos

La ==herencia== en CSS es el mecanismo por el cual ciertas propiedades aplicadas a un elemento padre se transmiten automáticamente a todos sus descendientes en el árbol DOM.

### 7.1. ¿Por qué algunas propiedades se heredan y otras no?

Para entenderlo sin memorizar listas interminables, piensa en el **sentido común del diseño**:

- **Propiedades tipográficas y de texto (SÍ se heredan por defecto):**
    - Ejemplos: `color`, `font-family`, `font-size`, `line-height`, `letter-spacing`, `text-align`, `cursor`.
    - *¿Por qué?* Si defines en el `<body>` que la tipografía de tu web es `font-family: 'Segoe UI', sans-serif` y el color es gris oscuro, esperas que todos los párrafos, listas, títulos y span de la página utilicen esa misma fuente sin tener que escribirlo cien veces.
- **Propiedades de caja y geometría (NO se heredan por defecto):**
    - Ejemplos: `margin`, `padding`, `border`, `background`, `width`, `height`, `position`, `display`.
    - *¿Por qué?* Imagina el desastre si el borde o el padding se heredasen: le pondrías `border: 2px solid red` a un `<section>` ¡y automáticamente cada `<p>`, `<strong>`, `<a>` e `<img>` dentro del section tendría su propio borde rojo individual! Las cajas hijas deben mantener su independencia espacial[^1].

!!! note "La excepción de los controles de formulario"

    Elementos como `<input>`, `<button>`, `<textarea>` y `<select>` **no heredan** la tipografía del `<body>` por defecto en las hojas de estilo del navegador (user-agent). Por eso es una práctica estándar en cualquier proyecto añadir:
    ```css
    button, input, select, textarea {
      font-family: inherit;
      font-size: inherit;
    }
    ```

### 7.2. Palabras clave universales de herencia

CSS proporciona cuatro palabras clave universales que pueden asignarse a **cualquier propiedad** para alterar deliberadamente este comportamiento:

| Palabra clave | Significado y uso práctico |
|---|---|
| `inherit` | **Fuerza la herencia:** Hace que el elemento tome el valor exacto de su padre directo, incluso si la propiedad normalmente no se hereda (ej: `border: inherit;` o `font-family: inherit;` en botones). |
| `initial` | **Valor original de fábrica de la W3C:** Devuelve la propiedad al valor especificado en el estándar internacional (ej: en `color` suele ser negro; en `display` suele ser `inline`). **Cuidado:** `initial` rompe la herencia por completo. |
| `unset` | **Comportamiento natural:** Actúa como `inherit` si la propiedad es de las que se heredan por naturaleza (como el texto), y actúa como `initial` si es una propiedad que no se hereda (como los márgenes). |
| `revert` | **Deshace tus estilos y vuelve a la cascada previa:** Ignora los estilos del autor y adopta el valor que le otorgaba la hoja de estilos del navegador o del usuario. Muy útil para devolver un `<button>` o un `<dialog>` a su apariencia nativa. |
| `revert-layer` | Igual que `revert`, pero solo retrocede a la capa anterior de `@layer`. |

### 7.3. Reset y normalize

- **Reset** (p. ej., *modern-normalize*, *sanitize*): anula defaults del navegador para **partir de cero**.
- **Normalize**: conserva los defaults razonables y corrige solo inconsistencias entre navegadores.
- Hoy, con `@layer` y `all: initial/unset`, se pueden hacer resets quirúrgicos:

```css title="reset.css" hl_lines="2"
@layer reset {
  *, *::before, *::after { box-sizing: border-box; }
  body, h1, h2, p, figure { margin: 0; }
  img, video { max-width: 100%; display: block; }
}
```

> **Claves para el examen**: diferenciar `initial` vs `inherit` vs `unset` es pregunta clásica.

## 8. Valores universales y unidades básicas

Todo valor dimensional puede ser:

- **Número puro** (solo en propiedades adimensionales: `z-index`, `opacity`, `flex-grow`…).
- **Longitud**: `px`, `rem`, `em`, `%`, `vw/vh`, `ch`, `ex`… (unidad 08 completa).
- **Keyword** propio de cada propiedad.
- **Función**: `calc()`, `clamp()`, `var()`, `url()`, `rgb()`…

Reglas generales:

- Los valores son **case-insensitive** para keywords y funciones; los URLs y `font-family` pueden serlo según contexto.
- Las ==`calc()`== permiten aritmética mixta: `width: calc(100% - 2rem);`.
- `var(--mi-var, fallback)` introduce las **custom properties** (unidad 12).

## 9. Validación y depuración (CE h del RA 2)

El CE h pide ==herramientas de validación== de hojas de estilo: aquí están las **tres que se citan en examen**.

### 9.1. Validador W3C (Jigsaw)

- <https://jigsaw.w3.org/css-validator/> : comprueba sintaxis y propiedades contra las specs.
- Limitaciones: valida CSS plano; no entiende preprocesadores (compila antes) ni todas las features muy recientes.
- En la práctica profesional se complementa con **linters**: `stylelint` (reglas configurables, integración CI).

### 9.2. DevTools del navegador

- **Panel Elements/Inspector**: estilos aplicados por selector, tachados (perdidos en la cascada), especificidad calculada.
- **Computed**: valor final resuelto.
- **Styles → View transition timeline / Layers**: inspeccionar capas de composición.
- **Rendering**: forzar repaints, mostrar layout shifts, emular `prefers-reduced-motion`.
- **Performance**: identificar problemas de layout/paint (unidad 14).

> **Claves para el examen**: el criterio «se han utilizado herramientas de validación de hojas de estilos» se cubre citando Jigsaw + stylelint + DevTools, y sabiendo qué detecta cada uno.

---

## 10. Ejemplo práctico: tarjeta de componente con cascada, herencia y reset controlado

El siguiente ejemplo integra todos los conceptos fundamentales de la unidad: separación de responsabilidades mediante archivo externo, reset con capas de cascada (`@layer`), diseño basado en tokens/variables semánticas, herencia natural y forzada en controles de interfaz, y resolución limpia de especificidad sin necesidad de recurrir al destructivo `!important`.

```html title="tarjeta-curso.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fundamentos de CSS · Tarjeta de Módulo</title>
  <!-- Inclusión recomendada por estándar: enlace externo no bloqueante -->
  <link rel="stylesheet" href="css/estilos.css">
</head>
<body>
  <main class="contenedor">
    <article class="tarjeta tarjeta--destacada">
      <header class="tarjeta__cabecera">
        <span class="badge">DAW · 1.º Curso</span>
        <h2 class="tarjeta__titulo">Lenguajes de Marcas</h2>
      </header>
      
      <p class="tarjeta__descripcion">
        Aprende a estructurar documentos con HTML5 semántico y a estilizarlos con CSS moderno, cascada predecible y accesibilidad universal.
      </p>

      <footer class="tarjeta__pie">
        <span class="tarjeta__horas">96 horas lectivas</span>
        <button type="button" class="btn btn--primario">Ver temario</button>
      </footer>
    </article>
  </main>
</body>
</html>
```

```css title="css/estilos.css"
/* 1. Capa de reset: prioridad mínima en la cascada */
@layer reset {
  *, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    min-height: 100vh;
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
  }

  /* Excepción clásica de formularios: forzar herencia */
  button, input, select, textarea {
    font-family: inherit;
    font-size: inherit;
    color: inherit;
  }
}

/* 2. Capa base y tokens de diseño */
@layer tema {
  :root {
    --color-fondo: #f8fafc;
    --color-superficie: #ffffff;
    --color-texto: #0f172a;
    --color-texto-secundario: #475569;
    --color-primario: #0284c7;
    --color-primario-hover: #0369a1;
    --color-borde: #e2e8f0;
    --color-destacado: #38bdf8;
    
    --fuente-principal: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
    --radio-borde: 0.75rem;
    --sombra-tarjeta: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  }

  body {
    background-color: var(--color-fondo);
    color: var(--color-texto);
    font-family: var(--fuente-principal);
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 1.5rem;
  }
}

/* 3. Capa de componentes */
@layer componentes {
  .tarjeta {
    background-color: var(--color-superficie);
    border: 1px solid var(--color-borde);
    border-radius: var(--radio-borde);
    box-shadow: var(--sombra-tarjeta);
    max-width: 24rem;
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  /* Modificador de especificidad limpia (0, 2, 0) */
  .tarjeta.tarjeta--destacada {
    border-color: var(--color-destacado);
    border-width: 2px;
  }

  .badge {
    display: inline-block;
    align-self: flex-start;
    padding: 0.25rem 0.625rem;
    background-color: #e0f2fe;
    color: #0369a1;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: 9999px;
  }

  .tarjeta__titulo {
    font-size: 1.35rem;
    color: var(--color-texto);
    line-height: 1.25;
  }

  .tarjeta__descripcion {
    color: var(--color-texto-secundario);
    font-size: 0.95rem;
  }

  .tarjeta__pie {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 0.5rem;
    padding-top: 1rem;
    border-top: 1px solid var(--color-borde);
  }

  .tarjeta__horas {
    font-size: 0.85rem;
    color: var(--color-texto-secundario);
    font-weight: 600;
  }

  .btn {
    border: none;
    cursor: pointer;
    padding: 0.5rem 1rem;
    border-radius: 0.375rem;
    font-weight: 600;
    transition: background-color 0.2s ease;
  }

  .btn--primario {
    background-color: var(--color-primario);
    color: #ffffff;
  }

  .btn--primario:hover {
    background-color: var(--color-primario-hover);
  }

  .btn:focus-visible {
    outline: 2px solid var(--color-primario);
    outline-offset: 2px;
  }
}
```

---

### 10.1 Explicación detallada: ¿Por qué se usa cada propiedad y para qué sirve?

A continuación se detalla la justificación técnica y de arquitectura CSS empleada en cada bloque:

#### 1. Inclusión externa `<link rel="stylesheet">`
- **¿Para qué sirve?** Vincula el documento HTML con la hoja de estilos externa `css/estilos.css`.
- **¿Por qué se usa aquí?** Es la regla fundamental de la **separación estricta de responsabilidades (SoC)**. Permite que el archivo CSS sea cacheado por el navegador tras la primera descarga, compartiendo los estilos en cientos de páginas sin transferir bytes duplicados y evitando la mala práctica de estilos en línea (`style="..."`).

#### 2. Declaración de capas de cascada `@layer`
- **¿Para qué sirve?** Organiza las reglas en capas lógicas explícitas: `@layer reset`, `@layer tema` y `@layer componentes`.
- **Comportamiento en la cascada:** Las capas declaradas después tienen mayor prioridad que las anteriores. Esto resuelve de raíz el problema clásico del CSS: una regla de componente en `@layer componentes` siempre ganará a un selector de reset en `@layer reset`, independientemente de la especificidad numérica de cada selector.

#### 3. Reset universal y modelo de caja
- **`*, *::before, *::after`:** Selector universal ampliado a pseudoelementos.
- **`box-sizing: border-box`:** Cambia el modelo de caja de fábrica del W3C (`content-box`) a `border-box`. Garantiza que al aplicar `padding` o `border` a cualquier caja, su ancho total (`width`) no crezca inesperadamente, eliminando desbordamientos horizontales.
- **`margin: 0; padding: 0;`:** Elimina los márgenes erráticos que los distintos motores de navegador inyectan por defecto en títulos, listas y párrafos.

#### 4. Herencia natural y la regla `inherit` en controles
- **Herencia en `body`:** Propiedades como `color`, `font-family` y `line-height` declaradas en el `<body>` se propagan automáticamente en cascada a todos los elementos hijos (títulos, párrafos, spans).
- **Forzado de herencia en `button, input, select, textarea`:**
    - Los controles de formulario son una **excepción histórica**: la hoja de estilos nativa del navegador (*user-agent stylesheet*) les asigna su propia tipografía de sistema (`system font`) ignorando al padre.
    - Al declarar `font-family: inherit; font-size: inherit; color: inherit;`, obligamos a los botones a adoptar la tipografía corporativa del proyecto de forma limpia.

#### 5. Tokens semánticos en `:root`
- **¿Para qué sirve?** `:root` representa el elemento raíz (`<html>`) con la máxima jerarquía del documento.
- **Variables CSS (`--color-*`, `--fuente-*`):** Permiten centralizar la paleta de colores y tokens de espaciado. Si el cliente solicita cambiar el color corporativo principal, solo se edita el valor de `--color-primario` en una sola línea, propagándose instantáneamente por toda la aplicación.

#### 6. Especificidad y cascada en `.tarjeta` y `.tarjeta.tarjeta--destacada`
- **Especificidad de `.tarjeta`:** Una clase simple tiene un peso de `(0, 1, 0)`.
- **Especificidad de `.tarjeta.tarjeta--destacada`:** Al encadenar dos clases, su especificidad se eleva limpiamente a `(0, 2, 0)`.
- **Sin `!important`:** El borde azul destacado sobreescribe al borde gris estándar de forma estrictamente matemática y predecible. No se utiliza `!important`, evitando deudas técnicas que bloqueen futuras variaciones de diseño.

#### 7. Accesibilidad visual con `:focus-visible`
- **`outline: 2px solid var(--color-primario)` con `outline-offset: 2px`:** Proporciona un anillo de enfoque nítido y separado visualmente del botón cuando el usuario navega mediante teclado (<kbd>Tab</kbd>). Cumple con el criterio de conformidad **WCAG 2.4.7 (Foco visible)** sin perjudicar la estética cuando un usuario hace clic con el ratón.

---

## 11. Resumen de la unidad

1. CSS separa **presentación** de estructura: mantenibilidad, consistencia, accesibilidad, rendimiento.
2. Sintaxis: `selector { prop: valor; }`; at-rules con `@`; el navegador **ignora** lo que no entiende (tolerancia → mejora progresiva).
3. Inclusión: en línea (excepción), `<style>` (componentes), **`<link>` externo (norma)**, `@import` (evitar por rendimiento).
4. Cascada: **origen/importancia → capas → especificidad → orden**.
5. Especificidad: `(ID, clase/pseudo-clase/atributo, tipo/pseudo-elemento)`; `:where()` = 0; `:is()` = máximo de sus argumentos; en línea y `!important` fuera de escala.
6. Herencia: solo propiedades de texto/tipo; keywords `initial/inherit/unset/revert`.
7. Valida con Jigsaw/stylelint y depura con DevTools.

!!! success "Checklist de la unidad"

    - [ ] Diferencio **estilo en línea**, **hoja interna** y **hoja externa**, y sé cuándo usar cada una.
    - [ ] Calculo la **especificidad** de selectores compuestos, incluidos `:is()`, `:where()` y `:has()`.
    - [ ] Explico la cascada por **fases**: origen e importancia, capas, especificidad y orden.
    - [ ] Distingo `initial`, `inherit`, `unset` y `revert`.
    - [ ] Valido con **Jigsaw** y **stylelint** y depuro con **DevTools**.

## 12. Autoevaluación rápida

1. ¿Por qué `@import` es peor que varios `<link>`?
2. Calcula la especificidad de `#main article .post:not(.borrador):hover h2::first-line`.
3. ¿Qué gana: `.a { color: red }` (hoja 1) frente a `p.a { color: blue }` (hoja 2)? ¿Y si la segunda lleva `!important`?
4. ¿`initial` o `inherit` para reiniciar `margin` en un `div` dentro de otro `div` con `margin: 2rem`?
5. ¿Qué es una «hoja de estilo alternativa» y cómo se implementa hoy?

!!! tip "Claves para el examen"

    - **Cascada** por fases: origen e importancia → capas (`@layer`) → especificidad → orden.
    - **Especificidad** `(A,B,C)`: ID, clase/pseudo-clase/atributo, tipo/pseudo-elemento; **no hay llevada**.
    - `:where()` aporta **cero**; `:is()` y `:has()` adoptan la del argumento más pesado.
    - `!important` **no** gana siempre: pierde ante el `!important` de la hoja de usuario.
    - Herencia: `initial` (valor spec) vs `inherit` (del padre) vs `unset` vs `revert`.
    - Inclusión: **`<link>` externo** como norma; `@import` solo si no hay alternativa.
    - Validación: **Jigsaw** + **stylelint** + **DevTools** = CE h del RA 2.

[^1]: Fuente: MDN Web Docs, tabla «Inherited» de cada propiedad de CSS.

*[W3C]: World Wide Web Consortium
*[RA]: Resultado de aprendizaje
*[CE]: Criterio de evaluación
