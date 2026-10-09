---
icon: lucide/laptop
title: "CSS 16 - Prácticas globales"
description: "Prácticas de desarrollo integral y proyectos acumulativos para consolidar los conocimientos de CSS."
modulo: "LMH (0373) / DIW (0615) / DI (0488)"
unidad: 16
fecha: "2026-10-09"
---

# CSS 16 — Prácticas globales

Este documento reúne prácticas extensas diseñadas para el alumnado de Ciclos Formativos de Grado Superior de la familia de Informática y Comunicaciones (**Desarrollo de Aplicaciones Web - DAW**, **Desarrollo de Aplicaciones Multiplataforma - DAM** y **Administración de Sistemas Informáticos en Red - ASIR**). 

Siguen una metodología **acumulativa y progresiva**: cada práctica evalúa los contenidos de las unidades anteriores e introduce los conceptos de una nueva unidad, desde la combinación inicial de las Unidades 1 y 2 hasta el proyecto integral que abarca hasta la Unidad 14. En todas ellas se proporciona el código **HTML base estructurado y semántico** para que el trabajo se focalice íntegramente en la arquitectura, maquetación, estilo y optimización de las hojas de estilo CSS.

---

## Práctica Global 1: Identidad Corporativa y Guía de Estilo Tipográfica

!!! info "Objetivo de la práctica"
    Esta práctica inicial evalúa de forma conjunta los contenidos de la **Unidad 1 (Fundamentos de CSS: sintaxis, cascada, especificidad, herencia e importancia)** y la **Unidad 2 (Selectores: combinadores, atributos, pseudoclases estructurales/estado y pseudoelementos)**.
    El objetivo es crear una hoja de estilos externa limpia, predecible y mantenible para el manual técnico de identidad de una consultora tecnológica, evitando guerras de especificidad y sin recurrir en ningún caso a `!important`.

### 1. Escenario y Tarea

Has entrado como desarrollador Frontend júnior en **DevCore Solutions**. El equipo de maquetación te entrega el archivo `index.html` con la estructura de la guía de estilo de la empresa. Tu tarea consiste en construir el archivo `styles.css` vinculado externamente, demostrando un control absoluto de la cascada, la especificidad calculada y la selección precisa de elementos en el árbol del DOM.

### 2. Requisitos Técnicos de CSS

1. **Inclusión y Normalización (Unidad 1):**
    - El CSS debe residir en un archivo externo enlazado mediante `<link rel="stylesheet">`.
    - Aplica un reseteo básico de márgenes y rellenos en elementos clave (`*`, `body`, `h1-h3`, `p`, `ul`).
    - Define la tipografía base y el color en el elemento `body`, permitiendo que la **herencia natural** de CSS propague estas propiedades a los elementos descendientes. Fuerza a que los botones y campos hereden explícitamente la fuente usando `inherit`.
2. **Cascada y Especificidad Controlada (Unidad 1):**
    - Queda **estrictamente prohibido el uso de `!important`**. Si una regla no se aplica, debes resolver el conflicto ajustando el orden de aparición o la especificidad de los selectores.
    - Utiliza la pseudoclase lógica `:where()` para definir estilos base o utilidades sin sumar peso de especificidad (`0-0-0`), permitiendo que cualquier selector posterior los sobreescriba con facilidad.
3. **Selectores Avanzados y Combinadores (Unidad 2):**
    - Usa combinadores hijos directos (`>`) para los elementos de navegación directa (`nav > ul > li`).
    - Usa el combinador de hermano adyacente (`+`) para aplicar un margen superior únicamente a los párrafos que sigan inmediatamente a un encabezado `<h2>`.
    - Usa selectores de atributos con comodines:
     - `a[href^="https://"]`: Añade un indicador visual a enlaces externos seguros.
     - `a[href$=".pdf"]`: Estiliza enlaces a documentos descargables.
4. **Pseudoclases Estructurales y de Estado (Unidad 2):**
    - En la lista de especificaciones técnicas, colorea las filas pares mediante `:nth-child(even)` y la primera fila mediante `:first-child`.
    - Utiliza `:not(.activo)` para atenuar los elementos inactivos de la lista.
    - Implementa estados interactivos con `:hover`, `:active`, y garantiza la accesibilidad con `:focus-visible` aplicando un contorno distintivo sin ensuciar la navegación con ratón.
5. **Pseudoelementos Decorativos (Unidad 2):**
    - Emplea `::before` y `::after` con `content` para generar comillas ornamentales en los bloques de citas (`blockquote`) y una pequeña barra de acento decorativa antes de cada título `<h2>`.
    - Personaliza la selección de texto del usuario mediante el pseudoelemento `::selection`.
    - Estiliza las viñetas de las listas con `::marker`.

---

### 3. Código HTML Base Proporcionado

Copia y guarda el siguiente documento como `index.html`. No debes alterar su estructura:

```html title="index.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DevCore Solutions — Guía de Estilo</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <header class="header">
    <div class="header__brand">DevCore Solutions</div>
    <nav class="nav">
      <ul>
        <li><a href="#introduccion" class="activo">Introducción</a></li>
        <li><a href="#colores">Paleta</a></li>
        <li><a href="#tipografia">Tipografía</a></li>
        <li><a href="https://docs.devcore.internal" target="_blank">Docs Externa</a></li>
        <li><a href="assets/manual-marca.pdf">Descargar PDF</a></li>
      </ul>
    </nav>
  </header>

  <main class="content">
    <section id="introduccion" class="section">
      <h1>Manual de Identidad y Estándares de Código</h1>
      <p>Este documento recoge los criterios visuales que deben regir en todos los desarrollos web corporativos.</p>
      <p>La consistencia visual reduce la fricción cognitiva del usuario y refuerza la confiabilidad de la plataforma.</p>
      
      <blockquote cite="https://devcore.internal/manifiesto">
        La elegancia en el software surge de la simplicidad de su arquitectura y la precisión de sus detalles.
      </blockquote>
    </section>

    <section id="reglas" class="section">
      <h2>Principios de Codificación</h2>
      <p>Cada línea de estilo debe tener un propósito justificado y medible en el navegador.</p>
      
      <ul class="specs-list">
        <li>Regla 1: Prohibido el uso de estilos en línea en el HTML.</li>
        <li>Regla 2: Especificidad calculada de forma plana, evitando selectores anidados profundos.</li>
        <li>Regla 3: Separación estricta entre presentación e información.</li>
        <li>Regla 4: Respetar siempre el valor de herencia en inputs y botones.</li>
        <li>Regla 5: Comprobar el comportamiento de foco en navegación por teclado.</li>
      </ul>

      <div class="action-bar">
        <button type="button" class="btn btn-primary">Aceptar directrices</button>
        <button type="button" class="btn btn-secondary">Reportar discrepancia</button>
      </div>
    </section>
  </main>

</body>
</html>
```

---

### 4. Criterios de Evaluación y Entrega

!!! success "Lista de comprobación (Rúbrica de autoevaluación)"
    - [ ] **Hoja externa:** La vinculación se realiza limpiamente en el `<head>` sin estilos `<style>` ni atributos `style=""`.
    - [ ] **Zero `!important`:** No existe ninguna declaración `!important` en todo el archivo CSS.
    - [ ] **Herencia demostrada:** Los botones y el cuerpo de la página comparten la tipografía mediante herencia (`inherit`).
    - [ ] **Selectores avanzados:** Se utilizan selectores de hermano adyacente (`h2 + p`), combinadores de hijo directo (`nav > ul > li`) y selectores de atributos con prefijo `^=` y sufijo `$=`.
    - [ ] **Pseudoelementos:** Se generan barras decorativas en `h2::before`, comillas en `blockquote::before` y estilos de selección con `::selection`.
    - [ ] **Validación:** El código CSS pasa la validación del [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) sin errores.

---

## Práctica Global 2: Fichas de Catálogo de Componentes de Hardware

!!! info "Objetivo de la práctica"
    Esta práctica integra las **Unidades 1 y 2** y añade la **Unidad 3 (El Modelo de Caja: content, padding, border, margin, box-sizing, colapso de márgenes y overflow)**.
    Construirás la maquetación de una tienda de servidores informáticos, controlando al milímetro el cálculo de dimensiones físicas de las cajas y gestionando el desbordamiento.

### 1. Escenario y Tarea

La empresa de infraestructura para centros de datos **ServerStack** necesita maquetar su catálogo de nodos de computación y discos NVMe. Debes estilizar las tarjetas de componentes, tablas de especificaciones de hardware y avisos de stock asegurando que ninguna caja desborde su contenedor y que las dimensiones declaradas coincidan con el renderizado final en pantalla.

### 2. Requisitos Técnicos de CSS

1. **Acumulativo (U1 y U2):**
    - Reset universal aplicando `box-sizing: border-box` a todos los elementos (`*, *::before, *::after`). Explica en un comentario por qué este modelo evita sorpresas al sumar padding y bordes.
    - Selectores de atributos para distinguir tarjetas en oferta (`[data-estado="oferta"]`) y tarjetas sin stock (`[data-stock="0"]`).
    - Pseudoclases `:nth-of-type()` para alternar fondos en las especificaciones técnicas.
2. **Modelo de Caja Estricto (Unidad 3):**
    - **Dimensiones:** Asigna a las tarjetas un ancho fijo o porcentual controlado mediante `min-width` y `max-width` para evitar colapsos visuales.
    - **Padding y Border:** Aplica un espaciado interno generoso en el cuerpo de la tarjeta y un borde sutil con esquinas redondeadas.
    - **Colapso de márgenes:** Demuestra el colapso vertical entre encabezados y párrafos dentro de la tarjeta, y documenta cómo un contenedor con `overflow: hidden` o un padding genera un nuevo contexto que aísla los márgenes interiores.
    - **Outline vs Border:** En el estado `:focus-visible` de los botones de compra, usa `outline` con `outline-offset` en lugar de `border` para no alterar el tamaño físico de la caja al recibir foco.
    - **Gestión de Overflow:** El contenedor de especificaciones de hardware tiene un alto fijo máximo (`max-height: 140px`) y debe gestionar el exceso de texto mediante `overflow-y: auto`, con barras de desplazamiento limpias.

---

### 3. Código HTML Base Proporcionado

