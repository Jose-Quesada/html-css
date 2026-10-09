---
icon: lucide/move
title: "Unidad 04 — Posicionamiento y z-index"
description: "Propiedad position en todos sus valores, bloques contenedores, offsets, contexto de apilamiento y z-index explicados a fondo, position: sticky y patrones prácticos."
modulo: "LMH (0373) / DIW (0615)"
unidad: 4
fecha: "2026-09-06"
---

# Unidad 04 · Posicionamiento y z-index

`position` decide **cómo se sitúa** la caja respecto al flujo normal del documento. Junto con el concepto de *contexto de apilamiento*, es uno de los temas con más «magia negra» aparente… hasta que se entiende.

!!! note "Conocimientos previos"

    - Flujo normal y modelo de caja (→ [03-modelo-de-caja.md](03-modelo-de-caja.md)).
    - `float` y `display`, que aquí interaccionan (→ [07-flujo-multicolumna-tablas-display.md](07-flujo-multicolumna-tablas-display.md)).

## 1. Los cinco valores de `position`


| Valor | Comportamiento | Sale del flujo? |
|---|---|---|
| `static` (default) | Flujo normal; ignora `top/right/bottom/left`. | No |
| `relative` | Flujo normal + desplazamiento **visual** desde su posición original (el espacio reservado se mantiene). | No |
| ==`absolute`== | Se posiciona respecto a su **bloque contenedor**; el espacio original desaparece. | Sí |
| `fixed` | Como `absolute`, pero respecto al **viewport** (no se mueve al hacer scroll). | Sí |
| ==`sticky`== | Híbrido: se comporta como `relative` hasta alcanzar un umbral, luego «se pega» como `fixed` dentro de su contenedor. | No |

## 2. Bloque contenedor (containing block)

El elemento de referencia para `absolute`/`fixed` y para porcentajes de offsets:

1. Para `position: absolute`: el **ancestro más cercano** con `position` ≠ `static` (o `transform`, `filter`, `perspective`, `contain: layout`… ver abajo). Si no existe, el *initial containing block* (≈ viewport).
2. Para `position: fixed`: el **viewport**, salvo que un ancestro tenga `transform`, `perspective`, `filter`, `backdrop-filter`, `contain: paint/layout` o `will-change` de esas propiedades → entonces ese ancestro se convierte en su bloque contenedor (bug clásico de modales que «saltan»).
3. Para `position: sticky`: el **contenedor padre directo** (solo puede moverse dentro de él).

!!! info "Los porcentajes se miden aquí"

    `top: 50%` se calcula sobre el **alto del bloque contenedor**, no sobre la ventana.

> **Claves para el examen**: «¿Respecto a qué se posiciona un elemento absoluto?» → el ancestro positioned más cercano. Y saber que `transform` en un abuelo rompe el `fixed` de un nieto.

## 3. Offsets: `top`, `right`, `bottom`, `left` y `inset`

```css title="offsets-y-inset.css" hl_lines="2 5"
.capa {
  position: absolute; /* (1)! */
  top: 1rem; right: 1rem;
  /* atajo moderno: */
  inset: 0;              /* rellena todo el bloque contenedor */
  inset: 1rem 2rem;      /* vertical horizontal */
}
```

1.  Sin `position` ≠ `static`, los offsets de debajo se ignoran.

Reglas de interacción (para `absolute`):

- Con `top`+`bottom` definidos y `height: auto` → la altura se resuelve entre ambos.
- Con `left`+`right` y `width: auto` → idem en horizontal.
- Con los cuatro y dimensiones fijas → **se ignora el valor según la dirección** (`direction: ltr` ignora `right`; `rtl` ignora `left`).
- En `relative`, los offsets son **desplazamientos** (pueden ser negativos).

Atajo moderno: ==`inset`== resume los cuatro offsets en una sola línea.

## 4. `z-index` y contexto de apilamiento ⚠️

El eje **Z** representa la profundidad de la pantalla (hacia los ojos del usuario). Cuando dos elementos coinciden en el mismo espacio bidimensional (ejes X e Y), `z-index` decide cuál se dibuja por encima y cuál queda tapado debajo.

