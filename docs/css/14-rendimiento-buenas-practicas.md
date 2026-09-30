---
icon: lucide/gauge
title: "Unidad 14 — Rendimiento y buenas prácticas"
description: "Critical rendering path, CSS render-blocking, tamaño y purga, containment, content-visibility, will-change, carga de fuentes, caché, Core Web Vitals, DevTools y calidad del código CSS."
modulo: "LMH (0373) / DIW (0615)"
unidad: 14
fecha: "2026-09-06"
---

# Unidad 14 · Rendimiento y buenas prácticas

El CSS afecta al rendimiento en tres frentes: **bloqueo del render** (aparece tarde), **tamaño de transferencia** (descarga lenta) y **coste de ejecución** (layout/paint/composite lentos). Esta unidad cubre los tres con técnicas medibles.

!!! note "Conocimientos previos"

    - DOM, CSSOM y árbol de render (HTML).
    - Capas de composición y coste de repintado (unidad 11).
    - `@layer`, tokens y estructura de archivos (unidad 12).

## 1. Critical Rendering Path (CRP)

Cómo el navegador pinta la primera pantalla (==CRP==):

```text title="crp.txt"
HTML → DOM          CSS → CSSOM
              \     /
                Render Tree
                   ↓
                Layout (geometría)
                   ↓
                Paint (píxeles por capa)
                   ↓
              Composite (composición GPU)
```

Hechos clave:

- El navegador **no pinta** hasta tener DOM + CSSOM (salvo streaming parcial con `@import`/chunking moderno).
- Un CSS lento o grande **retarda el First Paint**.
- Cambios de estilo que alteran geometría fuerzan **Layout → Paint → Composite** (caro); cambios solo de pintura fuerzan **Paint**; cambios de compositor (`transform`, `opacity`) solo **Composite** (barato).

## 2. CSS render-blocking: detectar y mitigar

### 2.1. El problema

`<link rel="stylesheet">` en `<head>` bloquea el render hasta descargarse y parsearse. En redes lentas, segundos de pantalla blanca: es el ==render-blocking== por antonomasia.

!!! info "Qué significa bloquear"

    - El navegador **no pinta una sola línea** hasta bajar y parsear el CSS.
    - No es «pantalla blanca un rato»: es **espera acumulada** en cada primera visita.
    - Mídelo con **throttling** (Fast 3G) en la pestaña **Network**.

### 2.2. Estrategias (de más a menos recomendada)

1. **Reducir**: minificar, purgar lo no usado, dividir por ruta (solo cargar el CSS de la página actual en SPAs). Es la solución raíz.
2. **Preload + swap** (CSS no crítico):

```html title="index.html" hl_lines="3 4"
<head>
  <style>/* CSS CRÍTICO inline: solo lo de la primera pantalla */</style>
  <link rel="preload" href="/css/styles.css" as="style"
        onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="/css/styles.css"></noscript>
</head>
```

   El preload descarga en paralelo sin bloquear; se convierte en stylesheet al terminar. (Los frameworks lo hacen por ti: Vite, Next.js…)
3. **`media="print"` + JS**: truco antiguo, hoy sustituido por el anterior.
4. **Dividir hojas por prioridad**: `base.css` (crítico, pequeño) + `components.css` (deferred).

### 2.3. CSS crítico

Conjunto mínimo que estiliza la **first viewport**: reset básico, tipografía, header, hero. Generadores: `critical` (puppeteer), plugins de build, o a mano en proyectos pequeños. Regla: si el CSS crítico supera ~14 KB minificado, algo sobra.

!!! example "Presupuesto de CSS crítico"

    ```css title="critico.css"
    *, *::before, *::after { box-sizing: border-box; margin: 0; }
    body { font: 16px/1.5 system-ui; }
    .hero { min-height: 60svh; padding: 2rem; }
    ```

    **< 14 KB** minificado: reset, tipografía base y todo lo que se ve sin scrollear.

## 3. Tamaño: minificación, purga y organización

| Técnica | Efecto típico | Herramientas |
|---|---|---|
| Minificación | −20–40% del peso | cssnano, Lightning CSS, esbuild. |
| Purga de selectores muertos | −30–80% en legacy | PurgeCSS (analiza tu HTML/JS). |
| Dividir por feature/ruta | Menos transfer por página | Build modular (Vite code-splitting de CSS en SPAs). |
| Evitar duplicados (mismas reglas en varias hojas) | Mantenimiento + bytes | Linter + revisión. |
| Comprimir en red (Brotli) | −15–25% adicional | Servidor (`Content-Encoding: br`). |

Métricas objetivo orientativas: CSS total por página < 100 KB (bruto), < 30 KB tras compresión; una sola petición de CSS principal.

## 4. Coste de ejecución: qué mover es barato

### 4.1. Jerarquía de coste (repaso de U11)