```html title="catalogo.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ServerStack — Catálogo de Infraestructura</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <header class="topbar">
    <h1>ServerStack Hardware Solutions</h1>
    <p>Módulos de computación de alto rendimiento para centros de datos</p>
  </header>

  <main class="catalog-container">
    <!-- Tarjeta 1: Producto estándar -->
    <article class="card" data-estado="disponible" data-stock="12">
      <div class="card__header">
        <span class="badge">Rack 1U</span>
        <h2>Nodo Compute Enterprise E5</h2>
      </div>
      <div class="card__body">
        <p class="card__price">1.850 € <span>/ unidad</span></p>
        <div class="card__specs">
          <h4>Especificaciones Técnicas:</h4>
          <ul>
            <li>Procesador: Dual AMD EPYC 9654 (192 núcleos)</li>
            <li>Memoria: 768 GB DDR5 ECC Registered</li>
            <li>Almacenamiento: 4 bahías U.2 PCIe 5.0 NVMe hot-swap</li>
            <li>Conectividad: Dual 25GbE SFP28 Mellanox</li>
            <li>Fuentes: Redundantes 80 Plus Platinum 1200W</li>
            <li>Gestión: IPMI 2.0 dedicado con KVM sobre IP</li>
          </ul>
        </div>
      </div>
      <div class="card__footer">
        <button class="btn btn-buy">Configurar y Pedir</button>
      </div>
    </article>

    <!-- Tarjeta 2: En oferta -->
    <article class="card" data-estado="oferta" data-stock="4">
      <div class="card__header">
        <span class="badge badge--promo">Oferta -15%</span>
        <h2>Array Flash NVMe 30TB</h2>
      </div>
      <div class="card__body">
        <p class="card__price card__price--promo">3.120 € <del>3.680 €</del></p>
        <div class="card__specs">
          <h4>Especificaciones Técnicas:</h4>
          <ul>
            <li>Capacidad: 30.72 TB brutos (8x 3.84TB NVMe)</li>
            <li>IOPS Lectura: Hasta 2.400.000 IOPS 4K</li>
            <li>Controladora: Hardware RAID PCIe Gen4</li>
            <li>Latencia: &lt; 15 microsegundos de acceso</li>
            <li>Factor de forma: 2U montaje en rack estándar</li>
          </ul>
        </div>
      </div>
      <div class="card__footer">
        <button class="btn btn-buy">Añadir al Presupuesto</button>
      </div>
    </article>

    <!-- Tarjeta 3: Sin Stock -->
    <article class="card" data-estado="agotado" data-stock="0">
      <div class="card__header">
        <span class="badge badge--danger">Agotado</span>
        <h2>Acelerador IA Tensor HGX</h2>
      </div>
      <div class="card__body">
        <p class="card__price">Consultar</p>
        <div class="card__specs">
          <h4>Especificaciones Técnicas:</h4>
          <ul>
            <li>Arquitectura: 4x GPU Hopper Tensor Core</li>
            <li>Memoria VRAM: 320 GB HBM3 ultra ancho de banda</li>
            <li>Refrigeración: Líquida directa por bloque de cobre</li>
            <li>Plazo estimado de entrega: 6 semanas</li>
          </ul>
        </div>
      </div>
      <div class="card__footer">
        <button class="btn btn-disabled" disabled>Sin existencias</button>
      </div>
    </article>
  </main>

</body>
</html>
```

---

### 4. Criterios de Evaluación y Entrega

!!! success "Lista de comprobación (Rúbrica de autoevaluación)"
    - [ ] **Modelo de caja universal:** Se declara `box-sizing: border-box` en `*` y sus pseudoelementos.
    - [ ] **Dimensiones y paddings:** Las tarjetas respetan un `max-width` coherente y padding simétrico sin provocar desbordamiento horizontal.
    - [ ] **Scroll interno:** La lista `.card__specs` implementa `max-height` con `overflow-y: auto`, funcionando correctamente sin romper la altura de la tarjeta.
    - [ ] **Uso de outline en foco:** Los botones utilizan `outline-offset` para el foco de teclado sin mover los píxeles de los elementos adyacentes.
    - [ ] **Alineación de badges:** Las etiquetas de oferta y stock emplean márgenes y rellenos proporcionales.

---

## Práctica Global 3: Consola de Operaciones de Ciberseguridad

!!! info "Objetivo de la práctica"
    Esta práctica integra las **Unidades 1, 2, 3** y añade la **Unidad 4 (Posicionamiento y z-index: static, relative, absolute, fixed, sticky, bloques contenedores y stacking context)**.
    Construirás la interfaz de un centro de respuesta a incidentes de seguridad (SOC), con barra de navegación fija, encabezados de logs adhesivos (*sticky*), badges de alerta absolutos y una ventana modal de contención con backdrop.

### 1. Escenario y Tarea

Formas parte del equipo de ingeniería de **CyberShield SOC**. Te solicitan maquetar el panel de monitorización de amenazas en tiempo real. La interfaz debe permitir a los analistas hacer scroll por miles de registros sin perder la cabecera de la tabla (`position: sticky`), mantener accesible la barra de herramientas superior (`position: fixed`) y desplegar un diálogo modal centrado sobre una cortina oscura con control riguroso de `z-index`.

### 2. Requisitos Técnicos de CSS

1. **Acumulativo (U1 a U3):**
    - Reset y modelo de caja (`border-box`).
    - Selectores de atributos para niveles de gravedad (`.log-entry[data-severity="critical"]`, `[data-severity="warning"]`).
    - Pseudoclases para resaltar la fila seleccionada y la última actualización.
2. **Posicionamiento y Capas (Unidad 4):**
    - **`position: fixed`:** La barra superior de estado y métricas (`.soc-header`) debe permanecer anclada en la parte superior del viewport, garantizando que el contenido del documento no quede tapado mediante el padding superior compensatorio en `body` o `main`.
    - **`position: sticky`:** Los títulos de las columnas de la tabla de eventos (`.logs-table thead th`) deben quedar adheridos en la parte superior de su contenedor con scroll cuando el analista navega hacia abajo.
    - **`position: absolute` y Bloque Contenedor:** Cada tarjeta de servidor monitoreado tiene `position: relative`. En su esquina superior derecha, un indicador luminoso de estado (`.status-dot`) se posiciona de forma absoluta usando la propiedad lógica `inset-block-start` e `inset-inline-end` (o `top` y `right`).
    - **Stacking Context y `z-index`:**
     - La ventana modal (`.modal-dialog`) y su fondo oscuro (`.modal-backdrop`) deben superponerse a la barra fija y a las celdas sticky.
     - Prohibido el uso de valores disparatados como `z-index: 99999`. Crea una escala lógica documentada en comentarios: base (1), sticky (10), fixed header (100), backdrop (1000), modal (1010).

---

### 3. Código HTML Base Proporcionado

```html title="soc-dashboard.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CyberShield — Centro de Operaciones de Seguridad</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <!-- Barra fija superior -->
  <header class="soc-header">
    <div class="soc-header__title">
      <span class="pulse-indicator"></span> CyberShield SIEM v4.2
    </div>
    <div class="soc-header__metrics">
      <span>Eventos/seg: 14.820</span>
      <span>Alertas activas: 3</span>
      <span class="user-badge">Operador: SecOps_07</span>
    </div>
  </header>

  <main class="soc-layout">
    <!-- Panel de Servidores (Tarjetas con indicadores absolutos) -->
    <section class="nodes-panel">
      <h2>Nodos en Vigilancia</h2>
      <div class="nodes-grid">
        <div class="node-card" data-status="compromised">
          <span class="status-dot"></span>
          <h3>srv-auth-prod01</h3>
          <p>IP: 10.140.2.15</p>
          <p class="node-alert">Fuerza bruta detectada</p>
        </div>

        <div class="node-card" data-status="secure">
          <span class="status-dot"></span>
          <h3>srv-db-cluster02</h3>
          <p>IP: 10.140.4.88</p>
          <p>Tráfico nominal</p>
        </div>

        <div class="node-card" data-status="warning">
          <span class="status-dot"></span>
          <h3>srv-vpn-gateway</h3>
          <p>IP: 192.168.1.1</p>
          <p>CPU al 94%</p>
        </div>
      </div>
    </section>

    <!-- Tabla con cabecera sticky -->
    <section class="logs-section">
      <h2>Registro de Eventos Recientes</h2>
      <div class="logs-scrollable">
        <table class="logs-table">
          <thead>
            <tr>
              <th>Timestamp</th>
              <th>Origen</th>
              <th>Protocolo</th>
              <th>Gravedad</th>
              <th>Descripción</th>
              <th>Acción</th>
            </tr>
          </thead>
          <tbody>
            <tr class="log-entry" data-severity="critical">
              <td>10:42:15.002</td>
              <td>185.220.101.5</td>
              <td>SSH</td>
              <td><span class="tag tag--critical">CRITICAL</span></td>
              <td>Multiple authentication failures (root)</td>
              <td><button class="btn-action">Aislar</button></td>
            </tr>
            <tr class="log-entry" data-severity="warning">
              <td>10:42:14.810</td>
              <td>10.140.2.15</td>
              <td>HTTPS</td>
              <td><span class="tag tag--warning">WARNING</span></td>
              <td>Certificado SSL próximo a expirar</td>
              <td><button class="btn-action">Revisar</button></td>
            </tr>
            <tr class="log-entry" data-severity="info">
              <td>10:41:59.201</td>
              <td>10.140.4.88</td>
              <td>SQL</td>
              <td><span class="tag tag--info">INFO</span></td>
              <td>Copia de seguridad incremental finalizada</td>
              <td><button class="btn-action">Ver log</button></td>
            </tr>
            <!-- Filas repetidas para forzar el scroll -->
            <tr class="log-entry" data-severity="critical">
              <td>10:40:12.115</td>
              <td>45.154.255.8</td>
              <td>RDP</td>
              <td><span class="tag tag--critical">CRITICAL</span></td>
              <td>Intento de exploit MS17-010 bloqueado</td>
              <td><button class="btn-action">Aislar</button></td>
            </tr>
            <tr class="log-entry" data-severity="info">
              <td>10:39:45.000</td>
              <td>10.140.0.1</td>
              <td>DNS</td>
              <td><span class="tag tag--info">INFO</span></td>
              <td>Sincronización de zona completada</td>
              <td><button class="btn-action">Ver log</button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </main>

  <!-- Ventana Modal de Confirmación de Aislamiento -->
  <div class="modal-backdrop">
    <div class="modal-dialog" role="dialog" aria-modal="true" aria-labelledby="modal-title">
      <div class="modal-header">
        <h3 id="modal-title">Confirmar Aislamiento de Red</h3>
      </div>
      <div class="modal-body">
        <p>¿Deseas aislar inmediatamente el nodo <strong>srv-auth-prod01 (10.140.2.15)</strong>?</p>
        <p class="modal-warning">Se cortarán todas las conexiones excepto el canal de administración por consola serie.</p>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary">Cancelar</button>
        <button class="btn btn-danger">Ejecutar Contención</button>
      </div>
    </div>
  </div>

</body>
</html>
```

---

### 4. Criterios de Evaluación y Entrega

!!! success "Lista de comprobación (Rúbrica de autoevaluación)"
    - [ ] **Cabecera fija sin colisión:** `.soc-header` tiene `position: fixed; top: 0; left: 0; width: 100%;` y el body tiene padding superior para que el contenido no quede oculto bajo ella.
    - [ ] **Encabezados adhesivos:** `thead th` permanece visible arriba al hacer scroll vertical en `.logs-scrollable` gracias a `position: sticky; top: 0;`.
    - [ ] **Indicador absoluto:** `.status-dot` está anclado en la esquina de `.node-card` mediante `position: absolute` referenciado a su padre `relative`.
    - [ ] **Modal centrado y apilado:** El backdrop cubre el 100% del viewport (`inset: 0`) y la modal está centrada con un `z-index` superior a la barra fija.
    - [ ] **Control de apilamiento:** No se usan valores arbitrarios de `z-index`; la jerarquía de capas está documentada en el CSS.

---

## Práctica Global 4: Plataforma de Gestión de Proyectos con Flexbox

!!! info "Objetivo de la práctica"
    Esta práctica integra las **Unidades 1 a 4** y añade la **Unidad 5 (Flexbox: contenedores, ejes, alineación, distribución, propiedades de ítems, gap y layouts fluidos)**.
    Maquetarás el panel de control de un gestor de tareas tipo Jira o Trello, resolviendo la alineación de barras de herramientas, columnas de tarjetas y áreas de trabajo fluidas sin recurrir a floats ni tablas.

### 1. Escenario y Tarea

