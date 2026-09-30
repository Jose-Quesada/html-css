---
title: "Unidad 11 — Transiciones y animaciones"
description: "Transiciones CSS, @keyframes, funciones de temporización, transform y 3D, scroll-driven animations, @starting-style, View Transitions y accesibilidad del movimiento."
modulo: "LMH (0373) / DIW (0615)"
unidad: 11
fecha: "2026-09-06"
---

# Unidad 11 · Transiciones y animaciones

Dos mecanismos distintos que se complementan:

| Mecanismo | Disparador | Uso |
|---|---|---|
| **Transición** | Cambio de valor de una propiedad (hover, clase, estado) | Micro-interacciones suaves entre dos estados. |
| **Animación** (`@keyframes`) | Tiempo (y hoy, scroll) | Secuencias complejas, loops, entradas/salidas. |

## 1. Transiciones

### 1.1. Propiedades

```css
.boton {
  background: #2563eb;
  transition:
    background-color .2s ease,
    transform .2s cubic-bezier(.34, 1.56, .64, 1),
    box-shadow .2s ease;
}
.boton:hover {
  background: #1d4ed8;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgb(37 99 235 / .4);
}
```

| Propiedad | Valores | Notas |
|---|---|---|
| `transition-property` | nombres, `all` | Evitar `all` en producción (sorpresas + rendimiento). |
| `transition-duration` | `s`, `ms` | 150–300 ms lo normal para UI. |
| `transition-timing-function` | ver 1.2 | Forma de la curva. |
| `transition-delay` | `s`, `ms` | Positivo o negativo (empieza a mitad de curva). |
| `transition-behavior` | `normal` / `allow-discrete` | Permite transicionar propiedades discretas (ver 1.4). |

El atajo `transition` acepta varias listas separadas por coma; el orden por lista es `propiedad duración función [delay]`.

### 1.2. Timing functions

Keywords: `ease` (def), `linear`, `ease-in`, `ease-out`, `ease-in-out`.

**`cubic-bezier(x1, y1, x2, y2)`**: curva bézier; x ∈ [0,1], y puede salirse (rebote). Referencias útiles:

```css
--ease-out-quint: cubic-bezier(.22, 1, .36, 1);   /* salida suave, estándar UI */
--ease-spring:    cubic-bezier(.34, 1.56, .64, 1);/* rebote ligero */
--ease-snappy:    cubic-bezier(.1, .9, .2, 1);
```

**`steps(n, direction)`**: saltos discretos (sprites, contadores): `steps(8, end)`.

Regla de diseño: las cosas que **aparecen** entran con `ease-out`; las que **desaparecen**, con `ease-in`; las que se **mueven continuamente**, `linear` o `ease-in-out`.

### 1.3. Qué propiedades transitan bien

- **Continuas** (siempre): `color`, `background-color`, `opacity`, `transform`, `width/height` (caras layout), `box-shadow`, bordes…
- **Discretas** (`display`, `visibility`, `z-index`…): no transitan salvo con `transition-behavior: allow-discrete` (Chrome 117+, Firefox 129+, Safari 17.4+):

```css
.menu {
  display: none;
  opacity: 0;
  transition: display .3s allow-discrete, opacity .3s;
}
.menu[aria-hidden="false"] { display: block; opacity: 1; }
@starting-style {
  .menu[aria-hidden="false"] { opacity: 0; }  /* punto de partida de entrada */
}
```

### 1.4. Trampas clásicas

| Problema | Causa | Solución |
|---|---|---|
| La transición «no va» al quitar clase | El estilo destino debe estar en el elemento cuando cambia | Definir `transition` en el estado base, no solo en `:hover`. |
| Animar `width/height/margin` tiembla | Recalcula layout cada frame | Animar `transform: scale()` u `opacity` donde sea posible. |
| `display:none` no transiciona | Es discreto | `allow-discrete` + `@starting-style`, o `visibility`+`opacity`. |

## 2. `@keyframes` y `animation`

### 2.1. Sintaxis

```css
@keyframes aparecer {
  from { opacity: 0; transform: translateY(1rem); }
  to   { opacity: 1; transform: none; }
}
@keyframes carga {
  0%   { transform: rotate(0deg); }
  50%  { transform: rotate(180deg); border-top-color: transparent; }
  100% { transform: rotate(360deg); }
}
.spinner { animation: carga .8s linear infinite; }
```

