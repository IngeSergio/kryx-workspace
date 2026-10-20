from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import pptx.oxml.ns as nsmap
from lxml import etree

W = Inches(13.33)
H = Inches(7.5)

# ── Colors ──────────────────────────────────────────
BG_DARK  = RGBColor(0x0D, 0x1B, 0x2A)
BG_NAVY  = RGBColor(0x0F, 0x20, 0x44)
BG_TEAL  = RGBColor(0x0A, 0x2A, 0x2A)
BG_WINE  = RGBColor(0x1A, 0x0A, 0x1A)
BG_GREEN = RGBColor(0x04, 0x1A, 0x0D)

BLUE   = RGBColor(0x5B, 0xC0, 0xDE)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
GRAY   = RGBColor(0xC8, 0xD8, 0xE0)
MUTED  = RGBColor(0x8A, 0xAB, 0xB8)
GREEN  = RGBColor(0x2E, 0xCC, 0x71)
RED    = RGBColor(0xE7, 0x4C, 0x3C)
GOLD   = RGBColor(0xF3, 0x9C, 0x12)
PURPLE = RGBColor(0x9B, 0x59, 0xB6)

prs = Presentation()
prs.slide_width  = W
prs.slide_height = H

blank = prs.slide_layouts[6]  # blank


def add_slide(bg_color):
    sl = prs.slides.add_slide(blank)
    bg = sl.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = bg_color
    return sl


def add_rect(sl, left, top, width, height, color, alpha=None):
    shape = sl.shapes.add_shape(1, left, top, width, height)
    shape.line.fill.background()
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    return shape


def txb(sl, text, left, top, width, height,
        size=24, bold=False, color=WHITE, align=PP_ALIGN.LEFT, italic=False):
    tb = sl.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return tb


def kicker(sl, text):
    txb(sl, text.upper(), Inches(0.7), Inches(0.35), Inches(11), Inches(0.4),
        size=9, bold=True, color=BLUE)


def title(sl, text, top=Inches(0.85), size=36):
    txb(sl, text, Inches(0.7), top, Inches(11.6), Inches(1.5),
        size=size, bold=True, color=WHITE)
    # underline bar
    add_rect(sl, Inches(0.7), top + Inches(1.2), Inches(11.6), Inches(0.04), BLUE)


def bullet(sl, items, top, size=16, color=GRAY, left=Inches(0.7), width=Inches(11.6)):
    y = top
    for item in items:
        txb(sl, "→  " + item, left, y, width, Inches(0.45),
            size=size, color=color)
        y += Inches(0.48)


# ════════════════════════════════════════════════════
# SLIDE 1 — PORTADA
# ════════════════════════════════════════════════════
sl = add_slide(BG_DARK)
txb(sl, "CJTAL — COMITÉ DE JUSTIFICACIONES TARDÍAS DE AMÉRICA LATINA",
    Inches(0.7), Inches(0.5), Inches(11.6), Inches(0.4),
    size=9, bold=True, color=BLUE)

txb(sl, "Evaluación y Poder de las\nMejores Excusas para Llegar Tarde",
    Inches(0.7), Inches(1.1), Inches(11.6), Inches(2.8),
    size=44, bold=True, color=WHITE)

txb(sl, "Estudio longitudinal 2010–2026  ·  Muestra n=1  ·  Resultados altamente reproducibles",
    Inches(0.7), Inches(3.8), Inches(11.6), Inches(0.5),
    size=14, italic=True, color=MUTED)

txb(sl, "Presentado por: Sergio Guillén   ·   15 años de experiencia en campo   ·   Récord personal: 47 min   ·   Nunca investigado",
    Inches(0.7), Inches(4.6), Inches(11.6), Inches(0.5),
    size=13, color=GRAY)

txb(sl, "Hora de inicio programada: 00:00   |   Hora de inicio real:  +23 min",
    Inches(0.7), Inches(5.4), Inches(11.6), Inches(0.4),
    size=11, color=RGBColor(0x55, 0x55, 0x55))