En la consultora **AgileFlow** te asignan maquetar el tablero Kanban de sprints. El layout exige una cabecera con buscador centrado y perfil empujado a la derecha, una barra de filtros con elementos que se envuelven en pantallas pequeñas (`flex-wrap`) y un tablero de tres columnas cuyas tareas distribuyen sus metadatos (avatar, prioridad, fecha límite) de forma elástica con Flexbox.

### 2. Requisitos Técnicos de CSS

1. **Acumulativo (U1 a U4):**
    - Reset, especificidad plana y modelo de caja estricto.
    - Posicionamiento `sticky` para las cabeceras de cada columna del tablero Kanban mientras se hace scroll por las tarjetas.
    - Indicadores absolutos en los avatares para mostrar el estado online/offline.
2. **Arquitectura Flexbox (Unidad 5):**
    - **Navbar con Margen Automático:** La cabecera principal (`.navbar`) es un flex container. El logo se alinea a la izquierda, el buscador se centra mediante `flex: 1` con `max-width`, y la sección de usuario se envía al extremo derecho mediante `margin-left: auto` o `margin-inline-start: auto`.
    - **Barra de Filtros y Envoltura:** `.filter-bar` debe usar `display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center;` para adaptarse limpiamente sin desbordar.
    - **Tablero de Columnas:** El contenedor `.board` alinea las tres columnas en fila horizontal. Cada columna tiene `flex: 1 1 300px;` para repartir el espacio disponible de forma equitativa.
    - **Tarjeta de Tarea (Eje Cruzado y Principal):**
     - La tarjeta `.task-card` tiene `display: flex; flex-direction: column; gap: 0.5rem;`.
     - El pie de la tarjeta (`.task-card__footer`) dispone las etiquetas y el avatar en los extremos opuestos usando `justify-content: space-between; align-items: center;`.
    - **Control de Crecimiento y Encogimiento:** En la tarjeta, el título ocupa el espacio necesario sin encogerse (`flex-shrink: 0`), mientras que la descripción se ajusta elásticamente.

---

### 3. Código HTML Base Proporcionado

```html title="kanban.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AgileFlow — Sprint Board</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <!-- Navegación Superior Flexbox -->
  <header class="navbar">
    <div class="navbar__brand">
      <span class="logo-icon">⚡</span> AgileFlow
    </div>
    <div class="navbar__search">
      <input type="search" placeholder="Buscar historias o tareas por clave...">
    </div>
    <div class="navbar__user">
      <span class="user-name">Laura Martínez (Scrum Master)</span>
      <div class="avatar-wrapper">
        <div class="avatar">LM</div>
        <span class="presence-dot"></span>
      </div>
    </div>
  </header>

  <!-- Filtros de sprint -->
  <div class="filter-bar">
    <span class="filter-label">Filtrar por:</span>
    <button class="chip chip--active">Mis tareas</button>
    <button class="chip">Solo bugs</button>
    <button class="chip">Backend API</button>
    <button class="chip">Frontend UI</button>
    <button class="btn btn-primary new-task-btn">+ Crear Incidencia</button>
  </div>

  <!-- Tablero Kanban de 3 columnas -->
  <main class="board">
    <!-- Columna 1: Por hacer -->
    <section class="column">
      <div class="column__header">
        <h3>Por Hacer <span class="counter">3</span></h3>
      </div>
      <div class="column__cards">
        <article class="task-card">
          <div class="task-card__tags">
            <span class="tag tag--feature">Feature</span>
            <span class="tag tag--high">Alta</span>
          </div>
          <h4 class="task-card__title">Implementar autenticación multifactor con WebAuthn</h4>
          <p class="task-card__desc">Integrar claves de paso FIDO2 en la pantalla de inicio de sesión.</p>
          <div class="task-card__footer">
            <span class="task-id">AF-104</span>
            <div class="avatar-mini">AL</div>
          </div>
        </article>

        <article class="task-card">
          <div class="task-card__tags">
            <span class="tag tag--docs">Docs</span>
          </div>
          <h4 class="task-card__title">Documentar endpoints de la API v3</h4>
          <p class="task-card__desc">Actualizar especificación OpenAPI con nuevos esquemas de respuesta.</p>
          <div class="task-card__footer">
            <span class="task-id">AF-108</span>
            <div class="avatar-mini">CR</div>
          </div>
        </article>
      </div>
    </section>

    <!-- Columna 2: En progreso -->
    <section class="column">
      <div class="column__header">
        <h3>En Progreso <span class="counter">2</span></h3>
      </div>
      <div class="column__cards">
        <article class="task-card">
          <div class="task-card__tags">
            <span class="tag tag--bug">Bug</span>
            <span class="tag tag--critical">Crítica</span>
          </div>
          <h4 class="task-card__title">Fuga de memoria en el worker de transcodificación</h4>
          <p class="task-card__desc">El proceso Node.js no libera los buffers de vídeo en streaming.</p>
          <div class="task-card__footer">
            <span class="task-id">AF-99</span>
            <div class="avatar-mini">LM</div>
          </div>
        </article>
      </div>
    </section>

    <!-- Columna 3: Completado -->
    <section class="column">
      <div class="column__header">
        <h3>Completado <span class="counter">1</span></h3>
      </div>
      <div class="column__cards">
        <article class="task-card task-card--done">
          <div class="task-card__tags">
            <span class="tag tag--tech">Refactor</span>
          </div>
          <h4 class="task-card__title">Migración de Docker Compose a clúster K8s local</h4>
          <p class="task-card__desc">Manifiestos validados en el entorno de preproducción.</p>
          <div class="task-card__footer">
            <span class="task-id">AF-85</span>
            <div class="avatar-mini">JP</div>
          </div>
        </article>
      </div>
    </section>
  </main>

</body>
</html>
```

---

### 4. Criterios de Evaluación y Entrega

!!! success "Lista de comprobación (Rúbrica de autoevaluación)"
    - [ ] **Navbar flex:** Se utiliza `display: flex` con distribución horizontal; el perfil se desplaza al extremo mediante `margin-left: auto`.
    - [ ] **Envoltura y gap:** La barra de filtros envuelve sus elementos de forma limpia usando `flex-wrap: wrap` y separación mediante `gap`.
    - [ ] **Columnas Kanban:** Las tres columnas del tablero se reparten el espacio horizontal mediante `flex: 1 1 300px` con un contenedor flexible.
    - [ ] **Ejes de las tarjetas:** Cada tarjeta utiliza `flex-direction: column` para el flujo vertical y `justify-content: space-between` en su pie para distanciar ID y avatar.
    - [ ] **Ausencia de floats:** No se emplea ninguna regla `float` ni hacks de despeje (`clearfix`) para alinear elementos.

---

## Práctica Global 5: Portal Tecnológico y Cuadrícula de Datos con CSS Grid

!!! info "Objetivo de la práctica"
    Esta práctica integra las **Unidades 1 a la 5** y añade la **Unidad 6 (CSS Grid: cuadrículas bidimensionales, tracks fr, minmax, auto-fit/auto-fill, grid-template-areas, alineación y subgrid)**.
    Diseñarás la portada de una revista digital de divulgación tecnológica ("TechGazette"), estructurando un layout asimétrico avanzado estilo editorial con tarjetas destacadas que abarcan múltiples filas y columnas.

### 1. Escenario y Tarea

El portal editorial **TechGazette** necesita rediseñar su página principal. El diseño debe combinar un área de artículo principal de doble anchura y doble altura (*hero feature*), una barra lateral de noticias de última hora, una cuadrícula de artículos secundarios autoajustables y un pie de página organizado en cuadrícula. Debes resolver el layout principal con **CSS Grid bidimensional**, reservando Flexbox únicamente para alineaciones unidimensionales en los componentes internos.

### 2. Requisitos Técnicos de CSS

1. **Acumulativo (U1 a U5):**
    - Reset, variables iniciales y modelo de caja.
    - Posicionamiento `relative`/`absolute` en los overlays de lectura sobre imágenes de fondo.
    - Flexbox en las cabeceras de los artículos (para alinear autor, fecha y tiempo de lectura).
2. **Maquetación Bidimensional con CSS Grid (Unidad 6):**
    - **Grid Principal con `grid-template-areas`:** Maqueta la vista principal del portal declarando una cuadrícula con áreas semánticas: `"hero hero aside"` en la parte superior y `"news news aside"` en la siguiente fila.
    - **Abarcamiento de Pistas (*Spanning*):** El artículo principal (`.article--hero`) debe expandirse ocupando `grid-column: span 2` y `grid-row: span 2`.
    - **Galería Autoajustable Responsiva:** La sección de artículos secundarios (`.secondary-grid`) debe maquetarse sin media queries utilizando la técnica:
     `grid-template-columns: repeat(auto-fit, minmax(min(260px, 100%), 1fr)); gap: 1.5rem;`.

    - **Alineación de Celdas:** Utiliza `align-items: stretch` para que todas las tarjetas de una misma fila conserven idéntica altura visual independientemente de la longitud de su contenido.
    - **Flujo Automático Denso:** Aplica `grid-auto-flow: dense` en la sección de píldoras temáticas para rellenar huecos libres si alguna tarjeta tiene dimensiones asimétricas.

---

### 3. Código HTML Base Proporcionado

```html title="portal-tech.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TechGazette — Portal Editorial de Tecnología</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <header class="main-header">
    <div class="site-title">TechGazette Daily</div>
    <div class="edition">Edición Digital Especial · Octubre 2026</div>
  </header>

  <!-- Layout Principal en Grid -->
  <main class="magazine-grid">
    
    <!-- Artículo Portada (Hero: span 2 cols x 2 rows) -->
    <article class="article article--hero">
      <div class="article__badge">En Portada</div>
      <div class="article__content">
        <div class="article__meta">
          <span>Inteligencia Artificial</span> · <time>Hace 2 horas</time>
        </div>
        <h2>La carrera cuántica: Los nuevos procesadores de 1.000 cúbits superan la barrera del ruido térmico</h2>
        <p>Los laboratorios de investigación presentan la primera arquitectura que mantiene la coherencia a temperatura ambiente mediante trampas iónicas de grafeno.</p>
        <span class="read-more">Leer reportaje completo →</span>
      </div>
    </article>

    <!-- Barra lateral de última hora (Aside) -->
    <aside class="sidebar-trending">
      <h3>Última Hora</h3>
      <ol class="trending-list">
        <li>
          <span class="time">11:30</span>
          <p>Publicada la versión 6.14 del kernel Linux con soporte preliminar para Rust en tiempo real.</p>
        </li>
        <li>
          <span class="time">10:45</span>
          <p>El consorcio W3C aprueba formalmente las consultas de contenedor de estilo en CSS.</p>
        </li>
        <li>
          <span class="time">09:15</span>
          <p>Vulnerabilidad Zero-Day detectada en librerías de compresión zlib para sistemas embebidos.</p>
        </li>
      </ol>
    </aside>

    <!-- Sección de Cuadrícula Secundaria (auto-fit) -->
    <section class="secondary-section">
      <h3 class="section-title">Análisis y Opinión</h3>
      <div class="secondary-grid">
        <article class="card-news">
          <span class="category">Ciberseguridad</span>
          <h4>La muerte de las contraseñas</h4>
          <p>Cómo la adopción de FIDO2 y Passkeys está reduciendo el phishing corporativo en un 80%.</p>
        </article>

        <article class="card-news">
          <span class="category">Cloud Computing</span>
          <h4>Repensando el Serverless</h4>
          <p>Por qué las startups vuelven a servidores dedicados para cargas de inferencia de modelos locales.</p>
        </article>

        <article class="card-news">
          <span class="category">Hardware</span>
          <h4>Memorias CXL 3.0 en centros de datos</h4>
          <p>La desagregación de memoria compartida promete triplicar la densidad en servidores virtualizados.</p>
        </article>

        <article class="card-news">
          <span class="category">Desarrollo Web</span>
          <h4>WebAssembly en el Servidor</h4>
          <p>Microservicios ultraligeros que arrancan en microsegundos usando runtimes Wasm/WASI.</p>
        </article>
      </div>
    </section>

  </main>

  <footer class="footer-grid">
    <div><strong>TechGazette</strong> · Información tecnológica independiente</div>
    <div>Licencia Creative Commons BY-SA 4.0</div>
  </footer>

</body>
</html>
```