- Paradas: `from/to` o porcentajes; pueden faltar (interpolación automática).
- Nombres case-sensitive; varios keyframes por regla vía `animation-name: a, b`.

### 2.2. Propiedades de `animation`

| Propiedad | Valores clave | Efecto |
|---|---|---|
| `animation-name` | nombre(s) | Obligatorio (en el atajo). |
| `animation-duration` | tiempo | Duración por iteración. |
| `animation-timing-function` | curvas | Por tramo si se define dentro de keyframes. |
| `animation-delay` | tiempo | Espera inicial (negativa = arranca adelantado). |
| `animation-iteration-count` | número, `infinite` | Repeticiones. |
| `animation-direction` | `normal`, `reverse`, `alternate`, `alternate-reverse` | Sentido. |
| `animation-fill-mode` | `none`, `forwards`, `backwards`, `both` | Mantener estilos fuera del ciclo: `forwards` conserva el último frame; `backwards` aplica el primer frame durante el delay; `both` = los dos. |
| `animation-play-state` | `running`, `paused` | Pausar (p. ej., fuera de viewport). |

Atajo: `animation: nombre duración función delay iteraciones dirección fill play-state`.

Ejemplo completo:

```css
.toast {
  animation:
    toast-in .3s ease-out both,
    toast-out .3s ease-in 3s forwards;
}
@keyframes toast-in  { from { translate: 0 100%; opacity: 0; } }
@keyframes toast-out { to   { translate: 0 100%; opacity: 0; } }
```

## 3. `transform`: el motor del movimiento

### 3.1. Funciones

```css
transform:
  translateX(10px) translateY(-4px)   /* o translate(10px, -4px) */
  scale(1.05)                          /* o scaleX/Y */
  rotate(45deg)                        /* o rotateX/Y/Z */
  skewX(10deg);
transform: matrix(a, b, c, d, tx, ty); /* forma cruda */
```

### 3.2. Propiedades individuales modernas

```css
.card {
  translate: 0 -4px;      /* independiente de transform */
  rotate: 2deg;
  scale: 1.03;
  transition: translate .2s, scale .2s;
}
```

Ventaja: se componen sin sobrescribir y son más legibles; `transform` sigue siendo el atajo combinado.

### 3.3. Origen y 3D

```css
.transformable {
  transform-origin: top left;        /* punto de referencia */
  perspective: 800px;                /* en el PADRE da profundidad a hijos */
  transform: rotateY(20deg);
  transform-style: preserve-3d;      /* mantiene 3D en hijos anidados */
  backface-visibility: hidden;       /* oculta la cara trasera */
}
```

- `perspective` en el padre ≠ `perspective()` en transform (equivalente pero distinto contexto).
- Crear `transform` genera bloque contenedor y contexto de apilamiento (unidad 04): cuidado con `position: fixed` dentro.

### 3.4. Rendimiento del movimiento

Jerarquía de coste por frame:

1. **Compositor** (baratísimo): `transform`, `opacity`, `filter` → se mueve en GPU sin repaint.
2. **Paint**: sombras, bordes, fondos → repinta.
3. **Layout** (caro): `top/left/width/height/margin/padding` → recalcula geometría global.

Reglas:

- Anima `transform`/`opacity` siempre que puedas («mover» = `translate`, no `top`).
- `will-change: transform` promociona a capa propia **antes** de la animación; retíralo después (consume memoria):

```css
.hero-img { will-change: transform; }
/* o desde JS: el.style.willChange = 'transform'; … luego 'auto' */
```

- No poner `will-change` «por si acaso» en todo: cada capa gasta RAM.

## 4. Scroll-driven animations (CSS puro, sin JS) ⭐

Nueva spec (Animations L2): ligar animaciones al **scroll**. Soporte: Chrome 115+, Safari 26+; Firefox en desarrollo. Usa `@supports` como fallback.

### 4.1. `animation-timeline`

```css
/* Progreso de lectura: barra que crece con el scroll de la página */
.progreso {
  position: fixed; top: 0; left: 0; height: 3px; width: 100%;
  transform-origin: left;
  transform: scaleX(0);
  animation: crecer linear;
  animation-timeline: scroll(root);
}
@keyframes crecer { to { transform: scaleX(1); } }

/* Elemento que aparece al entrar en viewport */
.revelar {
  animation: aparecer both;
  animation-timeline: view();
  animation-range: entry 0% entry 100%;
}
@keyframes aparecer {
  from { opacity: 0; transform: translateY(2rem); }
}
```

