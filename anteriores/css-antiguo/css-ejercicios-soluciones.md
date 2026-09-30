##  Ejercicios herencia 

### 1. **Ejercicio 1: B (Verde).** 
El `span` busca a su padre más cercano (`p`), el cual no tiene estilo propio y hereda de su padre (`.contenedor`). La herencia se transmite por proximidad en el árbol DOM.

### 2. **Ejercicio 2: B (No).** 
El `border` es una propiedad de caja/modelo de contenedor. Estas propiedades no se heredan por defecto para evitar el caos visual de replicar bordes y márgenes infinitamente.

### 3. **Ejercicio 3: C (5px negro).** 
Aunque `border` no se hereda de forma natural, la palabra clave `inherit` obliga al navegador a copiar el valor exacto del padre.

### 4. **Ejercicio 4: B (Azul).** 
Es un caso "trampa" común. Los navegadores tienen una hoja de estilos interna (*User Agent Stylesheet*) que da color azul a los `<a>`. Al ser un estilo directo del navegador, anula la herencia del padre. Para que sea rojo, habría que usar `color: inherit;` en el `<a>`.

### 5. **Ejercicio 5: B (Púrpura).** 
La herencia es la regla más débil de todas. Cualquier selector que apunte directamente al elemento (aunque sea un simple selector de etiqueta `p`) ganará siempre a un valor heredado, incluso si el padre tiene un ID.

## 6. **Ejercicio refactorización**

Solución Esperada

El código CSS limpio y profesional debería quedar así:

```css
/* 1. Definimos lo global en el body. Gracias a la herencia, 
      h1, h2, p y demás lo tomarán automáticamente. */
body {
    font-family: Arial, sans-serif;
    color: #2c3e50;
}

/* 2. El header tiene su propio color, que heredarán sus hijos */
header {
    color: #7f8c8d;
}

/* 3. Forzamos a los enlaces a que dejen de usar el azul del navegador 
      y miren el color de su padre (herencia forzada) */
a {
    color: inherit;
    text-decoration: none;
}

/* 4. La tarjeta solo define sus propias reglas de caja. 
      No intentamos que los hijos hereden bordes. */
.card {
    border: 2px solid #27ae60;
    padding: 20px;
    margin: 20px;
}

/* 5. Si queremos un color de marca para el título de la tarjeta, 
      lo ponemos aquí. */
.card h2 {
    color: #27ae60;
}

```

Puntos de reflexión para debatir en clase:

* **¿Qué pasó con `.card *`?** (Respuesta: Al usar `border: inherit`, cada `h2` y cada `p` dibujaron su propio borde de 2px, creando un efecto de "cajas dentro de cajas" horrible).
* **¿Por qué es mejor `color: inherit` que volver a escribir el hexadecimal?** (Respuesta: Si el cliente decide cambiar el color de la marca, solo tienes que cambiarlo en un sitio en lugar de buscar todos los enlaces).

## 7. Ejercicio desafío CSS

Guía de ayuda: Errores comunes

    1. "El naranja del header no aparece"
El error: El alumno ha usado span:only-child.

La explicación: :only-child es extremadamente estricto. Si el span tiene un hermano (como el h1), ya no es "hijo único".

La pista para el alumno: "¿Seguro que ese span está solo en su casa o tiene un hermano viviendo con él? Busca un selector que solo cuente a los de su misma especie."

    2. "La fila roja se ve gris o el texto no se lee"
El error: Conflicto de cascada entre :nth-child(even) y :nth-child(2).

La explicación: Como la fila 2 es par, si la regla de los pares está escrita después en el CSS, el fondo gris sobrescribirá al rojo. Además, si no definen el color dentro de la regla del fondo, heredarán el blanco del body y no se verá sobre el fondo claro.

La pista para el alumno: "El CSS se lee de arriba a abajo. Si dos reglas se pelean por el mismo elemento, ¿quién gana? Revisa el orden de tus selectores o haz que el del reactor sea 'más fuerte'."

    3. "El icono del PDF aparece en todos los enlaces"
