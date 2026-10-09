---
icon: lucide/laptop
title: "HTML 11 - Prácticas globales"
description: "Prácticas de desarrollo integral para consolidar los conocimientos de HTML5."
modulo: "LMH (0373) / DIW (0615) / DI (0488)"
unidad: 11
fecha: "2026-10-07"
---

# HTML 11 — Prácticas globales

Este documento reúne prácticas extensas diseñadas para evaluar de forma conjunta múltiples unidades del temario. Suponen un reto mayor que los ejercicios individuales y están pensadas para resolverse como proyectos de casa.

## Práctica Global 1: Maquetación Semántica de un Blog Técnico

!!! info "Objetivo de la práctica"
    Esta práctica global evalúa de forma conjunta los contenidos de la **Unidad 1** (esqueleto, metadatos, optimización) y la **Unidad 2** (jerarquía, semántica de texto, listas y citas). Partirás de cero y tu misión es crear un documento HTML5 perfecto a nivel de accesibilidad, SEO y semántica. 
    **Importante:** Queda estrictamente prohibido el uso de CSS o de etiquetas de presentación visual. Todo el significado debe recaer de manera nativa en las etiquetas HTML.

### 1. Escenario y Tarea

Has sido contratado para crear la plantilla del artículo principal del nuevo blog técnico del IES para el ciclo de Desarrollo de Aplicaciones Multiplataforma. El equipo de redacción te ha entregado un archivo de texto plano con el borrador del artículo. 

Debes construir el archivo `articulo.html` desde cero, aplicando todas las reglas de HTML5 moderno y superando la validación estricta del W3C.

### 2. Requisitos de Cabecera y Metadatos (Unidad 1)

El archivo debe contar con un esqueleto inmaculado que le encantaría a cualquier motor de búsqueda:

- **Raíz y codificación:** DOCTYPE nativo, idioma español en la raíz y charset UTF-8 en la primera línea de la cabecera.
- **Rendimiento:** Precarga de una fuente principal (`/fonts/inter.woff2`) mediante un *Resource Hint* (`preload` como `font`).
- **Open Graph:** Añade metadatos básicos de Open Graph para redes sociales (`og:title`, `og:type` declarado como `article`, y `og:image`).
- **SEO Semántico:** Incluye un bloque `<script type="application/ld+json">` (*Schema.org*) declarando un objeto de tipo `"Article"`, con su titular y el nombre del autor.
- **Sindicación:** Añade un enlace de autodescubrimiento para el feed RSS del blog (`/blog/feed.xml`).
- Asegúrate de que el documento es *mobile-friendly* incluyendo la etiqueta `viewport` obligatoria.

### 3. Requisitos de Estructura y Semántica (Unidad 2)

Aplica el marcado adecuado al contenido proporcionado por redacción. Debes cumplir las siguientes normas:

- **Jerarquía:** Usa un único `<h1>` en todo el documento para el titular. Las subsecciones deben estar en `<h2>` y `<h3>` sin dar saltos lógicos.
- **Fechas:** La fecha de publicación debe estar legible para máquinas con `<time>` y el atributo en formato ISO (`datetime`).
- **Términos y Acrónimos:** Usa `<abbr>` y `<dfn>` para explicar siglas técnicas (como API y UI).
- **Listas y Anidamientos:** Construye los pasos del tutorial con listas ordenadas. El paso 3 contiene una sub-lista desordenada: asegúrate de que la anidación ocurre de manera estrictamente correcta **dentro del `<li>`** padre.
- **Citas:** Aplica el marcado complejo de citas de bloque (`<blockquote>` con un `<p>` dentro), citas literales (`<q>`) y atribución al autor (`<cite>`).
- **Código y Teclado:** Señaliza semánticamente los comandos de terminal (`<code>`) y los atajos de teclado (`<kbd>`).
- **Historial de Cambios:** En la penúltima sección, marca lo que ha quedado obsoleto como eliminado (`<del>`) y la nueva tecnología como insertada (`<ins>`).
- **Escapado de caracteres:** Escapa correctamente cualquier etiqueta que deba mostrarse en pantalla literalmente, así como los espacios fijos u otros caracteres conflictivos (entidades HTML).
- **Separación visual e información de contacto:** Usa un salto de temática (`<hr>`) para separar el artículo de los datos del autor. Usa `<address>` para la información de contacto.

---

### 4. Borrador de Redacción (Texto plano a maquetar)

