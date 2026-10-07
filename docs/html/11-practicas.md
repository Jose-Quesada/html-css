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