---

### 4. Criterios de Evaluación y Entrega

!!! success "Lista de comprobación (Rúbrica de autoevaluación)"
    - [ ] **Estructura Grid:** El contenedor principal `.magazine-grid` utiliza `display: grid` con definición de columnas basada en fracciones (`fr`).
    - [ ] **Hero con expansión:** `.article--hero` abarca 2 columnas mediante `grid-column: span 2` (o coordenadas explícitas) y se diferencia del resto de elementos.
    - [ ] **Galería elástica:** La subsección `.secondary-grid` implementa `auto-fit` y `minmax()` adaptándose al ancho del navegador sin media queries.
    - [ ] **Separación limpia:** Se utiliza `gap` en ambas cuadrículas sin márgenes manuales entre celdas.
    - [ ] **Combinación Grid + Flex:** Las cuadrículas manejan el layout exterior y Flexbox se utiliza en los metadatos internos (`.article__meta`) demostrando el uso apropiado de cada tecnología.

---

## Práctica Global 6: Publicación Editorial y Tablas de Precios con Multicolumna y Display Avanzado

!!! info "Objetivo de la práctica"
    Esta práctica integra las **Unidades 1 a la 6** y añade la **Unidad 7 (Flujo normal, multicolumna, tablas CSS y valores avanzados de display: inline-block, none, contents, flow-root)**.
    Maquetarás un informe técnico y comparativa de suscripciones ("OpenSource Digest"), aplicando texto en columnas de estilo periodístico, control de cortes con `break-inside`, tablas con `table-layout: fixed` y cajas flotantes con `shape-outside`.

### 1. Escenario y Tarea

La publicación técnica **OpenSource Digest** necesita maquetar un artículo largo de investigación acompañado de una tabla comparativa de licencias y soporte empresarial. Debes lograr que el texto largo se distribuya en columnas de lectura cómodas, asegurar que los bloques de código y las citas nunca queden partidos entre dos columnas, maquetar una tabla de datos rígida y eficiente con CSS, y demostrar el uso de `display: contents` y `display: flow-root`.

### 2. Requisitos Técnicos de CSS

1. **Acumulativo (U1 a U6):**
    - Reset, especificidad, modelo de caja, posicionamiento de notas al pie y grid en la cabecera.
2. **Multicolumna CSS (Unidad 7):**
    - El cuerpo del informe (`.report-text`) debe distribuirse en **3 columnas** con ancho mínimo mediante `columns: 18rem 3;` y una separación `column-gap: 2rem;`.
    - Aplica una línea divisoria sutil entre columnas con `column-rule: 1px solid #e0e0e0;`.
    - El titular intermedio (`.span-all-heading`) debe romper el flujo de columnas y ocupar todo el ancho usando `column-span: all;`.
    - **Control de cortes:** Los bloques de código (`pre`) y citas (`blockquote`) deben impedir partirse a la mitad entre dos columnas declarando `break-inside: avoid;`.
3. **Tablas CSS y Rendimiento (Unidad 7):**
    - La tabla de tarifas (`.pricing-table`) debe usar `table-layout: fixed;` y `border-collapse: collapse;` para forzar un cálculo de layout instantáneo y determinista.
    - Aplica anchos explícitos en las columnas y cortes de texto con `text-overflow: ellipsis; overflow: hidden; white-space: nowrap;` en celdas estrechas.
4. **Display Avanzado y Flujo (Unidad 7):**
    - Utiliza `display: flow-root;` en los contenedores con cajas flotantes para establecer un nuevo contexto de formato de bloque (*Block Formatting Context - BFC*) sin hacks antiguos de clearfix.
    - Usa `display: contents;` en el envoltorio semántico `.tag-wrapper` para que sus elementos hijos participen directamente en el layout flex/grid del padre sin añadir una caja intermediaria al árbol de renderizado.

---

### 3. Código HTML Base Proporcionado

```html title="informe-editorial.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>OpenSource Digest — Informe Anual</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <article class="report">
    <header class="report-header">
      <h1>Estado del Ecosistema de Código Abierto 2026</h1>
      <p class="subtitle">Análisis de sostenibilidad, seguridad en la cadena de suministro y modelos de negocio</p>
    </header>

    <!-- Contenido Multicolumna -->
    <div class="report-text">
      <p>El software de código abierto sustenta más del noventa por ciento de la infraestructura de telecomunicaciones y computación en la nube actual. Sin embargo, el modelo de mantenimiento descansa con frecuencia sobre equipos reducidos de voluntarios.</p>
      
      <p>Durante el último ejercicio, los ataques contra la cadena de suministro de software se han multiplicado, poniendo de manifiesto la necesidad urgente de auditorías sistemáticas y firmas criptográficas verificables en los repositorios de paquetes comunitarios.</p>

      <blockquote class="callout-quote">
        "La seguridad en el código abierto no es un estado estático, sino un proceso colaborativo continuo de transparencia y verificación de dependencias."
      </blockquote>

      <p>Las organizaciones que consumen librerías externas deben adoptar una postura proactiva, contribuyendo con fondos o tiempo de ingeniería al sostenimiento de los proyectos críticos que integran en sus productos comerciales.</p>

      <!-- Titular que rompe las columnas (column-span: all) -->
      <h2 class="span-all-heading">Comparativa de Modelos de Soporte para Empresas</h2>

      <p>A continuación se evalúan las distintas modalidades de adhesión y licenciamiento para corporaciones que requieren garantías de tiempo de respuesta y parches de seguridad con acuerdos de nivel de servicio (SLA).</p>

      <pre class="code-box"><code># Verificación de firmas con cosign en pipelines CI/CD
cosign verify --key cosign.pub \
  registry.opensource.internal/app:v2.4.0</code></pre>

      <p>La automatización de estas comprobaciones en el ciclo de integración continua previene la inyección de artefactos maliciosos antes de que alcancen el clúster de producción.</p>
    </div>

    <!-- Tabla con table-layout: fixed -->
    <section class="pricing-section">
      <h3>Planes de Mantenimiento Corporativo</h3>
      <table class="pricing-table">
        <thead>
          <tr>
            <th style="width: 25%;">Modalidad</th>
            <th style="width: 25%;">SLA Respuesta</th>
            <th style="width: 25%;">Auditorías CVE</th>
            <th style="width: 25%;">Coste Anual</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Comunitario</strong></td>
            <td>Sin garantía (Best-effort)</td>
            <td>Públicas en GitHub</td>
            <td>0 € (Donación sugerida)</td>
          </tr>
          <tr>
            <td><strong>Business</strong></td>
            <td>&lt; 4 horas hábiles</td>
            <td>Trimestrales dedicadas</td>
            <td>4.800 € / clúster</td>
          </tr>
          <tr>
            <td><strong>Mission Critical</strong></td>
            <td>&lt; 30 minutos (24/7/365)</td>
            <td>Continuas con hotfixes</td>
            <td>18.500 € / clúster</td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- Wrapper que usa display: contents -->
    <div class="meta-footer">
      <div class="tag-wrapper">
        <span class="chip">Licencias</span>
        <span class="chip">Ciberseguridad</span>
        <span class="chip">Gobernanza</span>
      </div>
      <div class="author-info">Redactado por el Comité Técnico de OpenSource Digest</div>
    </div>
  </article>

</body>
</html>
```

---

### 4. Criterios de Evaluación y Entrega

!!! success "Lista de comprobación (Rúbrica de autoevaluación)"
    - [ ] **Multicolumna periodística:** Se aplican `columns`, `column-gap` y `column-rule` en `.report-text`.
    - [ ] **Ruptura horizontal con `column-span`:** El encabezado `.span-all-heading` cruza todas las columnas limpiamente.
    - [ ] **Prevención de cortes con `break-inside`:** Las citas (`blockquote`) y bloques de código (`pre`) evitan fragmentarse mediante `break-inside: avoid`.
    - [ ] **Tabla fija:** La tabla `.pricing-table` declara `table-layout: fixed; border-collapse: collapse;` con dimensiones fijadas por cabecera.
    - [ ] **Uso de `display: flow-root` y `contents`:** Se aplican estas propiedades modernas para gestionar contextos de formato sin divs superfluos.

---

## Práctica Global 7: Sistema de Diseño Tipográfico y Paleta Científica con Funciones Matemáticas

!!! info "Objetivo de la práctica"
    Esta práctica integra las **Unidades 1 a la 7** y añade la **Unidad 8 (Unidades absolutas y relativas: rem, em, ch, vw/vh/dvh, funciones calc(), min(), max(), clamp(), tipografía avanzada y espacios de color modernos)**.
    Construirás la web de un observatorio astronómico y meteorológico ("AstroData Lab"), diseñando una jerarquía tipográfica matemática totalmente fluida y una paleta de color calculada en espacios cromáticos modernos.

### 1. Escenario y Tarea

El centro de investigación **AstroData Lab** te encarga crear la plantilla de divulgación de telemetría celeste. La web debe ofrecer una legibilidad perfecta en cualquier resolución, limitando el ancho de lectura a un número óptimo de caracteres (`ch`), escalando títulos suavemente mediante `clamp()` sin saltos bruscos, e implementando colores mediante funciones de mezcla (`color-mix()`) y modelos HSL/OKLCH.

### 2. Requisitos Técnicos de CSS

1. **Acumulativo (U1 a U7):**
    - Reset, especificidad, modelo de caja, grid para métricas y flex para cabeceras.
2. **Unidades Relativas y Confort de Lectura (Unidad 8):**
    - **Ancho de línea óptimo:** La columna de lectura del artículo debe utilizar `max-width: 68ch;` y centrado horizontal con `margin-inline: auto;`, garantizando entre 60 y 75 caracteres por renglón para evitar la fatiga visual del lector.
    - **Unidades del Viewport Dinámicas:** La sección de portada debe medir la altura exacta visible en móviles utilizando `min-height: 100dvh;` (Dynamic Viewport Height), evitando el desbordamiento provocado por la barra de navegación del navegador en iOS y Android.
3. **Funciones Matemáticas en Tipografía (Unidad 8):**
    - **Escala Fluida con `clamp()`:**
     - Título principal `h1`: `font-size: clamp(2rem, 1.4rem + 2.5vw, 4rem);`.
     - Subtítulo `h2`: `font-size: clamp(1.4rem, 1.1rem + 1.2vw, 2.2rem);`.
     - Párrafo base: `font-size: clamp(1rem, 0.95rem + 0.25vw, 1.15rem);`.
    - **Altura de línea sin unidades:** Asigna `line-height: 1.6;` en párrafos y `line-height: 1.15;` en titulares grandes.
