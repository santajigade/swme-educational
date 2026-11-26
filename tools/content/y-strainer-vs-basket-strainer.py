META = {
    "category": "industrial-valve-guides",
    "title": "Y Strainer vs Basket Strainer: How to Choose",
    "keyword": "y strainer",
    "subtitle": "How Y and basket strainers are built, which way they must be installed, how dirt capacity and pressure drop compare, which screen to choose and when the screen needs cleaning",
    "meta_title": "Y Strainer vs Basket Strainer: How to Choose",
    "meta_description": "Y strainer vs basket strainer: construction, orientation, dirt capacity, pressure drop, open area ratio, mesh and perforation sizes, duplex units and cleaning.",
    "summary": "How a Y strainer and a basket strainer differ in construction, installation, dirt capacity and pressure drop, how to pick the screen, and when to clean it.",
    "card_title": "Y Strainer vs Basket Strainer",
    "author": "SWME Technical Staff",
    "published": "2026-11-26",
    "status": "published",
    "sort_order": 9,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "levels",
        "title": "Strainer Screens from Coarse to Fine",
        "alt": "Infographic ranking strainer screens from coarse to fine: 1/8 inch and 1/16 inch perforated plate, then 20, 60 and 200 mesh with their openings",
        "top_label": "Coarse",
        "bottom_label": "Fine",
        "levels": [
            ["1/8 in perforation", "0.125 in holes, 43% open area.", 0.92],
            ["1/16 in perforation", "0.062 in holes, 30% open area.", 0.7],
            ["20 mesh", "About 840 micron opening.", 0.48],
            ["60 mesh", "About 250 micron opening.", 0.27],
            ["200 mesh", "About 74 micron opening.", 0.06],
        ],
    },
}

_C = "#e67700"
_T = "#a35400"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