txb(sl, "* Esta presentación fue elaborada bajo estrictos estándares académicos de rigor cuestionable.\nNingún familiar fue dañado durante su producción.",
    Inches(0.7), Inches(6.5), Inches(11.6), Inches(0.7),
    size=9, italic=True, color=RGBColor(0x44, 0x44, 0x44))

# ════════════════════════════════════════════════════
# SLIDE 2 — AGENDA
# ════════════════════════════════════════════════════
sl = add_slide(BG_NAVY)
kicker(sl, "Agenda")
title(sl, "Índice de Contenidos")

items_left = [
    "01. Justificación y alcance",
    "02. Marco teórico — Taxonomía",
    "03. Metodología de evaluación",
    "04. Top 5 excusas rankeadas",
    "05. Análisis de distribución real",
]
items_right = [
    "06. Caso de estudio: Venia en camino",
    "07. Excusas por audiencia objetivo",
    "08. La excusa perfecta — Modelo matemático",
    "09. Contraindicaciones",
    "10. Conclusiones & Certificación",
]
y = Inches(2.3)
for item in items_left:
    add_rect(sl, Inches(0.7), y, Inches(5.6), Inches(0.4), RGBColor(0x1A, 0x3A, 0x6E))
    txb(sl, item, Inches(0.85), y + Inches(0.04), Inches(5.4), Inches(0.38), size=14, color=GRAY)
    y += Inches(0.5)

y = Inches(2.3)
for item in items_right:
    add_rect(sl, Inches(6.9), y, Inches(6.0), Inches(0.4), RGBColor(0x1A, 0x3A, 0x6E))
    txb(sl, item, Inches(7.05), y + Inches(0.04), Inches(5.8), Inches(0.38), size=14, color=GRAY)
    y += Inches(0.5)

# ════════════════════════════════════════════════════
# SLIDE 3 — JUSTIFICACIÓN
# ════════════════════════════════════════════════════
sl = add_slide(BG_TEAL)
kicker(sl, "Justificación")
title(sl, "¿Por Qué Estudiar Este Fenómeno?")

stats = [
    ("100%", "de los presentes han llegado tarde alguna vez"),
    ("0%",   "nunca ha llegado tarde\n(el otro 0% miente)"),
    ("∞",    "excusas posibles para una sola tardanza"),
]
xs = [Inches(0.7), Inches(4.7), Inches(8.7)]
for i, (num, label) in enumerate(stats):
    x = xs[i]
    add_rect(sl, x, Inches(2.2), Inches(3.5), Inches(2.5), RGBColor(0x0D, 0x40, 0x40))
    txb(sl, num, x, Inches(2.4), Inches(3.5), Inches(1.2),
        size=48, bold=True, color=BLUE, align=PP_ALIGN.CENTER)
    txb(sl, label, x, Inches(3.5), Inches(3.5), Inches(1.0),
        size=12, color=MUTED, align=PP_ALIGN.CENTER)

add_rect(sl, Inches(0.7), Inches(5.1), Inches(0.06), Inches(0.7), GOLD)
txb(sl, "Pregunta de investigación: ¿Existe una excusa óptima? ¿Puede estandarizarse, replicarse\ny certificarse ante organismos internacionales?",
    Inches(0.9), Inches(5.0), Inches(11.2), Inches(0.9),
    size=14, color=GRAY)

txb(sl, "Fuente: Instituto Mexicano de Investigaciones sobre Puntualidad (IMIP), 2023. Dato completamente inventado.",
    Inches(0.7), Inches(6.6), Inches(11.6), Inches(0.4),
    size=9, italic=True, color=RGBColor(0x33, 0x55, 0x44))

# ════════════════════════════════════════════════════
# SLIDE 4 — TAXONOMÍA
# ════════════════════════════════════════════════════
sl = add_slide(BG_DARK)
kicker(sl, "Marco Teórico")
title(sl, "Taxonomía de Excusas — Clasificación Oficial")

