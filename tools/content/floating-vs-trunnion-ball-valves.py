META = {
    "category": "industrial-valve-guides",
    "title": "Floating vs Trunnion Mounted Ball Valves: Key Differences",
    "keyword": "floating vs trunnion ball valve",
    "subtitle": "How each design holds the ball, seals, and where each one makes sense",
    "meta_title": "Floating vs Trunnion Ball Valve: Key Differences",
    "meta_description": "Floating vs trunnion ball valve explained: ball support, seat sealing, size and pressure class, torque, double block and bleed, cost and typical applications.",
    "summary": "How floating and trunnion mounted ball valves differ in ball support, sealing, torque, size, cost and typical service.",
    "card_title": "Floating vs Trunnion Ball Valves",
    "author": "SWME Technical Staff",
    "published": "2026-11-17",
    "status": "published",
    "sort_order": 3,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "flow",
        "title": "Choosing a Ball Valve Design",
        "alt": "Infographic showing four steps to choose between a floating and a trunnion mounted ball valve",
        "steps": [
            ["Size and class", "Small bore and low to medium class point to floating."],
            ["Isolation", "Double block and bleed needs a trunnion design."],
            ["Torque", "High pressure raises floating torque; trunnion stays steadier."],
            ["Cost", "Floating costs less; trunnion pays back in severe service."],
        ],
    },
}

_C = "#e67700"
_T = "#a35400"


def _body(x0):
    return (f'<rect x="{x0 + 20}" y="150" width="60" height="70" fill="#f1f3f5" stroke="#495057" stroke-width="2"/>'
            f'<rect x="{x0 + 300}" y="150" width="60" height="70" fill="#f1f3f5" stroke="#495057" stroke-width="2"/>'
            f'<rect x="{x0 + 80}" y="90" width="220" height="190" rx="20" fill="#f8f9fa" stroke="#495057" stroke-width="3"/>'
            f'<circle cx="{x0 + 190}" cy="185" r="62" fill="#ffe8cc" stroke="{_C}" stroke-width="3"/>'
            f'<rect x="{x0 + 132}" y="168" width="116" height="34" fill="#fff"/>'
            f'<rect x="{x0 + 180}" y="40" width="20" height="85" fill="#868e96"/>'
            f'<text x="{x0 + 210}" y="58" font-size="13" fill="#555">Stem</text>')


_diag = (
    arrow_defs(_C)
    # floating
    + _body(0)
    + '<rect x="114" y="150" width="12" height="70" fill="#adb5bd"/>'
    + '<rect x="254" y="150" width="12" height="70" fill="' + _T + '"/>'
    + '<line x1="20" y1="185" x2="105" y2="185" stroke="#e8590c" stroke-width="4" marker-end="url(#ah)"/>'
    + '<text x="20" y="140" font-size="13" font-weight="700" fill="#e8590c">Line pressure</text>'
    + '<text x="190" y="310" text-anchor="middle" font-size="13" fill="#333">Ball pushed onto the downstream seat</text>'
    + '<text x="190" y="22" text-anchor="middle" font-size="16" font-weight="700" fill="' + _T + '">Floating ball</text>'
    # trunnion
    + _body(410)
    + '<rect x="590" y="245" width="20" height="45" fill="#868e96"/>'
    + '<text x="620" y="300" font-size="13" fill="#555">Trunnion</text>'
    + '<rect x="530" y="150" width="12" height="70" fill="' + _T + '"/>'
    + '<rect x="658" y="150" width="12" height="70" fill="' + _T + '"/>'
    + '<polyline points="500,160 510,166 500,172 510,178 500,184 510,190 500,196 510,202 500,208 510,214 520,214" fill="none" stroke="#495057" stroke-width="2"/>'
    + '<polyline points="700,160 690,166 700,172 690,178 700,184 690,190 700,196 690,202 700,208 690,214 680,214" fill="none" stroke="#495057" stroke-width="2"/>'
    + '<text x="600" y="330" text-anchor="middle" font-size="13" fill="#333">Fixed ball; spring loaded seats seal on both sides</text>'
    + '<text x="600" y="22" text-anchor="middle" font-size="16" font-weight="700" fill="' + _T + '">Trunnion mounted ball</text>'
    + '<text x="400" y="350" text-anchor="middle" font-size="12" fill="#666">Seats shown in orange; sealing seat darker</text>'
)