def _a(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#1864ab" stroke-width="2.5" marker-end="url(#fa)"/>'


def _yleg():
    import math
    u = (math.sqrt(0.5), math.sqrt(0.5))
    n = (-math.sqrt(0.5), math.sqrt(0.5))
    ox, oy = 190, 135

    def P(sv, nv):
        return (ox + sv * u[0] + nv * n[0], oy + sv * u[1] + nv * n[1])

    def pt(sv, nv):
        x, y = P(sv, nv)
        return f"{x:.1f},{y:.1f}"
    # wall offsets +-26 across the leg; walls start where they meet the pipe bottom (y = 160)
    # for wall nv, y = oy + (sv + nv) * 0.707 = 160  ->  sv = 25 / 0.707 - nv
    s_l = 25 / u[1] - 26   # wall on the inlet side (nv = +26)
    s_r = 25 / u[1] + 26   # wall on the outlet side (nv = -26)
    end = 175
    xl0, _ = P(s_l, 26)
    xr0, _ = P(s_r, -26)
    fill = f'<polygon points="{pt(s_l, 26)} {pt(end, 26)} {pt(end, -26)} {pt(s_r, -26)}" fill="#fff4e6"/>'
    out = ('<rect x="30" y="110" width="330" height="50" fill="#fff4e6"/>' + fill
           + '<line x1="30" y1="110" x2="360" y2="110" stroke="#495057" stroke-width="3"/>'
           + f'<line x1="30" y1="160" x2="{xl0:.1f}" y2="160" stroke="#495057" stroke-width="3"/>'
           + f'<line x1="{xr0:.1f}" y1="160" x2="360" y2="160" stroke="#495057" stroke-width="3"/>'
           + f'<polyline points="{pt(s_l, 26)} {pt(end, 26)}" fill="none" stroke="#495057" stroke-width="3"/>'
           + f'<polyline points="{pt(s_r, -26)} {pt(end, -26)}" fill="none" stroke="#495057" stroke-width="3"/>'
           + f'<polygon points="{pt(30, 17)} {pt(165, 17)} {pt(165, -17)} {pt(30, -17)}" fill="none" stroke="#e67700" stroke-width="2.5" stroke-dasharray="5,3"/>'
           + f'<polygon points="{pt(end, 32)} {pt(end + 12, 32)} {pt(end + 12, -32)} {pt(end, -32)}" fill="#adb5bd" stroke="#495057" stroke-width="2"/>'
           + f'<line x1="{P(end + 12, 0)[0]:.1f}" y1="{P(end + 12, 0)[1]:.1f}" x2="{P(end + 34, 0)[0]:.1f}" y2="{P(end + 34, 0)[1]:.1f}" stroke="#495057" stroke-width="4"/>'
           + f'<circle cx="{P(end + 40, 0)[0]:.1f}" cy="{P(end + 40, 0)[1]:.1f}" r="8" fill="#ffe8cc" stroke="#d9480f" stroke-width="2"/>')
    sx, sy = P(60, 0)
    ex, ey = P(150, 0)
    out += (_a(40, 135, 120, 135) + _a(130, 128, round(sx), round(sy))
            + _a(round(ex) + 10, round(ey) - 40, 300, 135) + _a(300, 135, 350, 135))
    vx, vy = P(end + 40, 0)
    out += (_t(215, 250, "Screen", 13, "700", _C, "end") + _t(215, 266, "(dashed)", 12, "400", "#555", "end")
            + _t(round(vx) - 20, round(vy) + 32, "Cap with blowdown valve", 12, "700", "#d9480f", "end"))
    return out


_diag = (
    '<defs><marker id="fa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#1864ab"/></marker></defs>'
    # ---------------- Y strainer
    + _t(200, 40, "Y strainer", 16, "700", _T)
    + _yleg()
    + _t(200, 352, "Liquid service: pocket pointing down", 12, "400", "#555")
    # ---------------- basket strainer
    + _t(600, 40, "Basket strainer", 16, "700", _T)
    # pot
    + '<rect x="505" y="90" width="170" height="240" rx="10" fill="#fff4e6" stroke="#495057" stroke-width="3"/>'
    + '<rect x="495" y="76" width="190" height="14" rx="3" fill="#adb5bd" stroke="#495057" stroke-width="2"/>'
    + _t(700, 74, "Cover", 12, "700", "#495057", "start")
    # inlet nozzle (high) and outlet nozzle (low)
    + '<rect x="420" y="110" width="88" height="44" fill="#fff4e6"/>'
    + '<line x1="420" y1="110" x2="505" y2="110" stroke="#495057" stroke-width="3"/><line x1="420" y1="154" x2="505" y2="154" stroke="#495057" stroke-width="3"/>'
    + '<rect x="672" y="236" width="98" height="44" fill="#fff4e6"/>'
    + '<line x1="675" y1="236" x2="770" y2="236" stroke="#495057" stroke-width="3"/><line x1="675" y1="280" x2="770" y2="280" stroke="#495057" stroke-width="3"/>'
    # basket seat and basket
    + '<line x1="505" y1="180" x2="535" y2="180" stroke="#495057" stroke-width="4"/><line x1="645" y1="180" x2="675" y2="180" stroke="#495057" stroke-width="4"/>'
    + '<path d="M535 180 L535 305 L645 305 L645 180" fill="none" stroke="#e67700" stroke-width="2.5" stroke-dasharray="5,3"/>'
    + _a(430, 132, 560, 132) + _a(575, 140, 575, 260)
    + _a(610, 250, 668, 250) + _a(690, 258, 760, 258)
    + _t(590, 325, "Basket", 13, "700", _C)
    + _t(600, 352, "Horizontal lines only", 12, "400", "#555")
    + _t(470, 102, "In", 12, "700", "#1864ab")
    + _t(730, 228, "Out", 12, "700", "#1864ab")
)

BODY = [
    takeaways([
        "A Y strainer is compact and strong, with some models good for 400 bar g, and fits horizontal lines or vertical lines with downward flow.",
        "A basket strainer holds more dirt and has a lower pressure drop size for size, but it only goes in horizontal lines.",
        "Aim for a screen open area about four times the pipe area, and choose perforation or mesh by the particle size you need to stop.",
        "Clean the screen when the differential pressure reaches about 5 to 10 psi; duplex basket strainers let you do it without stopping flow.",
    ]),
    p("A <strong>Y strainer</strong> and a basket strainer do the same job: they catch scale, weld slag and other debris before it reaches pumps, control valves, meters and steam traps. The " + ext("https://www.instrumentationblog.in/strainer-and-filter-difference/", "difference between a strainer and a filter") + " is mainly particle size, with strainers catching particles larger than about 75 to 100 microns. SWME supplies Y, basket and duplex " + link("/strainers", "strainers") + " alongside its range of " + link("/industrial-valves", "industrial valves") + "."),
    toc([("build", "How each strainer is built"), ("compare", "Y strainer vs basket strainer"), ("orientation", "Installation and orientation"),
         ("area", "Open area ratio"), ("screens", "Choosing the screen"), ("cleaning", "When to clean"), ("other", "Duplex and temporary strainers"),
         ("select", "Selection checklist"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("build", "How Each Strainer Is Built"),
    p("Spirax Sarco's guide to " + ext("https://www.spiraxsarco.com/learn-about-steam/pipeline-ancillaries/strainers", "pipeline strainers") + " describes the Y type body as a compact cylindrical shape that is very strong and can handle high pressures, often up to 400 bar g. The screen sits in the angled leg, and a blowdown valve can usually be fitted in the cap. A basket strainer has a vertical chamber, typically larger than a Y type, with a removable basket under a cover."),
    svg(_diag, "Flow paths through a Y strainer, with the screen in the angled leg, and a basket strainer, where flow enters the basket from the top and leaves through its wall", 365),
    p("Project Materials' overview of " + ext("https://blog.projectmaterials.com/valves/pipeline-strainers", "pipeline strainer types") + " notes that a basket strainer holds more debris than a Y strainer of the same size because its element is larger."),
    h2("compare", "Y Strainer vs Basket Strainer"),
    table(["Point", "Y strainer", "Basket strainer"], [
        ["Body", "Compact cylinder, very strong, some to 400 bar g", "Vertical chamber, larger than a Y type"],
        ["Line orientation", "Horizontal, or vertical with downward flow", "Horizontal only"],
        ["Dirt holding, size for size", "Lower", "Higher"],
        ["Pressure drop, size for size", "Higher", "Lower"],
        ["Cleaning", "Blowdown valve in the cap, or remove the screen", "Remove the cover and lift out the basket"],
        ["Continuous service", "Line must be isolated", "Duplex version switches between two baskets"],
    ]),
    p("Spirax gives one figure for scale: a DN40 Y strainer passing 500 kg/h of steam at 8 bar g has a pressure drop of just over 0.5%."),
    h2("orientation", "Installation and Orientation"),
    rows([
        ("Y strainer, liquid", "In horizontal lines the pocket should point vertically downwards (Spirax)."),
        ("Y strainer, steam or gas", "In horizontal lines the pocket should lie in the horizontal plane (Spirax)."),
        ("Y strainer, vertical line", "Only with downward flow (Spirax, Titan FCI)."),
        ("Basket strainer", "Horizontal lines only (Spirax, Keckley)."),
    ], "Which way round"),
    p("Put a strainer upstream of the equipment it protects. Our guide to " + link("/types-of-industrial-valves", "types of industrial valves") + " covers the valves usually installed around it, and the article on " + link("/blog/pump-protection-pressure-flow-temperature-instruments", "pump protection instruments") + " shows where a strainer fits in a pump suction."),
    h2("area", "Open Area Ratio"),
    p("Watts' " + ext("https://www.watts.com/dfsmedia/0533dbba17714b1ab581ab07a4cbb521/45904-source/s-ms-strainerfacts", "strainer facts sheet") + " says the open area of the screen or basket should be four times the cross sectional area of the pipe. Its example, a 3 inch Y strainer with 1/8 inch perforations, has 31.4 sq in of open area, a ratio of 4.25 to 1. Keckley's " + ext("https://cdn.shopify.com/s/files/1/0484/9575/5432/files/Keckley_Strainer_Screen_Options.pdf", "screen options sheet") + " gives the method: screen area times percent open area, divided by the pipe ID area. For a 2 inch Y strainer with 20 mesh that is 17.753 ÷ 3.356 = 5.29 to 1."),
    dyk("Watts calculates that a basket 50% clogged has twice the pressure drop of a clean one. In its example, 0.4 psi at 1,000 GPM of water becomes 0.8 psi."),
    h2("screens", "Choosing the Screen"),
    p("Screens are perforated plate, mesh, or mesh lined perforated plate. Spirax puts perforated hole sizes typically between 0.8 and 3.2 mm, and says mesh openings as small as 0.07 mm are possible."),
    INFOGRAPHIC,
    table(["Screen", "Opening", "Open area"], [
        ["1/4 in perforation", "0.25 in", "58%"],
        ["1/8 in perforation", "0.125 in", "43%"],
        ["1/16 in perforation", "0.062 in", "30%"],
        ["1/32 in perforation", "0.033 in", "29%"],
        ["20 mesh", "0.034 in, about 840 micron", "n/a"],
        ["60 mesh", "0.010 in, about 250 micron", "n/a"],
        ["100 mesh", "0.0055 in, about 149 micron", "n/a"],
        ["200 mesh", "0.0029 in, about 74 micron", "n/a"],
    ]),
    p("Perforation and mesh openings are from Keckley; micron values are from the " + ext("https://engineeringtoolbox.com/mesh-size-strainer-filter-particle-diameter-d_2182.html", "mesh size to particle size table") + ". For a starting point, Watts lists .062, .033 and .020 in as the coarse, medium and fine screens for steam and water lines from 1/4 to 2 inch, and 1/8, .062 and .045 in for water lines of 2 1/2 to 4 inch."),
    h2("cleaning", "When to Clean"),
    p("Mueller Steam Specialty's " + ext("https://res.cloudinary.com/wholesale-plumbing/image/upload/Documents2/Mueller_Steam_Specialty_758_4_Instruction_Installation_Manual.pdf", "Y strainer instruction manual") + " says the screen normally needs cleaning when differential pressure reaches 5 to 10 psi, and that a strainer with a blowdown valve can be flushed by opening it until the sediment is gone. Caleffi's " + ext("https://www.caleffi.com/en-us/node/2566", "note on strainer maintenance") + " puts the cleaning point at about 5 or 6 psi, warns against letting it go above 10 psi, and suggests recording the clean differential pressure at design flow as a baseline."),
    p("A pressure gauge on each side of the strainer shows the loss as it clogs. A single " + link("/differential-pressure-gauges", "differential pressure gauge") + " across the strainer reads it directly, as our " + link("/differential-pressure-gauges-explained", "differential pressure gauge guide") + " explains. For the clean loss at design flow, the " + ext("https://zentacalculator.com/engineering/minor-losses/", "minor losses calculator") + " works out head loss from a fitting K factor and velocity."),
    h2("other", "Duplex and Temporary Strainers"),
    twocol([
        ("Duplex basket strainer", "bi-arrow-left-right", ["Two baskets with a diverter valve", "One stays in service while the other is cleaned", "For lines that cannot be shut down"]),
        ("Temporary strainer", "bi-funnel", ["Conical, basket or plate type", "Protects equipment during start up", "Cone types can collapse under high differential pressure if left in"]),
    ]),
    h2("select", "Selection Checklist"),
    checklist([
        ("Check the line orientation", "Vertical with upward flow rules out both; vertical downward flow rules out a basket strainer."),
        ("Estimate the dirt load", "Heavy debris favours a basket strainer, which holds more."),
        ("Decide if flow can stop for cleaning", "If not, choose a duplex basket strainer."),
        ("Pick the screen", "Match the opening to the particle size the protected equipment can pass."),
        ("Check the open area ratio", "Aim for about four times the pipe area."),
        ("Plan for monitoring", "Fit gauges or a differential pressure gauge and set a cleaning point."),
    ]),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Installing a Y strainer pocket down on steam.", "On steam or gas the pocket should lie horizontal."),
        ("Putting a basket strainer in a vertical line.", "Basket strainers are for horizontal lines only."),
        ("Leaving a temporary cone strainer in place.", "It can collapse under high differential pressure."),
        ("Running until the screen is blocked.", "Pressure drop doubles at 50% clogged; clean at 5 to 10 psi."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Which has the lower pressure drop?", "Size for size, a basket strainer has a lower pressure drop than a Y strainer, according to Spirax Sarco."),
        ("Can a Y strainer go in a vertical pipe?", "Yes, if the flow is downwards."),
        ("What mesh is 840 micron?", "20 mesh, with an opening of about 0.034 in."),
    ]),
]
