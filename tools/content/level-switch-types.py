META = {
    "category": "level-measurement-guides",
    "title": "Level Switch Types Explained: Float, Fork, Conductive and More",
    "keyword": "level switch",
    "subtitle": "How float, vibrating fork, conductive, capacitive, paddle and optical switches work",
    "meta_title": "Level Switch Types Explained: Float, Fork and More",
    "meta_description": "Learn how each level switch type works: float, vibrating fork, conductive, capacitive, rotary paddle and optical, with media, limits and selection tips.",
    "summary": "How the main point level switch technologies work, which media they suit and how to choose one.",
    "card_title": "Level Switch Types Explained",
    "author": "SWME Technical Staff",
    "published": "2026-11-16",
    "status": "published",
    "sort_order": 3,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "grid",
        "title": "Four Common Level Switch Types",
        "alt": "Infographic showing four common level switch types: float, vibrating fork, conductive and capacitive",
        "steps": [
            ["Float", "A float rides on the liquid and moves a magnet that operates a reed switch."],
            ["Vibrating fork", "A fork vibrates at resonance; product contact changes the vibration."],
            ["Conductive", "Conductive liquid bridges two electrodes and current flows."],
            ["Capacitive", "Product changes the capacitance between the probe and the tank wall."],
        ],
    },
}

_sw = lambda y, label, sub: (
    f'<rect x="452" y="{y - 14}" width="54" height="28" rx="5" fill="#0c8599"/>'
    f'<line x1="372" y1="{y}" x2="452" y2="{y}" stroke="#0c8599" stroke-width="6"/>'
    f'<line x1="506" y1="{y}" x2="560" y2="{y}" stroke="#495057" stroke-width="2" stroke-dasharray="5 4"/>'
    f'<text x="570" y="{y - 4}" font-size="14" font-weight="700" fill="#0a5f6d">{label}</text>'
    f'<text x="570" y="{y + 15}" font-size="13" fill="#555">{sub}</text>')

