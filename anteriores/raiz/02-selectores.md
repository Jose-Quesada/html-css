---
title: "Unidad 02 — Selectores"
description: "Tipos de selectores, combinadores, selectores de atributo, pseudo-clases (incluidas :has, :is, :where, :focus-visible), pseudo-elementos y cálculo práctico de especificidad."
modulo: "LMH (0373) / DIW (0615)"
unidad: 2
fecha: "2026-09-06"
---

# Unidad 02 · Selectores

Los selectores definen **a qué elementos** se aplican las declaraciones. Dominarlos es la diferencia entre CSS mantenible y CSS con `!important` por todas partes.

## 1. Taxonomía general

```text
Selector complejo = [combinador] + simple(s)
Simple = tipo | universal | clase | ID | atributo | pseudo-clase | pseudo-elemento
```

Ejemplo anatómico: `nav > ul li a[href^="https"]:not(.externo)::after`

| Parte | Rol |
|---|---|
| `nav` | tipo (ancestro) |
| `>` | combinador hijo |
| `ul li` | descendientes |
| `a[href^="https"]` | elemento con atributo que empieza por… |
| `:not(.externo)` | negación funcional |
| `::after` | pseudo-elemento |

## 2. Selectores simples

### 2.1. Universal

```css
* { box-sizing: border-box; }
```

Selecciona todo. En resets modernos se usa con cuidado (ver unidad 14: coste de estilo en muchos nodos).

### 2.2. Por tipo (etiqueta)

```css
h1 { font-size: 2rem; }
p  { line-height: 1.6; }
```

Case-insensitive en HTML. Evitar sobreuso: acopla el diseño al HTML concreto.

### 2.3. Por clase

```css
.alerta { border-left: 4px solid orange; }
.card--destacado { /* BEM: modificador */ }
```

- Es el selector **caballo de batalla**: reutilizable, semántico, especificidad moderada.
- Un elemento puede tener varias clases: `class="alerta alerta--error"`.
- Convenciones de nombre: kebab-case; patrones BEM en unidad 12.

### 2.4. Por ID

```css
#cabecera-principal { position: sticky; top: 0; }
```

- Debe ser **único por documento** (requisito HTML).
- Especificidad alta → difícil de sobreescribir sin más IDs o `!important`.
- Usos legítimos: anclas de navegación (`<section id="precios">`), puntos de entrada de JS, una instancia única (header, main landmark).
- **No** usar IDs como «clase fuerte» para maquetar componentes repetibles.

### 2.5. Por atributo

| Sintaxis | Significado | Ejemplo |
|---|---|---|
| `[attr]` | Tiene el atributo | `input[required]` |
| `[attr="valor"]` | Coincide exactamente (case-sensitive) | `a[target="_blank"]` |
| `[attr="valor" i]` | Case-**in**sensitive | `input[type="text" i]` |
| `[attr~="palabra"]` | Contiene la palabra (separada por espacios) | `li[data-tags~="css"]` |
| `[attr\|="prefijo"]` | Igual o empieza por `prefijo-` | `[lang\|="es"]` |
| `[attr^="prefijo"]` | Empieza por | `img[src^="data:image/svg"]` |
| `[attr$="sufijo"]` | Termina por | `a[href$=".pdf"]` |
| `[attr*="sub"]` | Contiene substring | `input[name*="busca"]` |

Flags `i`/`s`: `i` insensible a mayúsculas, `s` sensible (default). Solo tienen sentido en valores string.

Usos típicos: estilos condicionales según estado del formulario (`[aria-expanded="true"]`), enlaces externos, tipos de archivo, internacionalización (`[dir="rtl"]`).

## 3. Combinadores

| Combinador | Nombre | Significado | Ejemplo |
|---|---|---|---|
| *(espacio)* | Descendiente | `B` en cualquier nivel dentro de `A` | `article p` |
| `>` | Hijo | `B` hijo directo de `A` | `ul > li` |
| `+` | Hermano siguiente inmediato | `B` justo después de `A`, mismo padre | `h2 + p` |
| `~` | Hermano general siguiente | `B` tras `A` (no necesariamente seguido) | `input ~ .mensaje` |