headers = ["Categoría", "Ejemplo Canónico", "Veredicto Científico", "Cara dura req."]
col_x   = [Inches(0.5), Inches(3.0), Inches(6.5), Inches(10.8)]
col_w   = [Inches(2.4), Inches(3.4), Inches(4.2), Inches(2.2)]

# header row
add_rect(sl, Inches(0.5), Inches(2.0), Inches(12.5), Inches(0.45), RGBColor(0x1A, 0x3A, 0x5A))
for i, h in enumerate(headers):
    txb(sl, h.upper(), col_x[i], Inches(2.05), col_w[i], Inches(0.38),
        size=10, bold=True, color=BLUE)

rows = [
    ("⛈ Fuerza Mayor", "\"Había tráfico\"",               "Clásico, respetable, mentira",           "Baja"),
    ("💻 Técnica",      "\"Se me fue el cel\"",             "Inverificable. 10/10",                    "Muy baja"),
    ("😔 Emocional",    "\"Me senté un momento\"",          "Honesta. Completamente inaceptable.",    "Alta"),
    ("🧠 Existencial",  "\"Perdí la noción del tiempo\"",   "Filosófica. Nadie la puede rebatir.",    "Media"),
    ("☢ Nuclear",       "\"Tuve que ayudar a alguien\"",    "INMUNE. Nunca pregunten a quién.",       "Cero"),
]
risk_colors = [GOLD, GREEN, RED, GOLD, GREEN]

y = Inches(2.55)
for ri, (cat, ej, ver, risk) in enumerate(rows):
    bg = RGBColor(0x0D, 0x1B, 0x2A) if ri % 2 == 0 else RGBColor(0x11, 0x22, 0x33)
    add_rect(sl, Inches(0.5), y, Inches(12.5), Inches(0.55), bg)
    txb(sl, cat, col_x[0], y + Inches(0.06), col_w[0], Inches(0.45), size=13, color=BLUE)
    txb(sl, ej,  col_x[1], y + Inches(0.06), col_w[1], Inches(0.45), size=13, color=GRAY)
    txb(sl, ver, col_x[2], y + Inches(0.06), col_w[2], Inches(0.45), size=13, color=GRAY)
    txb(sl, risk,col_x[3], y + Inches(0.06), col_w[3], Inches(0.45), size=13, color=risk_colors[ri])
    y += Inches(0.57)

# ════════════════════════════════════════════════════
# SLIDE 5 — METODOLOGÍA / EJES CCETC
# ════════════════════════════════════════════════════
sl = add_slide(BG_NAVY)
kicker(sl, "Metodología")
title(sl, "Ejes de Evaluación — Modelo CCETC")

ejes = [
    ("Creatividad",    "¿Es original o ya la escucharon 40 veces?"),
    ("Credibilidad",   "¿Puede alguien verificarla sin que te dé infarto?"),
    ("Escalabilidad",  "¿Funciona con 5 min de retraso y también con 45?"),
    ("Preparación",    "¿Cuánto tiempo necesitas para contarla con convicción?"),
    ("Cara dura",      "¿Puedes mirar a los ojos mientras la dices?"),
]

y = Inches(2.3)
for eje, desc in ejes:
    add_rect(sl, Inches(0.7), y, Inches(0.05), Inches(0.4), BLUE)
    txb(sl, eje,  Inches(0.9), y,              Inches(2.5), Inches(0.42), size=15, bold=True, color=BLUE)
    txb(sl, desc, Inches(3.5), y,              Inches(9.5), Inches(0.42), size=14, color=GRAY)
    y += Inches(0.55)

add_rect(sl, Inches(0.7), Inches(5.5), Inches(0.05), Inches(0.6), BLUE)
txb(sl, "Validado por el Journal of Strategic Lateness, Vol. 3, 2024.\n*Revista ficticia con ISSN real por error tipográfico.",
    Inches(0.9), Inches(5.5), Inches(11.0), Inches(0.65),
    size=11, italic=True, color=MUTED)

