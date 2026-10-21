
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

console.log('Helpers defined successfully');
