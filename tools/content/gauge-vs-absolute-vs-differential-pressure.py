META = {
    "category": "pressure-measurement-guides",
    "title": "Gauge vs Absolute vs Differential Pressure Explained",
    "keyword": "gauge vs absolute vs differential pressure",
    "subtitle": "Reference points, formulas, examples and how to choose the right measurement",
    "meta_title": "Gauge vs Absolute vs Differential Pressure Explained",
    "meta_description": "Understand gauge vs absolute vs differential pressure, how each is referenced, how to convert between them and which one your application needs.",
    "summary": "Reference points, conversions, examples and selection tips for the three pressure types.",
    "card_title": "Gauge vs Absolute vs Differential Pressure",
    "author": "SWME Technical Staff",
    "published": "2026-11-15",
    "status": "published",
    "sort_order": 1,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "title": "Three Ways to Measure Pressure",
        "alt": "Infographic comparing gauge, absolute and differential pressure reference points",
        "steps": [
            ["Absolute pressure", "Measured from a perfect vacuum. Zero means no pressure at all."],
            ["Atmospheric pressure", "About 1.013 bar at sea level. It changes with weather and altitude."],
            ["Gauge pressure", "Measured from local atmosphere. Absolute pressure minus atmospheric pressure."],
            ["Differential pressure", "The difference between two process points, independent of atmosphere."],
        ],
    },
}

