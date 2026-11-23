META = {
    "category": "industrial-valve-guides",
    "title": "Control Valve Basics: Body, Trim and Actuator",
    "keyword": "control valve",
    "subtitle": "How a control valve fits the loop, what the body, trim, actuator and positioner each do, flow characteristics, Cv and Kv, leakage classes and sizing",
    "meta_title": "Control Valve Basics: Body, Trim and Actuator",
    "meta_description": "Control valve basics: sliding stem and rotary bodies, trim and flow characteristics, actuators and fail action, positioners, Cv and Kv, leakage classes.",
    "summary": "What each part of a control valve does, how trim shapes the flow, how actuators fail safe, and the Cv, leakage and sizing figures buyers need.",
    "card_title": "Control Valve Basics",
    "author": "SWME Technical Staff",
    "published": "2026-11-23",
    "status": "published",
    "sort_order": 7,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "steps",
        "title": "How a Control Valve Follows the Controller",
        "alt": "Infographic showing the signal path from controller output through the positioner and actuator to the valve trim",
        "steps": [
            ["Controller output", "The controller sends a 4 to 20 mA signal for the valve position it wants."],
            ["I/P and positioner", "The current becomes a 3 to 15 psi air signal, and the positioner holds the stem where asked."],
            ["Actuator moves the stem", "Air on the diaphragm or piston works against the spring to move the stem."],
            ["Trim varies the flow", "The plug moves against the seat ring and changes the size of the flow passage."],
        ],
    },
}

_C = "#e67700"
_T = "#a35400"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_spring = "M340,78 " + " ".join(f"L{320 if k % 2 == 0 else 360},{80 + 4 * k}" for k in range(7)) + " L340,108"

_diag = (
    '<defs><marker id="ahv" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="' + _C + '"/></marker></defs>'
    # pipes and body
    + '<rect x="100" y="300" width="160" height="50" fill="#fff4e6" stroke="#495057" stroke-width="2"/>'
    + '<rect x="420" y="300" width="170" height="50" fill="#fff4e6" stroke="#495057" stroke-width="2"/>'
    + '<ellipse cx="340" cy="325" rx="100" ry="62" fill="#fff4e6" stroke="#495057" stroke-width="3"/>'
    + '<rect x="96" y="292" width="8" height="66" fill="#adb5bd"/><rect x="586" y="292" width="8" height="66" fill="#adb5bd"/>'
    # internal walls and seat ring
    + '<line x1="300" y1="325" x2="300" y2="268" stroke="#495057" stroke-width="5"/>'
    + '<line x1="380" y1="325" x2="380" y2="382" stroke="#495057" stroke-width="5"/>'
    + '<rect x="298" y="322" width="22" height="8" fill="#495057"/><rect x="360" y="322" width="22" height="8" fill="#495057"/>'
    # bonnet, stem and plug
    + '<rect x="315" y="232" width="50" height="38" fill="#ced4da" stroke="#495057" stroke-width="2"/>'
    + '<line x1="340" y1="114" x2="340" y2="292" stroke="#495057" stroke-width="5"/>'
    + '<path d="M322,288 L358,288 L356,306 L340,322 L324,306 Z" fill="' + _C + '" stroke="#a35400" stroke-width="1.5"/>'
    # yoke and actuator
    + '<line x1="300" y1="150" x2="322" y2="232" stroke="#868e96" stroke-width="5"/>'
    + '<line x1="380" y1="150" x2="358" y2="232" stroke="#868e96" stroke-width="5"/>'
    + '<rect x="250" y="70" width="180" height="80" rx="28" fill="#fff" stroke="#495057" stroke-width="3"/>'
    + '<line x1="252" y1="112" x2="428" y2="112" stroke="#495057" stroke-width="3"/>'
    + '<rect x="300" y="108" width="80" height="8" fill="#868e96"/>'
    + '<path d="' + _spring + '" fill="none" stroke="#a35400" stroke-width="2.5"/>'
    # positioner, air tube and feedback
    + '<rect x="470" y="140" width="100" height="55" rx="8" fill="#ffe8cc" stroke="' + _C + '" stroke-width="2"/>'
    + _t(520, 163, "Positioner", 13, "700", _T, "middle")
    + _t(520, 180, "with I/P", 12, "400", "#555", "middle")
    + '<polyline points="515,140 515,132 430,132" fill="none" stroke="' + _C + '" stroke-width="2.5"/>'
    + _t(472, 124, "3 to 15 psi", 12, "700", _T, "middle")
    + '<line x1="470" y1="188" x2="344" y2="188" stroke="#868e96" stroke-width="2" stroke-dasharray="4 3"/>'
    + _t(424, 181, "travel feedback", 11, "400", "#555", "middle")
    + '<line x1="690" y1="167" x2="575" y2="167" stroke="' + _C + '" stroke-width="2.5" marker-end="url(#ahv)"/>'
    + _t(635, 155, "4 to 20 mA", 12, "700", _T, "middle")
    + _t(635, 186, "from controller", 12, "400", "#555", "middle")
    + '<line x1="545" y1="245" x2="545" y2="199" stroke="' + _C + '" stroke-width="2.5" marker-end="url(#ahv)"/>'
    + _t(555, 240, "Air supply,", 12, "700", _T)
    + _t(555, 256, "20 psig typical", 12, "400", "#555")
    # left labels
    + _t(240, 96, "Spring and diaphragm", 13, "700", "#495057", "end")
    + _t(240, 112, "actuator", 13, "700", "#495057", "end")
    + _t(240, 130, "air to open, fails closed", 12, "400", "#555", "end")
    + _t(296, 196, "Yoke and stem", 13, "700", "#495057", "end")
    + _t(306, 250, "Bonnet", 13, "700", "#495057", "end")
    # flow
    + '<line x1="112" y1="325" x2="232" y2="325" stroke="' + _C + '" stroke-width="3" marker-end="url(#ahv)"/>'
    + _t(112, 288, "Flow in", 13, "700", _T)
    + '<line x1="450" y1="314" x2="575" y2="314" stroke="' + _C + '" stroke-width="3" marker-end="url(#ahv)"/>'
    + _t(470, 288, "Flow out", 13, "700", _T)
    # bottom labels
    + '<line x1="470" y1="394" x2="372" y2="330" stroke="#adb5bd" stroke-width="1.5"/>'
    + _t(476, 408, "Trim: plug and seat ring", 13, "700", "#495057")
    + '<line x1="210" y1="394" x2="262" y2="362" stroke="#adb5bd" stroke-width="1.5"/>'
    + _t(210, 408, "Globe body", 13, "700", "#495057", "middle")
)

