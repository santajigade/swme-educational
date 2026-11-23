META = {
    "category": "level-measurement-guides",
    "title": "Point Level vs Continuous Level Measurement",
    "keyword": "point level vs continuous level",
    "subtitle": "What a level switch and a level transmitter each tell you, which technologies do each job, and why overfill protection keeps them separate",
    "meta_title": "Point Level vs Continuous Level Measurement",
    "meta_description": "Point level vs continuous level measurement: switches and transmitters compared, technologies for each, API 2350 overfill rules and when to install both.",
    "summary": "The difference between point level switches and continuous level transmitters, the technologies behind each, and why safety duties often need both.",
    "card_title": "Point Level vs Continuous Level",
    "author": "SWME Technical Staff",
    "published": "2026-11-23",
    "status": "published",
    "sort_order": 8,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "grid",
        "title": "Point Level vs Continuous Level",
        "alt": "Infographic comparing point level switches and continuous level transmitters by output and typical use",
        "steps": [
            ["Point level switch", "Detects material at one set height and sends an on or off signal."],
            ["Continuous transmitter", "Measures the level across a span, often as 4 to 20 mA with HART."],
            ["Typical point uses", "High and low alarms, pump control and overfill protection."],
            ["Typical continuous uses", "Process control, inventory and volume."],
        ],
    },
}

_C = "#0c8599"
_T = "#0a5f6d"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


def _fork(y):
    return (f'<rect x="214" y="{y - 12}" width="44" height="24" rx="4" fill="#495057"/>'
            f'<line x1="262" y1="{y - 5}" x2="300" y2="{y - 5}" stroke="#868e96" stroke-width="4" stroke-linecap="round"/>'
            f'<line x1="262" y1="{y + 5}" x2="300" y2="{y + 5}" stroke="#868e96" stroke-width="4" stroke-linecap="round"/>')


_diag = (
    '<defs><marker id="ahl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
    '<path d="M0,0 L10,5 L0,10 z" fill="' + _C + '"/></marker></defs>'
    # tank and liquid
    + '<rect x="262" y="202" width="236" height="156" fill="#d3f0f4"/>'
    + '<rect x="260" y="70" width="240" height="290" fill="none" stroke="#495057" stroke-width="4"/>'
    + '<line x1="262" y1="200" x2="498" y2="200" stroke="' + _C + '" stroke-width="2" stroke-dasharray="6 4"/>'
    # radar transmitter on the roof
    + '<rect x="356" y="20" width="48" height="30" rx="5" fill="' + _C + '"/>'
    + '<polygon points="368,50 392,50 400,72 360,72" fill="#868e96"/>'
    + '<line x1="380" y1="78" x2="380" y2="194" stroke="' + _C + '" stroke-width="2" stroke-dasharray="5 4" marker-start="url(#ahl)" marker-end="url(#ahl)"/>'
    + '<line x1="406" y1="34" x2="520" y2="34" stroke="#adb5bd" stroke-width="1.5"/>'
    + _t(526, 30, "Continuous: radar transmitter", 13, "700", _T)
    + _t(526, 47, "measures the whole span", 12, "400", "#555")
    + _t(526, 63, "output 4 to 20 mA with HART", 12, "400", "#555")
    # point switches
    + _fork(100) + _fork(320)
    + _t(205, 96, "High high switch", 13, "700", "#c92a2a", "end")
    + _t(205, 112, "independent overfill alarm", 12, "400", "#555", "end")
    + _t(205, 128, "on or off signal", 12, "400", "#555", "end")
    + _t(205, 316, "Low level switch", 13, "700", "#c92a2a", "end")
    + _t(205, 332, "pump dry run protection", 12, "400", "#555", "end")
    + _t(205, 348, "on or off signal", 12, "400", "#555", "end")
    # live level bar
    + '<rect x="536" y="100" width="22" height="258" rx="4" fill="#fff" stroke="#495057" stroke-width="1.5"/>'
    + '<rect x="538" y="200" width="18" height="156" fill="' + _C + '"/>'
    + _t(566, 106, "100%", 12, "400", "#555")
    + _t(566, 360, "0%", 12, "400", "#555")
    + _t(566, 198, "Live level", 13, "700", _T)
    + _t(566, 214, "anywhere in the span", 12, "400", "#555")
    + _t(380, 225, "Liquid", 13, "700", _T, "middle")
    + _t(400, 392, "A switch reports one height; a transmitter reports any height in its range", 12, "400", "#555", "middle")
)

