## Ejercicios de CSS: El Reto de la Herencia

**Instrucciones:** Analiza los siguientes fragmentos de código y determina cuál será el resultado visual final para el elemento indicado. Justifica tu respuesta basándote en las reglas de herencia y cascada.

---

### Ejercicio 1

**Pregunta:** ¿De qué color se mostrará el texto dentro de la etiqueta `<span>`?

```html
<style>
    body {
        color: blue;
        font-family: Arial;
    }
    .contenedor {
        color: green;
    }
</style>

<body>
    <div class="contenedor">
        <p>Hola, esto es un <span id="objetivo">mensaje de prueba</span>.</p>
    </div>
</body>

```

* **A)** Azul (hereda del body)
* **B)** Verde (hereda del div .contenedor)
* **C)** Negro (color por defecto del navegador)

---

### Ejercicio 2

**Pregunta:** ¿Tendrá el párrafo (`<p>`) un borde rojo a su alrededor?

```html
<style>
    .caja-padre {
        border: 2px solid red;
        padding: 20px;
    }
</style>

<div class="caja-padre">
    <p id="objetivo">¿Tengo yo también un borde rojo?</p>
</div>

```

* **A)** Sí, porque los hijos heredan los bordes de los padres.
* **B)** No, porque `border` no es una propiedad heredable.
* **C)** Solo si el párrafo tiene texto dentro.

---

### Ejercicio 3

**Pregunta:** ¿Qué ancho de borde tendrá el botón?

```html
<style>
    .seccion {
        border: 5px solid black;
    }
    button {
        border: inherit;
    }
</style>

<div class="seccion">
    <button id="objetivo">Heredo por la fuerza</button>
</div>

```

* **A)** El borde por defecto del navegador (gris y fino).
* **B)** Ningún borde (0px).
* **C)** 5px sólido y negro.

---

### Ejercicio 4

**Pregunta:** ¿De qué color se verá el enlace?

```html
<style>
    nav {
        color: red;
    }
</style>

<nav>
    <a href="#" id="objetivo">¿Soy rojo?</a>
</nav>

```

* **A)** Rojo, porque hereda del padre `nav`.
* **B)** Azul, porque el navegador impone su propio estilo a los enlaces.
* **C)** Negro, porque los enlaces no heredan nada.

---

### Ejercicio 5

**Pregunta:** ¿De qué color será finalmente el texto del párrafo?

```html
<style>
    #banner-principal {
        color: orange; /* Selector de ID */
    }
    p {
        color: purple; /* Selector de etiqueta */
    }
</style>

<div id="banner-principal">
    <p id="objetivo">¿Gana la herencia o mi propio estilo?</p>
</div>

```

* **A)** Naranja, porque el ID del padre es un selector muy fuerte.
* **B)** Púrpura, porque un estilo directo al hijo siempre gana a la herencia.
* **C)** Una mezcla de ambos (marrón).




---

## Ejercicio 6 - Refactorización

---

Este es un ejercicio de **refactorización y depuración**, un escenario muy común en el mundo laboral: te entregan un proyecto que "funciona" a medias, pero el código es un desastre porque el desarrollador anterior no entendió cómo funciona la herencia.

### 6.1. El Escenario

La agencia de viajes **"Andalucía Travel"** te ha contratado para arreglar su web. El programador anterior intentó aplicar estilos, pero como no entendía la herencia, el código es repetitivo, difícil de mantener y tiene fallos visuales graves.

### 6.2. El Código "Roto"