*(Convierte el siguiente texto plano a HTML5 semántico)*

```text
[TITULAR] Introducción a la Arquitectura Limpia en Aplicaciones Multiplataforma
[FECHA] Publicado el 15 de octubre de 2026.

[SECCIÓN] ¿Qué es la Arquitectura Limpia?
El concepto central es separar el código por responsabilidades. Cuando diseñamos una API (Interfaz de Programación de Aplicaciones), su lógica debe ser independiente de la UI (Interfaz de Usuario). Esto evita que un cambio en la base de datos rompa el aspecto visual.

[SUB-SECCIÓN] Principios Fundamentales
Como dijo Robert C. Martin en su libro "Clean Architecture": La arquitectura es sobre la intención, no sobre el framework. Siguiendo esta idea, nuestro código debe gritar su propósito.

[SECCIÓN] Guía de Configuración Inicial
Para empezar tu primer proyecto, sigue estos pasos:
1. Instala el entorno. Asegúrate de tener instalado el CLI de tu lenguaje.
2. Clona el repositorio base. Ejecuta en tu terminal el comando: git clone url-del-repo. Si el sistema se bloquea, pulsa Ctrl + C para cancelar.
3. Instala las dependencias. Esto descargará e instalará paquetes fundamentales como:
  - Motor de base de datos
  - Librería de testing
  - Linter de código
4. Ejecuta el servidor.

[SECCIÓN] Cambios de versión
El año pasado usábamos el archivo config.xml para esto, pero ahora ha sido deprecado y lo hemos sustituido por settings.json. Fíjate en que si intentas escribir la etiqueta <config>, el compilador te lanzará un error.

[SECCIÓN] Contacto del autor
Autora: María López, Ingeniera de Software.
Email: maria@iesf3.es
Edificio Tecnológico, Aula 12.
```

---

### 5. Criterios de Evaluación y Entrega

