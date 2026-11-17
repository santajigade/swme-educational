META = {
    "category": "level-measurement-guides",
    "title": "DP Level Measurement in Closed Tanks: Dry Leg and Wet Leg",
    "keyword": "dp level measurement",
    "subtitle": "How a differential pressure transmitter cancels vessel pressure, with worked dry leg and wet leg examples",
    "meta_title": "DP Level Measurement in Closed Tanks: Dry and Wet Leg",
    "meta_description": "How DP level measurement works in closed tanks: HP and LP connections, dry leg vs wet leg, LRV and URV formulas with worked examples, and remote seals.",
    "summary": "How a DP transmitter measures level in a pressurised tank, when to use a dry or wet leg, and how to calculate the range.",
    "card_title": "DP Level Measurement in Closed Tanks",
    "author": "SWME Technical Staff",
    "published": "2026-11-17",
    "status": "published",
    "sort_order": 4,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "levels",
        "title": "Key Heights in a Closed Tank",
        "alt": "Infographic showing the key heights for DP level measurement in a closed tank: HP tap, zero level, maximum level and LP tap",
        "top_label": "Tank top",
        "bottom_label": "Tank bottom",
        "steps": [
            ["HP tap", "Bottom connection senses liquid head plus vessel pressure."],
            ["Zero level", "Lowest level to measure; sets the LRV."],
            ["Maximum level", "Highest level to measure; sets the URV."],
            ["LP tap", "Top connection senses vessel pressure only."],
        ],
        "levels": [
            ["LP tap in vapour space", "Senses only the vessel pressure, which cancels out.", 0.93],
            ["Maximum level (URV, 20 mA)", "Top of the measured span, H1 above the zero level.", 0.68],
            ["Zero level (LRV, 4 mA)", "Bottom of the span, H2 above the HP tap.", 0.3],
            ["HP tap and transmitter", "Liquid head plus vessel pressure acts here.", 0.06],
        ],
    },
}

_C = "#0c8599"
_T = "#0a5f6d"

_diag = (
    arrow_defs(_C)
    + '<rect x="200" y="40" width="220" height="290" rx="18" fill="#f8f9fa" stroke="#495057" stroke-width="3"/>'
    + '<rect x="203" y="150" width="214" height="177" rx="14" fill="#d3f0f4"/>'
    + '<line x1="203" y1="150" x2="417" y2="150" stroke="' + _C + '" stroke-width="2"/>'
    + '<text x="310" y="100" text-anchor="middle" font-size="14" fill="#555">Vapour space</text>'
    + '<text x="310" y="122" text-anchor="middle" font-size="14" fill="#555">vessel pressure P</text>'
    + '<text x="310" y="240" text-anchor="middle" font-size="14" font-weight="700" fill="' + _T + '">Liquid, SG1</text>'
    # max and zero lines
    + '<line x1="170" y1="130" x2="200" y2="130" stroke="#495057" stroke-width="1.5" stroke-dasharray="4 3"/>'
    + '<line x1="170" y1="270" x2="200" y2="270" stroke="#495057" stroke-width="1.5" stroke-dasharray="4 3"/>'
    + '<line x1="170" y1="310" x2="200" y2="310" stroke="#495057" stroke-width="1.5" stroke-dasharray="4 3"/>'
    + '<line x1="160" y1="134" x2="160" y2="266" stroke="#495057" stroke-width="1.5" marker-end="url(#ah)"/>'
    + '<line x1="160" y1="266" x2="160" y2="134" stroke="#495057" stroke-width="1.5" marker-end="url(#ah)"/>'
    + '<text x="150" y="196" text-anchor="end" font-size="14" font-weight="700" fill="#333">H1</text>'
    + '<text x="150" y="214" text-anchor="end" font-size="12" fill="#555">span</text>'
    + '<text x="150" y="295" text-anchor="end" font-size="14" font-weight="700" fill="#333">H2</text>'
    + '<line x1="160" y1="274" x2="160" y2="306" stroke="#495057" stroke-width="1.5"/>'
    + '<text x="140" y="126" text-anchor="end" font-size="12" fill="#555">Maximum level</text>'
    + '<text x="140" y="266" text-anchor="end" font-size="12" fill="#555">Zero level</text>'
    # HP tap and transmitter
    + '<line x1="420" y1="310" x2="560" y2="310" stroke="#495057" stroke-width="4"/>'
    + '<rect x="560" y="285" width="90" height="50" rx="8" fill="#d3f0f4" stroke="' + _C + '" stroke-width="2"/>'
    + '<text x="605" y="315" text-anchor="middle" font-size="14" font-weight="700" fill="' + _T + '">DP</text>'
    + '<text x="545" y="302" text-anchor="end" font-size="13" font-weight="700" fill="' + _T + '">HP</text>'
    + '<text x="660" y="300" font-size="13" font-weight="700" fill="' + _T + '">LP</text>'
    # LP leg from top
    + '<line x1="420" y1="70" x2="690" y2="70" stroke="#495057" stroke-width="4"/>'
    + '<line x1="690" y1="70" x2="690" y2="310" stroke="#495057" stroke-width="4"/>'
    + '<line x1="690" y1="310" x2="650" y2="310" stroke="#495057" stroke-width="4"/>'
    + '<text x="700" y="160" font-size="13" font-weight="700" fill="#333">LP leg</text>'
    + '<text x="700" y="180" font-size="12" fill="#555">dry: gas filled</text>'
    + '<text x="700" y="198" font-size="12" fill="#555">wet: liquid SG2</text>'
    + '<text x="400" y="358" text-anchor="middle" font-size="13" fill="#555">DP = pressure on HP side minus pressure on LP side; the vessel pressure P acts on both and cancels</text>'
)

