META = {
    "category": "gas-detection-guides",
    "title": "LEL and UEL Explained: Flammable Limits and %LEL Readings",
    "keyword": "LEL and UEL",
    "subtitle": "Lower and upper explosive limits, flammable range, %LEL vs %vol and alarm levels",
    "meta_title": "LEL and UEL Explained: Flammable Limits and %LEL",
    "meta_description": "LEL and UEL explained: what lower and upper explosive limits mean, values for common gases, %LEL vs %vol and how gas detectors use them for alarms.",
    "summary": "What the lower and upper explosive limits mean, how %LEL relates to %vol and how detectors use LEL for alarms.",
    "card_title": "LEL and UEL Explained",
    "author": "SWME Technical Staff",
    "published": "2026-11-16",
    "status": "published",
    "sort_order": 3,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "steps",
        "title": "From %LEL Reading to Action",
        "alt": "Infographic showing how a gas detector measures percent LEL and raises a first and second alarm",
        "steps": [
            ["Sensor reads the gas", "A catalytic or infrared sensor measures flammable gas as a percentage of its LEL."],
            ["Signal to the control system", "0 to 100 percent LEL is sent as a 4 to 20 mA signal."],
            ["First alarm", "A common first alarm is 10 percent LEL: warn people and start ventilation."],
            ["Second alarm", "A second alarm, often 20 percent LEL, triggers shutdown, isolation or evacuation."],
        ],
    },
}

_bar = lambda x0, x1, y, c: f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="40" fill="{c}"/>'

