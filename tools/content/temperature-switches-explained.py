META = {
    "category": "temperature-measurement-guides",
    "title": "Temperature Switches Explained: Types, Setpoint and Deadband",
    "keyword": "temperature switch",
    "subtitle": "How bimetal, filled system and electronic temperature switches work, what setpoint and deadband mean, and how to install them",
    "meta_title": "Temperature Switches Explained: Types and Deadband",
    "meta_description": "Temperature switch guide: bimetal, filled bulb and electronic types, setpoint and deadband, SPDT contacts, limiters and installation tips for process plants.",
    "summary": "How a temperature switch opens or closes a contact at a set temperature, the main types, setpoint and deadband, and how to install one.",
    "card_title": "Temperature Switches Explained",
    "author": "SWME Technical Staff",
    "published": "2026-11-21",
    "status": "published",
    "sort_order": 6,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "flow",
        "title": "How a Filled Temperature Switch Trips",
        "alt": "Infographic showing how a filled bulb temperature switch turns a temperature rise into a contact change",
        "steps": [
            ["Bulb heats", "Process heat raises the pressure of the fill inside the bulb."],
            ["Capillary", "The pressure travels through a fine capillary to the switch housing."],
            ["Membrane moves", "A membrane or diaphragm expands against the range spring."],
            ["Contact changes", "At the setpoint a snap action switch changes over its contacts."],
        ],
    },
}

_C = "#d9480f"
_T = "#a33608"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_diag = (
    # process pipe and bulb
    '<rect x="40" y="250" width="240" height="70" fill="#fff4e6" stroke="#495057" stroke-width="2"/>'
    + _t(160, 340, "Process", 13, anchor="middle", fill="#495057")
    + '<rect x="120" y="215" width="80" height="16" fill="#adb5bd"/>'
    + '<rect x="140" y="231" width="40" height="78" rx="18" fill="' + _C + '"/>'
    + _t(212, 228, "Bulb", 13)
    # capillary
    + '<path d="M160,215 C160,140 260,170 330,120 C380,85 430,110 470,110" fill="none" stroke="#495057" stroke-width="3"/>'
    + _t(300, 175, "Capillary", 13)
    + _t(300, 193, "carries the fill pressure", 12, "400", "#555")
    # housing
    + '<rect x="470" y="40" width="290" height="250" rx="12" fill="#fff" stroke="#495057" stroke-width="2.5"/>'
    + _t(615, 64, "Switch housing", 13, anchor="middle", fill="#495057")
    # membrane
    + '<path d="M480,90 L480,130 Q500,110 480,90" fill="' + _C + '"/>'
    + '<line x1="480" y1="85" x2="480" y2="135" stroke="#495057" stroke-width="3"/>'
    + _t(474, 156, "Membrane", 12, "600")
    # push rod and spring
    + '<line x1="492" y1="110" x2="560" y2="110" stroke="#495057" stroke-width="4"/>'
    + '<path d="M560,110 l8,-10 l8,20 l8,-20 l8,20 l8,-20 l8,20 l8,-10" fill="none" stroke="#868e96" stroke-width="2.5"/>'
    + _t(588, 92, "Range spring sets the setpoint", 12, "400", "#555", "middle")
    # snap switch contacts
    + '<circle cx="560" cy="220" r="6" fill="#343a40"/>'
    + _t(560, 248, "C", 14, anchor="middle")
    + '<line x1="560" y1="220" x2="652" y2="196" stroke="#343a40" stroke-width="4"/>'
    + '<circle cx="660" cy="194" r="6" fill="#343a40"/>'
    + '<circle cx="660" cy="240" r="6" fill="#343a40"/>'
    + _t(676, 199, "NC", 14) + _t(676, 245, "NO", 14)
    + '<line x1="548" y1="112" x2="548" y2="208" stroke="#adb5bd" stroke-width="2" stroke-dasharray="5 4"/>'
    + _t(555, 186, "Snap action", 12, "600")
    + _t(40, 40, "Rising temperature", 14)
    + _t(40, 60, "raises fill pressure, membrane pushes", 12, "400", "#555")
    + _t(40, 78, "the snap switch from NC to NO", 12, "400", "#555")
)