BODY = [
    takeaways([
        "In a floating ball valve, line pressure pushes the ball onto the downstream seat to seal.",
        "In a trunnion mounted ball valve, the ball is fixed by upper and lower bearings and spring loaded seats move onto it.",
        "Floating designs suit smaller sizes and lower classes; trunnion designs cover large sizes and high pressure.",
        "Trunnion valves allow double block and bleed and keep torque steadier, but cost more.",
    ]),
    p("Ball valves rotate a quarter turn, 90°, to open or close, and they are the default isolation valve in many plants. Yet two very different designs sit behind the same name. Understanding <strong>floating vs trunnion ball valve</strong> construction helps you choose a valve that seals reliably, can be actuated economically and does not cost more than the duty needs.",
      "SWME supplies " + link("/ball-valves", "ball valves") + ", " + link("/lined-ball-valves", "lined ball valves") + " and a wide range of " + link("/industrial-valves", "industrial valves") + " for oil and gas, water and utility projects."),
    toc([("design", "How each design works"), ("compare", "Floating vs trunnion ball valve comparison"), ("torque", "Torque and actuation"),
         ("dbb", "Double block and bleed"), ("select", "How to choose"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("design", "How Each Design Works"),
    svg(_diag, "Floating ball valve compared with a trunnion mounted ball valve", 360),
    h3("Floating ball valve"),
    p("The ball has no bearings and is held only by the two seats and the stem. When the valve is closed, upstream pressure pushes the ball slightly downstream and presses it against the downstream seat, which makes the seal. As " + ext("https://www.fitok.com/en/blog/detail-17-049c4adbdc9d0b72.html", "FITOK") + " notes, the simple structure keeps manufacturing cost lower and maintenance easier."),
    h3("Trunnion mounted ball valve"),
    p("The ball is anchored by an upper stem and a lower trunnion running in bearings, so it rotates without moving sideways. Instead of the ball moving onto a seat, spring loaded seats press inward against the fixed ball. According to " + ext("https://blog.projectmaterials.com/quick-answers/valves/floating-vs-trunnion-ball-valve/", "Project Materials") + ", this makes the sealing force largely independent of line pressure."),
    h2("compare", "Floating vs Trunnion Ball Valve Comparison"),
    table(["Feature", "Floating ball", "Trunnion mounted ball"], [
        ["Ball support", "Free floating, no bearings", "Upper and lower trunnion bearings"],
        ["Sealing", "Downstream seat, by line pressure", "Spring loaded seats on both sides"],
        ["Typical size", "Practical limit about 8 to 10 in", "Up to 60 in and larger"],
        ["Pressure class", "Low to medium classes", "Class 150 to 2500"],
        ["Torque", "Rises with pressure", "Relatively constant"],
        ["Typical standards", "API 608, fire safe to API 607", "API 6D and API 608, fire safe to API 607"],
    ]),
    p("Values from Project Materials, which places the practical boundary between the two designs at about 8 in in Class 300."),
    INFOGRAPHIC,
    h2("torque", "Torque and Actuation"),
    p("In a floating ball valve, the higher the pressure, the harder the ball is pushed onto its seat, so the torque needed to turn it rises with pressure, especially in larger sizes. A trunnion valve takes the pressure load on its bearings, so torque stays relatively constant and a smaller actuator is needed at high pressure. This matters when sizing pneumatic or electric actuators for " + link("/automatic-control-valves", "automated valves") + "."),
    dyk("Weight tells the story of the two designs. Project Materials gives a 6 in Class 150 floating ball valve at about 40 kg and a trunnion mounted valve of the same size and class at about 100 kg, with a price two to four times higher."),
    h2("dbb", "Double Block and Bleed"),
    p("Because only the downstream seat is loaded, a floating ball valve cannot provide double block and bleed. In a trunnion valve both seats seal independently, so a bleed valve on the body cavity can confirm isolation. The trapped cavity must be protected from pressure build up with a self relieving upstream seat or an external relief valve."),
    twocol([
        ("Choose floating for", "bi-check-circle", [
            "Small bore process and utility piping",
            "Instrument root valves",
            "General isolation where cost drives the choice",
        ]),
        ("Choose trunnion for", "bi-shield-check", [
            "Pipeline isolation and high pressure gas",
            "Large sizes and high pressure classes",
            "Any service that needs double block and bleed",
        ]),
    ]),
    h2("select", "How to Choose"),
    checklist([
        ("Size and pressure class", "Check them first; large, high class valves point to trunnion."),
        ("Isolation duty", "If the procedure calls for double block and bleed, specify trunnion."),
        ("Actuator", "Compare torque at maximum pressure; trunnion often allows a smaller actuator."),
        ("Flow direction", "Many floating designs seal in one direction only; check bidirectional needs."),
        ("Lifecycle cost", "Trunnion costs more to buy, but FITOK notes a lower total cost of ownership in harsh service."),
    ]),
    p("For the bigger picture, read " + link("/types-of-industrial-valves", "types of industrial valves") + ", " + link("/gate-valve-vs-globe-valve", "gate valve vs globe valve") + " and our blog on " + link("/blog/how-to-select-the-right-industrial-valve", "how to select the right industrial valve") + ". For flow sizing, the " + ext("https://zentacalculator.com/engineering/control-valve-kv-cv/", "Kv and Cv calculator") + " helps, and the " + ext("https://zentacalculator.com/engineering/hydrostatic-test-pressure/", "hydrostatic test pressure calculator") + " supports pressure testing checks."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Large floating valve at high pressure.", "Torque climbs and seat loading becomes excessive; a trunnion design is the safer choice."),
        ("Expecting double block and bleed from a floating valve.", "Only the downstream seat seals, so true double isolation is not possible."),
        ("Ignoring cavity relief.", "A trunnion valve needs a self relieving seat or relief valve for the body cavity."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What is the main difference between floating and trunnion ball valves?", "A floating ball is pushed onto the downstream seat by line pressure, while a trunnion ball is fixed by bearings and the seats are spring loaded onto it."),
        ("Which is better for high pressure?", "Trunnion mounted ball valves, which cover classes up to 2500 and keep operating torque steadier."),
        ("Are floating ball valves cheaper?", "Yes. Project Materials puts a trunnion valve at two to four times the cost of a floating valve of the same size and class."),
    ]),
]
