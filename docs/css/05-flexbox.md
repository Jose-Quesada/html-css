---
icon: lucide/move-horizontal
title: "Unidad 05 — Flexbox"
description: "Modelo de flexión completo: ejes, propiedades del contenedor y de los items, shorthand flex, el problema de min-width:auto, centrado seguro y layouts típicos."
modulo: "LMH (0373) / DIW (0615)"
unidad: 5
fecha: "2026-09-06"
---

# Unidad 05 · Flexbox

**Flexbox es un modelo de distribución en UNA dimensión**: una fila O una columna. Es la herramienta ideal para distribuir espacio entre items y alinearlos dentro de un contenedor (navbars, toolbars, cards en fila, centrado, «espacio entre»).

Para dos dimensiones a la vez → **Grid** (unidad 06). La regla práctica:

- ¿Distribuyo contenido en una línea que puede envolver? → **Flex**.
- ¿Diseño la página/sección como cuadrícula (filas Y columnas)? → **Grid**.

!!! note "Conocimientos previos"

    - Modelo de caja y límites `min-*`/`max-*` (→ [03-modelo-de-caja.md](03-modelo-de-caja.md)).
    - Datos tabulares frente a maquetación (→ [../html/05-tablas.md](../html/05-tablas.md)).

## 1. Activación y anatomía

```css title="activacion-flex.css"
.contenedor { display: flex; }        /* o inline-flex */
```

Al activarse:

- El contenedor se convierte en **flex container**; sus hijos directos, en **flex items** (aunque sean inline, floats… dejan de comportarse como tales).
- Aparecen dos ejes:
    - **Main axis** (eje principal): dirección del flujo (`flex-direction`).
    - **Cross axis** (eje transversal): perpendicular al principal.

```text
row (default):          column:
→ main axis             ↓ main axis
↓ cross axis            → cross axis
```

El ==main axis== **reparte** el espacio; el transversal **alinea**.

`display: inline-flex` crea un contenedor flex que fluye como inline (útil para widgets embebidos en texto).

## 2. Propiedades del contenedor


| Propiedad | Valores habituales | Efecto |
|---|---|---|
| ==flex-direction== | `row` (def), `row-reverse`, `column`, `column-reverse` | Orienta el eje principal. |
| `flex-wrap` | `nowrap` (def), `wrap`, `wrap-reverse` | Permite saltar a líneas nuevas. |
| `flex-flow` | atajo de las dos anteriores: `row wrap`. |
| `justify-content` | Distribución **sobre el eje principal** (ver tabla abajo). |
| `align-items` | Alineación **sobre el eje transversal** de todos los items: `stretch` (def), `flex-start`, `flex-end`, `center`, `baseline`. |
| `align-content` | Alinea **las líneas** entre sí cuando hay `wrap`: `stretch`, `flex-start`, `center`, `space-between`, `space-around`, `space-evenly`. |
| ==`gap`== | Espacio entre items (y entre líneas si hay wrap). Soporte universal moderno. |

!!! info "Justify o align: dos reglas fijas"

    - `justify-content` → **eje principal** (el que define `flex-direction`).
    - `align-items` → **eje transversal** de todos los items.
    - `align-content` solo actúa con **varias líneas** (`wrap`).

### 2.1. `justify-content` desgranado

| Valor | Comportamiento |
|---|---|
| `flex-start` | Empaqueta al inicio del eje (default). |
| `flex-end` | Al final. |
| `center` | Centrado. |
| `space-between` | Espacios **iguales** entre items; primero y último pegados a los bordes. |
| `space-around` | Espacio igual alrededor; los bordes miden la mitad que el intermedio. |
| `space-evenly` | Espacio idéntico en todas partes (bordes incluidos). |
| `start` / `end` | Equivalentes lógicos (respetan `direction`) — preferirlos por i18n. |


### 2.2. Alineación «segura» (safe alignment)

Problema histórico: con `justify-content: center` + `overflow`, el contenido desbordado se corta **por el principio** (inaaccesible). Solución moderna:

```css title="alineacion-segura.css" hl_lines="2 3"
.contenedor {
  justify-content: safe center;   /* si no cabe, alinea al start */
  align-items: safe center;
}
```


## 3. Propiedades de los items

| Propiedad | Descripción |
|---|---|
| `order` | Orden visual (no afecta al DOM ni al foco). Default 0. Negativos válidos. |
| `flex-grow` | Factor de reparto del **espacio libre** positivo. Default 0. |
| `flex-shrink` | Factor de compresión ante **espacio negativo**. Default 1. |
| `flex-basis` | Tamaño inicial antes de repartir. Default `auto` (usa `width`/contenido). |
| `flex` | Atajo: `flex: grow shrink basis`. |
| `align-self` | Anula `align-items` para un item: `auto`, `stretch`, `flex-start`, `flex-end`, `center`, `baseline`. |

### 3.1. Las tres propiedades del item explicadas a fondo

Para entender el atajo `flex: grow shrink basis`, hay que desgranar qué hace cada una:

1. **`flex-basis` (El punto de partida):**
   Es el tamaño base inicial que el elemento pide tener antes de que empiece a repartirse o quitarse espacio. Si vale `200px`, el item intentará medir `200px`. Si vale `auto`, mirará su `width` explícito o el tamaño de su texto.

2. **`flex-grow` (El reparto del pastel sobrante):**
   Define cómo se reparte el **espacio positivo libre**.

    - Si un contenedor mide `1000px` y tiene dos hijos con `flex-basis: 300px`, la suma de bases es `600px`. Sobran `400px` de espacio libre en blanco.
    - Si el Hijo 1 tiene `flex-grow: 1` y el Hijo 2 tiene `flex-grow: 3`, los `400px` sobrantes se dividen en 4 partes (1+3 = 4 partes de 100px cada una).
    - El Hijo 1 se queda con 1 parte (+100px) $\rightarrow$ Ancho final: `400px`.
    - El Hijo 2 se queda con 3 partes (+300px) $\rightarrow$ Ancho final: `600px`.
    - Si `flex-grow: 0` (el valor por defecto), los elementos **no crecen** y el espacio libre queda vacío a la derecha.
3. **`flex-shrink` (El sacrificio ante la estrechez):**
   Define cómo se comprimen los elementos cuando el contenedor es **demasiado pequeño** y no caben todos.

    - Si vale `1` (por defecto), los items se encogen proporcionalmente para evitar salirse del contenedor.
    - Si vale `0`, el item se vuelve **inflexible y rígido**: prefiere desbordarse y salirse de la pantalla antes que encogerse un solo píxel (ideal para iconos o avatares circulares que no deben deformarse nunca).

### 3.2. El atajo `flex` en el día a día

| Declaración | Equivale a | Explicación intuitiva para el alumno |
|---|---|---|
| `flex: initial` | `0 1 auto` | **Comportamiento por defecto:** Se ajusta a su contenido, no crece si sobra espacio, pero sí se encoge si hace falta. |
| `flex: 1` | `1 1 0%` | **Reparto igualitario estricto:** Todos los elementos miden exactamente lo mismo, sin importar si uno tiene una palabra y otro tiene diez líneas de texto. |
| `flex: auto` | `1 1 auto` | **Crecimiento según contenido:** Todos crecen, pero el que tiene más texto o tamaño base siempre acabará siendo más ancho. |
| `flex: none` | `0 0 auto` | **Completamente rígido:** No crece ni mengua bajo ninguna circunstancia. |

!!! info "Regla de oro: ¿Por qué preferir `flex: 1` en casi todo?"

    Al poner `flex: 1`, la base es `0%`. Al no tener tamaño inicial, el `100%` del contenedor se reparte matemáticamente a partes iguales entre todos los hermanos con `flex: 1`. Es la forma más limpia y fiable de crear columnas idénticas.

## 4. La trampa: `min-width: auto`

Los flex items tienen por defecto `min-width: auto` (= su *min-content*). Consecuencia: **un item con mucho contenido no se encoge** y rompe el layout.

