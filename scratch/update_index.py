with open('docs/index.md', 'r', encoding='utf-8') as f:
    text = f.read()

target = """    - **Banco de Práctica:**
      - [15. Ejercicios, glosario y recursos](css/15-ejercicios-glosario-recursos.md) · [15. Soluciones](css/15-ejercicios-soluciones.md) · [16. Prácticas](css/16-practicas.md)

---"""

replacement = """    - **Banco de Práctica:**
      - [15. Ejercicios, glosario y recursos](css/15-ejercicios-glosario-recursos.md) · [15. Soluciones](css/15-ejercicios-soluciones.md) · [16. Prácticas](css/16-practicas.md)

=== "Librerías de Componentes Tailwind (DIW / DI)"

    Siete guías prácticas de desarrollo de interfaces con componentes basados en Tailwind CSS, comparando **DaisyUI 4.x** y **Flowbite 2.x**:

    1. [00. Introducción y arquitectura](librerias-componentes-tailwind/00-introduccion-y-configuracion.md) — Filosofía de diseño, CSS puro vs JS Headless, tokens semánticos y setup.
    2. [01. Catálogo de tarjetas y productos (Nivel 1)](librerias-componentes-tailwind/01-proyecto-tarjeta-catalogo.md) — Anatomía de Cards, badges de oferta, estados de botón y skeletons.
    3. [02. Portal de autenticación y validación (Nivel 2)](librerias-componentes-tailwind/02-proyecto-formulario-autenticacion.md) — Floating labels, inputs accesibles con iconos, toggles y mensajes de error.
    4. [03. Dashboard administrativo con tablas (Nivel 3)](librerias-componentes-tailwind/03-proyecto-dashboard-metricas-tablas.md) — Drawers responsivos, KPIs estadísticos, tablas cebra y paginación.
    5. [04. Centro de soporte, modales y tabs (Nivel 4)](librerias-componentes-tailwind/04-proyecto-modales-tabs-acordeon.md) — Pestañas interactivas, acordeón FAQ y modales accesibles (&lt;dialog&gt; vs JS).
    6. [05. Plataforma SaaS con modo oscuro y multitema (Nivel 5)](librerias-componentes-tailwind/05-proyecto-saas-layout-multitema.md) — App Shell integral, data-theme vs class="dark", avatar groups y timelines.
    7. [06. Guía comparativa, árbol de decisión y rúbrica](librerias-componentes-tailwind/06-comparativa-tecnica-y-guia.md) — Criterios de elección técnica y rúbrica de evaluación curricular.

---"""

text_norm = text.replace('\r\n', '\n')
target_norm = target.replace('\r\n', '\n')
if target_norm in text_norm:
    updated = text_norm.replace(target_norm, replacement.replace('\r\n', '\n'), 1)
    with open('docs/index.md', 'w', encoding='utf-8') as f:
        f.write(updated)
    print("INDEX UPDATED")
else:
    print("TARGET NOT FOUND IN INDEX")
