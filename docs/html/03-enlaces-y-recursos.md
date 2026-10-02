---
icon: lucide/link
title: "HTML 03 - Enlaces y recursos"
description: "Enlaces y rutas, atributos del enlace, accesibilidad, imágenes con alt, imagen responsive e iframes."
modulo: "LMH (0373) / DIW (0615) / DI (0488)"
unidad: 3
fecha: "2026-09-29"
---

# HTML 03 — Enlaces y recursos

Sin `<a>` no hay hipertexto: destinos, rutas, atributos, accesibilidad, imágenes *responsive* e `<iframe>`.

!!! note "Conocimientos previos"

    - Estructura del documento y atributos globales (`id`, `class`, `lang`).
    - Distinguir ruta absoluta (URL) de relativa (archivo del proyecto).
    - Saber que `id` identifica un bloque de forma única.

## 1. El elemento `<a>`: sintaxis y tipos de destinos

### 1.1 Anatomía de un enlace

```html title="enlace.html" hl_lines="2"
<!-- El destino va siempre en href; sin él <a> no navega -->
<a href="productos.html">Ver el catálogo de productos</a>
```

El destino se declara en ==href== (Hypertext Reference), **obligatorio**: sin él no hay navegación, y el texto interior es **lo que se lee**. `<a>` es de **línea** (*inline*), dentro de los párrafos.

### 1.2 Destinos absolutos, relativos y de raíz

```html title="destinos.html"
<!-- Absoluta: URL completa, sales de tu sitio -->
<a href="https://zensical.org/documentacion/">Documentación de Zensical</a>

<!-- Relativa: MISMA carpeta -->
<a href="aviso-legal.html">Aviso legal</a>

<!-- ./ significa "aquí mismo" (equivale a la anterior) -->
<a href="./contacto.html">Contacto</a>

<!-- ../ sube UN nivel en la estructura -->
<a href="../index.html">Volver a la portada</a> <!-- (1)! -->

<!-- Raíz del sitio: empieza en la carpeta raíz -->
<a href="/documentos/garantia-2-anios.pdf">Garantía de dos años</a> <!-- (2)! -->

<!-- Combinada: ../ + subcarpeta -->
<a href="../img/producto/zapatillas-800w.jpg">Ver la foto en grande</a>
```

1.  **`../`** sube un nivel **desde la página que enlazas**.
2.  **`/`** se ancla a la **raíz del sitio**.

La absoluta **sale del sitio**; la relativa **se mueve dentro**; la de raíz **no depende de la carpeta**.

### 1.3 Destinos especiales: anclas, `mailto:` y `tel:`

```html title="destinos-especiales.html"
<!-- Ancla: destino = id de la MISMA página -->
<h2 id="envios">Política de envíos</h2>
<a href="#envios">Ir a la política de envíos</a>

<!-- Abre el gestor de correo -->
<a href="mailto:soporte@mitienda.es?subject=Duda%20sobre%20un%20pedido">Escribir a soporte</a>

<!-- En un móvil inicia la llamada -->
<a href="tel:+34954123456">Llamar al 954 123 456</a>
```

Las anclas apuntan a `id` **únicos**; con cabecera fija reserva espacio con `scroll-margin-top` en CSS.

!!! info "Destinos que no son páginas"

    - **Ancla** (`#id`): salta a un bloque de la **misma página**.
    - **`mailto:`**: abre el **gestor de correo** con destinatario y asunto opcionales.
    - **`tel:`**: en **móvil inicia la llamada**; en escritorio, la persona elige la aplicación.

## 2. Rutas y estructura de carpetas

### 2.1 Árbol de ejemplo

```text title="arbol.txt"
tienda-ufro/                  <- raíz del sitio
├── index.html                <- página principal
├── producto/
│   ├── zapatillas.html
│   └── mochila.html
├── img/
│   ├── logo.svg
│   └── producto/
│       ├── zapatillas-400w.jpg
│       ├── zapatillas-800w.jpg
│       └── zapatillas-1200w.jpg
├── css/estilos.css
└── documentos/garantia-2-anios.pdf
```

Todas las rutas de este tema se resuelven sobre este **árbol de ejemplo**.

### 2.2 Cómo resolver una ruta paso a paso