```css title="trampa-min-width-auto.css" hl_lines="2"
.item { flex: 1; overflow: hidden; }  /* solución 1: permite encoger */
.item { min-width: 0; }               /* solución 2: explícita */
```

Casos donde muerde: textos largos sin espacios (URLs), tablas dentro de flex, inputs largos.

> **Claves para el examen**: «mi flex no se encoge y desborda» → ==`min-width: 0`== (o `overflow` distinto de visible) en el item.

!!! question "Mi flex no se encoge"

    Una tarjeta con una URL larguísima rompe la fila. ¿Diagnóstico y arreglo?

    ??? success "Respuesta"

        Conserva `min-width: auto` y no baja de su **min-content**: `min-width: 0` **en ese item**.

!!! warning "Error común"

    Olvidar cada eje: `justify-content` va por el **principal** y `align-items` por el transversal; con ==flex-direction== `: column`, «centrar en horizontal» deja de ser `justify-content: center`.

## 5. Layouts canónicos

### 5.1. Navbar clásico

```css title="navbar-clasica.css" hl_lines="6"
.nav {
  display: flex;
  align-items: center;
  gap: 1rem;
}
.nav .logo { margin-inline-end: auto; }  /* empuja el resto a la derecha */
.nav ul { display: flex; gap: .5rem; list-style: none; }
```

Truco: `margin-inline-end: auto` en un item absorbe todo el espacio libre → efecto «push».


### 5.2. Centrado total

```css title="centrado-total.css"
.centro {
  display: flex; /* (1)! */
  justify-content: center;   /* main */
  align-items: center;       /* cross */
  min-height: 100dvh;
}
/* o el atajo moderno: */
.centro { display: grid; place-items: center; }
```

1.  Sin `min-height` no hay altura donde **centrar** en el eje transversal.

### 5.3. Fila de cards iguales que envuelven

```css
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
.card { flex: 1 1 250px; }   /* base 250px, crecen por igual */
```

### 5.4. Toolbar con grupos

```css
.toolbar { display: flex; flex-wrap: wrap; gap: .5rem; }
.grupo  { display: flex; gap: .25rem; }
.grupo--fin { margin-inline-start: auto; }
```

### 5.5. «Holy grail» simplificado (header/footer fijos de altura, sidebar flexible)

```css title="holy-grail-flex.css"
.layout {
  display: flex;
  min-height: 100dvh; /* (1)! */
}
.sidebar { flex: 0 0 16rem; }      /* rígida */
.main    { flex: 1; min-width: 0; } /* absorbe el resto */
```

1.  `min-height` hace que la columna ocupe **toda la pantalla** con poco contenido.

### 5.6. Etiqueta + valor alineados (patrón de formulario)

```css
.fila { display: flex; justify-content: space-between; gap: 1rem; }
```

!!! example "Navbar resuelto en dos líneas"

    ```css
    .nav { display: flex; align-items: center; gap: 1rem; }
    .nav .logo { margin-inline-end: auto; }
    ```

## 6. Flex vs Grid: decisión rápida

| Criterio | Flexbox | Grid |
|---|---|---|
| Dimensiones | 1D | 2D |
| El contenido define el layout | Sí (contenido-first) | No (layout-first: defines tracks y colocas) |
| Espaciado | `gap` + justify/align | `gap` + placement |
| Superposición de items | No (salvo tricks) | Sí (mismas líneas) |
| Casos ideales | Componentes, navbars, centrado, distribuir espacio | Páginas, dashboards, galerías, formularios complejos |

Se pueden **combinar**: grid para la página, flex dentro de cada celda.

## 7. Accesibilidad y orden

- ==order== cambia el **visual**, no el **DOM**: lectores de pantalla y Tab siguen el DOM. Si el orden visual difiere del lógico, documenta o cambia el HTML.
- No uses flex para reordenar semánticamente importantes cosas (p. ej., mover el footer visualmente antes que el main).

---

## 8. Ejemplo práctico: barra de navegación y tarjetas autoajustables con Flexbox

