---
icon: lucide/layers
title: "HTML 07 - Estructura semántica y ARIA"
description: "Estructura semántica: elementos de sección, landmarks, skip link, jerarquía de encabezados y uso correcto de ARIA."
modulo: "LMH (0373) / DIW (0615) / DI (0488)"
unidad: 7
fecha: "2026-09-29"
---

# HTML 07 — Estructura semántica y ARIA

Una página tiene cabecera, menú, contenido principal, barra lateral y pie; si esa organización solo existe en CSS y `<div>`, el navegador, el buscador y el lector de pantalla la ignoran. Aquí lo construimos: esqueleto, *skip link*, encabezados y ARIA **justo y necesario**.

!!! note "Conocimientos previos"

    - Estructura del documento: [01-introduccion-html5.md](01-introduccion-html5.md). Enlaces y anclas: [03-enlaces-y-recursos.md](03-enlaces-y-recursos.md).
    - Qué es un landmark (clase de interfaces → [../css/13-accesibilidad-usabilidad.md](../css/13-accesibilidad-usabilidad.md)).
    - Formularios, si tu práctica los incluye: [06-formularios-html5.md](06-formularios-html5.md).

## 1. Por qué la semántica

### 1.1 Tres lectores del mismo HTML

- **Máquina** (buscadores): busca la estructura; con una sopa de `<div>` no distingue el artículo de un anuncio.
- **Accesibilidad** (lectores de pantalla y teclado): busca landmarks y orden de lectura; sin ellos la navegación es "ciega".
- **Mantenimiento** (tú, en unos meses): con `<div>` solo queda adivinar la intención por las clases.

La semántica es ==información que ya viaja en el HTML==: sirve para SEO, accesibilidad y legibilidad del código.

### 1.2 El coste de la "divitis"

```html title="divitis.html" hl_lines="2 4"
<!-- ❌ Cuatro divs: la máquina solo ve cajas -->
<div class="cabecera"><div class="menu"><div class="titulo">DAW</div></div></div>
<!-- ✅ mismo aspecto, significado explícito -->
<header class="cabecera"><nav class="menu"><h1>DAW</h1></nav></header>
```

Con `<div>` hay que añadir a mano `role`, `tabindex` y JavaScript: **reescribir lo que el HTML ya regala** (ejercicio "Desmontando el *divitis*" → [09-ejercicios.md](09-ejercicios.md)).

## 2. Elementos de sección

### 2.1 Los siete elementos estructurales y sus *landmarks*

Para comprender los elementos semánticos de HTML5, los alumnos deben entender primero el concepto de **punto de referencia o *landmark***:

> **Analogía pedagógica:** Imagina entrar a un aeropuerto o una estación de tren grande. No lees cada cartel ni cada puerta una por una; buscas los carteles grandes de orientación: *"Facturación"*, *"Puertas de embarque"*, *"Recogida de equipajes"*.
> 
> En la web ocurre exactamente lo mismo: una persona ciega no lee la página de arriba abajo como un documento de Word. Utiliza atajos de teclado de su lector de pantalla (como pulsar la tecla ++d++ o ++m++) para **saltar directamente de una sección mayor a otra**. Los *landmarks* son esos grandes carteles de orientación.

| Elemento HTML | Significado semántico | *Landmark* ARIA implícito | Regla de uso estricta |
|---|---|---|---|
| `<header>` | Cabecera introductoria de la página o de una sección | `banner` (solo si es hijo directo de `<body>`) | Contiene logos, eslóganes y títulos principales. No confundir con `<head>`. |
| `<nav>` | Bloque con enlaces de navegación importantes | `navigation` | Solo para menús principales, índices o paginaciones; **nunca** para listas de enlaces sueltas del pie. |
| `<main>` | Contenido central, exclusivo y principal de la página | `main` | **Estrictamente ÚNICO por página**. No puede haber dos elementos `<main>` visibles a la vez. |
| `<article>` | Contenido autocontenido e independiente | — | Aquello que tendría sentido por sí solo si se publicara en un feed RSS o en otra web (noticia, post, producto, comentario). |
| `<section>` | Agrupación temática genérica de contenido | `region` (solo si tiene un encabezado y nombre accesible) | Debe incluir un encabezado (`<h2>`-`<h6>`). Si solo necesitas una caja para estilizar con CSS, usa `<div>`. |
| `<aside>` | Contenido tangencial o complementario | `complementary` | Barras laterales, glosarios, enlaces relacionados, publicidad o biografías cortas del autor. |
| `<footer>` | Pie de página o cierre de un bloque | `contentinfo` (solo si es hijo directo de `<body>`) | Información de copyright, autoría, enlaces legales y datos de contacto corporativos. |

