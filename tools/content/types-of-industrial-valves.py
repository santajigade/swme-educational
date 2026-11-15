META = {
    "category": "industrial-valve-guides",
    "title": "Types of Industrial Valves Explained",
    "keyword": "types of industrial valves",
    "subtitle": "Gate, globe, ball, butterfly, check, safety relief and control valves",
    "meta_title": "Types of Industrial Valves Explained: Functions and Uses",
    "meta_description": "Learn the main types of industrial valves: gate, globe, ball, butterfly, check, safety relief and control valves, how they work and where to use them.",
    "summary": "How gate, globe, ball, butterfly, check, relief and control valves work and where each fits.",
    "card_title": "Types of Industrial Valves",
    "author": "SWME Technical Staff",
    "published": "2026-11-15",
    "status": "draft",
    "sort_order": 1,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "grid",
        "title": "Four Jobs a Valve Can Do",
        "alt": "Infographic showing the four main functions of the types of industrial valves",
        "steps": [
            ["Isolation", "Start or stop flow completely: gate, ball and butterfly valves."],
            ["Regulation", "Throttle and control flow: globe and control valves."],
            ["Non return", "Stop reverse flow automatically: check valves."],
            ["Protection", "Relieve excess pressure: safety and relief valves."],
        ],
    },
}