El error: El alumno ha usado un selector de atributo simple a[href] o ha olvidado el símbolo de "termina en" ($).

La explicación: Sin el $, el navegador no sabe que debe buscar la extensión al final de la cadena.

La pista para el alumno: "Estás marcando todos los archivos, pero solo queremos los que terminan en .pdf. ¿Qué símbolo de selector de atributo servía para mirar el final de una palabra?"

    4. "Al marcar el checkbox no pasa nada"
El error: Uso incorrecto del combinador. Muchos intentarán usar input:checked label (descendiente) en lugar de input:checked + label (hermano adyacente).

La explicación: El label no está dentro del input, está al lado.

La pista para el alumno: "Mira el HTML. ¿El label es un hijo del input o es su vecino? Los vecinos se seleccionan con el símbolo de la suma."

    5. "La animación de parpadeo no funciona"
El error: Olvidar la propiedad content en un pseudo-elemento o no definir los @keyframes.

La explicación: Sin @keyframes, la propiedad animation no tiene instrucciones de qué hacer.

La pista para el alumno: "Has nombrado la animación, pero no le has dado la hoja de ruta. ¿Dónde están definidos los pasos (0%, 50%, 100%) de ese parpadeo?"

    6. "He seleccionado la lista del Aside pero cambian las dos"
El error: Usar aside ul a secas.

La explicación: Eso selecciona todas las listas. Necesitan usar :nth-of-type(2) para ser precisos.

La pista para el alumno: "Hay dos listas en el panel lateral. Si quieres castigar solo al segundo hermano, tienes que decir su nombre o su posición exacta en la familia."

Archivo `style.css` que resuelve todos los puntos utilizando los selectores más precisos posibles.

```css
/* ======================================================
   ESTILOS DE BASE (Para la estética de Terminal)
   ====================================================== */
body {
    background-color: #1a1a1a;
    color: #ecf0f1; /* Texto blanco/grisáceo por defecto */
    font-family: 'Courier New', Courier, monospace;
    padding: 20px;
    line-height: 1.6;
}

h1, h2 {
    border-bottom: 1px solid #333;
    padding-bottom: 10px;
}

section {
    border: 1px solid #333;
    padding: 20px;
    margin-bottom: 20px;
    background-color: #222;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin-top: 15px;
    background-color: #2c3e50; /* Fondo base para la tabla */
}

th, td {
    border: 1px solid #444;
    padding: 12px;
    text-align: left;
}

/* ======================================================
   SOLUCIÓN DEL DESAFÍO ALFA-1
   ====================================================== */

/* 1. Identificador de Sistema (Uso de :only-of-type) 
   Usamos of-type porque tiene un hermano <h1> */
header span:only-of-type {
    color: #e67e22; /* Naranja */
    font-weight: bold;
}
header span:only-of-type::after {
    content: " (OFICIAL)";
}

/* 2. Cebra de Datos (Filas pares)
   IMPORTANTE: Definimos el fondo Y el color del texto para asegurar contraste */
tbody tr:nth-child(even) {
    background-color: #ecf0f1;
    color: #2c3e50; /* Texto oscuro sobre fondo claro */
}

/* 3. Reactor Crítico (Fila 2)
   La escribimos DESPUÉS de la cebra para que la cascada le dé prioridad,
   o usamos un selector más específico. */
tbody tr:nth-child(2) {
    background-color: #e74c3c !important; /* Rojo emergencia */
    color: white !important;
}

/* 4. Documentos Seguros (Atributos) */
a[href^="https"] {
    color: #2ecc71; /* Verde esmeralda */
    font-weight: bold;
}
a[href$=".pdf"]::before {
    content: "📄 ";
}

/* 5. Advertencia de Seguridad (HTTP no seguro) */
a[href^="http:"] {
    color: #95a5a6;
    text-decoration: line-through;
}

/* 6. Formulario Dinámico (Estado y Hermano adyacente) */
input[type="checkbox"]:checked + label {
    font-weight: bold;
    color: #3498db; /* Azul brillante */
}

/* 7. Acceso de Comandante (Atributo parcial y Focus) */
input[name*="secret"]:focus {
    outline: none;
    border: 2px solid #ff0000;
    box-shadow: 0 0 15px #ff0000;
    background-color: #000;
    color: #ff0000;
}

/* 8. Navegación Lateral (Selectores combinados) */
/* Seleccionamos la segunda lista del aside y su último elemento */
aside ul:nth-of-type(2) li:last-child {
    color: #e74c3c;
    font-weight: bold;
    text-transform: uppercase;
    animation: parpadeo 1s infinite;
}

/* Extra: Animación de parpadeo para el combustible bajo */
@keyframes parpadeo {
    0% { opacity: 1; }
    50% { opacity: 0.3; }
    100% { opacity: 1; }
}

/* Ajuste para inputs generales en modo oscuro */
input[type="text"] {
    background: #333;
    border: 1px solid #555;
    color: white;
    padding: 5px;
    margin-top: 10px;
}

```