### 2.2 `section` vs `div`: el criterio

Bloque con ==tema propio y encabezado propio== (suena a "sección de…") → `<section>`; bloque que existe **solo por la maquetación** (suena a "caja de…") → `<div>`.

```html title="seccion-vs-div.html"
<!-- ✅ section: tema + encabezado propio -->
<section aria-labelledby="horario">
  <h2 id="horario">Horario de módulos</h2>
  <table>...</table>
</section>

<!-- ❌ puro estilo, sin tema ni encabezado -->
<div class="contenedor-tarjetas"><div class="tarjeta">...</div></div>
```

## 3. Esqueleto de página completo

### 3.1 Blog con cabecera, menú, artículo, barra lateral y pie

```html title="estructura.html"
<body>
  <!-- Primer elemento del DOM: salta al contenido con Tab -->
  <a class="skip-link" href="#contenido">Saltar al contenido principal</a> <!-- (1)! -->

  <!-- header hijo directo de body => landmark "banner" -->
  <header class="cabecera">
    <h1 class="logo"><a href="/">El Cuaderno de Apuntes</a></h1>
    <nav aria-label="Principal">
      <ul>
        <li><a href="/" aria-current="page">Inicio</a></li>
        <li><a href="/lenguajes-de-marcas">Lenguajes de marcas</a></li>
        <li><a href="/contacto">Contacto</a></li>
      </ul>
    </nav>
  </header>

  <div class="rejilla">
    <!-- main => landmark "main"; SOLO UNO por página -->
    <main id="contenido" tabindex="-1"> <!-- (2)! -->
      <article>
        <header>
          <h2>Por qué escribimos HTML semántico</h2>
          <p><time datetime="2026-09-29">29 de septiembre de 2026</time> — Marta Ruiz</p>
        </header>
        <!-- section con encabezado propio -->
        <section aria-labelledby="ejemplos">
          <h3 id="ejemplos">Ejemplos de etiquetas</h3>
          <p><code>header</code>, <code>nav</code>, <code>main</code>…</p>
        </section>
        <footer>
          <!-- pie del artículo: NO es landmark contentinfo -->
          <p>Etiquetas: <a href="/temas/html">HTML</a></p>
        </footer>
      </article>
    </main>

    <!-- aside => landmark "complementary" -->
    <aside class="barra-lateral">
      <section>
        <h2>Entradas relacionadas</h2>
        <ul><li><a href="/entrada/landmarks">Landmarks en 5 minutos</a></li></ul>
      </section>
    </aside>
  </div>

  <!-- footer hijo directo de body => landmark "contentinfo" -->
  <footer class="pie">
    <p>&copy; 2026 El Cuaderno de Apuntes · <a href="/aviso-legal">Aviso legal</a></p>
  </footer>
</body>
```

1.  El *skip link* es el **primer elemento enfocable**: con la primera **Tab** aparece y con **Intro** deja el foco dentro del contenido.

2.  `tabindex="-1"` enfoca `<main>` **sin** añadirlo al recorrido del Tab, que es justo lo que necesita el saltador.

Los landmarks quedan así: `header` → `banner`, `nav` → `navigation`, `main` → `main`, `aside` → `complementary`, `footer` final → `contentinfo`; el `div.rejilla` es ==solo maquetación== (→ [../css/06-grid.md](../css/06-grid.md)). Es el esqueleto del ejercicio del **portafolio semántico** (→ [09-ejercicios.md](09-ejercicios.md)).

---

### 3.1 Explicación detallada: ¿Por qué se usa cada etiqueta y para qué sirve?

A continuación se detalla la función de cada contenedor semántico y atributo de accesibilidad ARIA presentes en la plantilla estructural `estructura.html`:

#### 1. `<a class="skip-link" href="#contenido">` — El enlace de salto (*Skip Link*)
- **¿Para qué sirve?** Es un enlace accesible colocado como el **primerísimo elemento hijo de `<body>`**.
- **¿Por qué es obligatorio en accesibilidad (Criterio WCAG 2.4.1)?**
    - Permite a los usuarios que navegan exclusivamente con teclado o pulsadores saltarse los bloques de contenido repetitivos (como el logotipo y menús de 20 enlaces) con una sola pulsación de la tecla <kbd>Intro</kbd>.
    - Visualmente se oculta fuera de la pantalla mediante CSS y solo se hace visible cuando recibe el foco del teclado (`:focus`).

#### 2. `<header class="cabecera">` — Hito `role="banner"`
- **¿Para qué sirve?** Al ser hijo directo del `<body>`, los navegadores le asignan automáticamente el rol de accesibilidad `banner`.
- **¿Por qué se usa aquí?** Actúa como el encabezado global de todo el sitio web, acogiendo la identidad corporativa (`<h1>` con enlace) y la barra de navegación principal.

#### 3. `<nav aria-label="Principal">` y `aria-current="page"`
- **`aria-label="Principal"`:** Diferencia este menú de navegación de otros posibles menús secundarios que existan en la página (como un menú de pie de página o un índice temático).
- **`aria-current="page"`:**
    - Se coloca en el enlace que apunta a la página en la que el usuario se encuentra actualmente.
    - El lector de pantalla avisa explícitamente: *"Inicio, página actual, enlace"*. Esto evita desorientación en personas ciegas que no pueden percibir el cambio de color visual del enlace activo.

#### 4. `<div class="rejilla">` — Contenedor neutro para CSS Grid
- **¿Para qué sirve?** Es un contenedor `<div>` sin valor semántico.
- **¿Por qué es legítimo su uso aquí?** Porque su único propósito es servir de envoltorio (*wrapper*) para aplicar maquetación visual bidimensional con CSS (`display: grid`), dividiendo la pantalla entre el área de contenido principal y la barra lateral sin interferir en la jerarquía semántica.

#### 5. `<main id="contenido" tabindex="-1">` — Hito principal y recepción de foco
- **`id="contenido"`:** Es el ancla de destino del enlace de salto inicial (`href="#contenido"`).
- **`tabindex="-1"`:**
    - Permite que el elemento `<main>` reciba el foco mediante JavaScript o por salto de enlace de hipertexto, pero **sin añadirlo a la secuencia de tabulación manual**.
    - Resuelve un error clásico de los navegadores: garantiza que, tras pulsar el enlace de salto, la siguiente pulsación de la tecla <kbd>Tab</kbd> avance hacia el primer enlace o botón del artículo, y no vuelva a saltar hacia arriba al menú.

#### 6. `<article>`, `<section aria-labelledby="ejemplos">` y `<footer>` interno
- **`<article>`:** Encapsula la entrada completa del blog como una entidad temática autónoma.
- **`<section aria-labelledby="ejemplos">`:**
    - Subdivide el artículo en un bloque temático coherente.
    - Mediante `aria-labelledby="ejemplos"`, reutiliza el texto del encabezado `<h3>` como su nombre accesible, transformando la sección en un hito navegable identificado (*"Región: Ejemplos de etiquetas"*).
- **`<footer>` dentro de `<article>`:** Cierra el post con metadatos específicos (etiquetas y categorías). A diferencia del footer del body, este footer local no genera un landmark global `contentinfo`.

#### 7. `<aside class="barra-lateral">` — Hito `role="complementary"`
- **¿Para qué sirve?** Aloja contenido tangencialmente relacionado con el documento (entradas recomendadas, enlaces a temas afines, widgets informativos).
- **Accesibilidad:** Los lectores de pantalla reconocen que este bloque no forma parte del flujo de lectura principal y permiten al usuario omitirlo si solo desea leer el artículo.

#### 8. `<footer class="pie">` — Hito `role="contentinfo"`
- **¿Para qué sirve?** Pie de página corporativo del sitio web. Contiene el copyright y el enlace al aviso legal obligatorio.

---

## 4. El *skip link*

### 4.1 Qué es y cómo se escribe

Es el ==primer elemento enfocable== de la página: permite saltarse la cabecera y el menú sin tabular por 30 enlaces.

