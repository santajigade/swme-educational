META = {
    "category": "industrial-valve-guides",
    "title": "Check Valve Types Explained",
    "keyword": "check valve",
    "subtitle": "How swing, lift, ball, dual plate, tilting disc and silent check valves stop backflow, and how to pick and install one",
    "meta_title": "Check Valve Types Explained",
    "meta_description": "Check valve types explained: swing, lift, ball, dual plate, tilting disc and silent checks, cracking pressure, slam, standards, orientation and mistakes.",
    "summary": "How each check valve type stops reverse flow, which ones resist slam and water hammer, and how orientation and sizing affect the choice.",
    "card_title": "Check Valve Types",
    "author": "SWME Technical Staff",
    "published": "2026-11-20",
    "status": "published",
    "sort_order": 5,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "steps",
        "title": "How a Check Valve Works",
        "alt": "Infographic showing four steps of check valve operation from cracking open to closing before reverse flow",
        "steps": [
            ["Cracking open", "Upstream pressure reaches the cracking pressure and lifts the disc off its seat."],
            ["Forward flow", "Flow holds the disc open; the valve does not regulate the flow."],
            ["Flow slows", "As the pump stops, flow falls and the disc starts to return."],
            ["Closed in time", "The disc must seat before line flow reaches zero to avoid slam."],
        ],
    },
}

_C = "#e67700"
_T = "#a35400"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_diag = (
    '<defs><marker id="ahc" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="#1971c2"/></marker></defs>'
    # ---- left panel: swing check
    + _t(200, 30, "Swing check (closed)", 14, anchor="middle")
    + '<line x1="20" y1="150" x2="380" y2="150" stroke="#495057" stroke-width="3"/>'
    + '<line x1="20" y1="250" x2="380" y2="250" stroke="#495057" stroke-width="3"/>'
    + '<path d="M120 150 Q200 70 280 150" fill="#fff4e6" stroke="#495057" stroke-width="3"/>'
    + _t(200, 100, "Cover", 12, "400", "#555", anchor="middle")
    # inclined seat ring
    + '<line x1="175" y1="152" x2="195" y2="248" stroke="#868e96" stroke-width="6"/>'
    # hinge pin and disc hanging on seat
    + '<circle cx="190" cy="140" r="6" fill="#343a40"/>'
    + '<line x1="190" y1="140" x2="205" y2="160" stroke="#343a40" stroke-width="3"/>'
    + '<rect x="198" y="158" width="12" height="86" rx="4" fill="' + _C + '" transform="rotate(-12 204 200)"/>'
    + _t(296, 128, "Hinge pin", 12, "400", "#555")
    + '<line x1="294" y1="124" x2="198" y2="139" stroke="#868e96" stroke-width="1" stroke-dasharray="3 3"/>'
    + '<line x1="30" y1="200" x2="120" y2="200" stroke="#1971c2" stroke-width="3" marker-end="url(#ahc)"/>'
    + _t(30, 190, "Flow in", 12, fill="#1864ab")
    + _t(200, 285, "Disc hangs from a pin and swings", 12, "400", "#555", anchor="middle")
    + _t(200, 302, "open with forward flow", 12, "400", "#555", anchor="middle")
    + _t(200, 320, "Main weakness: slam", 12, "700", "#c92a2a", anchor="middle")
    # ---- right panel: dual plate wafer check, open, top view section
    + _t(600, 30, "Dual plate check (open)", 14, anchor="middle")
    + '<rect x="420" y="140" width="40" height="120" fill="#dee2e6" stroke="#495057" stroke-width="2"/>'
    + '<rect x="740" y="140" width="40" height="120" fill="#dee2e6" stroke="#495057" stroke-width="2"/>'
    + _t(440, 130, "Flange", 11, "400", "#555", anchor="middle")
    + _t(760, 130, "Flange", 11, "400", "#555", anchor="middle")
    + '<line x1="460" y1="150" x2="740" y2="150" stroke="#495057" stroke-width="3"/>'
    + '<line x1="460" y1="250" x2="740" y2="250" stroke="#495057" stroke-width="3"/>'
    # wafer body with seat
    + '<rect x="560" y="150" width="20" height="25" fill="#ffe8cc" stroke="#495057" stroke-width="2"/>'
    + '<rect x="560" y="225" width="20" height="25" fill="#ffe8cc" stroke="#495057" stroke-width="2"/>'
    + '<line x1="570" y1="175" x2="570" y2="225" stroke="#495057" stroke-width="3"/>'
    # central hinge pin
    + '<circle cx="585" cy="200" r="6" fill="#343a40"/>'
    # two half plates folded downstream
    + '<line x1="588" y1="196" x2="660" y2="164" stroke="' + _C + '" stroke-width="7" stroke-linecap="round"/>'
    + '<line x1="588" y1="204" x2="660" y2="236" stroke="' + _C + '" stroke-width="7" stroke-linecap="round"/>'
    + '<path d="M600 186 q8 14 0 28" fill="none" stroke="#2b8a3e" stroke-width="2"/>'
    + '<line x1="470" y1="175" x2="550" y2="175" stroke="#1971c2" stroke-width="3" marker-end="url(#ahc)"/>'
    + '<line x1="470" y1="225" x2="550" y2="225" stroke="#1971c2" stroke-width="3" marker-end="url(#ahc)"/>'
    + '<line x1="670" y1="200" x2="732" y2="200" stroke="#1971c2" stroke-width="3" marker-end="url(#ahc)"/>'
    + _t(600, 285, "Two spring loaded half plates on", 12, "400", "#555", anchor="middle")
    + _t(600, 302, "a central pin; springs close them", 12, "400", "#555", anchor="middle")
    + _t(600, 320, "before reverse flow builds up", 12, "700", "#2b8a3e", anchor="middle")
    + _t(625, 108, "Spring", 12, "400", "#2b8a3e", anchor="middle")
    + '<line x1="618" y1="112" x2="603" y2="184" stroke="#2b8a3e" stroke-width="1" stroke-dasharray="3 3"/>'
)

