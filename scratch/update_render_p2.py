import re

with open('docs/css/practicas-posicionamiento-flexbox-grid-canvas.md', 'r', encoding='utf-8') as f:
    text = f.read()

old_p2_code = """    const headY = by + 32;
    drawRoundRect(ctx, bx, headY, bw, 46, 0, '#0f172a');
    drawText(ctx, '⚡ DominIA Academy', bx + 20, headY + 28, 'bold 14px system-ui', '#38bdf8');
    drawText(ctx, 'Inicio    Artículos    Lecciones    Recursos', bx + 180, headY + 28, '11px system-ui', '#e2e8f0');

    ctx.font = '16px system-ui'; ctx.fillText('🔔', bx + bw - 40, headY + 28);
    ctx.beginPath(); ctx.arc(bx + bw - 32, headY + 16, 5, 0, Math.PI*2); ctx.fillStyle = '#ef4444'; ctx.fill();"""

new_p2_code = """    const headY = by + 32;
    drawRoundRect(ctx, bx, headY, bw, 46, 0, '#0f172a');
    drawText(ctx, '⚡ DominIA Academy', bx + 20, headY + 28, 'bold 14px system-ui', '#38bdf8');
    drawText(ctx, 'Inicio    Artículos    Lecciones    Recursos', bx + 185, headY + 28, '11px system-ui', '#cbd5e1');

    // Campana de notificaciones con insignia numérica (position: absolute)
    const bellX = bx + bw - 35, bellY = headY + 28;
    ctx.font = '16px system-ui';
    ctx.fillText('🔔', bellX, bellY);
    ctx.beginPath();
    ctx.arc(bellX + 7, bellY - 11, 6, 0, Math.PI * 2);
    ctx.fillStyle = '#ef4444';
    ctx.fill();
    drawText(ctx, '3', bellX + 7, bellY - 8, 'bold 7px system-ui', '#ffffff', 'center');"""

if old_p2_code in text:
    text = text.replace(old_p2_code, new_p2_code)
    print("Replaced header drawing in renderP2!")
else:
    print("Could not find exact old_p2_code, searching with regex")
    pattern = r'(const headY = by \+ 32;.*?ctx\.beginPath\(\); ctx\.arc\(bx \+ bw - 32, headY \+ 16, 5, 0, Math\.PI\*2\); ctx\.fillStyle = \'#ef4444\'; ctx\.fill\(\);)'
    text = re.sub(pattern, new_p2_code, text, flags=re.DOTALL)
    print("Replaced with regex in renderP2!")

# Also fix the annotation in renderP2 so it doesn't overlap the bell
old_annot = "drawAnnotation(ctx, 'position: sticky; top: 0;', bx + bw - 130, headY + 23, bx + bw - 15, headY + 23, '#38bdf8');"
new_annot = "drawAnnotation(ctx, 'position: sticky; top: 0;', bx + bw - 120, headY + 12, bx + bw - 60, headY + 12, '#38bdf8');"
text = text.replace(old_annot, new_annot)

with open('docs/css/practicas-posicionamiento-flexbox-grid-canvas.md', 'w', encoding='utf-8') as f:
    f.write(text)

# Also update scratch/render_all_canvases.js
with open('scratch/render_all_canvases.js', 'r', encoding='utf-8') as f:
    js_text = f.read()

if old_p2_code in js_text:
    js_text = js_text.replace(old_p2_code, new_p2_code)
else:
    pattern = r'(const headY = by \+ 32;.*?ctx\.beginPath\(\); ctx\.arc\(bx \+ bw - 32, headY \+ 16, 5, 0, Math\.PI\*2\); ctx\.fillStyle = \'#ef4444\'; ctx\.fill\(\);)'
    js_text = re.sub(pattern, new_p2_code, js_text, flags=re.DOTALL)

js_text = js_text.replace(old_annot, new_annot)

with open('scratch/render_all_canvases.js', 'w', encoding='utf-8') as f:
    f.write(js_text)

print("Updated scratch/render_all_canvases.js successfully!")
