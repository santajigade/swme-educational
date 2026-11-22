META = {
    "category": "temperature-measurement-guides",
    "title": "Gas Filled vs Bimetal Thermometers: Which to Choose",
    "keyword": "gas filled vs bimetal thermometer",
    "subtitle": "How gas actuated and bimetal dial thermometers work, how they compare on range, response, remote mounting and cost, and how to choose",
    "meta_title": "Gas Filled vs Bimetal Thermometers Compared",
    "meta_description": "Gas filled vs bimetal thermometer: working principle, ranges, accuracy class, response time, capillary remote mounting, immersion and selection tips.",
    "summary": "How gas filled and bimetal dial thermometers work and how they compare on range, response time, remote mounting, vibration and cost.",
    "card_title": "Gas Filled vs Bimetal Thermometers",
    "author": "SWME Technical Staff",
    "published": "2026-11-22",
    "status": "published",
    "sort_order": 7,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "compare",
        "title": "Gas Filled vs Bimetal Thermometer",
        "alt": "Infographic comparing gas filled and bimetal dial thermometers on principle, range, response and mounting",
        "columns": [
            ["Bimetal", ["Helical bimetal coil turns the pointer", "WIKA range minus 70 to 600 °C", "About 90 s to settle in WIKA's test", "Direct mounting on the process"]],
            ["Gas filled", ["Inert gas pressure moves a Bourdon tube", "WIKA range minus 200 to 700 °C", "About 30 s to settle in WIKA's test", "Remote mounting with a capillary"]],
        ],
    },
}

_C = "#d9480f"
_T = "#a33608"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


def _coil(x, y0, y1):
    pts = []
    y = y0
    k = 0
    while y < y1:
        pts.append(f"{x + (10 if k % 2 else -10)},{y}")
        y += 8
        k += 1
    return '<polyline points="' + " ".join(pts) + '" fill="none" stroke="' + _C + '" stroke-width="2.5"/>'


_diag = (
    # ---------- bimetal (left)
    _t(170, 28, "Bimetal thermometer", 15, "700", _T, "middle")
    + '<circle cx="170" cy="100" r="55" fill="#fff" stroke="#495057" stroke-width="3"/>'
    + '<line x1="170" y1="100" x2="205" y2="70" stroke="#c92a2a" stroke-width="3"/>'
    + '<circle cx="170" cy="100" r="4" fill="#343a40"/>'
    + '<rect x="160" y="155" width="20" height="235" fill="#f1f3f5" stroke="#495057" stroke-width="2"/>'
    + '<line x1="170" y1="104" x2="170" y2="300" stroke="#868e96" stroke-width="2"/>'
    + _coil(170, 300, 384)
    + '<rect x="100" y="290" width="140" height="105" fill="#ffe3d5" opacity="0.45"/>'
    + _t(250, 315, "Helical bimetal coil", 13, "700", _T)
    + _t(250, 333, "near the stem tip", 12, "400", "#555")
    + _t(250, 351, "twists as it heats", 12, "400", "#555")
    + _t(250, 205, "Shaft turns", 13, "700", "#343a40")
    + _t(250, 223, "the pointer", 12, "400", "#555")
    + '<line x1="246" y1="210" x2="174" y2="210" stroke="#495057" stroke-width="1.5"/>'
    + _t(110, 412, "Process", 12, "700", "#495057", "middle")
    # divider
    + '<line x1="400" y1="20" x2="400" y2="420" stroke="#dee2e6" stroke-width="2"/>'
    # ---------- gas filled (right)
    + _t(600, 28, "Gas filled thermometer", 15, "700", _T, "middle")
    + '<circle cx="640" cy="110" r="65" fill="#fff" stroke="#495057" stroke-width="3"/>'
    + '<path d="M640,150 A40,40 0 1,1 680,110" fill="none" stroke="#495057" stroke-width="5"/>'
    + '<line x1="640" y1="110" x2="608" y2="78" stroke="#c92a2a" stroke-width="3"/>'
    + '<circle cx="640" cy="110" r="4" fill="#343a40"/>'
    + '<line x1="536" y1="62" x2="610" y2="82" stroke="#495057" stroke-width="1.5"/>'
    + '<path d="M664,135 l6,-6 l6,6 l6,-6 l6,6" fill="none" stroke="#f08c00" stroke-width="2.5"/>'
    + '<line x1="688" y1="140" x2="760" y2="236" stroke="#495057" stroke-width="1.5"/>'
    + _t(530, 60, "Bourdon tube", 13, "700", "#343a40", "end")
    + _t(530, 78, "uncoils as", 12, "400", "#555", "end")
    + _t(530, 96, "pressure rises", 12, "400", "#555", "end")
    + _t(785, 250, "Bimetal element", 12, "700", "#343a40", "end")
    + _t(785, 266, "corrects for case", 12, "400", "#555", "end")
    + _t(785, 282, "temperature", 12, "400", "#555", "end")
    # capillary
    + '<path d="M640,175 C640,260 470,230 470,300 L470,318" fill="none" stroke="#495057" stroke-width="3"/>'
    + _t(425, 215, "Capillary, sealed", 13, "700", "#343a40")
    + _t(425, 233, "and gas filled", 12, "400", "#555")
    # bulb
    + '<rect x="452" y="318" width="36" height="78" rx="14" fill="' + _C + '"/>'
    + _t(500, 350, "Bulb in the process", 13, "700", _T)
    + _t(500, 368, "inert gas pressure", 12, "400", "#555")
    + _t(500, 386, "rises with temperature", 12, "400", "#555")
)


