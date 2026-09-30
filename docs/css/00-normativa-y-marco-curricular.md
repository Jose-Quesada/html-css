---
icon: lucide/book-open
title: "Unidad 00 — Normativa y marco curricular"
description: "Marco normativo estatal y autonómico del ciclo DAW en Andalucía, resultados de aprendizaje y criterios de evaluación aplicables a CSS, y papel del W3C como organismo de estandarización."
modulo: "LMH (0373) / DIW (0615)"
unidad: 0
fecha: "2026-09-06"
---

# Unidad 00 · Normativa y marco curricular

Antes de entrar en técnica, conviene situar **qué nos exige el currículo** y **dónde se define**. En un examen o en una programación didáctica, saber citar la norma correcta es parte de la competencia profesional.

!!! note "Conocimientos previos"

    - Qué es un **módulo**, un **resultado de aprendizaje (RA)** y un **criterio de evaluación (CE)**.
    - Diferenciar **BOE** (estatal) y **BOJA** (andaluz).
    - Tu módulo: **0373 (LMH)** o **0615 (DIW)**.

## 1. El marco normativo del ciclo DAW

### 1.1. Nivel estatal

| Norma | Qué establece |
|---|---|
| **Real Decreto 686/2010**, de 20 de mayo (BOE de 21/05/2010) | Establece el título de **Técnico Superior en Desarrollo de Aplicaciones Web** y fija sus **enseñanzas mínimas**: objetivos generales, módulos profesionales, duración total (2.000 h), equivalencias ECTS, espacios, equipamientos y perfil docente. |
| Real Decreto 1538/2006, de 15 de diciembre | Ordenación general de la FP del sistema educativo (marco superior al RD 686/2010). |
| Ley Orgánica 2/2006 (LOE) y LO 3/2020 (LOMLOE) | Marco legal de las enseñanzas; la LOMLOE actualiza principios (competencias digitales, inclusión, accesibilidad universal) que afectan a cómo se imparten los módulos. |

El ciclo tiene **2.000 horas** y se organiza en dos cursos. Los módulos asociados a **unidades de competencia** incluyen **0612 Desarrollo web en entorno cliente** y **0615 Diseño de interfaces WEB**; entre los «otros módulos» está **0373 Lenguajes de marcas y sistemas de gestión de información**.

!!! info "Qué son las enseñanzas mínimas"

    **Núcleo común exigible**: se amplía, nunca se recorta. Se cita primero el **RD 686/2010** y luego su desarrollo autonómico; las ==enseñanzas mínimas== se dan por supuestas en examen.

### 1.2. Nivel autonómico (Andalucía)

| Norma | Qué establece |
|---|---|
| **Orden de 16 de junio de 2011**, de la Consejería de Educación, por la que se desarrolla el currículo correspondiente al título de Técnico Superior en Desarrollo de Aplicaciones Web. Publicada en el **BOJA n.º 149, de 1 de agosto de 2011** | Desarrolla el currículo andaluz: **resultados de aprendizaje (RA)**, **criterios de evaluación (CE)**, **contenidos básicos**, **duración** y **orientaciones pedagógicas** de cada módulo. Es la **norma de referencia** para programaciones didácticas y exámenes en centros públicos y privados concertados de Andalucía. |
| Decreto 436/2008, de 2 de septiembre | Ordenación de la FP inicial en Andalucía (faculta a la Consejería a regular cada currículo mediante Orden, art. 13). |
| Ley 17/2007, de 10 de diciembre, de Educación de Andalucía | Competencia autonómica en ordenación de la FP (capítulo V, Título II). |

> **Claves para el examen**: si te piden justificar el alcance de un contenido, la cadena correcta es:
> `RD 686/2010 (mínimos estatales) → Orden de 16/06/2011 (desarrollo andaluz, BOJA 149/2011) → Programación didáctica del centro`.
> La Orden de 2011 incluye además **horas de libre configuración** (3 h) que el departamento puede dedicar a profundizar en tecnologías TIC — buen contexto para justificar contenidos de CSS avanzado no contemplados explícitamente.

### 1.3. ¿Está vigente?