Sin embargo, el motivo por el que tantos desarrolladores acaban escribiendo frustrados `z-index: 999999 !important;` sin éxito es porque desconocen el concepto de **Contexto de Apilamiento (*Stacking Context*)**.

### 4.1. La analogía del rascacielos: ¿Por qué mi `z-index` no funciona?

Imagina dos edificios: el **Edificio A** y el **Edificio B**.

- El Edificio A solo tiene **1 planta**.
- El Edificio B tiene **10 plantas**.
- Dentro del Edificio A, una persona sube a una mesa de 3 metros de altura (`z-index: 9999`).
- En el Edificio B, una persona está en el suelo de la segunda planta (`z-index: 2`).

¿Quién está más alto en el cielo? Obviamente la persona del Edificio B. No importa que la persona de A se suba a una mesa de 10.000 metros: **está atrapada dentro del límite de altura de su edificio**.

En CSS ocurre exactamente igual:

- Cada **Contexto de Apilamiento** es un "edificio independiente".
- Los valores de `z-index` de los hijos solo compiten **dentro de su propio edificio**.
- Entre edificios distintos, lo único que decide quién tapa a quién es el `z-index` del **padre** que crea el contexto.

### 4.2. ¿Qué crea un nuevo Contexto de Apilamiento?

Un elemento crea su propio "edificio" (contexto de apilamiento) cuando cumple cualquiera de estas condiciones comunes:

1. Tiene `position: relative`, `absolute`, `fixed` o `sticky` **Y** tiene `z-index` distinto de `auto` (incluso `z-index: 0`).
2. Es un hijo de un contenedor Flexbox o Grid y tiene un `z-index` asignado.
3. Tiene una opacidad menor que 1 (`opacity: 0.99`).
4. Utiliza transformaciones CSS (`transform: translate(...)`, `scale()`, `rotate()`).
5. Utiliza filtros gráficos (`filter: blur(...)` o `backdrop-filter`).
6. Tiene la propiedad moderna declarada explícitamente: `isolation: isolate;`.

### 4.3. Orden natural de apilamiento dentro de un mismo contexto

Cuando varios elementos conviven en el mismo contexto, el navegador los dibuja estrictamente en este orden (de la capa del fondo hacia la capa superior más visible):

1. **Fondo y bordes** del elemento contenedor raíz.
2. Hijos con `z-index` **negativo** (ej: `z-index: -1`).
3. Bloques normales en el flujo estándar (sin posición definida).
4. Elementos flotantes (`float`).
5. Elementos en línea (*inline*) y textos en el flujo normal.
6. Elementos posicionados (`position` ≠ `static`) con `z-index: auto` o `0` (se desempatan por orden en el HTML: el que está más abajo en el código se dibuja encima).
7. Elementos posicionados con `z-index` **positivo** (de menor a mayor valor numérico).

### 4.4. Caso práctico: El modal y el menú desplegable

```html title="z-index-que-no-funciona.html"
<div class="tarjeta" style="opacity: 0.95;"> <!-- Crea contexto aislante -->
  <button class="btn-ayuda" style="position: absolute; z-index: 99999;">
    Botón con z-index gigante
  </button>
</div>

<nav class="barra-navegacion" style="position: sticky; top: 0; z-index: 10;">
  Menú superior
</nav>
```

- A pesar de que el botón tiene `z-index: 99999`, al hacer scroll el `.barra-navegacion` (con solo `z-index: 10`) **lo tapa por completo**.
- **Causa:** La `.tarjeta` tiene `opacity: 0.95`, lo que creó un nuevo contexto de apilamiento cuyo nivel global es `auto` (menor que 10). El botón quedó encerrado dentro.
- **Solución profesional:** Nunca infles el `z-index` de los hijos. Sube el `z-index` del contenedor padre o utiliza una escala semántica documentada.

!!! warning "Error común"

    Posicionar sin contexto: un `absolute` **sin ancestro positioned** vuela, y el `z-index` de un hijo **no sube** si su padre no crea contexto. Arregla el **contenedor**.

