---
title: "Unidad 10 — Diseño responsivo"
description: "Filosofía mobile-first, media queries completas, tipografía y espaciado fluidos con clamp(), breakpoints, unidades de viewport dinámicas y container queries (tamaño y estilo)."
modulo: "LMH (0373) / DIW (0615)"
unidad: 10
fecha: "2026-09-06"
---

# Unidad 10 · Diseño responsivo

El diseño responsivo (Ethan Marcotte, 2010) parte de tres pilares: **layout fluido**, **imágenes flexibles** y **media queries**. Hoy se completa con `clamp()`, unidades dinámicas y **container queries**. El objetivo: una sola base de código que se adapta a cualquier viewport, orientación y capacidad del dispositivo.

## 1. Fundamentos no negociables

### 1.1. El `<meta name="viewport">`

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Sin él, los móviles emulan un viewport de ~980px y «escalan» la página (texto diminuto). Es el requisito 0.

### 1.2. Mobile-first

Escribir primero las reglas para pantallas pequeñas y **ampliar** con `min-width`:

```css
/* Base = móvil */
.tarjetas { display: grid; gap: 1rem; }

/* Tablet+ */
@media (min-width: 48em) {
  .tarjetas { grid-template-columns: repeat(2, 1fr); }
}
/* Desktop+ */
@media (min-width: 64em) {
  .tarjetas { grid-template-columns: repeat(3, 1fr); }
}
```

Ventajas: CSS más ligero por defecto, progresivo (los navegadores viejos ven la versión simple), y fuerza a priorizar contenido.

> **Claves para el examen**: explicar por qué `min-width` (mobile-first) frente a `max-width` (desktop-first): mejora progresiva + menos overrides.

### 1.3. Layouts intrínsecamente fluidos antes que breakpoints

Mucho «responsivo» no necesita media queries:

```css
.contenedor {
  width: min(100% - 2rem, 70rem);   /* fluido con tope */
  margin-inline: auto;
}
.galeria {
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
}
.prosa { font-size: clamp(1rem, .9rem + .5vw, 1.125rem); }
```

Usa breakpoints solo cuando el **diseño cambia estructuralmente** (nav → hamburguesa, sidebar desaparece…), no para cada detalle.

## 2. Media queries a fondo

### 2.1. Sintaxis

```css
@media [not|only] tipo y (expresión) { … }
@media (min-width: 40em) and (max-width: 60em), (prefers-color-scheme: dark) { … }
```

- `and` combina; coma = OR.
- `not`/`only`: históricos (evitar `only`; hoy es ruido).
- Múltiples features en una consulta: todas deben cumplirse (`and` implícito entre paréntesis separados por coma NO: usa `and`).

### 2.2. Features principales

| Feature | Valores | Uso |
|---|---|---|
| `width` / `height` | longitudes | Breakpoints clásicos. |
| `aspect-ratio` | `16/9`, `4/3`… | Proporción del viewport. |
| `orientation` | `portrait` / `landscape` | Ajustes por giro. |
| `color` | entero | Bits de profundidad (raro hoy). |
| `color-gamut` | `srgb`, `p3`, `rec2020`… | Servir colores amplios si hay soporte. |
| `resolution` | `dpi/dppx` | Fondos nítidos en retina. |
| `pointer` | `none`, `coarse`, `fine` | ¿Tiene puntero preciso? |
| `hover` | `none`, `hover` | ¿Puede hoverear? (móviles: `hover: none`). |
| `any-pointer` / `any-hover` | Idem pero «algún dispositivo conectado». |
| `update` | `slow`, `fast` | Frecuencia de refresco. |
| `prefers-color-scheme` | `light`, `dark`, `no-preference` | Tema del SO. |
| `prefers-reduced-motion` | `no-preference`, `reduce` | **Accesibilidad**: reducir animaciones. |
| `prefers-reduced-transparency` | `no-preference`, `reduce` | Accesibilidad: evitar transparencias/backdrop. |
| `prefers-reduced-data` | `no-preference`, `reduce` | Ahorro de datos (navegadores con data saver). |
| `prefers-contrast` | `no-preference`, `less`, `more`, `custom` | Modos de alto contraste. |
| `forced-colors` | `active`, `none` | Windows Forced Colors (accesibilidad). |

### 2.3. Ejemplos combinados