BODY = [
    takeaways([
        "Every pressure value needs a reference point: vacuum, atmosphere or a second process point.",
        "Gauge pressure equals absolute pressure minus local atmospheric pressure.",
        "Differential pressure compares two points and is the basis of many flow, level and filter measurements.",
        "Choosing the wrong reference causes errors that no calibration can remove.",
    ]),
    p("Engineers often compare <strong>gauge vs absolute vs differential pressure</strong> when they specify a new instrument. The three terms describe the same physical quantity, but each one uses a different reference point. If the reference does not match the process, the reading will be wrong even when the instrument itself is perfectly accurate.",
      "This guide explains each pressure type in simple terms, shows how to convert between them and helps you decide which measurement your application needs. SWME supplies " + link("/pressure-gauges", "pressure gauges") + ", transmitters and switches in all three versions."),
    toc([("reference", "Why the reference point matters"), ("types", "The three pressure types"),
         ("conversion", "Converting between pressure types"), ("compare", "Gauge vs absolute vs differential pressure compared"),
         ("applications", "Typical applications"), ("choose", "How to choose"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("reference", "Why the Reference Point Matters"),
    p("Pressure is force per unit area. To give it a number, you must state where zero is. A tyre gauge reads zero when the tyre is open to air, yet the air around us still presses on everything at about 1 bar. In other words, the gauge ignores the atmosphere and shows only the extra pressure inside the tyre.",
      "For example, a vacuum pump that removes all the air from a chamber would read about minus 1 bar on a gauge instrument, but close to 0 bar on an absolute instrument. Both readings are correct. They simply start from different zero points."),
    INFOGRAPHIC,
    h2("types", "The Three Pressure Types"),
    svg(arrow_defs(T["c"]) +
        '<line x1="120" y1="320" x2="120" y2="30" stroke="#999" stroke-width="2"/>'
        '<line x1="100" y1="320" x2="600" y2="320" stroke="#333" stroke-width="2"/>'
        '<text x="610" y="324" font-size="14" fill="#333">Perfect vacuum (0 bar a)</text>'
        '<line x1="100" y1="200" x2="600" y2="200" stroke="#999" stroke-width="2" stroke-dasharray="8 6"/>'
        '<text x="610" y="204" font-size="14" fill="#333">Atmosphere (1.013 bar a)</text>'
        f'<circle cx="300" cy="80" r="9" fill="{T["c"]}"/><text x="315" y="75" font-size="14" font-weight="600" fill="{T["tx"]}">Process pressure</text>'
        f'<line x1="250" y1="318" x2="250" y2="90" stroke="{T["c"]}" stroke-width="3" marker-end="url(#ah)"/>'
        f'<text x="240" y="270" font-size="14" text-anchor="end" fill="{T["tx"]}" font-weight="600">Absolute</text>'
        f'<line x1="350" y1="198" x2="350" y2="90" stroke="{T["c"]}" stroke-width="3" marker-end="url(#ah)"/>'
        f'<text x="360" y="150" font-size="14" fill="{T["tx"]}" font-weight="600">Gauge</text>'
        f'<circle cx="520" cy="110" r="9" fill="{T["c"]}"/><text x="535" y="105" font-size="13" fill="#333">Point H</text>'
        f'<circle cx="520" cy="160" r="9" fill="#f08c00"/><text x="535" y="175" font-size="13" fill="#333">Point L</text>'
        f'<line x1="500" y1="158" x2="500" y2="118" stroke="#f08c00" stroke-width="3" marker-end="url(#ah)"/>'
        '<text x="490" y="140" font-size="14" text-anchor="end" fill="#d9480f" font-weight="600">Differential</text>'
        f'<circle cx="300" cy="260" r="9" fill="#868e96"/><text x="315" y="264" font-size="13" fill="#555">Vacuum reading (negative gauge)</text>',
        "Gauge, absolute and differential pressure measured from different reference points", 360),
    rows([
        ("Absolute pressure (bar a)", "measured relative to a perfect vacuum. It can never be negative, and it does not change with weather or altitude."),
        ("Gauge pressure (bar g)", "measured relative to the local atmosphere. It is the most common reading on pipelines, pumps, vessels and hydraulic systems."),
        ("Differential pressure (bar d)", "the difference between two process pressures. The instrument has two ports, often marked high (H) and low (L)."),
    ]),
    p("In addition, you will sometimes see <strong>sealed gauge</strong> pressure. A sealed gauge sensor uses a fixed reference, usually 1.013 bar, sealed inside the instrument. It behaves like a gauge sensor but is not affected by moisture entering a vent. Sealed gauge is common in high pressure ranges and in wet environments."),
    dyk("Atmospheric pressure in Dubai at sea level is close to 1.013 bar, but on a mountain site at 2,000 metres it drops to about 0.8 bar. A gauge instrument automatically follows this change, while an absolute instrument does not. Read more about the " + ext("https://www.instrumentationblog.in/category/process-instrumentation/pressure-measurement/", "fundamentals of pressure measurement") + "."),
    h2("conversion", "Converting Between Pressure Types"),
    p("The conversion between gauge and absolute pressure is simple, provided you know the local atmospheric pressure:"),
    rows([
        ("Absolute", "gauge pressure plus atmospheric pressure. For example, 5 bar g plus 1.013 bar equals 6.013 bar a."),
        ("Gauge", "absolute pressure minus atmospheric pressure. For example, 0.5 bar a minus 1.013 bar equals minus 0.513 bar g."),
        ("Differential", "high side pressure minus low side pressure. Both sides must use the same reference."),
    ]),
    p("You can check these values quickly with the " + ext("https://zentacalculator.com/engineering/absolute-gauge-pressure/", "absolute to gauge pressure calculator") + ". For liquid columns, the " + ext("https://zentacalculator.com/engineering/hydrostatic-pressure/", "hydrostatic pressure and tank level calculator") + " converts between pressure and height."),
    h2("compare", "Gauge vs Absolute vs Differential Pressure Compared"),
    table(["Feature", "Gauge", "Absolute", "Differential"], [
        ["Zero reference", "Local atmosphere", "Perfect vacuum", "Second process point"],
        ["Can read negative", "Yes (vacuum)", "No", "Yes, if low side is higher"],
        ["Affected by weather", "Yes, follows atmosphere", "No", "No"],
        ["Number of ports", "One (plus vent)", "One", "Two (H and L)"],
        ["Unit suffix", "bar g, psig", "bar a, psia", "bar d, psid"],
        ["Typical use", "Pumps, pipelines, vessels", "Vacuum, distillation, barometric", "Flow, level, filters"],
    ]),
    h3("Vacuum and compound ranges"),
    p("Vacuum work shows the difference between the three types most clearly. A process that runs at 50 mbar a is close to a perfect vacuum. On a gauge instrument the same condition reads about minus 963 mbar g, and the value drifts as the weather changes. For this reason, vacuum dryers, distillation columns and vacuum packaging lines use absolute sensors.",
      "A compound range covers both vacuum and positive pressure on one gauge scale, for example minus 1 to plus 5 bar g. Compound gauges are common on pump suction lines, where pressure can swing above and below atmosphere during start up. In addition, they help operators see cavitation risk at a glance."),
    h2("applications", "Typical Applications"),
    twocol([
        ("Gauge and absolute", "bi-speedometer2", [
            "Gauge: pump discharge, compressed air, hydraulic lines, tank blanketing.",
            "Absolute: vacuum distillation, evaporators, steam tables, gas density correction.",
            "Absolute is required wherever the process is near or below atmospheric pressure.",
        ]),
        ("Differential", "bi-arrow-left-right", [
            "Flow across an orifice plate, venturi or pitot tube.",
            "Liquid level in closed, pressurized tanks.",
            "Filter and strainer condition monitoring.",
        ]),
    ]),
    p("Differential pressure is especially useful for flow. A " + link("/differential-pressure-transmitters", "differential pressure transmitter") + " across an " + link("/orifice-plates", "orifice plate") + " gives a signal proportional to the square of the flow rate. The " + ext("https://zentacalculator.com/engineering/dp-flow-square-root/", "DP flow square root calculator") + " shows how this relationship works."),
    p("For filter monitoring, a " + link("/differential-pressure-gauges", "differential pressure gauge") + " shows the operator when a filter element is blocked. For closed tanks, see this guide on " + ext("https://www.instrumentationblog.in/dp-transmitter-level-measurement/", "DP transmitter level measurement") + "."),
    h2("choose", "How to Choose the Right Measurement"),
    checklist([
        ("Ask what the process cares about", "Use gauge when the result is compared with the surroundings, such as leak testing or pump performance."),
        ("Check for vacuum", "If pressure can fall below atmospheric, consider absolute or compound range instruments."),
        ("Look for a second point", "When you need the difference across a device, use differential, not two separate gauge readings."),
        ("Consider static pressure", "Differential instruments must withstand the full line pressure on both sides."),
        ("Match the control system", "Confirm whether the PLC or DCS expects bar g, bar a or bar d values."),
    ]),
    p("When you weigh gauge vs absolute vs differential pressure for a new project, write the reference on every datasheet line. This simple habit prevents most commissioning errors."),
    p("Gauge, absolute and differential versions exist for gauges, " + link("/pressure-switches", "pressure switches") + " and " + link("/pressure-transmitters", "pressure transmitters") + ". To understand how a transmitter converts the reading into a signal, read " + link("/what-is-a-pressure-transmitter", "what is a pressure transmitter") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Mixing units without the suffix.", "A value of 2 bar means nothing until you know if it is bar g or bar a."),
        ("Using gauge sensors for deep vacuum.", "Weather changes then appear as process changes."),
        ("Subtracting two gauge readings for flow.", "Small errors in each reading become a large error in the difference."),
        ("Blocking the vent of a gauge sensor.", "Paint or dirt on the vent turns it into an unintended sealed instrument."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Is psig the same as gauge pressure?", "Yes. The g in psig means gauge, so the value is measured relative to atmospheric pressure. Psia means absolute."),
        ("Can absolute pressure be negative?", "No. Absolute pressure starts at a perfect vacuum, so the lowest possible value is zero."),
        ("Which is better for flow measurement?", "Differential pressure, because flow creates a pressure drop across a primary element such as an orifice plate."),
    ]),
]

META["infographic"].update({"layout": "compare", "title": "Gauge vs Absolute vs Differential",
   "columns": [["Gauge", ["Zero = local atmosphere", "Can read vacuum as negative", "Unit: bar g, psig", "Pumps, pipelines, vessels"]],
               ["Absolute", ["Zero = perfect vacuum", "Never negative", "Unit: bar a, psia", "Vacuum and distillation"]],
               ["Differential", ["Zero = second process point", "Two ports, H and L", "Unit: bar d, psid", "Flow, level, filters"]]]})