| Fase | Propiedades típicas | Coste |
|---|---|---|
| Composite | `transform`, `opacity`, `filter` | Muy bajo (GPU). |
| Paint | `background`, `box-shadow`, `border-color`… | Medio. |
| Layout | `top/left/width/height/margin/padding/display`… | Alto (recalcula árbol). |

### 4.2. `will-change`

El ==will-change== promociona el elemento a capa de composición **antes** del cambio:

```css title="will-change.css" hl_lines="4"
/* Bien: justo antes de animar */
.carrusel:hover .slide { will-change: transform; }   /* (1)! */
/* Mal: en todo el sitio */
* { will-change: transform; }  /* RAM explosiva (2)! */
```

1.  Se aplica **justo antes** de necesitarla (hover, clase temporal).
2.  `*` crea una capa por elemento: **memoria** y capas que nadie recicla.

Retirar cuando termine (`will-change: auto`). Alternativa: JS que lo aplica temporalmente.

### 4.3. Containment (`contain`)

Le dice al navegador «esto es independiente» para acotar layout/paint:

```css title="contain.css"
.lista .item { contain: content; }      /* layout + paint (1)! */
.widget     { contain: strict; }        /* + size (cuidado) */
```

1.  `content` acota **sin** fijar tamaño: es el punto de partida seguro.

Usar en listas largas, widgets aislados. Verificar que nada dependa de medidas externas.

### 4.4. `content-visibility: auto`

Salta el render de contenido fuera de viewport (accesibilidad preservada gracias a ==`contain-intrinsic-size`==):

```css title="seccion.css" hl_lines="2 3"
.seccion-larga {
  content-visibility: auto;
  contain-intrinsic-size: auto 1200px;  /* altura estimada para no saltar el scroll (1)! */
}
```

1.  Sin esa **altura de reserva** el scrollbar salta y aparecen huecos al hacer scroll.

Ganancias enormes en páginas largas (blogs, docs). Soporte: Chrome 85+, Firefox 125+, Safari 18+.

### 4.5. Animaciones y scroll

- Anima `transform`/`opacity` (U11).
- Scroll handlers: `requestAnimationFrame` o mejor, **scroll-driven animations** (CSS puro, U11).
- `backdrop-filter` en muchos elementos = FPS bajos: limita su uso.
- Evita `position: fixed` con sombras grandes que repintan toda la página al scrollear.

!!! warning "Error común"

    - Dejar ==`will-change`== «por si acaso» en `*` o en toda una sección: **RAM** y capas huérfanas.
    - Aplicarlo sin **retirarlo** al terminar el cambio.
    - `contain: strict` donde el componente **lee medidas externas**: saltos y errores raros.

## 5. Fuentes: el otro cuello de botella visual

1. **WOFF2** + subconjuntos (`unicode-range`).
2. ==`font-display: swap`== (fallback visible mientras carga).
3. **Preload** de la fuente crítica:

```html title="head.html"
<link rel="preload" href="/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
```

4. Limitar pesos/familias (una variable vale más que 4 estáticas).
5. Self-hosting (control RGPD + rendimiento) frente a Google Fonts (extra hop + privacidad).
6. Mide el **FOUT** (flash of unstyled text): debe ser breve e imperceptible.

## 6. Caché y entrega

La pieza clave es el ==fingerprinting== del nombre de archivo:

| Mecanismo | Aplicación a CSS |
|---|---|
| `Cache-Control: public, max-age=31536000, immutable` | Para CSS con **fingerprint** en el nombre (`styles.a1b2c3.css`). |
| Fingerprinting/hashing | Cada cambio genera nuevo URL → caché eterna segura. Lo hace el build (Vite/Webpack). |
| Brotli/Gzip | `Content-Encoding: br` (mejor que gzip ~20%). |
| HTTP/2-3 | Multiplexación: muchas peticiones pequeñas ya no penalizan tanto (aún así, 1 CSS > 5). |
| CDN | Latencia reducida geográficamente. |
| Service Worker | Offline + updates controladas (PWA). |

## 7. Core Web Vitals y el papel del CSS

| Métrica | Qué mide | Impacto CSS |
|---|---|---|
| **LCP** (Largest Contentful Paint) | Tiempo hasta el mayor elemento de la first view | CSS blocking, fuentes, imagen hero (srcset, fetchpriority). |
| **CLS** (Cumulative Layout Shift) | Estabilidad visual | `aspect-ratio`/dimensiones en media, `font-display`, evitar insertar banners empujando contenido, `content-visibility` bien configurado. |
| **INP** (Interaction to Next Paint) | Responsividad a inputs | Main thread libre: menos trabajo de estilo/layout por frame; evita transiciones costosas en hover de elementos grandes. |

Objetivos «bueno»: LCP < 2.5 s, CLS < 0.1, INP < 200 ms[^1].

!!! info "Los tres umbrales, de memoria"

    - **LCP < 2.5 s** · **CLS < 0.1** · **INP < 200 ms** (percentil 75).
    - El CSS pesa sobre todo en ==LCP== (bloqueo) y en **CLS** (fuentes y media sin dimensiones).
    - Laboratorio (Lighthouse) y campo (CrUX) **no son intercambiables**.