> **Claves para el examen**: dibujar la jerarquía de contextos y explicar por qué `z-index` solo se compara **dentro del mismo contexto**. Pregunta estrella: «tengo z-index: 9999 y no sube, ¿por qué?».

### 4.4. Buena práctica: escala de z-index

Define una **escala documentada** (mejor, con custom properties):

```css title="escala-de-z-index.css" hl_lines="6"
:root {
  --z-bajo: 1;        /* fondos decorativos */
  --z-normal: 2;
  --z-header: 100;    /* cabecera sticky */
  --z-dropdown: 200;
  --z-modal: 300;
  --z-toast: 400;
  --z-tooltip: 500;
}
```

Evita `z-index: 9999` escalando conflictos; usa `isolation: isolate` para aislar componentes y no contaminar la escala global.

## 5. `position: sticky` en profundidad

```css title="cabecera-sticky.css" hl_lines="3"
.cabecera {
  position: sticky;
  top: 0;                 /* umbral respecto al borde superior del scroll portador */
  z-index: var(--z-header);
}
```

Características y trampas:

- Se «pega» **dentro de su contenedor directo**: cuando el contenedor termina, la cabecera se va con él.
- Necesita un **offset** (`top`/`bottom`/`left`/`right`); sin offset no hace nada.
- Un ancestro con `overflow: hidden/auto/scroll` **rompe** el sticky (ese ancestro se convierte en scroll portador). Revisa la cadena de padres.
- Los márgenes del elemento cuentan: `margin-top` desplaza el punto de enganche.
- No colapsa márgenes (no está en flujo «puro»).
- Usos: **cabeceras de tabla, TOC lateral, barras de acción**, columnas pegadas en tablas grandes.

!!! question "Mi sticky no se pega"

    He escrito `position: sticky; top: 0` y la cabecera no se mueve. ¿Dos causas?

    ??? success "Respuesta"

        1. **Falta el offset**: sin `top`/`bottom` no hay umbral y no se desplaza.
        2. Un **ancestro con `overflow`** es el scroll portador, o su contenedor ya terminó.

## 6. `position: fixed` y móvil

- Referencia al viewport: cuidado con la barra de direcciones de móviles que aparece/desaparece → las unidades `dvh/svh/lvh` (unidad 08/10) resuelven **alturas estables**.
- `env(safe-area-inset-*)` para no tapar zonas de notch/home-indicator:

```css
.barra {
  position: fixed; bottom: 0; left: 0; right: 0;
  padding-bottom: env(safe-area-inset-bottom);
}
```


## 7. Patrones prácticos

### 7.1. Overlay que cubre todo

```css title="overlay-fijo.css"
.overlay {
  position: fixed; inset: 0;
  background: rgb(0 0 0 / .5);
  z-index: var(--z-modal);
}
```

### 7.2. Modal centrado robusto

```css title="modal-centrado.css"
.modal {
  position: fixed; inset: 0;
  margin: auto;
  width: min(90vw, 32rem);
  max-height: 85dvh;
  overflow: auto;
}
```

(`inset: 0` + `margin: auto` centra sin calcular posiciones.)

### 7.3. Tooltip anclado

```css
.relativo { position: relative; }
.tooltip {
  position: absolute;
  bottom: calc(100% + .5rem);   /* justo encima */
  left: 50%;
  translate: -50% 0;            /* propiedad individual moderna */
  white-space: nowrap;
}
```

### 7.4. Parallax simple con sticky

```css
.parallax { height: 300vh; }
.parallax .escena {
  position: sticky; top: 0;
  height: 100vh;
  /* animación ligada al scroll en unidad 11 */
}
```

### 7.5. Cabecera sticky con sombra al hacer scroll

```css
header { position: sticky; top: 0; transition: box-shadow .3s; }
/* JS mínimo o :has() avanzado para detectar scroll; alternativa pura CSS con scroll-driven animations (U11) */
```

!!! example "Overlay + modal en dos reglas"

    ```css
    .overlay { position: fixed; inset: 0; z-index: var(--z-modal); }
    .modal { position: fixed; inset: 0; margin: auto; }
    ```

