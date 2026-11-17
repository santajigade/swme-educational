META = {
    "category": "pressure-measurement-guides",
    "title": "What Is a Pressure Switch and How Does It Work?",
    "keyword": "pressure switch",
    "subtitle": "Sensing elements, contacts, setpoint and deadband explained in plain terms",
    "meta_title": "What Is a Pressure Switch? How It Works Explained",
    "meta_description": "Learn how a pressure switch works: diaphragm, piston and bourdon sensing elements, NO and NC contacts, setpoint, deadband and practical selection tips.",
    "summary": "How a pressure switch senses pressure and changes an electrical contact, with setpoint, deadband and selection tips.",
    "card_title": "What Is a Pressure Switch?",
    "author": "SWME Technical Staff",
    "published": "2026-11-17",
    "status": "published",
    "sort_order": 3,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "steps",
        "title": "How a Pressure Switch Works",
        "alt": "Infographic showing four steps of pressure switch operation: pressure acts, spring opposes, element moves, contact changes",
        "steps": [
            ["Pressure acts", "Process pressure pushes on a diaphragm, piston or bourdon tube."],
            ["Spring opposes", "An adjustable range spring resists the force and sets the trip point."],
            ["Element moves", "When pressure beats the spring force, the element moves a push rod."],
            ["Contact changes", "The rod snaps a microswitch: NO contacts close and NC contacts open."],
        ],
    },
}

_C = "#5f3dc4"
_L = "#ece8fb"

_mech = (
    arrow_defs(_C)
    + '<rect x="120" y="40" width="300" height="250" rx="14" fill="#f8f9fa" stroke="#495057" stroke-width="3"/>'
    # adjusting nut and spring
    + '<rect x="225" y="52" width="90" height="22" rx="4" fill="#868e96"/>'
    + '<text x="440" y="68" font-size="14" font-weight="700" fill="#3b2a8c">Adjusting nut</text>'
    + '<line x1="432" y1="63" x2="320" y2="63" stroke="#495057" stroke-width="1.5"/>'
    + '<polyline points="270,74 245,90 295,106 245,122 295,138 245,154 295,170 270,180" fill="none" stroke="' + _C + '" stroke-width="4"/>'
    + '<text x="100" y="132" text-anchor="end" font-size="14" font-weight="700" fill="#3b2a8c">Range spring</text>'
    + '<line x1="106" y1="127" x2="243" y2="127" stroke="#495057" stroke-width="1.5"/>'
    # plate and diaphragm
    + '<rect x="205" y="180" width="130" height="14" rx="3" fill="#495057"/>'
    + '<path d="M150 214 Q270 196 390 214" fill="none" stroke="' + _C + '" stroke-width="5"/>'
    + '<line x1="270" y1="194" x2="270" y2="206" stroke="#495057" stroke-width="4"/>'
    + '<text x="440" y="214" font-size="14" font-weight="700" fill="#3b2a8c">Diaphragm</text>'
    + '<line x1="432" y1="209" x2="390" y2="212" stroke="#495057" stroke-width="1.5"/>'
    # push rod to microswitch
    + '<line x1="335" y1="187" x2="372" y2="187" stroke="#495057" stroke-width="4"/>'
    + '<line x1="372" y1="187" x2="372" y2="150" stroke="#495057" stroke-width="4"/>'
    + '<rect x="345" y="96" width="60" height="54" rx="6" fill="' + _L + '" stroke="' + _C + '" stroke-width="2"/>'
    + '<text x="375" y="128" text-anchor="middle" font-size="12" font-weight="700" fill="#3b2a8c">Switch</text>'
    + '<text x="440" y="98" font-size="14" font-weight="700" fill="#3b2a8c">Microswitch</text>'
    + '<text x="440" y="116" font-size="13" fill="#555">C, NO and NC terminals</text>'
    + '<line x1="432" y1="94" x2="405" y2="104" stroke="#495057" stroke-width="1.5"/>'
    # process port and pressure arrows
    + '<rect x="245" y="216" width="50" height="74" fill="#dee2e6" stroke="#495057" stroke-width="2"/>'
    + '<rect x="245" y="290" width="50" height="34" fill="#868e96"/>'
    + '<line x1="270" y1="318" x2="270" y2="244" stroke="#e8590c" stroke-width="4"/>'
    + '<polygon points="260,246 280,246 270,228" fill="#e8590c"/>'
    + '<text x="310" y="316" font-size="14" font-weight="700" fill="#e8590c">Process pressure</text>'
    + '<text x="400" y="352" text-anchor="middle" font-size="13" fill="#555">When pressure force exceeds spring force, the plate rises and the rod operates the microswitch</text>'
)