```html title="skip-link.html" hl_lines="3 6"
<body>
  <!-- Debe ser el PRIMER enlace del DOM -->
  <a class="skip-link" href="#contenido">Saltar al contenido principal</a>
  <header> ... menú con 12 enlaces ... </header>
  <!-- destino: el id de <main>; tabindex="-1" lo enfoca sin entrar en el Tab -->
  <main id="contenido" tabindex="-1"> <h1>...</h1> </main>
</body>
```

```css title="skip-link.css"
.skip-link { position: absolute; left: -9999px; background: #fff; padding: .6rem 1rem; }
.skip-link:focus { left: 0; top: 0; z-index: 1000; }
:focus-visible { outline: 3px solid #0b5fff; outline-offset: 2px; } /* nunca borres el foco */
```

### 4.2 Cómo probarlo con teclado

1. **Tab** una vez: aparece "Saltar al contenido principal".
2. **Intro**: el foco salta a `<main>`; el siguiente **Tab** va al primer enlace *dentro* del contenido, no al menú (y **Shift + Tab** vuelve hacia atrás).
3. En DevTools → *Elements* → *Accessibility*, el nombre accesible del enlace debe ser su texto visible.

Si no lo ves, casi siempre es ==`display: none`== (**tampoco sería enfocable**), que está **después** del menú, o un `href` sin `id` coincidente.

!!! success "Comprueba con teclado"

    - [ ] Con la primera **Tab** aparece el enlace de salto.
    - [ ] Con **Intro** el foco queda en `<main>` (ver *Elements* → nodo seleccionado).
    - [ ] El siguiente **Tab** entra en el contenido, **no** en el menú.
    - [ ] El foco es **visible**: `outline` aplicado, nunca `outline: none`.
    - [ ] En *Accessibility* el nombre accesible del enlace es su texto visible.

## 5. Jerarquía de encabezados y *outline*

### 5.1 Reglas

- **Un solo `<h1>` por página** (título del documento o de la entrada).
- ==Sin saltos de nivel==: `h1` → `h2` → `h3`… Los lectores de pantalla usan los encabezados como índice.
- **Cada sección lleva su nivel estructural**, no el que pida el diseño; **el tamaño es CSS** (`h2 { font-size: 1rem; }` es válido).

!!! quote "WCAG 2.1 — criterio 1.3.1, info y relaciones"

    "La información, la estructura y las relaciones transmitidas mediante la presentación pueden determinarse **programáticamente** o estar disponibles en texto."

    — traducción de la norma. Si el "título" de una sección es solo un `<div>` con fuente grande, esa relación **no** se puede determinar programáticamente y el criterio queda incumplido.

```html title="encabezados.html"
<!-- ❌ Salto de nivel y dos h1 -->
<h1>Curso de HTML</h1><h4>Etiquetas semánticas</h4> <!-- (1)! -->

<!-- ✅ niveles encadenados; el estilo lo pone CSS -->
<h1>Curso de HTML</h1>
  <h2>Etiquetas semánticas</h2> <!-- (2)! -->
    <h3>Elementos de sección</h3>
  <h2>Formularios</h2>
```

1.  Salto de nivel (`h1` → `h4`) y dos `h1`: el lector pierde el índice y el examen considera rota la jerarquía.

2.  Niveles encadenados (`h1` → `h2` → `h3`); el **tamaño visual** lo decide CSS, no la etiqueta.

## 6. ARIA: lo mínimo que funciona

### 6.1 Regla de oro: primero el elemento HTML nativo

ARIA es un **añadido** para lo que HTML no puede expresar; la ==regla de oro== de su especificación es: *no uses ARIA si existe un elemento HTML que haga ese trabajo*.

```html title="div-vs-button.html" hl_lines="2 5"
<!-- ❌ "divitis" accesible: hay que reimplementar todo a mano -->
<div role="button" class="boton" tabindex="0">Guardar cambios</div>
<!--  role no da teclado · falta tabindex · falta JS para Intro/Espacio -->

<!-- ✅ el nativo lo trae todo GRATIS -->
<button type="button">Guardar cambios</button>
<!--  teclado · foco · nombre accesible · disabled · ratón y dedo -->
```

