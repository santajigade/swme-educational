META = {
    "category": "industrial-valve-guides",
    "title": "Gate Valve vs Globe Valve: Key Differences and When to Use Each",
    "keyword": "gate valve vs globe valve",
    "subtitle": "Design, flow path, pressure drop, throttling, standards and typical services",
    "meta_title": "Gate Valve vs Globe Valve: Key Differences Explained",
    "meta_description": "Gate valve vs globe valve: compare design, flow path, pressure drop, throttling, sealing, standards and typical services to choose the right valve.",
    "summary": "How gate and globe valves differ in design, pressure drop, throttling and sealing, and where each one fits.",
    "card_title": "Gate Valve vs Globe Valve",
    "author": "SWME Technical Staff",
    "published": "2026-11-16",
    "status": "published",
    "sort_order": 2,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "compare",
        "title": "Gate Valve vs Globe Valve",
        "alt": "Infographic comparing gate valve vs globe valve function, flow path, pressure drop and typical use",
        "columns": [
            ["Gate valve", ["Fully open or fully closed", "Straight through bore", "Very low pressure drop", "Flow in both directions", "Mainline isolation"]],
            ["Globe valve", ["Throttles at any position", "S shaped flow path", "Higher pressure drop", "One flow direction, arrow on body", "Bypass, cooling water, dosing"]],
        ],
    },
}