_db = (
    arrow_defs(_C)
    + '<line x1="80" y1="290" x2="760" y2="290" stroke="#495057" stroke-width="2" marker-end="url(#ah)"/>'
    + '<line x1="80" y1="290" x2="80" y2="30" stroke="#495057" stroke-width="2" marker-end="url(#ah)"/>'
    + '<text x="740" y="315" text-anchor="end" font-size="13" fill="#555">Time</text>'
    + '<text x="70" y="40" text-anchor="end" font-size="13" fill="#555">Pressure</text>'
    + '<rect x="82" y="110" width="660" height="60" fill="' + _L + '"/>'
    + '<line x1="82" y1="110" x2="742" y2="110" stroke="' + _C + '" stroke-width="2" stroke-dasharray="7 5"/>'
    + '<line x1="82" y1="170" x2="742" y2="170" stroke="#e8590c" stroke-width="2" stroke-dasharray="7 5"/>'
    + '<text x="600" y="102" font-size="13" font-weight="700" fill="#3b2a8c">Setpoint (rising)</text>'
    + '<text x="600" y="188" font-size="13" font-weight="700" fill="#e8590c">Reset point (falling)</text>'
    + '<text x="560" y="145" font-size="14" font-weight="700" fill="#3b2a8c">Deadband</text>'
    + '<path d="M90 250 C180 240 220 140 280 110 C320 92 360 70 410 75 C460 80 480 140 520 170 C560 196 600 230 700 240" fill="none" stroke="#1971c2" stroke-width="3"/>'
    + '<circle cx="280" cy="110" r="7" fill="' + _C + '"/>'
    + '<circle cx="520" cy="170" r="7" fill="#e8590c"/>'
    + '<text x="270" y="210" text-anchor="middle" font-size="13" fill="#333">Contact trips</text>'
    + '<line x1="280" y1="196" x2="280" y2="120" stroke="#495057" stroke-width="1" stroke-dasharray="3 3"/>'
    + '<text x="520" y="230" text-anchor="middle" font-size="13" fill="#333">Contact resets</text>'
    + '<line x1="520" y1="216" x2="520" y2="180" stroke="#495057" stroke-width="1" stroke-dasharray="3 3"/>'
)