!!! warning "Error común"

    Escribir ARIA **antes** de comprobar si el HTML ya lo resuelve: `role="link"` sobre un `<div>` con `onclick`, `role="heading" level="2"` en un `<span>` donde existía `<h2>`, `role="list"` sobre un `<div>` con `display: flex`. Cada rol obliga a reimplementar teclado, foco y nombre accesible: casi siempre hay que cambiar la etiqueta.

### 6.2 Roles útiles

| Rol | Cuándo se justifica | Alternativa nativa |
|---|---|---|
| `role="button"` | Si el elemento **no puede** ser `<button>` | `<button>` |
| `role="link"` | Enlace que dispara JS en contenido rico | `<a href>` |
| `role="dialog"` | Ventana modal creada por tu código | `<dialog>` |
| `role="alert"` | Error que debe anunciarse de inmediato | `<output>` + `aria-live="assertive"` |

### 6.3 `aria-label` vs. `aria-labelledby` vs. `aria-describedby`

En los exámenes y en el desarrollo real, una de las mayores confusiones es cuándo usar cada uno de estos tres atributos de nombres accesibles:

#### 1. `aria-label` (Poner nombre cuando NO hay texto visible)
- **Cuándo se usa:** En botones o enlaces que solo contienen un icono, un emoji o una imagen vectorial, y que por tanto carecen de texto legible.
- **Efecto:** Le asigna una etiqueta invisible que el lector de pantalla pronunciará directamente:
```html
<!-- El usuario vidente ve una papelera; el usuario ciego escucha "Eliminar producto" -->
<button type="button" aria-label="Eliminar producto de la cesta">🗑️</button>
```
- **Regla:** Nunca uses `aria-label` si el elemento ya tiene texto visible (`<button>Guardar</button>`), porque `aria-label` **machaca y sustituye** el texto visible en el árbol de accesibilidad.

#### 2. `aria-labelledby` (Reutilizar un texto que ya existe en la pantalla)
- **Cuándo se usa:** Cuando el nombre que quieres darle a una sección o campo ya está escrito en otro lugar de la página (por ejemplo, en un encabezado `<h2>`).
- **Cómo funciona:** Recibe el `id` del elemento que tiene el texto:
```html
<section aria-labelledby="tit-ofertas">
  <h2 id="tit-ofertas">Ofertas especiales del mes</h2>
  <!-- Todo este bloque queda bautizado con el texto del h2 -->
</section>
```

#### 3. `aria-describedby` (Información adicional de ayuda o error)
- **Cuándo se usa:** **NO da nombre al control**, sino que añade una **descripción secundaria o instrucción de ayuda**.
- **Comportamiento del lector de pantalla:** El lector primero anuncia el nombre del campo, luego hace una pequeña pausa, y después lee la descripción:
```html
<label for="clave">Contraseña:</label>
<input type="password" id="clave" name="clave" aria-describedby="requisitos-clave">
<p id="requisitos-clave">Debe tener al menos 8 caracteres, una mayúscula y un número.</p>
```

> **Jerarquía de resolución del Nombre Accesible:**
> El navegador busca en este orden estricto: `aria-labelledby` $\rightarrow$ `aria-label` $\rightarrow$ Texto visible interior $\rightarrow$ `title`. El atributo `aria-describedby` **nunca forma parte del nombre**, solo aporta información complementaria.

---

### 6.4 `aria-expanded`, `aria-hidden` y `aria-current`

| Atributo | Estado que comunica | Ejemplo de uso |
|---|---|---|
| `aria-expanded="true/false"` | Si un acordeón o menú desplegable está actualmente abierto o cerrado. **Debe sincronizarse con JavaScript en cada clic**. | `<button aria-expanded="false" aria-controls="submenú">Menú</button>` |
| `aria-hidden="true"` | **Oculta el elemento al lector de pantalla**, pero lo mantiene 100% visible para los usuarios de ratón. | Iconos decorativos, estrellas de adorno: `<span aria-hidden="true">★</span>` |
| `aria-current="page"` | Indica que un enlace es la **página activa en la que se encuentra el usuario actualmente**. | `<a href="/contacto" aria-current="page">Contacto</a>` |

---

### 6.5 `aria-live`: Regiones dinámicas que anuncian cambios (SPA y AJAX)