El siguiente ejemplo combina los patrones más exigentes de Flexbox en producción: una barra de navegación con empuje automático (`margin-inline-start: auto`), un catálogo de tarjetas que envuelve con `flex-wrap` y bases adaptables (`flex: 1 1 280px`), la solución a la trampa de `min-width: auto` mediante `min-width: 0`, y tarjetas internas con pie empujado al fondo (`margin-top: auto`).

```html title="catalogo-flex.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flexbox · Navegación y Tarjetas Autoalineadas</title>
  <link rel="stylesheet" href="css/flexbox.css">
</head>
<body>
  <!-- 1. Barra de navegación 1D en fila -->
  <header class="navbar">
    <div class="navbar__logo">DevPlatform</div>
    <nav class="navbar__enlaces" aria-label="Navegación principal">
      <a href="#proyectos" class="navbar__link">Proyectos</a>
      <a href="#despliegues" class="navbar__link">Despliegues</a>
      <a href="#equipos" class="navbar__link">Equipos</a>
    </nav>
    <div class="navbar__usuario">
      <button type="button" class="btn btn--perfil">Mi Cuenta</button>
    </div>
  </header>

  <main class="contenedor">
    <header class="seccion-cabecera">
      <h1>Servicios Activos</h1>
      <p>Infraestructura desplegada y balanceo de carga.</p>
    </header>

    <!-- 2. Rejilla envolvente con Flexbox -->
    <div class="cards-grid">
      <article class="card">
        <div class="card__estado card__estado--ok">Operativo</div>
        <h2 class="card__titulo">API Gateway Principal</h2>
        <p class="card__texto">
          Punto de entrada microservicios con enrutamiento SSL y límite de peticiones activo.
        </p>
        <footer class="card__pie">
          <span class="card__metricas">99.98% uptime</span>
          <a href="#" class="card__accion">Detalles →</a>
        </footer>
      </article>

      <article class="card">
        <div class="card__estado card__estado--ok">Operativo</div>
        <h2 class="card__titulo">Cluster Postgres Primario</h2>
        <p class="card__texto">
          Base de datos transaccional con replicación asíncrona en 3 zonas de disponibilidad.
        </p>
        <footer class="card__pie">
          <span class="card__metricas">12.4 ms latencia</span>
          <a href="#" class="card__accion">Detalles →</a>
        </footer>
      </article>

      <article class="card">
        <div class="card__estado card__estado--alerta">Carga Alta</div>
        <h2 class="card__titulo">Cola de Tareas Redis</h2>
        <p class="card__texto">
          Procesamiento asíncrono de mensajes y colas de correos con consumo elevado de memoria.
        </p>
        <footer class="card__pie">
          <span class="card__metricas">84% memoria</span>
          <a href="#" class="card__accion">Detalles →</a>
        </footer>
      </article>
    </div>
  </main>
</body>
</html>
```