BODY = [
    takeaways([
        "A pressure switch opens or closes an electrical contact when process pressure reaches a set value.",
        "Electromechanical switches use a diaphragm, piston, bellows or bourdon tube against a spring and need no external power.",
        "Deadband is the gap between the trip point and the reset point; it stops the contacts from chattering.",
        "Select by range, setpoint position, overpressure, wetted materials, contact rating and approvals.",
    ]),
    p("Many control and protection functions only need to know when pressure crosses one value. A <strong>pressure switch</strong> does exactly that: it senses pressure and mechanically opens or closes an electrical circuit at a set point. Pressure switches are used with pumps, boilers, burners, compressors and filters wherever a pressure change must trigger an electrical response.",
      "SWME supplies " + link("/pressure-switches", "pressure switches") + " and " + link("/differential-pressure-switches", "differential pressure switches") + " for oil and gas, water and utility projects across the GCC."),
    toc([("how", "How a pressure switch works"), ("contacts", "Contacts and setpoint"), ("deadband", "Deadband explained"),
         ("types", "Mechanical vs solid state"), ("select", "How to select one"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("how", "How a Pressure Switch Works"),
    p("In an electromechanical design, process pressure acts on a sensing element against an opposing range spring. An adjusting nut sets the spring force, which sets the trip point. Only when the pressure force exceeds the spring force does the element move, pushing a rod that changes the state of a snap acting microswitch. According to " + ext("https://blog.ashcroft.com/what-is-a-pressure-switch", "Ashcroft") + ", raising the adjusting nut reduces the spring force and lowers the setpoint, while lowering it raises the setpoint."),
    INFOGRAPHIC,
    svg(_mech, "Simplified cross section of a diaphragm pressure switch", 365),
    h3("Sensing elements"),
    rows([
        ("Diaphragm", "Moves with pressure and passes the force to the switch. Material must suit the medium; Ashcroft lists elastomer diaphragms up to 3000 psi (210 bar) and stainless steel up to 1000 psi (70 bar)."),
        ("Piston", "Used for higher pressure designs, generally 1,000 psi and above. Piston switches handle surges and spikes best."),
        ("Bourdon tube or bellows", "A tube or bellows deflects with pressure and operates the switch; bourdon tube switches typically have narrow deadbands."),
    ]),
    h2("contacts", "Contacts and Setpoint"),
    p("A normally open (NO) contact is open below the setpoint and closes above it. A normally closed (NC) contact is closed below the setpoint and opens above it. For vacuum switches the behaviour is reversed. An SPDT microswitch has one NO, one NC and one common terminal, while a DPDT version uses two SPDT switches that actuate together, so two separate loads switch at the same time.",
      "Where the setpoint sits in the range matters. " + ext("https://library.automationdirect.com/pressure-switch-basics-and-selection-tips-issue-27-2013/", "AutomationDirect") + " advises placing it in the middle of the range for electromechanical switches, to balance accuracy and switch life, and in the upper 25% of the range for solid state switches."),
    h2("deadband", "Deadband Explained"),
    p("Deadband, also called differential or hysteresis, is the difference between the pressure at which the switch trips and the pressure at which it resets. On a rising setpoint the switch resets at a lower pressure; on a falling setpoint it resets at a higher pressure. As " + ext("https://omega.com/en-us/resources/understanding-deadband-for-pressure-switches", "Omega") + " explains, deadband prevents rapid switching that would disturb the process and wear the contacts."),
    svg(_db, "Deadband: the switch trips at the rising setpoint and resets only when pressure falls to the reset point", 330),
    p("As a rule, use a narrow deadband for alarms and a wider one for control duties, such as starting and stopping a pump. Bourdon tube and diaphragm switches typically have narrow deadbands, while piston switches have broad ones."),
    dyk("An electromechanical pressure switch needs no external power. Its sensing element moves the contacts directly, so it can switch loads rated at 3 to 15 amps and 120 to 480 VAC. A solid state switch, by contrast, typically needs a 24 VDC supply."),
    h2("types", "Mechanical vs Solid State Pressure Switch"),
    table(["Feature", "Electromechanical", "Solid state"], [
        ["Sensing", "Diaphragm, bellows, bourdon tube or piston", "Piezoresistive strain gauge"],
        ["Power", "None needed", "External supply, usually 24 VDC"],
        ["Deadband", "Fixed or rises with setpoint", "Adjustable up to 100% of range"],
        ["Cycle life", "Diaphragm over 500k, piston over 1 million", "Over 50 million"],
        ["Best setpoint position", "Middle of range", "Upper 25% of range"],
    ]),
    p("Figures from " + ext("https://library.automationdirect.com/pressure-switch-basics-and-selection-tips-issue-27-2013/", "AutomationDirect pressure switch basics") + ". When the process needs a continuous reading rather than one trip point, a transmitter is the better tool; see " + link("/what-is-a-pressure-transmitter", "what is a pressure transmitter") + " and our " + link("/pressure-transmitters", "pressure transmitters") + "."),
    h2("select", "How to Select a Pressure Switch"),
    checklist([
        ("Pressure type", "Gauge, absolute or differential; see " + link("/gauge-vs-absolute-vs-differential-pressure", "gauge vs absolute vs differential pressure") + "."),
        ("Range and setpoint", "Choose a range that puts the setpoint in the recommended part of the scale."),
        ("Overpressure", "Check proof and burst pressure; Ashcroft states burst pressure is typically at least 400% of range. Add a snubber from our " + link("/gauge-accessories", "gauge accessories") + " where spikes occur."),
        ("Wetted materials", "Match diaphragm, piston and O ring materials to the medium and temperature."),
        ("Electrical", "Contact type (SPDT or DPDT), rating and hazardous area approvals; read " + link("/blog/pressure-measurement-in-hazardous-areas", "pressure measurement in hazardous areas") + "."),
    ]),
    p("For a product example, see our blog on the " + link("/blog/ue-400-series-pressure-and-temperature-switch-uae", "UE 400 Series pressure and temperature switch") + ", and our guide to " + link("/blog/pump-protection-pressure-flow-temperature-instruments", "pump protection instruments") + ". In addition, the " + ext("https://zentacalculator.com/engineering/absolute-gauge-pressure/", "absolute and gauge pressure calculator") + " and the " + ext("https://zentacalculator.com/engineering/water-hammer/", "water hammer calculator") + " help when checking setpoints and surge risk, and " + ext("https://www.instrumentationblog.in/category/process-instrumentation/pressure-measurement/", "Instrumentation Blog") + " has more pressure measurement reading. For wiring switch inputs, see " + ext("https://zentaengineering.com/automation-robotics/plc-hardware-selection/", "PLC hardware selection") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Setpoint at the edge of the range.", "Accuracy and switch life both suffer; follow the recommended position."),
        ("Ignoring deadband.", "Too narrow a deadband on a pump control duty makes the pump start and stop too often."),
        ("Wrong contact logic.", "Confirm NO or NC with a multimeter before wiring an alarm or trip."),
        ("No surge protection.", "Pressure spikes beyond proof pressure can permanently damage the element."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What is the difference between a pressure switch and a pressure transmitter?", "A pressure switch gives an on or off contact at one setpoint, while a transmitter gives a continuous signal across its whole range."),
        ("What is deadband on a pressure switch?", "It is the difference between the trip pressure and the reset pressure, which prevents the contacts from chattering."),
        ("Does a mechanical pressure switch need power?", "No. The sensing element operates the contacts directly; only solid state switches need an external supply."),
    ]),
]
