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

  // --- PRÁCTICA 1: Tarjeta Comercial (Posicionamiento) ---
  function renderP1(ctx, w, h) {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
    ctx.lineWidth = 1;
    for (let x = 0; x < w; x += 30) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke(); }
    for (let y = 0; y < h; y += 30) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke(); }

    const cardW = 310, cardH = 415, cardX = (w - cardW) / 2, cardY = 22;
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

    const favX = cardX + cardW - 32, favY = cardY + 28;
    ctx.beginPath(); ctx.arc(favX, favY, 16, 0, Math.PI * 2); ctx.fillStyle = '#ffffff'; ctx.fill();
    ctx.font = '14px system-ui'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillText('🤍', favX, favY + 1);

    const tipText = 'Añadir a mi lista';
    ctx.font = '10px system-ui';
    const tipW = ctx.measureText(tipText).width + 12, tipX = favX - tipW / 2, tipY = favY - 34;
    drawRoundRect(ctx, tipX, tipY, tipW, 18, 4, '#0f172a');
    drawText(ctx, tipText, favX, tipY + 12, '10px system-ui', '#ffffff', 'center');
    ctx.beginPath(); ctx.moveTo(favX - 4, tipY + 18); ctx.lineTo(favX + 4, tipY + 18); ctx.lineTo(favX, tipY + 22);
    ctx.closePath(); ctx.fillStyle = '#0f172a'; ctx.fill();

    drawText(ctx, 'AUDIOPRO ELITE', cardX + 16, cardY + 222, 'bold 10px system-ui', '#2563eb');
    drawText(ctx, 'Auriculares Wireless Pro ANC', cardX + 16, cardY + 244, 'bold 14px system-ui', '#0f172a');
    drawText(ctx, '★★★★★', cardX + 16, cardY + 266, '13px system-ui', '#f59e0b');
    drawText(ctx, '(142 valoraciones)', cardX + 75, cardY + 266, '11px system-ui', '#64748b');

    drawText(ctx, '149,99 €', cardX + 16, cardY + 300, 'bold 20px system-ui', '#0f172a');
    drawText(ctx, '199,99 €', cardX + 110, cardY + 300, '12px system-ui', '#94a3b8');
    ctx.strokeStyle = '#94a3b8'; ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(cardX + 108, cardY + 296); ctx.lineTo(cardX + 155, cardY + 296); ctx.stroke();

    drawRoundRect(ctx, cardX + 16, cardY + 348, cardW - 32, 38, 8, '#2563eb');
    drawText(ctx, '🛒 Añadir a la Cesta', cardX + cardW / 2, cardY + 371, 'bold 12px system-ui', '#ffffff', 'center');

    drawAnnotation(ctx, 'position: absolute (top, left)', cardX - 25, cardY + 22, cardX + 12, cardY + 20, '#f87171');
    drawAnnotation(ctx, 'position: absolute (bottom: 100%)', cardX + cardW + 25, cardY + 15, favX, tipY + 9, '#60a5fa');
    drawAnnotation(ctx, 'position: relative (referencia)', cardX - 25, cardY + 105, cardX, cardY + 105, '#34d399');
  }

  // --- PRÁCTICA 2: Sticky vs Fixed ---
  function renderP2(ctx, w, h) {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);

    const bx = 20, by = 15, bw = w - 40, bh = h - 30;
    drawRoundRect(ctx, bx, by, bw, bh, 10, '#f8fafc', '#334155', 1);

    drawRoundRect(ctx, bx, by, bw, 32, [10, 10, 0, 0], '#1e293b');
    ctx.fillStyle = '#ef4444'; ctx.beginPath(); ctx.arc(bx + 16, by + 16, 4, 0, Math.PI*2); ctx.fill();
    ctx.fillStyle = '#f59e0b'; ctx.beginPath(); ctx.arc(bx + 28, by + 16, 4, 0, Math.PI*2); ctx.fill();
    ctx.fillStyle = '#10b981'; ctx.beginPath(); ctx.arc(bx + 40, by + 16, 4, 0, Math.PI*2); ctx.fill();
    drawRoundRect(ctx, bx + 55, by + 7, bw - 110, 18, 4, '#0f172a');
    drawText(ctx, '🔒 https://dominia-academy.com/articulos/posicionamiento', bx + 65, by + 19, '10px monospace', '#94a3b8');

    const headY = by + 32;
    drawRoundRect(ctx, bx, headY, bw, 46, 0, '#0f172a');
    drawText(ctx, '⚡ DominIA Academy', bx + 20, headY + 28, 'bold 14px system-ui', '#38bdf8');
    drawText(ctx, 'Inicio    Artículos    Lecciones    Recursos', bx + 180, headY + 28, '11px system-ui', '#e2e8f0');

    ctx.font = '16px system-ui'; ctx.fillText('🔔', bx + bw - 40, headY + 28);
    ctx.beginPath(); ctx.arc(bx + bw - 32, headY + 16, 5, 0, Math.PI*2); ctx.fillStyle = '#ef4444'; ctx.fill();

    const contY = headY + 60;
    drawText(ctx, 'Guía Maestra: Sticky vs Fixed en CSS', bx + 30, contY + 20, 'bold 18px system-ui', '#0f172a');
    drawText(ctx, 'Aprende la diferencia operativa entre elementos anclados al flujo y fijados a la ventana.', bx + 30, contY + 42, '12px system-ui', '#64748b');

    drawRoundRect(ctx, bx + 30, contY + 65, bw / 2 - 40, 130, 8, '#ffffff', '#e2e8f0', 1);
    drawText(ctx, '1. Comportamiento Sticky', bx + 45, contY + 90, 'bold 13px system-ui', '#2563eb');
    drawText(ctx, 'El elemento fluye con el scroll hasta', bx + 45, contY + 112, '11px system-ui', '#475569');
    drawText(ctx, 'alcanzar top: 0, donde queda congelado.', bx + 45, contY + 128, '11px system-ui', '#475569');
    drawBadge(ctx, 'position: sticky; top: 0;', bx + 45, contY + 155, '#dbeafe', '#1e40af', 10, true);

    drawRoundRect(ctx, bx + bw / 2 + 10, contY + 65, bw / 2 - 40, 130, 8, '#ffffff', '#e2e8f0', 1);
    drawText(ctx, '2. Comportamiento Fixed', bx + bw / 2 + 25, contY + 90, 'bold 13px system-ui', '#ea580c');
    drawText(ctx, 'Se extrae por completo del flujo y se ancla', bx + bw / 2 + 25, contY + 112, '11px system-ui', '#475569');
    drawText(ctx, 'al viewport físico de la pantalla.', bx + bw / 2 + 25, contY + 128, '11px system-ui', '#475569');
    drawBadge(ctx, 'position: fixed; bottom: 0;', bx + bw / 2 + 25, contY + 155, '#ffedd5', '#9a3412', 10, true);

    drawRoundRect(ctx, bx + bw - 12, headY + 50, 6, 200, 3, '#cbd5e1');
    drawRoundRect(ctx, bx + bw - 12, headY + 80, 6, 70, 3, '#94a3b8');

    const fabX = bx + bw - 45, fabY = by + bh - 100;
    ctx.beginPath(); ctx.arc(fabX, fabY, 20, 0, Math.PI*2); ctx.fillStyle = '#2563eb'; ctx.fill();
    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 16px system-ui'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillText('↑', fabX, fabY);

    const cookH = 55, cookY = by + bh - cookH;
    drawRoundRect(ctx, bx, cookY, bw, cookH, [0, 0, 10, 10], '#1e293b');
    drawText(ctx, '🍪 Utilizamos cookies técnicas para garantizar el funcionamiento del aula.', bx + 20, cookY + 32, '11px system-ui', '#f1f5f9');
    drawRoundRect(ctx, bx + bw - 110, cookY + 15, 90, 26, 6, '#10b981');
    drawText(ctx, 'Aceptar todas', bx + bw - 65, cookY + 31, 'bold 11px system-ui', '#ffffff', 'center');

    drawAnnotation(ctx, 'position: sticky; top: 0;', bx + bw - 130, headY + 23, bx + bw - 15, headY + 23, '#38bdf8');
    drawAnnotation(ctx, 'position: fixed (bottom: 5rem)', fabX - 25, fabY, fabX, fabY, '#60a5fa');
    drawAnnotation(ctx, 'position: fixed (bottom: 0)', bx + 160, cookY + 10, bx + 120, cookY + 25, '#34d399');
  }

  // --- PRÁCTICA 3: Ficha de Perfil (Flexbox + Posicionamiento) ---
  function renderP3(ctx, w, h) {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)'; ctx.lineWidth = 1;
    for (let x = 0; x < w; x += 30) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke(); }
    for (let y = 0; y < h; y += 30) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke(); }

    const cardW = 420, cardH = 430, cardX = (w - cardW) / 2, cardY = 25;
    drawRoundRect(ctx, cardX, cardY, cardW, cardH, 14, '#ffffff', '#e2e8f0', 1);

    const bannerH = 95;
    const banGrad = ctx.createLinearGradient(cardX, cardY, cardX + cardW, cardY + bannerH);
    banGrad.addColorStop(0, '#4338ca'); banGrad.addColorStop(1, '#6366f1');
    drawRoundRect(ctx, cardX, cardY, cardW, bannerH, [14, 14, 0, 0], banGrad);

    const avX = cardX + 30, avY = cardY + bannerH - 35, avR = 38;
    ctx.beginPath(); ctx.arc(avX + avR, avY + avR, avR + 4, 0, Math.PI*2); ctx.fillStyle = '#ffffff'; ctx.fill();
    ctx.beginPath(); ctx.arc(avX + avR, avY + avR, avR, 0, Math.PI*2); ctx.fillStyle = '#1e293b'; ctx.fill();
    ctx.font = '36px system-ui'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillText('👩‍💻', avX + avR, avY + avR);

    const dotX = avX + avR * 2 - 6, dotY = avY + avR * 2 - 6;
    ctx.beginPath(); ctx.arc(dotX, dotY, 9, 0, Math.PI*2); ctx.fillStyle = '#ffffff'; ctx.fill();
    ctx.beginPath(); ctx.arc(dotX, dotY, 7, 0, Math.PI*2); ctx.fillStyle = '#10b981'; ctx.fill();

    const infoX = cardX + 125, infoY = cardY + bannerH + 12;
    drawText(ctx, 'Elena Rostova', infoX, infoY, 'bold 17px system-ui', '#0f172a');
    ctx.beginPath(); ctx.arc(infoX + 115, infoY - 5, 8, 0, Math.PI*2); ctx.fillStyle = '#2563eb'; ctx.fill();
    drawText(ctx, '✓', infoX + 115, infoY - 2, 'bold 10px system-ui', '#ffffff', 'center');

    drawText(ctx, 'Senior Frontend Architect & UI Lead', infoX, infoY + 20, 'bold 12px system-ui', '#2563eb');
    drawText(ctx, 'Especialista en Design Systems, accesibilidad web y CSS moderno.', cardX + 25, cardY + 185, '12px system-ui', '#475569');

    const tagY = cardY + 215;
    let currX = cardX + 25;
    const tags = ['CSS Grid', 'Flexbox', 'TypeScript', 'Design Systems', 'A11y'];
    tags.forEach(t => {
      currX += drawBadge(ctx, t, currX, tagY, '#f1f5f9', '#334155', 10, true) + 8;
    });

    const statY = cardY + 265;
    ctx.strokeStyle = '#e2e8f0'; ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(cardX + 20, statY); ctx.lineTo(cardX + cardW - 20, statY); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(cardX + 20, statY + 55); ctx.lineTo(cardX + cardW - 20, statY + 55); ctx.stroke();

    const stats = [
      { val: '1.4k', lbl: 'Seguidores' },
      { val: '42', lbl: 'Proyectos' },
      { val: '99.8%', lbl: 'Feedback' }
    ];
    stats.forEach((s, idx) => {
      const colX = cardX + (cardW / 3) * (idx + 0.5);
      drawText(ctx, s.val, colX, statY + 25, 'bold 15px system-ui', '#0f172a', 'center');
      drawText(ctx, s.lbl, colX, statY + 42, '10px system-ui', '#64748b', 'center');
    });

    const btnY = cardY + 345, btnW = (cardW - 60) / 2;
    drawRoundRect(ctx, cardX + 25, btnY, btnW, 38, 8, '#ffffff', '#cbd5e1', 1.5);
    drawText(ctx, '💬 Enviar Mensaje', cardX + 25 + btnW/2, btnY + 23, 'bold 12px system-ui', '#334155', 'center');

    drawRoundRect(ctx, cardX + 35 + btnW, btnY, btnW, 38, 8, '#2563eb');
    drawText(ctx, '+ Seguir Perfil', cardX + 35 + btnW + btnW/2, btnY + 23, 'bold 12px system-ui', '#ffffff', 'center');

    drawAnnotation(ctx, 'position: absolute (online dot)', cardX - 25, dotY, dotX, dotY, '#34d399');
    drawAnnotation(ctx, 'display: flex; flex-wrap: wrap;', cardX + cardW + 25, tagY + 10, currX - 15, tagY + 10, '#38bdf8');
    drawAnnotation(ctx, 'justify-content: space-around;', cardX + cardW + 25, statY + 28, cardX + cardW - 25, statY + 28, '#818cf8');
  }

  // --- PRÁCTICA 4: Catálogo de Cursos (Grid + Flexbox + Posicionamiento) ---
  function renderP4(ctx, w, h) {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);

    drawText(ctx, 'Catálogo de Formación Especializada', 35, 30, 'bold 16px system-ui', '#ffffff');
    drawText(ctx, 'Cuadrícula CSS Grid con Tarjetas Flexbox y Badges Absolutos', 35, 48, '11px system-ui', '#94a3b8');

    const cardW = 215, cardH = 400, gap = 20, startX = 35, startY = 65;
    const courses = [
      {
        icon: '📐', title: 'CSS Grid & Flexbox Avanzado', badge: 'Nuevo', badgeBg: '#10b981',
        grad: ['#1e3a8a', '#1e1b4b'], hours: '24 Horas',
        desc: 'Domina los modelos de maquetación web modernos sin depender de frameworks externos.',
        teacher: 'Carlos Méndez', price: '49,99 €'
      },
      {
        icon: '🎨', title: 'Design Systems con Tokens', badge: 'Destacado', badgeBg: '#f59e0b',
        ribbon: '★ Bestseller', grad: ['#581c87', '#2e1065'], hours: '36 Horas',
        desc: 'Crea arquitecturas CSS modulares, escalables y mantenibles con tokens semánticos.',
        teacher: 'Sara Connor', price: '69,99 €'
      },
      {
        icon: '⚡', title: 'Animaciones y UI Fluida', badge: 'Práctico', badgeBg: '#3b82f6',
        grad: ['#134e4a', '#042f2e'], hours: '18 Horas',
        desc: 'Microinteracciones de alto impacto visual y optimización de renderizado en 60 FPS.',
        teacher: 'David Valdés', price: '39,99 €'
      }
    ];

    courses.forEach((c, idx) => {
      const cx = startX + idx * (cardW + gap);
      drawRoundRect(ctx, cx, startY, cardW, cardH, 12, '#ffffff', '#e2e8f0', 1);

      const mediaH = 130;
      const gr = ctx.createLinearGradient(cx, startY, cx + cardW, startY + mediaH);
      gr.addColorStop(0, c.grad[0]); gr.addColorStop(1, c.grad[1]);
      drawRoundRect(ctx, cx, startY, cardW, mediaH, [12, 12, 0, 0], gr);

      ctx.font = '40px system-ui'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillText(c.icon, cx + cardW / 2, startY + mediaH / 2);

      drawBadge(ctx, c.badge, cx + 10, startY + 10, c.badgeBg, '#ffffff', 9, true);
      if (c.ribbon) {
        drawBadge(ctx, c.ribbon, cx + cardW - 78, startY + 10, '#d97706', '#ffffff', 9, true);
      }

      drawText(ctx, '⏱ ' + c.hours, cx + 14, startY + mediaH + 20, 'bold 10px system-ui', '#2563eb');
      drawText(ctx, c.title, cx + 14, startY + mediaH + 40, 'bold 13px system-ui', '#0f172a');

      ctx.font = '11px system-ui'; ctx.fillStyle = '#64748b';
      const words = c.desc.split(' ');
      let line = '', lineY = startY + mediaH + 68;
      for (let n = 0; n < words.length; n++) {
        const testLine = line + words[n] + ' ';
        if (ctx.measureText(testLine).width > cardW - 28) {
          ctx.fillText(line, cx + 14, lineY);
          line = words[n] + ' '; lineY += 15;
        } else { line = testLine; }
      }
      ctx.fillText(line, cx + 14, lineY);

      drawText(ctx, '👤 ' + c.teacher, cx + 14, startY + cardH - 60, '11px system-ui', '#475569');

      const footY = startY + cardH - 42;
      ctx.strokeStyle = '#f1f5f9'; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(cx + 12, footY); ctx.lineTo(cx + cardW - 12, footY); ctx.stroke();

      drawText(ctx, c.price, cx + 14, footY + 25, 'bold 15px system-ui', '#0f172a');
      drawRoundRect(ctx, cx + cardW - 90, footY + 10, 78, 26, 6, '#2563eb');
      drawText(ctx, 'Inscribirme', cx + cardW - 51, footY + 25, 'bold 10px system-ui', '#ffffff', 'center');
    });

    drawAnnotation(ctx, 'grid-template-columns: repeat(3, 1fr)', w - 180, 48, startX + cardW * 2 + gap, 65, '#38bdf8');
    drawAnnotation(ctx, 'margin-top: auto; (pie alineado)', w - 170, startY + cardH - 25, startX + cardW * 3 + gap * 2, startY + cardH - 25, '#34d399');
  }

  // --- PRÁCTICA 5: Proyecto TechNova Solutions (Landing Page) ---
  function renderP5(ctx, w, h) {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);

    const bx = 20, by = 15, bw = w - 40, bh = h - 30;
    drawRoundRect(ctx, bx, by, bw, bh, 10, '#f8fafc', '#334155', 1);

    drawRoundRect(ctx, bx, by, bw, 42, [10, 10, 0, 0], '#0f172a');
    drawText(ctx, '💠 TechNova Solutions', bx + 20, by + 26, 'bold 13px system-ui', '#38bdf8');
    drawText(ctx, 'Servicios      Soluciones      Casos      Contacto', bx + 210, by + 26, '11px system-ui', '#cbd5e1');
    drawRoundRect(ctx, bx + bw - 110, by + 9, 95, 24, 6, '#2563eb');
    drawText(ctx, 'Solicitar Demo', bx + bw - 62, by + 24, 'bold 10px system-ui', '#ffffff', 'center');

    const heroY = by + 42, heroH = 175;
    const heroGrad = ctx.createLinearGradient(bx, heroY, bx + bw, heroY + heroH);
    heroGrad.addColorStop(0, '#0f172a'); heroGrad.addColorStop(1, '#1e293b');
    ctx.fillStyle = heroGrad; ctx.fillRect(bx, heroY, bw, heroH);

    drawBadge(ctx, '🚀 ARQUITECTURA DIGITAL 2026', bx + 25, heroY + 22, 'rgba(56, 189, 248, 0.2)', '#38bdf8', 9, true);
    drawText(ctx, 'Infraestructuras Cloud & Frontend', bx + 25, heroY + 62, 'bold 18px system-ui', '#ffffff');
    drawText(ctx, 'de Rendimiento Crítico', bx + 25, heroY + 84, 'bold 18px system-ui', '#38bdf8');
    drawText(ctx, 'Diseñamos plataformas web resilientes y escalables para empresas globales.', bx + 25, heroY + 110, '11px system-ui', '#94a3b8');

    drawRoundRect(ctx, bx + 25, heroY + 128, 110, 30, 6, '#2563eb');
    drawText(ctx, 'Comenzar Ahora', bx + 80, heroY + 147, 'bold 11px system-ui', '#ffffff', 'center');
    drawRoundRect(ctx, bx + 145, heroY + 128, 100, 30, 6, 'transparent', '#475569', 1);
    drawText(ctx, 'Ver Portfolio', bx + 195, heroY + 147, 'bold 11px system-ui', '#cbd5e1', 'center');

    const cardGX = bx + bw - 240, cardGY = heroY + 20, cardGW = 215, cardGH = 135;
    drawRoundRect(ctx, cardGX, cardGY, cardGW, cardGH, 10, '#1e293b', '#334155', 1);
    drawText(ctx, '📊 Estado de Nodos Cloud', cardGX + 15, cardGY + 25, 'bold 11px system-ui', '#ffffff');
    const mBars = [45, 65, 85, 95, 75, 99];
    mBars.forEach((val, i) => {
      drawRoundRect(ctx, cardGX + 15 + i * 32, cardGY + 105 - val * 0.5, 20, val * 0.5, 3, '#38bdf8');
    });
    drawBadge(ctx, '● 99.98% SLA Activo', cardGX + cardGW - 120, cardGY - 10, '#10b981', '#ffffff', 9, true);

    const servY = heroY + heroH + 20;
    drawText(ctx, 'Nuestros Servicios de Consultoría Técnica', bx + 25, servY, 'bold 14px system-ui', '#0f172a');
    
    const sCards = [
      { icon: '☁️', title: 'Cloud Architecture', desc: 'Diseño de nubes híbridas y microservicios con alta disponibilidad.' },
      { icon: '🎨', title: 'Design Systems UI', desc: 'Sistemas atómicos con CSS Tokens y componentes desacoplados.' },
      { icon: '🛡️', title: 'Ciberseguridad Web', desc: 'Auditorías de código y protección conforme a estándares OWASP.' }
    ];
    const sCardW = (bw - 60) / 3;
    sCards.forEach((sc, i) => {
      const scX = bx + 20 + i * (sCardW + 10);
      drawRoundRect(ctx, scX, servY + 15, sCardW, 110, 8, '#ffffff', '#e2e8f0', 1);
      ctx.font = '24px system-ui'; ctx.fillText(sc.icon, scX + 15, servY + 45);
      drawText(ctx, sc.title, scX + 15, servY + 70, 'bold 12px system-ui', '#0f172a');
      drawText(ctx, sc.desc, scX + 15, servY + 90, '10px system-ui', '#64748b');
    });

    const metY = servY + 140;
    drawRoundRect(ctx, bx + 20, metY, bw - 40, 42, 6, '#0f172a');
    const mets = ['500+ Clientes Globales', '15+ Países', '99.9% Uptime Garantizado', '24/7 Soporte N3'];
    mets.forEach((m, idx) => {
      drawText(ctx, m, bx + 30 + idx * ((bw - 40) / 4), metY + 25, 'bold 11px system-ui', '#38bdf8');
    });

    const footY = by + bh - 40;
    drawRoundRect(ctx, bx, footY, bw, 40, [0, 0, 10, 10], '#1e293b');
    drawText(ctx, '© 2026 TechNova Solutions S.L. Todos los derechos reservados.', bx + 20, footY + 24, '10px system-ui', '#94a3b8');
    drawText(ctx, 'Aviso Legal    Privacidad    Cookies', bx + bw - 210, footY + 24, '10px system-ui', '#cbd5e1');

    drawAnnotation(ctx, 'position: sticky; top: 0;', bx + bw - 120, by + 26, bx + bw - 20, by + 26, '#38bdf8');
    drawAnnotation(ctx, 'grid-template-columns: repeat(3, 1fr)', bx + bw - 140, servY + 60, bx + bw - 40, servY + 60, '#10b981');
  }

  // --- PRÁCTICA 6: Proyecto DevPulse Magazine (Portal Editorial) ---
  function renderP6(ctx, w, h) {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);

    const bx = 20, by = 15, bw = w - 40, bh = h - 30;
    drawRoundRect(ctx, bx, by, bw, bh, 10, '#ffffff', '#334155', 1);

    drawRoundRect(ctx, bx, by, bw, 28, [10, 10, 0, 0], '#0f172a');
    drawBadge(ctx, '🔴 EN DIRECTO', bx + 12, by + 5, '#ef4444', '#ffffff', 9, true);
    drawText(ctx, 'W3C aprueba formalmente las especificaciones finales de CSS Grid Nivel 3 y Subgrid.', bx + 115, by + 18, '10px system-ui', '#f1f5f9');

    const mastY = by + 28;
    ctx.strokeStyle = '#0f172a'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(bx + 20, mastY + 12); ctx.lineTo(bx + bw - 20, mastY + 12); ctx.stroke();
    drawText(ctx, 'THE DEVPULSE GAZETTE', bx + bw / 2, mastY + 42, 'bold 26px serif', '#0f172a', 'center');
    drawText(ctx, 'EL DIARIO INTERNACIONAL DE ARQUITECTURA WEB Y DESARROLLO DE INTERFACES', bx + bw / 2, mastY + 58, '9px system-ui', '#64748b', 'center');
    ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(bx + 20, mastY + 66); ctx.lineTo(bx + bw - 20, mastY + 66); ctx.stroke();

    const gridY = mastY + 80;
    const col1W = 340, col2W = 165, col3W = 165, gap = 15;

    const heroH = 165;
    const heroGr = ctx.createLinearGradient(bx + 20, gridY, bx + 20 + col1W, gridY + heroH);
    heroGr.addColorStop(0, '#1e293b'); heroGr.addColorStop(1, '#0f172a');
    drawRoundRect(ctx, bx + 20, gridY, col1W, heroH, 6, heroGr);
    drawBadge(ctx, 'EXCLUSIVA', bx + 30, gridY + 12, '#ea580c', '#ffffff', 9, true);
    ctx.font = '50px system-ui'; ctx.fillText('📰', bx + 20 + col1W / 2, gridY + 85);

    drawText(ctx, 'El Fin del CSS Tradicional: La Revolución Agéntica', bx + 20, gridY + heroH + 22, 'bold 14px serif', '#0f172a');
    drawText(ctx, 'Por Dra. Lucía Aranda • 21 Oct 2026 • 8 min de lectura', bx + 20, gridY + heroH + 38, '10px system-ui', '#64748b');
    drawText(ctx, 'El auge de modelos agénticos autónomos transforma la maquetación en código verificable...', bx + 20, gridY + heroH + 55, '11px system-ui', '#334155');

    const col2X = bx + 20 + col1W + gap;
    drawText(ctx, 'BREVES TÉCNICAS', col2X, gridY + 12, 'bold 11px system-ui', '#2563eb');
    const news2 = [
      { t: 'Subgrid 100% Adoptado', d: 'Compatibilidad universal lograda en todos los navegadores.' },
      { t: 'Container Queries vs Media', d: 'El diseño desacoplado sustituye a los breakpoints globales.' },
      { t: 'CSS @starting-style', d: 'Transiciones de entrada nativas para dialog sin hacks de JS.' }
    ];
    news2.forEach((n, idx) => {
      const ny = gridY + 30 + idx * 75;
      drawRoundRect(ctx, col2X, ny, col2W, 68, 6, '#f8fafc', '#e2e8f0', 1);
      drawText(ctx, n.t, col2X + 10, ny + 20, 'bold 11px system-ui', '#0f172a');
      drawText(ctx, n.d, col2X + 10, ny + 38, '9px system-ui', '#64748b');
    });

    const col3X = col2X + col2W + gap;
    drawRoundRect(ctx, col3X, gridY, col3W, 255, 6, '#f1f5f9', '#e2e8f0', 1);
    drawText(ctx, '🔥 MÁS LEÍDOS HOY', col3X + 12, gridY + 22, 'bold 11px system-ui', '#ea580c');
    const ranks = [
      '1. Guía de z-index sin trampas',
      '2. Flexbox: flex-basis vs width',
      '3. Centrar un div en 2026',
      '4. Grid Areas semánticas'
    ];
    ranks.forEach((r, idx) => {
      drawText(ctx, r, col3X + 12, gridY + 55 + idx * 50, 'bold 10px system-ui', '#0f172a');
      drawText(ctx, '👁 ' + (4200 - idx * 800) + ' lecturas', col3X + 12, gridY + 72 + idx * 50, '9px system-ui', '#64748b');
    });

    const multY = by + bh - 70;
    ctx.strokeStyle = '#e2e8f0'; ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(bx + 20, multY); ctx.lineTo(bx + bw - 20, multY); ctx.stroke();
    drawText(ctx, '🎙️ Podcast #42: Accesibilidad Web Real', bx + 25, multY + 35, 'bold 10px system-ui', '#2563eb');
    drawText(ctx, '🎥 Taller: Retículas Complejas con Subgrid', bx + 270, multY + 35, 'bold 10px system-ui', '#2563eb');
    drawText(ctx, '📊 Infografía: El Box Model Moderno', bx + 510, multY + 35, 'bold 10px system-ui', '#2563eb');

    drawAnnotation(ctx, 'grid-template-columns: 2fr 1fr 1fr', bx + bw - 180, mastY + 42, col2X, gridY, '#2563eb');
  }

  // --- PRÁCTICA 7: Proyecto CloudMatrix Analytics (Dashboard SPA) ---
  function renderP7(ctx, w, h) {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);

    const bx = 20, by = 15, bw = w - 40, bh = h - 30;
    drawRoundRect(ctx, bx, by, bw, bh, 10, '#090d16', '#334155', 1);

    const sideW = 160;
    drawRoundRect(ctx, bx, by, sideW, bh, [10, 0, 0, 10], '#0f172a');
    drawText(ctx, '☁ CloudMatrix', bx + 16, by + 30, 'bold 14px system-ui', '#38bdf8');
    drawText(ctx, 'ENTERPRISE SUITE', bx + 16, by + 44, 'bold 8px system-ui', '#64748b');

    const menu = [
      { i: '📊', t: 'Dashboard', act: true },
      { i: '📈', t: 'Analítica', act: false },
      { i: '👥', t: 'Usuarios', act: false },
      { i: '💳', t: 'Facturación', act: false },
      { i: '⚙️', t: 'Ajustes', act: false }
    ];
    menu.forEach((m, idx) => {
      const my = by + 70 + idx * 40;
      if (m.act) {
        drawRoundRect(ctx, bx + 10, my, sideW - 20, 32, 6, '#2563eb');
        drawText(ctx, m.i + '  ' + m.t, bx + 22, my + 21, 'bold 11px system-ui', '#ffffff');
      } else {
        drawText(ctx, m.i + '  ' + m.t, bx + 22, my + 21, '11px system-ui', '#94a3b8');
      }
    });

    drawRoundRect(ctx, bx + 10, by + bh - 50, sideW - 20, 38, 6, '#1e293b');
    drawText(ctx, 'Carlos Dev', bx + 20, by + bh - 32, 'bold 10px system-ui', '#ffffff');
    drawBadge(ctx, '● Online', bx + 20, by + bh - 24, 'transparent', '#10b981', 8, true);

    const topX = bx + sideW, topW = bw - sideW, topH = 46;
    drawRoundRect(ctx, topX, by, topW, topH, [0, 10, 0, 0], '#0f172a');
    drawText(ctx, 'Dashboard  /  Resumen General de Rendimiento', topX + 20, by + 28, '11px system-ui', '#cbd5e1');

    const bellX = topX + topW - 40, bellY = by + 28;
    ctx.font = '16px system-ui'; ctx.fillText('🔔', bellX, bellY);
    ctx.beginPath(); ctx.arc(bellX + 8, bellY - 12, 5, 0, Math.PI*2); ctx.fillStyle = '#ef4444'; ctx.fill();
    drawText(ctx, '5', bellX + 8, bellY - 9, 'bold 8px system-ui', '#ffffff', 'center');

    const mainX = topX + 20, mainW = topW - 40, kpiY = by + topH + 15;

    const kpis = [
      { t: 'Ingresos Mensuales', v: '128.450 €', d: '+14.2% ↗', col: '#10b981' },
      { t: 'Usuarios Activos', v: '24.320', d: '+8.1% ↗', col: '#10b981' },
      { t: 'Tasa Conversión', v: '3.82%', d: '+1.2% ↗', col: '#10b981' },
      { t: 'Incidencias Abiertas', v: '2', d: '-40% ↘', col: '#ef4444' }
    ];
    const kpiW = (mainW - 30) / 4;
    kpis.forEach((k, idx) => {
      const kx = mainX + idx * (kpiW + 10);
      drawRoundRect(ctx, kx, kpiY, kpiW, 75, 8, '#1e293b', '#334155', 1);
      drawText(ctx, k.t, kx + 12, kpiY + 20, '10px system-ui', '#94a3b8');
      drawText(ctx, k.v, kx + 12, kpiY + 45, 'bold 16px system-ui', '#ffffff');
      drawBadge(ctx, k.d, kx + 12, kpiY + 52, 'rgba(16, 185, 129, 0.15)', k.col, 9, true);
    });

    const splitY = kpiY + 90, splitH = 210;
    const chartW = mainW * 0.62;
    drawRoundRect(ctx, mainX, splitY, chartW, splitH, 8, '#1e293b', '#334155', 1);
    drawText(ctx, 'Tráfico de Red y Peticiones API (Meses)', mainX + 15, splitY + 25, 'bold 12px system-ui', '#ffffff');

    const months = ['Mayo', 'Junio', 'Julio', 'Agosto', 'Sept', 'Oct'];
    const values = [60, 85, 110, 95, 140, 165];
    const maxVal = 180;
    months.forEach((m, idx) => {
      const barX = mainX + 30 + idx * 52;
      const barH = (values[idx] / maxVal) * 110;
      const barY = splitY + 165 - barH;
      const bGrad = ctx.createLinearGradient(barX, barY, barX, barY + barH);
      bGrad.addColorStop(0, '#38bdf8'); bGrad.addColorStop(1, '#1e3a8a');
      drawRoundRect(ctx, barX, barY, 32, barH, [4, 4, 0, 0], bGrad);
      drawText(ctx, m, barX + 16, splitY + 185, '9px system-ui', '#94a3b8', 'center');
    });

    const actX = mainX + chartW + 15, actW = mainW - chartW - 15;
    drawRoundRect(ctx, actX, splitY, actW, splitH, 8, '#1e293b', '#334155', 1);
    drawText(ctx, 'Eventos Recientes', actX + 15, splitY + 25, 'bold 12px system-ui', '#ffffff');

    const events = [
      { t: 'Despliegue v2.4', st: 'Éxito', c: '#10b981' },
      { t: 'Copia BD S3', st: 'Completado', c: '#38bdf8' },
      { t: 'Pico CPU > 85%', st: 'Alerta', c: '#ef4444' }
    ];
    events.forEach((ev, idx) => {
      const ey = splitY + 50 + idx * 48;
      drawRoundRect(ctx, actX + 12, ey, actW - 24, 40, 6, '#0f172a');
      drawText(ctx, ev.t, actX + 20, ey + 24, '10px system-ui', '#e2e8f0');
      drawBadge(ctx, ev.st, actX + actW - 75, ey + 11, 'transparent', ev.c, 9, true);
    });

    const fabX = bx + bw - 35, fabY = by + bh - 35;
    ctx.beginPath(); ctx.arc(fabX, fabY, 18, 0, Math.PI*2); ctx.fillStyle = '#2563eb'; ctx.fill();
    ctx.font = 'bold 20px system-ui'; ctx.fillStyle = '#ffffff'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillText('+', fabX, fabY + 1);

    drawAnnotation(ctx, 'grid: sidebar + main (100vh)', mainX + 20, by + 12, topX, by + 12, '#38bdf8');
    drawAnnotation(ctx, 'position: fixed (bottom: 20px)', fabX - 25, fabY, fabX, fabY, '#60a5fa');
  }

  // Inicializador global
  function initAllCanvases() {
    const list = [
      { id: 'canvas-practica-1', fn: renderP1 },
      { id: 'canvas-practica-2', fn: renderP2 },
      { id: 'canvas-practica-3', fn: renderP3 },
      { id: 'canvas-practica-4', fn: renderP4 },
      { id: 'canvas-practica-5', fn: renderP5 },
      { id: 'canvas-practica-6', fn: renderP6 },
      { id: 'canvas-practica-7', fn: renderP7 }
    ];
    list.forEach(item => {
      const cv = document.getElementById(item.id);
      if (cv && cv.getContext) {
        const ctx = cv.getContext('2d');
        item.fn(ctx, cv.width, cv.height);
      }
    });
  }

  if (typeof window !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initAllCanvases);
    } else {
      initAllCanvases();
    }
    window.addEventListener('resize', initAllCanvases);
  }
})();
