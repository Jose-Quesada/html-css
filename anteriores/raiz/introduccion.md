# Inicio
## 1. ¿Qué es Angular y cuáles son sus características?

Angular es una plataforma de desarrollo de código abierto liderada por Google. Al estar construida íntegramente con TypeScript, ofrece una estructura robusta y tipada, ideal tanto para prototipos rápidos como para aplicaciones empresariales de gran escala.

### Características principales
**-Arquitectura modular:** Las aplicaciones se construyen uniendo pequeños bloques fundamentales (Componentes, Rutas, Directivas, Servicios, Módulos y Pipes)

**-Plataforma completa:** A diferencia de otras herramientas que solo son librerías de vistas, Angular integra de forma nativa soluciones para enrutamiento, formularios reactivos y peticiones HTTP

**-Multiplataforma:** Permite abarcar no solo web (SPA, SSR, SSG), sino también desarrollo móvil (usando Ionic o NativeScript) y de escritorio (con Electron)

**-Reactivad granular:** Gracias a la introducción de **Signals** (señales), permite actualizaciones de estado rápidas y muy localizadas

**-Arquitectura SPA (Single Page Application):** Olvídate de recargas innecesarias. La aplicación carga una sola vez y el contenido fluye dinámicamente, mejorando la experiencia del usuario.

**-HTML Potenciado:** Angular extiende las capacidades del HTML estándar mediante el uso de interpolación, directivas inteligentes y vinculación de atributos, haciendo que la interfaz sea mucho más expresiva.

**-Modularidad y Carga Diferida (Lazy Loading):** Diseñado para ser eficiente. Solo cargas lo que necesitas cuando lo necesitas, optimizando el rendimiento y la velocidad inicial de la aplicación.

**-Componentización:** Fomenta la creación de piezas de software (componentes) reutilizables y fáciles de mantener.

**-Conectividad Backend:** Facilita la comunicación con servidores a través de una integración nativa y sencilla con APIs de servicios web.

**-SEO y Rendimiento con SSR:** Gracias al Server Side Rendering, Angular permite renderizar el contenido en el servidor, asegurando que los motores de búsqueda indexen tu sitio correctamente antes de que el navegador tome el control.

**-Ecosistema de Calidad:** Incluye herramientas de depuración avanzadas (Angular DevTools) y marcos de pruebas como Karma o Jasmine para garantizar un código libre de errores.

**-Diseño Versátil:** Compatible con las librerías estéticas más populares como Angular Material, Bootstrap (ngBootstrap) o Taiga UI.

### Evolución

Angular no deja de actualizarse para adoptar los mejores paradigmas de programación:

**- Componentes Standalone:** Simplifican el desarrollo al eliminar la obligatoriedad de los módulos.

**- Sintaxis de Control Renovada:** Las nuevas estructuras de control hacen que el código sea mucho más legible, reemplazando las antiguas directivas (ngIf, ngFor) por una sintaxis más limpia.

**- Signals:** Una forma revolucionaria y eficiente de gestionar la reactividad y el estado de los datos, simplificando procesos que antes requerían una lógica compleja con observables.

## 2. Ventajas y Desventajas (vs. otras tecnologías)
Aunque Angular es inmensamente potente, tiene claros puntos fuertes y retos para quienes empiezan:

### Ventajas:
**- Todo incluido y estandarizado:** Provee soluciones propias para casi cualquier necesidad ("Opinionated"). No tienes que decidir qué librería externa usar para enrutamiento o validación de formularios, ya lo trae integrado.

**- Alta escalabilidad y mantenimiento:** Su uso de inyección de dependencias y su organización basada en módulos lo hacen ideal para que millones de desarrolladores mantengan grandes proyectos en equipo.

**- Evolución hacia el rendimiento:** Las versiones recientes (v16 a v21) han mejorado drásticamente la velocidad eliminando la necesidad de librerías como Zone.js (arquitectura Zoneless) y usando Deferrable Views y Control Flow.