En aplicaciones web modernas (como las que se desarrollan en Angular, React o con JavaScript asíncrono), cuando el usuario realiza una acción no se recarga la página completa. Si un mensaje de éxito aparece en verde en pantalla (*"Tu solicitud se ha guardado correctamente"*), un usuario vidente lo lee al instante. Sin embargo, para una persona ciega, **el lector de pantalla no emite ningún sonido porque el foco no se ha movido**, dejándola con la duda de si la operación tuvo éxito.

Para solucionar este grave problema de accesibilidad existen las **Live Regions** mediante el atributo `aria-live`:

| Valor | Comportamiento del lector de pantalla | Cuándo usarlo |
|---|---|---|
| `aria-live="polite"` | **Educado:** Espera pacientemente a que termine la frase que esté leyendo antes de anunciar la novedad. | Confirmaciones no críticas: *"Mensaje enviado"*, *"3 artículos añadidos al carrito"*, resultados de búsqueda. |
| `aria-live="assertive"` | **Asertivo / Urgente:** Interrumpe de inmediato cualquier frase que esté diciendo para alertar al usuario. | Errores graves del sistema, caídas de conexión o pérdida inminente de sesión por tiempo. |
| `aria-live="off"` | Desactivado (comportamiento por defecto). | Regiones estáticas normales. |

```html title="aviso-en-vivo.html"
<!-- role="status" equivale automáticamente a aria-live="polite" aria-atomic="true" -->
<div id="notificacion" role="status" aria-live="polite" aria-atomic="true"></div>

<button type="button" onclick="guardarDatos()">Guardar borrador</button>

<script>
function guardarDatos() {
  // Al inyectar texto aquí, el lector de pantalla lo anunciará automáticamente al usuario
  document.getElementById('notificacion').textContent = 'Borrador guardado con éxito a las 18:45.';
}
</script>
```

- **`aria-atomic="true"`:** Fuerza al sintetizador a leer **todo el contenido completo del contenedor**, en lugar de leer solo las letras o palabras que hayan cambiado.
- Para alertas críticas de error, `role="alert"` equivale automáticamente a `aria-live="assertive"`.

## 7. Cuándo NO usar ARIA (anti-patrones)

1. **`aria-label` redundante con el texto visible** (`<a href="/ayuda">Ayuda</a>` + `aria-label="Ir a la página de ayuda"`): anuncia dos frases y **sobrescribe** el texto visible.
2. **Roles que empeoran**: `role="button"` sobre un `<div>` sin teclado, `role="img"` con texto dentro, `role="presentation"` en una tabla con datos.
3. **Marcar lo que el HTML ya hace**: `role="navigation"` sobre `<nav>`, `role="heading"` sobre `<h2>`, `role="main"` sobre `<main>`.
4. **ARIA sin JavaScript**: `aria-expanded`, `aria-selected`, `aria-checked` e `aria-invalid` **no cambian solos**; si no los actualizas, estás mintiendo.
5. **`aria-hidden` en contenido enfocable**: el foco llega a un sitio que el lector no anuncia.
6. **Empezar por ARIA en vez de arreglar el HTML**: si faltaba un `<h2>`, la solución es el `<h2>`.

!!! failure "Anti-patrón: ARIA de más"

    El problema no es que "haya mucho ARIA", sino que **estorba**:

    - Doble anuncio: el lector lee el texto visible **y** el `aria-label` redundante.
    - Doble mantenimiento: cada `role` de más obliga a reimplementar **teclado, foco y nombre accesible**.
    - Estado desfasado: un atributo que nadie sincroniza convierte la página en una mentira anunciada.

    Corrección: ==cambia la etiqueta, no añadas roles==.

## 8. Práctica: cómo comprobarlo

### 8.1 El árbol de accesibilidad de DevTools

*Elements* → sub-pestaña **Accessibility**: verás los **roles y nombres accesibles reales**, no lo que tú crees haber escrito. Comprueba que `main`, `nav` y `aside` aparecen como landmark y que Issues no señala problemas. El árbol **no cambia** con colores o tamaños: la ==semántica es independiente del CSS== (→ [../css/13-accesibilidad-usabilidad.md](../css/13-accesibilidad-usabilidad.md)).

### 8.2 Lector de pantalla y teclado

