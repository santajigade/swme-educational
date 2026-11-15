META = {
    "category": "temperature-measurement-guides",
    "title": "How an RTD Works: Pt100 Principle, Wiring and Accuracy",
    "keyword": "RTD",
    "subtitle": "Resistance temperature detectors, Pt100 values, 2, 3 and 4 wire circuits",
    "meta_title": "How an RTD Works: Pt100 Principle, Wiring and Accuracy",
    "meta_description": "Learn how an RTD works, why Pt100 sensors are used, accuracy classes, 2, 3 and 4 wire connections and installation tips for accurate temperature.",
    "summary": "Pt100 principle, accuracy classes, wiring options and installation tips for RTD sensors.",
    "card_title": "How an RTD Works",
    "author": "SWME Technical Staff",
    "published": "2026-11-15",
    "status": "published",
    "sort_order": 1,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "title": "How an RTD Measures Temperature",
        "alt": "Infographic showing how an RTD Pt100 sensor converts temperature into a resistance and a 4 to 20 mA signal",
        "steps": [
            ["Heat reaches the element", "Process heat passes through the thermowell and sheath to the platinum element."],
            ["Resistance changes", "Platinum resistance rises about 0.385 ohm per degree Celsius for a Pt100."],
            ["Small current applied", "The transmitter passes a tiny current and measures the voltage across the element."],
            ["Temperature output", "Resistance is converted to temperature and sent as 4 to 20 mA or HART."],
        ],
    },
}