```css
/* Solo dispositivos con puntero fino y hover real */
@media (hover: hover) and (pointer: fine) {
  .card:hover { transform: translateY(-2px); }
}

/* Movimiento reducido: desactivar animaciones no esenciales */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: .01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: .01ms !important;
    scroll-behavior: auto !important;
  }
}

/* Alto contraste forzado: respetar colores del sistema */
@media (forced-colors: active) {
  .boton { forced-color-adjust: none; border: 1px solid ButtonText; }
}
```

> **Error común**: usar `hover:` como única condición de interacción sin fallback para táctil. Los estados deben funcionar también con `:focus-visible` y toque directo.

## 3. Tipografía y espaciado fluidos con `clamp()`

Fórmula general: `clamp(mínimo, valor_ideal_fluido, máximo)`.

Derivación rápida (interpolación lineal entre dos puntos):

```text
quiero 1.5rem a 360px y 3rem a 1200px
pendiente m = (3 - 1.5) / (1200 - 360) rem/px
en vw: m_vw = m * 100 / ancho_base_viewport(1200) ≈ 0.347vw
ordenada b = 1.5rem - m*360 ≈ 1.25rem
→ font-size: clamp(1.5rem, 1.25rem + 0.347vw, 3rem)
```

En la práctica se usan calculadoras (fluid-typography, type-scale-cli) o valores de memoria:

```css
:root {
  --fs-h1: clamp(2.25rem, 1.6rem + 2.2vw, 4rem);
  --fs-h2: clamp(1.75rem, 1.4rem + 1.2vw, 2.5rem);
  --space-section: clamp(3rem, 2rem + 4vw, 6rem);
}
```

Reglas:

- Siempre con **topes** (min/max) para no romper en extremos.
- Aplica a `font-size`, `padding`, `gap`, `margin` → todo el ritmo visual escala.
- Combina con escala modular (unidad 08): los tokens ya son fluidos.

## 4. Breakpoints: estrategia

No existen «los» breakpoints universales; se derivan del **contenido**:

1. Diseña mobile-first y busca los puntos donde el layout **se rompe o mejora**.
2. Referencias habituales (ajustar al proyecto): `480px` (móvil landscape), `768px` (tablet), `1024px` (laptop), `1280px` (desktop), `1536px` (grande).
3. Mejor en `em` que `px` (respeta zoom del usuario): `@media (min-width: 48em)`.
4. Documenta la escala en la guía de estilo (tokens de breakpoint).
5. Evita «breakpoint por feature»: agrupa cambios coherentes.

## 5. Imágenes y media responsivos (repaso operativo)

- `srcset`/`sizes` (unidad 09) para servir el tamaño correcto según viewport.
- `picture` con `media` para arte direccional (cortes distintos móvil/desktop).
- `image-set()` por densidad.
- Video: `<video>` con `poster` y dimensiones; evita autoplay con sonido (usabilidad + baterías).

## 6. Tablas y formularios en pantallas pequeñas

| Técnica | Cuándo |
|---|---|
| `overflow-x: auto` en wrapper | Tablas anchas: scroll horizontal controlado. |
| Columnas ocultas con clases + media query | Datos secundarios en móvil. |
| Transformar fila en bloque (`display:block` + `data-label`) | Tablas simples; cuidar accesibilidad. |
| Formularios: 1 columna → 2 en ancho | `grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr))`. |
| Inputs a `100%` con `max-width` | Evita campos enormes en desktop. |

## 7. Container queries ⭐ (el futuro del componente responsivo)

Las media queries miran el **viewport**; las container queries miran el **contenedor**. Permiten componentes verdaderamente reutilizables que se adaptan al espacio disponible, no al tamaño de pantalla.

### 7.1. Activar un contenedor

```css
.tarjeta-wrap {
  container-type: inline-size;   /* observa el ancho */
  /* container-type: size → observa ancho Y alto (requiere altura definida) */
  container-name: tarjeta;       /* nombre opcional para varias consultas */
}
```

- `inline-size`: solo eje inline (el 95% de los casos).
- `size`: ambos ejes (el contenedor debe tener tamaño definido en ese eje).
- `style`: solo para style queries (ver 7.4).

### 7.2. Consultas `@container`

