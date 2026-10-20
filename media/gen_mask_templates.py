#!/usr/bin/env python3
"""
Genera plantillas A4 imprimibles para dos máscaras de cartón:
1. Cabeza de Quetzalcoatl (serpiente emplumada)
2. Máscara facial azteca simplificada
Para niños de ~9 años.
"""

import math

# ── helpers ──────────────────────────────────────────────────────────────────

CUT   = 'stroke="#cc0000" stroke-width="0.5" fill="none"'
FOLD  = 'stroke="#0044cc" stroke-width="0.35" fill="none" stroke-dasharray="3,2"'
MTN   = 'stroke="#006600" stroke-width="0.3"  fill="none" stroke-dasharray="1,2.5"'
TAB_F = 'fill="#e8e8e8" stroke="none"'
SCORE = 'stroke="#880088" stroke-width="0.3" fill="none" stroke-dasharray="0.5,1.5"'

def pt(x, y): return f"{x},{y}"

def rect_cut(x, y, w, h, rx=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" {CUT}/>'

def rect_fold(x, y, w, h):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" {FOLD}/>'

def line(x1, y1, x2, y2, style=CUT):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {style}/>'

def poly(pts, style=CUT):
    return f'<polygon points="{" ".join(pt(x,y) for x,y in pts)}" {style}/>'

def path(d, style=CUT):
    return f'<path d="{d}" {style}/>'

def text(x, y, s, size=3, anchor="middle", bold=False, color="#000"):
    w = "bold" if bold else "normal"
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-size="{size}mm" font-weight="{w}" fill="{color}">{s}</text>'

def circle(cx, cy, r, style=CUT):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" {style}/>'

def label_piece(x, y, letter, name, qty):
    return (text(x, y,   f"PIEZA {letter}", 4.5, bold=True) +
            text(x, y+6, name, 3.2) +
            text(x, y+11,f"Cantidad: {qty}", 2.8, color="#555"))

def arrow(x1, y1, x2, y2):
    """Simple arrow line."""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#333" stroke-width="0.4" marker-end="url(#arr)"/>'

def tab_rect(x, y, w, h):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" {TAB_F}/>'

# ── page wrapper ──────────────────────────────────────────────────────────────

def page(svg_body, page_title=""):
    title_svg = f'<text x="105" y="14" text-anchor="middle" font-family="Arial,sans-serif" font-size="4.5mm" font-weight="bold" fill="#222">{page_title}</text>' if page_title else ""
    return f"""
<div class="page">
<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">
<defs>
  <marker id="arr" markerWidth="4" markerHeight="4" refX="3" refY="2" orient="auto">
    <path d="M0,0 L4,2 L0,4 Z" fill="#333"/>
  </marker>
</defs>
<!-- page border -->
<rect x="4" y="4" width="202" height="289" fill="none" stroke="#bbb" stroke-width="0.3"/>
{title_svg}
{svg_body}
</svg>
</div>"""

# ─────────────────────────────────────────────────────────────────────────────
# PAGE 1 – Portada / instrucciones
# ─────────────────────────────────────────────────────────────────────────────

def page1_cover():
    body = []
    body.append(text(105, 25, "PLANTILLAS MÁSCARA CARTÓN 3D", 6.5, bold=True))
    body.append(text(105, 34, "Quetzalcóatl y Máscara Azteca · Para niños de 9 años", 3.5))

    # decorative line
    body.append(f'<line x1="15" y1="38" x2="195" y2="38" stroke="#cc0000" stroke-width="0.7"/>')

    # Legend
    lx, ly = 15, 44
    body.append(text(lx, ly, "LEYENDA DE LÍNEAS", 3.8, anchor="start", bold=True))
    ly += 7
    items = [
        (CUT,  "────",  "CORTAR (línea roja sólida)"),
        (FOLD, "- - -", "DOBLAR hacia ARRIBA (línea azul punteada)"),
        (MTN,  "·····", "DOBLAR hacia ABAJO (línea verde punteada)"),
        (TAB_F, "████", "ZONA DE PESTAÑA (área gris – pegar aquí)"),
    ]
    for sty, sym, desc in items:
        if "████" in sym:
            body.append(f'<rect x="{lx}" y="{ly-3}" width="18" height="4" {TAB_F} stroke="#999" stroke-width="0.3"/>')
        else:
            body.append(f'<line x1="{lx}" y1="{ly-1}" x2="{lx+18}" y2="{ly-1}" {sty}/>')
        body.append(text(lx+22, ly, desc, 3, anchor="start"))
        ly += 7

    # Materials
    ly += 4
    body.append(f'<line x1="15" y1="{ly-2}" x2="195" y2="{ly-2}" stroke="#ccc" stroke-width="0.4"/>')
    body.append(text(15, ly+5, "MATERIALES NECESARIOS", 3.8, anchor="start", bold=True))
    mats = [
        "• Cartón corrugado o cartón gris (3-4 mm de grosor) — 4 a 6 hojas tamaño oficio",
        "• Cartón delgado (tipo caja de cereal) para detalles — 2 hojas",
        "• Pegamento blanco PVA o pistola de silicón",
        "• Cúter o tijeras resistentes (uso exclusivo de adultos)",
        "• Regla metálica",
        "• Pintura acrílica: azul turquesa, dorado, negro, blanco, rojo",
        "• Plumas decorativas (azul, negro — opcionales)",
        "• Cinta adhesiva para refuerzo interior",
        "• Cuerda o liga elástica para sujetar la máscara",
    ]
    for i, m in enumerate(mats):
        body.append(text(18, ly + 12 + i*7, m, 3, anchor="start"))

    # Instructions
    iy = ly + 12 + len(mats)*7 + 6
    body.append(f'<line x1="15" y1="{iy-2}" x2="195" y2="{iy-2}" stroke="#ccc" stroke-width="0.4"/>')
    body.append(text(15, iy+5, "INSTRUCCIONES GENERALES", 3.8, anchor="start", bold=True))
    steps = [
        "1. Imprime todas las páginas en tamaño REAL (sin reducir, sin márgenes automáticos).",
        "2. Recorta las piezas siguiendo las LÍNEAS ROJAS.",
        "3. Marca los pliegues presionando suavemente con el dorso de un cúter sobre las líneas azules/verdes.",
        "4. Pega las pestañas grises con silicón o PVA; mantén presión 30 seg antes de soltar.",
        "5. Ensambla de adentro hacia afuera siguiendo el orden A → B → C… indicado en cada pieza.",
        "6. Pinta ANTES de ensamblar las piezas decorativas (ojos, escamas, dientes).",
        "7. Las piezas marcadas ×2 deben cortarse DOS VECES (una en espejo para el lado contrario).",
    ]
    for i, s in enumerate(steps):
        body.append(text(18, iy + 12 + i*7.5, s, 2.8, anchor="start"))

    # scale indicator
    sy = 270
    body.append(text(105, sy, "ESCALA 1:1  —  NO REDUCIR AL IMPRIMIR", 3, bold=True, color="#cc0000"))
    body.append(f'<line x1="15" y1="{sy+5}" x2="115" y2="{sy+5}" stroke="#000" stroke-width="0.5"/>')
    body.append(text(15, sy+10, "0", 2.5, anchor="start"))
    body.append(text(115, sy+10, "100 mm", 2.5, anchor="end"))
    for i in range(11):
        x = 15 + i*10
        h = 3 if i % 5 == 0 else 1.5
        body.append(f'<line x1="{x}" y1="{sy+5}" x2="{x}" y2="{sy+5+h}" stroke="#000" stroke-width="0.5"/>')

    return page("\n".join(body), "")

# ─────────────────────────────────────────────────────────────────────────────
# QUETZALCOATL — cabeza de dragón
# Dimensiones internas (caben en cabeza niño 9 años):
#   caja principal: 170 ancho × 190 fondo × 115 alto
#   hocico superior: 170 base → 100 punta, 150 largo, 70 alto base → 30 punta
#   mandíbula inf:  170 base → 100 punta, 120 largo, 40 alto
# Pestañas: 10 mm
# ─────────────────────────────────────────────────────────────────────────────

# PAGE 2 – Pieza A: Panel Superior de la Caja de la Cabeza

def page2_head_top():
    """Panel superior (techo) de la caja principal.
    Pieza sin pestaña: 175 × 165 mm
    Con pestañas 10mm en los 4 lados: 195 × 185 mm
    Centrada en página: x_off=7.5, y=35
    """
    x0, y0 = 7.5, 38   # top-left corner of full piece (with tabs)
    W, H = 195, 185     # total with tabs
    T = 10              # tab width
    pw, ph = 175, 165   # panel actual

    body = []
    # Tab fills (shade the 4 border strips)
    body.append(tab_rect(x0,    y0,    W,  T))        # top tab
    body.append(tab_rect(x0,    y0+H-T, W,  T))       # bottom tab
    body.append(tab_rect(x0,    y0+T, T, H-2*T))      # left tab
    body.append(tab_rect(x0+W-T,y0+T, T, H-2*T))      # right tab

    # Outer cut line
    body.append(rect_cut(x0, y0, W, H))

    # Fold lines (inner panel boundary)
    body.append(rect_fold(x0+T, y0+T, pw, ph))

    # Center label
    cx, cy = x0+W/2, y0+H/2
    body.append(label_piece(cx, cy-10, "A", "Panel Superior Caja Cabeza", "1"))
    body.append(text(cx, cy+8, f"Corte exterior: {W}×{H} mm", 2.8, color="#555"))
    body.append(text(cx, cy+15, f"Panel interior: {pw}×{ph} mm", 2.8, color="#555"))
    body.append(text(cx, cy+22, "▲ Pestañas grises = pegar ▲", 2.8, color="#cc0000"))

    # Tab labels
    body.append(text(x0+W/2, y0+T/2+1, "TAB→ Une con Panel Frontal", 2.3, color="#555"))
    body.append(text(x0+W/2, y0+H-T/2+1, "TAB→ Une con Panel Trasero", 2.3, color="#555"))
    body.append(text(x0+T/2, y0+H/2, "TAB→", 2.3, color="#555"))
    body.append(text(x0+W-T/2, y0+H/2, "TAB→", 2.3, color="#555"))

    # Note
    body.append(text(105, y0+H+8, "Usar cartón corrugado grueso (3-4mm). Esta pieza es el TECHO de la cabeza.", 2.8, color="#333"))

    return page("\n".join(body), "PIEZA A — CABEZA: PANEL SUPERIOR   [Quetzalcóatl]")

# PAGE 3 – Pieza B: Paneles Laterales (×2)

def page3_head_sides():
    """Dos paneles laterales: sin pestaña 185×115mm, con pestañas 205×135mm.
    Los dos caben uno encima del otro: 2×135+15gap = 285mm → caben en 277mm usable?
    Ajustamos: panel a 180×110, con tabs 200×130. 2×130+12=272 ✓
    """
    W, H = 195, 125   # total with tabs
    T = 10
    pw, ph = 175, 105  # panel actual

    body = []
    for idx, (x0, y0, label_side) in enumerate([
        (7.5, 32,  "LADO IZQUIERDO"),
        (7.5, 32+H+12, "LADO DERECHO  (espejo del izquierdo)"),
    ]):
        # Tab fills
        body.append(tab_rect(x0,    y0,    W,  T))
        body.append(tab_rect(x0,    y0+H-T, W,  T))
        body.append(tab_rect(x0,    y0+T, T, H-2*T))
        body.append(tab_rect(x0+W-T,y0+T, T, H-2*T))

        # Cut
        body.append(rect_cut(x0, y0, W, H))
        # Fold
        body.append(rect_fold(x0+T, y0+T, pw, ph))

        # Ojo: círculo de visión (solo en el panel real)
        ex, ey = x0+T+55, y0+T+ph//2
        body.append(circle(ex, ey, 28, CUT))
        body.append(circle(ex, ey, 22, FOLD))
        body.append(text(ex, ey+2, "OJO", 3, color="#cc0000", bold=True))

        # Breathing holes (small circles at bottom)
        for bx in [x0+T+20, x0+T+40]:
            body.append(circle(bx, y0+H-T-15, 5, SCORE))

        # Etiqueta
        cx, cy = x0+W/2+10, y0+H/2
        body.append(label_piece(cx, cy-10, "B", f"Panel Lateral — {label_side}", "×2"))
        body.append(text(cx, cy+8, f"Corte: {W}×{H} mm · Panel: {pw}×{ph} mm", 2.8, color="#555"))

        # dimension lines
        body.append(f'<line x1="{x0}" y1="{y0+H+3}" x2="{x0+W}" y2="{y0+H+3}" stroke="#888" stroke-width="0.3"/>')
        body.append(text(x0+W/2, y0+H+8, f"← {W} mm →", 2.5, color="#555"))

    body.append(text(105, 283, "Recorta el círculo grande (OJO) — es la ventana de visión/decoración del ojo.", 2.8, color="#333"))
    return page("\n".join(body), "PIEZA B — CABEZA: PANELES LATERALES ×2   [Quetzalcóatl]")

# PAGE 4 – Pieza C: Panel Trasero

def page4_head_back():
    """Panel trasero: sin pestaña 165×105mm, con tabs 185×125mm."""
    W, H = 185, 125
    T = 10
    pw, ph = 165, 105

    body = []
    x0, y0 = 12.5, 35

    body.append(tab_rect(x0,    y0,    W,  T))
    body.append(tab_rect(x0,    y0+H-T, W,  T))
    body.append(tab_rect(x0,    y0+T, T, H-2*T))
    body.append(tab_rect(x0+W-T,y0+T, T, H-2*T))
    body.append(rect_cut(x0, y0, W, H))
    body.append(rect_fold(x0+T, y0+T, pw, ph))

    # Abertura para cabeza en la parte inferior (semicírculo)
    # El panel trasero tiene un semicírculo para que la cabeza entre
    opx = x0+T+pw/2
    opy = y0+H-T
    body.append(path(f"M {opx-40} {opy} A 40 30 0 0 1 {opx+40} {opy}", CUT))
    body.append(text(opx, opy-8, "↑ apertura cabeza", 2.5, color="#cc0000"))

    # Elastic cord holes
    for ex in [x0+T+30, x0+T+pw-30]:
        body.append(circle(ex, y0+H-T-20, 4, CUT))
        body.append(text(ex, y0+H-T-8, "●hilo", 2, color="#555"))

    cx, cy = x0+W/2, y0+H/2 - 10
    body.append(label_piece(cx, cy, "C", "Panel Trasero", "1"))
    body.append(text(cx, cy+18, f"Corte: {W}×{H} mm · Panel: {pw}×{ph} mm", 2.8, color="#555"))
    body.append(text(cx, cy+26, "Semicírculo inferior = abertura para la cabeza del niño", 2.8, color="#cc0000"))

    # PAGE 4 also contains: Pieza D — Panel Frontal (más simple)
    # Panel frontal: solo tira horizontal que conecta los dos lados en frente
    # pero el "frente" realmente es la apertura del hocico.
    # Agregamos Pieza D — Refuerzo de frente (tira 165×30mm + tabs)
    x0d, y0d = 12.5, y0+H+18
    Wd, Hd = 185, 50
    T2 = 10
    body.append(tab_rect(x0d, y0d, Wd, T2))
    body.append(tab_rect(x0d, y0d+Hd-T2, Wd, T2))
    body.append(tab_rect(x0d, y0d+T2, T2, Hd-2*T2))
    body.append(tab_rect(x0d+Wd-T2, y0d+T2, T2, Hd-2*T2))
    body.append(rect_cut(x0d, y0d, Wd, Hd))
    body.append(rect_fold(x0d+T2, y0d+T2, 165, 30))
    body.append(label_piece(x0d+Wd/2, y0d+Hd/2-4, "D", "Tira Frontal Caja (unión entre lados)", "1"))
    body.append(text(x0d+Wd/2, y0d+Hd/2+12, "Corte: 185×50 mm · Panel: 165×30 mm", 2.8, color="#555"))

    return page("\n".join(body), "PIEZAS C + D — CABEZA: TRASERO Y FRONTAL   [Quetzalcóatl]")

# PAGE 5 – Piezas E+F: Hocico Superior (trapezoid net)

def page5_snout():
    """Hocico superior:
    Vista desde arriba: trapecio 165mm (base) → 95mm (punta), longitud 145mm
    Vista lateral: trapecio 165mm base, 145mm largo, 65mm alto base, 28mm alto punta
    """
    body = []

    # --- Pieza E1: Tapa superior del hocico (trapecio top) ---
    # Points (with 10mm tabs extended):
    # The trapezoid: base=165, top=95, height=145
    # We add a 10mm pestaña on all sides.
    # Actual trapezoid pts (no tabs):
    bw, tw, L = 165, 95, 145  # base width, tip width, length
    T = 10
    # Place at x0=10, y0=28
    x0, y0 = 10, 28
    # The trapezoid without tabs:
    # bl=x0, br=x0+bw, tl=x0+(bw-tw)/2, tr=x0+(bw+tw)/2
    # y_base=y0+L, y_top=y0
    bl = x0 + T
    br = x0 + T + bw
    tl = x0 + T + (bw-tw)//2
    tr = x0 + T + (bw+tw)//2
    yb = y0 + T + L
    yt = y0 + T

    # Tab fills (approximate as outer polygon)
    # For simplicity, show cut outline and fold inner
    # Outer cut (with tabs extending ~10mm perpendicular to each edge)
    # Simplified: just extend bounding box for tabs
    body.append(tab_rect(x0, y0, bw+2*T, L+2*T))
    # Actual piece polygon (fold line)
    body.append(poly([(bl,yb),(br,yb),(tr,yt),(tl,yt)], FOLD))
    # Cut outline (simplified outer boundary with tabs)
    body.append(rect_cut(x0, y0, bw+2*T, L+2*T))
    # Tab notes
    body.append(text(x0+(bw+2*T)/2, y0+T/2+2, "TAB → une con panel lateral izquierdo", 2.2, color="#555"))
    body.append(text(x0+(bw+2*T)/2, y0+T+L+T/2+2, "TAB → punta del hocico", 2.2, color="#555"))

    cx = x0+(bw+2*T)/2
    cy = y0+T+L/2
    body.append(label_piece(cx, cy-12, "E", "Tapa Superior del Hocico", "1"))
    body.append(text(cx, cy+8, f"Base: {bw}mm · Punta: {tw}mm · Largo: {L}mm", 2.8, color="#555"))
    body.append(text(cx, cy+15, "El trapecio crea la forma cónica del hocico", 2.8, color="#333"))

    # --- Pieza F: Lados del Hocico (×2) ---
    # Side profile is a right trapezoid:
    # bottom=145mm (same as length),
    # height at back=65mm, height at front=28mm
    sh, sf, sb = 145, 28, 65   # length, front height, back height
    x0f, y0f = 10, y0+L+2*T+15
    Wf, Hf = sh+2*T, sb+2*T

    body.append(tab_rect(x0f, y0f, Wf, Hf))
    # Actual side trapezoid (fold line)
    pts_f = [(x0f+T, y0f+T+sb), (x0f+T+sh, y0f+T+sf), (x0f+T+sh, y0f+T+sb)]
    # It's a right trapezoid: back is tall, front is short, top is slanted, bottom is flat
    pts_fold = [
        (x0f+T,      y0f+T),
        (x0f+T+sh,   y0f+T+(sb-sf)),
        (x0f+T+sh,   y0f+T+sb),
        (x0f+T,      y0f+T+sb),
    ]
    body.append(poly(pts_fold, FOLD))
    body.append(rect_cut(x0f, y0f, Wf, Hf))

    cx2 = x0f + Wf/2
    cy2 = y0f + Hf/2
    body.append(label_piece(cx2+20, cy2-8, "F", "Lado del Hocico", "×2"))
    body.append(text(cx2+20, cy2+8, f"Largo: {sh}mm · Alto atrás: {sb}mm · Alto frente: {sf}mm", 2.5, color="#555"))

    body.append(text(105, 283, "Tip: dobla el trapecio (Pieza E) en forma de cono plano y pega los lados F a cada costado.", 2.8, color="#333"))
    return page("\n".join(body), "PIEZAS E + F — HOCICO SUPERIOR   [Quetzalcóatl]")

# PAGE 6 – Pieza G: Mandíbula inferior + dientes

def page6_jaw():
    """Mandíbula inferior:
    Planta: trapecio 165mm (base) → 95mm (punta), largo 120mm
    Perfil: alto 40mm (plano — es plana la mandíbula)
    Dientes: tira dentada superior e inferior
    """
    body = []
    T = 10

    # ---- G1: Tapa mandíbula (top de la mandíbula = la cara visible inferior del hocico) ----
    bw2, tw2, L2 = 155, 85, 115
    x0, y0 = 10, 30

    body.append(tab_rect(x0, y0, bw2+2*T, L2+2*T))
    tl2 = x0+T+(bw2-tw2)//2
    tr2 = x0+T+(bw2+tw2)//2
    pts_g = [(x0+T,y0+T), (x0+T+bw2,y0+T), (tr2,y0+T+L2), (tl2,y0+T+L2)]
    body.append(poly(pts_g, FOLD))
    body.append(rect_cut(x0, y0, bw2+2*T, L2+2*T))
    cx = x0+(bw2+2*T)/2
    cy = y0+T+L2/2
    body.append(label_piece(cx, cy-10, "G", "Tapa Mandíbula Inferior", "1"))
    body.append(text(cx, cy+8,  f"Base: {bw2}mm · Punta: {tw2}mm · Largo: {L2}mm", 2.8, color="#555"))

    # ---- G2: Costados mandíbula (rectángulos planos, alto=40mm) ----
    x0s, y0s = 10, y0+L2+2*T+12
    Ws, Hs = 115+2*T, 40+2*T
    for i, lbl in enumerate(["LADO IZQ.", "LADO DER."]):
        xi = x0s + i*(Ws+8)
        body.append(tab_rect(xi, y0s, Ws, Hs))
        body.append(rect_cut(xi, y0s, Ws, Hs))
        body.append(rect_fold(xi+T, y0s+T, 115, 40))
        body.append(text(xi+Ws/2, y0s+Hs/2, f"G2 · Costado Mandíbula {lbl}", 2.8))
        body.append(text(xi+Ws/2, y0s+Hs/2+8, "115×40 mm", 2.5, color="#555"))

    # ---- H: Tira de dientes ×2 (hocico y mandíbula) ----
    # Zigzag/castellated strip: 140mm long, 25mm tall
    # Teeth: 15mm wide × 15mm tall, spacing 5mm
    y0h = y0s + Hs + 15
    body.append(text(105, y0h-5, "PIEZA H — Tiras de Dientes (Cortar 2 tiras — una para hocico, una para mandíbula)", 3, bold=True, color="#cc0000"))
    n_teeth = 7
    tooth_w = 14
    gap = 6
    strip_W = n_teeth * (tooth_w + gap)
    tooth_H = 22
    base_H = 12
    total_H = tooth_H + base_H
    x0h = (210 - strip_W) / 2
    # Base rectangle with tabs
    body.append(tab_rect(x0h-T, y0h, strip_W+2*T, total_H+T))
    # Cut outline with teeth
    d = f"M {x0h} {y0h+total_H}"  # start bottom-left
    d += f" L {x0h} {y0h+tooth_H}"  # up left side
    for i in range(n_teeth):
        xstart = x0h + i*(tooth_w+gap)
        xend   = xstart + tooth_w
        if i > 0:
            d += f" L {xstart} {y0h+tooth_H}"
        d += f" L {xstart} {y0h}"
        d += f" L {xend} {y0h}"
        d += f" L {xend} {y0h+tooth_H}"
    d += f" L {x0h+strip_W} {y0h+tooth_H} L {x0h+strip_W} {y0h+total_H} Z"
    body.append(f'<path d="{d}" fill="#f9f9f9" {CUT}/>')
    body.append(rect_fold(x0h, y0h+tooth_H, strip_W, base_H))
    body.append(text(x0h+strip_W/2, y0h+tooth_H+base_H/2+2, "H — Tira Dientes", 3, color="#cc0000"))
    body.append(text(x0h+strip_W/2, y0h+tooth_H+base_H/2+8, f"Cortar 2 piezas iguales · {strip_W:.0f}×{total_H}mm", 2.5, color="#555"))

    return page("\n".join(body), "PIEZAS G + H — MANDÍBULA + DIENTES   [Quetzalcóatl]")

# PAGE 7 – Piezas I (ojos) + J (cresta/plumas)

def page7_eyes_crest():
    body = []

    # ---- I: Ojo decorativo (anillo) ×2 ----
    # Outer ring: r=30mm, inner ring: r=21mm → donut
    # Separate concentric circles to cut
    body.append(text(65, 22, "PIEZA I — Anillo del Ojo ×2", 4, bold=True))
    body.append(text(65, 29, "Cortar 2 veces. Usar cartón delgado.", 3, color="#333"))

    cx1, cy1 = 55, 65
    body.append(circle(cx1, cy1, 30, CUT))       # outer cut
    body.append(circle(cx1, cy1, 21, CUT))       # inner cut (remove this circle)
    body.append(circle(cx1, cy1, 25, FOLD))      # decorative score ring

    # Spiral decoration lines (manual marks)
    body.append(text(cx1, cy1, "●", 5))
    for ang in range(0, 360, 45):
        r1, r2 = 23, 29
        ax = math.radians(ang)
        body.append(f'<line x1="{cx1+r1*math.cos(ax):.1f}" y1="{cy1+r1*math.sin(ax):.1f}" x2="{cx1+r2*math.cos(ax):.1f}" y2="{cy1+r2*math.sin(ax):.1f}" {SCORE}/>')
    body.append(text(cx1, cy1+2, "OJO", 3, color="#cc0000", bold=True))
    body.append(text(cx1, cy1+40, "∅ exterior: 60mm · ∅ interior: 42mm", 2.8, color="#555"))
    body.append(text(cx1, cy1+47, "Doblar el anillo ligeramente convexo y pegar al panel lateral", 2.5, color="#333"))

    # 2nd eye (mirror, same)
    cx2 = 145
    body.append(circle(cx2, cy1, 30, CUT))
    body.append(circle(cx2, cy1, 21, CUT))
    body.append(circle(cx2, cy1, 25, FOLD))
    for ang in range(0, 360, 45):
        r1, r2 = 23, 29
        ax = math.radians(ang)
        body.append(f'<line x1="{cx2+r1*math.cos(ax):.1f}" y1="{cy1+r1*math.sin(ax):.1f}" x2="{cx2+r2*math.cos(ax):.1f}" y2="{cy1+r2*math.sin(ax):.1f}" {SCORE}/>')
    body.append(text(cx2, cy1+2, "OJO", 3, color="#cc0000", bold=True))

    # Espiral central (pupila)
    for cxe, lbl in [(cx1, "1"), (cx2, "2")]:
        body.append(text(cxe, cy1-36, f"I{lbl}", 3.5, bold=True, color="#0044cc"))

    # ---- J: Pétalos de la cresta ×7 ----
    body.append(text(105, cy1+60, "PIEZA J — Pétalo de Cresta ×7", 4, bold=True))
    body.append(text(105, cy1+68, "Cortar 7 veces · Cartón delgado", 3, color="#333"))

    # Petal shape: teardrop, 80mm tall × 46mm wide
    pw, ph = 46, 80
    # Per petal: place 7 in a row with 4mm gap
    gap = 3
    total_petal_W = 7 * pw + 6 * gap
    px0 = (210 - total_petal_W) / 2
    py0 = cy1 + 75

    for i in range(7):
        px = px0 + i*(pw+gap) + pw/2
        py = py0

        # Teardrop path: pointed top, rounded bottom
        cx_p = px
        cy_top = py
        cy_bot = py + ph

        ctrl = 28
        d = (f"M {cx_p} {cy_top} "
             f"C {cx_p+ctrl} {cy_top+ph*0.3} {cx_p+pw/2} {cy_top+ph*0.6} {cx_p} {cy_bot} "
             f"C {cx_p-pw/2} {cy_top+ph*0.6} {cx_p-ctrl} {cy_top+ph*0.3} {cx_p} {cy_top} Z")
        body.append(f'<path d="{d}" fill="#f0f0f0" {CUT}/>')
        # Center score line
        body.append(line(cx_p, cy_top+5, cx_p, cy_bot-10, FOLD))

        if i == 3:  # label on middle petal
            body.append(text(cx_p, py+ph/2, "J", 3.5, bold=True, color="#0044cc"))

    body.append(text(105, py0+ph+8, f"Pétalos: {pw}mm ancho × {ph}mm alto · Doblar por la línea central (azul) ligeramente", 2.8, color="#555"))

    return page("\n".join(body), "PIEZAS I + J — OJOS Y CRESTA   [Quetzalcóatl]")

# PAGE 8 – Pieza K: Tiras de escamas + Pieza L: Lengua

def page8_scales_tongue():
    body = []
    body.append(text(105, 22, "PIEZA K — Tiras de Escamas  +  PIEZA L — Lengua bífida", 4, bold=True))

    # ---- K: Scale strip (scalloped edge) ----
    # 3 strips: 170mm × 35mm with scalloped top (scales)
    body.append(text(105, 30, "PIEZA K — Tira de Escamas ×3 · Pegar escalonadas sobre el hocico", 3.2, color="#333"))
    scale_r = 12
    n_scales = 7
    strip_w = n_scales * (scale_r * 2) + 4
    strip_base = 18
    strip_total = strip_base + scale_r

    for row in range(3):
        xs = (210 - strip_w) / 2
        ys = 35 + row * (strip_total + 10)
        # Base strip fill
        body.append(tab_rect(xs, ys+scale_r, strip_w, strip_base))
        body.append(rect_cut(xs, ys+scale_r, strip_w, strip_base))

        # Scalloped top: arcs
        d = f"M {xs} {ys+scale_r}"
        for sc in range(n_scales):
            cx_sc = xs + sc * scale_r * 2 + scale_r
            cy_sc = ys + scale_r
            d += f" A {scale_r} {scale_r} 0 0 1 {xs+(sc+1)*scale_r*2} {ys+scale_r}"
        d += f" L {xs+strip_w} {ys+scale_r+strip_base} L {xs} {ys+scale_r+strip_base} Z"
        body.append(f'<path d="{d}" fill="#e8e8e8" {CUT}/>')

        body.append(text(xs+strip_w/2, ys+scale_r+strip_base/2+2, f"K{row+1} · {strip_w:.0f}×{strip_total:.0f}mm", 2.5, color="#333"))

    # Tab instruction
    ky = 35 + 3*(strip_total+10) + 5
    body.append(text(105, ky, "Pegar la parte PLANA (gris) al hocico. Las escamas quedan hacia afuera. Superponer filas 1-2-3.", 2.8, color="#555"))

    # ---- L: Lengua bífida ----
    ly0 = ky + 12
    body.append(text(105, ly0, "PIEZA L — Lengua Bífida ×1 · Cartón delgado · Opcional", 3.5, bold=True, color="#cc0000"))
    ly0 += 8

    # Tongue shape: forked tongue
    tx, ty = 105, ly0 + 80
    # Main body
    tongue_pts_l = [
        (tx, ty-80),      # tip center top
        (tx+15, ty-60),
        (tx+18, ty-10),
        (tx+8, ty),       # right fork tip
        (tx, ty-15),
    ]
    tongue_pts_r = [
        (tx, ty-80),
        (tx-15, ty-60),
        (tx-18, ty-10),
        (tx-8, ty),
        (tx, ty-15),
    ]
    # Draw a forked tongue
    d_t = (f"M {tx} {ty-80} "
           f"C {tx+20} {ty-60} {tx+25} {ty-20} {tx+10} {ty} "
           f"C {tx+3} {ty-12} {tx-3} {ty-12} {tx-10} {ty} "
           f"C {tx-25} {ty-20} {tx-20} {ty-60} {tx} {ty-80} Z")
    body.append(f'<path d="{d_t}" fill="#f9f0f0" {CUT}/>')
    body.append(line(tx, ty-80, tx, ty-18, FOLD))  # center line (fork divider)
    body.append(text(tx, ty-40, "L", 4, bold=True, color="#0044cc"))
    body.append(text(tx, ty-30, "LENGUA", 3, color="#cc0000"))
    body.append(text(tx, ty+8, "Largo: 80mm · Pegar en punta del hocico", 2.8, color="#555"))

    return page("\n".join(body), "PIEZAS K + L — ESCAMAS Y LENGUA   [Quetzalcóatl]")

# PAGE 9 – Guía de ensamble Quetzalcóatl

def page9_assembly():
    body = []
    body.append(text(105, 22, "GUÍA DE ENSAMBLE — Quetzalcóatl", 5, bold=True))
    body.append(text(105, 30, "Sigue este orden. Deja secar el pegamento 5 min entre pasos.", 3.2))

    steps = [
        ("PASO 1", "CAJA DE LA CABEZA",
         ["a) Dobla los 4 bordes con pestañas de la Pieza A (techo).",
          "b) Pega los Paneles B (lados) a las pestañas laterales de A.",
          "c) Pega el Panel C (trasero) cerrando la caja por atrás.",
          "d) Pega la Tira D (frontal) uniendo los dos costados por enfrente.",
          "   → Resultado: caja abierta por abajo, con abertura frontal para el hocico."]),
        ("PASO 2", "HOCICO SUPERIOR",
         ["a) Dobla la Pieza E (tapa) en forma cónica/trapezoidal.",
          "b) Pega los Costados F a cada lado de E.",
          "c) Pega la tira de dientes H en el borde inferior del hocico.",
          "d) Une el hocico completo a la abertura frontal de la caja (Paso 1)."]),
        ("PASO 3", "MANDÍBULA",
         ["a) Arma la mandíbula con G+G2 (tapa + costados).",
          "b) Pega la segunda tira de dientes H en el borde superior de la mandíbula.",
          "c) Une la mandíbula debajo del hocico dejando ~2-3cm de apertura.",
          "   (La boca puede quedar fija abierta o articulada con bisagra de cartón.)"]),
        ("PASO 4", "DECORACIÓN",
         ["a) Pega los Anillos I sobre los agujeros de ojo en los paneles B.",
          "b) Pega los Pétalos J (cresta) en la parte superior de la caja en abanico.",
          "c) Pega las Tiras de Escamas K escalonadas sobre el hocico.",
          "d) Inserta la Lengua L en la punta del hocico."]),
        ("PASO 5", "ACABADO",
         ["a) Pinta con acrílico: base verde oscuro o café.",
          "b) Detalla ojos con amarillo/dorado y negro.",
          "c) Dientes: blanco con punta negra.",
          "d) Escamas: tonos alternos verde-azul.",
          "e) Pasa cuerda elástica por los agujeros del panel C para sujetar en la cabeza."]),
    ]

    y = 40
    for i, (title, sub, items) in enumerate(steps):
        col = "#cc0000" if i == 0 else ("#0044cc" if i == 1 else ("#006600" if i == 2 else ("#880088" if i == 3 else "#884400")))
        body.append(f'<rect x="10" y="{y-4}" width="190" height="{len(items)*7+16}" rx="2" fill="#f8f8f8" stroke="{col}" stroke-width="0.4"/>')
        body.append(text(15, y+2, f"{title}: {sub}", 3.8, anchor="start", bold=True, color=col))
        for j, item in enumerate(items):
            body.append(text(18, y+10+j*7, item, 2.8, anchor="start"))
        y += len(items)*7 + 22

    # Simple schematic
    if y < 250:
        body.append(text(105, y+8, "ESQUEMA LATERAL (no a escala)", 3, bold=True))
        # Simple box sketch
        sx, sy = 40, y+15
        body.append(f'<rect x="{sx}" y="{sy}" width="60" height="40" fill="none" stroke="#333" stroke-width="0.6"/>')  # head box
        body.append(f'<polygon points="{sx+60},{sy+5} {sx+100},{sy+10} {sx+100},{sy+30} {sx+60},{sy+35}" fill="none" stroke="#333" stroke-width="0.6"/>')  # snout
        body.append(f'<polygon points="{sx+60},{sy+37} {sx+95},{sy+35} {sx+95},{sy+45} {sx+60},{sy+40}" fill="none" stroke="#555" stroke-width="0.4"/>')  # jaw
        body.append(f'<circle cx="{sx+15}" cy="{sy+15}" r="8" fill="none" stroke="#333" stroke-width="0.5"/>')  # eye
        for k in range(5):
            px = sx+45+k*8
            body.append(f'<ellipse cx="{px}" cy="{sy-8}" rx="4" ry="10" fill="none" stroke="#333" stroke-width="0.4"/>')  # petals
        body.append(text(sx+80, sy+55, "← hocico + mandíbula", 2.5, anchor="start", color="#555"))
        body.append(text(sx+30, sy+55, "← caja cabeza", 2.5, color="#555"))

    return page("\n".join(body), "GUÍA DE ENSAMBLE — Quetzalcóatl   [Paso a Paso]")

# PAGE 10 – Máscara Azteca (facial, plana + tocado)

def page10_aztec_mask():
    body = []
    body.append(text(105, 20, "MÁSCARA AZTECA — Calavera Turquesa", 5.5, bold=True, color="#4400aa"))
    body.append(text(105, 29, "Máscara facial + Tocado. Usar cartón delgado para curvar.", 3))

    # ---- Pieza AA: Base facial ----
    # Oval face mask: 140mm wide × 175mm tall
    x0, y0 = 35, 38
    fw, fh = 140, 175
    cx_f, cy_f = x0+fw/2, y0+fh/2

    # Outer oval (cut)
    body.append(f'<ellipse cx="{cx_f}" cy="{cy_f}" rx="{fw/2}" ry="{fh/2}" {CUT}/>')

    # Eye holes: large sunken circles
    eye_y = cy_f - 20
    eler, erer = 27, 27  # eye radius
    el_cx = cx_f - 35
    er_cx = cx_f + 35
    body.append(circle(el_cx, eye_y, eler, CUT))   # left eye hole
    body.append(circle(er_cx, eye_y, erer, CUT))   # right eye hole
    body.append(circle(el_cx, eye_y, eler-6, FOLD))  # inner ring
    body.append(circle(er_cx, eye_y, erer-6, FOLD))

    # Nose triangle
    nose_y = cy_f + 5
    body.append(poly([(cx_f-10, nose_y), (cx_f+10, nose_y), (cx_f, nose_y+18)], CUT))

    # Mouth: rectangular with teeth detail
    mouth_y = cy_f + 40
    body.append(rect_cut(cx_f-35, mouth_y, 70, 22))
    # Teeth dividers
    for t in range(1, 5):
        body.append(line(cx_f-35+t*14, mouth_y, cx_f-35+t*14, mouth_y+12, FOLD))
    body.append(line(cx_f-35, mouth_y+12, cx_f+35, mouth_y+12, FOLD))

    # Tab holes for string
    body.append(circle(x0+8, cy_f, 4, CUT))
    body.append(circle(x0+fw-8, cy_f, 4, CUT))
    body.append(text(x0+8, cy_f+10, "●hilo", 2.3, color="#555"))
    body.append(text(x0+fw-8, cy_f+10, "●hilo", 2.3, color="#555"))

    body.append(label_piece(cx_f, y0+fh+10, "AA", "Base Facial Calavera", "1"))
    body.append(text(cx_f, y0+fh+22, f"Oval: {fw}×{fh}mm · Cartón delgado para poder curvar", 2.8, color="#555"))
    body.append(text(cx_f, y0+fh+29, "Pinta: azul turquesa con detalles negros/dorados", 2.8, color="#4400aa"))

    # ---- Pieza BB: Tocado lateral (corona/casco) ----
    # Horizontal band: 340mm (head circumference) × 50mm + pointed top elements
    # Simplified: show as strip
    x0t, y0t = 10, y0+fh+38
    body.append(text(105, y0t, "PIEZA BB — Banda Tocado (casco circular)", 3.5, bold=True))
    Wt, Ht = 165, 45
    x0t = (210-Wt)/2
    y0t += 6
    body.append(tab_rect(x0t, y0t, Wt, Ht))
    body.append(rect_cut(x0t, y0t, Wt, Ht))
    body.append(rect_fold(x0t+10, y0t+10, Wt-20, Ht-20))
    # Geometric pattern suggestion (diamond row)
    for di in range(8):
        dx = x0t+10+di*19+9
        dy = y0t+Ht/2
        r = 6
        body.append(poly([(dx,dy-r),(dx+r,dy),(dx,dy+r),(dx-r,dy)], SCORE))
    body.append(text(x0t+Wt/2, y0t+Ht/2, "BB · Banda Tocado · 165×45mm", 2.8))
    body.append(text(x0t+Wt/2, y0t+Ht/2+8, "Curvar y pegar en círculo (circunferencia de cabeza)", 2.5, color="#555"))

    return page("\n".join(body), "PIEZA AA + BB — MÁSCARA AZTECA   [Calavera Turquesa]")

# PAGE 11 – Tocado superior + pectoral azteca

def page11_aztec_headdress():
    body = []
    body.append(text(105, 20, "MÁSCARA AZTECA — Tocado Superior y Collar Pectoral", 4.5, bold=True, color="#4400aa"))

    # ---- CC: Tocado arco central (frente) ----
    body.append(text(105, 30, "PIEZA CC — Arco del Tocado (pieza frontal vertical)", 3.5, bold=True))
    # Arch shape: wide at bottom, arched top, with geometric ornaments
    ax0, ay0 = 30, 38
    aw, ah = 150, 80
    # Arch: bottom rectangle + semicircle top
    d_arch = (f"M {ax0} {ay0+ah} L {ax0} {ay0+40} "
              f"A {aw/2} {40} 0 0 1 {ax0+aw} {ay0+40} "
              f"L {ax0+aw} {ay0+ah} Z")
    body.append(f'<path d="{d_arch}" fill="#f0f0ff" {CUT}/>')
    # Ornamental lines on arch
    for row in range(3):
        y_r = ay0 + 50 + row*10
        body.append(line(ax0+5, y_r, ax0+aw-5, y_r, SCORE))
    # Central rectangle ornament
    body.append(rect_cut(ax0+55, ay0+42, 40, 28))
    body.append(line(ax0+75, ay0+42, ax0+75, ay0+70, FOLD))  # divider
    body.append(text(ax0+aw/2, ay0+ah+8, "CC · Arco Tocado · 150×80mm", 2.8, color="#555"))
    body.append(text(ax0+aw/2, ay0+ah+15, "Pegar vertical sobre la Banda BB, centrado en frente", 2.5, color="#333"))

    # ---- DD: Piezas laterales tocado (×4 triángulos decorativos) ----
    body.append(text(105, ay0+ah+30, "PIEZA DD — Triángulos Laterales Tocado ×4", 3.5, bold=True))
    # Simple isoceles triangles: base 35mm, height 50mm
    y0d = ay0+ah+36
    for i in range(4):
        tx = 20 + i*47
        body.append(poly([(tx,y0d),(tx+35,y0d),(tx+17,y0d+50)], CUT))
        body.append(line(tx+17, y0d+5, tx+17, y0d+45, FOLD))
        body.append(text(tx+17, y0d+28, f"DD{i+1}", 3, color="#4400aa"))
    body.append(text(105, y0d+58, "DD · 35mm base × 50mm alto · Decorar con líneas geométricas aztecas antes de pegar", 2.8, color="#555"))

    # ---- EE: Collar pectoral ----
    body.append(text(105, y0d+70, "PIEZA EE — Collar Pectoral (media luna)", 3.5, bold=True, color="#cc0000"))
    # Crescent/gorget shape: half-donut
    cx_e, cy_e = 105, y0d+130
    body.append(f'<path d="M {cx_e-75} {cy_e} A 75 75 0 0 1 {cx_e+75} {cy_e} L {cx_e+55} {cy_e} A 55 55 0 0 0 {cx_e-55} {cy_e} Z" fill="#f0f0e8" {CUT}/>')
    # Geometric decoration
    for ang_i in range(5):
        ang = 10 + ang_i*36
        a = math.radians(ang)
        r1, r2 = 57, 73
        body.append(line(cx_e+r1*math.cos(a), cy_e-r1*math.sin(a), cx_e+r2*math.cos(a), cy_e-r2*math.sin(a), SCORE))
    body.append(text(cx_e, cy_e-45, "EE · Pectoral/Collar", 3, bold=True, color="#cc0000"))
    body.append(text(cx_e, cy_e-35, "Media luna: radio ext.75mm · radio int.55mm", 2.8, color="#555"))
    body.append(text(cx_e, cy_e-27, "Pegar plumas (papel o reales) en el borde curvo superior", 2.5, color="#333"))

    # String holes on pectoral
    for ph in [-60, -30, 0, 30, 60]:
        px = cx_e + ph
        py_h = cy_e - 1
        body.append(circle(px, py_h, 3, CUT))

    body.append(text(cx_e, cy_e+10, "Pasar hilo por los agujeros para colgar el pectoral al cuello", 2.5, color="#555"))

    return page("\n".join(body), "PIEZAS CC+DD+EE — TOCADO + PECTORAL AZTECA   [Calavera Turquesa]")

# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    pages_html = [
        page1_cover(),
        page2_head_top(),
        page3_head_sides(),
        page4_head_back(),
        page5_snout(),
        page6_jaw(),
        page7_eyes_crest(),
        page8_scales_tongue(),
        page9_assembly(),
        page10_aztec_mask(),
        page11_aztec_headdress(),
    ]

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Máscaras 3D Cartón — Quetzalcóatl y Azteca</title>
<style>
  @page {{ size: A4; margin: 0; }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; padding: 0; background: #eee; }}
  .page {{
    width: 210mm;
    height: 297mm;
    background: white;
    display: block;
    margin: 0 auto 10px;
    page-break-after: always;
    overflow: hidden;
  }}
  .page:last-child {{ page-break-after: auto; margin-bottom: 0; }}
  @media print {{
    body {{ background: white; }}
    .page {{ margin: 0; box-shadow: none; }}
  }}
</style>
</head>
<body>
{''.join(pages_html)}
</body>
</html>"""

    out = "/Users/sergioguillen/.openclaw/workspace/media/mascaras_carton_templates.html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Generado: {out}")
    print(f"   Páginas: {len(pages_html)}")
    print(f"   Tamaño: {len(html):,} bytes")

if __name__ == "__main__":
    main()