BODY = [
    takeaways([
        "Valves are grouped by what they do: isolate, regulate, prevent backflow or protect against overpressure.",
        "Gate, ball and butterfly valves are mainly used for on and off isolation.",
        "Globe and control valves are designed for throttling and accurate flow control.",
        "Check and safety relief valves work automatically, without an operator.",
    ]),
    p("Every process plant relies on valves to start, stop and control flow. With so many designs on the market, it helps to understand the main <strong>types of industrial valves</strong> and the job each one is built to do. Choosing a valve for the wrong duty is a common cause of leaks, wear and poor control.",
      "This guide explains each valve type in plain terms. SWME supplies " + link("/industrial-valves", "industrial valves") + " for upstream, midstream and downstream Oil and Gas, Petrochemical, Water and Utilities projects across the GCC."),
    toc([("functions", "Valve functions"), ("types", "Main types of industrial valves"), ("compare", "Comparison table"),
         ("symbols", "Valve symbols on P&amp;ID drawings"), ("standards", "Standards and ratings"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("functions", "Valve Functions"),
    p("Before looking at individual designs, decide what the valve must do. Most valves fall into four functional groups."),
    INFOGRAPHIC,
    h2("types", "Main Types of Industrial Valves"),
    h3("Gate valves"),
    p("A flat or wedge shaped gate moves up and down across the flow. When fully open, the bore is clear, so pressure loss is very low. " + link("/gate-valves", "Gate valves") + " are ideal for isolation in large lines, but they should not be used half open, because the gate vibrates and the seats erode. For wellhead and pipeline duty, see " + link("/api-6a-gate-valves", "API 6A gate valves") + " and " + link("/api-6d-gate-valves", "API 6D gate valves") + "."),
    h3("Globe valves"),
    p("A disc moves onto a seat inside a spherical body, and the flow changes direction through the valve. This shape gives good throttling control and tight shut off, at the cost of higher pressure loss. " + link("/globe-valves", "Globe valves") + " are common on steam, cooling water and bypass lines."),
    h3("Ball valves"),
    p("A ball with a bore rotates a quarter turn to open or close. " + link("/ball-valves", "Ball valves") + " operate quickly, seal tightly and suit most gases and liquids. For corrosive chemicals, " + link("/lined-ball-valves", "PTFE and PFA lined ball valves") + " protect the body from attack."),
    h3("Butterfly valves"),
    p("A disc rotates a quarter turn inside the pipe. " + link("/butterfly-valves", "Butterfly valves") + " are light, compact and economical in large diameters, so they are popular in water treatment, cooling and HVAC systems. High performance and triple offset designs extend their use to higher pressures and temperatures."),
    h3("Check valves"),
    p("A disc, ball or flap opens with forward flow and closes when flow reverses. " + link("/check-valves", "Check valves") + " protect pumps and compressors from backflow and need no operator. Swing, lift, dual plate and piston designs suit different flow rates and orientations."),
    h3("Safety relief valves"),
    p("A spring holds the valve closed until system pressure reaches the set point. The valve then opens to release fluid and protect equipment and people. " + link("/safety-relief-valves", "Safety relief valves") + " are the last line of defence against overpressure, so they must be sized, set and tested correctly."),
    h3("Control valves"),
    p("A control valve receives a signal from the control system and positions its trim to hold a set flow, pressure, level or temperature. " + link("/pneumatic-control-valves", "Pneumatic control valves") + " and " + link("/pressure-reducing-valves", "pressure reducing valves") + " are typical examples. Sizing uses the flow coefficient; try the " + ext("https://zentacalculator.com/engineering/control-valve-kv-cv/", "control valve Kv and Cv calculator") + " and the " + ext("https://zentacalculator.com/engineering/valve-authority/", "valve authority calculator") + "."),
    dyk("A gate valve used for throttling can wear out in weeks. At small openings, high velocity flow hits the bottom of the gate and the seat, cutting grooves called wire drawing. Once damaged, the valve can no longer seal. Use a globe or control valve wherever flow must be regulated."),
    h2("compare", "Comparing the Types of Industrial Valves"),
    table(["Valve type", "Main function", "Operation", "Pressure loss", "Typical use"], [
        ["Gate", "Isolation", "Multi turn", "Very low", "Pipelines, large lines"],
        ["Globe", "Throttling", "Multi turn", "High", "Steam, bypass, cooling"],
        ["Ball", "Isolation", "Quarter turn", "Very low", "Gas, liquids, chemicals"],
        ["Butterfly", "Isolation, coarse control", "Quarter turn", "Low", "Water, HVAC, large diameters"],
        ["Check", "Non return", "Automatic", "Low to medium", "Pump and compressor discharge"],
        ["Safety relief", "Overpressure protection", "Automatic", "Not applicable", "Vessels, boilers, pipelines"],
        ["Control", "Regulation", "Actuated", "Medium", "Flow, pressure, level loops"],
    ]),
    h2("symbols", "Valve Symbols on P&amp;ID Drawings"),
    svg(
        "".join(
            f'<g transform="translate({x},40)">'
            f'<line x1="0" y1="60" x2="30" y2="60" stroke="#495057" stroke-width="3"/>'
            f'<line x1="90" y1="60" x2="120" y2="60" stroke="#495057" stroke-width="3"/>'
            f'<path d="M30 35 L90 85 L90 35 L30 85 Z" fill="{fill}" stroke="{T["c"]}" stroke-width="3"/>'
            + extra +
            f'<text x="60" y="130" text-anchor="middle" font-size="15" font-weight="600" fill="{T["tx"]}">{name}</text></g>'
            for x, name, fill, extra in (
                (20, "Gate", "#fff", ""),
                (175, "Globe", "#fff", f'<circle cx="60" cy="60" r="8" fill="{T["c"]}"/>'),
                (330, "Ball", "#fff", f'<circle cx="60" cy="60" r="13" fill="#fff" stroke="{T["c"]}" stroke-width="3"/>'),
                (485, "Butterfly", "#fff", f'<line x1="60" y1="35" x2="60" y2="85" stroke="{T["c"]}" stroke-width="3"/><circle cx="60" cy="60" r="5" fill="{T["c"]}"/>'),
                (640, "Check", "#fff", f'<line x1="30" y1="100" x2="90" y2="100" stroke="#e67700" stroke-width="3" marker-end="url(#ah)"/>'),
            )
        ) + arrow_defs("#e67700"),
        "Common P&ID symbols for the main types of industrial valves", 200),
    p("Reading these symbols correctly helps you check that the right valve type has been chosen for each duty during design reviews. In addition, valve tags on the drawing link to datasheets that state body material, pressure class and end connections. For background on control loops that use control valves, see this overview of " + ext("https://zentaengineering.com/automation-robotics/scada-system-architecture/", "SCADA system architecture") + "."),
    h2("standards", "Standards and Pressure Ratings"),
    rows([
        ("API 600 and API 6D", "steel gate valves for refinery service and pipeline valves."),
        ("API 6A", "wellhead and Christmas tree equipment, rated in psi up to 20,000 psi and above."),
        ("ASME B16.34", "pressure and temperature ratings for flanged, threaded and welded end valves."),
        ("ASME classes", "150, 300, 600, 900, 1500 and 2500, matching the flange rating of the line."),
        ("API 526 and API 520", "dimensions and sizing for pressure relief valves."),
    ]),
    p("Valves also need clean fluid to seal well. Installing " + link("/strainers", "strainers") + " upstream protects seats from scale and weld debris. To understand pressure drop across valves and fittings, use the " + ext("https://zentacalculator.com/engineering/minor-losses/", "minor losses calculator") + ". For a step by step selection process, read our blog on " + link("/blog/how-to-select-the-right-industrial-valve", "how to select the right industrial valve") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Throttling with gate or ball valves.", "Seats erode and the valve stops sealing."),
        ("Wrong check valve orientation.", "Some designs only work in horizontal or upward flow."),
        ("Ignoring pressure class.", "A class 150 valve on a class 300 line is a serious safety risk."),
        ("Oversized control valves.", "The valve works near closed and control becomes unstable."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What is the most common type of industrial valve?", "Ball and gate valves are the most common, because most valves in a plant are used for simple on and off isolation."),
        ("What is the difference between a gate valve and a globe valve?", "A gate valve is designed for full open or full closed isolation with low pressure loss, while a globe valve is designed for throttling and flow control."),
        ("Which valve prevents backflow?", "A check valve, also called a non return valve, closes automatically when flow tries to reverse."),
    ]),
]