BODY = [
    takeaways([
        "A check valve lets fluid flow one way; forward flow opens it and reverse flow returns the disc to its seat.",
        "Cracking pressure is the minimum upstream pressure at which the valve opens, and it varies with design and size.",
        "Swing checks have low pressure drop but can slam; dual plate and tilting disc checks close faster and cause less water hammer.",
        "Orientation and sizing also matter: an oversized check flutters and wears.",
    ]),
    p("Every pump discharge and many process lines need protection against reverse flow. A <strong>check valve</strong> gives that protection with no actuator. SWME supplies " + link("/check-valves", "check valves") + " alongside our wider range of " + link("/industrial-valves", "industrial valves") + " for oil, gas, water and process plants in the UAE."),
    toc([("works", "How it works"), ("types", "Check valve types"), ("slam", "Slam and water hammer"),
         ("standards", "Standards"), ("select", "Selection checklist"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("works", "How a Check Valve Works"),
    p("According to " + ext("https://blog.projectmaterials.com/valves/bs-api-check-valves", "Projectmaterials") + ", forward flow pushes the closing element off its seat and reverse flow pushes it back. Check valves do not regulate flow. " + ext("https://www.pumpsandsystems.com/preventing-backflow-selecting-right-check-valve", "Pumps and Systems") + " defines cracking pressure as the minimum upstream pressure at which the valve opens, and stresses that the valve must be fully closed before line flow reaches zero."),
    INFOGRAPHIC,
    h2("types", "Check Valve Types"),
    table(["Type", "How it closes", "Notes from the sources"],
          [["Swing", "Hinged disc swings onto the seat", "Low pressure drop; install horizontal or slightly sloping; main weakness is slam"],
           ["Lift (piston)", "Piston or disc lifts vertically off the seat", "Higher pressure drop; suits pulsating flow such as reciprocating compressor discharge"],
           ["Ball", "Free ball rolls onto the seat", "Suits viscous fluids; a free floating ball needs vertical flow up"],
           ["Dual plate (wafer)", "Two spring loaded half plates on a central pin", "Compact for tight spaces; works horizontal and vertical"],
           ["Tilting disc", "Disc pivots off centre with short travel", "Opens at low flow; suits low and pulsating flow and pump discharge"],
           ["Silent and nozzle", "Spring driven axial disc with minimum travel", "Fastest closure; silent checks have higher pressure drop, nozzle checks lower head loss but not for suspended solids"]]),
    p("A stop check is a swing type body with a stem and handwheel that can force the disc shut, giving positive isolation in one body. The pressure drop ranking in the " + ext("https://blog.projectmaterials.com/quick-answers/valves/what-is-check-valve/", "Projectmaterials overview") + " is low for swing and tilting disc, medium for dual plate and ball, and medium to high for lift checks. For how check valves fit among other valve families, see " + link("/types-of-industrial-valves", "types of industrial valves") + "."),
    svg(_diag, "Swing check valve closed on an inclined seat, and dual plate wafer check valve open with two half plates folded downstream", 340),
    h2("slam", "Slam and Water Hammer"),
    p("Pumps and Systems says swing checks are highly susceptible to water hammer when the disc slams shut. Projectmaterials says dual plate and tilting disc check valves close faster and generate less water hammer, because the springs snap the plates shut before the fluid column builds momentum."),
    rows([
        ("Damping", "Larger swing checks can be fitted with dampers or counterweights."),
        ("Lighter discs", "Dual plate designs use light plates that close quickly."),
        ("Right size", "Avoid oversizing; an oversized valve may not open fully, causing flutter and premature wear."),
        ("Placement", "Install the check as close as possible to the pump discharge."),
    ], "Ways to reduce slam"),
    p("The " + ext("https://zentacalculator.com/engineering/water-hammer/", "water hammer calculator") + " estimates the surge when flow stops suddenly, and the " + ext("https://zentacalculator.com/engineering/pipe-flow-velocity/", "pipe flow velocity calculator") + " checks line velocity."),
    dyk("MSS SP 92 asks for a check valve to sit at least five pipe diameters downstream of an elbow and ten diameters downstream of a tee or control valve."),
    h2("standards", "Check Valve Standards"),
    rows([
        ("API 594", "Dedicated check valve standard: Type A single plate and Type B double plate."),
        ("BS 1868", "Steel check valves, flanged and butt welding ends, DN 50 to DN 600."),
        ("API 602 and BS 5352", "Forged small bore check valves."),
        ("API 6D", "Pipeline check valves."),
        ("ASME B16.34", "Pressure and temperature ratings, Class 150 to 2500."),
        ("AWWA C508", "Check valves for water service."),
        ("API 598 and ISO 5208", "Testing."),
    ]),
    h2("select", "Selection Checklist"),
    checklist([
        ("Line size and orientation", "Pumps and Systems prefers horizontal installation where possible; avoid swing checks in vertical upflow."),
        ("Speed of flow reversal", "Where flow reverses quickly, the faster closing dual plate, tilting disc or silent checks suit better."),
        ("Fluid", "For dirty or abrasive service, consider a swing check with an external lever and spring, or a duckbill."),
        ("Pressure and temperature", "Pick the class from ASME B16.34; Projectmaterials notes pressure seal bonnets above about Class 900."),
        ("Sizing", "Size from the manufacturer flow curve or Cv, not the line size. Try the " + ext("https://zentacalculator.com/engineering/control-valve-kv-cv/", "Kv and Cv calculator") + "."),
        ("End connection", "Wafer, flanged or butt welding ends to suit the line."),
    ]),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Oversizing the valve.", "The disc floats partly open, chatters and wears."),
        ("Mounting a swing check in vertical upflow.", "Projectmaterials advises against it; choose a type rated for vertical lines."),
        ("Placing the check right after an elbow.", "Keep the MSS SP 92 spacing of five diameters from elbows and ten from tees and control valves."),
    ]),
    p("For valve choice in general, read our post on " + link("/blog/how-to-select-the-right-industrial-valve", "how to select the right industrial valve") + " and the guide to " + link("/gate-valve-vs-globe-valve", "gate valve vs globe valve") + ". For pump protection, see " + link("/blog/pump-protection-pressure-flow-temperature-instruments", "pump protection instruments") + "."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What is cracking pressure?", "The minimum upstream pressure at which a check valve opens. It depends on the valve design and size."),
        ("Which check valve causes the least water hammer?", "Dual plate, tilting disc and silent checks close faster than swing checks and generate less water hammer."),
        ("Can a check valve be installed vertically?", "Some can. Dual plate checks work in vertical lines, a ball check needs flow up, and swing checks should stay horizontal."),
    ]),
]