```css
@container (min-width: 30rem) {
  .tarjeta { grid-template-columns: 12rem 1fr; }  /* horizontal */
}
@container tarjeta (min-width: 40rem) and (orientation: landscape) {
  .tarjeta .titulo { font-size: 1.5rem; }
}
```

Sintaxis idéntica a `@media` (mismas features de tamaño/orientación), pero evaluadas contra el contenedor.

### 7.3. Unidades de contenedor

Dentro del árbol del contenedor:

| Unidad | Significado |
|---|---|
| `cqw` / `cqh` | 1% del ancho/alto del contenedor. |
| `cqi` / `cqb` | 1% del inline/block size. |
| `cqmin` / `cqmax` | Menor/mayor de los anteriores. |

```css
@container { .logo { width: 20cqw; } }   /* siempre 20% del contenedor */
```

### 7.4. Style queries (consultas de estilo)

Consultan **custom properties** del contenedor (temas dinámicos):

```css
.panel { container-style: --theme-density; }

@container style(--theme-density: compact) {
  .panel .item { padding: .25rem; }
}
```

Soporte reciente (Chrome 111+, Firefox 151+, Safari 18+); aún en consolidación.

### 7.5. ¿MQ o CQ?

| Caso | Herramienta |
|---|---|
| Cambia la estructura de la PÁGINA (nav, sidebar) | Media query. |
| Cambia un COMPONENTE según su hueco (widget, tarjeta, sidebar embeddable) | Container query. |
| Preferecias del USUARIO (tema, movimiento, contraste) | Media query `prefers-*`. |

> **Claves para el examen**: diferenciar MQ (viewport) vs CQ (contenedor) y dar el ejemplo del widget reutilizable que se ve distinto en sidebar (estrecho) y en main (ancho) con el mismo código.

## 8. Otras técnicas responsivas

- **`scroll-snap`**: carruseles nativos:

```css
.carrusel {
  display: flex; gap: 1rem;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scrollbar-width: none;
}
.carrusel > * { scroll-snap-align: start; }
```

- **Orden responsive con `order`** (flex/grid): cambiar jerarquía visual por breakpoint (cuidado a11y, unidad 05).
- **Nav adaptativa**: lista → menú desplegable con checkbox hack o JS mínimo + `dialog`.
- **Safe areas**: `env(safe-area-inset-*)` para notches.
- **`text-wrap: balance`** en títulos para evitar viudas en columnas estrechas.

## 9. Testing responsivo

1. DevTools → Device Mode (perfiles + viewport libre + velocidad de red).
2. **Dispositivos reales** (mínimo 1 móvil Android + 1 iOS): emulador ≠ realidad (gestos, barras, teclado).
3. Prueba orientaciones, zoom 200%, texto grande, modo oscuro, datos limitados.
4. Lighthouse (mobile) para métricas reales.
5. Checklist: ¿desbordes horizontales? ¿táctiles ≥ 44×44 px? ¿lectura sin zoom?

## 10. Errores comunes

| Error | Consecuencia | Solución |
|---|---|---|
| Breakpoints en `px` absolutos sin topes | Layout roto en TV/monitores grandes | `max-width` en contenedor + `em` en MQ. |
| Desktop-first con cascada de `max-width` | CSS hinchado, overrides encadenados | Mobile-first con `min-width`. |
| `100vh` fijo en móvil | Barras tapadas / huecos | `100dvh`. |
| Hover como única affordance | Móviles sin feedback | Estados `:active`/`:focus-visible` + color. |
| Imagen gigante servida a móvil | LCP horrible | `srcset`/`sizes` + `loading="lazy"`. |
| Olvidar `prefers-reduced-motion` | Mareos/vértigo | Bloque global de reducción (ver 2.3). |

## 11. Autoevaluación rápida

1. Escribe la consulta: «pantalla ≥ 768px Y modo oscuro preferido».
2. Deriva un `clamp()` para `--space-section` entre 2rem (360px) y 5rem (1200px).
3. ¿Por qué `container-type: inline-size` es suficiente para la mayoría de widgets?
4. Un widget debe verse en 2 columnas si su contenedor supera 400px, sea donde esté. Escríbelo con CQ.
5. ¿Qué features de media query usarías para detectar «dispositivo táctil sin ratón»?
6. Explica la diferencia entre `svh`, `dvh` y `lvh` y cuál usas por defecto.