> **Claves para el examen**: diferenciar `+` (inmediato) y `~` (cualquier posterior). Y recordar que el combinador descendiente **no** exige parentesco directo.

## 4. Pseudo-clases

Estados dinámicos del elemento. Se escriben con un `:`.

### 4.1. Estructurales

| Pseudo-clase | Descripción |
|---|---|
| `:root` | El elemento raíz (`<html>`). Donde viven las custom properties globales. |
| `:first-child` | Primer hijo de su padre. |
| `:last-child` | Último hijo. |
| `:only-child` | Único hijo. |
| `:nth-child(n)` | n-ésimo hijo (cuenta **todos** los hermanos). |
| `:nth-last-child(n)` | n-ésimo desde el final. |
| `:first-of-type` / `:last-of-type` / `:only-of-type` | Como arriba pero filtrando por tipo. |
| `:nth-of-type(n)` / `:nth-last-of-type(n)` | n-ésimo de su tipo. |
| `:empty` | Sin hijos ni texto. |
| `:scope` | El elemento desde el que se evalúa (útil en contexto de `:has` y consultas). |

#### La fórmula `An+B` de `:nth-*`

`n` y `b` son enteros (puede ser 0); `n` indica el paso:

| Fórmula | Selección |
|---|---|
| `:nth-child(2n)` | pares: 2, 4, 6… |
| `:nth-child(2n+1)` | impares: 1, 3, 5… |
| `:nth-child(3n)` | cada 3: 3, 6, 9… |
| `:nth-child(3n+1)` | 1, 4, 7… (posición 1 de cada grupo de 3) |
| `:nth-child(-n+3)` | solo los 3 primeros |
| `:nth-child(even)` / `:nth-child(odd)` | alias de `2n` / `2n+1` |
| `:nth-child(5)` | exactamente el quinto (equivalente a `n+4`) |

Truco visual para `3n+1`: imagina los hijos en filas de 3; selecciona siempre la primera columna.

### 4.2. Estado de la interfaz (UI states)

| Pseudo-clase | Cuándo aplica |
|---|---|
| `:hover` | Cursor encima (solo dispositivos con puntero fino). |
| `:active` | Mientras se pulsa. |
| `:focus` | Tiene foco (click o teclado). |
| `:focus-visible` | Foco **por teclado** (o cuando el navegador decide mostrarlo). Es la forma accesible de estilizar foco sin molestar al ratón. |
| `:focus-within` | El elemento **o un descendiente** tiene foco (ideal para «glow» de formularios). |
| `:target` | Elemento cuyo `id` coincide con el fragmento de la URL (`#seccion`). |
| `:target-is(sel)` | `:target` aplicado a un conjunto de selectores. |
| `:playing` / `:paused` | Media en reproducción/pausa. |
| `:defined` | Web Component definido. |

Orden recomendado para estados interactivos (evita conflictos):

```css
.boton {}
.boton:hover {}
.boton:focus-visible {}
.boton:active {}
.boton:disabled {}
```

### 4.3. Estado de recursos / formularios

| Pseudo-clase | Aplica a | Significado |
|---|---|---|
| `:link` / `:visited` | `<a>` | Visitado o no. |
| `:checked` | `input` radio/checkbox | Marcado. |
| `:indeterminate` | checkbox | Estado mixto (JS `indeterminate = true`). |
| `:enabled` / `:disabled` | Formularios | Habilitado/deshabilitado. |
| `:read-only` / `:read-write` | Campos | Solo lectura / editable. |
| `:valid` / `:invalid` | Campos con constraints | Válido/inválido (con constraint validation API). |
| `:user-valid` / `:user-invalid` | Idem | Solo tras interacción del usuario (más amable). |
| `:required` / `:optional` | Campos | Con/sin restricción requerida. |
| `:placeholder-shown` | Campos | Muestra el placeholder (vacío). |
| `:default` | Elementos | En estado por defecto. |
| `:current` / `:past` / `:future` | Tiempo (`time`, `output`) | Relación con la fecha actual. |

