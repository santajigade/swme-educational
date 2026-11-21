META = {
    "category": "flow-measurement-guides",
    "title": "How a Rotameter Works: Variable Area Flow Measurement",
    "keyword": "rotameter",
    "subtitle": "The tapered tube and float principle, glass and metal tube designs, accuracy, mounting rules and fluid corrections",
    "meta_title": "How a Rotameter Works: Variable Area Flow Meters",
    "meta_description": "How a rotameter works: float and tapered tube principle, glass, plastic and metal tubes, accuracy and turndown, vertical mounting and fluid corrections.",
    "summary": "The float and tapered tube principle behind the rotameter, which tube suits your service, typical accuracy and the mounting rules that matter.",
    "card_title": "How a Rotameter Works",
    "author": "SWME Technical Staff",
    "published": "2026-11-21",
    "status": "published",
    "sort_order": 6,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "steps",
        "title": "How a Rotameter Measures Flow",
        "alt": "Infographic showing how a rotameter float rises in a tapered tube until the forces balance and the flow is read on the scale",
        "steps": [
            ["Flow enters at the bottom", "Fluid moves up through a tube that widens toward the top."],
            ["The float lifts", "Drag and buoyancy push the float up against its weight."],
            ["The gap opens", "As the float rises, the annular area around it gets larger."],
            ["Forces balance", "The float settles where the open area passes the flow, and you read the scale."],
        ],
    },
}

_C = "#1971c2"
_T = "#14508a"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_ticks = "".join(
    f'<line x1="452" y1="{y}" x2="{468 if k % 2 == 0 else 462}" y2="{y}" stroke="#495057" stroke-width="1.5"/>'
    for k, y in enumerate(range(80, 361, 28)))

_diag = (
    '<defs><marker id="ahr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="' + _C + '"/></marker>'
    '<marker id="ahk" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="#c92a2a"/></marker></defs>'
    # tapered tube: narrow bottom, wide top
    + '<polygon points="370,60 450,60 432,380 388,380" fill="#e7f5ff" stroke="#495057" stroke-width="2.5"/>'
    + '<rect x="360" y="44" width="100" height="16" fill="#adb5bd"/>'
    + '<rect x="372" y="380" width="76" height="16" fill="#adb5bd"/>'
    + _ticks
    # float with sharp edge at top
    + '<polygon points="390,198 430,198 418,240 402,240" fill="' + _C + '"/>'
    + '<rect x="388" y="190" width="44" height="8" fill="#14508a"/>'
    # flow arrows in and out
    + '<line x1="410" y1="440" x2="410" y2="402" stroke="' + _C + '" stroke-width="3" marker-end="url(#ahr)"/>'
    + '<line x1="410" y1="40" x2="410" y2="8" stroke="' + _C + '" stroke-width="3" marker-end="url(#ahr)"/>'
    + _t(425, 432, "Flow in", 13, fill="#1864ab")
    + _t(425, 26, "Flow out", 13, fill="#1864ab")
    # force arrows on the float
    + '<line x1="340" y1="250" x2="340" y2="196" stroke="' + _C + '" stroke-width="3" marker-end="url(#ahr)"/>'
    + _t(330, 220, "Drag", 13, anchor="end") + _t(330, 238, "and buoyancy", 12, "400", "#555", "end")
    + '<line x1="480" y1="190" x2="480" y2="244" stroke="#c92a2a" stroke-width="3" marker-end="url(#ahk)"/>'
    + _t(492, 214, "Float weight", 13, fill="#c92a2a") + _t(492, 232, "(gravity)", 12, "400", "#555")
    # labels
    + '<line x1="432" y1="194" x2="560" y2="150" stroke="#adb5bd" stroke-width="1.5"/>'
    + _t(565, 146, "Read at the float edge", 13) + _t(565, 164, "against the tube scale", 12, "400", "#555")
    + '<line x1="446" y1="90" x2="560" y2="80" stroke="#adb5bd" stroke-width="1.5"/>'
    + _t(565, 76, "Wide end at the top", 13) + _t(565, 94, "more annular area, more flow", 12, "400", "#555")
    + '<line x1="434" y1="350" x2="560" y2="340" stroke="#adb5bd" stroke-width="1.5"/>'
    + _t(565, 336, "Narrow end at the bottom", 13) + _t(565, 354, "float rests here at zero flow", 12, "400", "#555")
    + _t(40, 60, "Mount vertically", 14) + _t(40, 80, "flow always upward", 12, "400", "#555")
)