BODY = [
    takeaways([
        "The LEL is the lowest concentration of a gas in air that can ignite; the UEL is the highest.",
        "Between the two limits lies the flammable range, for example 5 to 15 percent by volume for methane.",
        "Gas detectors usually read in %LEL, so 100 percent LEL means the gas has reached its lower explosive limit.",
        "Temperature, pressure and oxygen level all change the flammable range.",
    ]),
    p("Every flammable gas or vapour can only burn when it is mixed with air in the right proportion. The <strong>LEL and UEL</strong>, the lower and upper explosive limits, mark the edges of that proportion. They are the foundation of combustible gas detection, hot work permits and confined space entry.",
      "This guide explains what the limits mean, how %LEL readings work and why alarm levels sit far below the LEL. SWME supplies fixed and portable " + link("/gas-detectors", "gas detectors") + " for Oil and Gas, Petrochemical and Utilities plants across the GCC."),
    toc([("define", "What LEL and UEL mean"), ("range", "Flammable range of common gases"), ("percent", "%LEL vs %vol"),
         ("alarms", "How detectors use LEL and UEL"), ("factors", "What changes the limits"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("define", "What LEL and UEL Mean"),
    p("Combustion needs fuel, oxygen and an ignition source, and the fuel and oxygen must be mixed in the right proportion. The lower explosive limit (LEL) is the lowest concentration of a gas in air that will ignite. Below it, the mixture is too lean. The upper explosive limit (UEL) is the highest concentration that will ignite. Above it, the mixture is too rich, but it can become flammable again as it mixes with fresh air.",
      "The same limits are also called the lower and upper flammable limits (LFL and UFL), and the terms are often used interchangeably. For example, methane can only ignite when its concentration in air is between 5 and 15 percent."),
    svg(
        arrow_defs("#2b8a3e")
        + '<text x="400" y="28" text-anchor="middle" font-size="16" font-weight="700" fill="#1f6a2f">Methane in air (percent by volume)</text>'
        + _bar(60, 230, 60, "#d0ebff") + _bar(230, 570, 60, "#ffc9c9") + _bar(570, 740, 60, "#e5dbff")
        + '<rect x="60" y="60" width="680" height="40" fill="none" stroke="#495057" stroke-width="2"/>'
        + '<text x="140" y="85" text-anchor="middle" font-size="14" font-weight="600" fill="#1864ab">Too lean</text>'
        + '<text x="400" y="85" text-anchor="middle" font-size="14" font-weight="600" fill="#c92a2a">Flammable range</text>'
        + '<text x="655" y="85" text-anchor="middle" font-size="14" font-weight="600" fill="#5f3dc4">Too rich</text>'
        + "".join(f'<line x1="{60 + v * 34}" y1="100" x2="{60 + v * 34}" y2="110" stroke="#495057" stroke-width="2"/>'
                  f'<text x="{60 + v * 34}" y="128" text-anchor="middle" font-size="13" fill="#333">{v}</text>' for v in (0, 5, 10, 15, 20))
        + '<text x="230" y="150" text-anchor="middle" font-size="13" font-weight="700" fill="#c92a2a">LEL 5</text>'
        + '<text x="570" y="150" text-anchor="middle" font-size="13" font-weight="700" fill="#c92a2a">UEL 15</text>'
        + '<text x="400" y="195" text-anchor="middle" font-size="13" fill="#555">The detector scale stretches 0 to 5 percent by volume across 0 to 100 percent LEL</text>'
        + _bar(60, 128, 220, "#d3f9d8") + _bar(128, 196, 220, "#ffe066") + _bar(196, 740, 220, "#ffc9c9")
        + '<rect x="60" y="220" width="680" height="40" fill="none" stroke="#495057" stroke-width="2"/>'
        + "".join(f'<line x1="{60 + v * 6.8:.0f}" y1="260" x2="{60 + v * 6.8:.0f}" y2="270" stroke="#495057" stroke-width="2"/>'
                  f'<text x="{60 + v * 6.8:.0f}" y="288" text-anchor="middle" font-size="13" fill="#333">{v}</text>' for v in (0, 10, 20, 50, 100))
        + '<text x="94" y="245" text-anchor="middle" font-size="12" font-weight="600" fill="#1f6a2f">Below 10</text>'
        + '<text x="162" y="245" text-anchor="middle" font-size="12" font-weight="600" fill="#8f6c00">10 to 20</text>'
        + '<text x="468" y="245" text-anchor="middle" font-size="12" font-weight="600" fill="#c92a2a">Rising toward the LEL</text>'
        + '<text x="400" y="318" text-anchor="middle" font-size="14" font-weight="600" fill="#333">Detector reading in %LEL (25 percent LEL of methane = 1.25 percent by volume)</text>',
        "Methane flammable range and how a 0 to 100 percent LEL detector scale maps onto it", 340),
    h2("range", "Flammable Range of Common Gases"),
    p("Each gas has its own limits. Values below are percent by volume in air at about 25 degrees Celsius and 1 atmosphere, as listed in published reference tables. Small differences between sources come from test method, temperature and pressure."),
    table(["Gas", "LEL (% vol)", "UEL (% vol)", "Relative to air"], [
        ["Methane", "5.0", "15.0", "Lighter"],
        ["Propane", "2.1", "9.5", "Heavier"],
        ["Butane", "1.8", "8.4", "Heavier"],
        ["Hydrogen", "4.0", "75.0", "Much lighter"],
        ["Hydrogen sulphide", "4.3", "46.0", "Heavier"],
        ["Carbon monoxide", "12.5", "74.0", "About the same"],
        ["Hexane", "1.2", "7.5", "Heavier"],
    ]),
    svg(
        "".join(f'<text x="150" y="{50 + k * 52}" text-anchor="end" font-size="14" font-weight="600" fill="#333">{g}</text>'
                f'<rect x="170" y="{33 + k * 52}" width="{(u - l) * 6.5:.0f}" height="24" rx="4" transform="translate({l * 6.5:.0f},0)" fill="#2b8a3e"/>'
                f'<text x="{170 + u * 6.5 + 8:.0f}" y="{50 + k * 52}" font-size="13" fill="#555">{l} to {u}</text>'
                for k, (g, l, u) in enumerate((("Methane", 5.0, 15.0), ("Propane", 2.1, 9.5), ("Hydrogen", 4.0, 75.0),
                                              ("Hydrogen sulphide", 4.3, 46.0), ("Carbon monoxide", 12.5, 74.0))))
        + '<line x1="170" y1="290" x2="690" y2="290" stroke="#495057" stroke-width="2"/>'
        + "".join(f'<line x1="{170 + v * 6.5:.0f}" y1="290" x2="{170 + v * 6.5:.0f}" y2="298" stroke="#495057" stroke-width="2"/>'
                  f'<text x="{170 + v * 6.5:.0f}" y="316" text-anchor="middle" font-size="13" fill="#333">{v}</text>' for v in (0, 20, 40, 60, 80))
        + '<text x="470" y="342" text-anchor="middle" font-size="13" fill="#555">Percent by volume in air</text>',
        "Flammable range (LEL to UEL) of common gases in percent by volume", 360),
    p("Notice how wide the hydrogen range is. In addition, gases heavier than air settle near the floor, while light gases rise, which is why detector height matters. See our " + link("/gas-detector-placement-guide", "gas detector placement guide") + " for mounting heights."),
    h2("percent", "%LEL vs %vol"),
    p("A combustible gas detector rarely shows percent by volume. Instead it shows the concentration as a fraction of the LEL. At 100 percent LEL the gas has reached its lower explosive limit. The conversion is simple: percent by volume equals %LEL divided by 100, multiplied by the LEL of that gas.",
      "For example, 25 percent LEL of methane is 0.25 multiplied by 5, which is 1.25 percent by volume. Percent by volume also converts to ppm by multiplying by 10,000, so the methane LEL equals 50,000 ppm. To scale the detector output, try the " + ext("https://zentacalculator.com/engineering/4-20ma-scaling/", "4 to 20 mA scaling calculator") + " and the " + ext("https://zentacalculator.com/engineering/plc-analog-scaling/", "PLC analog scaling calculator") + "."),
    dyk("A very rich atmosphere is not a safe atmosphere. Above the UEL the mixture is too rich to burn, but as fresh air leaks in, it passes back through the flammable range. In addition, catalytic sensors need oxygen to work, so readings in gas rich, oxygen poor air can be misleading. Never assume a very rich atmosphere is safe."),
    h2("alarms", "How Gas Detectors Use LEL and UEL"),
    p("Fixed detectors usually transmit 0 to 100 percent LEL as a 4 to 20 mA signal to a control panel or PLC. Alarm points sit far below the LEL to give people time to react. Published guidance commonly uses a first alarm at 10 percent LEL as a warning and a second alarm at 20 percent LEL for evacuation, while some suppliers describe 25 percent LEL as a standard alarm point.",
      "The low alarm typically starts ventilation and alerts staff, and the high alarm triggers shutdown, isolation or evacuation. In addition, work permits set their own gas test limits, such as below 10 percent LEL for confined space entry."),
    INFOGRAPHIC,
    p("The sensor type matters too. Catalytic bead sensors need oxygen and can be poisoned by some compounds, and infrared sensors suit most hydrocarbons but typically cannot detect hydrogen. Compare the options in our guide to " + link("/types-of-gas-sensors", "types of gas sensors") + ". For a wireless example, read our blog on the " + link("/blog/vanguard-wireless-hart-gas-detector-uae", "Vanguard WirelessHART gas detector") + "."),
    h2("factors", "What Changes the LEL and UEL"),
    rows([
        ("Temperature", "as temperature rises, the LEL tends to fall and the UEL tends to rise, so the range widens."),
        ("Pressure", "higher pressure often widens the flammable range."),
        ("Oxygen enrichment", "lowers the LEL and raises the UEL significantly."),
        ("Oxygen depletion and inerting", "narrows the range; nitrogen or carbon dioxide inerting is used to prevent explosions."),
    ]),
    p("Ventilation dilutes leaks and keeps them below the LEL. Use the " + ext("https://zentacalculator.com/engineering/air-changes-per-hour/", "air changes per hour calculator") + " to check room ventilation, and read more about sensors on the " + ext("https://www.instrumentationblog.in/category/process-instrumentation/analytical-measurements/", "analytical measurements") + " pages of Instrumentation Blog. Detectors must be bump tested and calibrated regularly; SWME offers " + link("/test-calibration", "test and calibration equipment") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Reading %LEL as %vol.", "50 percent LEL of methane is only 2.5 percent by volume, but it is already half way to ignition."),
        ("Forgetting the oxygen level.", "Catalytic sensors need oxygen, and oxygen enrichment widens the flammable range."),
        ("Assuming below 10 percent LEL is always safe.", "Stratification, ventilation changes and poor sensor placement can hide pockets of gas."),
        ("Using an infrared sensor for hydrogen.", "Most infrared sensors cannot see hydrogen; choose catalytic or another suitable technology."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What is the LEL of methane?", "About 5 percent by volume in air, and its UEL is about 15 percent. So 100 percent LEL on a methane detector equals about 5 percent methane."),
        ("What is the difference between LEL and UEL?", "The LEL is the lowest concentration that can ignite and the UEL is the highest. Between them is the flammable range."),
        ("Why do detectors alarm far below the LEL?", "Low alarm points, such as 10 or 20 percent LEL, give people time to ventilate, isolate the leak or evacuate before the mixture can ignite."),
    ]),
]