# ════════════════════════════════════════════════════
# SLIDE 6 — TOP 5
# ════════════════════════════════════════════════════
sl = add_slide(BG_DARK)
kicker(sl, "Resultados")
title(sl, "Top 5 Excusas Rankeadas")

bars = [
    ("#1 — Nuclear: \"ayudé a alguien\"",    96, GREEN),
    ("#2 — Técnica: \"el internet\"",         88, BLUE),
    ("#3 — Existencial: \"perdí el tiempo\"", 79, PURPLE),
    ("#4 — Fuerza mayor: tráfico",            61, GOLD),
    ("#5 — Emocional: \"me senté\"",          12, RED),
]

y = Inches(2.2)
bar_max_w = Inches(8.0)
for label, score, color in bars:
    txb(sl, label, Inches(0.7), y, Inches(3.8), Inches(0.45), size=13, color=GRAY)
    add_rect(sl, Inches(4.7), y + Inches(0.05), bar_max_w, Inches(0.36),
             RGBColor(0x22, 0x33, 0x44))
    add_rect(sl, Inches(4.7), y + Inches(0.05), int(bar_max_w * score / 100), Inches(0.36), color)
    txb(sl, str(score), Inches(4.7) + int(bar_max_w * score / 100) + Inches(0.1),
        y, Inches(0.8), Inches(0.45), size=13, bold=True, color=color)
    y += Inches(0.75)

txb(sl, "Scores calculados con metodología CCETC v2.1  ·  Margen de error: ±∞  ·  Reproducibilidad: alta (si tienes la misma cara dura)",
    Inches(0.7), Inches(6.6), Inches(11.6), Inches(0.5),
    size=9, italic=True, color=RGBColor(0x33, 0x44, 0x55))

# ════════════════════════════════════════════════════
# SLIDE 7 — DISTRIBUCIÓN REAL (PIE texto)
# ════════════════════════════════════════════════════
sl = add_slide(BG_TEAL)
kicker(sl, "Análisis de Datos")
title(sl, "Distribución Real de Causas de Tardanza")

# Big donut-like visual with text
add_rect(sl, Inches(0.7), Inches(2.2), Inches(5.5), Inches(3.5), RGBColor(0x0A, 0x30, 0x30))
txb(sl, "87%", Inches(0.7), Inches(2.5), Inches(5.5), Inches(1.8),
    size=72, bold=True, color=RED, align=PP_ALIGN.CENTER)
txb(sl, "Me quedé dormido / perdí la noción",
    Inches(0.7), Inches(4.0), Inches(5.5), Inches(0.6),
    size=14, color=GRAY, align=PP_ALIGN.CENTER)

add_rect(sl, Inches(6.5), Inches(2.2), Inches(6.5), Inches(1.5), RGBColor(0x0A, 0x30, 0x30))
txb(sl, "13%  →  \"Otras razones\"",
    Inches(6.7), Inches(2.35), Inches(6.1), Inches(0.5),
    size=18, bold=True, color=BLUE)
txb(sl, "(tráfico / emergencias / lo que dije en público)",
    Inches(6.7), Inches(2.85), Inches(6.1), Inches(0.5),
    size=11, italic=True, color=MUTED)

add_rect(sl, Inches(6.5), Inches(3.95), Inches(0.05), Inches(1.2), RED)
txb(sl, "Hallazgo crítico: El 91.3% reportó haber usado \"el tráfico\"\ncomo excusa en al menos una ocasión donde no había salido a tiempo.\nEl 8.7% restante no recordaba.",
    Inches(6.7), Inches(3.95), Inches(6.2), Inches(1.3),
    size=13, color=GRAY)

txb(sl, "N=247 encuestados ficticios  ·  Desviación estándar: considerable  ·  Aprobado por Comité de Ética: pendiente",
    Inches(0.7), Inches(6.65), Inches(11.6), Inches(0.4),
    size=9, italic=True, color=RGBColor(0x33, 0x55, 0x44))