| Timeline | Referencia |
|---|---|
| `scroll(root)` | Scroll del documento. |
| `scroll(nearest)` / `scroll(self)` / `scroll(verso)` | Contenedor scrolleable cercano/propio. |
| `view()` | Progreso del **elemento animado** cruzando el viewport. |
| `view(inline/block)` | Por eje. |

### 4.2. `animation-range`

Segmentos de `view()`: `cover`, `entry`, `containment`, `exit` (con `%`):

```css
animation-range: entry 0% cover 30%;  /* empieza a entrar, termina cubierto al 30% */
```

### 4.3. Patrones

- Barra de progreso de lectura.
- Revelado de secciones al hacer scroll (parallax suave con `translate` ligado a `view()`).
- Escala de imágenes en carrousel según cercanía al centro.
- Indicadores de sección activos (nav lateral).

> **Claves para el examen**: saber que existen, su estado de soporte (parcial) y el patrón de degradación con `@supports (animation-timeline: scroll())`.

## 5. `@starting-style`

Define el **estado inicial** para elementos que aparecen (montados) en el DOM, permitiendo transiciones de entrada sin JS:

```css
.modal {
  opacity: 0;
  translate: 0 1rem;
  transition: opacity .25s ease-out, translate .25s ease-out;
}
.modal.abierto { opacity: 1; translate: 0 0; }

@starting-style {
  .modal.abierto { opacity: 0; translate: 0 1rem; }
}
```

Sin él, al añadir `.abierto` el navegador parte del estilo ya aplicado (sin transición de entrada). Soporte: Chrome 117+, Firefox 129+, Safari 17.5+.

## 6. View Transitions API (transiciones entre vistas)

Permite transicionar **entre dos estados completos del documento** (navegación SPA o MPA con progressive enhancement):

```css
::view-transition-old(root),
::view-transition-new(root) { animation-duration: .3s; }

.tarjeta { view-transition-name: tarjeta-principal; }
/* ese elemento hace morphing entre vistas (shared element) */
```

```js
// JS mínimo para activar (MPA):
document.startViewTransition(() => navegar());
```

- Pseudo-elementos: `::view-transition-old/new/group/root`, `::view-transition-image-pair`.
- Soporte: Chrome 111+, Firefox 144+, Safari 18+.
- Casos: cambio de detalle↔lista con morphing, rotación de tema, navegación entre páginas.

## 7. Accesibilidad del movimiento (imprescindible)

1. **`prefers-reduced-motion: reduce`**: desactiva o minimiza animaciones no esenciales (WCAG 2.3.3 AA):

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: .01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: .01ms !important;
  }
  html { scroll-behavior: auto; }
}
```

2. Nunca parpadeos > 3 veces/segundo (epilepsia fotosensible, WCAG 2.3.1).
3. Las animaciones deben ser **decorativas o reversibles**; la información no debe depender solo de ellas.
4. Respetar también `prefers-reduced-transparency` (glassmorphism) y `forced-colors`.
5. Prueba con el ajuste del SO activado, no solo emulando.

## 8. Errores comunes

| Error | Síntoma | Solución |
|---|---|---|
| `transition: all` | Propiedades inesperadas animan (incluso layout) | Listar propiedades concretas. |
| Animar `left/top` | Jank en móvil | `transform: translate()`. |
| `will-change` permanente | RAM alta, artefactos | Aplicar justo antes y retirar. |
| Olvidar `fill-mode` | Salto al terminar | `forwards`/`both`. |
| Keyframes con `!important` | No funciona (los keyframes no aceptan importancia así) | Reestructurar. |
| Ignorar reduced motion | Usuarios mareados | Bloque global (sección 7). |

## 9. Autoevaluación rápida

1. Diferencia entre `transition` y `animation` con un ejemplo de cada uno.
2. ¿Qué hace `animation-fill-mode: backwards` durante el `delay`?
3. Explica `cubic-bezier(.34, 1.56, .64, 1)` y cuándo usarías esa curva.
4. Escribe una scroll-driven animation de revelado con `view()` y su fallback con `@supports`.
5. ¿Por qué animar `transform` es más barato que animar `top`?
6. ¿Qué problema resuelve `@starting-style`?
