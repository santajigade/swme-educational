META = {
    "category": "temperature-measurement-guides",
    "title": "Bimetal Thermometer Working Principle Explained",
    "keyword": "bimetal thermometer",
    "subtitle": "How two bonded metals, a helical coil and a pointer shaft turn temperature into a dial reading with no power",
    "meta_title": "Bimetal Thermometer Working Principle Explained",
    "meta_description": "How a bimetal thermometer works: bonded metals, helical coil, accuracy classes to EN 13190, ranges, stem immersion, mounting options and calibration tips.",
    "summary": "How a bimetal thermometer converts thermal expansion into pointer movement, with accuracy classes, ranges and installation tips.",
    "card_title": "Bimetal Thermometer Working Principle",
    "author": "SWME Technical Staff",
    "published": "2026-11-18",
    "status": "published",
    "sort_order": 4,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "steps",
        "title": "How a Bimetal Thermometer Works",
        "alt": "Infographic showing four steps of the bimetal thermometer working principle from temperature change to dial reading",
        "steps": [
            ["Temperature change", "Heat from the process reaches the sensing end of the stem."],
            ["Unequal expansion", "Two bonded metals expand by different amounts, so the strip bends."],
            ["Coil rotates", "The helical coil winds or unwinds and turns the pointer shaft."],
            ["Dial reading", "The pointer shows temperature on the dial with no power needed."],
        ],
    },
}

_C = "#d9480f"

_diag = (
    arrow_defs(_C)
    # dial
    + '<circle cx="200" cy="80" r="62" fill="#fff" stroke="#495057" stroke-width="4"/>'
    + '<circle cx="200" cy="80" r="5" fill="#495057"/>'
    + '<line x1="200" y1="80" x2="238" y2="50" stroke="' + _C + '" stroke-width="3"/>'
    + '<text x="272" y="84" font-size="13" font-weight="700" fill="#a33608">Dial and pointer</text>'
    # stem
    + '<rect x="186" y="142" width="28" height="208" fill="#f1f3f5" stroke="#495057" stroke-width="2"/>'
    # shaft
    + '<line x1="200" y1="144" x2="200" y2="270" stroke="#868e96" stroke-width="3"/>'
    # helix in lower stem
    + "".join(f'<path d="M190 {y} Q200 {y - 8} 210 {y + 4}" fill="none" stroke="{_C}" stroke-width="3"/>' for y in range(272, 344, 10))
    + '<circle cx="200" cy="344" r="4" fill="#495057"/>'
    # labels
    + '<line x1="214" y1="200" x2="300" y2="200" stroke="#495057" stroke-width="1.5"/>'
    + '<text x="306" y="204" font-size="13" font-weight="700" fill="#a33608">Pointer shaft</text>'
    + '<line x1="214" y1="300" x2="300" y2="290" stroke="#495057" stroke-width="1.5"/>'
    + '<text x="306" y="288" font-size="13" font-weight="700" fill="#a33608">Helical bimetal coil</text>'
    + '<text x="306" y="304" font-size="12" fill="#555">in the lower part of the stem</text>'
    + '<line x1="204" y1="344" x2="300" y2="340" stroke="#495057" stroke-width="1.5"/>'
    + '<text x="306" y="344" font-size="13" font-weight="700" fill="#a33608">Fixed end at the stem tip</text>'
    # strip inset
    + '<rect x="500" y="30" width="280" height="300" rx="10" fill="#fff1ea" stroke="#ffe3d5" stroke-width="2"/>'
    + '<text x="640" y="56" text-anchor="middle" font-size="14" font-weight="700" fill="#a33608">Bimetal strip</text>'
    + '<text x="520" y="88" font-size="12" fill="#555">Cold: straight</text>'
    + '<rect x="530" y="100" width="220" height="10" fill="#ffa94d"/>'
    + '<rect x="530" y="110" width="220" height="10" fill="#868e96"/>'
    + '<rect x="520" y="94" width="10" height="32" fill="#495057"/>'
    + '<text x="520" y="170" font-size="12" fill="#555">Hot: bends toward the low expansion side</text>'
    + '<path d="M530 200 Q640 205 742 250" fill="none" stroke="#ffa94d" stroke-width="10"/>'
    + '<path d="M530 210 Q636 215 736 259" fill="none" stroke="#868e96" stroke-width="10"/>'
    + '<rect x="520" y="190" width="10" height="32" fill="#495057"/>'
    + '<rect x="530" y="290" width="14" height="14" fill="#ffa94d"/>'
    + '<text x="552" y="302" font-size="12" fill="#333">High expansion metal</text>'
    + '<rect x="530" y="310" width="14" height="14" fill="#868e96"/>'
    + '<text x="552" y="322" font-size="12" fill="#333">Low expansion metal</text>'
)