La Orden de 16 de junio de 2011[^1] sigue siendo el desarrollo curricular del DAW en Andalucía (los portales oficiales de la Junta lo citan como ==normativa vigente del ciclo==). Aun así, buena práctica: **comprobar en el BOJA** (<https://www.juntadeandalucia.es/eboja.html>) si existen órdenes posteriores de modificación antes de citar la norma en un trabajo formal.

## 2. Resultados de aprendizaje aplicables a CSS

Los ==resultados de aprendizaje== dicen lo que hay que **saber hacer**; los **criterios de evaluación**, cómo se comprueba. Todo el cuerpo técnico (U01–15) responde a ese par **RA–CE**.

### 2.1. Módulo 0373 — Lenguajes de marcas y sistemas de gestión de información (128 h, 7 ECTS)

El bloque de CSS corresponde al **Resultado de aprendizaje 2**:

> **«Utiliza lenguajes de marcas para la transmisión de información a través de la Web analizando la estructura de los documentos e identificando sus elementos».**

Criterios de evaluación directamente aplicables a estos apuntes:

| CE | Texto (resumido) | Unidades de estos apuntes |
|---|---|---|
| 2.g | Se han identificado las ventajas que aporta la utilización de hojas de estilo | 01 (separación de preocupaciones, mantenibilidad) |
| 2.h | Se han aplicado hojas de estilo | 01–12 (todo el cuerpo técnico) |

**Contenidos básicos** del bloque «Utilización de lenguajes de marcas en entornos Web»: *estructura de un documento HTML, etiquetas y atributos, XHTML, versiones de HTML/XHTML, herramientas de diseño web, **hojas de estilo***.

!!! example "Del criterio al código (CE 2.h)"

    El CE **2.h** («se han aplicado hojas de estilo»): **una sola regla** cambia todas las tarjetas.

    ```css title="estilos.css" hl_lines="4"
    /* RA 2 (0615): clases de estilos */
    .tarjeta {
      padding: 1rem;
      border: 1px solid #d0d0d0;   /* (1)! */
    }
    .tarjeta--destacado {
      border-color: crimson;       /* (2)! */
    }
    ```

    1.  Regla base compartida: **consistencia** con una declaración.
    2.  Modificador que ajusta un caso sin duplicar reglas.

### 2.2. Módulo 0615 — Diseño de interfaces web (80 h, 9 ECTS)

El módulo **0615 (DIW)** es el **núcleo de la asignatura**: sus seis RA recorren casi todo el temario, de la planificación (RA 1) a accesibilidad (RA 5) y usabilidad (RA 6).

| RA | Enunciado | Criterios clave | Unidades |
|---|---|---|---|
| **RA 1** | Planifica la creación de una interfaz web valorando y aplicando especificaciones de diseño | Comunicación visual; selección de **colores y tipografías** para pantalla; alternativas de presentación de la información; **guía de estilo**; plantillas de diseño; maquetación y elementos de ordenación | 08, 09, 12 (tokens/guía de estilo), 10 |
| **RA 2** | Crea interfaces Web homogéneos definiendo y aplicando estilos | Estilos directos (en línea); **estilos globales en hojas externas**; **hojas de estilo alternativas**; redefinición de estilos; propiedades de cada elemento; **clases de estilos**; **herramientas de validación**; guía de estilo | 01, 02, 12, 14 |
| **RA 3** | Prepara archivos multimedia para la Web | Formatos de imagen/audio/vídeo; optimización | 09 (imágenes), 14 (rendimiento) |
| **RA 4** | Integra contenido multimedia en documentos Web | Tecnologías de inclusión; verificación multi-navegador | 09, 11 |
| **RA 5** | Desarrolla interfaces Web **accesibles** | W3C; **WCAG**; prioridades y puntos de verificación; niveles de adecuación; herramientas de análisis; chequeo desde distintos navegadores | 13 |
| **RA 6** | Desarrolla interfaces Web **amigables** (usabilidad) | Uso de estándares; facilidad de navegación; verificación en diferentes navegadores y tecnologías | 10, 13, 14 |

> **Nota curricular**: el RA 1 cita «marcos, tablas y capas» como elementos de ordenación. Los *frames* (==`<frameset>`==) están **obsoletos** en HTML5 y no se recomiendan; su equivalente moderno son los layouts con `display: grid`/`flexbox` (unidades 05–07). En clase conviene explicitar esta evolución: marcos → tablas → capas (divs + CSS) → grid/flex.

!!! warning "Error común"

    - Citar el **RD 686/2010** como norma andaluza: el desarrollo es la **Orden de 16/06/2011**.
    - Confundir **BOE** y **BOJA**: Estado → BOE; Consejería → BOJA.

## 3. El W3C y la estandarización de CSS

CSS no es una invención de un navegador: es un **estándar abierto** desarrollado por el **World Wide Web Consortium (W3C)** a través del **CSS Working Group (CSS WG)**.

!!! quote "Posicionamiento del W3C"

    «Making the web work — for everyone.» (la Web **para todos**.)

    — W3C, *Our mission*: <https://www.w3.org/Consortium/mission>

### 3.1. Proceso de estandarización

1. **Working Draft (WD)**: borrador de trabajo, sin garantías de compatibilidad.
2. **Candidate Recommendation (CR)**: candidatos a recomendación; los navegadores deberían implementarlo.
3. **Recommendation (REC)**: estándar estable; base para certificaciones y licitaciones.

Solo ==Recommendation== es **estándar oficial del W3C**: antes es borrador en movimiento.

Las specs se publican en <https://www.w3.org/TR/> (versiones TR) y <https://drafts.csswg.org/> (borradores vivos del CSS WG).

### 3.2. De CSS 2.1 a la modularización

- **CSS1** (REC 1996): tipografía, colores, posicionamiento básico, caja.
- **CSS2** (REC 1998) y **CSS2.1** (REC 2011): posicionamiento absoluto/fijo, floats, media types…
- **CSS3**: cambio de modelo: en lugar de un único documento gigante, se divide en **módulos independientes** (Selectors, Color, Backgrounds & Borders, Box Model, Flexbox, Grid, Media Queries, Conditional Rules, Animations, Transitions…). Cada módulo avanza por separado con su propio nivel (L1, L2, L3…).
- **CSS4 / CSS moderno**: la numeración «CSS4» no existe oficialmente; hoy se habla de los **niveles actuales de cada módulo** (p. ej., Selectors Level 4, Color Level 5, Grid Level 2).

### 3.3. Módulos más relevantes para este curso

| Módulo (spec) | Contenido | Estado orientativo |
|---|---|---|
| Selectors L4 | `:has()`, `:is()`, `:where()`, `:focus-visible`, selectores estructurales nuevos | WD (implementado en todos los navegadores principales) |
| Color L5 | `oklch()`, `color-mix()`, `light-dark()` | WD (implementado) |
| Box Alignment L3 | `place-items`, `place-content`, alineación moderna | WD (implementado) |
| Flexbox L1 | Modelo de flexión | REC (implementado) |
| Grid L2 | Cuadrícula + **subgrid** | CRD (implementado) |
| Conditional Rules L5 | `@media`, `@supports`, **container queries** | WD (implementado) |
| Nesting L1 | Anidación nativa | WD (implementado) |
| Cascade L5/L6 | `!important`, orígenes, **`@layer`**, `@scope` | WD (implementado) |
| Animations L2 | `animation-timeline` (scroll-driven) | WD (parcial) |
| View Transitions L1 | Transiciones entre vistas | CRD (implementado) |
| Values & Units L4 | `clamp()`, `min()`, `max()`, unidades viewport dinámicas | WD (implementado) |

> **Claves para el examen**: «CSS3» es un término histórico/marketing; lo correcto es hablar de **módulos del lenguaje CSS y sus niveles**. Un examinador valora que sepas que cada característica pertenece a una spec concreta.

### 3.4. Otros organismos y referencias técnicas

- **WHATWG**: mantiene la especificación de HTML (el **Living Standard**). HTML y CSS son complementarios pero specs distintas.
- **WCAG** (Web Content Accessibility Guidelines, W3C): no es una spec de CSS, pero define requisitos de accesibilidad que CSS debe cumplir (contraste, foco, movimiento…). Base del RA 5 del módulo 0615.
- **MDN Web Docs**: documentación de referencia mantenida por Mozilla con datos de compatibilidad (browser-compat-data). Es la fuente didáctica principal de estos apuntes.

!!! info "Cómo se cita un estándar"

    - **Organismo**: W3C (CSS, WCAG) o WHATWG (HTML).
    - **Spec y fase**: p. ej. *Selectors Level 4*, fase **REC**.
    - **Fecha**: obligatoria en licitaciones.

## 4. Mapa de contenidos: de la norma a las unidades

El ==mapa de contenidos== vincula cada **criterio** (p. ej. ==`CE 2.h`==) con la unidad donde se practica.

```text title="mapa-de-contenidos.txt" hl_lines="3 4"
Orden 16/06/2011 (BOJA)
├── Módulo 0373 (LMH)
│   └── RA 2 (g, h): hojas de estilo
│        ├── Ventajas y aplicación básica ............ U01, U02
│        └── Herramientas de validación .............. U14
└── Módulo 0615 (DIW)
    ├── RA 1: planificación de interfaz
    │    ├── Color y tipografía ....................... U08
    │    ├── Guía de estilo y plantillas .............. U12
    │    └── Maquetación y ordenación ................. U03–U07
    ├── RA 2: uso de estilos
    │    ├── En línea / externo / alternativo ......... U01
    │    ├── Clases y redefinición .................... U01, U02
    │    └── Validación ............................... U14
    ├── RA 3/4: multimedia
    │    └── Imágenes, formatos, integración .......... U09
    ├── RA 5: accesibilidad
    │    └── WCAG aplicada a CSS ...................... U13
    └── RA 6: usabilidad
         ├── Responsivo y navegación .................. U10
         └── Rendimiento y estándares ................. U14
```

!!! question "Cadena normativa"

    ¿Qué normas citas, y en qué orden, para justificar *container queries* en tu programación?

    ??? success "Respuesta"

        **RD 686/2010** → **Orden de 16/06/2011** (BOJA 149, con **3 h de libre configuración**) → **programación didáctica** del centro.

## 5. Resumen ejecutivo

1. El DAW en Andalucía se rige por el **RD 686/2010** (estatal) y la **Orden de 16 de junio de 2011** (BOJA 149/2011).
2. CSS aparece explícitamente en el **RA 2 del 0373** y de forma extensa en los **RA 1, 2, 5 y 6 del 0615**.
3. CSS es un estándar **W3C/CSS WG** organizado en **módulos con niveles**, no «CSS3 vs CSS4».
4. La accesibilidad (WCAG) y la usabilidad son **requisitos curriculares explícitos**, no adornos: dedican aquí una unidad completa (U13).

!!! success "Checklist de la unidad"

    - [ ] Cito **RD 686/2010** y **Orden de 16/06/2011 (BOJA 149)** con fechas.
    - [ ] Señalo el **RA** y el **CE** de cada contenido de CSS.
    - [ ] Explico qué hace el **W3C** y por qué «CSS3» no es una spec.
    - [ ] Distingo **BOE** de **BOJA**.

!!! tip "Claves para el examen"

    - **RD 686/2010 → Orden de 16/06/2011 (BOJA 149) → programación didáctica**.
    - CSS en el currículo: **RA 2 del 0373** y **RA 1, 2, 5 y 6 del 0615**.
    - «CSS3» es marketing: se citan **módulos con nivel y fase** (WD, CR, REC).
    - **W3C** estandariza CSS y WCAG; **WHATWG** mantiene HTML.
    - **3 h de libre configuración** = CSS avanzado no citado literalmente.
    - Toda cita lleva **número, fecha y diario** correctos.

[^1]: BOJA n.º 149, de 1 de agosto de 2011 (desarrollo del currículo DAW en Andalucía).

*[W3C]: World Wide Web Consortium
*[RA]: Resultado de aprendizaje
*[CE]: Criterio de evaluación
