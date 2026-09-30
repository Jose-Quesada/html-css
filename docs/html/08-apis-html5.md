---
icon: lucide/braces
title: "HTML 08 - APIs y funcionalidades nativas"
description: "Atributos data-*, almacenamiento con localStorage y sessionStorage, Constraint Validation API, geolocation, drag and drop, canvas, fetch y qué NO es HTML5."
modulo: "LMH (0373) / DIW (0615) / DI (0488)"
unidad: 8
fecha: "2026-09-29"
---

# HTML 08 — APIs y funcionalidades nativas

HTML5 no es solo etiquetas: trae un **conjunto de APIs del navegador** que resuelven tareas que antes exigían librerías (guardar datos, validar formularios, obtener la posición, arrastrar, dibujar, pedir datos). Todas se usan "solas", sin instalar nada.

!!! note "Conocimientos previos"

    - Formularios y validación nativa con `required`, `pattern`, `setCustomValidity`: [06-formularios-html5.md](06-formularios-html5.md).
    - JavaScript básico: eventos, funciones y `const`/`let`.
    - Estructura semántica de la página y accesibilidad: [07-estructura-semantica-y-aria.md](07-estructura-semantica-y-aria.md).

## 1. Atributos `data-*`: el puente con JavaScript

### 1.1 Qué son

Cualquier atributo que empiece por ==`data-*`== es válido en HTML5, no lo valida el navegador y **se puede leer desde JS** con `elemento.dataset`. Sirve para pegar datos al marcado sin inventar clases ni atributos a medida.

```html title="ficha.html"
<!-- El estado de la conexión viaja en el propio elemento -->
<article class="ficha" data-estado="borrador" data-id="42" data-fecha="2026-09-29"> <!-- (1)! -->
  <h3>Apuntes de Lenguajes de Marcas</h3>
  <button class="publicar">Publicar</button>
</article>

<script>
const ficha = document.querySelector('.ficha');

// data-estado → dataset.estado (se convierte a camelCase: data-id-unidad → idUnidad)
console.log(ficha.dataset.estado);   // "borrador" <!-- (2)! -->
console.log(ficha.dataset.id);       // "42" (siempre STRING)

ficha.querySelector('.publicar').addEventListener('click', () => {
  ficha.dataset.estado = 'publicado';   // escribe data-estado="publicado"
});
</script>
```

1.  El estado viaja en el propio marcado (`data-estado`, `data-id`, `data-fecha`), sin inventar clases ni atributos a medida.

2.  `dataset` devuelve siempre **texto** (`"42"`, no `42`) y pasa a *camelCase*: `data-id-unidad` → `idUnidad`.

Usos típicos: estado de un componente (`data-abierto`), identificador para una petición (`data-id`), configuración de un gráfico (`data-max`) o preferencias de tema.

## 2. Almacenamiento: cookies, `localStorage` y `sessionStorage`

### 2.1 Comparativa

| | Cookies | `localStorage` | `sessionStorage` |
|---|---|---|---|
| **Duración** | Caducan (hasta ~4000 días, lo decides tú) | Indefinida hasta borrarla | Se borra al cerrar la pestaña/ventana |
| **Tamaño** | ~4 KB por cookie | ~5 MB por origen | ~5 MB por pestaña |
| **Se envía al servidor** | **Sí**, en **cada** petición HTTP | No | No |
| **Alcance** | Dominio + ruta | Pestaña/ventana, todas las del origen | Solo esa pestaña |
| **Usos** | Sesión, idioma, preferencias | Carrito, borradores, caché de datos | Asistente paso a paso, formularios temporales |

!!! info "Qué guarda y quién puede leerlo"

    Las tres guardan **cadenas de texto** por **origen**[^1]: cualquier script de esa misma página puede leerlas y escribirlas. ==`localStorage`== es la que **no caduca**; `sessionStorage` vive solo en su pestaña; las cookies son las únicas que **viajan al servidor**.

### 2.2 API de almacenamiento con JSON

Solo guardan **cadenas de texto**: un objeto hay que convertirlo con `JSON.stringify` y recuperarlo con `JSON.parse`.