def _band():
    out = []
    out.append('<line x1="80" y1="40" x2="80" y2="250" stroke="#495057" stroke-width="2"/>')
    out.append('<line x1="80" y1="250" x2="760" y2="250" stroke="#495057" stroke-width="2"/>')
    out.append(_t(70, 30, "Temperature", 12, "600", "#495057", "start"))
    out.append(_t(760, 270, "Time", 12, "600", "#495057", "end"))
    out.append('<line x1="80" y1="100" x2="760" y2="100" stroke="' + _C + '" stroke-width="2" stroke-dasharray="7 5"/>')
    out.append('<line x1="80" y1="170" x2="760" y2="170" stroke="#1971c2" stroke-width="2" stroke-dasharray="7 5"/>')
    out.append(_t(90, 92, "Setpoint: contact changes on rising temperature", 12, "700", _C))
    out.append(_t(90, 188, "Reset point: contact returns on falling temperature", 12, "700", "#1864ab"))
    out.append('<polyline points="80,230 220,100 330,80 420,130 500,170 580,200 660,100 760,90" fill="none" stroke="#343a40" stroke-width="3"/>')
    out.append('<circle cx="220" cy="100" r="6" fill="' + _C + '"/>')
    out.append('<circle cx="500" cy="170" r="6" fill="#1971c2"/>')
    out.append('<circle cx="660" cy="100" r="6" fill="' + _C + '"/>')
    out.append('<line x1="720" y1="104" x2="720" y2="166" stroke="#495057" stroke-width="2"/>')
    out.append('<line x1="712" y1="104" x2="728" y2="104" stroke="#495057" stroke-width="2"/>')
    out.append('<line x1="712" y1="166" x2="728" y2="166" stroke="#495057" stroke-width="2"/>')
    out.append(_t(712, 140, "Deadband", 13, "700", "#343a40", "end"))
    return "".join(out)