```css title="css/flexbox.css"
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: system-ui, -apple-system, sans-serif;
  background-color: #f8fafc;
  color: #0f172a;
  line-height: 1.5;
}

/* 1. Navbar con Flexbox y empuje automático */
.navbar {
  display: flex;
  align-items: center; /* Alineación vertical perfecta en el eje transversal */
  gap: 1.5rem;
  padding: 1rem 2rem;
  background-color: #ffffff;
  border-bottom: 1px solid #e2e8f0;
}

.navbar__logo {
  font-weight: 800;
  font-size: 1.25rem;
  color: #0284c7;
}

.navbar__enlaces {
  display: flex;
  gap: 1rem;
}

.navbar__link {
  text-decoration: none;
  color: #475569;
  font-weight: 500;
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  transition: color 0.15s ease;
}

.navbar__link:hover {
  color: #0284c7;
}

/* margin-inline-start: auto absorbe todo el espacio sobrante en el eje principal */
.navbar__usuario {
  margin-inline-start: auto;
}

.btn--perfil {
  background-color: #0f172a;
  color: #ffffff;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-weight: 600;
  cursor: pointer;
}

/* 2. Contenedor principal */
.contenedor {
  max-width: 72rem;
  margin-inline: auto;
  padding: 2.5rem 1.5rem;
}

.seccion-cabecera {
  margin-block-end: 2rem;
}

.seccion-cabecera h1 {
  font-size: 1.75rem;
  margin-block-end: 0.25rem;
}

.seccion-cabecera p {
  color: #64748b;
}

/* 3. Rejilla flex envolvente */
.cards-grid {
  display: flex;
  flex-wrap: wrap; /* Permite que las tarjetas salten a la siguiente línea */
  gap: 1.5rem; /* Espaciado uniforme en filas y columnas sin hacks de márgenes */
}

/* 4. Tarjetas individuales como items y sub-contenedores flex */
.card {
  /* flex: 1 1 280px => crece si hay hueco, encoge si falta, base ideal de 280px */
  flex: 1 1 18rem;
  min-width: 0; /* Solución crucial a la trampa de desbordamiento de min-width: auto */
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 0.75rem;
  padding: 1.5rem;
  box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);

  /* Tarjeta interna en columna para empujar el footer */
  display: flex;
  flex-direction: column;
}

.card__estado {
  align-self: flex-start; /* Sobreescribe align-items stretch en el item */
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.2rem 0.5rem;
  border-radius: 9999px;
  margin-block-end: 0.75rem;
}

.card__estado--ok {
  background-color: #dcfce7;
  color: #166534;
}

.card__estado--alerta {
  background-color: #fef3c7;
  color: #92400e;
}

.card__titulo {
  font-size: 1.15rem;
  margin-block-end: 0.5rem;
}

.card__texto {
  color: #64748b;
  font-size: 0.9rem;
  margin-block-end: 1.5rem;
}

/* 5. Pie de tarjeta empujado al fondo con margin-top: auto */
.card__pie {
  margin-top: auto; /* Empuja el pie al fondo sin importar la cantidad de texto superior */
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 1rem;
  border-top: 1px solid #f1f5f9;
}

.card__metricas {
  font-size: 0.8rem;
  font-weight: 600;
  color: #64748b;
}

.card__accion {
  color: #0284c7;
  font-weight: 600;
  text-decoration: none;
  font-size: 0.85rem;
}

.card__accion:hover {
  text-decoration: underline;
}
```

---

### 8.1 Explicación detallada: ¿Por qué se usa cada propiedad y para qué sirve?

A continuación se detalla la justificación técnica de las propiedades Flexbox utilizadas:

#### 1. `align-items: center` en `.navbar`
- **¿Para qué sirve?** Controla la alineación en el **eje transversal** (*cross axis*), que en un flujo de fila (`flex-direction: row`) corresponde al eje vertical.
- **Resultado:** Centra automáticamente el logotipo, los enlaces de texto y el botón de usuario sin necesidad de calcular alturas fijas, márgenes verticales o rellenos compensatorios.

#### 2. `margin-inline-start: auto` para empujar elementos
- **El patrón canónico:** En Flexbox, declarar un margen automático en cualquier dirección absorbe la totalidad del espacio libre disponible en ese eje.
- **¿Por qué se usa en `.navbar__usuario`?** Separa limpiamente el menú de navegación izquierdo del botón de usuario derecho, empujando este último hasta el extremo final de la pantalla sin trucos de `float: right` ni posicionamiento absoluto.

#### 3. La combinación `flex-wrap: wrap` con `gap: 1.5rem`
- **`flex-wrap: wrap`:** Permite que los elementos flex fluyan a nuevas líneas horizontales en lugar de comprimirse indefinidamente en una sola fila rígida.
- **`gap: 1.5rem`:** Establece el canalón de separación exacto entre tarjetas contiguas (tanto horizontal como verticalmente) sin agregar espacio residual en los extremos exteriores del contenedor.