```js title="storage.js" hl_lines="3 8"
// Guardar un objeto completo
const perfil = { nombre: 'Marta Ruiz', ciclo: 'DAW', curso: 2, notas: [7, 8, 9] };
localStorage.setItem('perfil', JSON.stringify(perfil));
sessionStorage.setItem('ultimoPaso', '3');

// Recuperarlo y convertirlo otra vez a objeto
try {
  const guardado = JSON.parse(localStorage.getItem('perfil'));
  console.log(guardado.nombre, guardado.notas[0]);
} catch (e) {
  // Clave vacía o contenido corrupto: JSON.parse lanza SyntaxError
  console.warn('No había JSON válido en la clave "perfil"');
}

// Borrar: una clave o todo el origen
localStorage.removeItem('perfil');
localStorage.clear();
```

> **Regla de oro del almacenamiento:** escritura con `JSON.stringify`, lectura con `JSON.parse` dentro de `try/catch`. Guardar el objeto tal cual (`localStorage.setItem('perfil', perfil)`) escribe `[object Object]` y al recargar `JSON.parse` falla.

!!! danger "Nada de datos sensibles"

    **Nada de datos sensibles** (contraseñas, DNI, tarjetas): el almacenamiento es texto plano compartido por cualquier script de la página. Lo abre cualquiera en las herramientas de desarrollo (pestaña *Application*) y también lo lee un XSS.

    - Si el dato es **secreto**, no puede vivir en el cliente: va en el **servidor** (sesión) o en una cookie `HttpOnly`.
    - Aquí solo guardan cosas **reversibles**: preferencias, borradores, carrito, caché.

## 3. Constraint Validation API

### 3.1 Qué ofrece

La validación nativa de los formularios (→ [06-formularios-html5.md](06-formularios-html5.md)) no termina en los atributos: JavaScript puede consultarla y personalizarla.

| Miembro | Qué hace |
|---|---|
| `form.checkValidity()` | `true`/`false` con todo el formulario |
| `input.checkValidity()` | `true`/`false` con un campo |
| `input.validity` | Objeto con el motivo exacto del fallo |
| `input.validationMessage` | Texto que muestra el navegador |
| `input.setCustomValidity('…')` | Mensaje de error **propio** (vacío = sin error) |
| `form.reportValidity()` | Muestra la burbuja de error nativa |

Estados de ==`validity`== que conviene memorizar: `valueMissing` (`required` vacío), `patternMismatch` (no cumple `pattern`), `typeMismatch` (email/url mal formados), `tooLong`, `rangeUnderflow`/`rangeOverflow` (`min`/`max`), `stepMismatch`, `badInput` y, cuando todo va bien, `valid`.

!!! question "Autoevaluación: validación nativa"

    Un campo con `required` está vacío y el formulario no envía. ¿Qué propiedad te dice el motivo exacto y cómo pondrías tú el mensaje de error?

    ??? success "Respuesta"

        El motivo es `input.validity.valueMissing` (aquí vale `true`); tu mensaje se crea con `input.setCustomValidity('El NIF es obligatorio')` y **se borra con cadena vacía** (`setCustomValidity('')`). Para preguntar de un golpe, `form.checkValidity()` devuelve `true`/`false`.

### 3.2 Ejemplo: NIF con mensaje personalizado

```html title="nif.html" hl_lines="3 6"
<form id="alta" novalidate>
  <label for="nif">NIF</label>
  <input id="nif" name="nif" required pattern="\d{8}[A-Za-z]"
         placeholder="12345678Z">
  <button type="submit">Comprobar</button>
  <p id="error" role="alert"></p>
</form>

<script>
const form = document.getElementById('alta');
const nif = document.getElementById('nif');
const error = document.getElementById('error');

// Mensaje propio: el navegador no sabe validar un NIF de verdad
nif.addEventListener('input', () => {
  if (nif.value && nif.validity.patternMismatch) {
    nif.setCustomValidity('Debe tener 8 dígitos seguidos de una letra');
  } else {
    nif.setCustomValidity('');   // vacío = sin error, hay que resetearlo
  }
});

form.addEventListener('submit', (e) => {
  e.preventDefault();
  if (form.checkValidity()) {
    error.textContent = '¡NIF correcto!';
  } else if (nif.validity.valueMissing) {
    error.textContent = 'El NIF es obligatorio';
  } else {
    error.textContent = nif.validationMessage;
  }
});
</script>
```

