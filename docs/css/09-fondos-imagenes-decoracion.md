---
icon: lucide/image
title: "Unidad 09 — Fondos, imágenes y decoración"
description: "Propiedad background completa, degradados, formatos de imagen y su optimización, srcset/picture/object-fit, bordes, sombras, filtros, blend modes, máscaras y clip-path."
modulo: "LMH (0373) / DIW (0615)"
unidad: 9
fecha: "2026-09-06"
---

# Unidad 09 · Fondos, imágenes y decoración

Cubre el RA 3/4 del módulo 0615 (preparar e integrar contenido multimedia) desde el lado CSS: cómo presentar, optimizar y decorar con imágenes.

!!! note "Conocimientos previos"

    - Modelo de caja y **unidades** de la [unidad 03](03-modelo-de-caja.md).
    - Imágenes y multimedia en HTML: `<img>`, `alt` y formatos (unidad 04).
    - Idea de **accesibilidad** y de métrica de rendimiento (unidad 13).

## 1. `background`: la propiedad maestra

Domina ==background-size==: `cover` **llena recortando**, `contain` **cabe entero**.

### 1.1. Subpropiedades

| Propiedad | Valores clave | Notas |
|---|---|---|
| `background-image` | `url()`, degradados, `image-set()`, `element()` (sin soporte), `paint()` (Houdini, parcial) | Acepta **lista** (varias capas). |
| `background-position` | `x y`, keywords (`top left`…), `%`, longitudes | Con dos valores: primero X, luego Y. |
| `background-size` | `cover`, `contain`, longitud(es), `%`, `auto` | `cover`: llena recortando; `contain`: cabe entero. |
| `background-repeat` | `repeat`, `no-repeat`, `repeat-x/y`, `space`, `round` | `space`/`round`: reparten sin cortar tiles. |
| `background-origin` | `padding-box`, `border-box`, `content-box` | De dónde se mide la posición. |
| `background-clip` | `border-box` (def), `padding-box`, `content-box`, **`text`** | `text`: recorta al texto (efecto degradado tipográfico). |
| `background-attachment` | `scroll` (def), `local`, `fixed` | `fixed`: parallax barato (cuidado en móvil: muchos lo desactivan). |
| `background-color` | cualquier color | Capa base siempre visible. |
| `background-blend-mode` | modos de mezcla (ver sección 6) | Mezcla cada capa de imagen con el color/capas inferiores. |

!!! info "Una propiedad, ocho subpropiedades"

    - `background` es un **atajo**: lo que no escribas se resetea.
    - Cada subpropiedad admite **listas**, una entrada por capa.
    - Primera capa de la lista = **la que se pinta encima**.

### 1.2. El atajo `background`

```css title="hero.css" hl_lines="2"
.hero {
  background: #0b1020 url("/img/fondo.jpg") center / cover no-repeat fixed;
}
```

Orden libre, pero: la **primera** longitud = position, la **segunda** = size (separadas por `/`). Resetear con `background: none` o `background: initial`.

### 1.3. Múltiples capas

```css title="capas.css"
.textura {
  background-image:
    url("ruido.svg"),                       /* capa 1 (encima) (1)! */
    radial-gradient(circle at 20% 20%, rgb(255 0 0 / .2), transparent 50%),
    linear-gradient(#222, #111);            /* capa base */
  background-size: 200px, auto, auto;       /* por capa, mismo orden (2)! */
  background-repeat: repeat, no-repeat, no-repeat;
}
```

1.  La **primera de la lista se pinta encima** de las demás.
2.  Las listas se emparejan **por posición**: 3 tamaños para 3 capas.

La primera de la lista se pinta **encima**. Cada subpropiedad en lista se aplica por posición.

## 2. Degradados (gradient)

Para examen, el ==linear-gradient== es el rey: **dirección + paradas de color**.

### 2.1. `linear-gradient`