Windows: NVDA (gratuito y estándar en pruebas), Narrador o JAWS; macOS: VoiceOver (`Cmd + F5`). **Prueba mínima**: recorre la página solo con **Tab**, lista los encabezados (`h`) y usa los atajos de landmark (`D` = *main*, `M` = *navigation*). Si no llegas a todo el contenido sin ratón, algo falla.

## 9. Marco legal de accesibilidad y relación con la clase de interfaces

En España y la Unión Europea, la accesibilidad digital no es una recomendación estética opcional, sino una **obligación legal estricta** regulada por:

- **Real Decreto 1112/2018**, de 7 de septiembre: Exige a las administraciones públicas y a empresas con financiación pública o servicios esenciales garantizar el nivel de adecuación **WCAG 2.1 nivel AA**.
- **Norma UNE-EN 301549**: Estándar europeo de requisitos de accesibilidad para productos y servicios TIC.
- **Módulo 0615 (DIW - RA 5) y Módulo 0488 (DI - RA 5):** Exigen evaluar la conformidad de las interfaces mediante herramientas automáticas (WAVE, axe DevTools, Lighthouse) y manuales (recorrido completo por teclado y lectores de pantalla como NVDA o VoiceOver).

Esta unidad cubre la capa **HTML** de la accesibilidad (estructura semántica, landmarks y nombres accesibles); la capa **CSS** (contraste cromático, tipografía adaptativa, foco visible y animaciones reducidas) se desarrolla en [../css/13-accesibilidad-usabilidad.md](../css/13-accesibilidad-usabilidad.md).

## 10. Errores frecuentes y claves para el examen

!!! warning "Error común"

    Los tres fallos que más se corrigen en la práctica:
    
    - **Dos `<main>`** en la página (contenido y pie, o contenido y modal): solo puede haber **uno visible**; para el otro usa `<section>` o `<div>`.
    - **Elegir el encabezado por el tamaño visual** (`<h4>` porque "queda más pequeño" o varias `<h1>` porque el diseño las pide): el nivel es **estructural**, el tamaño es CSS.
    - **ARIA de más**: `aria-label` redundante con el texto visible, `role="navigation"` sobre `<nav>`, `aria-expanded` que nadie actualiza. Más ARIA no significa más accesibilidad.

!!! tip "Claves para el examen"

    - Semántica = **significado en el HTML** (buscadores, lectores de pantalla y mantenimiento; no es estética). Siete elementos: `header`, `nav`, `main`, `article`, `section`, `aside`, `footer`; landmark `banner`/`contentinfo` **solo** si `header`/`footer` son hijos directos de `<body>`.
    - **Un solo `<main>` visible**; `article` = contenido independiente; `section` = tema con encabezado propio; si es solo maquetación → `<div>`.
    - **Skip link**: primer enlace del DOM, `href="#id"` del `<main>`, visible **solo con el foco**; se prueba con Tab → Intro → Tab.
    - **Encabezados sin saltos** y un solo `h1`; el tamaño visual lo decide CSS.
    - **ARIA**: primero el nativo (`<button>` frente a `<div role="button">`, que exige `tabindex` y JS); `aria-label`/`aria-labelledby` → **nombre accesible**, `aria-describedby` → **descripción**; `aria-expanded`/`aria-current` describen estado, `aria-hidden` oculta solo del lector, `aria-live="polite"` avisa sin interrumpir y `"assertive"` interrumpe.
    - Verifica el **árbol de accesibilidad de DevTools** y recorre la página con teclado y lector de pantalla.


!!! success "Practica esta unidad"

    - Enunciados: [Ejercicios de la Unidad 7 — Estructura semántica y ARIA](09-ejercicios.md#ejercicio-2-articulo-semantico) — cuatro retos (`U7.1` a `U7.4`) — del más básico al más avanzado.
    - Comprueba tu trabajo con [las soluciones de esta unidad](10-ejercicios-soluciones.md#sol-u7).

*[ARIA]: Accessible Rich Internet Applications — roles y atributos que describen interfaces cuando el HTML nativo no llega.
*[WCAG]: Web Content Accessibility Guidelines — pautas de accesibilidad del W3C citadas en los criterios 1.3.1 y 2.4.1.
*[landmark]: región navegable de la página (banner, navigation, main, complementary, contentinfo) que el lector de pantalla puede listar y saltar.