1. **Sitúate en la página desde la que enlazas**: la ruta se calcula *desde ahí*, no desde el explorador.
2. **¿Misma carpeta?** → solo el nombre: `aviso-legal.html`.
3. **¿Bajas a una subcarpeta?** → carpeta y nombre: `img/logo.svg`.
4. **¿Subes?** → `../` tantas veces como niveles subas.
5. **¿No depender de dónde estés?** → raíz: `/img/logo.svg`.

```html title="rutas.html"
<!-- CALCULADOS DESDE index.html (raíz) -->
<link rel="stylesheet" href="css/estilos.css">
<a href="producto/zapatillas.html">Zapatillas Run 300</a>

<!-- LOS MISMOS DESDE producto/zapatillas.html (un nivel más abajo) -->
<link rel="stylesheet" href="../css/estilos.css">
<a href="mochila.html">Mochila Trail 25 L</a>   <!-- hermano: misma carpeta -->
<a href="../index.html">Volver a la portada</a> <!-- subo un nivel -->
```

Una ==ruta relativa== depende de la página desde la que se escribe: por eso el paso 1 es **sitúate en esa página** antes de contar niveles.

Mover un fichero rompe las rutas que apuntaban a él y las que salían de él: es **el error más común** en prácticas de FP. En una subcarpeta (`/tienda/`) las rutas de raíz fallan.

!!! question "Autoevaluación: resuelve la ruta"

    Estás en `producto/zapatillas.html` y necesitas enlazar a `img/logo.svg` y a `index.html`. ¿Qué escribes?

    ??? success "Respuesta"

        - `img/logo.svg` → **`../img/logo.svg`**: bajas de la raíz a `img/`.
        - `index.html` → **`../index.html`**: subes un nivel hasta la raíz.

## 3. Atributos del enlace

### 3.1 `download`: forzar la descarga

```html title="descarga.html"
<!-- Con valor: nombre nuevo -->
<a href="documentos/garantia-2-anios.pdf" download="Garantia_2_anios.pdf">
  Descargar la garantía (PDF, 320 KB)
</a>

<!-- Sin valor: conserva el nombre original -->
<a href="img/producto/zapatillas-1200w.jpg" download>Foto en alta resolución</a>
```

Solo descarga ficheros del **mismo origen** (o con CORS); con otro dominio el navegador **navega** en vez de guardar.

### 3.2 `target="_blank"` y `rel="noopener"`

```html title="pestana-nueva.html" hl_lines="3"
<a href="https://zensical.org/documentacion/"
   target="_blank"
   rel="noopener noreferrer">
  Ver la documentación (se abre en pestaña nueva)
</a>
```

- `target="_blank"` abre en **pestaña nueva** (por defecto, `_self`); avisa en el texto.
- `rel="noopener"` impide que la página abierta acceda a tu ventana con `window.opener` (riesgo de *tabnabbing* y *phishing*): **obligatorio en examen**.
- `rel="noreferrer"` evita además enviar la cabecera `Referer` (opcional).

Recuerda: `target="_blank"` viaja siempre con ==noopener==.

### 3.3 `title` y `hreflang`

```html title="title-hreflang.html"
<!-- title: complementa el texto visible, nunca lo repite -->
<a href="condiciones.html"
   title="Condiciones generales: plazos de entrega y devoluciones">
  Condiciones de compra
</a>

<!-- hreflang: idioma del documento enlazado (SEO multilingüe) -->
<a href="https://mitienda.es/fr/" lang="fr" hreflang="fr">Version française</a>
```

Usa `title` **con moderación**: no todos los lectores lo anuncian y no aparece en pantallas táctiles. **El texto visible** es lo único garantizado; `hreflang` declara el **idioma del documento enlazado**.

## 4. Accesibilidad de los enlaces

### 4.1 Texto descriptivo: nada de "haz clic aquí"

| Mal | Bien |
|---|---|
| `<a href="ofertas.html">Haz clic aquí</a>` | `<a href="ofertas.html">Ver todas las ofertas de septiembre</a>` |
| `<a href="nota.pdf">Más información</a>` | `<a href="nota.pdf">Descargar la nota de prensa (PDF)</a>` |

El lector de pantalla lista los enlaces **fuera de su contexto**: "haz clic aquí" repetido no dice nada; si es una imagen, su `alt` cumple esa función. Un ==enlace descriptivo== se entiende **sin leer el párrafo**.

!!! quote "WCAG 2.4.4 — Finalidad del enlace (nivel A)"

    "El propósito de cada enlace se puede determinar a partir del texto del enlace o del contexto del enlace determinado programáticamente, excepto cuando el propósito del enlace sería ambiguo para los usuarios en general."

