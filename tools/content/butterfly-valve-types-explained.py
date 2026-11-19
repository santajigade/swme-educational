META = {
    "category": "industrial-valve-guides",
    "title": "Butterfly Valve Types Explained",
    "keyword": "butterfly valve types",
    "subtitle": "Concentric, double offset and triple offset designs, body styles, seats and how to choose",
    "meta_title": "Butterfly Valve Types Explained: Offsets and Bodies",
    "meta_description": "Butterfly valve types explained: concentric, double offset and triple offset designs, wafer, lug and flanged bodies, seats, API 609 and selection tips.",
    "summary": "How concentric, double offset and triple offset butterfly valves differ, plus wafer, lug and flanged bodies and how to choose.",
    "card_title": "Butterfly Valve Types",
    "author": "SWME Technical Staff",
    "published": "2026-11-19",
    "status": "published",
    "sort_order": 4,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "levels",
        "title": "Butterfly Valve Types by Duty",
        "alt": "Infographic ranking concentric, double offset and triple offset butterfly valves from utility duty to severe duty",
        "top_label": "Severe duty",
        "bottom_label": "Utility duty",
        "levels": [
            ["Concentric (zero offset)", "Resilient seat; water, HVAC, fire protection and low pressure utility service.", 0.15],
            ["Double offset", "Cam action cuts seat rubbing; cooling water, process water and moderate pressure process lines.", 0.5],
            ["Triple offset", "Conical metal seat touches only at closure; hydrocarbon, steam and high temperature service.", 0.85],
        ],
    },
}

_C = "#e67700"
_T = "#a35400"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


def _panel(x0, title, sx, sy, conical=False, sub=()):
    """Side view along the shaft, valve closed. Pipe bore from y=80 to y=240, centre y=160.
    Disc sits in the seat plane at x0+120; shaft (circle) at (sx, sy)."""
    cx = x0 + 120
    out = [_t(x0 + 120, 34, title, 15)]
    # pipe walls
    out.append(f'<rect x="{x0 + 10}" y="66" width="220" height="14" fill="#dee2e6" stroke="#495057" stroke-width="1.5"/>')
    out.append(f'<rect x="{x0 + 10}" y="240" width="220" height="14" fill="#dee2e6" stroke="#495057" stroke-width="1.5"/>')
    # pipe centreline
    out.append(f'<line x1="{x0 + 14}" y1="160" x2="{x0 + 226}" y2="160" stroke="#868e96" stroke-width="1" stroke-dasharray="6 4"/>')
    # seat plane
    out.append(f'<line x1="{cx}" y1="84" x2="{cx}" y2="236" stroke="#868e96" stroke-width="1" stroke-dasharray="2 3"/>')
    if conical:
        # angled seat faces and disc with conical edges
        out.append(f'<polygon points="{cx - 12},80 {cx + 12},80 {cx + 12},100 {cx + 8},98 {cx - 8},90 {cx - 12},88" fill="#495057"/>')
        out.append(f'<polygon points="{cx - 12},240 {cx + 12},240 {cx + 12},220 {cx + 8},222 {cx - 8},230 {cx - 12},232" fill="#495057"/>')
        out.append(f'<polygon points="{cx - 8},90 {cx + 8},98 {cx + 8},222 {cx - 8},230" fill="#ffd8a8" stroke="{_C}" stroke-width="2"/>')
    else:
        out.append(f'<rect x="{cx - 9}" y="80" width="18" height="10" fill="#343a40"/>')
        out.append(f'<rect x="{cx - 9}" y="230" width="18" height="10" fill="#343a40"/>')
        out.append(f'<rect x="{cx - 7}" y="90" width="14" height="140" fill="#ffd8a8" stroke="{_C}" stroke-width="2"/>')
    # shaft and its connection to the disc
    if sx != cx:
        out.append(f'<rect x="{min(cx, sx)}" y="{sy - 7}" width="{abs(sx - cx)}" height="14" fill="#ffd8a8" stroke="{_C}" stroke-width="1.5"/>')
    out.append(f'<circle cx="{sx}" cy="{sy}" r="10" fill="#495057"/>')
    out.append(f'<circle cx="{sx}" cy="{sy}" r="3" fill="#fff"/>')
    # flow arrow
    out.append(f'<line x1="{x0 + 24}" y1="110" x2="{x0 + 70}" y2="110" stroke="#1971c2" stroke-width="2.5" marker-end="url(#ahv)"/>')
    out.append(_t(x0 + 47, 102, "Flow", 11, "700", "#1971c2"))
    for k, line in enumerate(sub):
        out.append(_t(x0 + 120, 284 + k * 18, line, 12, "400", "#495057"))
    return "".join(out)


_diag = (
    '<defs><marker id="ahv" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="#1971c2"/></marker></defs>'
    + _panel(10, "Concentric", 130, 160, sub=("Shaft on the disc and", "on the pipe centreline", "Seat rubs through full stroke"))
    + _panel(280, "Double offset", 430, 186, sub=("Offset 1: shaft behind seat", "Offset 2: shaft off pipe", "centreline (cam action)"))
    + _panel(550, "Triple offset", 700, 186, conical=True, sub=("Offsets 1 and 2, plus", "Offset 3: conical seat", "Contact only at closure"))
)