---

## 8. Ejercicio especifidad

### **8.1: El Calentamiento**

* A) `h2` = 1 etiqueta ➔ **0-0-1 (1 punto)**.
* B) `.titulo` = 1 clase ➔ **0-1-0 (10 puntos)**.
* C) `*` = Universal ➔ **0-0-0 (0 puntos)**.
* **Ganador:** **Rojo (Opción B)** con 10 puntos.

### **8.2: Cantidad vs. Calidad**

* A) `div ul li a` = 4 etiquetas ➔ **0-0-4 (4 puntos)**.
* B) `.menu a` = 1 clase + 1 etiqueta ➔ **0-1-1 (11 puntos)**.
* **Ganador:** **Púrpura (Opción B)** con 11 puntos. *(Lección: Un montón de etiquetas nunca le ganarán a una sola clase).*

### **8.3: El Peso Pesado**

* A) `button.boton.primario` = 2 clases + 1 etiqueta ➔ **0-2-1 (21 puntos)**.
* B) `#btn-enviar` = 1 ID ➔ **1-0-0 (100 puntos)**.
* **Ganador:** **Blanco (Opción B)** con 100 puntos. *(Lección: El ID es el rey absoluto, no importa cuántas clases le pongas enfrente).*

### **8.4: El Empate Técnico**

* A) `p.alerta` = 1 clase + 1 etiqueta ➔ **0-1-1 (11 puntos)**.
* B) `p.error` = 1 clase + 1 etiqueta ➔ **0-1-1 (11 puntos)**.
* **Ganador:** **Rosa (Opción B)**. *(Lección: Ante un empate matemático de especificidad, siempre gana la regla que esté escrita más abajo en el archivo CSS).*

### **8.5: El Jefe Final**

* A) `#navegacion-principal ul.lista-enlaces li a` = 1 ID + 1 clase + 3 etiquetas ➔ **1-1-3 (113 puntos)**.
* B) `nav ul li.item a.link-contacto` = 2 clases + 4 etiquetas ➔ **0-2-4 (24 puntos)**.
* C) `#navegacion-principal a:hover` = 1 ID + 1 pseudo-clase (`:hover` cuenta como clase) + 1 etiqueta ➔ **1-1-1 (111 puntos)**.
* **Ganador:** **Teal (Verde azulado) (Opción A)** con 113 puntos. *(Lección: A los alumnos les suele despistar el `:hover` pensando que es más fuerte, pero sigue contando como una clase. La Opción A tiene más etiquetas sumando junto al ID y la clase).*

## Ejericio 9

Código resuelto, documentado con el *por qué* de cada propiedad clave.