4. **Color y Espacios Cromáticos Modernos (Unidad 8):**
    - Declara una variable base para el azul astronómico (`--astro-blue: hsl(220, 80%, 55%);`).
    - Genera tonos derivados de fondo y contraste usando la función moderna `color-mix()`:
     `--astro-surface: color-mix(in srgb, var(--astro-blue) 12%, #0a0e17);`.
     `--astro-border: color-mix(in srgb, var(--astro-blue) 35%, transparent);`.

---

### 3. Código HTML Base Proporcionado

```html title="astrodata.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AstroData Lab — Observación y Telemetría</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <!-- Hero que ocupa el viewport dinámico -->
  <header class="hero-dvh">
    <div class="hero-content">
      <span class="mission-tag">Misión DeepSky-4 · Estación Canfranc</span>
      <h1>Detección de Ondas Gravitacionales en Fusión Binaria de Agujeros Negros</h1>
      <p class="hero-lead">El interferómetro registra una deformación espacio-temporal de orden attométrica correspondiente al evento GW261009.</p>
    </div>
  </header>

  <!-- Métricas en Grid -->
  <section class="telemetry-bar">
    <div class="metric-card">
      <span class="metric-value">1.42 Mly</span>
      <span class="metric-label">Distancia Luminosa estimada</span>
    </div>
    <div class="metric-card">
      <span class="metric-value">64.8 M☉</span>
      <span class="metric-label">Masa Final del Objeto Remanente</span>
    </div>
    <div class="metric-card">
      <span class="metric-value">0.038 s</span>
      <span class="metric-label">Duración del Chirp Signal</span>
    </div>
    <div class="metric-card">
      <span class="metric-value">3.2 × 10⁴⁹ W</span>
      <span class="metric-label">Energía Pico Liberada</span>
    </div>
  </section>

  <!-- Artículo de Lectura Cómoda con límite en caracteres (ch) -->
  <main class="reading-container">
    <article class="paper">
      <h2>Análisis de la Deformación y Señal Espectral</h2>
      <p>La señal capturada presenta un incremento cuasi-exponencial en la frecuencia de oscilación a lo largo de los últimos tres ciclos de órbita antes de la coalescencia. Los detectores criogénicos mantuvieron un ratio señal/ruido superior a veintiocho durante la ventana de muestreo.</p>

      <p>El espectro electromagnético fue monitorizado de forma simultánea por la red de telescopios ópticos y de rayos gamma sin detección de contrapartida visible, lo que confirma que ambos progenitores carecían de discos de acreción de materia bariónica significativos en el instante del choque.</p>

      <h2>Implicaciones Cosmológicas</h2>
      <p>Esta observación permite restringir las cotas de la constante de Hubble local con una incertidumbre inferior al tres por ciento, aportando evidencia independiente a la tensión cosmológica entre las medidas del fondo cósmico de microondas y las candelas estándar de supernovas tipo Ia.</p>
    </article>
  </main>

</body>
</html>
```

---

### 4. Criterios de Evaluación y Entrega

!!! success "Lista de comprobación (Rúbrica de autoevaluación)"
    - [ ] **Viewport dinámico (`100dvh`):** El hero inicial ocupa el 100% de la altura visible mediante `100dvh`.
    - [ ] **Límite de lectura en `ch`:** La columna `.reading-container` o `.paper` utiliza `max-width: 65ch` o `68ch` para una lectura ergonómica.
    - [ ] **Tipografía fluida con `clamp()`:** Los títulos y textos escalan continuamente sin saltos de media queries.
    - [ ] **Interlineado sin unidades:** Se asignan valores como `1.6` o `1.2` sin sufijos `px` ni `rem` en `line-height`.
    - [ ] **Mezcla de color moderna:** Se generan colores derivados utilizando `color-mix()` o espacios HSL/OKLCH.

---

## Práctica Global 8: Hero Section Inmersivo y Tarjetas con Efectos Visuales

!!! info "Objetivo de la práctica"
    Esta práctica integra las **Unidades 1 a la 8** y añade la **Unidad 9 (Fondos, imágenes y decoración: background avanzado, gradientes lineales/radiales/cónicos, object-fit, sombras complejas, border-radius, filtros, backdrop-filter y clip-path)**.
    Maquetarás la página de aterrizaje de un congreso internacional de desarrollo de software ("FutureDev Summit"), empleando degradados multicapa, efectos de vidrio esmerilado (*glassmorphism*), recortes poligonales y sombras realistas.

### 1. Escenario y Tarea

La conferencia tecnológica **FutureDev Summit** necesita su nueva *Landing Page*. El diseño debe destacar por un impacto visual contemporáneo: un hero con degradados angulares superpuestos, tarjetas de ponentes con imágenes perfectamente encajadas (`object-fit: cover`), un menú flotante con efecto de cristal translúcido (`backdrop-filter`) y un banner en diagonal creado mediante `clip-path`.

### 2. Requisitos Técnicos de CSS

1. **Acumulativo (U1 a U8):**
    - Reset, variables de escala, modelo de caja, posicionamiento fixed/absolute y tipografía con `clamp()`.
2. **Fondos y Gradientes Avanzados (Unidad 9):**
    - El fondo del `.hero` debe combinar un `linear-gradient` semitransparente con un `radial-gradient` que simule un foco de luz ambiental cálido en la esquina superior.
    - En el pie de página, utiliza un degradado angular cónico (`conic-gradient`) como borde perimetral decorativo.
3. **Ajuste de Medios y Decoración (Unidad 9):**
    - Las fotos de los ponentes (`.speaker-card img`) deben mantener su proporción original sin deformarse usando `object-fit: cover; object-position: center top; width: 100%; height: 260px;`.
    - **Sombras multicapa:** Las tarjetas no deben llevar bordes duros; utiliza una sombra suave de doble capa para simular elevación física natural:
     `box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.06);`.
     Al hacer `:hover`, la tarjeta se eleva suavemente aumentando la profundidad de la sombra.

4. **Efecto Glassmorphism y Filtros (Unidad 9):**
    - La barra de navegación flotante (`.glass-nav`) y las tarjetas VIP deben tener un fondo semitransparente (`background: rgba(255, 255, 255, 0.15);`) con desenfoque de fondo mediante `backdrop-filter: blur(12px);` y un borde blanco translúcido (`border: 1px solid rgba(255, 255, 255, 0.25);`).
5. **Recortes Geométricos con `clip-path` (Unidad 9):**
    - La sección de llamada a la acción (`.cta-banner`) debe tener un corte biselado diagonal en su parte superior e inferior usando `clip-path: polygon(0 8%, 100% 0, 100% 92%, 0 100%);`.

---

### 3. Código HTML Base Proporcionado

```html title="summit.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FutureDev Summit 2027 — Innovación y Arquitectura Web</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <!-- Barra flotante Glassmorphism -->
  <nav class="glass-nav">
    <div class="nav-brand">FutureDev '27</div>
    <div class="nav-links">
      <a href="#ponentes">Ponentes</a>
      <a href="#agenda">Agenda</a>
      <a href="#entradas" class="btn-ticket">Conseguir Pase</a>
    </div>
  </nav>

  <!-- Hero con fondo de gradientes múltiples -->
  <header class="hero">
    <div class="hero-inner">
      <span class="pill-date">12–14 de Mayo, 2027 · Palacio de Congresos</span>
      <h1>La Próxima Década del Desarrollo de Software</h1>
      <p>Tres jornadas inmersivas sobre compiladores WebAssembly, inteligencia distribuida en el borde y arquitecturas resilientes.</p>
      <div class="hero-actions">
        <button class="btn btn-primary">Registrarse ahora</button>
        <button class="btn btn-outline">Ver programa completo</button>
      </div>
    </div>
  </header>

  <!-- Grid de Ponentes con object-fit y sombras -->
  <section id="ponentes" class="speakers-section">
    <h2>Ponentes Destacados</h2>
    <div class="speakers-grid">
      <article class="speaker-card">
        <div class="speaker-img-wrapper">
          <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=600&q=80" alt="Dra. Elena Vasquez">
        </div>
        <div class="speaker-info">
          <h3>Dra. Elena Vásquez</h3>
          <p class="role">Chief Architect en QuantumEdge</p>
          <p class="talk-title">Conferencia: "Modelos Fundacionales en Dispositivos Embebidos"</p>
        </div>
      </article>

      <article class="speaker-card">
        <div class="speaker-img-wrapper">
          <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=600&q=80" alt="Marcus Lindqvist">
        </div>
        <div class="speaker-info">
          <h3>Marcus Lindqvist</h3>
          <p class="role">Lead Core Contributor en V8 Engine</p>
          <p class="talk-title">Conferencia: "Optimizaciones JIT de Nueva Generación"</p>
        </div>
      </article>

      <article class="speaker-card speaker-card--featured">
        <div class="speaker-img-wrapper">
          <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=600&q=80" alt="Sarah Chen">
        </div>
        <div class="speaker-info">
          <h3>Sarah Chen</h3>
          <p class="role">Directora de Infraestructura en CloudScale</p>
          <p class="talk-title">Keynote: "Escalando a 100 Millones de Conexiones WebSocket"</p>
        </div>
      </article>
    </div>
  </section>

  <!-- Banner con clip-path diagonal -->
  <section class="cta-banner">
    <div class="cta-inner">
      <h2>¿Preparado para liderar el cambio tecnológico?</h2>
      <p>Plazas presenciales limitadas a 1.200 asistentes para garantizar sesiones de trabajo de alta interacción.</p>
      <button class="btn btn-white">Reservar Entrada Early Bird</button>
    </div>
  </section>

</body>
</html>
```

---

### 4. Criterios de Evaluación y Entrega

!!! success "Lista de comprobación (Rúbrica de autoevaluación)"
    - [ ] **Degradados múltiples:** El fondo del hero superpone al menos dos gradientes (`linear-gradient` y `radial-gradient`).
    - [ ] **`object-fit: cover`:** Las imágenes de los ponentes no sufren estiramientos ni distorsiones de aspecto al ajustar sus dimensiones en CSS.
    - [ ] **Glassmorphism:** La barra `.glass-nav` implementa `backdrop-filter: blur(...)` y borde translúcido.
    - [ ] **Sombras naturales:** Las tarjetas implementan sombras multicapa y elevación sutil en estado hover.
    - [ ] **Recorte con `clip-path`:** La sección `.cta-banner` presenta un corte angular funcional generado con la función `polygon()`.

---

## Práctica Global 9: Comercio Electrónico Totalmente Responsivo (Mobile-First)

!!! info "Objetivo de la práctica"
    Esta práctica integra las **Unidades 1 a la 9** y añade la **Unidad 10 (Diseño responsivo: enfoque mobile-first, viewport, media queries con sintaxis de rango moderna, consultas de características de puntero y patrones de layout fluido)**.
    Diseñarás la interfaz completa de un ecommerce de productos tecnológicos ("TechMarket"), asegurando que la experiencia comience perfectamente optimizada para smartphones y evolucione hacia tablets y pantallas de escritorio panorámicas.

### 1. Escenario y Tarea

En **TechMarket** el 70% del tráfico proviene de dispositivos móviles. La dirección exige una arquitectura CSS puramente **Mobile-First**: el código fuera de media queries debe dar formato al móvil pequeño (`320px–480px`), y mediante media queries con sintaxis moderna (`min-width`) se ampliará progresivamente el catálogo hacia 2, 3 y 4 columnas, transformando el menú colapsable en una barra horizontal y adaptando las dianas táctiles según el dispositivo disponga de ratón (`hover: hover`) o pantalla táctil (`pointer: coarse`).