!!! question "Diagnóstico CWV"

    Una landing carga su titular con `font-display: block` de 3 s y las imágenes sin dimensiones. ¿Qué métricas se disparan?

    ??? success "Respuesta"

        Sube el **LCP** (la fuente bloquea el mayor texto) y el **CLS** (las imágenes sin `width/height` empujan el contenido). Corrige con `swap` + preload y `aspect-ratio`.

## 8. DevTools: flujo de diagnóstico

1. **Network**: ¿cuánto pesa el CSS? ¿Cuándo termina? (throttle a Fast 3G/Slow 4G).
2. **Performance** (grabar interacción): busca *Layout* largos, *Recalculate Style* repetido, long tasks.
3. **Rendering**:
   - «Paint flashing»: ve qué se repinta.
   - «Layer borders»: capas de composición.
   - «Layout shifting» + badge de CLS.
4. **Elements → Styles**: especificidad y orígenes de cada regla (depurar cascada).
5. **Coverage** (pestaña Coverage del panel Sources): porcentaje de CSS **usado** en la página → guía la purga.

## 9. Calidad del código CSS

### 9.1. Linting y formato

- **stylelint**: reglas (orden de propiedades, unidades permitidas, bans de `!important`, id duplicados…), formateo con Prettier.
- CI: fallar el build con errores de lint → deuda cero.

### 9.2. Convenciones de equipo (para la guía de estilo)

1. Una propiedad por línea; bloques separados por salto.
2. Orden lógico dentro de la regla: posicionamiento → caja → tipografía → visual → misc (o seguir orden de stylelint-order).
3. Nombres kebab-case; BEM o convención acordada (U12).
4. Sin `!important` salvo justificación documentada.
5. Tokens para cualquier valor repetido 3+ veces.
6. Comentarios solo para el «por qué», nunca el «qué».
7. Versionar con git; commits atómicos por componente.

### 9.3. Testing de estilos

- **Visual regression**: screenshots comparados entre builds (Chromatic, Argos, BackstopJS). Detecta regresiones visuales en CI.
- **Unit testing de utilidades CSS**: raro pero posible (p. ej., probar funciones de cálculo con Playwright midiendo computed styles).
- **Contraste automatizado**: plugin de axe/Stark en CI sobre componentes.

### 9.4. Seguridad (matiz)

- CSS puede leer poco, pero `url()` a dominios externos filtra datos (exfiltration vía timing/DNS en casos extremos): no cargar recursos de origen no confiable.
- CSP no cubre CSS directamente, pero `style-src` restringe estilos inline dinámicos.
- Sanear cualquier CSS generado desde input de usuario (inyección de estilos).

## 10. Checklist final de rendimiento (por entregar)

!!! success "Checklist antes de entregar"

    - [ ] 1 hoja CSS principal (+ deferred si procede), minificada, Brotli.
    - [ ] CSS crítico inline para first paint; resto preloaded.
    - [ ] Sin selectores muertos (Coverage > 80% usado).
    - [ ] Imágenes con dimensiones y `srcset`; fuentes WOFF2 preloaded con `swap`.
    - [ ] Animaciones solo `transform`/`opacity`; `will-change` puntual.
    - [ ] `contain`/`content-visibility` en secciones largas.
    - [ ] Lighthouse mobile: Performance ≥ 90, CLS < 0.1.
    - [ ] Cache inmutable con fingerprinting.

## 11. Autoevaluación rápida

1. Explica el CRP y señala en qué fase impacta un CSS de 500 KB.
2. Diferencia entre `contain: paint` y `content-visibility: auto`.
3. ¿Por qué `will-change` en todos los elementos es peor que no usarlo?
4. Diseña la estrategia de CSS (crítico + deferred) para una landing con hero pesado.
5. ¿Qué métrica CWV empeora si cargas una fuente con `font-display: block` de 3 s?
6. ¿Qué te dice la pestaña Coverage y cómo actúas con ese dato?

!!! tip "Claves para el examen"

    - **CRP**: nada se pinta sin DOM + CSSOM; el CSS de `<head>` **bloquea**.
    - Crítico inline (**< 14 KB**) + el resto con ==preload== y swap.
    - Coste por frame: **Composite < Paint < Layout** → anima `transform`/`opacity`.
    - ==`will-change`== puntual y **retirado**; `content-visibility` con altura de reserva.
    - Fuentes: **WOFF2**, `swap` y preload; mide el FOUT.
    - CWV: **LCP < 2.5 s · CLS < 0.1 · INP < 200 ms**.
    - **Coverage > 80 %** usado antes de publicar.

[^1]: Umbrales recomendados por Google para los Core Web Vitals (web.dev).

*[CRP]: Critical Rendering Path
*[CWV]: Core Web Vitals
*[CLS]: Cumulative Layout Shift