BODY = [
    takeaways([
        "A bimetal thermometer uses two bonded metals with different thermal expansion coefficients.",
        "The strip is wound into a helical coil in the stem; its rotation turns the pointer shaft.",
        "It is fully mechanical, needs no power and is classed for accuracy under EN 13190.",
        "The sensing coil sits in the lower part of the stem, so correct immersion decides accuracy.",
    ]),
    p("Pumps, heat exchangers, tanks and utility lines all need a local temperature reading that works without power or wiring. The <strong>bimetal thermometer</strong> is the usual answer: a simple dial thermometer that relies on how metals expand with heat.",
      "This guide explains the working principle, the specifications that matter and how to install and check one. SWME supplies " + link("/temperature-gauges", "temperature gauges") + " and " + link("/thermowells", "thermowells") + " for process plants across the GCC."),
    toc([("principle", "Bimetal thermometer working principle"), ("coil", "Helix and spiral coils"), ("specs", "Ranges and accuracy"),
         ("install", "Installation tips"), ("calibrate", "Checking calibration"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("principle", "Bimetal Thermometer Working Principle"),
    p("As " + ext("https://tameson.com/pages/bimetallic-thermometer", "Tameson") + " explains, a bimetallic strip consists of two different metals with different coefficients of thermal expansion, typically steel and copper, or steel and brass. When the temperature changes, one metal expands more than the other, so the bonded strip bends. " + ext("https://www-prod.wika.com/en-us/lp_bimetal_thermometer.WIKA", "WIKA") + " describes how this mechanical deformation is converted into a rotary movement and passed to the pointer through the pointer shaft."),
    INFOGRAPHIC,
    svg(_diag, "Bimetal thermometer with helical coil in the stem and the bending of a bimetal strip", 360),
    h2("coil", "Helix and Spiral Coils"),
    rows([
        ("Helix", "The strip is wound helically inside the stem, with the pointer shaft connected at the free end. This is the form used in most industrial thermometers, often inside a thermowell."),
        ("Spiral", "The strip is coiled flat. It is sensitive to small temperature changes and is used in thermostats and for ambient temperature."),
    ]),
    p("Because the coil turns a shaft directly, the reading can only be shown at the measuring point. WIKA notes that gas actuated thermometers, by contrast, can use remote capillaries up to 60 metres long. For remote signals, see " + link("/how-an-rtd-works", "how an RTD works") + " or our " + link("/temperature-transmitters", "temperature transmitters") + "."),
    h2("specs", "Ranges and Accuracy"),
    table(["Item", "Typical value", "Source"],
          [["Scale ranges", "Minus 70 to 600 °C", "WIKA"],
           ["Accuracy classes", "Class 1 and Class 2 to EN 13190", "WIKA"],
           ["Class 1 / Class 2", "1% / 2% of full scale", "Centro"],
           ["Silicone filled case", "Maximum 250 °C", "WIKA"],
           ["Dial sizes", "2 to 5 in, 3 in most common", "Centro"],
           ["Stem lengths", "2.5 to 12 in", "Centro"]]),
    p("For example, on a 0 to 400 °F dial, " + ext("https://www.centromrosupply.com/resources/centroblog/bimetal-thermometer-guide", "Centro") + " shows Class 1 as plus or minus 4 °F and Class 2 as plus or minus 8 °F. Work out your own tolerance with the " + ext("https://zentacalculator.com/engineering/instrument-accuracy/", "instrument accuracy calculator") + "."),
    dyk("Liquid filling is not only for looks. WIKA explains that a silicone oil fill damps vibration on pumps and compressors, but it limits the maximum temperature to 250 °C."),
    h2("install", "Installation Tips"),
    checklist([
        ("Immerse the coil", "The active element sits in the lower 1.5 to 2 in of the stem; Centro gives a minimum immersion of half the pipe bore plus 1 in."),
        ("Use a thermowell", "A " + link("/what-is-a-thermowell", "thermowell") + " lets you remove the thermometer without shutting the line, at the cost of slightly slower response."),
        ("Pick the mounting", "Back, bottom or every angle connections suit pipe tees, vertical runs and panels."),
        ("Size the range", "Centro suggests a scale of about 1.5 to 2 times the expected process temperature, so readings sit mid scale."),
        ("Mind vibration", "Use a liquid filled case where pipework vibrates."),
    ]),
    p("Thermowell lag is part of the response time; estimate it with the " + ext("https://zentacalculator.com/engineering/sensor-response-time/", "sensor response time calculator") + "."),
    h2("calibrate", "Checking Calibration"),
    p("Tameson describes the ice point method. Fill a glass with ice, add cold water and wait 4 to 5 minutes. Insert the stem without touching the glass and wait for the pointer to settle; it should read 0 °C. If not, many models allow adjustment with the nut under the dial. In addition, rough handling can disturb calibration, so check after any knock. " + ext("https://www.instrumentationblog.in/temperature-gauge-calibration/", "Instrumentation Blog") + " covers temperature gauge calibration in more detail, and the " + ext("https://zentacalculator.com/engineering/calibration-error/", "calibration error calculator") + " helps record the results."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Short insertion.", "If the coil sits in air or near the pipe wall, the dial reads low or high."),
        ("Full scale operation.", "A range too close to the process temperature leaves no margin and wears the movement."),
        ("Dry case on a vibrating pump.", "The pointer flutters and the movement wears quickly."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Does a bimetal thermometer need power?", "No. It is fully mechanical; thermal expansion moves the pointer directly."),
        ("How accurate is a bimetal thermometer?", "EN 13190 Class 1 and Class 2 units are typically within 1% or 2% of full scale."),
        ("Why does the stem need full immersion?", "The bimetal coil sits in the lower part of the stem, so that part must be in the process fluid to read correctly."),
    ]),
]