BODY = [
    takeaways([
        "A temperature switch opens or closes an electrical contact when the temperature goes above or below a set level.",
        "Mechanical types use the expansion of a bimetal, liquid or gas and need no power; electronic types read an RTD.",
        "The deadband is the gap between the setpoint on rising temperature and the reset point on falling temperature.",
        "A limiter stays tripped after an over temperature until someone presses reset.",
    ]),
    p("A <strong>temperature switch</strong> gives a plain on or off signal at a chosen temperature: switch off a heater, start a fan on a compressor, or act as a high limit. SWME supplies " + link("/temperature-switches", "temperature switches") + ", " + link("/thermowells", "thermowells") + " and " + link("/rtd-thermocouples", "RTD and thermocouple sensors") + " for plants across the UAE and GCC."),
    toc([("how", "How a temperature switch works"), ("types", "Switch types"), ("deadband", "Setpoint and deadband"),
         ("contacts", "Contacts and limiters"), ("install", "Installation"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("how", "How a Temperature Switch Works"),
    p("" + ext("https://www.jumo.group/nl/en/services/faq/temperature-measurement/temperature-switches", "JUMO") + " explains that mechanical switches rely on metals, liquids or gases expanding as they warm until they actuate a contact. In a filled system the probe, capillary and membrane form a sealed unit. When the probe heats up the system pressure rises, the membrane expands and a snap action switch trips.",
      "Baumer, quoted by " + ext("https://instrumentationtools.com/basics-of-temperature-switch", "Instrumentation Tools") + ", describes the same idea as a pressure switch with a sealed bulb fitted to its pressure port. The fill's vapour pressure acts on a diaphragm and piston assembly, which works a micro switch at the setpoint. Compare it with our guide to " + link("/what-is-a-pressure-switch", "what a pressure switch is") + "."),
    INFOGRAPHIC,
    svg(_diag, "Filled system temperature switch: the bulb, capillary and membrane drive a snap action switch with C, NO and NC contacts", 350),
    h2("types", "Temperature Switch Types"),
    table(["Type", "How it senses", "Points from JUMO"],
          [["Bimetal", "Two metals with different expansion rates, for example copper and nickel, are rolled together and bend with temperature", "Switching point fixed in production; vibration resistance up to 10 g is not uncommon; screws in like a sensor"],
           ["Filled (gas or liquid)", "Fill pressure in a probe and capillary moves a membrane", "Capillary bore 0.2 mm, practical length up to 5 m; switching point usually set on the housing"],
           ["Electronic", "An RTD signal is evaluated electronically", "Setpoint by keypad, optional display, can also give a 4 to 20 mA output"]]),
    p("Mechanical switches are passive and need no supply voltage. JUMO says most handle switching currents of 10 A or more, so small heaters can be switched directly, while larger loads need a contactor. The bimetal principle is the same one used in our " + link("/bimetal-thermometer-working-principle", "bimetal thermometer guide") + "."),
    h2("deadband", "Setpoint and Deadband"),
    p("The setpoint is where the contact changes. The reset point is where it changes back, and the gap between the two is the deadband, which JUMO calls switching hysteresis. Baumer says the setpoint must sit inside the adjustable range and be stated as rising or falling, that the deadband is normally fixed, and that the standard factory setting is 50% of the scale on falling temperature, though this varies by vendor."),
    svg(_band(), "Deadband: the contact changes at the setpoint on rising temperature and returns only at the lower reset point", 280),
    dyk("Some switches, such as WIKA's TS 972, let you adjust the differential. Its manual lists a switch differential larger than the switch point as one reason a contact will not switch."),
    h2("contacts", "Contacts and Limiters"),
    rows([
        ("SPDT", "Three terminals: common (C), normally open (NO) and normally closed (NC)."),
        ("DPDT", "Two SPDT elements that actuate and reset together, so two separate circuits can be switched."),
        ("Limiter", "After an over temperature trip the contact does not close by itself; a reset button must be pressed. JUMO notes limiters are often used on unattended systems."),
        ("Typical duties", "Heater cutouts, compressor protection with bimetal switches, and limits that JUMO says are mandatory on heat transfer oil systems and grain dryers."),
    ]),
    p("JUMO also describes pairing a controller with a separate switch, so the controller regulates and the switch acts as an independent limit. For a continuous signal instead, see " + link("/temperature-transmitters", "temperature transmitters") + "."),
    h2("install", "Installation"),
    checklist([
        ("Orientation", "WIKA's TS 972 manual says to mount vertically with the bulb fully immersed."),
        ("Temperature limit", "The same manual warns the sensing element is permanently damaged if its maximum temperature is exceeded even once."),
        ("Thermowell", "Use one for incompatible media; WIKA also recommends it above 1 bar line pressure or above boiling point. See " + link("/what-is-a-thermowell", "what is a thermowell") + "."),
        ("Capillary care", "Do not carry the switch by the capillary or bend it sharply at the bulb."),
        ("Environment", "Avoid temperature shocks, and stop ice forming in humid conditions below zero."),
    ]),
    p("For sensor lag, try the " + ext("https://zentacalculator.com/engineering/sensor-response-time/", "sensor response time calculator") + ", and for electronic switches the " + ext("https://zentacalculator.com/engineering/pt100-resistance/", "Pt100 resistance calculator") + ". More reading is in the " + ext("https://www.instrumentationblog.in/category/process-instrumentation/temperature-measurements/", "Instrumentation Blog temperature section") + " and our blog on the " + link("/blog/ue-400-series-pressure-and-temperature-switch-uae", "UE 400 series pressure and temperature switch") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Ignoring the deadband.", "A temperature switch does not reset at its setpoint; it resets at the lower reset point."),
        ("Overloading the contact.", "Switch large loads through a contactor."),
        ("Overheating the bulb once.", "WIKA says a single excursion past the maximum can permanently damage the element."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Does a temperature switch need power?", "Mechanical types do not. Electronic types do, because they evaluate an RTD signal."),
        ("What is the deadband?", "The difference between the setpoint on rising temperature and the reset point on falling temperature."),
        ("What is the difference between a switch and a limiter?", "A limiter stays tripped after an over temperature until it is reset by hand."),
    ]),
]
