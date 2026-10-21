
(function() {
  function drawRoundRect(ctx, x, y, w, h, r, fill, stroke, strokeWidth) {
    if (r === undefined) r = 0;
    if (typeof r === 'number') {
      r = { tl: r, tr: r, br: r, bl: r };
    } else if (Array.isArray(r)) {
      r = { tl: r[0] || 0, tr: r[1] || 0, br: r[2] || 0, bl: r[3] || 0 };
    }
    ctx.beginPath();
    ctx.moveTo(x + r.tl, y);
    ctx.lineTo(x + w - r.tr, y);
    ctx.quadraticCurveTo(x + w, y, x + w, y + r.tr);
    ctx.lineTo(x + w, y + h - r.br);
    ctx.quadraticCurveTo(x + w, y + h, x + w - r.br, y + h);
    ctx.lineTo(x + r.bl, y + h);
    ctx.quadraticCurveTo(x, y + h, x, y + h - r.bl);
    ctx.lineTo(x, y + r.tl);
    ctx.quadraticCurveTo(x, y, x + r.tl, y);
    ctx.closePath();
    if (fill) { ctx.fillStyle = fill; ctx.fill(); }
    if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = strokeWidth || 1; ctx.stroke(); }
  }

  function drawText(ctx, text, x, y, font, color, align, baseline) {
    ctx.font = font || '12px system-ui, sans-serif';
    ctx.fillStyle = color || '#0f172a';
    ctx.textAlign = align || 'left';
    ctx.textBaseline = baseline || 'alphabetic';
    ctx.fillText(text, x, y);
  }

  function drawBadge(ctx, text, x, y, bg, color, fontSize, bold) {
    fontSize = fontSize || 11;
    ctx.font = (bold ? 'bold ' : '') + fontSize + 'px system-ui, sans-serif';
    const textWidth = ctx.measureText(text).width;
    const padX = 8;
    const h = fontSize + 8;
    const w = textWidth + padX * 2;
    drawRoundRect(ctx, x, y, w, h, 6, bg);
    drawText(ctx, text, x + padX, y + fontSize + 1, ctx.font, color);
    return w;
  }

  function drawAnnotation(ctx, text, x, y, tx, ty, color) {
    color = color || '#2563eb';
    ctx.save();
    ctx.strokeStyle = color;
    ctx.fillStyle = color;
    ctx.lineWidth = 1.5;
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(tx, ty);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.beginPath();
    ctx.arc(tx, ty, 3, 0, Math.PI * 2);
    ctx.fill();
    ctx.font = '10px monospace';
    ctx.fillStyle = color;
    ctx.textAlign = (x < tx) ? 'right' : 'left';
    ctx.textBaseline = 'middle';
    ctx.fillText(text, (x < tx) ? x - 6 : x + 6, y);
    ctx.restore();
  }

  // PRÁCTICA 1
  function renderP1(ctx, w, h) {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
    ctx.lineWidth = 1;
    for (let x = 0; x < w; x += 30) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke(); }
    for (let y = 0; y < h; y += 30) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke(); }

    const cardW = 310;
    const cardH = 415;
    const cardX = (w - cardW) / 2;
    const cardY = 22;

    drawRoundRect(ctx, cardX, cardY, cardW, cardH, 12, '#ffffff', '#e2e8f0', 1);

    const mediaH = 195;
    const mediaGrad = ctx.createLinearGradient(cardX, cardY, cardX + cardW, cardY + mediaH);
    mediaGrad.addColorStop(0, '#1e293b');
    mediaGrad.addColorStop(1, '#0f172a');
    drawRoundRect(ctx, cardX, cardY, cardW, mediaH, [12, 12, 0, 0], mediaGrad);

    ctx.font = '64px system-ui';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('🎧', cardX + cardW / 2, cardY + mediaH / 2);

    drawBadge(ctx, '-25% HOY', cardX + 12, cardY + 12, '#ef4444', '#ffffff', 10, true);

    const favX = cardX + cardW - 32;
    const favY = cardY + 28;
    ctx.beginPath();
    ctx.arc(favX, favY, 16, 0, Math.PI * 2);
    ctx.fillStyle = '#ffffff';
    ctx.fill();
    ctx.font = '14px system-ui';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('🤍', favX, favY + 1);

    const tipText = 'Añadir a mi lista';
    ctx.font = '10px system-ui';
    const tipW = ctx.measureText(tipText).width + 12;
    const tipX = favX - tipW / 2;
    const tipY = favY - 34;
    drawRoundRect(ctx, tipX, tipY, tipW, 18, 4, '#0f172a');
    drawText(ctx, tipText, favX, tipY + 12, '10px system-ui', '#ffffff', 'center');
    ctx.beginPath();
    ctx.moveTo(favX - 4, tipY + 18);
    ctx.lineTo(favX + 4, tipY + 18);
    ctx.lineTo(favX, tipY + 22);
    ctx.closePath();
    ctx.fillStyle = '#0f172a';
    ctx.fill();

    drawText(ctx, 'AUDIOPRO ELITE', cardX + 16, cardY + 222, 'bold 10px system-ui', '#2563eb');
    drawText(ctx, 'Auriculares Wireless Pro ANC', cardX + 16, cardY + 244, 'bold 14px system-ui', '#0f172a');
    drawText(ctx, '★★★★★', cardX + 16, cardY + 266, '13px system-ui', '#f59e0b');
    drawText(ctx, '(142 valoraciones)', cardX + 75, cardY + 266, '11px system-ui', '#64748b');

    drawText(ctx, '149,99 €', cardX + 16, cardY + 300, 'bold 20px system-ui', '#0f172a');
    drawText(ctx, '199,99 €', cardX + 110, cardY + 300, '12px system-ui', '#94a3b8');
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(cardX + 108, cardY + 296);
    ctx.lineTo(cardX + 155, cardY + 296);
    ctx.stroke();

    drawRoundRect(ctx, cardX + 16, cardY + 348, cardW - 32, 38, 8, '#2563eb');
    drawText(ctx, '🛒 Añadir a la Cesta', cardX + cardW / 2, cardY + 371, 'bold 12px system-ui', '#ffffff', 'center');

    drawAnnotation(ctx, 'position: absolute (top, left)', cardX - 25, cardY + 22, cardX + 12, cardY + 20, '#f87171');
    drawAnnotation(ctx, 'position: absolute (bottom: 100%)', cardX + cardW + 25, cardY + 15, favX, tipY + 9, '#60a5fa');
    drawAnnotation(ctx, 'position: relative (referencia)', cardX - 25, cardY + 105, cardX, cardY + 105, '#34d399');
  }

  // PRÁCTICA 2
  function renderP2(ctx, w, h) {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);

    const bx = 20, by = 15, bw = w - 40, bh = h - 30;
    drawRoundRect(ctx, bx, by, bw, bh, 10, '#f8fafc', '#334155', 1);

    // Barra navegador
    drawRoundRect(ctx, bx, by, bw, 32, [10, 10, 0, 0], '#1e293b');
    ctx.fillStyle = '#ef4444'; ctx.beginPath(); ctx.arc(bx + 16, by + 16, 4, 0, Math.PI*2); ctx.fill();
    ctx.fillStyle = '#f59e0b'; ctx.beginPath(); ctx.arc(bx + 28, by + 16, 4, 0, Math.PI*2); ctx.fill();
    ctx.fillStyle = '#10b981'; ctx.beginPath(); ctx.arc(bx + 40, by + 16, 4, 0, Math.PI*2); ctx.fill();
    drawRoundRect(ctx, bx + 55, by + 7, bw - 110, 18, 4, '#0f172a');
    drawText(ctx, '🔒 https://dominia-academy.com/articulos/posicionamiento', bx + 65, by + 19, '10px monospace', '#94a3b8');

    // Sticky Header
    const headY = by + 32;
    drawRoundRect(ctx, bx, headY, bw, 46, 0, '#0f172a');
    drawText(ctx, '⚡ DominIA Academy', bx + 20, headY + 28, 'bold 14px system-ui', '#38bdf8');
    drawText(ctx, 'Inicio    Artículos    Lecciones    Recursos', bx + 180, headY + 28, '11px system-ui', '#e2e8f0');

    // Bell con badge
    ctx.font = '16px system-ui';
    ctx.fillText('🔔', bx + bw - 40, headY + 28);
    ctx.beginPath(); ctx.arc(bx + bw - 32, headY + 16, 5, 0, Math.PI*2); ctx.fillStyle = '#ef4444'; ctx.fill();

    // Contenido del artículo
    const contY = headY + 60;
    drawText(ctx, 'Guía Maestra: Sticky vs Fixed en CSS', bx + 30, contY + 20, 'bold 18px system-ui', '#0f172a');
    drawText(ctx, 'Aprende la diferencia operativa entre elementos anclados al flujo y fijados a la ventana.', bx + 30, contY + 42, '12px system-ui', '#64748b');

    // Tarjeta 1
    drawRoundRect(ctx, bx + 30, contY + 65, bw / 2 - 40, 130, 8, '#ffffff', '#e2e8f0', 1);
    drawText(ctx, '1. Comportamiento Sticky', bx + 45, contY + 90, 'bold 13px system-ui', '#2563eb');
    drawText(ctx, 'El elemento fluye con el scroll hasta', bx + 45, contY + 112, '11px system-ui', '#475569');
    drawText(ctx, 'alcanzar top: 0, donde queda congelado.', bx + 45, contY + 128, '11px system-ui', '#475569');
    drawText(ctx, 'Requiere que su padre tenga altura.', bx + 45, contY + 144, '11px system-ui', '#475569');
    drawBadge(ctx, 'top: 0; z-index: 100;', bx + 45, contY + 160, '#dbeafe', '#1e40af', 10, true);

    // Tarjeta 2
    drawRoundRect(ctx, bx + bw / 2 + 10, contY + 65, bw / 2 - 40, 130, 8, '#ffffff', '#e2e8f0', 1);
    drawText(ctx, '2. Comportamiento Fixed', bx + bw / 2 + 25, contY + 90, 'bold 13px system-ui', '#ea580c');
    drawText(ctx, 'Se extrae por completo del flujo y se ancla', bx + bw / 2 + 25, contY + 112, '11px system-ui', '#475569');
    drawText(ctx, 'al viewport físico de la pantalla.', bx + bw / 2 + 25, contY + 128, '11px system-ui', '#475569');
    drawText(ctx, 'No se mueve jamás al hacer scroll.', bx + bw / 2 + 25, contY + 144, '11px system-ui', '#475569');
    drawBadge(ctx, 'bottom: 0; z-index: 95;', bx + bw / 2 + 25, contY + 160, '#ffedd5', '#9a3412', 10, true);

    // Scrollbar mockup
    drawRoundRect(ctx, bx + bw - 12, headY + 50, 6, 200, 3, '#cbd5e1');
    drawRoundRect(ctx, bx + bw - 12, headY + 80, 6, 70, 3, '#94a3b8');

    // Botón flotante Volver Arriba (position: fixed)
    const fabX = bx + bw - 45, fabY = by + bh - 100;
    ctx.beginPath(); ctx.arc(fabX, fabY, 20, 0, Math.PI*2); ctx.fillStyle = '#2563eb'; ctx.fill();
    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 16px system-ui'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillText('↑', fabX, fabY);

    // Banner de cookies (position: fixed; bottom: 0)
    const cookH = 55;
    const cookY = by + bh - cookH;
    drawRoundRect(ctx, bx, cookY, bw, cookH, [0, 0, 10, 10], '#1e293b');
    drawText(ctx, '🍪 Utilizamos cookies técnicas para garantizar el funcionamiento del aula.', bx + 20, cookY + 32, '11px system-ui', '#f1f5f9');
    drawRoundRect(ctx, bx + bw - 110, cookY + 15, 90, 26, 6, '#10b981');
    drawText(ctx, 'Aceptar todas', bx + bw - 65, cookY + 31, 'bold 11px system-ui', '#ffffff', 'center');

    // Anotaciones
    drawAnnotation(ctx, 'position: sticky; top: 0;', bx + bw - 130, headY + 23, bx + bw - 15, headY + 23, '#38bdf8');
    drawAnnotation(ctx, 'position: fixed (bottom: 5rem)', fabX - 25, fabY, fabX, fabY, '#60a5fa');
    drawAnnotation(ctx, 'position: fixed (bottom: 0)', bx + 160, cookY + 10, bx + 120, cookY + 25, '#34d399');
  }

  console.log('P1 and P2 defined');
})();