```css title="degradado.css"
background-image: linear-gradient(
  135deg,                          /* dirección */
  var(--c1) 0%,                    /* parada inicial */
  var(--c2) 50%, var(--c3) 100%    /* paradas intermedias */
);
/* atajos de dirección: to right, to bottom left, 45deg… */
```

- Ángulo: `0deg` = hacia arriba; `90deg` = hacia la derecha.
- Paradas dobles (`red 20% 40%`) crean **tramos sólidos**.
- Interpolación en espacio elegido: `linear-gradient(in oklab, red, blue)` evita el paso por marrón.

### 2.2. `radial-gradient`

```css title="radial.css"
background-image: radial-gradient(
  circle at top left,              /* forma + origen */
  #fff 0%, #8894d0 90%
);
/* ellipse | circle [radio], at pos */
```

### 2.3. `conic-gradient`

```css title="conico.css"
background-image: conic-gradient(from 45deg, #f00, #ff0, #0f0, #00f, #f0f, #f00);
/* anillos: conic-gradient(at 50% 50%, transparent 0 25%, #fff 0 50%, …) */
```

Usos: donuts de progreso, aros, efectos «candy stripe», combinado con `mask` para gauge.

### 2.4. Repetidos

`repeating-linear-gradient(45deg, #eee 0 10px, #fff 10px 20px)` → rayas infinitas sin imagen. Ídem `repeating-radial-gradient` y `repeating-conic-gradient`.

!!! example "Rayas sin descargar nada"

    ```css
    .via {
      background: repeating-linear-gradient(90deg, #facc15 0 40px, transparent 40px 80px);
    }
    ```

    **Cero peticiones** y escala infinita: patrón generado por el navegador.

### 2.5. Trucos clásicos con degradados

```css title="trucos.css"
/* Texto con degradado */
.titulo {
  background: linear-gradient(90deg, #6366f1, #ec4899);
  background-clip: text;
  color: transparent;   /* -webkit-background-clip: text en Safari antiguo */
}

/* Borde degradado (truco de doble fondo) */
.borde-grad {
  border: 3px solid transparent;
  background:
    linear-gradient(#fff, #fff) padding-box,
    linear-gradient(90deg, #f0f, #0ff) border-box;
}

/* Línea divisoria que desvanece */
.divisor {
  height: 1px; border: 0;
  background: linear-gradient(90deg, transparent, currentColor, transparent);
}
```

## 3. Imágenes: formatos y elección (RA 3)

La regla de oro: foto → ==AVIF==/WebP, **icono → SVG**, animación corta → WebP.

| Formato | Tipo | Compresión | Transparencia | Animación | Cuándo |
|---|---|---|---|---|---|
| **AVIF** | Raster | Mejor (20–50% menos que WebP) | Sí | Sí | Imágenes modernas; fallback WebP. |
| **WebP** | Raster | Muy buena | Sí | Sí | Estándar actual universal. |
| **JPEG** | Raster | Buena (pérdida) | No | No | Fotos sin transparencia. |
| **PNG-8** | Raster | Media (paleta) | 1 bit | No | Gráficos simples, logos planos. |
| **PNG-24** | Raster | Pesada | Alfa | No | Capturas con gradientes/transparencia compleja. |
| **GIF** | Raster | Pobres (256 colores) | 1 bit | Sí | Legacy; sustituir por WebP animado. |
| **SVG** | Vector | Textual | Sí | Sí (SMIL/CSS) | Iconos, logotipos, ilustraciones geométricas, patrones. |
| **ICO/cur** | Raster | — | — | — | Favicons/cursors. |

Reglas de oro:

1. **Foto → AVIF/WebP**; **icono/logo → SVG**; **animación corta → WebP/GIF solo legacy**.
2. Optimiza: calidad 70–85, dimensiones reales (no servir 4000 px donde caben 800), stripping de metadatos.
3. SVG: comprime (SVGO), inline si es un icono pequeño (permite `currentColor`), `aria-hidden="true"` si decorativo.
4. Pesa: una imagen de 200 KB mal elegida cuesta más que toda tu hoja CSS.

