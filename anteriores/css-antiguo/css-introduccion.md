## **¿Qué es CSS y para qué sirve realmente?**

### **1. ¿Qué es CSS?"**

**CSS** (*Cascading Style Sheets* o Hojas de Estilo en Cascada) no es un lenguaje de programación; es un **lenguaje de diseño gráfico** o de estilos.

Su función principal es separar el **qué** (el contenido y la estructura que definimos en HTML) del **cómo** (la apariencia visual). Esta separación es el "santo grial" del desarrollo web profesional, ya que permite cambiar el diseño completo de un sitio web sin tocar ni una sola línea de HTML.

---

### **2. La Metáfora del Desarrollo Web**

Solemos comparar la creación de una web con la construcción de un cuerpo humano o un edificio:

* **HTML (La Estructura):** Es el esqueleto. Define dónde van los órganos, los huesos y la altura. Sin CSS, la web es funcional pero "desnuda" y poco atractiva.
* **CSS (La Presentación):** Es la piel, la ropa, el color de ojos y el peinado. Define si el botón es redondo, si el fondo es verde oliva o si el texto brilla.
* **JavaScript (El Comportamiento):** Son los músculos y el cerebro. Define qué pasa cuando alguien parpadea o corre.

![Imagen comparación HTML vs CSS vs JavaScript](assets/images/CSS-introduccion-html-css-js.jpg)

---

### **3. Anatomía de una Regla CSS**

Es vital recordarles que el CSS funciona mediante "reglas". Una regla le dice al navegador: *"Busca este elemento y aplícale estos cambios"*.

**Sintaxis básica:**

```css
Selector { Propiedad: Valor; }
```

* **Selector:** El "quién". (Ej: todos los `<h1>`).
* **Propiedad:** El "qué". (Ej: el color de fondo).
* **Valor:** El "cuánto". (Ej: azul).

---

### **4. ¿Para qué utilizamos CSS hoy en día?**

Más allá de poner colores bonitos, en el módulo de **Diseño de Interfaces** usamos CSS para:

1. **Diseño Responsivo (Responsive Design):** Hacer que una web se vea bien en un iPhone, en una tablet y en un monitor de 27 pulgadas.
2. **Tipografía:** Controlar la legibilidad, el espaciado entre letras y la carga de fuentes personalizadas.
3. **Layout (Disposición):** Organizar los elementos en columnas, cuadrículas o cajas flexibles (Flexbox y Grid).
4. **Animaciones y Transiciones:** Dar feedback visual al usuario (por ejemplo, que un botón cambie suavemente de color al pasar el ratón).
5. **Accesibilidad:** Asegurar que hay suficiente contraste para que todo el mundo pueda leer el contenido.

---

### **Resumen**

> **HTML construye, CSS embellece.** > Sin CSS, la web sería un documento de Word infinito. Con CSS, la web es una **interfaz de usuario**.

---

¿Te gustaría que prepare una **comparativa visual** (quizás con código) de cómo se ve una misma página HTML con y sin CSS para que se la puedas proyectar el primer día? Es el famoso efecto "desnudar la web" que suele impactar mucho.


¡Excelente elección para empezar con CSS! Es fundamental que el alumnado entienda no solo cómo escribir estilos, sino dónde ubicarlos y qué implicaciones tiene cada decisión en cuanto a **rendimiento, mantenibilidad y la famosa "Cascada"**.

Aquí tienes el material listo en **Markdown** para tus clases de Diseño de Interfaces.

---

# Formas de aplicar CSS en HTML: La Cascada en Acción

El CSS (Cascading Style Sheets) puede integrarse en un documento HTML de varias formas. La elección de una u otra depende de si queremos algo rápido, algo para una sola página o una estructura profesional escalable.

---

## 1. Estilos en Línea (Inline Styles)

Se aplican directamente sobre un elemento HTML usando el atributo `style`.

* **Uso:** `<etiqueta style="propiedad: valor;">`
* **Ejemplo:**
```html
<p style="color: blue; font-size: 18px;">Este texto es azul y grande.</p>

```


* **Pros:** Muy útil para pruebas rápidas o para estilos dinámicos generados por JavaScript.
* **Contras:** **Es la peor práctica para proyectos reales**. Mezcla contenido con diseño, hace que el HTML sea difícil de leer y tiene la prioridad más alta (especificidad), lo que dificulta sobrescribirlo luego.

---

## 2. Estilos Internos o Incrustados (Internal Styles)

Los estilos se escriben dentro de una etiqueta `<style>`, que normalmente se ubica en el `<head>` del documento.

* **Uso:** Dentro de la cabecera del HTML.
* **Ejemplo:**
```html
<head>
    <style>
        body { background-color: #f0f0f0; }
        h1 { color: darkgreen; }
    </style>
</head>

```


* **Pros:** Útil para páginas únicas (como una *landing page*) donde no quieres cargar un archivo extra.
* **Contras:** Si tienes 20 páginas, tendrías que copiar y pegar el código en las 20. Si quieres cambiar un color, ¡tienes que editar 20 archivos!