BODY = [
    takeaways([
        "A gate valve is an isolation valve: it should be either fully open or fully closed.",
        "A globe valve is built for throttling and can hold any position between open and closed.",
        "Gate valves have a straight bore and very low pressure drop; globe valves turn the flow and lose more pressure.",
        "Gate valves are usually bidirectional, while most globe valves have a flow arrow on the body.",
    ]),
    p("Gate and globe valves look similar from the outside. Both have a handwheel, a rising stem and a linear closing element. Inside, however, they are built for very different jobs, and the <strong>gate valve vs globe valve</strong> choice decides whether a line isolates cleanly or controls flow smoothly.",
      "This guide compares the two designs in plain terms. SWME supplies " + link("/gate-valves", "gate valves") + " and " + link("/globe-valves", "globe valves") + " for Oil and Gas, Petrochemical, Water and Utilities projects across the GCC. For an overview of all designs, see our guide to " + link("/types-of-industrial-valves", "types of industrial valves") + "."),
    toc([("design", "How each valve works"), ("compare", "Gate valve vs globe valve comparison"), ("throttling", "Throttling and pressure drop"),
         ("standards", "Standards and sizes"), ("select", "How to choose"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("design", "How Each Valve Works"),
    h3("Gate valve"),
    p("A flat or wedge shaped gate moves up and down at right angles to the flow. When the gate is lifted, the bore is clear and the fluid passes straight through. When it is lowered, the gate seals against two seats. Because the flow path does not change direction, pressure loss in the fully open position is very low."),
    h3("Globe valve"),
    p("A disc moves onto a seat that sits across the flow. An internal wall forces the fluid to turn and pass through the seat opening, so the path is S shaped. The gap between disc and seat sets the flow rate, which is why a globe valve can throttle. In addition, the closing force acts directly on the disc, which gives very good shut off."),
    svg(
        arrow_defs("#e67700")
        # gate valve
        + '<text x="200" y="28" text-anchor="middle" font-size="16" font-weight="700" fill="#a35400">Gate valve (open)</text>'
        + '<rect x="30" y="170" width="340" height="60" fill="#f1f3f5" stroke="#495057" stroke-width="3"/>'
        + '<rect x="150" y="120" width="100" height="150" rx="14" fill="#fff" stroke="#495057" stroke-width="3"/>'
        + '<rect x="150" y="170" width="100" height="60" fill="#f1f3f5"/>'
        + '<line x1="150" y1="170" x2="150" y2="230" stroke="#f1f3f5" stroke-width="4"/><line x1="250" y1="170" x2="250" y2="230" stroke="#f1f3f5" stroke-width="4"/>'
        + '<rect x="170" y="70" width="60" height="50" rx="6" fill="#fff" stroke="#495057" stroke-width="3"/>'
        + '<path d="M186 78 L214 78 L210 160 L190 160 Z" fill="#e67700" opacity="0.85"/>'
        + '<line x1="200" y1="78" x2="200" y2="40" stroke="#495057" stroke-width="4"/>'
        + '<ellipse cx="200" cy="40" rx="34" ry="7" fill="#fff" stroke="#495057" stroke-width="3"/>'
        + '<line x1="60" y1="200" x2="340" y2="200" stroke="#1971c2" stroke-width="4" marker-end="url(#ah)"/>'
        + '<text x="262" y="110" font-size="13" fill="#333">Wedge lifted</text>'
        + '<text x="200" y="300" text-anchor="middle" font-size="14" fill="#333">Straight through bore</text>'
        + '<text x="200" y="322" text-anchor="middle" font-size="14" fill="#333">Very low pressure drop</text>'
        # globe valve
        + '<text x="600" y="28" text-anchor="middle" font-size="16" font-weight="700" fill="#a35400">Globe valve (throttling)</text>'
        + '<rect x="420" y="170" width="80" height="60" fill="#f1f3f5" stroke="#495057" stroke-width="3"/>'
        + '<rect x="700" y="170" width="80" height="60" fill="#f1f3f5" stroke="#495057" stroke-width="3"/>'
        + '<ellipse cx="600" cy="200" rx="105" ry="80" fill="#f1f3f5" stroke="#495057" stroke-width="3"/>'
        + '<rect x="490" y="172" width="24" height="56" fill="#f1f3f5"/><rect x="686" y="172" width="24" height="56" fill="#f1f3f5"/>'
        + '<polyline points="560,124 560,200 582,200" fill="none" stroke="#495057" stroke-width="5"/>'
        + '<polyline points="618,200 640,200 640,276" fill="none" stroke="#495057" stroke-width="5"/>'
        + '<rect x="578" y="160" width="44" height="14" rx="3" fill="#e67700"/>'
        + '<line x1="600" y1="160" x2="600" y2="60" stroke="#495057" stroke-width="4"/>'
        + '<rect x="582" y="104" width="36" height="16" fill="#fff" stroke="#495057" stroke-width="3"/>'
        + '<ellipse cx="600" cy="60" rx="34" ry="7" fill="#fff" stroke="#495057" stroke-width="3"/>'
        + '<polyline points="440,215 540,215 540,248 600,248 600,187 760,187" fill="none" stroke="#1971c2" stroke-width="4" marker-end="url(#ah)"/>'
        + '<text x="652" y="220" font-size="13" fill="#333">Seat</text><line x1="650" y1="215" x2="624" y2="203" stroke="#868e96" stroke-width="1.5"/>'
        + '<text x="632" y="172" font-size="13" fill="#333">Disc</text>'
        + '<text x="600" y="300" text-anchor="middle" font-size="14" fill="#333">S shaped path through the seat</text>'
        + '<text x="600" y="322" text-anchor="middle" font-size="14" fill="#333">Higher pressure drop, fine control</text>'
        + '<text x="430" y="160" font-size="13" fill="#1971c2">Flow</text><text x="730" y="160" font-size="13" fill="#1971c2">Flow</text>',
        "Simplified cross sections: gate valve vs globe valve flow paths", 340),
    INFOGRAPHIC,
    h2("compare", "Gate Valve vs Globe Valve Comparison"),
    table(["Feature", "Gate valve", "Globe valve"], [
        ["Main function", "On and off isolation", "Throttling and flow regulation"],
        ["Flow path", "Straight through", "Turns through the seat (S shaped)"],
        ["Pressure drop when open", "Very low", "High"],
        ["Throttling", "Poor, causes seat erosion", "Excellent"],
        ["Flow direction", "Bidirectional", "Unidirectional, arrow on body"],
        ["Shut off", "Good, metal wedge on seats", "Very good, disc on seat"],
        ["Weight and cost", "Lighter and lower cost", "Heavier and higher cost"],
        ["Typical services", "Mainline and equipment isolation", "Cooling water, steam bypass, chemical dosing"],
    ]),
    p("Both designs can be operated by handwheel, gearbox, pneumatic or electric actuator. When a line needs automatic control rather than manual throttling, a " + link("/pneumatic-control-valves", "pneumatic control valve") + " is usually the better choice."),
    h2("throttling", "Throttling and Pressure Drop"),
    p("Pressure drop is the price of control. The straight bore of a gate valve wastes very little energy, which matters on long pipelines and large pump discharge lines. A globe valve turns the flow and loses more pressure, but that same restriction is what makes accurate throttling possible.",
      "Globe valves come in three body patterns. In the T pattern, also called the Z body, the flow follows the S shaped path shown above. The Y pattern has the lowest pressure drop of the globe types but is the least efficient at throttling. The angle pattern turns the flow through 90 degrees. To estimate the energy lost across valves and fittings, use the " + ext("https://zentacalculator.com/engineering/minor-losses/", "minor losses calculator") + " or the " + ext("https://zentacalculator.com/engineering/darcy-weisbach-head-loss/", "Darcy Weisbach head loss calculator") + "."),
    dyk("A gate valve left a few turns open is one of the fastest ways to destroy it. High velocity flow under the gate cuts grooves in the seats and wedge, a type of damage called wire drawing. Once the seats are cut, the valve no longer isolates, even when it is fully closed."),
    h2("standards", "Standards and Typical Sizes"),
    rows([
        ("API 600", "cast steel gate valves for refinery and process service."),
        ("API 623 and BS 1873", "cast steel globe valves."),
        ("API 602 and BS 5352", "forged steel gate and globe valves in small sizes."),
        ("API 6D", "pipeline valves; see our " + link("/api-6d-gate-valves", "API 6D gate valves") + "."),
        ("Typical sizes", "gate valves from about 2 inches to 60 inches and above; globe valves from half an inch to about 24 inches."),
    ]),
    p("Pressure class must always match the piping class of the line. For a wider look at the selection process, read our blog on " + link("/blog/how-to-select-the-right-industrial-valve", "how to select the right industrial valve") + "."),
    h2("select", "How to Choose Between Them"),
    twocol([
        ("Choose a gate valve when", "bi-door-open", [
            "The valve will stay fully open or fully closed.",
            "Low pressure loss matters, for example on mainlines.",
            "Flow may run in both directions.",
            "The line size is large and weight and cost matter.",
        ]),
        ("Choose a globe valve when", "bi-sliders", [
            "Flow must be adjusted or throttled by hand.",
            "Tight shut off with frequent operation is needed.",
            "The service is steam, cooling water, bypass or dosing.",
            "A higher pressure drop is acceptable.",
        ]),
    ]),
    p("Clean fluid protects both valve types. Fit " + link("/strainers", "strainers") + " upstream to keep weld debris and scale off the seats. When a control valve replaces a manual globe valve, size it with the " + ext("https://zentacalculator.com/engineering/control-valve-kv-cv/", "Kv and Cv calculator") + " and check the " + ext("https://zentacalculator.com/engineering/valve-authority/", "valve authority") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Throttling with a gate valve.", "The seats erode and the valve stops sealing."),
        ("Installing a globe valve against the arrow.", "The body is designed for one flow direction, so always follow the arrow."),
        ("Using a globe valve on a long mainline.", "The permanent pressure loss raises pumping energy for the life of the plant."),
        ("Ignoring vertical space.", "A rising stem gate valve is tall when open and needs clearance above it."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Can a gate valve be used for throttling?", "No. A gate valve should be fully open or fully closed. Partial opening causes vibration and wire drawing of the seats."),
        ("Is a globe valve bidirectional?", "Most globe valves are designed for one flow direction, which is marked with an arrow on the body."),
        ("Which valve has the lower pressure drop?", "The gate valve. Its straight bore gives almost no restriction when fully open, while a globe valve turns the flow through the seat."),
    ]),
]