!!! success "Checklist antes de subir una imagen"

    - [ ] Formato elegido: **AVIF/WebP**, SVG para iconos.
    - [ ] Dimensiones **reales** de uso (sin 4000 px de sobra).
    - [ ] Calidad 70–85 y metadatos retirados.
    - [ ] `width`/`height` o `aspect-ratio` declarados.

## 4. Integrar imágenes en HTML+CSS (RA 4)

La etiqueta responsable es ==srcset==: **variantes + `sizes`** y el navegador elige.

### 4.1. `<img>` responsivo con `srcset` y `sizes`

```html title="imagen.html" hl_lines="2 3"
<img src="foto-800.webp"
     srcset="foto-400.webp 400w, foto-800.webp 800w, foto-1600.webp 1600w"
     sizes="(max-width: 600px) 100vw, 50vw"
     alt="Descripción" width="800" height="600" loading="lazy"> <!-- (1)! -->
```

1.  `400w/800w/1600w` declaran el **ancho real** de cada variante; `width`/`height` y `loading="lazy"` **evitan CLS**.

- `width`/`height` en atributos → reserva de espacio → **evita CLS** (unidad 14).
- `loading="lazy"` nativo; `fetchpriority="high"` para LCP.

### 4.2. `<picture>` para arte direccional y formatos

```html title="picture.html"
<picture>
  <source media="(min-width: 900px)" srcset="hero-ancha.avif" type="image/avif">
  <source srcset="hero-movil.webp" type="image/webp">
  <img src="hero-movil.jpg" alt="" width="1600" height="900">
</picture>
```

### 4.3. `object-fit` / `object-position`

```css title="tarjeta.css"
.card img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;          /* fill | contain | cover | none | scale-down */
  object-position: center top;
}
```

`object-fit` resuelve el «recorte elegante» sin crop manual; combínalo con ==`aspect-ratio`== para galerías uniformes.

### 4.4. Imagen como fondo vs `<img>`

| Criterio | `background-image` | `<img>` |
|---|---|---|
| Semántica/accesibilidad | Decorativa (invisible para AT) | Contenido (alt, focusable, seleccionable) |
| Carga | Solo si se pinta (puede no cargarse) | Siempre (con lazy) |
| Layout | No ocupa espacio propio | Ocupa caja |
| Uso correcto | Texturas, hero decorativos, patrones | Fotografía de contenido, iconos informativos |

> **Claves para el examen**: «¿Cuándo usar background-image?» → cuando la imagen es **decorativa**. Si aporta información, es `<img>` con `alt`.

!!! warning "Error común"

    Meter una imagen **con información** en `background-image`: el lector de pantalla no la anuncia y no admite `alt`. Si comunica, va en un `<img>`; el fondo es solo **decoración**.

### 4.5. `image-rendering` y `image-set()`

```css title="fondos.css"
.pixel-art { image-rendering: pixelated; }   /* o crisp-edges */
.fondo-adaptable {
  background-image: image-set(url("fondo-1x.png") 1x, url("fondo-2x.png") 2x);
}
```

## 5. Bordes, sombras y contornos

### 5.1. Bordes

```css title="bordes.css"
.tarjeta {
  border: 1px solid var(--borde);
  border-radius: 1rem;               /* los 4 */
  border-start-start-radius: 2rem;   /* esquinas lógicas (i18n) */
  border-end-end-radius: 2rem;
}
```

- `border-style` obligatorio (`solid`, `dashed`, `dotted`, `double`, `groove`…).
- Radio > mitad del lado → **elipse automática**.

### 5.2. `box-shadow`

```css title="sombras.css" hl_lines="3"
.elevada {
  box-shadow:
    0 1px 2px rgb(0 0 0 / .08),
    0 8px 24px rgb(0 0 0 / .12);   /* (1)! */
}
.interna { box-shadow: inset 0 2px 4px rgb(0 0 0 / .2); }
/* formato: x y blur spread color [inset] — varias capas separadas por coma */
```