## 4. Geolocalización

### 4.1 `getCurrentPosition`

```js title="geolocalizacion.js"
if (!navigator.geolocation) {
  alert('Tu navegador no soporta geolocalización');
} else {
  navigator.geolocation.getCurrentPosition(
    (pos) => {
      // coords: latitude, longitude, accuracy (metros), altitude…
      console.log(`${pos.coords.latitude}, ${pos.coords.longitude}`);
    },
    (err) => console.warn(`Error ${err.code}: ${err.message}`),
    { enableHighAccuracy: true, timeout: 8000, maximumAge: 60000 }
  );
}
```

### 4.2 Permisos, seguridad y privacidad

- **Permiso explícito**: el navegador pregunta (permitir / bloquear / recordar). `err.code` 1 = permiso denegado, 2 = no disponible, 3 = *timeout*.
- ==Solo en contextos seguros==: la API **no funciona en `http://`** (sí en `https://` y en `localhost`, que el navegador considera seguro).
- **Privacidad**: se pide en el momento, no en la carga de la página, y conviene explicar **para qué** (p. ej. "mostrar la distancia al centro de estudios"). Alternativa ligera y menos intrusiva: `navigator.geolocation.watchPosition()` solo si realmente necesitas seguimiento.

## 5. Arrastrar y soltar (*drag & drop*) nativo

### 5.1 Eventos y `dataTransfer`

```html title="drag-drop.html"
<ul id="lista">
  <li draggable="true" data-mod="LMH">Lenguajes de marcas</li>
  <li draggable="true" data-mod="DIW">Diseño de interfaces</li>
  <li draggable="true" data-mod="DI">Desarrollo en entorno servidor</li>
</ul>
<div id="zona">Suelta aquí</div>

<script>
const zona = document.getElementById('zona');
let origen = null;

document.querySelectorAll('#lista li').forEach((li) => {
  li.addEventListener('dragstart', (e) => {
    origen = li;
    e.dataTransfer.setData('text/plain', li.textContent);  // datos del arrastre <!-- (1)! -->
    e.dataTransfer.effectAllowed = 'move';
  });
});

zona.addEventListener('dragover', (e) => {
  e.preventDefault();   // SIN ESTO el drop NUNCA se dispara <!-- (2)! -->
});

zona.addEventListener('drop', (e) => {
  e.preventDefault();
  const texto = e.dataTransfer.getData('text/plain');
  zona.textContent = `Has soltado: ${texto}`;
  if (origen) origen.remove();
});
</script>
```

1.  `dragstart` escribe en `dataTransfer` los datos del arrastre y guarda el elemento de origen: ahí solo se puede **meter** información.

2.  En `dragover` hace falta `preventDefault()`; sin él, el navegador cree que vas a soltar en otra aplicación y **`drop` no se dispara nunca**.

Orden de los eventos: **`dragstart` → `drag` → `dragenter` → `dragover` → `drop` → `dragend`**. El elemento arrastrado **no** recibe `drop` por sí solo: hay que hacer `preventDefault()` en ==`dragover`==.

!!! warning "Error común"

    Olvidar `e.preventDefault()` dentro de **`dragover`**: sin él, el navegador asume que vas a dejar caer el archivo en otra aplicación y el evento `drop` no se ejecuta nunca. El segundo fallo típico es intentar probarlo con el dedo: **la DnD nativa no funciona en pantallas táctiles**. Para móvil se usan **Pointer Events** (`pointerdown`/`pointermove`/`pointerup`), que unifican ratón, lápiz y dedo, o el HTML5 Drag and Drop con una librería.

### 5.2 Límites y alternativas modernas

- Táctil: no soportado (ver aviso anterior).
- Accesibilidad: arrastrar es imposible con teclado; si el orden importa, añade botones "subir/bajar".
- Alternativas: Pointer Events, `addEventListener` con eventos `pointer*`, o patrones de lista con teclado.

## 6. Canvas y SVG