## 8. Interacciones con otras propiedades

| Propiedad | Efecto sobre posicionamiento |
|---|---|
| `transform` | Crea bloque contenedor para `absolute/fixed` descendientes + contexto de apilamiento. |
| `filter` / `backdrop-filter` | Idem. |
| `will-change: transform` | Idem (anticipado). |
| `contain: layout/paint` | Aísla layout/pintura; afecta a `fixed`. |
| `display: contents` | El elemento deja de generar caja: su `position` se pierde (los hijos «heredan» el contexto del abuelo). |
| `float` | Genera BFC parcial; incompatible con `position` positioned (el float se ignora). |

---

## 9. Ejemplo práctico: interfaz con cabecera sticky, badge flotante, modal y escala de `z-index`

El siguiente ejemplo articula los esquemas fundamentales de posicionamiento (`relative`, `absolute`, `fixed`, `sticky`) junto a una escala modular de variables para `z-index`, aplicando la propiedad `isolation: isolate` para blindar los contextos de apilamiento y evitar colisiones entre capas.

```html title="posicionamiento.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Posicionamiento y Capas · Panel de Control</title>
  <link rel="stylesheet" href="css/posicionamiento.css">
</head>
<body>
  <!-- 1. Cabecera adhesiva (Sticky) -->
  <header class="barra-navegacion">
    <div class="barra-navegacion__contenido">
      <span class="logo">AppDAW</span>
      <nav class="acciones">
        <button type="button" class="btn-notificaciones" aria-label="Notificaciones del sistema">
          🔔
          <span class="insignia-contador" aria-hidden="true">3</span>
        </button>
      </nav>
    </div>
  </header>

  <main class="contenedor-principal">
    <section class="tarjeta-perfil">
      <div class="tarjeta-perfil__cabecera">
        <!-- Badge posicionado absolutamente respecto a su padre -->
        <span class="etiqueta-estado">En línea</span>
      </div>
      <h2>Servidor de Despliegue</h2>
      <p>Instancia de producción ejecutándose en Ubuntu 24.04 LTS.</p>
    </section>

    <!-- Simulación de scroll vertical para evidenciar el comportamiento sticky -->
    <div class="espaciador-scroll">
      <p>Haz scroll para comprobar cómo la cabecera se mantiene adherida en la parte superior del viewport.</p>
    </div>
  </main>

  <!-- 2. Ventana modal flotante con telón fijo (Fixed + Inset) -->
  <aside class="modal-overlay" role="dialog" aria-modal="true" aria-labelledby="tit-modal">
    <div class="modal-caja">
      <h3 id="tit-modal">Confirmar reinicio</h3>
      <p>¿Estás seguro de que deseas reiniciar la instancia de producción?</p>
      <div class="modal-botones">
        <button type="button" class="btn btn--cancelar">Cancelar</button>
        <button type="button" class="btn btn--peligro">Reiniciar</button>
      </div>
    </div>
  </aside>
</body>
</html>
```