1.  Dos capas: **sombra corta** de contacto + **sombra difusa** de elevación.

Las sombras **no** afectan al layout (pintan fuera): reserva espacio si son grandes o usa `outline`/bordes para elementos interactivos.

### 5.3. `outline` (el amigo del foco)

```css title="foco.css"
:focus-visible { outline: 2px solid var(--enfoque); outline-offset: 2px; }
```

`outline` no ocupa espacio, sigue el radio moderno en navegadores actuales, y es **obligatorio** mantenerlo visible (WCAG 2.4.7). Nunca `outline: none` sin reemplazo.

## 6. Filtros y modos de mezcla

### 6.1. `filter`

```css title="filtros.css"
.desenfocada { filter: blur(8px); }
.combinado   { filter: grayscale(1) contrast(1.1) brightness(.95) drop-shadow(0 4px 8px rgb(0 0 0/.3)); }
```

Funciones: `blur()`, `brightness()`, `contrast()`, `grayscale()`, `hue-rotate()`, `invert()`, `opacity()`, `saturate()`, `sepia()`, ==`drop-shadow()`== (respeta alpha, a diferencia de box-shadow), `url()` (SVG filters).

!!! info "Filtro, sombra o blend"

    - **`filter`**: altera el propio elemento (píxeles ya pintados).
    - **`drop-shadow()`**: sombra que **respeta la alfa** de formas irregulares.
    - **`mix-blend-mode`**: mezcla el elemento con lo que hay **detrás**.

### 6.2. `backdrop-filter`

```css title="vidrio.css"
.vidrio {
  background: rgb(255 255 255 / .6);
  backdrop-filter: blur(12px) saturate(1.4);
  /* glassmorphism clásico; requiere -webkit- en Safari */
}
```

Coste de GPU alto: no abusar en listas largas.

### 6.3. Blend modes (`mix-blend-mode`, `background-blend-mode`)

Modos principales: `multiply` (oscurece), `screen` (aclara), `overlay`, `soft-light`, `difference`, `exclusion`, `hue`, `saturation`, `color`, `luminosity`.

```css title="mezcla.css"
.marca-sobre-foto { mix-blend-mode: multiply; }   /* logo tinta sobre foto */
.capas { background-blend-mode: overlay; }        /* textura sobre degradado */
```

Requieren que el elemento no rompa la «banda» (sin `opacity` fraccionaria en intermediarios sin necesidad).

## 7. Máscaras y `clip-path`

Aquí decide ==clip-path== (recorte **duro**) frente a `mask` (máscara de **alfa**).

### 7.1. `clip-path`

```css title="recortes.css"
.circulo  { clip-path: circle(50% at 50% 50%); }
.hexagono { clip-path: polygon(25% 0, 75% 0, 100% 50%, 75% 100%, 25% 100%, 0 50%); }
.inset    { clip-path: inset(10px round 12px); }
.trayecto { clip-path: path("M0,50 C50,0 150,100 200,50"); }
.externa { clip-path: url("#mi-mascara-svg"); }
```

Recorta la **pintura** (incluye shadow? no: box-shadow se recorta también). No afecta al hit-testing fuera del recorte.

### 7.2. `mask` / `mask-image`

A diferencia de clip (dúo todo/nada), mask trabaja con **alfa**:

```css title="mascara.css"
.desvanecido {
  mask-image: linear-gradient(to right, black 60%, transparent);
  mask-size: 100% 100%;
}
.mascara-img {
  mask: url("logo.svg") center / contain no-repeat;
  /* el contenido solo se ve donde el logo es opaco */
}
```

Propiedades: `mask-image`, `mask-mode` (`match-source | alpha | luminance`), `mask-position/size/repeat`, `mask-clip` (`border-box | padding-box | content-box | stroke | fill`), `mask-origin`, `mask-composite`. Soporte sin prefijo: Chrome 120+, Firefox 53+, Safari 15.4+.