### 4.4. Funcionales (el poder moderno)

#### `:is()` — «cualquiera de»

Toma una lista de selectores complejos; el elemento lo cumple si **cualquiera** de ellos lo hace. Aporta la especificidad del argumento de mayor peso.

```css
/* Antes: repetir reglas */
h1, h2, h3, .titulo { margin-bottom: 0.5em; }

/* Después */
:is(h1, h2, h3, .titulo) { margin-bottom: 0.5em; }

/* Potente con combinadores */
article :is(h2, h3) a { color: inherit; }
```

#### `:where()` — «cualquiera de», especificidad cero

Igual que `:is()`, pero **siempre aporta 0** a la especificidad. Ideal para construir selectores «blandos» fáciles de sobreescribir:

```css
:where(article, aside) :where(p, li) { line-height: 1.6; }
/* Especificidad total: (0,0,0)… gana cualquier regla concreta */
```

Además, es *forgiving*: si un argumento es inválido en algún navegador, se descarta ese argumento y no toda la regla.

#### `:not()` — negación

Acepta cualquier selector complejo (Selectors L4):

```css
:not(.activo)          /* todos menos .activo */
li:not(:nth-child(3))  /* todos menos el tercero */
a:not([href])          /* enlaces sin href */
button:not(:disabled)  /* botones operativos */
```

#### `:has()` — el «selector padre»

Selecciona un elemento **si contiene (o está relacionado con)** algo que cumple la condición. Es el selector más potente de la historia de CSS:

```css
/* Card que contiene imagen → cambia estilo */
.card:has(> img) { grid-template-columns: 200px 1fr; }

/* Campo con error marcado por JS */
.form-field:has(input:user-invalid) { border-color: red; }

/* Nav con submenú abierto */
.nav-item:has(> .submenu[aria-expanded="true"]) { background: #eee; }

/* Página con vídeo → layout distinto */
body:has(video) { overflow: hidden; }

/* Tabla con filas vacías */
.table:has(tbody:empty) { display: none; }
```

Reglas clave:

- El argumento de `:has()` puede usar **cualquier combinador**, incluso hacia atrás: `:has(+ .etiqueta)` («tengo una etiqueta inmediatamente después»).
- Su especificidad = la del argumento.
- Soporte: Chrome 105+, Safari 15.4+, Firefox 121+ (estable en los tres grandes).
- Permite patronear estados **sin JavaScript** (checkbox hack, menús desplegables, validación visual).

#### Otros funcionales útiles

| Pseudo-clase | Uso |
|---|---|
| `:lang(es)` | Elemento cuyo idioma calculado es español (según `lang`). |
| `:dir(ltr)` / `:dir(rtl)` | Dirección de escritura del elemento. |
| `:any-link` | `:link` + `:visited` juntos (permite estilizar ambos sin exponer historial). |
| `:local-link` | Enlaces a la misma máquina (experimental). |

## 5. Pseudo-elementos

Representan **partes** de un elemento, no el elemento. Se escriben con **dos** dos puntos (`::`).

| Pseudo-elemento | Qué genera |
|---|---|
| `::before` | Caja ficticia **antes** del contenido (requiere `content`). |
| `::after` | Caja ficticia **después**. |
| `::first-line` | Primera línea de un bloque. |
| `::first-letter` | Primera letra (capitular). |
| `::selection` | Texto seleccionado por el usuario. |
| `::placeholder` | Texto placeholder de inputs. |
| `::marker` | Viñeta/número de listas (`list-style` fuera del flujo). |
| `::backdrop` | Fondo oscurecido de diálogos (`<dialog>`). |
| `::file-selector-button` | Botón «Examinar…» de `<input type=file>`. |
| `::cue` | Subtítulos (WebVTT). |
| `::spelling` / `::grammar-error` | Errores ortográficos/gramaticales (soporte limitado). |
| `::part(nombre)` | Pieza expuesta de un Web Component. |
| `::slotted(selector)` | Contenido slotted de un Web Component. |
| `::view-transition-old/new/group/root` | Capas de view transitions (unidad 11). |