!!! example "Qué oye el lector de pantalla"

    - "Ver todas las ofertas de septiembre — enlace"
    - "Haz clic aquí — enlace" (varias veces): **no dice nada** sin el párrafo.

### 4.2 `aria-label` cuando el texto visible no basta

```html title="enlace-icono.html"
<!-- Enlace-icono: aria-label aporta el nombre accesible -->
<a href="cesta/eliminar-42.html"
   aria-label="Eliminar el producto Zapatillas Run 300 de la cesta">
  <img src="img/papelera.svg" alt="" width="20" height="20">
</a>
```

`aria-label` **sobrescribe** el texto visible: debe coincidir con lo que **se ve en pantalla**. En la imagen interior el `alt` queda **vacío**.

### 4.3 Foco visible y *skip link*

```html title="skip-link.html"
<body>
  <!-- Primer enlace: salta la cabecera con Tab -->
  <a class="skip-link" href="#contenido">Saltar al contenido principal</a>
  <header><nav aria-label="Principal">...</nav></header>
  <main id="contenido"><h1>Zapatillas Run 300</h1></main>
</body>
```

```css title="foco.css"
a:focus-visible { outline: 3px solid #0b5fff; }       /* el foco nunca se elimina */
.skip-link { position: absolute; left: -9999px; }      /* oculto hasta el foco */
.skip-link:focus { left: 1rem; top: 1rem; background: #fff; padding: .6rem 1rem; }
```

El foco **nunca se elimina**: solo se estiliza. La estrategia completa de *skip link*, landmarks y ARIA está en [07-estructura-semantica-y-aria.md](07-estructura-semantica-y-aria.md).

!!! success "Comprueba que tus enlaces son accesibles"

    - [ ] Cada enlace se entiende **sin leer el párrafo**.
    - [ ] Ningún texto repite **"haz clic aquí"** o "más información".
    - [ ] Los enlaces-icono llevan `aria-label` **igual que lo visible**.
    - [ ] El foco se ve con `:focus-visible` y hay **skip link**.
    - [ ] `target="_blank"` va con **`rel="noopener noreferrer"`**.

## 5. Imágenes: `img`, `alt` y buenas prácticas

### 5.1 `alt`: informativa, neutra o vacía

```html title="alt.html"
<img src="img/producto/zapatillas-800w.jpg"
     alt="Zapatillas Run 300 azules vistas de perfil"
     width="800" height="600">
```

| Tipo | Cuándo ocurre | Ejemplo de `alt` |
|---|---|---|
| **Informativa** | Aporta información que no está en el texto | `alt="Zapatillas Run 300 azules vistas de perfil"` |
| **Neutra / redundante** | El pie de foto o el texto ya lo dicen | `alt="Zapatillas Run 300"` |
| **Decorativa** | No aporta nada al contenido | `alt=""` (vacío, entre comillas) |

Un ==alt== informativo se redacta como **una línea**: si contiene texto, **describe lo que dice**; si es un gráfico, **resume el mensaje** en el `figcaption`. No empieces con **"imagen de…"** ni dejes `alt` vacío en una informativa.

### 5.2 `width`, `height`, `loading` y `decoding`

```html title="rendimiento.html"
<!-- Imagen principal: carga prioritaria -->
<img src="img/producto/zapatillas-800w.jpg" alt="Zapatillas Run 300 azules"
     width="800" height="600" loading="eager"> <!-- (1)! -->

<!-- Fuera del pliegue: carga diferida -->
<img src="img/producto/zapatillas-400w.jpg" alt="Zapatillas Run 300, suela de goma"
     width="400" height="300" loading="lazy" decoding="async"> <!-- (2)! -->
```

1.  `eager`: descarga **inmediata** en la imagen principal.
2.  `lazy` + `async` en las de **fuera del pliegue**.

- `width` y `height` (píxeles) **reservan el espacio** y evitan el salto de diseño (*CLS*); CSS las sobreescribe con `max-width: 100%`.
- `loading="lazy"` retrasa la descarga hasta que la imagen se acerca al viewport: solo **fuera del pliegue**; la principal va en `eager`.
- `decoding`: `async`, `sync` o `auto` (por defecto, **decide el navegador**).

### 5.3 `figure` y `figcaption`