Casos: fundidos de carrousels, textos con textura, íconos rellenables con `currentColor` + mask.

!!! question "Recorte o máscara"

    ¿Qué uso para un hexágono de bordes nítidos y qué para fundir un logo hacia la derecha?

    ??? success "Respuesta"

        **Hexágono → `clip-path`** (recorte duro, todo/nada). **Fundido → `mask-image`** con degradado: trabaja por **alfa** y permite medios tonos.

## 8. Patrones decorativos completos

### 8.1. Glassmorphism accesible

```css title="glass.css"
.panel {
  background: light-dark(rgb(255 255 255 / .65), rgb(20 20 25 / .65));
  backdrop-filter: blur(14px);
  border: 1px solid rgb(from var(--marca) r g b / .25); /* relative color syntax */
}
@media (prefers-reduced-transparency: reduce) {
  .panel { backdrop-filter: none; background: Canvas; }
}
```

(`rgb(from … r g b / .25)` = *relative color syntax*, Color L5.)

### 8.2. Skeleton loader con degradado animado

```css title="skeleton.css"
.skeleton {
  background: linear-gradient(90deg, #eee 25%, #f7f7f7 50%, #eee 75%);
  background-size: 200% 100%;
  animation: shimmer 1.2s infinite;
}
@keyframes shimmer { to { background-position: -200% 0; } }
```

### 8.3. Fondo con ruido (textura)

```css title="ruido.css"
body::before {
  content: "";
  position: fixed; inset: 0;
  background: url("data:image/svg+xml,…fractalNoise…") ;
  opacity: .04; pointer-events: none;
}
```

??? note "Para saber más"

    Las texturas **inline en `data:`** ahorran una petición, pero inflan el HTML: para gráficos grandes, mejor un archivo aparte con **caché** y `background-size` ajustado.

## 9. Errores comunes

| Error | Síntoma | Solución |
|---|---|---|
| Imagen de contenido como `background` | Invisible para lectores de pantalla | `<img>` + `alt`. |
| Sin `width/height` ni `aspect-ratio` | CLS al cargar | Dimensiones explícitas. |
| `background-size: cover` sin `position` | Recorte aleatorio | `background-position` intencional. |
| GIF pesado de 3 MB | LCP fatal | WebP animado o video corto. |
| `backdrop-filter` en 50 items | FPS bajos | Limitar a pocos elementos. |
| `transparent` en degradado de color | Banda gris | Alpha del propio tono. |

## 10. Autoevaluación rápida

1. Ordena las capas de este `background-image` de arriba a abajo y explica el resultado visual.
2. ¿Qué hace `object-fit: cover` con `aspect-ratio: 1` en una foto 16:9?
3. Diferencia entre `clip-path` y `mask-image` con un ejemplo de uso de cada uno.
4. Escribe el CSS de un borde degradado de 3px con interior blanco.
5. ¿Por qué `drop-shadow()` es mejor que `box-shadow` para un SVG con formas irregulares?
6. Justifica la elección de formato para: (a) logo, (b) foto de producto, (c) animación de 2 s.

!!! tip "Claves para el examen"

    - `background` es un **atajo**: lo no indicado se resetea y la **primera capa va encima**.
    - Foto → **AVIF/WebP**, icono → **SVG**; calidad 70–85 y dimensiones reales.
    - Imagen decorativa → `background`; imagen con información → **`<img>` con `alt`**.
    - `width`/`height` + `aspect-ratio` = **cero CLS**.
    - `clip-path` recorta **duro**; `mask` trabaja con **alfa**.
    - `outline` **nunca** se elimina sin reemplazo visible (WCAG 2.4.7).

*[RA]: Resultado de Aprendizaje
*[CLS]: Cumulative Layout Shift
*[LCP]: Largest Contentful Paint