# ════════════════════════════════════════════════════
# SLIDE 8 — CASO DE ESTUDIO
# ════════════════════════════════════════════════════
sl = add_slide(BG_WINE)
kicker(sl, "Caso de Estudio — Vol. 1")
title(sl, "\"Venía en Camino\" — Análisis Forense")

# Left column
add_rect(sl, Inches(0.7), Inches(2.1), Inches(5.9), Inches(0.4), RGBColor(0x0A, 0x35, 0x1A))
txb(sl, "✅  Cuándo ES verdad", Inches(0.8), Inches(2.15), Inches(5.7), Inches(0.35),
    size=14, bold=True, color=GREEN)

truths = [
    "Ya saliste de casa",
    "Estás en el transporte",
    "Maps muestra \"en camino\"",
    "Hay testigos del punto de partida",
]
y = Inches(2.6)
for t in truths:
    add_rect(sl, Inches(0.7), y, Inches(5.9), Inches(0.42), RGBColor(0x08, 0x28, 0x14))
    txb(sl, "→  " + t, Inches(0.85), y + Inches(0.04), Inches(5.6), Inches(0.38),
        size=13, color=GRAY)
    y += Inches(0.45)
txb(sl, "✔ Efectividad: 94.2%  ·  Riesgo: bajo", Inches(0.7), y + Inches(0.05),
    Inches(5.9), Inches(0.4), size=12, color=GREEN)

# Right column
add_rect(sl, Inches(7.1), Inches(2.1), Inches(5.9), Inches(0.4), RGBColor(0x35, 0x0A, 0x0A))
txb(sl, "⚠  Cuándo es estrategia", Inches(7.2), Inches(2.15), Inches(5.7), Inches(0.35),
    size=14, bold=True, color=RED)

lies = [
    "Acabas de despertar y lo mandas por texto",
    "\"Camino\" = buscar las llaves 20 min",
    "Enviado mientras sigues desayunando",
    "El Maps no lo has abierto",
]
y = Inches(2.6)
for l in lies:
    add_rect(sl, Inches(7.1), y, Inches(5.9), Inches(0.42), RGBColor(0x28, 0x08, 0x08))
    txb(sl, "→  " + l, Inches(7.25), y + Inches(0.04), Inches(5.6), Inches(0.38),
        size=13, color=GRAY)
    y += Inches(0.45)
txb(sl, "⚠ Riesgo: alto si el otro tiene Maps compartido", Inches(7.1), y + Inches(0.05),
    Inches(5.9), Inches(0.4), size=12, color=RED)

add_rect(sl, Inches(0.7), Inches(5.8), Inches(0.05), Inches(0.65), GOLD)
txb(sl, "Recomendación técnica: Si vas a usar esta excusa en modalidad estratégica, abrir Maps primero.\nAsí técnicamente \"estás viendo el camino\".",
    Inches(0.9), Inches(5.8), Inches(12.0), Inches(0.7),
    size=13, color=GRAY)

# ════════════════════════════════════════════════════
# SLIDE 9 — POR AUDIENCIA
# ════════════════════════════════════════════════════
sl = add_slide(BG_NAVY)
kicker(sl, "Segmentación de Mercado")
title(sl, "Excusas por Audiencia Objetivo")

aud_headers = ["Audiencia", "Excusa recomendada", "Por qué funciona", "Riesgo latente"]
col_x2 = [Inches(0.5), Inches(2.6), Inches(5.4), Inches(8.7)]
col_w2 = [Inches(2.0), Inches(2.7), Inches(3.2), Inches(4.3)]

add_rect(sl, Inches(0.5), Inches(2.0), Inches(12.5), Inches(0.42), RGBColor(0x1A, 0x3A, 0x5A))
for i, h in enumerate(aud_headers):
    txb(sl, h.upper(), col_x2[i], Inches(2.05), col_w2[i], Inches(0.35),
        size=10, bold=True, color=BLUE)