```css
/* =========================================
   1. ESTILOS BASE
   ========================================= */
body {
    background-color: #e6ecf0; /* Color de fondo típico de redes sociales */
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: flex;
    justify-content: center;
    padding-top: 50px;
    margin: 0;
}

/* =========================================
   2. LA TARJETA (El Ancla)
   ========================================= */
.tarjeta-perfil {
    width: 400px;
    background-color: #ffffff;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    
    /* ¡CRÍTICO! Esto convierte a la tarjeta en el sistema de coordenadas 
       para cualquier elemento hijo que sea 'absolute' */
    position: relative; 
}

/* =========================================
   3. LA PORTADA
   ========================================= */
.portada {
    height: 120px;
    background-color: #3498db; /* Azul corporativo */
    /* Redondeamos solo arriba para que encaje en la tarjeta */
    border-radius: 15px 15px 0 0; 
}

/* =========================================
   4. EL AVATAR (El Hijo Absoluto)
   ========================================= */
.avatar {
    width: 100px;
    height: 100px;
    border-radius: 50%; /* Círculo perfecto */
    border: 4px solid #ffffff; /* Borde blanco para separar de la portada */
    
    /* ¡AQUÍ ESTÁ LA MAGIA! */
    position: absolute; 
    
    /* MATEMÁTICAS CLÁSICAS:
       La portada mide 120px de alto. El avatar mide 100px (+ 8px de bordes = 108px).
       Para que el centro del avatar quede en la línea de la portada:
       Top = Altura Portada (120) - Mitad del Avatar (54) = ~66px. */
    top: 66px; 
    left: 20px; 
}

/* =========================================
   5. LA INFORMACIÓN (Ajustando el Flujo Normal)
   ========================================= */
.info-usuario {
    padding: 20px;
    /* Como el avatar ya NO ocupa espacio (es absolute), el texto subiría de golpe.
       Le damos un margen superior para "hacerle sitio" artificialmente al avatar. */
    margin-top: 40px; 
}

h2 { margin: 0; font-size: 1.4em; color: #14171a; }
.arroba { margin: 2px 0 15px 0; color: #657786; font-size: 0.9em; }
.bio { color: #14171a; font-size: 0.95em; line-height: 1.5; }

/* =========================================
   6. EL BOTÓN (Otro Hijo Absoluto)
   ========================================= */
.btn-seguir {
    /* Lo posicionamos absolutamente dentro de la tarjeta */
    position: absolute;
    top: 135px; /* Justo debajo de la portada */
    right: 20px;
    
    background-color: #ffffff;
    color: #1da1f2;
    border: 1px solid #1da1f2;
    padding: 8px 16px;
    border-radius: 20px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.2s;
}

.btn-seguir:hover {
    background-color: #e8f5fe;
}

```

---

### Conceptos a repasar

Hay dos conceptos de oro:

1. **El problema del fantasma desaparecido:** Cuando le pongan `position: absolute` al avatar, verán que el nombre del usuario se sube y se queda oculto detrás de la foto. Es el momento perfecto para decirles: *"¿Veis? El avatar se ha salido del flujo normal, su espacio físico ya no existe. El texto de abajo ha subido a ocupar ese vacío"*. La solución es el `margin-top` en `.info-usuario` para devolver ese espacio visual.

2. **Las Matemáticas del Solapamiento:** Para dejar la foto clavada exactamente a la mitad de la línea entre el azul y el blanco, enséñales el cálculo: `top` debe ser igual a la altura de la portada menos la mitad de lo que mida la foto. *(Nota: Si hay alumnos más avanzados, puedes enseñarles que hoy en día también se puede usar `transform: translateY(-50%)`, que es la forma moderna de no tener que calcular píxeles)*.

Este proyecto les deja una sensación de haber construido "algo real". Con este conocimiento súper afianzado, el salto a **Flexbox** (donde no tenemos que hacer estas matemáticas manuales para centrar cosas) les parecerá pura gloria.

¿Te gustaría que entremos ya con la introducción a **Flexbox**? Podemos empezar con el concepto de Eje Principal vs. Eje Cruzado.


