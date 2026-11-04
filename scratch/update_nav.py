with open('zensical.toml', 'r', encoding='utf-8') as f:
    text = f.read()

marker = '    { "10. Diseño responsivo" = "css/Código ejemplo/10-diseno-responsivo.md" },\n  ] },\n]'

addition = '''    { "10. Diseño responsivo" = "css/Código ejemplo/10-diseno-responsivo.md" },
  ] },
  { "Librerías de componentes (Tailwind)" = [
    { "00. Introducción y arquitectura" = "librerias-componentes-tailwind/00-introduccion-y-configuracion.md" },
    { "01. Catálogo y tarjetas (Nivel 1)" = "librerias-componentes-tailwind/01-proyecto-tarjeta-catalogo.md" },
    { "02. Portal autenticación (Nivel 2)" = "librerias-componentes-tailwind/02-proyecto-formulario-autenticacion.md" },
    { "03. Dashboard y tablas (Nivel 3)" = "librerias-componentes-tailwind/03-proyecto-dashboard-metricas-tablas.md" },
    { "04. Modales, tabs y FAQ (Nivel 4)" = "librerias-componentes-tailwind/04-proyecto-modales-tabs-acordeon.md" },
    { "05. Plataforma SaaS multitema (Nivel 5)" = "librerias-componentes-tailwind/05-proyecto-saas-layout-multitema.md" },
    { "06. Comparativa técnica y rúbrica" = "librerias-componentes-tailwind/06-comparativa-tecnica-y-guia.md" },
  ] },
]'''

# Normalize line endings
text_normalized = text.replace('\r\n', '\n')
if marker in text_normalized:
    updated = text_normalized.replace(marker, addition, 1)
    with open('zensical.toml', 'w', encoding='utf-8') as f:
        f.write(updated)
    print("SUCCESS")
else:
    print("MARKER NOT FOUND")
    # Let's find where 10-diseno-responsivo.md is
    idx = text_normalized.find('10-diseno-responsivo.md')
    print("idx:", idx)
    if idx != -1:
        print("Surrounding:", repr(text_normalized[idx:idx+100]))
