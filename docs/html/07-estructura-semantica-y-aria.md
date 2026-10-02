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

### 2.1 Los siete elementos y su significado

| Elemento | Significado | Landmark implícito |
|---|---|---|
| `<header>` | Cabecera de la página **o de un bloque** | `banner` **solo** si es hijo directo de `<body>` |
| `<nav>` | Bloque de navegación | `navigation` |
| `<main>` | Contenido **único y principal** | `main` |
| `<article>` | Contenido independiente (entrada, ficha, comentario) | — |
| `<section>` | Agrupación **temática**, normalmente con encabezado | — (con nombre accesible → `region`) |
| `<aside>` | Contenido complementario o tangencial | `complementary` |
| `<footer>` | Pie de la página **o de un bloque** | `contentinfo` **solo** si es hijo directo de `<body>` |

Matices de examen: **`<main>` es único**; **`header`/`footer` anidados** en `article` o `section` **no** son `banner`/`contentinfo`; **`nav`** solo para navegación real.

!!! info "Qué es un landmark"

    Región de la página que el lector de pantalla puede **listar y saltar** con un atajo (`D` → *main*, `M` → *navigation*). No se crea con CSS: lo define el **elemento** y su **posición** en el árbol. De la tabla, cinco elementos lo traen implícito; `article` no, y `section` solo si recibe un nombre accesible → `region`.

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

### 6.3 `aria-label` vs `aria-labelledby` vs `aria-describedby`

| Atributo | ¿Forma el nombre accesible? | Cuándo se lee | Para qué sirve |
|---|---|---|---|
| `aria-label` | **Sí** | Al enfocar/anunciar | Nombre donde **no hay texto visible** |
| `aria-labelledby` | **Sí** (lo toma de otro `id`) | Igual que `aria-label` | Unir el nombre a un **texto ya existente** |
| `aria-describedby` | **No**: es **descripción** | **Después** del nombre | Ayuda, instrucción o error largo |

```html title="nombres-accesibles.html"
<button type="button" aria-label="Eliminar el borrador">🗑️</button> <!-- (1)! -->

<section aria-labelledby="tit-promo">
  <h2 id="tit-promo">Oferta de matrícula</h2>
  <button type="button">Ver condiciones</button>
</section>

<label for="dni">NIF</label>
<input id="dni" required aria-describedby="ayuda-dni"> <!-- (2)! -->
<p id="ayuda-dni">Ejemplo: 12345678Z.</p>
```

1.  `aria-label` aporta **nombre** donde no hay texto visible: el emoji se anuncia completo como "Eliminar el borrador".

2.  `aria-describedby` aporta **descripción**: se anuncia después del nombre y **no** forma parte de él.

> **Orden del nombre accesible:** `aria-labelledby` → `aria-label` → texto visible → `title`. ==`aria-describedby`== **nunca** sustituye al nombre.

### 6.4 `aria-expanded`, `aria-hidden` y `aria-current`

```html
<!-- estado de un desplegable: sincronízalo SIEMPRE con el JS -->
<button type="button" aria-expanded="false" aria-controls="menu">Cursos ▾</button>
<ul id="menu" hidden> ... </ul>
<span aria-hidden="true">★</span>   <!-- decorativo junto a texto -->
<a href="/" aria-current="page">Inicio</a>   <!-- "estás aquí" -->
```

`hidden` / `display: none` → **no existe** para nadie (ni foco, ni ratón, ni lector); `aria-hidden="true"` → sigue visible y clicable pero **no se anuncia**, y si además es enfocable creas un *foco fantasma*. `aria-expanded` es **solo informativo**: si tu JS no lo actualiza, anuncia mentiras (con `<details>` lo gestiona el navegador).

### 6.5 `aria-live`: regiones que anuncian cambios

Marcaste con ==`aria-live`== la región que debe **reanunciarse** cuando su contenido cambia; sin esa marca, el lector de pantalla no se entera de nada.

| Valor | Comportamiento | Ejemplo típico |
|---|---|---|
| `aria-live="polite"` | Espera su turno; **no interrumpe** | "Cambios guardados", resultados |
| `aria-live="assertive"` | **Interrumpe** lo que se esté leyendo | Error de validación |
| `aria-live="off"` | No anuncia nada (por defecto) | — |

```html title="aviso-en-vivo.html"
<p id="aviso" role="status" aria-live="polite" aria-atomic="true"></p>
<button onclick="guardar()">Guardar</button>

<script>
function guardar() {
  // role="status" = aria-live="polite": no interrumpe
  document.getElementById('aviso').textContent = 'Cambios guardados ✓';
}
</script>
```

`aria-atomic="true"` lee **toda** la región; `role="alert"` es el equivalente *assertive* (errores reales).

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

## 9. Relación con la clase de interfaces

Esta unidad es la parte **HTML** de la accesibilidad (estructura y nombres accesibles); la parte **CSS** está en la clase de interfaces → [../css/13-accesibilidad-usabilidad.md](../css/13-accesibilidad-usabilidad.md).

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

    - Enunciados: [Ejercicios de la Unidad 7 — Estructura semántica y ARIA](09-ejercicios.md#ej-u7) — cuatro retos (`U7.1` a `U7.4`) — del más básico al más avanzado.
    - Comprueba tu trabajo con [las soluciones de esta unidad](10-ejercicios-soluciones.md#sol-u7).

*[ARIA]: Accessible Rich Internet Applications — roles y atributos que describen interfaces cuando el HTML nativo no llega.
*[WCAG]: Web Content Accessibility Guidelines — pautas de accesibilidad del W3C citadas en los criterios 1.3.1 y 2.4.1.
*[landmark]: región navegable de la página (banner, navigation, main, complementary, contentinfo) que el lector de pantalla puede listar y saltar.