---

## 3. Estilos Externos (External Styles) - El Estándar

Es la forma profesional de trabajar. Los estilos viven en un archivo separado (con extensión `.css`) y se vinculan al HTML.

* **Uso:** Etiqueta `<link>` en el `<head>`.
* **Ejemplo:**
```html
<head>
    <link rel="stylesheet" href="css/estilos.css">
</head>

```


* **Pros:**
* **Mantenibilidad:** Cambias un archivo y toda la web se actualiza.
* **Caché:** El navegador descarga el CSS una vez y lo guarda, haciendo que el resto de páginas carguen más rápido.
* **Orden:** Separa totalmente el contenido (HTML) del diseño (CSS).



---

## 4. La Regla `@import`

Es una forma de cargar un archivo CSS desde **dentro** de otro archivo CSS o de una etiqueta `<style>`.

* **Uso:** Al principio de un archivo CSS.
* **Ejemplo:**
```css
/* En tu archivo estilos.css */
@import url("tipografias.css");
@import url("colores.css");

body { font-family: 'Open Sans', sans-serif; }

```


* **Pros:** Permite organizar el CSS en módulos (por ejemplo, un archivo para botones, otro para la rejilla).
* **Contras:** **Rendimiento**. El navegador tiene que descargar el primer CSS, leerlo, y luego empezar a descargar los `@import`. Esto puede ralentizar la carga visual de la página.

---

## 5. Shadow DOM (Estilos encapsulados)

Esta es una forma avanzada que tus alumnos verán si llegan a trabajar con **Web Components** o frameworks modernos.

* **Concepto:** Permite que un componente tenga sus propios estilos que no afectan al resto de la página y que no pueden ser afectados por el CSS externo. Es como una "burbuja de estilos" privada.

---

## Resumen de Prioridades (La Cascada)

Si un mismo elemento recibe estilos de las tres formas, ¿cuál gana? El navegador sigue este orden de prioridad (de más importante a menos):

1. **Estilos en línea** (Ganan siempre).
2. **Estilos internos y externos** (Gana el que esté escrito más abajo en el código HTML).
3. **Estilos por defecto del navegador** (Los que pone Chrome o Firefox si no escribes nada).

---

### Tabla Comparativa

| Método | Ubicación | ¿Recomendado? | Impacto en Rendimiento |
| --- | --- | --- | --- |
| **En línea** | Atributo `style` | No (solo pruebas) | Bajo (pero ensucia el código) |
| **Interno** | Etiqueta `<style>` | Solo páginas únicas | Medio (no se cachea) |
| **Externo** | Archivo `.css` | **Sí (Siempre)** | **Óptimo (Cacheable)** |
| **@import** | Dentro de CSS | Con moderación | Lento (bloquea renderizado) |

---

## Ejemplo código sin vs con CSS

Se muestra comparativa visual completa, con el código y las descripciones visuales para observar la transformación radical que CSS aporta a una página web.

Este es un recurso introductorio esencial que ilustra la **separación de preocupaciones** (estructura vs. presentación).

---

## **Paso 1: El Código Común (HTML)**

Utilizaremos el mismo archivo HTML base para ambas comparaciones. Se debe diferenciar el código que define **qué** hay en la página (estructura y contenido), pero no **cómo** se ve.

Crea un archivo llamado `comparativa.html` y pega este código:

=== "HTML"
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comparativa Visual: Con vs. Sin CSS</title>
    </head>
<body>

    <header>
        <h1>Andalucía Tech Hub</h1>
        <p>Centro de Innovación y Desarrollo Web</p>
    </header>

    <nav>
        <ul>
            <li><a href="#">Inicio</a></li>
            <li><a href="#">Cursos</a></li>
            <li><a href="#">Proyectos</a></li>
            <li><a href="#">Contacto</a></li>
        </ul>
    </nav>

    <main>
        <article>
            <h2>Desarrollo de Interfaces Web (DAW)</h2>
            <p>Este módulo profesional se centra en la creación de interfaces web atractivas, accesibles y responsivas, utilizando tecnologías estándar como HTML5 y CSS3.</p>
            <button>Más Información</button>
        </article>
    </main>

    <footer>
        <p>&copy; 2026 Andalucía Tech Hub. Todos los derechos reservados.</p>
    </footer>

</body>
</html>