```html title="figure.html"
<figure>
  <img src="img/producto/zapatillas-800w.jpg"
       alt="Zapatillas Run 300 azules sobre fondo blanco"
       width="800" height="600" loading="lazy" decoding="async">
  <figcaption>Zapatillas Run 300 · Color azul marino · Foto: estudio propio</figcaption>
</figure>
```

`figcaption` va **dentro** de `<figure>`, tras la imagen; un `figure` es contenido **autónomo** que se puede mover. El lado CSS está en [../css/09-fondos-imagenes-decoracion.md](../css/09-fondos-imagenes-decoracion.md).

## 6. Imagen responsive: `srcset`, `sizes` y `picture`

### 6.1 `srcset` + `sizes`

```html title="srcset.html"
<img src="img/producto/zapatillas-800w.jpg"
     srcset="img/producto/zapatillas-400w.jpg 400w,
             img/producto/zapatillas-800w.jpg 800w,
             img/producto/zapatillas-1200w.jpg 1200w"
     sizes="(max-width: 600px) 100vw,
            (max-width: 1000px) 50vw,
            400px"
     alt="Zapatillas Run 300 azules vistas de perfil"
     width="1200" height="800" loading="lazy" decoding="async">
```

- Descriptores de ancho (`400w`, `800w`, `1200w`): tamaño real de cada fichero; el navegador elige el adecuado.
- `sizes` traduce **dónde se colocará** en píxeles: `(max-width: 600px) 100vw` = todo el ancho hasta 600 px. Sin `sizes` se asume `100vw`.
- `src` es **obligatorio como reserva**; también vale `srcset="foto.png 1x, foto@2x.png 2x"`.

Los descriptores viven en ==srcset== y las medidas de colocación en `sizes`: **no se mezclan**.

??? note "Para saber más"

    srcset admite además **descriptores de densidad**: `srcset="foto.png 1x, foto@2x.png 2x"`. En CSS el equivalente es `image-set()`, ver [../css/09-fondos-imagenes-decoracion.md](../css/09-fondos-imagenes-decoracion.md).

### 6.2 `picture` con `source`: formatos y recortes

```html title="picture.html"
<picture>
  <!-- Formatos modernos si el navegador los entiende -->
  <source srcset="img/producto/zapatillas.avif" type="image/avif">
  <source srcset="img/producto/zapatillas.webp" type="image/webp">
  <!-- Recorte vertical para móvil -->
  <source media="(max-width: 600px)"
          srcset="img/producto/zapatillas-movil.jpg" type="image/jpeg"> <!-- (1)! -->
  <!-- Fallback y portador del alt -->
  <img src="img/producto/zapatillas.jpg"
       alt="Zapatillas Run 300 azules vistas de perfil"
       width="1200" height="800" loading="lazy"> <!-- (2)! -->
</picture>
```

1.  El `media` solo manda **en móvil**; si no coincide, sigue al siguiente.
2.  El `<img>` es el **respaldo obligatorio** y el único con `alt`.

El navegador recorre los `<source>` **de arriba abajo** y usa el primero cuyo `type` y `media` coinciden; si no, carga el `<img>`.

### 6.3 Formatos modernos y soporte

| Formato | Uso | Comentario |
|---|---|---|
| `image/avif` | Foto | Máxima compresión |
| `image/webp` | Foto | Amplio soporte, admite transparencia |
| `image/jpeg` | Foto | Respaldo universal |
| `image/svg+xml` | Iconos y logotipos | Vectorial, escala sin pixelarse |

Comprueba el soporte en **`caniuse.com`** antes de quitar un respaldo; `alt`, `width` y `height` van siempre en el **`<img>` final**.

## 7. Los marcos `<iframe>`

### 7.1 Atributos esenciales

```html title="iframe.html" hl_lines="3"
<iframe
  src="https://www.openstreetmap.org/export/embed.html?bbox=-5.99,37.37,-5.97,37.39"
  title="Mapa de situación de la tienda en el centro de Sevilla"
  width="600" height="400"
  loading="lazy"
  sandbox="allow-scripts allow-same-origin allow-popups">
</iframe>
```

| Atributo | Función |
|---|---|
| `src` | Documento incrustado (propio o de otro dominio). |
| `title` | **Obligatorio** por accesibilidad: describe el contenido. |
| `sandbox` | Restringe lo que puede hacer el documento incrustado. |
| `loading="lazy"` | Retrasa la carga hasta que el marco está cerca del viewport. |