BODY = [
    takeaways([
        "A point level switch tells you whether material is at one set height and gives an on or off signal.",
        "A continuous level transmitter tracks the level across a span and usually outputs 4 to 20 mA, often with HART.",
        "Emerson notes that one continuous sensor can replace two, and sometimes four, separate point level sensors.",
        "API 2350 Category 3 tanks need an independent overfill prevention system as well as an automatic tank gauge, which is why both often sit on one tank.",
    ]),
    p("The choice of <strong>point level vs continuous level</strong> measurement starts with the data you need, as ISA puts it. An alarm at one height needs a switch, while a reading you can trend, control on or turn into volume needs a transmitter. SWME supplies " + link("/level-switches", "level switches") + " and " + link("/level-transmitters", "level transmitters") + " for tanks and silos across the UAE and GCC."),
    toc([("difference", "The difference"), ("point", "Point level technologies"), ("continuous", "Continuous level technologies"),
         ("limits", "Limits of each"), ("overfill", "Overfill protection and safety"), ("select", "Selection checklist"),
         ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("difference", "Point Level vs Continuous Level: The Difference"),
    p("Emerson describes a point level device as one that works like a switch: it detects whether material is present at a specific level and sends an on or off signal. Endress+Hauser describes continuous measurement as a real time reading of the exact level, used for process control, inventory and volume, and sent as a standard signal such as 4 to 20 mA or HART. The " + ext("https://www.us.endress.com/level", "Endress+Hauser level overview") + " sets the two side by side.",
      "Gems puts it in terms of the vessel: a continuous sensor indicates the level within a span, while a point sensor only indicates whether the fluid is above or below one point. Its " + ext("https://www.gemssensors.com/blog/blog-details/difference-between-level-sensors", "guide to the difference between level sensors") + " includes product examples."),
    INFOGRAPHIC,
    svg(_diag, "Point level vs continuous level on one tank: a radar transmitter reads the whole span while separate fork switches give high high and low alarms", 405),
    h2("point", "Point Level Technologies"),
    p("Emerson lists vibrating forks, paddles, vibrating rods and capacitance switches, and DirectIndustry adds float, conductive and electro optical switches. Rotary paddles are widely used in silos for grain, sugar, cocoa and animal feed. Emerson also calls point devices simple and comparatively cheap. Our guide to " + link("/level-switch-types", "level switch types") + " explains how each one works, and the " + ext("https://www.emerson.com/en-us/automation/measurement-instrumentation/level/point-level-detection", "point level detection range") + " shows Emerson's switches."),
    h2("continuous", "Continuous Level Technologies"),
    p("Water Online lists radar, ultrasonic, magnetostrictive, capacitive, float and tape, and differential pressure for continuous measurement. Guided wave radar sends microwave pulses along a probe and can measure interfaces too. As an example of a laser device, ABB rates its LLT100 at 0.5 to 30 m for liquids and 0.5 to 100 m for solids, with a typical accuracy of ±11 mm and a NAMUR compliant 4 to 20 mA output with HART 7."),
    p("Our guides to " + link("/guided-wave-radar-level-measurement", "guided wave radar level measurement") + " and " + link("/radar-vs-ultrasonic-level-measurement", "radar vs ultrasonic level measurement") + " go deeper. To turn the reading into stock, the " + ext("https://zentacalculator.com/engineering/vertical-tank-volume/", "vertical tank volume calculator") + " gives the volume at a measured level, and the " + ext("https://zentacalculator.com/engineering/4-20ma-scaling/", "4 to 20 mA scaling calculator") + " gives the current that matches a given height."),
    h2("limits", "Limits of Each"),
    twocol([
        ("Point level", "bi-toggle-on", [
            "One device for each alarm point",
            "Mechanical parts can collect build up",
            "Conductive switches only work on conductive liquids",
            "Floats are sensitive to surface waves; paddles suit solids only",
        ]),
        ("Continuous level", "bi-graph-up", [
            "Usually more expensive and complex than a basic float switch",
            "Obstructions can disturb radar and ultrasonic readings",
            "Turbulence, foam, vapour or dust can give false ultrasonic readings",
            "Hydrostatic readings depend on liquid density",
        ]),
    ]),
    p("Water Online adds that newer radar and ultrasonic models have come down in price. ISA also reminds readers that level instruments do not measure volume, so a volume figure always depends on the tank dimensions."),
    h2("overfill", "Overfill Protection and Safety"),
    p("Emerson's " + ext("https://emerson.com/documents/automation/article-api-2350-reducing-risk-of-overfills-en-8330454.pdf", "summary of API 2350") + " says the fifth edition covers storage tanks in petroleum facilities over 5,000 litres (1,320 gallons). A Category 3 tank needs at least one independent overfill prevention system and one automatic tank gauge. The high high alarm is the only alarm API 2350 requires, the safety margin between levels of concern must be no less than 75 mm (3 in), and the system is proof tested at least annually.",
      "Independent point level sensors can serve as that high high alarm, and the " + ext("https://emerson.com/documents/automation/white-paper-selecting-right-overfill-prevention-technology-en-8746986.pdf", "overfill prevention technology white paper") + " says the overfill system must stay separate from the basic process control system. It cites overfills in 1 out of 3300 fillings and says the sensor should be certified to IEC 61508."),
    dyk("Pepperl+Fuchs makes the case for two technologies on one tank: if a single probe fails, the operator loses both the continuous reading and the limit alarm. Its article on " + ext("https://blog.pepperl-fuchs.com/en/2024/reliable-level-measurement-why-two-different-technologies-are-crucial/", "why two level technologies matter") + " gives the reasoning, and VEGA describes vibrating switches with SIL2/3 certification used alongside guided radar on steam boilers."),
    p("Transmitters that follow NAMUR NE 107 also report their own health through four status signals: Failure, Check Function, Out of Specification and Maintenance Required. The " + ext("https://www.us.endress.com/en/support-overview/learning-center/namur-ne-107", "NAMUR NE 107 explainer") + " shows how each one appears."),
    h2("select", "Selection Checklist"),
    checklist([
        ("Define the data", "Control Engineering says a discrete device will do if you only need a high or low alarm."),
        ("Separate safety from control", "Keep the overfill alarm independent of the gauge used for control."),
        ("Check the product", "DirectIndustry lists conductivity, aggressiveness, abrasion, foam, turbulence, pressure and temperature."),
        ("Pick the output", "Switches give a dry contact, NPN or PNP output; transmitters give 4 to 20 mA or HART."),
        ("Prefer forks over floats", "For new switch installations, Emerson says vibrating forks are almost always recommended over float switches."),
    ]),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Using the control transmitter as the only overfill protection.", "API 2350 Category 3 needs an independent system."),
        ("Expecting a level reading to be a volume.", "Convert it with the tank geometry."),
        ("Fitting a conductive switch on a hydrocarbon.", "It only works on conductive liquids."),
    ]),
    p("If a transmitter disagrees with a switch, our blog on " + link("/blog/level-transmitter-calibration-mistakes", "level transmitter calibration mistakes") + " lists common calibration errors."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Can one continuous transmitter replace my level switches?", "For control it can replace two or more switches, but a safety alarm such as API 2350 high high should stay independent."),
        ("Which point level switch suits a new installation?", "Emerson recommends vibrating fork switches over floats in almost all new installations."),
        ("What output does a continuous level transmitter give?", "Usually 4 to 20 mA, often with HART."),
    ]),
]