BODY = [
    takeaways([
        "A rotameter is a variable area meter: a float rises in a tapered tube until the upward force of the flow equals its weight.",
        "It needs no external power, gives a direct visual reading on a linear scale and has a low pressure drop.",
        "It must be mounted vertically with the wide end of the taper at the top and the flow going up.",
        "The scale is valid only for the fluid and conditions it was calibrated for, so other fluids need a correction.",
    ]),
    p("A <strong>rotameter</strong> shows flow as the height of a float in a tube. It has a single moving part, glass and plastic versions need no power, and you read it directly. SWME supplies " + link("/rotameters", "rotameters") + " and other " + link("/flowmeters", "flow meters") + " for plants across the UAE and GCC."),
    toc([("principle", "How a rotameter works"), ("tubes", "Glass, plastic and metal tubes"), ("accuracy", "Accuracy and turndown"),
         ("install", "Installation rules"), ("fluid", "Fluid changes and correction"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("principle", "How a Rotameter Works"),
    p("The tube is narrow at the bottom and wide at the top. With no flow the float rests at the bottom. When fluid enters, it lifts the float, and as the float rises the gap around it opens up. " + ext("https://www.dwyeromega.com/en-au/resources/variable-area-flow-meter", "DwyerOmega") + " says the float reaches a stable position when the upward force from the fluid equals the downward pull of the float's weight. With liquids the float is lifted by buoyancy plus the velocity head; with gas, buoyancy is negligible.",
      "Because the open area changes instead of the pressure drop, the drop across the float stays nearly constant. That is where the name variable area comes from."),
    INFOGRAPHIC,
    svg(_diag, "Rotameter: flow enters at the narrow bottom of a tapered tube and lifts the float until drag and buoyancy balance its weight", 450),
    dyk("The name comes from early floats with slots cut in them, which made the float spin to keep it stable and centred in the tube. " + ext("https://www.globalspec.com/learnmore/sensors_transducers_detectors/flow_sensing/rotameters", "GlobalSpec") + " notes that floats now come in many shapes, including spheres."),
    h2("tubes", "Glass, Plastic and Metal Tubes"),
    p("The tube decides where you can use the meter. Figures vary between makers, so treat these GlobalSpec values as typical and check the datasheet."),
    table(["Tube", "Typical limits (GlobalSpec)", "Reading", "Notes"],
          [["Glass", "Up to 300 psig and 250 °F", "Float seen directly against the scale", "Project Materials calls glass fragile and unsuitable for high pressure or hazardous service"],
           ["Plastic (acrylic)", "Up to 100 psig and 150 °F", "Direct", "Practically unbreakable; suits ionised water and corrosive media"],
           ["Metal (armoured, 316 stainless steel)", "Up to 1500 psig and 900 °F", "A magnet in the float drives a pointer", "Can carry high and low flow alarms and a transmitter"]]),
    p("Tube sizes run from 1/16 to 4 inches, and GlobalSpec says 1/8 to 2 inches is the most common. Common float materials include 316 stainless steel, black glass, sapphire, Carboloy and tantalum. A needle valve is the valve most often fitted with a rotameter."),
    h2("accuracy", "Accuracy and Turndown"),
    rows([
        ("Glass tube accuracy", "±1 to 5% of full scale (Project Materials)."),
        ("Metal tube with transmitter", "±1 to 2%."),
        ("Repeatability", "±0.25 to 0.5% of full scale."),
        ("Turndown", "10:1 as standard, up to 12:1."),
    ], "At a glance"),
    p("Because accuracy is stated against full scale, the error is a bigger share of the reading at low flow. The " + ext("https://zentacalculator.com/engineering/instrument-accuracy/", "instrument accuracy calculator") + " and " + ext("https://zentacalculator.com/engineering/turndown-ratio/", "turndown ratio calculator") + " help you check a meter against your range. Project Materials also notes rotameters are less accurate than DP or Coriolis meters; see our " + link("/types-of-flow-meters", "types of flow meters") + " guide."),
    h2("install", "Installation Rules"),
    checklist([
        ("Vertical", "GlobalSpec says rotameters should always be mounted vertically with the widest end of the taper at the top."),
        ("Flow upward", "Fluid enters at the bottom and leaves at the top."),
        ("Spring types excepted", "DwyerOmega notes spring operated variable area meters can be mounted in any position."),
        ("Connections", "In line flanged, threaded (NPT is most common) or clamp, or insertion types."),
    ]),
    h2("fluid", "Fluid Changes and Correction"),
    p("GlobalSpec says the meter must be calibrated for a specific fluid with a known specific gravity, with water at 1.0 as the reference. Changes in pressure or temperature change the reading, and for gas the operating pressure matters because it changes the density. Project Materials gives the example of an air calibrated meter used on nitrogen at elevated pressure, which reads wrong unless correction factors are applied. The " + ext("https://zentacalculator.com/engineering/rotameter-correction/", "rotameter correction calculator") + " works the factor out.",
      "Floats are generally insensitive to viscosity, but GlobalSpec still advises checking it, and recommends calibrating yearly to allow for changes in the system. More background is in the " + ext("https://www.instrumentationblog.in/category/process-instrumentation/flow-measurement/", "Instrumentation Blog flow section") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Mounting the rotameter at an angle.", "The float depends on gravity, so the reading is only valid when the tube is vertical."),
        ("Reading a water scale on another liquid.", "Apply a correction for the new specific gravity."),
        ("Glass on high pressure or hazardous service.", "Use an armoured metal tube instead."),
    ]),
    p("For an alarm without a reading, see " + link("/flow-switches", "flow switches") + ". To see flow without measuring it, a " + link("/sight-flow-indicators", "sight flow indicator") + " may be enough. If the reading looks wrong, our blog on " + link("/blog/flow-meter-incorrect-readings-causes-fixes", "flow meter incorrect readings") + " covers common causes."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Does a rotameter need power?", "Not for a local reading. Glass and plastic meters are read directly, and metal tube meters use a magnet to drive the pointer."),
        ("Can a rotameter be mounted horizontally?", "No. It relies on gravity and must be vertical with flow going up. Only spring operated variable area meters can go in any position."),
        ("Can I use a water rotameter on oil?", "Only with a correction for the different specific gravity, or a meter calibrated for that fluid."),
    ]),
]