```css title="css/posicionamiento.css"
/* 1. Reset y escala semántica de contextos de apilamiento */
:root {
  --z-base: 1;
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-overlay: 300;
  --z-modal: 400;
  --z-tooltip: 500;

  --color-fondo: #f1f5f9;
  --color-primario: #0284c7;
  --color-peligro: #ef4444;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: system-ui, -apple-system, sans-serif;
  background-color: var(--color-fondo);
  color: #0f172a;
  min-height: 200vh; /* Permite scroll vertical */
}

/* 2. Cabecera adhesiva (Sticky) */
.barra-navegacion {
  position: sticky;
  top: 0; /* Punto de anclaje obligatorio para activar sticky */
  z-index: var(--z-sticky);
  background-color: rgb(255 255 255 / 0.9);
  backdrop-filter: blur(8px); /* Efecto translúcido */
  border-bottom: 1px solid #cbd5e1;
  padding: 0.75rem 1.5rem;
}

.barra-navegacion__contenido {
  max-width: 60rem;
  margin-inline: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* 3. Botón contenedor y Badge absoluto */
.btn-notificaciones {
  position: relative; /* Bloque contenedor para la insignia absoluta */
  background: none;
  border: none;
  font-size: 1.25rem;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 0.5rem;
}

.insignia-contador {
  position: absolute;
  top: 0.15rem;
  right: 0.15rem;
  background-color: var(--color-peligro);
  color: #ffffff;
  font-size: 0.7rem;
  font-weight: 700;
  min-width: 1.1rem;
  height: 1.1rem;
  line-height: 1.1rem;
  text-align: center;
  border-radius: 9999px;
  box-shadow: 0 0 0 2px #ffffff; /* Separador nítido contra el fondo */
}

/* 4. Tarjeta con contexto de apilamiento aislado */
.contenedor-principal {
  max-width: 60rem;
  margin-inline: auto;
  padding: 2rem 1.5rem;
}

.tarjeta-perfil {
  position: relative;
  isolation: isolate; /* Crea un nuevo stacking context local e infranqueable */
  background: #ffffff;
  padding: 2rem;
  border-radius: 1rem;
  border: 1px solid #e2e8f0;
  box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);
}

.etiqueta-estado {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background-color: #dcfce7;
  color: #15803d;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.25rem 0.6rem;
  border-radius: 9999px;
}

.espaciador-scroll {
  margin-top: 4rem;
  padding: 2rem;
  background-color: #e2e8f0;
  border-radius: 0.5rem;
  text-align: center;
  color: #64748b;
}

/* 5. Modal centrado en viewport con telón Fixed */
.modal-overlay {
  position: fixed;
  inset: 0; /* Equivale a top: 0; right: 0; bottom: 0; left: 0; */
  background-color: rgb(15 23 42 / 0.6);
  z-index: var(--z-overlay);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem;
}

.modal-caja {
  position: relative;
  background: #ffffff;
  border-radius: 1rem;
  padding: 2rem;
  max-width: 28rem;
  width: 100%;
  box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.2);
  z-index: var(--z-modal);
}

.modal-botones {
  display: flex;
  justify-content: flex-end;
  gap: 0.75rem;
  margin-top: 1.5rem;
}

.btn {
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-weight: 600;
  cursor: pointer;
  border: 1px solid transparent;
}

.btn--cancelar {
  background: #f1f5f9;
  color: #475569;
}

.btn--peligro {
  background: var(--color-peligro);
  color: #ffffff;
}
```

---

### 9.1 Explicación detallada: ¿Por qué se usa cada propiedad y para qué sirve?

A continuación se analizan en detalle las reglas de posicionamiento y gestión del apilamiento empleadas en el código:

#### 1. `position: sticky` con `top: 0`
- **¿Cómo funciona?** El elemento se comporta como `position: relative` en el flujo normal hasta que el usuario realiza scroll y alcanza el umbral definido por el offset (`top: 0`). A partir de ese punto exacto, se "pega" a la parte superior de la ventana comportándose como `fixed` hasta que su elemento padre sale de la vista.
- **Requisitos obligatorios:**
    - Debe acompañarse siempre de al menos un offset direccional (`top`, `bottom`, etc.).
    - Ningún elemento ancestro puede tener propiedades de recorte (`overflow: hidden`, `auto` o `scroll`), ya que de lo contrario el contenedor de scroll se transferiría a ese ancestro e impediría la fijación contra la ventana.

#### 2. La pareja `position: relative` + `position: absolute`
- **En la insignia `.insignia-contador`:**
    - Un elemento con `position: absolute` sale por completo del flujo normal del documento y se posiciona respecto a su **ancestro posicionado más próximo** (*Containing Block*).
    - Para que la insignia roja se coloque exactamente en la esquina del botón de la campana y no viaje hasta la esquina superior de toda la pantalla, añadimos deliberadamente `position: relative` a `.btn-notificaciones`.
    - `position: relative` en el padre no mueve el botón (no tiene offsets), pero **crea el marco de coordenadas cerrado** para los cálculos de `top: 0.15rem; right: 0.15rem;` del hijo.