### 6.1 `<canvas>`: lienzo de mapa de bits

```html title="canvas.html"
<canvas id="lienzo" width="400" height="200">
  Tu navegador no soporta canvas.
</canvas>

<script>
// getContext('2d') devuelve el contexto de dibujo; sin JS, el canvas está vacío
const ctx = document.getElementById('lienzo').getContext('2d');

ctx.fillStyle = '#0b5fff';
ctx.fillRect(20, 20, 120, 60);              // rectángulo

ctx.fillStyle = '#fff';
ctx.font = '18px sans-serif';
ctx.fillText('Hola, canvas', 30, 55);       // texto

ctx.strokeStyle = '#333';
ctx.lineWidth = 3;
ctx.beginPath();                            // líneas
ctx.moveTo(20, 120);
ctx.lineTo(380, 120);
ctx.stroke();
</script>
```

Claves: es un **bitmap** (píxeles; al escalar con CSS se pixela), su contenido ==se pierde al recargar== y **no existe sin JavaScript**. Se usa para gráficos, juegos, visualizaciones y efectos en tiempo real. El ejercicio de vídeo/canvas de los apuntes (`drawImage` sobre fotogramas) está en [09-ejercicios.md](09-ejercicios.md) y su sección teórica en los apuntes de elementos.

### 6.2 SVG como alternativa vectorial

SVG describe el dibujo con **XML** (caminos, círculos, texto): escala sin pixelarse, se puede dar estilo con CSS y es seleccionable y accesible. Regla rápida: **bitmap + movimiento + muchos píxeles → canvas; formas nítidas, iconos y gráficos interactivos → SVG**. Rutas y enlaces de descarga en [03-enlaces-y-recursos.md](03-enlaces-y-recursos.md).

## 7. El ecosistema JavaScript que acompaña

### 7.1 Tres APIs que sí usas a diario

```js title="fetch.js" hl_lines="2 4"
// Fetch: peticiones HTTP modernas, dentro de una función async (sustituye a XMLHttpRequest)
const respuesta = await fetch('/api/notas.json');
if (!respuesta.ok) throw new Error('HTTP ' + respuesta.status);
const notas = await respuesta.json();   // ya es objeto, sin parsear a mano
console.log(notas);
```

- **Web Workers**: ejecutan JavaScript en un ==hilo aparte== para no bloquear la interfaz (procesado, cálculos pesados); no pueden tocar el DOM directamente.
- **IntersectionObserver**: avisa cuando un elemento **entra o sale del viewport**; es lo que usan el *lazy loading* y las animaciones al hacer scroll.

### 7.2 ¿Qué NO es HTML5? (mitos)

| Se dice | En realidad |
|---|---|
| "HTML5 = todo el stack moderno" | HTML5 es el **lenguaje de marcado**; CSS y JavaScript son especificaciones aparte |
| "localStorage, Fetch y Workers son HTML5" | Son APIs del **navegador** (WHATWG) que conviven con HTML5 |
| "React, Vue o Angular son HTML5" | Son **librerías/frameworks** de JavaScript |
| "HTML5 sustituye al backend" | Solo cubre el cliente; seguirás necesitando servidor y base de datos |

## 8. Ejemplo práctico: mini app de notas

```html title="notas.html"
<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"><title>Notas</title></head>
<body>
  <h1>Mis notas</h1>

  <form id="formNota">
    <label for="texto">Nueva nota</label>
    <input id="texto" name="texto" required maxlength="80">
    <button type="submit">Añadir</button>
  </form>

  <ul id="listaNotas"></ul>

  <script>
    const CLAVE = 'mis-notas';
    const form = document.getElementById('formNota');
    const texto = document.getElementById('texto');
    const lista = document.getElementById('listaNotas');

    // Leer: siempre con JSON.parse dentro de try/catch <!-- (1)! -->
    const leer = () => {
      try { return JSON.parse(localStorage.getItem(CLAVE)) || []; }
      catch { return []; }
    };

    const pintar = () => {
      const notas = leer();
      lista.innerHTML = notas.map((n, i) =>
        `<li>${n} <button data-i="${i}">✕</button></li>`).join('');
    };

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const notas = leer();
      notas.push(texto.value.trim());
      localStorage.setItem(CLAVE, JSON.stringify(notas));  // guardar: stringify <!-- (2)! -->
      texto.value = '';
      pintar();
    });

    lista.addEventListener('click', (e) => {
      if (e.target.tagName !== 'BUTTON') return;
      const notas = leer();
      notas.splice(Number(e.target.dataset.i), 1);
      localStorage.setItem(CLAVE, JSON.stringify(notas));
      pintar();
    });

    pintar();
  </script>
</body>
</html>
```

