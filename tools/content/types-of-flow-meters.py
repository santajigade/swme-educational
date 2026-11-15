META = {
    "category": "flow-measurement-guides",
    "title": "Types of Flow Meters Explained: Principles and Selection",
    "keyword": "types of flow meters",
    "subtitle": "How each flow meter works, where it fits best and how to choose",
    "meta_title": "Types of Flow Meters Explained: Principles and Uses",
    "meta_description": "Compare the main types of flow meters: differential pressure, electromagnetic, vortex, turbine, ultrasonic, Coriolis and variable area, with selection tips.",
    "summary": "Working principles, strengths and typical uses of the main flow meter technologies.",
    "card_title": "Types of Flow Meters",
    "author": "SWME Technical Staff",
    "published": "2026-11-15",
    "status": "published",
    "sort_order": 1,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "title": "Choosing a Flow Meter",
        "alt": "Infographic showing four questions to choose between the main types of flow meters",
        "steps": [
            ["What is the fluid?", "Liquid, gas, steam or slurry, and is it conductive or clean?"],
            ["Volume or mass?", "Volumetric meters measure flow rate; Coriolis measures mass directly."],
            ["Pipe and range", "Check line size, flow range, turndown and straight run available."],
            ["Accuracy and cost", "Balance accuracy, pressure loss, maintenance and installed cost."],
        ],
    },
}