### 2. Requisitos Técnicos de CSS

1. **Acumulativo (U1 a U9):**
    - Reset, variables CSS, Flexbox, Grid y efectos visuales de tarjetas.
2. **Filosofía Mobile-First y Sintaxis de Rango (Unidad 10):**
    - Todo el CSS base debe escribirse pensando en una única columna móvil.
    - Prohibido el uso exclusivo de `@media (max-width: ...)`. Utiliza la sintaxis moderna de rangos:
     - Tablet: `@media (width >= 768px) { ... }`.
     - Escritorio: `@media (width >= 1024px) { ... }`.
     - Monitores anchos: `@media (width >= 1440px) { ... }`.
3. **Adaptación de Interacción según Capacidades del Puntero (Unidad 10):**
    - En dispositivos táctiles (`@media (pointer: coarse)`), aumenta la altura mínima de todos los botones y enlaces a **48px** para cumplir la directriz de ergonomía táctil de Fitts.
    - En pantallas con puntero de precisión (`@media (hover: hover)`), añade efectos de elevación al posar el ratón sobre los productos que no se activen accidentalmente en móviles.
4. **Patrón de Layout Responsivo (Unidad 10):**
    - La barra lateral de filtros (`.filters-aside`) aparece debajo o colapsada en móvil, y en pantallas de escritorio (`width >= 1024px`) se convierte en una columna fija a la izquierda de `260px` mientras el catálogo ocupa el resto.
    - El catálogo de productos (`.products-grid`) pasa de 1 columna (móvil) a 2 columnas (tablet) y 3-4 columnas (escritorio).
    - Uso de `aspect-ratio: 1 / 1` en las imágenes de producto para reservar el espacio antes de que carguen, impidiendo saltos de página (CLS).

---

### 3. Código HTML Base Proporcionado

```html title="techmarket.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TechMarket — Componentes y Gadgets</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <!-- Cabecera Responsiva -->
  <header class="app-header">
    <div class="header-main">
      <button class="menu-toggle" aria-label="Abrir menú">☰</button>
      <div class="brand">TechMarket</div>
      <div class="search-box">
        <input type="search" placeholder="Buscar productos...">
      </div>
      <div class="cart-btn">🛒 <span class="cart-count">2</span></div>
    </div>
    <nav class="nav-menu">
      <ul>
        <li><a href="#">Portátiles</a></li>
        <li><a href="#">Periféricos</a></li>
        <li><a href="#">Monitores</a></li>
        <li><a href="#">Componentes</a></li>
        <li><a href="#">Ofertas</a></li>
      </ul>
    </nav>
  </header>

  <!-- Contenedor Principal con Layout Adaptativo -->
  <div class="store-layout">
    <!-- Filtros laterales -->
    <aside class="filters-aside">
      <h3>Filtros</h3>
      <div class="filter-group">
        <h4>Disponibilidad</h4>
        <label><input type="checkbox" checked> En stock (envío 24h)</label>
        <label><input type="checkbox"> En oferta</label>
      </div>
      <div class="filter-group">
        <h4>Rango de Precio</h4>
        <label><input type="radio" name="price" checked> Todos los precios</label>
        <label><input type="radio" name="price"> Hasta 200 €</label>
        <label><input type="radio" name="price"> 200 € a 600 €</label>
        <label><input type="radio" name="price"> Más de 600 €</label>
      </div>
    </aside>

    <!-- Catálogo de Productos -->
    <main class="products-container">
      <div class="catalog-toolbar">
        <h2>Periféricos y Monitores (24 resultados)</h2>
        <select class="sort-select">
          <option>Ordenar por: Más relevantes</option>
          <option>Precio: de menor a mayor</option>
          <option>Precio: de mayor a menor</option>
        </select>
      </div>

      <div class="products-grid">
        <article class="product-card">
          <div class="product-media">
            <img src="https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?auto=format&fit=crop&w=500&q=80" alt="Ratón ergonómico inalámbrico">
          </div>
          <div class="product-details">
            <span class="product-category">Periféricos</span>
            <h3 class="product-title">Ratón Ergonómico Vertical 4000 DPI</h3>
            <p class="product-price">59,99 €</p>
            <button class="btn btn-add-cart">Añadir a la cesta</button>
          </div>
        </article>

        <article class="product-card">
          <div class="product-media">
            <img src="https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=500&q=80" alt="Teclado mecánico custom">
          </div>
          <div class="product-details">
            <span class="product-category">Periféricos</span>
            <h3 class="product-title">Teclado Mecánico 75% Switch Táctil Hot-Swap</h3>
            <p class="product-price">124,50 €</p>
            <button class="btn btn-add-cart">Añadir a la cesta</button>
          </div>
        </article>

        <article class="product-card">
          <div class="product-media">
            <img src="https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=500&q=80" alt="Monitor panorámico 34 pulgadas">
          </div>
          <div class="product-details">
            <span class="product-category">Monitores</span>
            <h3 class="product-title">Monitor Curvo UltraWide 34" WQHD 144Hz</h3>
            <p class="product-price">489,00 €</p>
            <button class="btn btn-add-cart">Añadir a la cesta</button>
          </div>
        </article>

        <article class="product-card">
          <div class="product-media">
            <img src="https://images.unsplash.com/photo-1590658268037-6bf12165a8df?auto=format&fit=crop&w=500&q=80" alt="Auriculares con cancelación de ruido">
          </div>
          <div class="product-details">
            <span class="product-category">Audio</span>
            <h3 class="product-title">Auriculares Inalámbricos ANC Pro 40h Batería</h3>
            <p class="product-price">179,00 €</p>
            <button class="btn btn-add-cart">Añadir a la cesta</button>
          </div>
        </article>
      </div>
    </main>
  </div>

</body>
</html>
```

---

### 4. Criterios de Evaluación y Entrega

!!! success "Lista de comprobación (Rúbrica de autoevaluación)"
    - [ ] **Filosofía Mobile-First:** El código base no depende de media queries; las reglas para pantallas mayores se introducen progresivamente con `min-width`.
    - [ ] **Sintaxis de rango moderna:** Se escriben expresiones como `@media (width >= 768px)`.
    - [ ] **Diana táctil adaptativa:** Se utiliza `@media (pointer: coarse)` para expandir el área clicable de controles a $\ge 48\text{px}$.
    - [ ] **Patrón Column Drop:** En pantallas grandes (`>= 1024px`), el layout pasa de una columna vertical a un sistema de dos columnas (filtros a la izquierda + catálogo a la derecha).
    - [ ] **Prevención de CLS:** Las imágenes de producto tienen `aspect-ratio` declarado en CSS para reservar el espacio antes de cargar.

---

## Práctica Global 10: Interfaz Interactiva de Videojuego con Transiciones y Animaciones 3D

!!! info "Objetivo de la práctica"
    Esta práctica integra las **Unidades 1 a la 10** y añade la **Unidad 11 (Transiciones, animaciones con @keyframes, transformaciones 2D y 3D, funciones de temporización y aceleración por hardware en la GPU)**.
    Crearás el panel de mandos (*HUD*) de una nave en un videojuego de estrategia espacial ("Galaxy Vanguard"), con radares pulsantes, tarjetas de naves con giro 3D (*flip cards*), barras de energía reactivas y efectos de telemetría a 60 FPS.

### 1. Escenario y Tarea

En el estudio de videojuegos indie **Nebula Games** necesitan maquetar la interfaz web del hangar de combate. Debes crear una experiencia interactiva puramente en CSS: un radar con rotación continua, barras de escudo que se animan con transiciones suaves, tarjetas de cazas que se giran 180 grados en tres dimensiones al hacer hover o clic para mostrar su armamento, y un botón de alerta roja que pulsa rítmicamente sin causar repintados continuos (*layout thrashing*).

### 2. Requisitos Técnicos de CSS

1. **Acumulativo (U1 a U10):**
    - Reset, variables, posicionamiento, flexbox, grid y comportamiento responsivo.
2. **Transiciones y Temporización Personalizada (Unidad 11):**
    - Los botones interactivos (`.btn-combat`) deben reaccionar con transiciones fluidas de `transform` y `background-color` utilizando una curva de rebote elástica personalizada:
     `transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease;`.

    - En `:active`, el botón debe contraerse con `transform: scale(0.95);`.
3. **Animaciones con `@keyframes` y Rendimiento GPU (Unidad 11):**
    - **Radar Escáner:** El barrido del radar (`.radar-sweep`) debe girar infinitamente mediante una animación `@keyframes radarSpin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }` con `animation: radarSpin 3s linear infinite;`.
    - **Alerta Pulsante:** La señal de peligro (`.alert-beacon`) debe emitir pulsos expansivos modulando `transform: scale()` y `opacity`. Queda estrictamente prohibido animar `width`, `height` o `margin` para no forzar la fase de Layout del motor de renderizado.
4. **Transformaciones Tridimensionales (Unidad 11):**
    - **Tarjeta 3D Flip Card:**
     - El contenedor `.flip-card` define la profundidad con `perspective: 1000px;`.
     - El elemento interior `.flip-card__inner` debe declarar `transform-style: preserve-3d;` y una transición en `transform: rotateY(180deg);`.
     - Las caras delantera (`.flip-card__front`) y trasera (`.flip-card__back`) deben tener `backface-visibility: hidden;` y posición absoluta, con la cara trasera prerrotada a `rotateY(180deg)`.

---

### 3. Código HTML Base Proporcionado

```html title="hangar.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Galaxy Vanguard — Terminal Táctico del Hangar</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <header class="hud-header">
    <div class="hud-brand">
      <span class="alert-beacon"></span> SISTEMA DE DEFENSA ORBITAL
    </div>
    <div class="hud-status">
      <span>Estado: CONDICIÓN AMARILLA</span>
      <span>Sector: Kepler-186f</span>
    </div>
  </header>

  <main class="hud-main">
    
    <!-- Módulo de Radar Circular -->
    <section class="radar-module">
      <h2>Escáner de Proximidad</h2>
      <div class="radar-screen">
        <div class="radar-grid"></div>
        <div class="radar-sweep"></div>
        <div class="radar-blip blip-1"></div>
        <div class="radar-blip blip-2"></div>
      </div>
    </section>

    <!-- Módulo de Tarjetas 3D de Cazas -->
    <section class="ships-module">
      <h2>Hangar de Cazas Disponibles (Pasa el ratón para voltear)</h2>
      
      <div class="ships-grid">
        <!-- Tarjeta 3D 1 -->
        <div class="flip-card">
          <div class="flip-card__inner">
            <div class="flip-card__front">
              <div class="ship-badge">Intersector</div>
              <h3>Interceptor FX-9 Phoenix</h3>
              <p class="ship-class">Clase: Caza Ligero de Ataque Rápido</p>
              <div class="stat-bar">
                <label>Velocidad Sublumínica</label>
                <div class="bar-track"><div class="bar-fill bar-fill--speed" style="width: 95%;"></div></div>
              </div>
              <div class="stat-bar">
                <label>Escudos Deflectores</label>
                <div class="bar-track"><div class="bar-fill bar-fill--shields" style="width: 45%;"></div></div>
              </div>
            </div>
            <div class="flip-card__back">
              <h3>Configuración de Armas</h3>
              <ul>
                <li>2x Cañones de Plasma Duales</li>
                <li>4x Torpedos de Protones</li>
                <li>Postquemador de Iones</li>
              </ul>
              <button class="btn btn-launch">Desplegar Nave</button>
            </div>
          </div>
        </div>

        <!-- Tarjeta 3D 2 -->
        <div class="flip-card">
          <div class="flip-card__inner">
            <div class="flip-card__front">
              <div class="ship-badge">Bombardero</div>
              <h3>Titan Siege B-2</h3>
              <p class="ship-class">Clase: Nave Pesada de Asedio</p>
              <div class="stat-bar">
                <label>Velocidad Sublumínica</label>
                <div class="bar-track"><div class="bar-fill bar-fill--speed" style="width: 40%;"></div></div>
              </div>
              <div class="stat-bar">
                <label>Escudos Deflectores</label>
                <div class="bar-track"><div class="bar-fill bar-fill--shields" style="width: 90%;"></div></div>
              </div>
            </div>
            <div class="flip-card__back">
              <h3>Configuración de Armas</h3>
              <ul>
                <li>1x Batería de Cañón Gauss</li>
                <li>8x Cargas Sísmicas de Fragmentación</li>
                <li>Blindaje de Nanotubos de Carbono</li>
              </ul>
              <button class="btn btn-launch">Desplegar Nave</button>
            </div>
          </div>
        </div>
      </div>
    </section>

  </main>

</body>
</html>
```

