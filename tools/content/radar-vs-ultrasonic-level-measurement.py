META = {
    "category": "level-measurement-guides",
    "title": "Radar vs Ultrasonic Level Measurement: Which One to Choose?",
    "keyword": "radar vs ultrasonic level",
    "subtitle": "Working principles, strengths, limits and selection for tanks and silos",
    "meta_title": "Radar vs Ultrasonic Level Measurement Compared",
    "meta_description": "Compare radar vs ultrasonic level measurement: how each works, effect of vapour, foam and temperature, accuracy, cost and how to choose for your tank.",
    "summary": "How radar and ultrasonic level transmitters work and when to choose each one.",
    "card_title": "Radar vs Ultrasonic Level Measurement",
    "author": "SWME Technical Staff",
    "published": "2026-11-15",
    "status": "published",
    "sort_order": 1,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "title": "Noncontact Level Measurement",
        "alt": "Infographic showing how radar vs ultrasonic level measurement works using time of flight",
        "steps": [
            ["Send a pulse", "The sensor sends a sound pulse (ultrasonic) or microwave pulse (radar) down to the surface."],
            ["Surface reflection", "The pulse reflects from the liquid or solid surface back to the sensor."],
            ["Time of flight", "The sensor measures the travel time and calculates the distance."],
            ["Level output", "Tank height minus distance gives level, sent as 4 to 20 mA or HART."],
        ],
    },
}