aud_rows = [
    ("👔 Tu jefe",        "Técnica / Fuerza Mayor",    "No puede verificar tráfico ni señal",       "Que pregunte detalles"),
    ("👩 Tu mamá",        "Emocional (con cuidado)",   "Le llega al corazón... momentáneamente",    "Memoria perfecta. Recuerda TODO."),
    ("👫 Tus amigos",     "Cualquiera / ninguna",      "Ya saben quién eres. No les importa.",      "Ya esperaban 30 min extra de base"),
    ("💍 Tu pareja",      "Nuclear obligatorio",       "Única categoría con inmunidad parcial",     "¿Quién? ¿Dónde? ¿Con quién?"),
    ("🎂 Evento familiar","Fuerza Mayor + infantil",   "\"El niño/perro\" desactiva todo juicio",   "Solo si tienes niño/perro"),
]
risk_c2 = [GOLD, RED, GREEN, RED, GREEN]

y = Inches(2.5)
for ri, row in enumerate(aud_rows):
    bg = RGBColor(0x0F, 0x20, 0x44) if ri % 2 == 0 else RGBColor(0x13, 0x28, 0x50)
    add_rect(sl, Inches(0.5), y, Inches(12.5), Inches(0.52), bg)
    for ci, (val, cx, cw) in enumerate(zip(row, col_x2, col_w2)):
        col = risk_c2[ri] if ci == 3 else (BLUE if ci == 0 else GRAY)
        txb(sl, val, cx, y + Inches(0.06), cw, Inches(0.42), size=12, color=col)
    y += Inches(0.54)

# ════════════════════════════════════════════════════
# SLIDE 10 — FÓRMULA
# ════════════════════════════════════════════════════
sl = add_slide(BG_DARK)
kicker(sl, "Modelo Matemático")
title(sl, "La Excusa Perfecta — Formulación")