Debes crear un archivo `index.html` con este código:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Andalucía Travel - Error de Diseño</title>
    <style>
        /* EL DESASTRE EMPIEZA AQUÍ */

        body {
            font-family: Arial, sans-serif;
            color: #2c3e50;
        }

        /* El programador no sabía que el color se hereda, 
           así que lo puso en cada etiqueta por separado */
        h1 { color: #2c3e50; font-family: Arial, sans-serif; }
        h2 { color: #2c3e50; font-family: Arial, sans-serif; }
        p { color: #2c3e50; font-family: Arial, sans-serif; }

        .card {
            border: 2px solid #27ae60;
            padding: 20px;
            margin: 20px;
            /* Intentó que todo en la tarjeta tuviera borde heredando... 
               ¡pero los bordes no se heredan! */
        }

        /* Error grave: Intentó forzar la herencia de márgenes y bordes 
           en todos los elementos de la tarjeta */
        .card * {
            border: inherit; 
            margin: inherit;
        }

        /* Los enlaces no se ven del color de la marca (#27ae60) */
        a {
            text-decoration: none;
        }
    </style>
</head>
<body>

    <header>
        <h1>Andalucía Travel</h1>
        <nav>
            <a href="#">Inicio</a> | <a href="#">Destinos</a>
        </nav>
    </header>

    <main>
        <section class="card">
            <h2>Visita la Alhambra</h2>
            <p>Disfruta de una experiencia única en Granada con guías oficiales.</p>
            <a href="#">Reservar ahora</a>
        </section>
    </main>

</body>
</html>

```

### 6.3. La misión 

Debes limpiar el código siguiendo estas instrucciones:

1. **Limpieza de redundancias:** Elimina las propiedades `font-family` y `color` de los selectores `h1`, `h2` y `p`. Haz que se hereden correctamente desde el `body`.
2. **Arreglo de la Tarjeta:** Elimina la regla `.card *`. Explica por qué el diseño se rompe cuando intentas que elementos como `h2` o `p` hereden el `border` y el `margin` del padre.
3. **Color de Marca:** Haz que todos los enlaces (`<a>`) hereden el color del texto de su elemento padre de forma automática, sin tener que escribir el código de color hexadecimal otra vez.
4. **Optimización:** El `header` debería tener un color de texto distinto (gris suave `#7f8c8d`). Comprueba que al cambiar el color del `header`, los enlaces dentro de él también cambien solos.

---

### 6.4. Puntos de reflexión:

* **¿Qué pasó con `.card *`?**

* **¿Por qué es mejor `color: inherit` que volver a escribir el hexadecimal?**

---

## Ejercicio 7 - Desafío CSS

Este es un desafío de nivel **profesional**. Está diseñado para que no se pueda resolver simplemente "poniendo parches", sino que hay que analizar profundamente la estructura del DOM y aplicar lógica de selectores avanzados.

El tema del desafío es: **"El Panel de Control de la Estación Espacial Alfa-1"**.

---


**Instrucciones**
Habéis recibido el código HTML de la terminal de una estación espacial. El sistema está en modo de emergencia y el HTML está "bloqueado" (no podéis añadir clases, ni IDs, ni tocar una sola etiqueta).

Vuestra misión es restaurar la interfaz visual utilizando **exclusivamente selectores avanzados de CSS**.

---

### 7.1. El Código HTML (Proporcionado)

Debes guardar esto como `index.html`.

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Terminal de Emergencia Alfa-1</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <header>
        <span>SISTEMA OPERATIVO ALFA</span>
        <h1>Panel de Control de Energía</h1>
    </header>

    <main>
        <section>
            <h2>Estado de los Reactores</h2>
            <p>Reactor principal funcionando al 80%.</p>
            <p>Reactor secundario en modo espera.</p>
            
            <table>
                <thead>
                    <tr>
                        <th>Módulo</th>
                        <th>Estado</th>
                        <th>Carga</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Propulsores</td>
                        <td>Activo</td>
                        <td>45%</td>
                    </tr>
                    <tr>
                        <td>Soporte Vital</td>
                        <td>CRÍTICO</td>
                        <td>12%</td>
                    </tr>
                    <tr>
                        <td>Escudos</td>
                        <td>Inactivo</td>
                        <td>0%</td>
                    </tr>
                    <tr>
                        <td>Comunicaciones</td>
                        <td>Activo</td>
                        <td>90%</td>
                    </tr>
                </tbody>
            </table>
        </section>

        <section>
            <h2>Protocolos de Seguridad</h2>
            <p>Revisar los siguientes documentos antes de proceder:</p>
            <ul>
                <li><a href="manual_v1.html">Manual de usuario</a></li>
                <li><a href="seguridad_extrema.pdf">Protocolo de evacuación (PDF)</a></li>
                <li><a href="https://agencia-espacial.com/login">Acceso externo seguro</a></li>
                <li><a href="http://archivo-viejo.log">Logs antiguos (No seguros)</a></li>
            </ul>

            <form>
                <div>
                    <input type="checkbox" id="p1" name="protocolo-oxigeno" checked>
                    <label for="p1">Oxígeno presurizado</label>
                </div>
                <div>
                    <input type="checkbox" id="p2" name="secret-code-check">
                    <label for="p2">Código de autodestrucción</label>
                </div>
                <input type="text" name="user-secret-id" placeholder="ID de Comandante">
            </form>
        </section>
    </main>

    <aside>
        <ul>
            <li>Notificaciones: 5</li>
            <li>Alertas: 2</li>
        </ul>
        <ul>
            <li>Oxígeno: OK</li>
            <li>Gravedad: 1G</li>
            <li>Combustible: BAJO</li>
        </ul>
    </aside>

</body>
</html>

```

---

### 7.2. Los 8 objetivos del desafío

1. **Identificador de Sistema:** El `<span>` que está dentro del `header` es el único hijo de su tipo. Haz que sea de color naranja, negrita, y que después del texto aparezca automáticamente la palabra "(OFICIAL)".
2. **Reactores Críticos:** En la tabla, localiza la fila que contiene el estado "CRÍTICO" y haz que toda esa fila tenga el fondo rojo y el texto blanco.
3. **Cebra de Datos:** Haz que las filas **pares** de la tabla tengan un fondo gris muy suave, pero no afectes al encabezado (`thead`).
4. **Documentos Seguros:** Busca los enlaces que apunten a una dirección segura (que empiece por `https`) y ponles un color verde. A los que terminen en `.pdf`, añade un icono de aviso 📄 (puedes usar el emoji) antes del texto.
5. **Advertencia de Seguridad:** El enlace que utiliza un protocolo no seguro (`http`) debe aparecer con el texto tachado y en color gris.
6. **Formulario Dinámico:** Cuando un `checkbox` esté marcado (`checked`), el `label` que le sigue inmediatamente debe ponerse en negrita y color azul.
7. **Acceso de Comandante:** El campo de texto (`input`) cuyo nombre contenga la palabra "secret" debe tener un borde rojo brillante cuando el usuario haga clic en él (`focus`).
8. **Navegación Lateral:** En el `aside`, hay dos listas. Selecciona **solo la segunda lista** y haz que el **último elemento** sea de color rojo y parpadee (opcional lo del parpadeo, pero que sea distinto).

---

![Solucion desafío 8 objetivos](assets/images/CSS-solucion-ejercicio7.png)

---

## Ejercicio 8 - La calculadora de especificidad

**Instruccioness:**
Imagina que la especificidad es un marcador de 3 dígitos: **(IDs, Clases, Etiquetas)**.

* Un ID vale 100 puntos `(1, 0, 0)`.
* Una clase, atributo o pseudo-clase vale 10 puntos `(0, 1, 0)`.
* Una etiqueta o pseudo-elemento vale 1 punto `(0, 0, 1)`.
* El selector universal `*` vale 0 puntos `(0, 0, 0)`.

En cada "Round", un mismo elemento HTML está siendo atacado por varios selectores CSS que quieren cambiar su color. Tu misión es:

1. Calcular los puntos de cada selector.
2. Declarar al ganador (qué color se verá en pantalla).

---

### 8.1. El Calentamiento

**El HTML:** `<h2 class="titulo">Bienvenidos</h2>`

**Los contendientes (CSS):**

* **Opción A:** `h2 { color: blue; }`
* **Opción B:** `.titulo { color: red; }`
* **Opción C:** `* { color: green; }`

**Calcula y responde:** ¿Qué color gana y con cuántos puntos?

---

### 8.2. Cantidad vs. Calidad

**El HTML:** 

```HTML
<div id="cabecera">
    <ul class="menu">
        <li>
            <a href="#">Inicio</a>
        </li>
    </ul>
</div>
```

**Los contendientes (CSS):**

* **Opción A:** `div ul li a { color: orange; }`
* **Opción B:** `.menu a { color: purple; }`

**Calcula y responde:** ¿Qué color gana y con cuántos puntos?

---

### 8.3. El Peso Pesado

**El HTML:** `<button id="btn-enviar" class="boton primario">Enviar</button>`

**Los contendientes (CSS):**

* **Opción A:** `button.boton.primario { background-color: black; }`
* **Opción B:** `#btn-enviar { background-color: white; }`

**Calcula y responde:** ¿Qué color gana y con cuántos puntos?

---

### 8.4. El Empate Técnico

**El HTML:** `<p class="alerta error">Contraseña incorrecta</p>`

**Los contendientes (CSS):**

```css
p.alerta { color: yellow; }
p.error { color: pink; }

```

**Calcula y responde:** ¿Qué color gana y por qué?

---

### 8.5. El Jefe Final (Nivel Profesional)

**El HTML:** 

```HTML
<nav id="navegacion-principal">
    <ul class="lista-enlaces">
        <li class="item">
            <a href="/contacto" class="link-contacto">Contacto</a>
        </li>
    </ul>
</nav>
```

**Los contendientes (CSS):**

* **Opción A:** `#navegacion-principal ul.lista-enlaces li a { color: teal; }`
* **Opción B:** `nav ul li.item a.link-contacto { color: crimson; }`
* **Opción C:** `#navegacion-principal a:hover { color: gold; }` *(Supongamos que el ratón está encima)*

**Calcula y responde:** ¿Qué color gana y con cuántos puntos?

---

## 9. Mini-Proyecto: La tarjeta de perfil social

Este proyecto requiere recrear el perfil de una red social (estilo Twitter/X o LinkedIn). El reto visual está en lograr que la **foto de perfil (avatar) se solape** exactamente entre la imagen de portada y la zona de información.

**Objetivo para los alumnos:** Crear una tarjeta de usuario donde la foto de perfil "rompa" el flujo normal del documento y se posicione flotando entre la portada y el contenido, utilizando `position: relative` y `position: absolute`.

---

### 9.1. El código base (HTML)

Crear un archivo `perfil.html` y pegar esta estructura. Es muy sencilla y semántica.

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Perfil Social - Posicionamiento</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>

    <article class="tarjeta-perfil">
        
        <div class="portada"></div>

        <img src="https://i.pravatar.cc/150?img=47" alt="Foto de perfil" class="avatar">

        <div class="info-usuario">
            <button class="btn-seguir">Seguir</button>
            <h2>Laura Developer</h2>
            <p class="arroba">@laura_code</p>
            <p class="bio">Apasionada del diseño de interfaces, CSS y el café. Construyendo la web del futuro pieza a pieza. ☕✨</p>
        </div>

    </article>

</body>
</html>

```

*(Nota: Se ha usado `pravatar.cc` para generar una foto de perfil aleatoria y rápida).*

---

### 9.2. El reto paso a paso

1. **Dale forma a la tarjeta:** La clase `.tarjeta-perfil` debe tener un ancho fijo (ej. `400px`), fondo blanco, bordes redondeados y una sombra suave para que parezca una tarjeta física. **¡Súper importante!** Debe ser tu ancla de posicionamiento.
2. **Crea la portada:** La clase `.portada` debe tener una altura de `150px`, un color de fondo (o una imagen) y tener los bordes superiores redondeados para encajar en la tarjeta.
3. **El avatar:** Convierte el `.avatar` en un círculo perfecto (usa `width`, `height` y `border-radius`). Ponle un borde blanco grueso para que resalte. Ahora, **sácatelo del flujo normal** y colócalo a la izquierda, solapando justo la línea donde termina la portada y empieza la zona blanca.
4. **Ajusta el contenido:** Como el avatar ha salido del flujo normal, el texto de la `.info-usuario` se habrá subido y estará chocando con el avatar o tapado por él. ¡Arréglalo usando márgenes!
5. **El botón rebelde:** Haz que el `.btn-seguir` flote en la parte superior derecha de la zona blanca, sin importar cuánto texto tenga la biografía.

---

S