!!! success "Lista de comprobación (Rúbrica de autoevaluación)"
    - [ ] **Validación:** El código obtiene 0 errores en el [W3C Validator](https://validator.w3.org/).
    - [ ] **Esqueleto impecable:** Todas las etiquetas vacías carecen de la barra final heredada de XHTML (`/>`).
    - [ ] **Entidades:** La etiqueta `<config>` se muestra correctamente en el texto gracias al uso de `&lt;` y `&gt;`.
    - [ ] **Semántica en línea:** Se ha usado correctamente `<abbr>`, `<dfn>`, `<code>`, `<kbd>`, `<del>` e `<ins>`.
    - [ ] **Citas:** Se utiliza `<blockquote>` con atributo `cite`, anidando un `<p>` y una `<q>` para las comillas generadas por el navegador, rematado con `<cite>` para el nombre del autor.
    - [ ] **Listas robustas:** La lista desordenada (motor, librería, linter) está anidada **dentro** del `<li>` del tercer paso, y no de forma flotante.

## Práctica Global 2: Portafolio Profesional Multimedia

!!! info "Objetivo de la práctica"
    Esta práctica integra las unidades **1, 2 y 3**. Deberás crear la estructura de un portafolio profesional construyendo enlaces seguros, implementando recursos multimedia optimizados (imágenes responsivas y mapas incrustados) y manteniendo la excelencia semántica de las unidades anteriores.

### 1. Escenario y Tarea

Vas a desarrollar la página `sobre-mi.html`, la carta de presentación de tu portafolio como desarrollador/a. El cliente final es exigente con el rendimiento web y requiere que todos los recursos externos se manejen con seguridad y eficiencia.

### 2. Requisitos de Cabecera (Unidad 1)
- Esqueleto HTML5 validado con idioma y `charset` moderno.
- Título atractivo y un `<meta name="description">` detallando tu perfil (vital para SEO).
- Configuración obligatoria para dispositivos móviles (`viewport`).

### 3. Texto, Jerarquía e Identificadores (Unidad 2)
- El titular principal debe ser tu nombre.
- Utiliza etiquetas semánticas (`<abbr>`, `<time>`, `<strong>`, `<cite>`, `<q>`, `<blockquote>`) según corresponda en el texto base.
- Prepara los contenedores (o encabezados) con los atributos `id` necesarios para que los enlaces internos funcionen (por ejemplo, `id="contacto"`).

### 4. Enlaces, Multimedia e Incrustaciones (Unidad 3)
- **Navegación Interna:** Crea un pequeño menú al inicio con enlaces que salten internamente a las secciones "Experiencia" y "Contacto" usando anclas (hashes). Envuélvelo en una etiqueta semántica de navegación.
- **Enlaces Externos Seguros:** Incluye un enlace a tu GitHub o LinkedIn. Este debe abrirse en una pestaña nueva, pero es obligatorio aplicar la política de seguridad correspondiente (`rel`) para evitar vulnerabilidades de tipo *tabnabbing*.
- **Enlaces de Acción:** El email de contacto debe ser funcional y abrir directamente el cliente de correo del usuario al ser pulsado.
- **Imagen Responsiva (Rendimiento):** Muestra una fotografía de tus proyectos. Debes usar el atributo `srcset` y `sizes` para ofrecer al menos dos resoluciones distintas (por ejemplo, 400w y 800w), además de `width`, `height`, `loading="lazy"` y un `alt` perfecto. Envuelve la imagen en la estructura semántica que permita añadirle una leyenda visible (pie de foto).
- **Mapa Incrustado:** Utiliza un `<iframe>` para incrustar un mapa de Google Maps (ficticio o real) de tu zona de trabajo. Asegúrate de añadir el atributo `title` para accesibilidad y de diferir su carga visual (`loading="lazy"`).

---

### 5. Borrador de Redacción (Texto plano a maquetar)

```text
[MENÚ DE NAVEGACIÓN]
Ir a Experiencia | Ir a Contacto

[TITULAR] Portfolio de [Tu Nombre]
Desarrollador web especializado en accesibilidad.

[SECCIÓN] Experiencia
He trabajado creando interfaces de usuario (UI) desde el año 2024. 
Mi lema de trabajo lo saqué del W3C: "El poder de la Web está en su universalidad".

[AQUÍ VA LA IMAGEN RESPONSIVA] 
(Usa 'proyecto-movil.jpg' como versión de 400px y 'proyecto.jpg' como versión de 800px. La leyenda visible de la foto debe ser: "Mi entorno de desarrollo").

[SECCIÓN] Contacto
Puedes ver mi código fuente en mi perfil de GitHub [haz que esto sea un enlace externo en nueva pestaña].
Escríbeme a: correo@ejemplo.com [haz que esto sea un enlace de envío de correo].
Trabajo desde la zona tecnológica de Málaga.

[AQUÍ VA EL MAPA INCRUSTADO CON IFRAME]
```

## Práctica Global 3: Plataforma de Videoeducación (EdTech)

!!! info "Objetivo de la práctica"
    Esta práctica eleva la dificultad al incorporar la **Unidad 4 (Multimedia)** junto con todo lo aprendido en las unidades 1, 2 y 3. Crearás la interfaz de una lección de un curso online, asegurando que el contenido audiovisual sea plenamente accesible y que se ofrezcan alternativas de formato para distintos navegadores y dispositivos.

### 1. Escenario y Tarea

Trabajas en una startup de educación online (EdTech). Te han encargado maquetar la vista de una "Lección de Curso". Esta página debe contener el reproductor de vídeo principal con subtítulos, una alternativa en audio (podcast de la lección), una transcripción semántica, y material complementario enlazado.

### 2. Requisitos Técnicos

- **Cabecera y Metadatos (U1):** Configuración base, meta descripción y recursos precargados.
- **Estructura y Texto (U2):** Uso estricto de `<header>`, `<main>`, `<section>`, y un `<h1>` único. Emplea correctamente `<abbr>`, `<strong>`, y listas descriptivas (`<dl>`, `<dt>`, `<dd>`) para el glosario de términos del vídeo.
- **Imágenes y Enlaces (U3):** Las miniaturas de los "Cursos Relacionados" deben usar `<picture>` para cargar versiones en formato moderno (AVIF/WebP) con un *fallback* a JPG.
- **Multimedia (U4):**
    - **Vídeo principal:** Debe usar la etiqueta `<video>` con controles nativos (`controls`), una imagen de portada (`poster`) y precarga automática de metadatos (`preload="metadata"`).
    - **Múltiples fuentes:** Proveer al menos dos formatos de vídeo (`.mp4` y `.webm`) mediante la etiqueta `<source>`.
    - **Accesibilidad VTT:** Incluir subtítulos en español y descripciones de audio para personas con discapacidad visual, usando al menos dos etiquetas `<track>`.
    - **Reproductor de Audio:** Un reproductor secundario `<audio>` para quienes prefieran escuchar la lección en formato podcast.

---

### 3. Borrador de Redacción y Recursos

```text
[TITULAR DE LA PÁGINA] Lección 4: Introducción a la Lógica de Programación

[VÍDEO PRINCIPAL]
Archivo 1: leccion4.webm
Archivo 2: leccion4.mp4
Portada: poster-leccion4.jpg
Subtítulos: subs-es.vtt (Español, por defecto)
Descripciones: desc-es.vtt

[AUDIO ALTERNATIVO]
"Escucha esta lección en formato podcast:"
Archivo: podcast-leccion4.mp3

[SECCIÓN] Glosario de la lección
(Usa una lista de descripción para estos dos términos)
Algoritmo: Conjunto ordenado de operaciones sistemáticas que permite hacer un cálculo.
Bucle: Secuencia que ejecuta repetidas veces un trozo de código.

[SECCIÓN] Cursos Recomendados
Imagen: usa la etiqueta picture. Formato preferido 'curso-avanzado.avif', alternativo 'curso-avanzado.jpg'.
Enlace: "Ver curso avanzado de JavaScript" (Debe abrir en pestaña nueva de forma segura).
```

---

## Práctica Global 4: Panel de Control Financiero (Dashboard)

!!! info "Objetivo de la práctica"
    Esta práctica es de **alta dificultad**. Evalúa las unidades 1, 2, 3, 4 y añade la **Unidad 5 (Tablas de Datos Complejas)**. Construirás un informe anual donde el protagonista es una tabla de datos financieros que requiere agrupaciones avanzadas y accesibilidad perfecta para lectores de pantalla.

### 1. Escenario y Tarea

El departamento de contabilidad necesita maquetar en HTML el informe de resultados del último trimestre. Tienen una tabla con agrupaciones de columnas y filas. Si no estructuras bien la tabla, un usuario invidente escuchará una sopa de números incomprensible.

### 2. Requisitos Técnicos

- **Acumulativo (U1-U4):** Todo el esqueleto base, un logo responsivo, un vídeo corporativo breve sin controles que se reproduzca en bucle (modo presentación/background), y semántica perfecta.
- **Tablas Avanzadas (U5):**
    - Debes incluir un título descriptivo intrínseco usando `<caption>`.
    - Separar semánticamente la cabecera (`<thead>`), el cuerpo (`<tbody>`) y el pie (`<tfoot>`) de la tabla.
    - Usar atributos de expansión (`colspan` y `rowspan`) para agrupar categorías.
    - **Crítico para A11y:** Definir explícitamente el alcance de cada encabezado de fila o columna usando el atributo `scope="row"` o `scope="col"`.

---

### 3. Estructura de Datos (Borrador)

```text
[TITULAR] Informe Financiero Q3

[VÍDEO DE FONDO CORPORATIVO]
Archivo: bg-finance.mp4. (Debe reproducirse solo, en silencio, en bucle y sin controles).

[SECCIÓN TABLA] "Resumen de Ingresos y Gastos"
Estructura deseada de la tabla:
Cabecera Principal (2 filas):
- Fila 1: Una celda vacía (esquina), seguida de "Ingresos" (que ocupa 2 columnas), seguida de "Gastos" (ocupa 2 columnas).
- Fila 2: "Norteamérica", "Europa", "Norteamérica", "Europa". (Debajo de sus respectivos grupos).

Cuerpo (2 filas):
- Fila 1: Categoría "Software" (encabezado de fila). Valores: $50k, $40k, $10k, $12k.
- Fila 2: Categoría "Hardware" (encabezado de fila). Valores: $30k, $20k, $15k, $10k.

Pie de tabla:
- Fila 1: "Totales" (encabezado de fila), Valores: $80k, $60k, $25k, $22k.
```

---

## Práctica Global 5: Sistema de Reservas Complex (Hotel)

!!! info "Objetivo de la práctica"
    El reto final para el bloque de HTML. Unifica las **Unidades 1 a 6**. Te enfrentarás a un formulario de reservas extenso y avanzado, que requiere agrupar datos lógicamente, validar campos en el cliente con HTML5 nativo y garantizar la vinculación estricta de etiquetas (labels) con sus controles.

### 1. Escenario y Tarea

Debes maquetar el portal de reservas del "Hotel Paraíso". La vista necesita estructurar un gran formulario interactivo que valide los datos antes de enviarlos al servidor, maximizando la usabilidad tanto para usuarios de ratón como de teclado o lectores de pantalla.

### 2. Requisitos Técnicos

- **Formularios Avanzados (U6):**
    - **Agrupación lógica:** El formulario debe estar dividido en al menos dos bloques (Ej: "Datos Personales" y "Detalles de la Reserva") usando `<fieldset>` y `<legend>`.
    - **Vinculación A11y:** Todo `<input>`, `<select>` o `<textarea>` debe tener su `<label>` asociado mediante el binomio `for` / `id`.
    - **Validación HTML5 nativa:**
    - Correo electrónico obligatorio con formato correcto (`type="email"`, `required`).
    - Fechas de entrada y salida (`type="date"`).
    - Número de huéspedes (`type="number"`, mínimo 1, máximo 5).
    - Código postal exacto de 5 dígitos (usar atributo `pattern` con expresión regular `[0-9]{5}`).
    - **Listas de sugerencias:** Un campo de texto para "País de procedencia" que cuente con autocompletado nativo apoyado en una etiqueta `<datalist>`.
    - **Desplegables complejos:** Un `<select>` para el tipo de habitación, cuyas opciones estén agrupadas (Ej: Suite vs Estándar) mediante `<optgroup>`.

---

### 3. Borrador de Requisitos del Formulario

```text
[TITULAR] Reserva tu Estancia
(Incluye la tabla de precios y el mapa de las unidades anteriores como contexto previo).

[FORMULARIO] Debe enviar los datos por el método POST a la ruta '/procesar-reserva'.

Bloque 1: Datos del Huésped
- Nombre Completo (Texto, obligatorio).
- Email de contacto (Email, obligatorio).
- País (Texto, sugerencias de datalist: España, Francia, Italia, Portugal).
- Código postal (Texto, forzar mediante patrón que sean 5 números exactamente).

Bloque 2: Detalles de la Reserva
- Fecha de Entrada (Fecha, obligatoria).
- Fecha de Salida (Fecha, obligatoria).
- Número de Personas (Número, entre 1 y 5, obligatorio).
- Tipo de Habitación (Desplegable, obligatorio).
  - Grupo "Básicas": Individual, Doble.
  - Grupo "Premium": Suite Junior, Suite Presidencial.
- Peticiones especiales (Área de texto de múltiples líneas).
- Botón de Envío: "Confirmar Reserva".
```

## Práctica Global 6: Plataforma de Noticias Accesible (WAI-ARIA)

!!! info "Objetivo de la práctica"
    Esta práctica integra las **Unidades 1 a la 7**. El objetivo principal es construir una estructura HTML5 semánticamente impecable que, además de utilizar *landmarks* clásicos, eleve la accesibilidad al nivel profesional integrando atributos y roles WAI-ARIA para lectores de pantalla.

### 1. Escenario y Tarea

Estás desarrollando "A11y News", un portal de noticias que debe cumplir los estándares WCAG más estrictos. La página principal contiene un atajo de teclado oculto (*skip link*), una navegación por pestañas (tabs), un buscador y una región de alertas en vivo. Sin CSS ni JS, el HTML debe declarar toda esta lógica estructural a las tecnologías de asistencia.

### 2. Requisitos Técnicos

- **Acumulativo (U1-U6):** Esqueleto base validado, imágenes con alternativas precisas, y un formulario de suscripción a la newsletter con validación nativa.
- **Estructura y ARIA (U7):**
    - **Skip Link:** Justo al inicio del `<body>`, incluye un enlace para saltar al contenido principal.
    - **Landmarks explícitos:** Usa `<header>`, `<nav>`, `<main>`, `<aside>` y `<footer>`. Refuérzalos con atributos `aria-label` donde haya ambigüedad (ej. diferenciar el `<nav>` principal del `<nav>` del pie de página).
    - **Buscador Accesible:** El formulario de búsqueda debe usar `role="search"`.
    - **Widget de Pestañas (Tabs):** Maqueta la estructura de un componente de pestañas (Ej: "Noticias Locales" y "Noticias Globales") usando los roles ARIA correctos: `role="tablist"`, `role="tab"`, y `role="tabpanel"`. Usa `aria-selected` y `aria-controls` para vincularlos.
    - **Región Viva (Live Region):** Un área para notificaciones de "Última hora" que el lector de pantalla anuncie automáticamente usando `aria-live="polite"`.

---

### 3. Estructura de Datos (Borrador)

```text
[SKIP LINK] "Saltar al contenido principal" (Enlaza al id del main)

[CABECERA]
- Logo de "A11y News".
- Navegación Principal (con aria-label "Navegación principal"). Enlaces: Inicio, Política, Tecnología.
  -> Señaliza que "Inicio" es la página actual con aria-current="page".
- Buscador de Noticias (Input tipo search, botón buscar). Debe tener rol de búsqueda.

[CONTENIDO PRINCIPAL]
[Región de Alertas]
Texto: "Última hora: Se aprueba la nueva ley de accesibilidad web." (Esta área debe leerse automáticamente al actualizarse su contenido).

[Sección de Pestañas: Categorías]
Pestañas:
- Pestaña 1: Locales (Seleccionada por defecto).
- Pestaña 2: Globales.
Paneles de contenido:
- Panel Locales: Lista de enlaces a noticias de la ciudad.
- Panel Globales: Lista de enlaces a noticias internacionales. (Debe estar oculto de los lectores con aria-hidden="true" inicialmente si no es el panel activo).

[BARRA LATERAL / ASIDE]
- Formulario de Suscripción (U6): Pide el email y muestra los Términos y Condiciones.

[PIE DE PÁGINA]
- Navegación secundaria (con aria-label "Navegación secundaria").
```

---

## Práctica Global 7: Aplicación Web de Gestión de Tareas (APIs y Elementos Interactivos)

!!! info "Objetivo de la práctica"
    El proyecto final. Cubre el temario completo **(Unidades 1 a la 8)**. Consiste en crear el marcado (DOM) de una SPA (Single Page Application) que hace uso intensivo de los elementos interactivos nativos de HTML5 y deja el terreno preparado para consumir las APIs del navegador mediante JavaScript.

### 1. Escenario y Tarea

Vas a maquetar el esqueleto de "TaskTrack", un gestor de proyectos interactivo. No programarás el JavaScript, pero tu HTML debe estar estructurado para que los desarrolladores Frontend puedan "enganchar" los scripts a tus etiquetas nativas interactivas y APIs de forma transparente.

### 2. Requisitos Técnicos

- **Elementos Interactivos (U8):**
    - **Acordeones Nativos:** Usa las etiquetas `<details>` y `<summary>` para ocultar/mostrar la descripción detallada de cada tarea en la lista.
    - **Ventana Modal (Dialog):** Crea un formulario para "Añadir nueva tarea" dentro de una etiqueta `<dialog>`. Incluye un botón para cerrarla que utilice el método nativo (ej. enviando un formulario con `method="dialog"`).
    - **Plantillas (Templates):** Escribe el esqueleto de una tarjeta de tarea dentro de una etiqueta `<template>`. Este código será inerte hasta que JS lo clone.
- **Integración con APIs (U8):**
    - **Atributos data-*: ** Cada tarea (o el template) debe tener atributos de datos personalizados para guardar información como: `data-tarea-id`, `data-prioridad` y `data-estado`.
    - **Canvas:** Incluye una etiqueta `<canvas>` donde posteriormente JS dibujará un gráfico circular del progreso de las tareas.
    - **Geolocalización / Interacción:** Un botón semántico preparado para solicitar la ubicación ("Añadir ubicación a la tarea").

---

### 3. Borrador de la Interfaz

```text
[CABECERA]
- Título: TaskTrack
- Gráfico de progreso (Elemento Canvas preparado).

[PANEL PRINCIPAL]
Lista de Tareas Pendientes.
- Tarea 1: "Reunión de Diseño". (Debe tener data-atributos: id="t1", estado="pendiente", prioridad="alta").
  -> Dentro de esta tarea, usa un elemento interactivo nativo (details/summary) donde el resumen sea "Ver notas de la reunión" y el detalle explique el orden del día.

[BOTONES DE ACCIÓN]
- Botón: "Añadir Tarea". (Este abrirá el modal en JS).
- Botón: "Vincular GPS".

[MODAL (DIALOG)]
Crea un modal nativo que contenga:
- Título: Nueva Tarea.
- Formulario con campo para título y fecha límite.
- Botón para "Guardar".
- Botón para "Cerrar" (usando method="dialog" en un form envolvente o botón).

[PLANTILLA DE COMPONENTE (TEMPLATE)]
Crea un elemento template oculto por defecto que contenga la estructura genérica de una Tarea (un div con título y un botón de borrar), listo para ser clonado por el script.
```