add_rect(sl, Inches(1.5), Inches(2.2), Inches(10.0), Inches(1.4), RGBColor(0x05, 0x10, 0x1A))
txb(sl, "E_opt  =  (C × Kα)  /  (R_d + ε)  ·  Φβ",
    Inches(1.5), Inches(2.3), Inches(10.0), Inches(1.2),
    size=32, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

vars_left = [
    ("C",  "Creatividad de la excusa (0–10)"),
    ("Kα", "Coeficiente de cara dura del emisor"),
    ("Rd", "Riesgo de detección (función del receptor)"),
]
vars_right = [
    ("ε",  "Margen de error emocional del momento"),
    ("Φβ", "Factor de historial previo con esa persona"),
    ("→ 0","Si Φβ tiende a cero: ninguna excusa funciona ya"),
]

y = Inches(3.85)
for sym, desc in vars_left:
    txb(sl, sym,  Inches(1.0), y, Inches(0.8), Inches(0.44), size=16, bold=True, color=BLUE)
    txb(sl, "=  " + desc, Inches(1.9), y, Inches(4.6), Inches(0.44), size=14, color=GRAY)
    y += Inches(0.5)

y = Inches(3.85)
for sym, desc in vars_right:
    txb(sl, sym,  Inches(6.8), y, Inches(0.8), Inches(0.44), size=16, bold=True, color=BLUE)
    txb(sl, "=  " + desc, Inches(7.7), y, Inches(5.3), Inches(0.44), size=14, color=GRAY)
    y += Inches(0.5)

add_rect(sl, Inches(0.7), Inches(5.7), Inches(0.05), Inches(0.8), BLUE)
txb(sl, "Corolario de Guillén: Cuando Φβ → 0 (4 tardanzas seguidas), el sistema colapsa.\nLa única salida: llegar 20 min antes la próxima vez y no decir nada.",
    Inches(0.9), Inches(5.7), Inches(11.5), Inches(0.85),
    size=13, color=GRAY)

txb(sl, "Guillén, S. (2026). \"Towards a Unified Theory of Strategic Lateness.\" arXiv:2026.xxxxx [cs.EXCUSE]. Pre-print. No revisado por pares.",
    Inches(0.7), Inches(6.7), Inches(11.6), Inches(0.4),
    size=9, italic=True, color=RGBColor(0x33, 0x44, 0x55))

# ════════════════════════════════════════════════════
# SLIDE 11 — CONTRAINDICACIONES
# ════════════════════════════════════════════════════
sl = add_slide(BG_WINE)
kicker(sl, "Advertencias de Seguridad")
title(sl, "Contraindicaciones — Leer Antes de Aplicar")

# Red column
add_rect(sl, Inches(0.6), Inches(2.1), Inches(5.9), Inches(0.42), RGBColor(0x40, 0x08, 0x08))
txb(sl, "⛔  NO funciona si...", Inches(0.7), Inches(2.15), Inches(5.7), Inches(0.35),
    size=14, bold=True, color=RED)
no_items = [
    "Llevas +3 tardanzas con la misma audiencia",
    "Alguien ya llegó más tarde que tú ese día",
    "Tu cara no aguanta la historia",
    "Hay evidencia digital (GPS, WhatsApp seen)",
    "Usaste la misma excusa la semana anterior",
]
y = Inches(2.62)
for item in no_items:
    add_rect(sl, Inches(0.6), y, Inches(5.9), Inches(0.44), RGBColor(0x2A, 0x06, 0x06))
    txb(sl, "→  " + item, Inches(0.75), y + Inches(0.04), Inches(5.6), Inches(0.38),
        size=12, color=GRAY)
    y += Inches(0.46)

# Green column
add_rect(sl, Inches(7.0), Inches(2.1), Inches(5.9), Inches(0.42), RGBColor(0x06, 0x2E, 0x14))
txb(sl, "✅  Condiciones ideales", Inches(7.1), Inches(2.15), Inches(5.7), Inches(0.35),
    size=14, bold=True, color=GREEN)
yes_items = [
    "Primera tardanza del mes con esa audiencia",
    "Excusa creativa, nunca usada antes",
    "Llegas con algo (comida, detalle, buena noticia)",
    "La persona también ha llegado tarde contigo",
]
y = Inches(2.62)
for item in yes_items:
    add_rect(sl, Inches(7.0), y, Inches(5.9), Inches(0.44), RGBColor(0x06, 0x20, 0x0E))
    txb(sl, "→  " + item, Inches(7.15), y + Inches(0.04), Inches(5.6), Inches(0.38),
        size=12, color=GRAY)
    y += Inches(0.46)

add_rect(sl, Inches(0.6), Inches(5.8), Inches(0.05), Inches(0.65), GOLD)
txb(sl, "Pro tip no documentado: Llegar con tacos anula cualquier tardanza de hasta 45 minutos\nen el 98.7% de audiencias mexicanas.",
    Inches(0.8), Inches(5.8), Inches(12.0), Inches(0.7),
    size=13, bold=True, color=GOLD)

# ════════════════════════════════════════════════════
# SLIDE 12 — CONCLUSIONES
# ════════════════════════════════════════════════════
sl = add_slide(BG_GREEN)
kicker(sl, "Conclusiones")
title(sl, "Síntesis Ejecutiva")

conclusions = [
    "La excusa nuclear (\"tuve que ayudar\") es la única con inmunidad universal demostrada",
    "El 87% de las tardanzas tienen causa idéntica, independientemente de la excusa reportada",
    "La excusa perfecta no existe — existe la persona perfecta que la recibe",
    "Llegar con tacos supera cualquier modelo teórico sin excepción",
    "\"La mejor excusa es la que nunca tendrás que usar... pero igual prepara dos\"",
]
y = Inches(2.2)
for c in conclusions:
    add_rect(sl, Inches(0.7), y, Inches(0.05), Inches(0.44), BLUE)
    txb(sl, c, Inches(0.9), y, Inches(11.0), Inches(0.5), size=15, color=GRAY)
    y += Inches(0.62)

add_rect(sl, Inches(7.5), Inches(4.5), Inches(5.2), Inches(1.8), RGBColor(0x06, 0x25, 0x12))
txb(sl, "🏆  Excusa del Año 2026",
    Inches(7.6), Inches(4.6), Inches(5.0), Inches(0.45),
    size=13, bold=True, color=BLUE)
txb(sl, "\"Me avisaron de último momento\npero venía en camino\"",
    Inches(7.6), Inches(5.0), Inches(5.0), Inches(0.85),
    size=16, bold=True, color=WHITE)
txb(sl, "Híbrido Nuclear-Técnica  ·  Score: 94.1  ·  Riesgo: muy bajo",
    Inches(7.6), Inches(5.85), Inches(5.0), Inches(0.35),
    size=10, color=MUTED)

# ════════════════════════════════════════════════════
# SLIDE 13 — CERTIFICADO
# ════════════════════════════════════════════════════
sl = add_slide(BG_DARK)
kicker(sl, "Acto de Clausura")

add_rect(sl, Inches(1.8), Inches(1.2), Inches(9.7), Inches(5.5), RGBColor(0x10, 0x10, 0x10))
# Gold border simulation
add_rect(sl, Inches(1.85), Inches(1.25), Inches(9.6), Inches(0.05), RGBColor(0xD4, 0xAF, 0x37))
add_rect(sl, Inches(1.85), Inches(6.65), Inches(9.6), Inches(0.05), RGBColor(0xD4, 0xAF, 0x37))
add_rect(sl, Inches(1.85), Inches(1.25), Inches(0.05), Inches(5.45), RGBColor(0xD4, 0xAF, 0x37))
add_rect(sl, Inches(11.4), Inches(1.25), Inches(0.05), Inches(5.45), RGBColor(0xD4, 0xAF, 0x37))

txb(sl, "EL COMITÉ DE JUSTIFICACIONES TARDÍAS DE AMÉRICA LATINA · CJTAL · CERTIFICA QUE",
    Inches(2.0), Inches(1.6), Inches(9.3), Inches(0.5),
    size=10, bold=True, color=RGBColor(0xD4, 0xAF, 0x37), align=PP_ALIGN.CENTER)

txb(sl, "Sergio Guillén",
    Inches(2.0), Inches(2.2), Inches(9.3), Inches(1.2),
    size=48, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

txb(sl, "ha completado satisfactoriamente el\nPrograma de Certificación en Gestión Estratégica de la Impuntualidad\nhabiendo llegado puntual a esta presentación sobre impuntualidad,\nlo cual representa un logro estadísticamente improbable.",
    Inches(2.0), Inches(3.5), Inches(9.3), Inches(1.6),
    size=13, color=GRAY, align=PP_ALIGN.CENTER)

txb(sl, "* Los asistentes que llegaron tarde recibirán su certificado en cuanto terminen de explicar por qué.",
    Inches(2.0), Inches(5.1), Inches(9.3), Inches(0.45),
    size=10, italic=True, color=RGBColor(0x55, 0x55, 0x55), align=PP_ALIGN.CENTER)

txb(sl, "📜  ✦  CJTAL  ✦  2026",
    Inches(2.0), Inches(5.6), Inches(9.3), Inches(0.6),
    size=18, bold=True, color=RGBColor(0xD4, 0xAF, 0x37), align=PP_ALIGN.CENTER)

txb(sl, "Preguntas  ·  Anécdotas  ·  Defensa pública de excusas personales",
    Inches(0.7), Inches(6.8), Inches(11.6), Inches(0.4),
    size=11, italic=True, color=RGBColor(0x44, 0x44, 0x44), align=PP_ALIGN.CENTER)

# ════════════════════════════════════════════════════
out = "/Users/sergioguillen/.openclaw/workspace/Excusas_CJTAL_2026.pptx"
prs.save(out)
print(f"Saved: {out}")
