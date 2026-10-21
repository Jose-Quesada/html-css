// Engine de renderizado para los 7 lienzos <canvas>
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
    if (fill) {
      ctx.fillStyle = fill;
      ctx.fill();
    }
    if (stroke) {
      ctx.strokeStyle = stroke;
      ctx.lineWidth = strokeWidth || 1;
      ctx.stroke();
    }
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

  // --- PRÁCTICA 1 ---
  function renderP1(ctx, w, h) {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);
    
    // Grid sutil de fondo
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
    ctx.lineWidth = 1;
    for (let x = 0; x < w; x += 30) {
      ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
    }
    for (let y = 0; y < h; y += 30) {
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
    }

    const cardW = 300;
    const cardH = 410;
    const cardX = (w - cardW) / 2;
    const cardY = 25;

    // Tarjeta
    drawRoundRect(ctx, cardX, cardY, cardW, cardH, 12, '#ffffff', '#e2e8f0', 1);

    // Media contenedor (position: relative)
    const mediaH = 190;
    const mediaGrad = ctx.createLinearGradient(cardX, cardY, cardX + cardW, cardY + mediaH);
    mediaGrad.addColorStop(0, '#1e293b');
    mediaGrad.addColorStop(1, '#0f172a');
    drawRoundRect(ctx, cardX, cardY, cardW, mediaH, [12, 12, 0, 0], mediaGrad);

    // Auriculares emoji
    ctx.font = '60px system-ui';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('🎧', cardX + cardW / 2, cardY + mediaH / 2);

    // Insignia descuento (position: absolute; top: 12px; left: 12px;)
    drawBadge(ctx, '-25% HOY', cardX + 12, cardY + 12, '#ef4444', '#ffffff', 10, true);

    // Botón favorito (position: absolute; top: 12px; right: 12px;)
    const favX = cardX + cardW - 36;
    const favY = cardY + 28;
    ctx.beginPath();
    ctx.arc(favX, favY, 16, 0, Math.PI * 2);
    ctx.fillStyle = '#ffffff';
    ctx.fill();
    ctx.font = '14px system-ui';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('🤍', favX, favY + 1);

    // Tooltip sobre el botón favorito (position: absolute; bottom: calc(100% + 6px))
    const tipText = 'Añadir a mi lista';
    ctx.font = '10px system-ui';
    const tipW = ctx.measureText(tipText).width + 12;
    const tipX = favX - tipW / 2;
    const tipY = favY - 34;
    drawRoundRect(ctx, tipX, tipY, tipW, 18, 4, '#0f172a');
    drawText(ctx, tipText, favX, tipY + 12, '10px system-ui', '#ffffff', 'center');
    // Flecha tooltip
    ctx.beginPath();
    ctx.moveTo(favX - 4, tipY + 18);
    ctx.lineTo(favX + 4, tipY + 18);
    ctx.lineTo(favX, tipY + 22);
    ctx.closePath();
    ctx.fillStyle = '#0f172a';
    ctx.fill();

    // Detalles del producto (flujo normal)
    drawText(ctx, 'AUDIOPRO ELITE', cardX + 16, cardY + 215, 'bold 10px system-ui', '#2563eb');
    drawText(ctx, 'Auriculares Wireless Pro ANC', cardX + 16, cardY + 238, 'bold 14px system-ui', '#0f172a');
    drawText(ctx, '★★★★★', cardX + 16, cardY + 260, '13px system-ui', '#f59e0b');
    drawText(ctx, '(142 valoraciones)', cardX + 75, cardY + 260, '11px system-ui', '#64748b');

    // Precios
    drawText(ctx, '149,99 €', cardX + 16, cardY + 295, 'bold 20px system-ui', '#0f172a');
    drawText(ctx, '199,99 €', cardX + 110, cardY + 295, '12px system-ui', '#94a3b8');
    // Tachado
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(cardX + 108, cardY + 291);
    ctx.lineTo(cardX + 155, cardY + 291);
    ctx.stroke();

    // Botón comprar
    drawRoundRect(ctx, cardX + 16, cardY + 345, cardW - 32, 38, 8, '#2563eb');
    drawText(ctx, '🛒 Añadir a la Cesta', cardX + cardW / 2, cardY + 368, 'bold 12px system-ui', '#ffffff', 'center');

    // Anotaciones educativas
    drawAnnotation(ctx, 'position: absolute (top, left)', cardX - 20, cardY + 20, cardX + 12, cardY + 20, '#f87171');
    drawAnnotation(ctx, 'position: absolute (bottom: 100%)', cardX + cardW + 20, cardY + 15, favX, tipY + 9, '#60a5fa');
    drawAnnotation(ctx, 'position: relative (contenedor)', cardX - 20, cardY + 100, cardX, cardY + 100, '#34d399');
  }

  window.renderP1 = renderP1;
  console.log('P1 defined');
})();