BODY = [
    takeaways([
        "Both technologies measure the time a pulse takes to reach the surface and return.",
        "Ultrasonic uses sound, so temperature, vapour, dust and foam affect it.",
        "Radar uses microwaves, which pass through vapour, pressure and temperature changes almost unaffected.",
        "Ultrasonic costs less for simple water tanks; radar suits demanding process vessels.",
    ]),
    p("Noncontact level transmitters are popular because nothing touches the product. The two main options are ultrasonic and radar. Choosing between <strong>radar vs ultrasonic level</strong> measurement depends on the vessel, the product and the process conditions inside the tank.",
      "This guide compares the two technologies side by side. SWME supplies " + link("/level-transmitters", "level transmitters") + ", " + link("/level-switches", "level switches") + " and " + link("/level-gauges", "level gauges") + " for storage tanks, process vessels and open channels."),
    toc([("principle", "How both technologies work"), ("ultrasonic", "Ultrasonic level measurement"), ("radar", "Radar level measurement"),
         ("compare", "Radar vs ultrasonic level compared"), ("choose", "How to choose"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("principle", "How Both Technologies Work"),
    svg(arrow_defs(T["c"]) +
        '<rect x="200" y="60" width="300" height="280" fill="none" stroke="#495057" stroke-width="4"/>'
        f'<rect x="202" y="200" width="296" height="138" fill="{T["bg"]}"/>'
        f'<path d="M202 200 Q 260 190 320 200 T 440 200 T 498 200" fill="none" stroke="{T["c"]}" stroke-width="3"/>'
        f'<rect x="330" y="30" width="40" height="36" rx="5" fill="{T["c"]}"/>'
        f'<path d="M340 66 L300 198 L400 198 L360 66 Z" fill="{T["c"]}" opacity="0.12"/>'
        f'<line x1="350" y1="72" x2="350" y2="192" stroke="{T["c"]}" stroke-width="2.5" marker-end="url(#ah)"/>'
        '<line x1="530" y1="66" x2="530" y2="198" stroke="#333" stroke-width="1.5"/><text x="540" y="135" font-size="15" fill="#333" font-weight="600">D: measured distance</text>'
        '<line x1="530" y1="200" x2="530" y2="338" stroke="#e67700" stroke-width="3"/><text x="540" y="275" font-size="15" fill="#e67700" font-weight="600">L: level</text>'
        '<line x1="170" y1="66" x2="170" y2="338" stroke="#999" stroke-width="1.5"/><text x="160" y="205" font-size="15" fill="#555" text-anchor="end">H: tank height</text>'
        f'<text x="380" y="52" font-size="13" fill="{T["tx"]}">Radar or ultrasonic sensor</text>'
        f'<text x="560" y="320" font-size="16" fill="{T["c"]}" font-weight="700">L = H minus D</text>',
        "Noncontact level measurement: the sensor measures distance D and calculates level L", 360),
    p("Both sensors mount on top of the tank and point down at the surface. They send a pulse, wait for the echo and measure the time of flight. Because the speed of the pulse is known, the sensor converts time into distance. The level is then the tank height minus that distance.",
      "The key difference is the type of pulse. Ultrasonic sensors send sound waves, while radar sensors send electromagnetic waves. Sound needs a medium to travel through and changes speed with temperature. Microwaves travel at the speed of light and are almost unaffected by the gas above the product."),
    INFOGRAPHIC,
    h2("ultrasonic", "Ultrasonic Level Measurement"),
    p("An ultrasonic transducer sends a sound pulse, typically between 10 and 70 kHz, and listens for the echo. The sensor includes a temperature probe to correct the speed of sound. You can try the effect with the " + ext("https://zentacalculator.com/engineering/ultrasonic-level/", "ultrasonic level calculator") + "."),
    rows([
        ("Strengths", "low cost, simple setup, good for water, wastewater, chemicals in atmospheric tanks and open channel flow."),
        ("Limits", "affected by vapour layers, heavy foam, dust, strong temperature gradients and pressure."),
        ("Blocking distance", "a dead zone close to the sensor, usually 0.25 to 0.5 m, where it cannot measure."),
    ]),
    h2("radar", "Radar Level Measurement"),
    p("Radar sensors send microwave pulses or a continuous frequency sweep (FMCW). Modern 80 GHz radars have a very narrow beam, so they can measure in small tanks with internal fittings. Guided wave radar is a related technology that sends the pulse along a probe or cable; see this " + ext("https://www.instrumentationblog.in/guided-wave-radar-troubleshooting/", "guided wave radar troubleshooting guide") + "."),
    rows([
        ("Strengths", "unaffected by temperature, pressure, vacuum and most vapours; high accuracy, often within 1 to 3 mm."),
        ("Limits", "higher cost; very low dielectric products and heavy foam may weaken the echo."),
        ("Beam angle", "high frequency radars focus the beam, reducing false echoes from ladders and agitators."),
    ]),
    dyk("Sound travels about 18% faster at 50 degrees Celsius than at 0 degrees Celsius. Without temperature compensation, an ultrasonic sensor on a hot tank would show a large level error. Radar has no such problem, because microwaves travel at nearly the same speed in air, vapour and most gases."),
    h2("compare", "Radar vs Ultrasonic Level Compared"),
    table(["Factor", "Ultrasonic", "Radar"], [
        ["Pulse type", "Sound", "Microwave"],
        ["Typical accuracy", "0.25% of span", "1 to 3 mm"],
        ["Pressure and vacuum", "Not suitable", "Suitable"],
        ["High temperature", "Limited, usually below 90 degrees Celsius", "Up to 200 degrees Celsius or more"],
        ["Vapour and dust", "Can absorb the signal", "Little effect"],
        ["Foam", "Absorbs the echo", "Can weaken the echo"],
        ["Cost", "Lower", "Higher"],
        ["Typical use", "Water tanks, sumps, open channels", "Process vessels, fuel tanks, reactors"],
    ]),
    h2("choose", "How to Choose"),
    twocol([
        ("Choose ultrasonic when", "bi-soundwave", [
            "The tank is atmospheric and at moderate temperature.",
            "The product is water, wastewater or a mild chemical.",
            "Budget is a key factor and accuracy needs are moderate.",
        ]),
        ("Choose radar when", "bi-broadcast", [
            "The vessel is pressurised, under vacuum or hot.",
            "Vapours, steam or dust are present above the product.",
            "High accuracy or custody level data is required.",
        ]),
    ]),
    p("When the radar vs ultrasonic level decision is still unclear, consider a differential pressure solution instead. The " + ext("https://zentacalculator.com/engineering/dp-level-range/", "DP level transmitter range calculator") + " and the guide to " + ext("https://www.instrumentationblog.in/dp-transmitter-level-measurement/", "DP transmitter level measurement") + " explain that method. For tank contents, the " + ext("https://zentacalculator.com/engineering/vertical-tank-volume/", "vertical tank volume calculator") + " converts level to volume."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Mounting too close to the wall.", "Echoes from the wall or welds are mistaken for the surface."),
        ("Ignoring the blocking distance.", "The tank can overfill into the zone the sensor cannot see."),
        ("Pointing at the inlet stream.", "Falling product creates false echoes and noisy readings."),
        ("Skipping a false echo map.", "Fixed obstacles such as ladders should be mapped out at commissioning."),
    ]),
    p("Calibration also matters for every level device. Read our article on " + link("/blog/level-transmitter-calibration-mistakes", "level transmitter calibration mistakes") + " for practical advice."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Is radar always better than ultrasonic?", "No. Radar is more robust, but ultrasonic is accurate and cheaper for simple atmospheric water tanks."),
        ("Can ultrasonic sensors work in a vacuum?", "No. Sound needs air or gas to travel, so ultrasonic sensors cannot work in a vacuum."),
        ("What is the difference between radar and guided wave radar?", "Free space radar sends the pulse through the air, while guided wave radar sends it along a probe, which helps with foam and low dielectric products."),
    ]),
]

META["infographic"].update({"layout": "compare", "title": "Radar vs Ultrasonic Level",
   "columns": [["Ultrasonic", ["Sound pulse, 10 to 70 kHz", "Affected by vapour, foam, dust", "Atmospheric tanks only", "Lower cost"]],
               ["Radar", ["Microwave pulse, up to 80 GHz", "Little effect from vapour", "Pressure, vacuum and heat", "Accuracy 1 to 3 mm"]]]})