BODY = [
    takeaways([
        "In a closed tank, the transmitter HP side connects to the bottom and the LP side to the vapour space.",
        "Vessel pressure acts on both sides and cancels, so the DP is set by liquid height and density.",
        "Use a dry leg when the vapour does not condense; use a wet leg when it does.",
        "A wet leg adds a fixed head on the LP side, which makes the calibrated range negative.",
    ]),
    p("A level transmitter on an open tank only has to read the liquid head. In a pressurised or vented vapour space, however, the vessel pressure adds to the reading and must be removed. <strong>DP level measurement</strong> solves this by measuring the difference between the bottom of the tank and the vapour space above the liquid.",
      "This guide explains the connections, the dry leg and wet leg options and how to calculate the range. SWME supplies " + link("/differential-pressure-transmitters", "differential pressure transmitters") + ", " + link("/level-transmitters", "level transmitters") + " and " + link("/diaphragm-seals", "diaphragm seals") + " for tanks and vessels across the GCC."),
    toc([("principle", "How DP level measurement works"), ("legs", "Dry leg vs wet leg"), ("calc", "Calculating LRV and URV"),
         ("seals", "Remote seals and capillaries"), ("check", "Installation checklist"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("principle", "How DP Level Measurement Works in a Closed Tank"),
    p("The hydrostatic pressure of a liquid is its height times its density. In a closed tank, the bottom connection sees that head plus the vessel pressure, while the top connection sees the vessel pressure alone. As " + ext("https://yokogawa.com/us/library/resources/media-publications/how-to-avoid-temperature-effects-in-differential-pressure-level-measurements", "Yokogawa") + " explains, the low pressure side of the transmitter is connected to the top of the tank, so the pressure at the tank top becomes the reference. The vessel pressure cancels, and the output, 4 mA at empty and 20 mA at full, follows level only."),
    svg(_diag, "DP level measurement on a closed tank with HP tap at the bottom and LP leg to the vapour space", 370),
    INFOGRAPHIC,
    p("You can check the head for any liquid with the " + ext("https://zentacalculator.com/engineering/hydrostatic-pressure/", "hydrostatic pressure calculator") + " or read about the " + ext("https://www.instrumentationblog.in/hydrostatic-pressure-formula/", "hydrostatic pressure formula") + "."),
    h2("legs", "Dry Leg vs Wet Leg"),
    twocol([
        ("Dry leg", "bi-wind", [
            "LP impulse line is filled with gas or air",
            "For vapour that does not condense",
            "Process temperature close to ambient",
            "LP side adds no liquid head",
        ]),
        ("Wet leg", "bi-droplet", [
            "LP impulse line is filled with a liquid",
            "For vapour that tends to condense",
            "Process temperature well above or below ambient",
            "Fixed head on the LP side shifts the range",
        ]),
    ]),
    p("The choice follows the guidance from " + ext("https://instrumentationtools.com/dp-transmitter-dry-leg-wet-leg-calculations", "Instrumentation Tools") + ". If condensate collects in a dry leg, it adds an unknown head on the LP side and the level reading drifts low, which is why a condensing service needs a deliberately filled wet leg instead."),
    h2("calc", "Calculating LRV and URV"),
    p("The lower range value (LRV) is the DP at the zero level and the upper range value (URV) is the DP at the maximum level. With H1 as the span, H2 as the height of the zero level above the HP tap, SG1 as the liquid specific gravity and, for a wet leg, Y as the wet leg height and SG2 as its fill liquid gravity:"),
    rows([
        ("Dry leg", "LRV = H2 × SG1 and URV = (H1 + H2) × SG1."),
        ("Wet leg", "LRV = H2 × SG1 minus Y × SG2 and URV = (H1 + H2) × SG1 minus Y × SG2."),
    ]),
    table(["Worked example", "Dry leg", "Wet leg"], [
        ["Inputs", "H1 = 500 mm, H2 = 200 mm, SG1 = 0.9", "Same, plus Y = 700 mm, SG2 = 1.0"],
        ["LRV", "180 mmWC", "minus 520 mmWC"],
        ["URV", "630 mmWC", "minus 70 mmWC"],
        ["Span", "450 mmWC", "450 mmWC"],
    ]),
    p("Example values from Instrumentation Tools. Note that the span is the same in both cases; the wet leg only shifts the whole range below zero. Enter the LRV and URV in the transmitter with a HART communicator. The " + ext("https://zentacalculator.com/engineering/dp-level-range/", "DP level range calculator") + " and the " + ext("https://zentacalculator.com/engineering/4-20ma-scaling/", "4 to 20 mA scaling calculator") + " help you check the numbers."),
    dyk("In the wet leg example, both the LRV and the URV are negative. With the tank full, the liquid head on the HP side (630 mmWC) is still smaller than the 700 mmWC head of the wet leg, so the transmitter sees more pressure on its LP side across the whole range."),
    h2("seals", "Remote Seals and Capillaries"),
    p("Remote seals connected by filled capillaries are one of the most common ways to connect a DP transmitter, and Yokogawa notes that they eliminate corrosion, heat and maintenance issues of impulse lines. The fill fluid adds its own head, which the transmitter can compensate for, but temperature changes the fill density. Unequal capillary lengths or sun on one side cause drift, so balanced systems use equal capillaries or matched fill volumes. Electronic remote sensors replace capillaries with wiring, although accuracy is harder to achieve at high static pressure."),
    h2("check", "Installation Checklist"),
    checklist([
        ("Connections", "HP to the bottom tap, LP to the vapour space above the maximum level."),
        ("Leg type", "Dry leg for non condensing vapour, wet leg for condensing service."),
        ("Isolation", "Fit a valve manifold from our " + link("/manifolds-fittings", "manifolds and fittings") + " range for safe zeroing."),
        ("Ranging", "Calculate LRV and URV from the real tap heights and fill liquid gravity."),
        ("Verification", "Check the reading at a known level after commissioning."),
    ]),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Dry leg on condensing vapour.", "Condensate builds up in the LP line and the reading drifts."),
        ("Wrong wet leg gravity.", "An incorrect SG2 shifts both range values."),
        ("Unbalanced capillaries.", "Different lengths or temperatures on each side cause zero drift."),
    ]),
    p("For calibration pitfalls, read our blog on " + link("/blog/level-transmitter-calibration-mistakes", "level transmitter calibration mistakes") + ". To compare non contact options, see " + link("/radar-vs-ultrasonic-level-measurement", "radar vs ultrasonic level measurement") + ", and for alarms, " + link("/level-switch-types", "level switch types") + ". More reading is on the " + ext("https://www.instrumentationblog.in/category/process-instrumentation/level-measurement/", "level measurement") + " pages of Instrumentation Blog."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Why is DP level measurement used on closed tanks?", "Because the LP side senses the vessel pressure and cancels it, leaving only the liquid head."),
        ("When should I use a wet leg instead of a dry leg?", "Use a wet leg when the vapour tends to condense, for example when the process is well above ambient temperature."),
        ("Why are the range values negative with a wet leg?", "The filled LP leg adds a fixed head; when that head is larger than the liquid head, the DP stays below zero across the range."),
    ]),
]