### `::before` / `::after` en profundidad

```css
.icono::before {
  content: "";               /* obligatorio (string, counter o url) */
  display: inline-block;
  width: 1em; height: 1em;
  background: currentColor;
  mask: url("icon.svg") center / contain no-repeat;
}

.cita::before { content: open-quote; }
.cita::after  { content: close-quote; }   /* respetan lang → « » vs " " */
.paso::before { content: counter(paso) ". "; counter-increment: paso; }
```

- No aparecen en el DOM (los lectores de pantalla los ignoran salvo `content` textual relevante: cuidado, el texto de `content` **sí** puede leerse en algunos lectores → usa `aria-hidden` si es decorativo).
- `content: counter(nombre)` y `counters()` permiten numeración avanzada (índices, apéndices).
- `@counter-style` personaliza formatos (romanos, alfabetos, imágenes por valor) — ver unidad 12.

> **Error común**: escribir `:before` con un solo dos puntos. Los navegadores lo aceptan por compatibilidad, pero la spec manda `::before`; en código nuevo, siempre doble.

## 6. Especificidad: ejemplos resueltos

Recordad la escala: **en línea > !important (autor) > (ID, clase, tipo)**.

| Selector | Cálculo | Resultado |
|---|---|---|
| `p` | 1 tipo | 0-0-1 |
| `.card` | 1 clase | 0-1-0 |
| `#hero` | 1 ID | 1-0-0 |
| `ul li a.active:hover` | 2 clases + pseudo-clase + 2 tipos | 0-3-2 |
| `:is(#a, .b, span)` | toma el máximo: ID | 1-0-0 |
| `:where(.a, .b)` | siempre 0 | 0-0-0 |
| `:has(.error input)` | especificidad del argumento | 0-1-1 |
| `div::before` | 1 tipo + 1 pseudo-elemento | 0-0-2 |
| `style="color:red"` | en línea | ∞ (fuera de escala) |

### Estrategias anti-guerra-de-especificidad

1. **Acotar profundidad**: máx. 2–3 niveles de combinadores.
2. **Preferir clases** a cadenas de tipos.
3. Usar `:where()` para «reglas base» que cualquiera pueda pisar.
4. `@layer` para ordenar prioridades de arquitectura (unidad 12).
5. Si necesitas `!important`, pregunta si el problema es de **arquitectura**, no de fuerza.

## 7. Rendimiento de selectores (matiz importante)

El coste real está en **cuántos elementos visita** el motor, no en la «complejidad teórica»:

- `body div p` recorre mucho más que `p.texto`.
- El selector universal `*` en resets toca a todos los nodos: hoy aceptado (coste trivial frente a claridad), pero evita `*` en reglas frecuentes.
- Los selectores se compilan una vez; el matching se repite en cada cambio de DOM. Mantener selectores cortos y específicos ayuda al **estilo incremental**.
- No optimices prematuramente: primero estructura clara, luego mide con DevTools.

## 8. Buenas prácticas resumidas

1. Clases semánticas (`.tarjeta__precio`), no visuales (`.caja-blanca-grande`).
2. Máximo un ID por selector; mejor ninguno en componentes.
3. `:focus-visible` para foco, nunca `outline: none` sin alternativa.
4. Estados de formulario con pseudo-clases nativas antes que clases JS.
5. `:has()` para lógica condicional simple sin JS.
6. `:is()`/`:where()` para DRY sin inflar especificidad.
7. Documenta selectores «mágicos» con comentarios.

## 9. Autoevaluación rápida

1. ¿Qué selecciona `form :nth-child(2n) input`? ¿Y `form input:nth-child(2n)`?
2. Escribe un selector: «párrafos que contienen un enlace externo, pero no si están dentro de `footer`».
3. ¿Por qué `:where(a, b, c)` es útil en un design system?
4. Calcula: `main article:has(figure) h2 + p:first-of-type`.
5. ¿Puedo seleccionar el padre de un `input:focus` sin `:has()`? ¿Cómo lo haría con él?