### Desventajas:
**- Curva de aprendizaje pronunciada:** Exige entender conceptos avanzados desde el principio, como la inyección de dependencias y, especialmente, flujos de datos asíncronos con Observables y librerías como RxJS. Los operadores como switchMap pueden "asustar al principio".

**- Tamaño y sobrecarga heredada:** Históricamente, el uso de herramientas como Zone.js añadía un peso extra al "bundle" final de la aplicación y ejecutaba verificaciones de cambios ("monkey-patching") más veces de las necesarias, afectando al rendimiento inicial (problema que se está solucionando con el nuevo enfoque Zoneless).

## 3. Instalaciones previas necesarias##
Antes de instalar Angular, necesitas preparar el entorno de tu equipo. Las instalaciones recomendadas son:

- **Node JS:** Fundamental para el ecosistema.

- **Editor de código:** Visual Studio Code (recomendado). Además, deberías instalarle la extensión oficial "Angular Language Service", junto con otras útiles como "Angular Snippets" y "Auto Close Tag".

    - Extensiones recomendadas:
        - [Angular Language Service](https://marketplace.visualstudio.com/items?itemName=Angular.ng-template "Angular Language Service")
        - [Angular Snippets](https://marketplace.visualstudio.com/items?itemName=johnpapa.Angular2 "Angular Snippets")
        - [Angular Schematics](https://marketplace.visualstudio.com/items?itemName=cyrilletuzi.angular-schematics "Angular Schematics")
        - [Angular 2 Inline](https://marketplace.visualstudio.com/items?itemName=natewallace.angular2-inline "Angular 2 Inline")
        - [Auto Close Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-close-tag "Auto Close Tag")
        - [Auto import](https://marketplace.visualstudio.com/items?itemName=steoates.autoimport "Auto import")
        - [Auto Rename Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag "Auto rename tag")
        - [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens "Error Lens")
        - [Paste JSON as Code](https://marketplace.visualstudio.com/items?itemName=quicktype.quicktype "Paste JSON as Code")
        - [Tailwind CSS IntelliSense](hhttps://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss "Tailwind CSS IntelliSense")


- **Otras herramientas recomendadas:** Google Chrome (junto con la extensión "Angular DevTools"), Postman (para probar APIs) y Git.

- **Instalación de Angular CLI** El "Command Line Interface" de Angular se instala desde la terminal (se recomienda ejecutarla como administrador). El comando es:
```
npm install -g @angular/cli
```
Para verificar que todo se ha instalado correctamente, comprueba la versión ejecutando:
```
ng version
```
> Ir a [documentación oficial](https://angular.dev/installation)


## 4. Creación del Proyecto y Arranque Inicial##
**1. Generar el proyecto** Para crear una nueva aplicación desde cero, ejecuta:
```
ng new nombre-del-proyecto
```
Durante este proceso, el CLI te hará unas preguntas:

- Seleccionar formato de estilos: Puedes elegir **"CSS"** u opciones modernas integrando frameworks como **Tailwind**

- Enable Server-Side Rendering (SSR)?: Puedes marcar **"n"** (No) para un arranque más sencillo si harás una web estándar (SPA)

- En cuando la integración de la IA: Seleccinamos la opción por defecto **"none"**

**2. Archivos generados** Este proceso te generará una estructura lista para funcionar. Destacan:

**- angular.json:** El cerebro del proyecto, con las configuraciones globales.

**- package.json:** Maneja tus dependencias.

**- src/:** Directorio principal. Aquí está el main.ts (punto de entrada) y la carpeta **app/** donde programarás los componentes.

**- app.ts** y **app.html**: Constituyen tu primer bloque visual en pantalla


**3. Arrancar el servidor** Accede a la carpeta creada y lanza el servidor de desarrollo:

```
ng serve -o
```

El parámetro -o abrirá automáticamente Google Chrome u otro navegador predeterminado mostrando tu primera aplicación Angular en http://localhost:4200.