```

![Visualización del código HTML en el navegador](assets/images/CSS-introduccion-ejemplo-html.png)

---

## **Paso 2: La Página "SIN CSS"**

### El Resultado Visual: "El Esqueleto"

Al abrir `comparativa.html` en cualquier navegador, se verá el contenido en su **estado más puro y "desnudo"**. Es la presentación por defecto del navegador.

#### **Descripción Visual de la Página Sin CSS:**

1. **Fondo y Texto:** Fondo blanco puro, texto negro puro.
2. **Fuentes:** Fuente por defecto (normalmente *Times New Roman* o similar, con serifa).
3. **Encabezados:** El `<h1>` y `<h2>` son simplemente texto más grande y en negrita.
4. **Lista de Navegación (`<nav>`):** Se muestra como una lista con viñetas vertical estándar. No hay ninguna pista visual de que sea un menú de navegación.
5. **Botón:** Es el botón gris y rectangular por defecto del sistema operativo.
6. **Disposición (Layout):** Todo el contenido fluye en una sola columna vertical. No hay márgenes, ni espaciado entre secciones, ni columnas. Los elementos están "pegados" unos a otros.

---

## **Paso 3: El Código CSS Transformador**

Ahora vamos a aplicar el diseño. Crea un archivo llamado `estilos.css` en la misma carpeta que tu HTML y pega este código. Este código define **cómo** se ve la estructura del HTML.

=== "CSS"
```css
/* estilos.css */

/* 1. Estilos Globales: Fondo y Tipografía */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Cambiamos a sans-serif */
    background-color: #f0f2f5; /* Fondo gris muy suave */
    color: #1c1e21; /* Texto casi negro */
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* 2. Cabecera (`<header>`) */
header {
    background-color: #007f5f; /* Verde oliva (Andalucía) */
    color: white;
    width: 100%;
    padding: 40px 0;
    text-align: center;
}

header h1 {
    margin: 0;
    font-size: 2.5em;
}

header p {
    margin: 10px 0 0;
    font-weight: 300;
}

/* 3. Navegación (`<nav>`) */
nav {
    background-color: #ffffff;
    width: 100%;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

nav ul {
    list-style: none; /* Quitamos las viñetas */
    margin: 0;
    padding: 0;
    display: flex; /* Menú horizontal */
    justify-content: center;
}

nav a {
    display: block;
    padding: 15px 25px;
    text-decoration: none; /* Quitamos el subrayado */
    color: #007f5f;
    font-weight: bold;
}

nav a:hover {
    background-color: #e0f2ed; /* Efecto al pasar el ratón */
}

/* 4. Contenido Principal (`<main>`) */
main {
    width: 80%; /* Ancho controlado */
    max-width: 800px;
    margin: 40px 0;
}

article {
    background-color: white;
    padding: 30px;
    border-radius: 8px; /* Esquinas redondeadas */
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

article h2 {
    color: #007f5f;
}

article button {
    background-color: #007f5f;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    font-size: 1em;
    cursor: pointer;
}

/* 5. Pie de Página (`<footer>`) */
footer {
    background-color: #1c1e21;
    color: #ffffff;
    width: 100%;
    padding: 20px 0;
    text-align: center;
    font-size: 0.9em;
}

```

---

## **Paso 4: La Página "CON CSS"**

### El Resultado Visual: "El Diseño Completo"

Para que la transformación tenga efecto, **vuelve a abrir `comparativa.html` y añade esta línea dentro de la etiqueta `<head>**`, justo después de `<title>`:

```html
<link rel="stylesheet" href="estilos.css">

```

Al refrescar la página, los alumnos verán una interfaz web **profesional y diseñada**.

![Visualización del código HTML + CSS en el navegador](assets/images/CSS-introduccion-ejemplo-html-css.png)

#### **Descripción Visual de la Página Con CSS:**

1. **Identidad Visual:** La página tiene una paleta de colores coherente (verde oliva, grises suaves, blanco), dando una identidad visual corporativa.
2. **Tipografía:** Usamos una fuente *sans-serif* moderna, legible y estilizada. Los encabezados tienen colores específicos.
3. **Menú de Navegación (`<nav>`):** La lista vertical se ha transformado en una barra de menú horizontal, centrada y sin subrayado. Los enlaces tienen un efecto visual suave al pasar el ratón (*hover*).
4. **Disposición (`<main>` y `article`):** El contenido principal ya no está pegado a los bordes. Tiene márgenes, un ancho controlado, y el `article` se muestra como una "tarjeta" visual con un fondo blanco, esquinas redondeadas y una sombra suave para darle profundidad.
5. **Botón:** Es un botón estilizado con el color de la marca y texto blanco.
6. **Pie de Página:** Está integrado visualmente como una sección oscura separada en la parte inferior.

---

## **Tabla Resumen de la Comparativa**

| Elemento | Presentación Sin CSS | Presentación Con CSS | Función del CSS Ilustrada |
| --- | --- | --- | --- |
| **Página Completa** | Una columna vertical, pegada al borde. | Diseño estructurado, márgenes, secciones visuales. | **Disposición (Layout)** |
| **Fuentes** | *Serif* por defecto. | *Sans-serif* moderna. | **Tipografía** |
| **Navegación** | Lista vertical con viñetas. | Barra horizontal, centrada, con efectos *hover*. | **Diseño y Estilo** |
| **Colores** | Blanco/Negro por defecto. | Paleta de colores de marca. | **Identidad Visual** |
| **Elementos (ej. botón)** | Botón gris por defecto. | Botón de marca, redondeado, con cursor. | **Estilo de UI** |

---