---

### 4. Criterios de Evaluación y Entrega

!!! success "Lista de comprobación (Rúbrica de autoevaluación)"
    - [ ] **Animación continua del radar:** La línea del radar gira $360^\circ$ en un bucle continuo infinito con `@keyframes` y `linear`.
    - [ ] **Tarjeta 3D funcional:** La tarjeta utiliza `perspective: 1000px`, `transform-style: preserve-3d` y `backface-visibility: hidden` para rotar al hacer hover.
    - [ ] **Curva cubic-bezier:** Se implementan transiciones de rebote o suavizadas mediante `cubic-bezier()` en botones interactivos.
    - [ ] **Optimización de renderizado:** Solo se animan propiedades transformadas (`transform`) y transparencia (`opacity`), evitando microtirones y repintados de layout.

---

## Práctica Global 11: Aplicación Dashboard Arquitecturada con CSS Moderno (Variables, Nesting, Container Queries y BEM)

!!! info "Objetivo de la práctica"
    Esta práctica integra las **Unidades 1 a la 11** y añade la **Unidad 12 (CSS moderno y arquitectura: variables en 3 capas, anidamiento nativo con &, consultas de contenedor @container, capas de cascada @layer y metodología BEM)**.
    Construirás la arquitectura de estilos de un panel analítico multi-tenant ("MetricFlow"), utilizando las funcionalidades más avanzadas de los estándares CSS actuales.

### 1. Escenario y Tarea

En la compañía SaaS **MetricFlow** te encargan rehacer el núcleo de estilos del dashboard de analítica. El proyecto requiere una arquitectura profesional: organizar la especificidad con `@layer`, nombrar componentes con metodología BEM, gestionar temas (modo claro y oscuro) mediante variables CSS nativas, anidar reglas con CSS Nesting nativo (sin compiladores Sass) y lograr que los widgets adapten su disposición interna según el ancho de su propio contenedor gracias a **Container Queries**.

### 2. Requisitos Técnicos de CSS

1. **Capas de Cascada con `@layer` (Unidad 12):**
    - Declara el orden de prelación al inicio del archivo: `@layer reset, base, components, utilities;`.
    - Coloca los estilos de reseteo en `@layer reset` y los componentes en `@layer components`. De este modo, una clase de componente siempre prevalece sobre una regla base independientemente de la especificidad del selector.
2. **Tokens de Diseño en 3 Capas y Modos de Color (Unidad 12):**
    - **Primitivos:** `--color-brand-500: #6366f1;`, `--color-slate-900: #0f172a;`, etc.
    - **Semánticos:** `--bg-app`, `--text-main`, `--card-bg`, referenciando los primitivos.
    - **De componente:** `--widget-padding`, `--widget-border`.
    - Soporte para cambio de tema: redefine las variables semánticas en `[data-theme="dark"]` sin modificar las reglas de los componentes.
3. **Metodología BEM y Anidamiento Nativo (Unidad 12):**
    - Aplica BEM riguroso: bloque `.widget`, elemento `.widget__header`, modificador `.widget--highlighted`.
    - Emplea el anidamiento nativo de CSS usando `&`:
     ```css
     .widget {
       background: var(--card-bg);
       &__header { display: flex; justify-content: space-between; }
       &--highlighted { border-color: var(--color-brand-500); }
       &:hover { transform: translateY(-2px); }
     }
     ```
4. **Consultas de Contenedor (*Container Queries*) (Unidad 12):**
    - Declara el contenedor de cada widget como contexto de consulta:
     `.widget-wrapper { container-type: inline-size; container-name: widget; }`.

    - Escribe una consulta `@container widget (min-width: 420px)` para que el widget pase de una disposición vertical compacta a una horizontal expandida cuando su celda de la cuadrícula sea suficientemente ancha, con total independencia del tamaño de la ventana global.

---

### 3. Código HTML Base Proporcionado

```html title="metricflow.html"
<!DOCTYPE html>
<html lang="es" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MetricFlow — Analytics Dashboard</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <div class="app-shell">
    <header class="app-shell__topbar">
      <div class="topbar-logo">MetricFlow Platform</div>
      <div class="topbar-actions">
        <button class="theme-toggle-btn" aria-label="Cambiar tema">Modo Claro/Oscuro</button>
      </div>
    </header>

    <!-- Layout del Dashboard con widgets de anchos desiguales -->
    <main class="dashboard-grid">
      
      <!-- Widget 1: Contenedor Ancho (2 columnas) -->
      <div class="widget-wrapper widget-wrapper--wide">
        <article class="widget widget--highlighted">
          <header class="widget__header">
            <h3 class="widget__title">Ingresos Mensuales Recurrentes (MRR)</h3>
            <span class="widget__badge">+18.4%</span>
          </header>
          <div class="widget__body">
            <div class="widget__metric">84.250 €</div>
            <div class="widget__detail">
              <p>Objetivo de Q4: 100.000 € alcanzado al 84%.</p>
              <div class="progress-bar"><div class="progress-bar__fill" style="width: 84%;"></div></div>
            </div>
          </div>
          <footer class="widget__footer">Actualizado en tiempo real desde Stripe API</footer>
        </article>
      </div>

      <!-- Widget 2: Contenedor Estrecho (1 columna) -->
      <div class="widget-wrapper widget-wrapper--narrow">
        <article class="widget">
          <header class="widget__header">
            <h3 class="widget__title">Usuarios Activos</h3>
            <span class="widget__badge">Online</span>
          </header>
          <div class="widget__body">
            <div class="widget__metric">1.428</div>
            <div class="widget__detail">
              <p>Sesiones activas en los últimos 15 min.</p>
            </div>
          </div>
          <footer class="widget__footer">Telemetría WebSocket</footer>
        </article>
      </div>

      <!-- Widget 3: Contenedor Estrecho (1 columna) -->
      <div class="widget-wrapper widget-wrapper--narrow">
        <article class="widget">
          <header class="widget__header">
            <h3 class="widget__title">Tasa de Churn</h3>
            <span class="widget__badge widget__badge--good">1.2%</span>
          </header>
          <div class="widget__body">
            <div class="widget__metric">Bajo</div>
            <div class="widget__detail">
              <p>Promedio de la industria: 3.5%.</p>
            </div>
          </div>
          <footer class="widget__footer">Retención a 30 días</footer>
        </article>
      </div>

    </main>
  </div>

</body>
</html>
```

---

### 4. Criterios de Evaluación y Entrega

!!! success "Lista de comprobación (Rúbrica de autoevaluación)"
    - [ ] **Capas de cascada (`@layer`):** Se declaran y utilizan capas (`reset`, `base`, `components`, etc.) para estructurar la precedencia.
    - [ ] **Tokens en 3 capas:** Se definen variables primitivas, semánticas y de componente; el tema oscuro conmuta reasignando variables en `[data-theme="dark"]`.
    - [ ] **CSS Nesting nativo:** Se utiliza anidamiento con `&` sin herramientas de preprocesado externo.
    - [ ] **Container Queries:** Se define `container-type: inline-size` y se aplica `@container` para adaptar el layout del widget según el ancho de su celda.
    - [ ] **Nomenclatura BEM:** Se respetan estrictamente los convenios de bloque, elemento y modificador.

---

## Práctica Global 12: Portal de Trámites Públicos con Accesibilidad Universal (WCAG 2.1 AA/AAA)

!!! info "Objetivo de la práctica"
    Esta práctica integra las **Unidades 1 a la 12** y añade la **Unidad 13 (Accesibilidad y usabilidad: ratios de contraste WCAG, foco visible, navegación por teclado, consultas de preferencias prefers-reduced-motion / prefers-color-scheme / prefers-contrast, clase .sr-only y formularios accesibles)**.
    Diseñarás la interfaz de la Sede Electrónica de solicitud de becas para el Ministerio de Educación ("SedeEduca"), garantizando el cumplimiento riguroso de la normativa legal de accesibilidad (Directiva Europea 2016/2102 y RD 1112/2018).

### 1. Escenario y Tarea

En la consultora de administración digital te encomiendan auditar y maquetar la interfaz de **SedeEduca**. La aplicación debe ser 100% operable por personas ciegas que usan lectores de pantalla, usuarios con visión reducida que requieren contrastes elevados o zoom al 200%, usuarios con discapacidad motriz que navegan exclusivamente con teclado (tecla Tab) y personas con trastornos vestibulares sensibles a las animaciones bruscas.

### 2. Requisitos Técnicos de CSS

1. **Acumulativo (U1 a U12):**
    - Reset, `@layer`, tokens semánticos, Flexbox, Grid y BEM.
2. **Contraste y Foco Visible (Unidad 13):**
    - **Ratios WCAG 2.1 AA:** Todo el texto regular debe tener un contraste $\ge 4.5:1$ contra el fondo, y los textos grandes o bordes de formulario $\ge 3:1$.
    - **Foco visible de teclado:** Declara un anillo de foco visible personalizado e inconfundible usando `:focus-visible { outline: 3px solid #1a56db; outline-offset: 3px; }`.
    - **Contenedores activos:** Usa `.form-card:focus-within` para iluminar sutilmente la tarjeta del formulario cuando el usuario esté editando cualquiera de sus campos interiores.
3. **Skip Link (Enlace de Salto) (Unidad 13):**
    - El enlace `.skip-link` debe estar ubicado fuera de la pantalla mediante `position: absolute; top: -9999px; left: 1rem;` y debe aparecer inmediatamente en la esquina superior cuando reciba el foco del teclado (`.skip-link:focus { top: 1rem; z-index: 1000; }`), permitiendo saltar la cabecera directamente al `<main>`.
4. **Consultas de Preferencias del Usuario (Unidad 13):**
    - **`@media (prefers-reduced-motion: reduce)`:** Desactiva todas las transiciones y transformaciones decorativas (`animation-duration: 0.01ms !important; transition-duration: 0.01ms !important;`) para respetar la salud de personas con migrañas o vértigo.
    - **`@media (prefers-contrast: more)`:** Aumenta el grosor de los bordes a 2px sólidos y utiliza fondos de máximo contraste blanco/negro puro.
    - **`@media (prefers-color-scheme: dark)`:** Adapta automáticamente los tokens semánticos al modo oscuro del sistema operativo.