BODY = [
    takeaways([
        "An RTD measures temperature through the change in resistance of a metal, usually platinum.",
        "A Pt100 has 100 ohms at 0 degrees Celsius and about 138.5 ohms at 100 degrees Celsius.",
        "Three wire and four wire circuits cancel the resistance of the connecting cables.",
        "RTD sensors are more accurate and stable than thermocouples but cover a lower temperature range.",
    ]),
    p("A resistance temperature detector, or <strong>RTD</strong>, is the most common sensor for accurate process temperature between about minus 200 and plus 600 degrees Celsius. It is used in pipelines, tanks, heat exchangers and HVAC systems across every industry.",
      "This guide explains how an RTD works, what the Pt100 tables mean and how to wire the sensor for the best accuracy. SWME supplies " + link("/rtd-thermocouples", "RTD and thermocouple sensors") + ", " + link("/temperature-transmitters", "temperature transmitters") + " and " + link("/thermowells", "thermowells") + "."),
    toc([("principle", "Working principle"), ("pt100", "Pt100 and Pt1000 values"), ("accuracy", "Accuracy classes"),
         ("wiring", "RTD wiring: 2, 3 and 4 wire"), ("vs", "RTD or thermocouple?"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("principle", "How an RTD Works"),
    p("The electrical resistance of a pure metal increases as it gets hotter. Platinum is the preferred metal because its resistance changes in a very stable, repeatable and almost linear way. The sensing element is either a fine wire coil or a thin platinum film on a ceramic substrate.",
      "The transmitter passes a small, constant current through the element and measures the voltage across it. Using Ohm's law, it calculates the resistance and then converts it to temperature. For example, a measured resistance of 119.4 ohms corresponds to about 50 degrees Celsius for a Pt100."),
    INFOGRAPHIC,
    h2("pt100", "Pt100 and Pt1000 Values"),
    table(["Temperature", "Pt100 resistance", "Pt1000 resistance"], [
        ["Minus 50 degrees Celsius", "80.31 ohm", "803.1 ohm"],
        ["0 degrees Celsius", "100.00 ohm", "1000.0 ohm"],
        ["50 degrees Celsius", "119.40 ohm", "1194.0 ohm"],
        ["100 degrees Celsius", "138.51 ohm", "1385.1 ohm"],
        ["200 degrees Celsius", "175.86 ohm", "1758.6 ohm"],
    ]),
    p("These values follow the IEC 60751 standard. You can calculate any point with the " + ext("https://zentacalculator.com/engineering/pt100-resistance/", "Pt100 and Pt1000 resistance calculator") + ". A Pt1000 has ten times the resistance, so cable resistance matters less, which makes it popular in building automation."),
    dyk("A Pt100 changes by only about 0.385 ohm per degree Celsius. That means 1 ohm of extra cable resistance looks like an error of more than 2.5 degrees Celsius. This is why two wire connections are rarely used for accurate process measurement. Check the effect with the " + ext("https://zentacalculator.com/engineering/rtd-lead-wire-error/", "RTD lead wire error calculator") + "."),
    h2("accuracy", "Accuracy Classes"),
    rows([
        ("Class AA (1/3 DIN)", "plus or minus 0.1 degrees Celsius at 0 degrees Celsius; for laboratory and critical measurements."),
        ("Class A", "plus or minus 0.15 degrees Celsius at 0 degrees Celsius; for precise process control."),
        ("Class B", "plus or minus 0.3 degrees Celsius at 0 degrees Celsius; the standard industrial choice."),
    ]),
    p("Tolerance grows with temperature, so a class B sensor at 200 degrees Celsius may be off by about 1.3 degrees Celsius. In addition, the transmitter and installation add their own errors."),
    h2("wiring", "RTD Wiring: 2, 3 and 4 Wire"),
    svg("".join(
        f'<g transform="translate({x},0)">'
        f'<text x="120" y="40" text-anchor="middle" font-size="16" font-weight="700" fill="{T["tx"]}">{title}</text>'
        f'<rect x="20" y="110" width="40" height="140" rx="6" fill="{T["bg"]}" stroke="{T["c"]}" stroke-width="2.5"/>'
        f'<path d="M40 125 l10 8 l-20 10 l20 10 l-20 10 l20 10 l-20 10 l20 10 l-20 10 l20 10 l-10 8" fill="none" stroke="{T["c"]}" stroke-width="2"/>'
        f'<text x="40" y="275" text-anchor="middle" font-size="12" fill="#333">Pt100</text>'
        + "".join(f'<polyline points="60,{ty} {80+12*k},{ty} {80+12*k},{wy} 190,{wy}" fill="none" stroke="#495057" stroke-width="2"/>'
                  f'<circle cx="60" cy="{ty}" r="3" fill="#495057"/>'
                  for k, (ty, wy) in enumerate(wires))
        + f'<rect x="190" y="70" width="44" height="220" rx="6" fill="{T["c"]}"/>'
        f'<text x="212" y="185" text-anchor="middle" font-size="11" fill="#fff" transform="rotate(-90 212 180)">Transmitter</text>'
        f'<text x="120" y="325" text-anchor="middle" font-size="13" fill="#555">{note}</text></g>'
        for x, title, wires, note in (
            (10, "2 wire", [(125, 125), (235, 235)], "Cable adds error"),
            (275, "3 wire", [(125, 100), (125, 150), (235, 235)], "Cable resistance cancelled"),
            (540, "4 wire", [(125, 95), (125, 140), (235, 215), (235, 260)], "Highest accuracy"))),
        "RTD connection options from sensor (left) to transmitter (right)", 340),
    twocol([
        ("2 and 3 wire", "bi-diagram-2", [
            "2 wire: cable resistance adds directly to the reading.",
            "3 wire: a third lead lets the transmitter subtract cable resistance.",
            "3 wire is the industrial standard for most process RTD loops.",
        ]),
        ("4 wire", "bi-diagram-3", [
            "Separate leads carry current and measure voltage.",
            "Cable resistance is almost fully cancelled.",
            "Used for laboratory, custody and very long cable runs.",
        ]),
    ]),
    p("Mounting a head transmitter on the sensor shortens the RTD cable to a few centimetres and sends a robust 4 to 20 mA signal to the control room. See this practical guide to " + ext("https://www.instrumentationblog.in/temperature-transmitter-wiring/", "temperature transmitter wiring") + "."),
    h2("vs", "RTD or Thermocouple?"),
    table(["Factor", "RTD", "Thermocouple"], [
        ["Typical range", "Minus 200 to 600 degrees Celsius", "Up to 1,700 degrees Celsius"],
        ["Accuracy", "Higher", "Lower"],
        ["Long term stability", "Excellent", "Drifts at high temperature"],
        ["Response time", "Slower", "Faster"],
        ["Cost", "Higher", "Lower"],
    ]),
    p("For a deeper comparison at high temperatures, read our blog on " + link("/blog/rtd-vs-thermocouple-high-temperature-guide", "RTD vs thermocouple for high temperature") + ". Every RTD should also be protected by a well; see " + link("/what-is-a-thermowell", "what is a thermowell") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Two wire connection on long cables.", "Cable resistance shows up as a large temperature offset."),
        ("Too short immersion length.", "Heat conducted along the stem makes the reading too low."),
        ("Wrong curve in the transmitter.", "Pt100 and Pt1000, or different alpha values, give large errors."),
        ("Vibration without support.", "Wire wound elements can crack; use thin film or spring loaded designs."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What does Pt100 mean?", "Pt is the chemical symbol for platinum, and 100 is the resistance in ohms at 0 degrees Celsius."),
        ("Is an RTD better than a thermocouple?", "An RTD is more accurate and stable below about 600 degrees Celsius. A thermocouple is better for very high temperatures and fast response."),
        ("How do I test an RTD?", "Disconnect it and measure the resistance with a multimeter, then compare it with the Pt100 table for the known temperature."),
    ]),
]

META["infographic"].update({"layout": "flow"})