BODY = [
    takeaways([
        "A butterfly valve is a quarter turn valve with a disc that rotates on a shaft in the flow stream.",
        "The three main butterfly valve types are concentric, double offset and triple offset.",
        "Each added offset reduces seat rubbing, which allows harder seats, higher pressure and higher temperature.",
        "Body style (wafer, lug or double flanged) decides how the valve bolts into the line and whether it can serve as a line end.",
    ]),
    p("Butterfly valves are light, compact and quick to operate, which makes them a common choice for large lines. But a rubber lined water valve and a metal seated steam valve are very different products. Knowing the main <strong>butterfly valve types</strong> helps you match the design to the pressure, temperature and shutoff the line needs.",
      "SWME supplies " + link("/butterfly-valves", "butterfly valves") + " and the full range of " + link("/industrial-valves", "industrial valves") + " for oil and gas, utilities and process plants in the UAE."),
    toc([("basics", "How a butterfly valve works"), ("types", "Butterfly valve types by offset"), ("compare", "Comparison table"),
         ("bodies", "Body styles"), ("select", "Selection checklist"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("basics", "How a Butterfly Valve Works"),
    p("" + ext("https://www.fabrico.io/blog/butterfly-valve/", "Fabrico") + " describes the butterfly valve as a quarter turn valve that uses a rotating disc mounted on a shaft through the pipe. In the closed position the disc edge presses against the seat to seal. Because the disc and shaft stay in the flow stream, there is some permanent pressure loss even when the valve is fully open. Operation is by handle, gearbox, pneumatic or electric actuator."),
    rows([
        ("Disc", "The closing member; it turns 90 degrees from fully closed to fully open."),
        ("Shaft", "Carries the disc and transmits torque from the operator."),
        ("Seat", "Resilient (EPDM, NBR or Viton), soft polymer or metal, depending on the type."),
        ("Throttling", "Fabrico limits throttling to roughly 20 to 70 degrees of disc rotation."),
    ], "Main parts"),
    h2("types", "Butterfly Valve Types by Offset"),
    p("The types are named after where the shaft sits relative to the disc, the seat and the pipe. " + ext("https://blog.projectmaterials.com/quick-answers/valves/butterfly-valve-offset-types/", "Project Materials") + " explains the three offsets. In the first, the shaft moves behind the plane of the seat. In the second, it moves off the centreline of the pipe bore, which creates a cam action on closure. In the third, the seating surface is machined to a conical profile, so contact occurs only at final closure."),
    INFOGRAPHIC,
    svg(_diag, "Side view of a closed concentric, double offset and triple offset butterfly valve showing where the shaft and seat sit", 340),
    h2("compare", "Comparison Table"),
    table(["Point", "Concentric", "Double offset", "Triple offset"],
          [["Seat contact", "Rubs through full stroke", "Reduced rubbing, cam action", "Contact only at final closure"],
           ["Seat", "Resilient", "Resilient or metal", "Metal"],
           ["Typical class", "Class 150", "Class 150 to 300", "Class 150 to 900"],
           ["API 609", "Category A", "Category A or B", "Category B"],
           ["Typical use", "Water, HVAC, fire protection", "Cooling and process water", "Hydrocarbon, steam, high temperature"]]),
    p("Figures follow Project Materials, which also lists ASME B16.34 for pressure and temperature ratings and ASME B16.10 for face to face dimensions. It advises against resilient seated concentric valves for hydrocarbon service above 200 degrees C. Always confirm the rating on the valve datasheet."),
    dyk("Actuators are sized on breakaway torque, the torque needed to unseat the disc. Fabrico notes that mid stroke torque is lower, and that resilient seats gain breakaway torque as they age, so size with margin. For flow capacity, use the " + ext("https://zentacalculator.com/engineering/control-valve-kv-cv/", "control valve Kv and Cv calculator") + "."),
    h2("bodies", "Body Styles"),
    twocol([
        ("Wafer", "bi-layout-split", ["Clamped between two pipe flanges", "Bolts pass through the whole assembly", "Compact face to face length", "Cannot isolate one side on its own"]),
        ("Lug", "bi-nut", ["Threaded lugs bolt each side to its own flange", "Suits dead end service", "Check the dead end rating"]),
    ]),
    p("Double flanged bodies have integral flanges on both ends and are used in larger sizes or higher pressure service beyond wafer and lug ratings, according to Fabrico."),
    h2("select", "Selection Checklist"),
    checklist([
        ("Service", "Define fluid, pressure class and maximum temperature first."),
        ("Shutoff", "Resilient seats give bubble tight shutoff; metal seats need a triple offset for tight closure."),
        ("Duty", "Isolation or throttling; for control duty see our " + link("/pneumatic-control-valves", "pneumatic control valves") + "."),
        ("Body", "Wafer, lug or double flanged to suit the piping and maintenance plan."),
        ("Operator", "Lever, gearbox or actuator sized on breakaway torque."),
    ]),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Using a rubber seated valve in hot hydrocarbon service.", "Choose a triple offset metal seated design instead."),
        ("Fitting a wafer valve at a line end.", "Use a lug body rated for dead end service."),
        ("Throttling near the closed position.", "Keep control within the usable opening range to protect the seat."),
    ]),
    p("For a wider overview, read " + link("/types-of-industrial-valves", "types of industrial valves") + " and our " + link("/blog/how-to-select-the-right-industrial-valve", "valve selection post") + ". For quarter turn alternatives, see " + link("/floating-vs-trunnion-ball-valves", "floating vs trunnion ball valves") + ", and check line losses with the " + ext("https://zentacalculator.com/engineering/minor-losses/", "minor losses calculator") + "."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What are the main butterfly valve types?", "Concentric (zero offset), double offset (high performance) and triple offset."),
        ("Why is it called triple offset?", "Two shaft offsets plus a conical seat, so the disc touches the seat only at final closure."),
        ("Wafer or lug: which do I need?", "A lug body when the valve must hold pressure with one side unbolted; a wafer body otherwise."),
    ]),
]