1.  Lectura defensiva: `JSON.parse` dentro de `try` devuelve `[]` cuando la clave no existe o está corrupta.

2.  Escritura con `JSON.stringify`: guardas un **array**, no su representación `[object Object]`.

!!! success "Antes de usar storage"

    - [ ] ¿El dato es **no sensible**? Nada de contraseñas, DNI ni tarjetas.
    - [ ] ¿Escribo con `JSON.stringify` y leo con `JSON.parse` dentro de `try/catch`?
    - [ ] ¿Contemplo el **primer uso**, con la clave todavía vacía (`[]` o `{}`)?
    - [ ] ¿Distingo `localStorage` (permanente) de `sessionStorage` (se borra al cerrar la pestaña)?
    - [ ] ¿Compruebo la cuota y capturo `QuotaExceededError` si el volumen puede crecer?

??? note "Para saber más: cuando el storage se queda pequeño"

    Los ~5 MB bastan para preferencias y borradores, pero no para imágenes o colecciones grandes. La opción nativa es **IndexedDB** (base de datos asíncrona en el navegador) y, si solo necesitas cachear peticiones, la **Cache API** junto a *service workers*.

## 9. Errores frecuentes y claves para el examen

!!! warning "Error común"

    Los dos fallos que más se corrigen en la práctica:
    - **Guardar un objeto en storage sin `JSON.stringify`**: se escribe `[object Object]` y al recargar `JSON.parse` revienta. Escribe con `JSON.stringify` y lee con `JSON.parse` en un `try`.
    - **Probar la geolocalización en `http://`**: la API no se activa (solo `https://` y `localhost`), y además hay que conceder el permiso. Comprueba siempre `navigator.geolocation` antes de usarla.

!!! tip "Claves para el examen"

    - `data-*` es **válido en HTML5** y se lee por `elemento.dataset` (camelCase: `data-id-unidad` → `idUnidad`); siempre devuelve **texto**.
    - `localStorage` (~5 MB, **indefinido**, no viaja al servidor), `sessionStorage` (se borra al cerrar la pestaña), cookies (~4 KB, **sí viajan en cada petición**).
    - Storage solo guarda **cadenas**: `JSON.stringify` al guardar, `JSON.parse` + `try/catch` al leer. **Nada de datos sensibles**.
    - **Constraint Validation API**: `checkValidity()` (booleano), `validity.valueMissing` / `patternMismatch` (motivo), `setCustomValidity('')` para **borrar** un error propio.
    - `getCurrentPosition` necesita **permiso** y **HTTPS** (no en `http://`); errores: 1 permiso, 2 no disponible, 3 *timeout*.
    - Drag & drop: `draggable="true"`, `dragstart` (carga `dataTransfer`), **`dragover` + `preventDefault()`** (obligatorio) y `drop`; no funciona con dedo → **Pointer Events**.
    - `<canvas>` = **bitmap** con JS (se pierde al recargar); **SVG** = vectorial y con estilo CSS. Fetch/Workers/IntersectionObserver son APIs del navegador, **no "HTML5"**.

[^1]: Un **origen** es protocolo + dominio + puerto: `https://ejemplo.es` y `http://ejemplo.es` **no** comparten origen, y por eso el almacenamiento no se pasa de un sitio a otro.

*[API]: Application Programming Interface — interfaz que el navegador expone a JavaScript (storage, geolocalización, fetch…).
*[WHATWG]: Web Hypertext Application Technology Working Group — comunidad que mantiene la especificación de HTML y sus APIs.
*[DOM]: Document Object Model — el árbol de objetos que manipula JavaScript; los Web Workers no pueden tocarlo.