Con `sandbox` vacío se bloquea casi todo (scripts, formularios, ventanas) y los `allow-*` van **sumando** permisos; si el proveedor indica una etiqueta, cópiala. Cada permiso amplía el ==sandbox== de forma **acumulativa**.

### 7.2 Cuándo NO usar `<iframe>`

- **Contenido tuyo**: vídeo, PDF o mapa que controlas → incrusta el fichero (ver [04-multimedia.md](04-multimedia.md)); el marco añade HTTP y seguridad de más.
- **Rendimiento y seguridad**: cada `<iframe>` crea un documento completo y muchos sitios bloquean la incrustación (`X-Frame-Options`, `frame-ancestors`).
- **SEO y usabilidad**: el buscador rara vez indexa el marco y, en móvil, los marcos pequeños son incómodos.
- **Diseño**: la maquetación con marcos o tablas está retirada; se maqueta con CSS, ver [../css/10-diseno-responsivo.md](../css/10-diseno-responsivo.md).

## 8. Ejemplo práctico: galería de producto con pies de foto

```html title="galeria.html"
<main id="contenido">
  <h1>Zapatillas Run 300</h1>

  <figure>
    <img src="../img/producto/zapatillas-800w.jpg"
         srcset="../img/producto/zapatillas-400w.jpg 400w,
                 ../img/producto/zapatillas-800w.jpg 800w,
                 ../img/producto/zapatillas-1200w.jpg 1200w"
         sizes="(max-width: 600px) 100vw, (max-width: 1000px) 50vw, 600px"
         alt="Zapatillas Run 300 azules vistas de perfil sobre fondo blanco"
         width="1200" height="800" loading="eager">
    <figcaption>Vista lateral · <a href="../img/producto/zapatillas-1200w.jpg" download>Ampliar</a></figcaption>
  </figure>

  <figure>
    <picture>
      <source srcset="../img/producto/suela.avif" type="image/avif">
      <source srcset="../img/producto/suela.webp" type="image/webp">
      <img src="../img/producto/suela.jpg"
           alt="Detalle de la suela de goma con dibujo antideslizante"
           width="800" height="600" loading="lazy">
    </picture>
    <figcaption>Suela de goma con taco antideslizante (foto: estudio propio)</figcaption>
  </figure>
</main>
```

Añade además *skip link*, `<header>` y `<footer>` (**sección 4.3**). Más práctica: [09-ejercicios.md](09-ejercicios.md).

## 9. Errores frecuentes y claves del examen

### 9.1 Error común

!!! warning "Error común"

    - **`alt=""` en imagen informativa**: el lector la salta; `alt=""` solo vale para **decorativas**.
    - **`target="_blank"` sin `rel="noopener"`**: la pestaña accede a tu ventana con `window.opener`; usa `target="_blank" rel="noopener noreferrer"`.
    - **Rutas relativas mal calculadas**: contar mal los `../` al mover un fichero o calcular la ruta desde el explorador.

### 9.2 Claves para el examen

!!! tip "Claves para el examen"

    - `href` obligatorio: sin él `<a>` no es enlace; `href="#id"` salta a un id de la misma página.
    - Relativas: `archivo.html` = misma carpeta, `carpeta/…` = bajar, `../` = subir, `/ruta/` = raíz.
    - Destinos: `mailto:`, `tel:` y `#ancla`; `title` con moderación e `hreflang` para el idioma.
    - `download` solo del mismo origen; `target="_blank"` con `rel="noopener noreferrer"`.
    - Texto descriptivo y `aria-label` si el visible no basta; no elimines el foco; usa *skip link*.
    - `alt` descriptivo si informa, vacío si decora; `width`/`height` evitan el CLS; `lazy` fuera del pliegue.
    - Responsive: `srcset` + `sizes`, `<picture>` para formatos; `<iframe>` con `title`.


!!! success "Practica esta unidad"

    - Enunciados: [Ejercicios de la Unidad 3 — Enlaces y recursos](09-ejercicios.md#ej-u3) — cuatro retos (`U3.1` a `U3.4`) — del más básico al más avanzado.
    - Comprueba tu trabajo con [las soluciones de esta unidad](10-ejercicios-soluciones.md#sol-u3).

*[URL]: Uniform Resource Locator
*[srcset]: Source Set
*[CLS]: Cumulative Layout Shift