BODY = [
    takeaways([
        "No single flow meter suits every application; the fluid decides the technology.",
        "Electromagnetic meters suit conductive liquids, vortex meters suit steam and gases, Coriolis meters give direct mass flow.",
        "Straight pipe runs, turndown and pressure loss matter as much as accuracy.",
        "Clamp on ultrasonic meters measure without cutting the pipe.",
    ]),
    p("Flow is one of the most measured variables in any process plant. It is also one of the most varied, because the right meter depends on the fluid, the pipe and the purpose of the measurement. Understanding the main <strong>types of flow meters</strong> helps you avoid costly mistakes at the design stage.",
      "This guide explains each technology in plain terms and compares their strengths. SWME supplies " + link("/flowmeters", "flowmeters") + ", " + link("/flow-transmitters", "flow transmitters") + " and " + link("/flow-switches", "flow switches") + " from leading principals."),
    toc([("basics", "Flow measurement basics"), ("types", "Main types of flow meters"), ("compare", "Comparison table"),
         ("select", "How to select"), ("install", "Installation tips"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("basics", "Flow Measurement Basics"),
    p("Flow can be expressed as volume per unit time, such as cubic metres per hour, or as mass per unit time, such as kilograms per hour. For liquids at constant temperature the two are closely related. For gases and steam, density changes with pressure and temperature, so mass flow or corrected volume flow is usually required.",
      "In addition, the way the fluid moves in the pipe matters. The " + ext("https://zentacalculator.com/engineering/reynolds-number/", "Reynolds number calculator") + " tells you whether flow is laminar or turbulent, which affects many meter types. You can also check line velocity with the " + ext("https://zentacalculator.com/engineering/pipe-flow-velocity/", "pipe flow velocity calculator") + "."),
    INFOGRAPHIC,
    h2("types", "Main Types of Flow Meters"),
    h3("Differential pressure"),
    svg(arrow_defs(T["c"]) +
        f'<rect x="40" y="140" width="720" height="90" fill="{T["bg"]}" stroke="{T["c"]}" stroke-width="2"/>'
        '<rect x="392" y="120" width="16" height="45" fill="#495057"/><rect x="392" y="205" width="16" height="45" fill="#495057"/>'
        + "".join(f'<line x1="{x}" y1="185" x2="{x+60}" y2="185" stroke="{T["c"]}" stroke-width="2.5" marker-end="url(#ah)"/>' for x in (80, 200, 520, 640))
        + '<line x1="300" y1="140" x2="300" y2="80" stroke="#333" stroke-width="3"/><line x1="500" y1="140" x2="500" y2="80" stroke="#333" stroke-width="3"/>'
        '<path d="M300 80 L300 50 L500 50 L500 80" fill="none" stroke="#333" stroke-width="3"/>'
        f'<rect x="355" y="30" width="90" height="40" rx="8" fill="{T["c"]}"/><text x="400" y="56" text-anchor="middle" font-size="14" fill="#fff" font-weight="600">DP cell</text>'
        '<text x="285" y="105" text-anchor="end" font-size="14" fill="#333" font-weight="600">H</text><text x="515" y="105" font-size="14" fill="#333" font-weight="600">L</text>'
        '<text x="400" y="275" text-anchor="middle" font-size="14" fill="#333">Orifice plate creates a pressure drop that rises with the square of flow</text>'
        f'<text x="60" y="130" font-size="13" fill="{T["tx"]}">Flow</text>',
        "Differential pressure flow measurement across an orifice plate", 300),
    p("A restriction such as an " + link("/orifice-plates", "orifice plate") + ", venturi or nozzle creates a pressure drop that rises with the square of flow. A differential pressure transmitter measures this drop. It is a proven, low cost method for clean liquids, gases and steam. You can explore the relationship with the " + ext("https://zentacalculator.com/engineering/orifice-flow/", "orifice plate flow calculator") + "."),
    h3("Electromagnetic"),
    p("A magnetic field across the pipe induces a voltage in a conductive liquid. The voltage is proportional to velocity. There are no moving parts and no pressure loss, which makes these meters ideal for water, wastewater and slurries. Read " + link("/electromagnetic-flow-meter-working-principle", "how an electromagnetic flow meter works") + " for more detail."),
    h3("Vortex"),
    p("A bluff body in the flow sheds vortices at a frequency proportional to velocity. Vortex meters suit steam, gases and clean liquids, and they handle high temperatures well."),
    h3("Turbine"),
    p("A rotor spins at a speed proportional to flow. Turbine meters offer good accuracy for clean, low viscosity fluids, such as fuel and light oils, but their bearings wear over time."),
    h3("Ultrasonic"),
    p("Transit time meters compare the travel time of sound pulses with and against the flow. Clamp on versions mount outside the pipe, so you can measure without shutting down. See the " + link("/blog/xft-clamp-on-ultrasonic-flow-meter-uae", "XFT clamp on ultrasonic flow meter") + " for an example."),
    h3("Coriolis"),
    p("Vibrating tubes twist slightly as mass flows through them. The twist is proportional to mass flow, and the vibration frequency gives density. Coriolis meters are very accurate but cost more, especially in large sizes."),
    h3("Variable area"),
    p("In a " + link("/rotameters", "rotameter") + " a float rises in a tapered tube until it balances the flow. It needs no power and gives a local reading, which makes it popular for purge, dosing and utility lines."),
    dyk("A differential pressure flow meter has a natural turndown of only about 4 to 1, because the signal falls with the square of flow. At 10% flow, the differential pressure is just 1% of its maximum. This is why low flow cutoffs are used. Try the " + ext("https://zentacalculator.com/engineering/low-flow-cutoff/", "low flow cutoff calculator") + " to see the effect."),
    h2("compare", "Comparing the Types of Flow Meters"),
    table(["Meter type", "Best for", "Pressure loss", "Typical accuracy", "Moving parts"], [
        ["Differential pressure", "Clean liquids, gas, steam", "Medium to high", "1 to 2%", "No"],
        ["Electromagnetic", "Conductive liquids, slurries", "None", "0.2 to 0.5%", "No"],
        ["Vortex", "Steam, gas, clean liquids", "Low", "0.75 to 1.5%", "No"],
        ["Turbine", "Clean, low viscosity liquids", "Medium", "0.25 to 0.5%", "Yes"],
        ["Ultrasonic", "Large pipes, clean liquids", "None", "0.5 to 2%", "No"],
        ["Coriolis", "Mass flow, density, custody transfer", "Medium", "0.1 to 0.2%", "No"],
        ["Variable area", "Local indication, purge, utilities", "Low", "1.6 to 4%", "Float only"],
    ]),
    h2("select", "How to Select a Flow Meter"),
    checklist([
        ("Fluid", "Identify liquid, gas, steam or slurry, plus conductivity, viscosity and cleanliness."),
        ("Measurement", "Decide between volume flow, mass flow or a simple flow or no flow signal."),
        ("Range", "State minimum, normal and maximum flow, and the turndown required."),
        ("Line", "Note pipe size, material, pressure and temperature."),
        ("Installation", "Check available straight runs before and after the meter."),
        ("Output", "Confirm 4 to 20 mA, pulse, HART or fieldbus requirements."),
    ]),
    p("Comparing the types of flow meters against this checklist usually narrows the choice to one or two options. For basic formulas, the " + ext("https://www.instrumentationblog.in/flow-rate-formula/", "flow rate formula guide") + " is a useful reference."),
    h2("install", "Installation Tips"),
    twocol([
        ("Do", "bi-check-circle-fill", [
            "Provide the straight runs stated by the manufacturer.",
            "Keep liquid meters full; install in a rising line where possible.",
            "Ground electromagnetic meters correctly.",
        ]),
        ("Avoid", "bi-x-circle-fill", [
            "Installing right after pumps, valves or elbows.",
            "Air or gas pockets in liquid lines.",
            "Vibration sources close to vortex and Coriolis meters.",
        ]),
    ]),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Sizing to the pipe, not the flow.", "An oversized meter runs near its minimum and loses accuracy."),
        ("Ignoring fluid conductivity.", "Electromagnetic meters do not work on oils or hydrocarbons."),
        ("Too short straight runs.", "Swirl and distorted profiles cause large errors."),
        ("Forgetting density correction.", "Gas and steam volumes change with pressure and temperature."),
    ]),
    p("If a meter already shows strange values, read our guide on " + link("/blog/flow-meter-incorrect-readings-causes-fixes", "flow meter incorrect readings, causes and fixes") + "."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Which flow meter is the most accurate?", "Coriolis meters are generally the most accurate, often within 0.1% of reading, and they measure mass flow directly."),
        ("Which flow meter has no moving parts?", "Electromagnetic, ultrasonic, vortex, Coriolis and differential pressure meters all have no moving parts in the flow."),
        ("Can one meter measure both liquid and gas?", "Coriolis and some ultrasonic meters can, but most installations use a technology optimised for one phase."),
    ]),
]

META["infographic"].update({"layout": "compare", "title": "Which Flow Meter for Which Fluid?",
   "columns": [["Clean liquids", ["Electromagnetic (conductive)", "Turbine", "Ultrasonic", "Coriolis for mass"]],
               ["Gases and steam", ["Vortex", "Differential pressure", "Thermal mass", "Coriolis for gas"]],
               ["Slurries and dirty liquids", ["Electromagnetic", "Clamp on ultrasonic", "Coriolis", "Avoid turbine meters"]]]})