#### 4. La terna `flex: 1 1 18rem`
- **Desglose de valores:**
    - `flex-grow: 1`: Si la fila tiene espacio sobrante, las tarjetas crecen equitativamente para rellenar todo el ancho disponible.
    - `flex-shrink: 1`: Si la pantalla se estrecha, las tarjetas reducen su tamaño por igual para evitar el desbordamiento horizontal.
    - `flex-basis: 18rem`: Fija el tamaño ideal de partida (~288 px). Cuando el espacio es inferior a 18 rem, la tarjeta salta a la siguiente fila.

#### 5. La trampa de `min-width: auto` y la salvaguarda con `min-width: 0`
- **El problema de diseño:** Por especificación del W3C, todos los items de un contenedor flex nacen con `min-width: auto`. Esto significa que si dentro de una tarjeta aparece una URL larguísima, una palabra técnica sin espacios o una tabla, el item flex **se negará a encogerse por debajo del ancho de ese texto**, rompiendo el ancho de la tarjeta y desbordando la pantalla.
- **La solución técnica:** Declarar explícitamente `min-width: 0` anula ese límite mínimo impuesto por el contenido y permite que la tarjeta se encoja correctamente.

#### 6. Tarjeta interior en columna (`flex-direction: column`) con `margin-top: auto`
- **El problema visual habitual:** Si una tarjeta tiene 3 líneas de texto y su vecina tiene 6 líneas, los pies de tarjeta (`.card__pie`) quedan a diferentes alturas desalineadas, dando una apariencia descuidada.
- **La solución elegante:** Al convertir la tarjeta en un contenedor flex vertical (`flex-direction: column`), declarar `margin-top: auto` en el elemento `.card__pie` empuja el pie contra la base de la tarjeta independientemente de la longitud del texto descriptivo superior, logrando una alineación perfecta en todas las tarjetas de la fila.

---

## 9. Errores comunes

| Error | Síntoma | Solución |
|---|---|---|
| Esperar que flex alinee «hijos de hijos» | No pasa nada | Flex solo actúa sobre hijos **directos**. |
| `height: 100%` en items de columna | Altura 0/extraña | Usar `align-items: stretch` (default) o alturas definidas en el contenedor. |
| Items que no encogen | Desborde horizontal | `min-width: 0` / `overflow: hidden`. |
| `float` dentro de flex | Float ignorado | Esperado: flex items no flotan. |
| Esperar que `justify-content` centre en vertical | No pasa nada | En `row`, el eje transversal se controla con `align-items` (o `margin-block: auto` en el item). |
| Olvidar `flex-wrap: wrap` | Items comprimidos hasta desaparecer | Añadir wrap o revisar bases. |

!!! success "Checklist antes de dar el flex por bueno"

    - [ ] Sé cuál es el **eje principal** con mi `flex-direction` actual.
    - [ ] `flex-wrap: wrap` está **donde quiero** (envolver) o se ha olvidado.
    - [ ] Los items con texto largo llevan `min-width: 0` o `overflow` distinto de `visible`.

## 9. Autoevaluación rápida

1. ¿Qué hace `flex: 1 1 0%` y por qué es distinto de `flex: auto`?
2. Explica la diferencia visual entre `space-between`, `space-around` y `space-evenly`.
3. Tu tarjeta con una URL larguísima rompe la fila. Diagnóstico y arreglo en una línea.
4. ¿Cómo harías que el tercer item ocupara el doble de espacio que el resto?
5. ¿Por qué `order` es peligroso para accesibilidad?

!!! tip "Claves para el examen"

    - Flexbox es **1D** (un eje reparte, el otro alinea); para filas Y columnas → Grid (unidad 06).
    - `justify-content` = eje principal; `align-items` = eje transversal; `align-content` solo con **varias líneas**.
    - `flex: 1` = `1 1 0%` (**ignora el contenido**); `flex: auto` = `1 1 auto` (**parte del contenido**).
    - El item nace con `min-width: auto`: si no se encoge, la solución es ==`min-width: 0`==.
    - `gap` separa items y `margin-*-auto` **empuja**; `order` cambia solo lo visual.

*[DOM]: Document Object Model, el árbol de elementos del documento
*[i18n]: internacionalización (del inglés *internationalization*)