#### 3. `position: fixed` con la propiedad lógica abreviada `inset: 0`
- **¿Para qué sirve?** Ancla el elemento de forma inamovible respecto al **viewport** del navegador (la pantalla del dispositivo), ignorando el desplazamiento del scroll.
- **`inset: 0`:** Es la propiedad abreviada moderna que reemplaza a la declaración clásica de cuatro líneas:
  ```css
  top: 0; right: 0; bottom: 0; left: 0;
  ```
  Al combinarse con un color semitransparente, genera un telón de fondo (*overlay*) que cubre el 100% de la ventana en cualquier resolución o dispositivo.

#### 4. `isolation: isolate` y control defensivo de `z-index`
- **El problema de la guerra de `z-index: 9999`:** En proyectos grandes, distintos desarrolladores empiezan a aumentar descontroladamente los valores de `z-index` para hacer que un elemento suba por encima de otro, generando conflictos catastróficos donde un desplegable traspasa una ventana modal.
- **La solución con `isolation: isolate`:**
    - Crea un **nuevo contexto de apilamiento local** (*stacking context*) en `.tarjeta-perfil` sin necesidad de aplicar `z-index` ni propiedades complejas.
    - Todo lo que ocurra dentro de esa tarjeta (sus sombras, sus badges absolutos) queda estrictamente confinado dentro de su capa. Ningún elemento interno podrá jamás escapar ni solaparse por encima del modal o de la cabecera sticky global.

#### 5. Escala de variables para capas en `:root`
- Centralizar los valores en `--z-sticky: 200; --z-overlay: 300; --z-modal: 400;` asegura que la arquitectura visual sea coherente y fácil de auditar: un modal siempre estará por encima del overlay, y este por encima de la barra de navegación pegajosa.

---

## 10. Errores comunes

| Error | Síntoma | Solución |
|---|---|---|
| `absolute` sin ancestro positioned | Vuela a la esquina del viewport | Añadir `position: relative` al contenedor lógico. |
| `fixed` que «salta» al abrir modal | El modal se descoloca | Eliminar `transform/filter` de ancestros del portal, o montar el modal en `<body>` (portal). |
| Sticky que no se pega | Queda quieto | Buscar `overflow` en ancestros; comprobar offset. |
| Guerra de `z-index: 9999` | Caos de capas | Escala de variables + `isolation: isolate`. |
| `top/left` con `static` | No pasa nada | Esperado: static ignora offsets. |

!!! success "Checklist de posicionamiento"

    - [ ] Los `absolute` apuntan al **contenedor lógico** correcto.
    - [ ] Ningún ancestro con `transform/filter` rompe mi `fixed`/`sticky`.
    - [ ] Los `z-index` salen de una **escala con variables**.

## 11. Autoevaluación rápida

1. Enumera cinco formas (además de `position+z-index`) de crear un contexto de apilamiento.
2. ¿Por qué un `position: fixed` dentro de un carrusel con `transform` se mueve con el carrusel?
3. Tu tooltip tiene `z-index: 9999` y sigue debajo del header. Explica dos causas posibles y su arreglo.
4. ¿Qué rompería primero un `position: sticky`: un `overflow: hidden` en el body o en el padre directo?
5. Escribe el CSS para una barra fija inferior que respete el safe-area de iOS.

!!! tip "Claves para el examen"

    - `static` **ignora** los offsets; `relative` desplaza **sin** salir del flujo; `absolute`/`fixed` **sí** salen.
    - Bloque contenedor: **ancestro positioned más cercano** en `absolute`; **viewport** en `fixed` (salvo `transform`/`filter`). Crea contexto de apilamiento `position` ≠ `static` con `z-index` ≠ `auto`, y también `opacity`, `transform`, `filter` o `isolation: isolate`.
    - **Dentro** de un contexto los `z-index` se comparan **entre sí**: «tengo 9999 y no sube» → revisa el **contenedor**.
    - `sticky` necesita **offset** y un padre **sin `overflow`**; para centrar, `inset: 0` + `margin: auto` (§7.2).

*[viewport]: área visible de la ventana del navegador (la ventana de render)