5. **Patrón `.sr-only` (Screen Reader Only) (Unidad 13):**
    - Escribe la clase accesible `.sr-only` que oculta visualmente el texto sin usar `display: none` ni `visibility: hidden`, de modo que los sintetizadores de voz puedan leerlo.

---

### 3. Código HTML Base Proporcionado

```html title="sededuca.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SedeEduca — Convocatoria General de Becas 2026/2027</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <!-- Skip link para navegación por teclado -->
  <a href="#contenido-principal" class="skip-link">Saltar directamente al trámite principal</a>

  <header class="gov-header">
    <div class="gov-header__banner">
      <span>Gobierno de España · Ministerio de Educación y Formación Profesional</span>
    </div>
    <div class="gov-header__main">
      <h1>SedeEduca · Portal Oficial de Trámites Telemáticos</h1>
    </div>
  </header>

  <main id="contenido-principal" class="gov-main" tabindex="-1">
    
    <nav aria-label="Migas de pan" class="breadcrumbs">
      <ol>
        <li><a href="#">Inicio</a></li>
        <li><a href="#">Becas y Ayudas</a></li>
        <li aria-current="page">Estudios Universitarios y Superiores</li>
      </ol>
    </nav>

    <div class="form-card">
      <h2>Formulario de Solicitud de Beca General</h2>
      <p class="form-desc">Los campos marcados con <span class="required-indicator" aria-hidden="true">*</span><span class="sr-only">obligatorio</span> deben cumplimentarse obligatoriamente.</p>

      <form novalidate class="gov-form">
        
        <div class="form-group">
          <label for="dni" class="form-label">
            Documento Nacional de Identidad (DNI/NIE) <span class="required-indicator" aria-hidden="true">*</span>
          </label>
          <input type="text" id="dni" class="form-control" placeholder="12345678Z" aria-describedby="dni-help">
          <span id="dni-help" class="form-help">Incluye la letra final sin espacios ni guiones.</span>
        </div>

        <div class="form-group">
          <label for="ingresos" class="form-label">
            Renta Computable de la Unidad Familiar (€) <span class="required-indicator" aria-hidden="true">*</span>
          </label>
          <input type="number" id="ingresos" class="form-control" placeholder="Ej: 18500" aria-describedby="ingresos-help">
          <span id="ingresos-help" class="form-help">Conforme a la casilla 435 de la declaración de IRPF del ejercicio anterior.</span>
        </div>

        <div class="form-group form-group--checkbox">
          <label class="checkbox-label">
            <input type="checkbox" id="movilidad">
            <span>Solicito la ayuda complementaria por residencia fuera del domicilio familiar</span>
          </label>
        </div>

        <div class="form-actions">
          <button type="submit" class="btn btn-primary">Firmar y Enviar Solicitud</button>
          <button type="button" class="btn btn-secondary">Guardar Borrador</button>
        </div>

      </form>
    </div>

  </main>

  <footer class="gov-footer">
    <p>Conforme con las Pautas de Accesibilidad para el Contenido Web (WCAG) 2.1 nivel AA.</p>
  </footer>

</body>
</html>
```

---

### 4. Criterios de Evaluación y Entrega

!!! success "Lista de comprobación (Rúbrica de autoevaluación)"
    - [ ] **Skip link accesible:** El enlace está oculto fuera de pantalla y se visualiza claramente arriba al tabular con el teclado.
    - [ ] **Foco visible:** Se implementa `:focus-visible` con outline visible sin depender del contorno por defecto del navegador.
    - [ ] **`:focus-within`:** La tarjeta `.form-card` reacciona visualmente al enfocar cualquiera de sus campos de formulario.
    - [ ] **Clase `.sr-only`:** Se define correctamente la clase para lectores de pantalla sin usar `display: none`.
    - [ ] **Consultas de accesibilidad:** Se implementa `@media (prefers-reduced-motion: reduce)` para anular animaciones y transiciones.
    - [ ] **Ratios WCAG:** Todos los textos cumplen un contraste mínimo de $4.5:1$ verificado con herramientas de accesibilidad.

---

## Práctica Global 13: Aplicación Web de Alto Rendimiento para Producción (Auditoría Lighthouse 100/100)

!!! info "Objetivo de la práctica"
    Esta práctica culmina el itinerario completo integrando las **Unidades 1 a la 13** y añadiendo la **Unidad 14 (Rendimiento, optimización y buenas prácticas: contención con contain, content-visibility, optimización de selectores, prevención de Layout Thrashing, Core Web Vitals LCP/CLS/INP y auditorías profesionales)**.
    Diseñarás y optimizarás el feed en tiempo real de una plataforma de streaming y medios audiovisuales ("StreamFlow"), garantizando 60 FPS estables al hacer scroll por miles de elementos y superando una auditoría Lighthouse con puntuación perfecta.

### 1. Escenario y Tarea

En la plataforma de streaming **StreamFlow** los usuarios experimentaban lentitud y bloqueos en dispositivos móviles de gama media al desplazarse por el catálogo principal con cientos de reproducciones y listas de canales. Como arquitecto/a Frontend sénior, tu misión es refactorizar y estructurar la hoja de estilos final, implementando **CSS Containment** y **`content-visibility: auto`** para que el navegador únicamente renderice los elementos visibles en el viewport, garantizando un índice CLS igual a 0 y un LCP ultrarrápido.

### 2. Requisitos Técnicos de CSS

1. **Acumulativo Completo (U1 a U13):**
    - Todas las técnicas aprendidas: variables en capas, Flexbox/Grid, transiciones en GPU, accesibilidad y diseño responsivo.
2. **CSS Containment y Renderizado Diferido (Unidad 14):**
    - **Aislamiento de Celdas:** Aplica `contain: layout paint;` en las tarjetas de vídeo `.video-card` para que las modificaciones internas en un elemento no provoquen el recálculo geométrico (*Reflow*) del resto del documento.
    - **Renderizado bajo demanda:** Declara `content-visibility: auto;` y `contain-intrinsic-size: 0 320px;` en los bloques de contenido largo. Esto permite al navegador ignorar por completo el renderizado y pintura de los elementos situados fuera del viewport hasta que el usuario se aproxime a ellos con el scroll, reduciendo el consumo de memoria en un 70%.
3. **Prevención de Saltos de Diseño (CLS < 0.1) (Unidad 14):**
    - Declara de forma obligatoria `aspect-ratio: 16 / 9;` en todos los contenedores de miniaturas multimedia para que el navegador reserve exactamente su altura antes de cargar la imagen.
4. **Optimización de Selectores y Limpieza de Cascada (Unidad 14):**
    - Mantén selectores de especificidad plana de nivel 1 (una sola clase BEM) y evita selectores descendientes universales costosos (como `body *` o `.container div ul li a`).
    - Evita la propiedad `will-change` de forma indiscriminada; aplícala únicamente a elementos que sufran transformaciones continuas durante la interacción.

---

### 3. Código HTML Base Proporcionado

```html title="streamflow.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>StreamFlow — Catálogo de Contenidos en Directo</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <header class="app-header">
    <div class="brand">StreamFlow Live</div>
    <nav class="nav-channels">
      <a href="#" class="active">Siguiendo</a>
      <a href="#">Explorar</a>
      <a href="#">Torneos</a>
    </nav>
  </header>

  <main class="feed-container">
    
    <!-- Hero Streamer Destacado -->
    <section class="featured-stream">
      <div class="featured-stream__media">
        <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=1200&q=80" alt="Gran Final del Campeonato Mundial de eSports">
        <span class="live-badge">EN DIRECTO · 142.500 Espectadores</span>
      </div>
      <div class="featured-stream__info">
        <h2>Gran Final Internacional de eSports — Temporada de Otoño</h2>
        <p>Retransmisión oficial con comentarios tácticos y análisis de datos en tiempo real.</p>
      </div>
    </section>

    <!-- Feed Masivo con Optimización de Rendimiento -->
    <section class="streams-section">
      <h3>Canales Recomendados en tu Región</h3>

      <div class="streams-grid">
        
        <!-- Tarjeta 1 -->
        <article class="video-card">
          <div class="video-card__thumbnail">
            <img src="https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=600&q=80" alt="Partida competitiva de estrategia">
            <span class="duration-pill">4:12:00</span>
          </div>
          <div class="video-card__meta">
            <div class="avatar-channel">TS</div>
            <div class="details">
              <h4>Torneo Clasificatorio Europeo - Ronda 4</h4>
              <p class="channel-name">TacticalStreams</p>
              <p class="viewers-count">18.400 espectadores · Estrategia</p>
            </div>
          </div>
        </article>

        <!-- Tarjeta 2 -->
        <article class="video-card">
          <div class="video-card__thumbnail">
            <img src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=600&q=80" alt="Música Synthwave en directo">
            <span class="duration-pill">2:05:10</span>
          </div>
          <div class="video-card__meta">
            <div class="avatar-channel">NL</div>
            <div class="details">
              <h4>Programación en Rust y Música Synthwave para Concentrarse</h4>
              <p class="channel-name">NightLab Radio</p>
              <p class="viewers-count">6.210 espectadores · Dev & Code</p>
            </div>
          </div>
        </article>

        <!-- Tarjeta 3 -->
        <article class="video-card">
          <div class="video-card__thumbnail">
            <img src="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=600&q=80" alt="Speedrun en directo">
            <span class="duration-pill">1:48:30</span>
          </div>
          <div class="video-card__meta">
            <div class="avatar-channel">SR</div>
            <div class="details">
              <h4>Intento de Récord Mundial Any% sin glitches</h4>
              <p class="channel-name">SpeedRunCentral</p>
              <p class="viewers-count">42.100 espectadores · Speedrun</p>
            </div>
          </div>
        </article>

        <!-- Tarjeta 4 -->
        <article class="video-card">
          <div class="video-card__thumbnail">
            <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=600&q=80" alt="Laboratorio de Hardware">
            <span class="duration-pill">0:55:12</span>
          </div>
          <div class="video-card__meta">
            <div class="avatar-channel">HW</div>
            <div class="details">
              <h4>Montaje y banco de pruebas de refrigeración por inmersión</h4>
              <p class="channel-name">HardwareLabTV</p>
              <p class="viewers-count">9.800 espectadores · Tecnología</p>
            </div>
          </div>
        </article>

      </div>
    </section>

  </main>

  <footer class="app-footer">
    <p>&copy; 2026 StreamFlow Live Media Technologies · Rendimiento optimizado para redes de baja latencia.</p>
  </footer>

</body>
</html>
```

---

### 4. Criterios de Evaluación y Entrega

!!! success "Lista de comprobación (Rúbrica de autoevaluación)"
    - [ ] **CSS Containment:** Se utiliza `contain: layout paint;` en los elementos repetitivos para aislar el árbol de renderizado.
    - [ ] **`content-visibility: auto`:** Se implementa junto con `contain-intrinsic-size` para diferir el renderizado de bloques largos fuera del viewport.
    - [ ] **Prevención de CLS:** Todas las miniaturas tienen un ratio fijo reservado mediante `aspect-ratio: 16 / 9;`.
    - [ ] **Selectores optimizados:** No existen selectores descendientes universales ni cadenas excesivamente anidadas; se respeta la especificidad plana de clases.
    - [ ] **Auditoría Lighthouse:** El sitio obtiene una puntuación de 100/100 en la categoría de Rendimiento y Accesibilidad en Google Chrome DevTools.