BODY = [
    takeaways([
        "A control valve is the most common final control element: it changes the size of the flow passage as the controller asks.",
        "The body holds the pressure, the trim (plug, seat ring, cage and stem) shapes the flow, and the actuator supplies the force.",
        "An air to open valve fails closed on loss of air, and an air to close valve fails open.",
        "Emerson advises sizing for about 60 to 80% open at maximum flow and not less than 20% open at minimum flow.",
    ]),
    p("Emerson's " + ext("https://d1-auth.emerson.com/documents/automation/control-valve-handbook-en-3661206.pdf", "Fisher control valve handbook") + " calls the <strong>control valve</strong> the most common final control element in the process industries, and defines it as a device that modulates flow by varying the size of the flow passage as directed by a signal from a controller. SWME supplies " + link("/pneumatic-control-valves", "pneumatic control valves") + " and " + link("/automatic-control-valves", "automatic control valves") + " for plants across the UAE and GCC."),
    toc([("loop", "Control valve in the loop"), ("body", "Body styles"), ("trim", "Trim and flow characteristics"),
         ("actuator", "Actuators and fail action"), ("cv", "Cv and Kv"), ("leakage", "Seat leakage classes"),
         ("sizing", "Sizing"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("loop", "How a Control Valve Works in the Loop"),
    p("The controller output is usually 4 to 20 mA, while most actuators run on air. An I/P converter turns the current into air pressure; ABB lists 0/4 to 20 mA in and 0.2 to 1 bar or 3 to 15 psi out. Emerson gives 20 psig as a common supply pressure for a 3 to 15 psig range. A positioner is a position controller mechanically linked to the valve stem, which Emerson describes as a high proportional gain device. Its job is to make sure the stem goes where the signal asks."),
    INFOGRAPHIC,
    svg(_diag, "Control valve assembly: a positioner drives a spring and diaphragm actuator, and the stem moves the plug against the seat ring in a globe body", 420),
    h2("body", "Body Styles"),
    p("Emerson divides bodies into two groups. Sliding stem valves use linear motion to move a closure member into and out of a seating surface, and the globe valve is the usual example. Rotary valves turn the closure member instead: full or segmented ball, butterfly disc and eccentric plug designs. Emerson notes segmented ball bodies give rangeability in excess of 300:1. For background on each body, see our guides to the " + link("/gate-valve-vs-globe-valve", "gate valve vs globe valve") + " and " + link("/butterfly-valve-types-explained", "butterfly valve types") + "."),
    h2("trim", "Trim and Flow Characteristics"),
    rows([
        ("Trim", "The internal parts that modulate the flow (Emerson)."),
        ("Plug", "The closure member in a sliding stem valve."),
        ("Seat ring", "Gives the closure member its seating surface."),
        ("Cage", "Surrounds the closure member and can characterise the flow or provide the seat."),
        ("Stem", "Connects the actuator stem to the closure member."),
    ], "Trim parts"),
    p("The flow characteristic is the relationship between flow and percent of rated travel from 0 to 100%. The " + ext("https://www.spiraxsarco.com/learn-about-steam/control-hardware-electric-pneumatic-actuation/control-valve-characteristics", "control valve characteristics guide") + " describes the three common shapes, all at constant differential pressure:"),
    table(["Characteristic", "How flow follows lift", "Note"],
          [["Linear", "Flow is directly proportional to lift", "Defined at constant differential pressure (Spirax Sarco)"],
           ["Equal percentage", "Each step in lift adds a set percentage of the previous flow", "Emerson gives about 30:1 turndown unless the valve is oversized"],
           ["Quick opening", "A large change in flow for a small lift", "Engineering ToolBox limits it to on and off service such as batch operation"]]),
    h2("actuator", "Actuators and Fail Action"),
    p("Emerson defines an actuator as a pneumatic, hydraulic or electric device that supplies force and motion to open or close a valve. The " + ext("https://control.com/textbook/control-valves/control-valve-actuators/", "guide to control valve actuators") + " explains the main types:"),
    twocol([
        ("Pneumatic", "bi-wind", [
            "Diaphragm actuators use a large coil spring for the default position",
            "Piston actuators generally have longer strokes than diaphragm types",
            "Double acting actuators tend to stay in position on air failure",
        ]),
        ("Electric and hydraulic", "bi-lightning-charge", [
            "Most electric actuators use a worm gear to cut motor speed",
            "Electric valves usually stay in their last position on power loss",
            "Nearly all hydraulic designs use a piston, some with their own pump",
        ]),
    ]),
    p("The " + ext("https://control.com/textbook/control-valves/valve-failure-mode/", "valve failure mode lesson") + " sums up fail action: an air to open valve fails closed on loss of air pressure, and an air to close valve fails open."),
    dyk("In a control valve the positioner, not the actuator spring alone, decides where the stem stops. Emerson describes it as a servomechanism: it compares the signal with the actual travel and adjusts the air until they match."),
    h2("cv", "Cv and Kv"),
    p("Cv is the number of US gallons per minute of 60 °F water that flows through a valve with a 1 psi pressure drop. Kv is the flow in m³/h of water at 5 to 30 °C with a 1 bar drop. Project Materials gives Cv = 1.156 × Kv and Kv = 0.865 × Cv, and Spirax Sarco gives the more exact factor 1.156 099. The " + ext("https://zentacalculator.com/engineering/control-valve-kv-cv/", "control valve Kv and Cv calculator") + " converts between them and works out the coefficient your duty needs, and the " + ext("https://zentacalculator.com/engineering/valve-authority/", "valve authority calculator") + " checks whether the valve has enough of the system pressure drop to control well."),
    h2("leakage", "Seat Leakage Classes"),
    table(["ANSI/FCI 70 2 class", "Allowed leakage (Emerson handbook)"],
          [["Class I", "No test, if user and supplier agree"], ["Class II", "0.5% of rated capacity"],
           ["Class III", "0.1% of rated capacity"], ["Class IV", "0.01% of rated capacity"],
           ["Class V", "0.0005 ml per minute of water per inch of orifice diameter per psi differential"],
           ["Class VI", "Air or nitrogen at 3.5 bar: 0.15 ml/min (1 bubble a minute) for a 1 inch port"]]),
    h2("sizing", "Sizing a Control Valve"),
    checklist([
        ("Size for the right travel", "Emerson's " + ext("https://d1-live.emerson.com/documents/automation/article-properly-size-control-valves-fisher-en-38152.pdf", "valve sizing article") + " says a valve controls best at about 60 to 80% open at maximum flow and not less than 20% open at minimum flow."),
        ("Avoid oversizing", "The same article says an oversized equal percentage valve throttling at the low end can fall to a turndown of 3:1 or less."),
        ("Allow enough pressure drop", "A rule of thumb from The Chemical Engineer is 20% of the total system drop or 10 psi (0.7 bar), whichever is greater."),
        ("Check for cavitation and flashing", "Emerson says choked flow is cavitation if outlet pressure is above the vapour pressure, and flashing if it is below."),
        ("Pick the leakage class", "Match the class to how tightly the valve must shut off."),
    ]),
    p("Our blog on " + link("/blog/how-to-select-the-right-industrial-valve", "how to select the right industrial valve") + " covers material and connection choices, and our full range of " + link("/industrial-valves", "industrial valves") + " includes " + link("/globe-valves", "globe valves") + " and " + link("/ball-valves", "ball valves") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Oversizing the control valve.", "It throttles near its seat and loses turndown."),
        ("Picking the fail position by habit.", "Decide what the process needs on loss of air, then choose air to open or air to close."),
        ("Using quick opening trim for throttling.", "It suits on and off service."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What is the difference between Cv and Kv?", "Cv uses US gpm at 1 psi drop; Kv uses m³/h at 1 bar. Cv = 1.156 × Kv."),
        ("What does air to open mean?", "Air pressure opens the valve and the spring closes it, so it fails closed when air is lost."),
        ("What does a valve positioner do?", "It is a position controller linked to the stem. Emerson calls it a high gain device that keeps the stem where the signal asks."),
    ]),
]