BODY = [
    takeaways([
        "A level switch detects whether product is present at one set height and gives an on or off signal.",
        "Float, vibrating fork, conductive, capacitive, rotary paddle and optical switches are the most common types.",
        "The right type depends on the medium: liquid or solid, conductive or not, clean, foaming or sticky.",
        "Switches are used for high and low alarms, pump protection and overfill prevention.",
    ]),
    p("Not every tank needs a continuous level reading. Often the process only needs to know whether the level has reached a certain point, for example to stop a pump before it runs dry. That is the job of a <strong>level switch</strong>, a point level device that changes state when product reaches its sensing position.",
      "This guide explains the main types and where each fits. SWME supplies " + link("/level-switches", "level switches") + ", " + link("/level-transmitters", "level transmitters") + " and " + link("/level-gauges", "level gauges") + " for tanks, vessels and silos across the GCC."),
    toc([("what", "What a level switch does"), ("types", "Level switch types"), ("compare", "Comparison table"),
         ("select", "How to choose"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("what", "What a Level Switch Does"),
    p("A level switch is a digital input: it tells the control system that the level is above or below one point. It typically triggers a high or low alarm or a process action, such as starting or stopping a pump. For example, when the level in a suction tank falls below the low switch, the input turns off and the PLC stops the pump, which protects it from running dry."),
    svg(
        '<rect x="150" y="40" width="260" height="280" rx="16" fill="#f8f9fa" stroke="#495057" stroke-width="3"/>'
        + '<rect x="153" y="150" width="254" height="167" rx="12" fill="#d3f0f4"/>'
        + '<line x1="153" y1="150" x2="407" y2="150" stroke="#0c8599" stroke-width="2"/>'
        + '<rect x="250" y="16" width="20" height="30" fill="#868e96"/><text x="200" y="30" text-anchor="end" font-size="13" fill="#555">Inlet</text>'
        + _sw(90, "High level switch", "Alarm or stop filling")
        + _sw(270, "Low level switch", "Stop pump to prevent dry running")
        + '<rect x="76" y="290" width="76" height="18" fill="#868e96"/>'
        + '<circle cx="50" cy="299" r="26" fill="#fff" stroke="#495057" stroke-width="3"/><text x="50" y="304" text-anchor="middle" font-size="12" font-weight="700" fill="#333">Pump</text>'
        + '<text x="280" y="200" text-anchor="middle" font-size="14" font-weight="600" fill="#0a5f6d">Liquid</text>'
        + '<text x="400" y="348" text-anchor="middle" font-size="13" fill="#555">Each switch gives an on or off signal to the PLC at one fixed height</text>',
        "Typical use of a high level switch and a low level switch on a tank with a pump", 360),
    h2("types", "Level Switch Types"),
    INFOGRAPHIC,
    h3("Float switch"),
    p("A float rides on the liquid surface and operates a mechanical or reed switch at a set position. In vertical designs, a magnetic float slides on a stem and operates a reed switch inside it. Suspended cable floats tilt to change state and are simple and popular for pump protection, though their switching point is less precise. Displacer switches work in a similar way, using buoyancy on a heavy displacer hung from a spring."),
    h3("Vibrating fork switch"),
    p("A piezoelectric drive makes a fork vibrate at its resonant frequency. When product covers the fork, the vibration changes and the switch changes state. Vibrating fork switches suit liquids and granular solids, and they are largely unaffected by viscosity, conductivity, foam and pressure. They need no calibration and little maintenance."),
    h3("Conductive switch"),
    p("Two or more electrodes sit in an open circuit. When a conductive liquid such as water, acid or a water based solution bridges them, current flows and the switch operates. Conductive switches are simple and inexpensive, and multi electrode versions can detect several levels. However, they do not work on hydrocarbons, solvents or oils."),
    h3("Capacitive switch"),
    p("The probe and the tank wall form a capacitor. When product covers the probe, the capacitance changes and the electronics switch the output. Capacitive switches work on both conductive and non conductive liquids and solids. For an example, read our blog on the " + link("/blog/gems-uls-200-capacitive-level-sensor-uae", "Gems ULS 200 capacitive level sensor") + "."),
    h3("Rotary paddle and optical switches"),
    p("A rotary paddle switch uses a slow motor to turn a paddle. When bulk solids such as cement, grain or sugar stop the paddle, the switch changes state, which makes it a simple choice for bins, hoppers and silos. An optical switch sends infrared light into a prism; when the tip is in liquid, less light returns to the receiver. Optical switches have no moving parts and need no calibration."),
    dyk("A conductive level switch that works perfectly in a water tank will never switch in a diesel tank. Oils and hydrocarbons have very low conductivity, so no current can flow between the electrodes. For these liquids, choose a float, vibrating fork, capacitive or optical switch instead."),
    h2("compare", "Level Switch Comparison Table"),
    table(["Type", "Principle", "Suits", "Watch out for"], [
        ["Float", "Buoyancy moves a magnet or contact", "Clean liquids, pump control", "Moving parts; cable floats less precise"],
        ["Vibrating fork", "Change in fork vibration", "Liquids and granular solids", "Point detection only"],
        ["Conductive", "Liquid bridges electrodes", "Water, acids, water based liquids", "Does not work on oils or solvents"],
        ["Capacitive", "Change in capacitance", "Conductive and non conductive liquids and solids", "Point detection only"],
        ["Rotary paddle", "Product stops a turning paddle", "Bulk solids in bins and silos", "Best for simple applications"],
        ["Optical", "Infrared light in a prism", "Most liquids", "Designed for liquids"],
    ]),
    h2("select", "How to Choose a Level Switch"),
    checklist([
        ("Medium", "Is it a liquid, slurry or bulk solid?"),
        ("Electrical properties", "Conductive liquids allow conductive switches; oils need another type."),
        ("Process conditions", "Check pressure, temperature, foam, viscosity and buildup."),
        ("Function", "Define each point: high alarm, low alarm, pump start or pump stop."),
        ("Mounting", "Top, side or cable mounting, and the space available inside the vessel."),
    ]),
    p("When the process needs the full level rather than one point, a continuous instrument is the better choice; compare options in " + link("/radar-vs-ultrasonic-level-measurement", "radar vs ultrasonic level measurement") + " and " + link("/how-a-magnetic-level-gauge-works", "how a magnetic level gauge works") + ". In addition, our blog on " + link("/blog/pump-protection-pressure-flow-temperature-instruments", "pump protection instruments") + " shows how switches fit into pump systems.",
      "For switch inputs to the control system, see this guide to " + ext("https://zentaengineering.com/automation-robotics/plc-hardware-selection/", "PLC hardware selection") + ". To work out the volume between high and low switch points, use the " + ext("https://zentacalculator.com/engineering/vertical-tank-volume/", "vertical tank volume calculator") + " or the " + ext("https://zentacalculator.com/engineering/horizontal-tank-volume/", "horizontal tank volume calculator") + ". More reading is on the " + ext("https://www.instrumentationblog.in/category/process-instrumentation/level-measurement/", "level measurement") + " pages of Instrumentation Blog."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Conductive switch on hydrocarbons.", "Oils and solvents do not conduct, so the switch never operates."),
        ("Too light a displacer.", "The displacer must be heavier than the medium in normal conditions, or the weight change cannot be detected."),
        ("Liquid switches in silos.", "Float and conductive switches are made for liquids; bulk solids need a paddle, fork or capacitive switch."),
        ("Paddle switch on complex duties.", "Rotary paddles suit simple bulk solids applications; harder duties need another technology."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What is the difference between a level switch and a level transmitter?", "A level switch gives an on or off signal at one point, while a level transmitter gives a continuous reading across the whole range."),
        ("Which level switch works on both liquids and solids?", "Vibrating fork and capacitive switches can be used on both liquids and bulk solids."),
        ("Can a float switch protect a pump from running dry?", "Yes. A low level float switch is a common way to stop a pump before the tank empties."),
    ]),
]