BODY = [
    takeaways([
        "A bimetal thermometer uses a helical coil of two bonded metals that twists as it heats and turns the pointer.",
        "A gas filled thermometer uses the pressure of an inert gas in a sealed bulb, capillary and Bourdon tube.",
        "Only gas filled types can be mounted remotely with a capillary; WIKA lists capillaries up to 60 m.",
        "In WIKA's test the gas filled type settled in about 30 s and the bimetal in about 90 s.",
    ]),
    p("Choosing between a <strong>gas filled vs bimetal thermometer</strong> comes down to range, response, mounting and price. Both are mechanical dial thermometers and need no power. SWME supplies both types in its range of " + link("/temperature-gauges", "temperature gauges") + ", together with matching " + link("/thermowells", "thermowells") + "."),
    toc([("how", "How each type works"), ("compare", "Gas filled vs bimetal thermometer compared"), ("remote", "Remote mounting and ambient effects"),
         ("immersion", "Immersion and vibration"), ("select", "How to choose"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("how", "How Each Type Works"),
    p("WIKA describes the bimetal gauge as having a measuring system in the form of a helical or spiral tube. Two metals bonded together expand at different rates, so the coil twists as the temperature changes and turns the pointer shaft. Our guide to the " + link("/bimetal-thermometer-working-principle", "bimetal thermometer working principle") + " explains the coil in more detail.",
      "In a gas filled thermometer, Ashcroft explains that the entire system, including the bulb, head assembly and capillary, is filled with an inert gas. WIKA names helium or another inert gas. A temperature rise raises the gas pressure, which moves a Bourdon tube and the pointer. WIKA adds a bimetal element in the case to compensate for ambient temperature."),
    INFOGRAPHIC,
    svg(_diag, "Bimetal thermometer with a helical coil in the stem, and gas filled thermometer with a bulb, capillary and Bourdon tube", 430),
    h2("compare", "Gas Filled vs Bimetal Thermometer Compared"),
    table(["Feature", "Bimetal", "Gas filled"],
          [["Range (WIKA)", "Minus 70 to 600 °C", "Minus 200 to 700 °C"],
           ["Accuracy class (EN 13190, WIKA)", "Class 1 and 2", "Class 1"],
           ["Response, 10 to 90 °C step (WIKA)", "About 90 s", "About 30 s"],
           ["Remote mounting", "No, direct mount only (Ashcroft)", "Yes, capillary up to 60 m bare (WIKA Model 73)"],
           ["Ambient effect", "WIKA: no influence on the result", "Compensated; class 1 held at 23 °C ± 10 °C ambient"],
           ["Typical cost (Ashcroft)", "About $20 to $200", "About $250 to $1,500 or more"]]),
    p("The " + ext("https://www.wika.com/en-us/lp_temperature_gauge.WIKA", "WIKA temperature gauge overview") + " lists the ranges and accuracy classes, and Ashcroft's " + ext("https://blog.ashcroft.com/gas-actuated-vs-bi-metal-thermometers", "gas actuated vs bimetal comparison") + " gives the cost and mounting points. Ashcroft also calls the gas design movementless and resistant to shock and vibration, with no head or elevation error."),
    dyk("WIKA measured the response of both types to a step from 10 °C to 90 °C. The gas filled thermometer settled after about 30 seconds and the bimetal after 90 seconds. A thermowell slows both, depending on its material and wall thickness."),
    p("To estimate how fast a sensor follows a change in your own process, try the " + ext("https://zentacalculator.com/engineering/sensor-response-time/", "sensor response time calculator") + ". WIKA's note on " + ext("https://blog.wika.com/knowhow/selection-criteria-for-mechanical-thermometers-response-time-2/", "response time of mechanical thermometers") + " gives the test details."),
    h2("remote", "Remote Mounting and Ambient Effects"),
    p("WIKA states that only gas actuated thermometers can be combined with a capillary. Its capillary is 2 mm outside diameter with a 0.1 to 0.2 mm bore, and accuracy class 1 is guaranteed up to 60 m. On the Model 73, the maximum is 60 m bare, 40 m with a spiral sleeve and 20 m with a sleeve and PVC coating. The fill pressure ranges from 25 bar for large spans to 180 bar for small spans, as set out in WIKA's " + ext("https://blog.wika.com/en/knowhow/selection-criteria-for-dial-thermometers-3-capillary/", "capillary selection notes") + ".",
      "For a bimetal thermometer, WIKA says ambient temperature has no influence on the result. For gas filled types it guarantees class 1 at an ambient of 23 °C ± 10 °C."),
    h2("immersion", "Immersion and Vibration"),
    rows([
        ("Bimetal immersion", "Reotemp says the sensing area is the last 2 to 4 inches of the stem, with a minimum immersion of 2 in. in liquid and 4 in. in gas."),
        ("Gas filled immersion", "WIKA recommends a stem of at least 8 mm and an active gas sensor length of at least 100 mm."),
        ("Vibration, bimetal", "Ashcroft recommends liquid fill; WIKA says silicone fill limits the process temperature to 250 °C."),
        ("Vibration, gas filled", "WIKA says liquid dampening on the Model 73 allows use under high vibration."),
    ]),
    h2("select", "How to Choose"),
    twocol([
        ("Choose bimetal when", "bi-thermometer-half", [
            "The dial can be read at the measuring point",
            "Range sits within minus 70 to 600 °C",
            "Cost matters and a slower response is acceptable",
            "An every angle dial helps reading on site"]),
        ("Choose gas filled when", "bi-thermometer-high", [
            "The dial must be mounted away from the point",
            "You need down to minus 200 °C or up to 700 °C",
            "A faster response is needed",
            "Strong shock or vibration is expected"]),
    ]),
    p("Fit both types in a thermowell where the process allows; Ashcroft recommends one for protection and easy removal. Our guide to " + link("/what-is-a-thermowell", "what a thermowell is") + " covers sizing, and these " + ext("https://www.instrumentationblog.in/temperature-gauge-calibration/", "temperature gauge calibration steps") + " help when you check either type against a reference. If you need a contact output as well as a dial, see " + link("/temperature-switches-explained", "temperature switches explained") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Too little immersion.", "A bimetal coil sits in the last few inches of the stem, so a short insertion reads low."),
        ("Ignoring the capillary limit.", "WIKA allows 60 m of bare capillary on the Model 73 but only 20 m with a sleeve and PVC coating."),
        ("Liquid filled bimetal on a hot line.", "WIKA limits a silicone filled bimetal to 250 °C process temperature."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Is a gas filled thermometer more accurate than a bimetal?", "WIKA offers gas filled in class 1 and bimetal in class 1 or 2 to EN 13190, so check the class on the datasheet."),
        ("Can a bimetal thermometer be mounted remotely?", "No. Only gas filled types can be combined with a capillary."),
        ("Which type reacts faster?", "In WIKA's test the gas filled type settled in about 30 seconds and the bimetal in about 90."),
    ]),
]
