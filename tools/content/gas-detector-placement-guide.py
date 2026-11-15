META = {
    "category": "gas-detection-guides",
    "title": "Gas Detector Placement Guide: Where to Install Fixed Detectors",
    "keyword": "gas detector placement",
    "subtitle": "Gas density, leak sources, airflow, mounting height and coverage",
    "meta_title": "Gas Detector Placement Guide for Fixed Detectors",
    "meta_description": "A practical gas detector placement guide: how gas density, leak sources, ventilation and mounting height decide where to install fixed gas detectors.",
    "summary": "Where to install fixed gas detectors based on gas density, leak sources and airflow.",
    "card_title": "Gas Detector Placement Guide",
    "author": "SWME Technical Staff",
    "published": "2026-11-15",
    "status": "published",
    "sort_order": 2,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "title": "Where to Mount Gas Detectors",
        "alt": "Infographic showing gas detector placement heights for heavy, light and air density gases",
        "steps": [
            ["Heavier than air", "H2S, propane, butane: mount 0.3 to 0.5 m above floor or grade."],
            ["Lighter than air", "Methane, hydrogen, ammonia: mount near the ceiling or highest point."],
            ["Similar to air", "CO and O2: mount in the breathing zone, about 1.5 m above floor."],
            ["Near leak sources", "Place detectors close to pumps, valves, flanges and compressor seals."],
        ],
    },
}

BODY = [
    takeaways([
        "Good gas detector placement depends on gas density, leak sources, airflow and people.",
        "Heavy gases collect low, light gases rise, and gases similar to air follow the airflow.",
        "Detectors belong near likely leak points and where people work or breathe.",
        "A documented placement study, often using gas dispersion modelling, gives the best coverage.",
    ]),
    p("Even the best sensor cannot warn of a leak if the gas never reaches it. That is why <strong>gas detector placement</strong> is as important as choosing the right technology. Detectors in the wrong place give a false sense of safety.",
      "This guide explains the main factors that decide where fixed detectors should go. SWME supplies fixed and wireless " + link("/gas-detectors", "gas detectors") + " and supports clients with selection for Oil and Gas, Petrochemical and Utilities facilities."),
    toc([("factors", "Factors that decide placement"), ("height", "Mounting height by gas"), ("sources", "Leak sources and coverage"),
         ("areas", "Placement by area type"), ("checklist", "Gas detector placement checklist"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("factors", "Factors That Decide Placement"),
    rows([
        ("Gas density", "whether the gas is heavier or lighter than air decides the mounting height."),
        ("Leak sources", "pumps, compressors, valves, flanges, sampling points and vents are the most likely leak points."),
        ("Airflow", "wind, ventilation and natural convection carry the gas cloud in a specific direction."),
        ("People", "detectors must protect occupied areas, escape routes and air intakes."),
        ("Access", "detectors must be reachable for calibration and bump testing."),
    ]),
    INFOGRAPHIC,
    h2("height", "Mounting Height by Gas"),
    svg('<rect x="40" y="30" width="720" height="300" fill="#f8f9fa" stroke="#495057" stroke-width="3"/>'
        '<line x1="40" y1="330" x2="760" y2="330" stroke="#495057" stroke-width="6"/>'
        '<text x="50" y="350" font-size="13" fill="#555">Floor</text><text x="50" y="25" font-size="13" fill="#555">Ceiling</text>'
        + "".join(f'<rect x="{x}" y="{y}" width="34" height="44" rx="6" fill="{c}"/><circle cx="{x+17}" cy="{y+17}" r="7" fill="#fff"/>'
                  f'<text x="{x+50}" y="{y+18}" font-size="15" font-weight="600" fill="#333">{t1}</text><text x="{x+50}" y="{y+38}" font-size="13" fill="#555">{t2}</text>'
                  for x, y, c, t1, t2 in ((100, 45, "#1971c2", "Light gases", "Methane, hydrogen, ammonia"),
                                          (300, 165, T["c"], "Similar to air", "CO, O2 in breathing zone"),
                                          (520, 270, "#e67700", "Heavy gases", "H2S, propane, chlorine")))
        + '<g fill="none" stroke="#adb5bd" stroke-width="2"><circle cx="160" cy="130" r="10"/><circle cx="185" cy="105" r="7"/><circle cx="470" cy="305" r="12"/><circle cx="440" cy="315" r="8"/></g>'
        '<text x="300" y="150" font-size="12" fill="#666">about 1.5 m</text><text x="520" y="262" font-size="12" fill="#666">0.3 to 0.5 m above floor</text>',
        "Typical mounting heights for gas detectors in an enclosed room", 360),
    table(["Gas", "Relative density (air = 1)", "Mounting position"], [
        ["Hydrogen (H2)", "0.07", "High, near ceiling or roof apex"],
        ["Methane (CH4)", "0.55", "High, near ceiling"],
        ["Ammonia (NH3)", "0.59", "High, near ceiling"],
        ["Carbon monoxide (CO)", "0.97", "Breathing zone, about 1.5 m"],
        ["Oxygen (O2)", "1.10", "Breathing zone, about 1.5 m"],
        ["Hydrogen sulphide (H2S)", "1.19", "Low, 0.3 to 0.5 m above floor"],
        ["Propane (C3H8)", "1.56", "Low, 0.3 to 0.5 m above floor"],
        ["Chlorine (Cl2)", "2.49", "Low, close to floor"],
    ]),
    dyk("Density is not the whole story. A cold release of a light gas, such as liquefied natural gas boiling off, can sink and spread along the ground before it warms up and rises. Likewise, hot heavy gases may rise at first. This is why gas detector placement should consider release temperature as well as molecular weight."),
    h2("sources", "Leak Sources and Coverage"),
    p("Place detectors close to the equipment most likely to leak, but not so close that a small, harmless release triggers constant alarms. Typical distances are 1 to 5 metres from the source, on the downwind side of the prevailing airflow.",
      "Large open areas also need perimeter detectors to warn before a gas cloud reaches occupied buildings or ignition sources. In addition, open path infrared detectors can cover a line of sight up to 100 metres or more, which helps along pipe racks and fence lines."),
    twocol([
        ("Point detectors", "bi-geo-alt-fill", [
            "Measure gas at one location.",
            "Best near specific leak sources.",
            "Required for toxic gases in ppm.",
        ]),
        ("Open path detectors", "bi-arrows-expand", [
            "Measure along a beam between two units.",
            "Cover large areas and perimeters.",
            "Report concentration over the path length.",
        ]),
    ]),
    h2("areas", "Placement by Area Type"),
    rows([
        ("Compressor and pump houses", "near seals and couplings, plus at the ventilation outlet."),
        ("Enclosed rooms", "at the gas accumulation point and close to the HVAC exhaust."),
        ("HVAC air intakes", "detectors trip the fans to stop gas entering control rooms."),
        ("Tank farms and loading bays", "low level detectors for heavy hydrocarbon vapours around bunds and pumps."),
        ("Battery rooms", "high level hydrogen detection near the ceiling."),
    ]),
    p("Ventilation design and detection work together. The " + ext("https://zentacalculator.com/engineering/air-changes-per-hour/", "air changes per hour calculator") + " helps you check room ventilation rates that affect where gas collects."),
    h2("checklist", "Gas Detector Placement Checklist"),
    checklist([
        ("List the gases", "Include density, toxicity and release temperature for each."),
        ("Map leak sources", "Mark pumps, compressors, flanges, valves and vents on a layout."),
        ("Study the airflow", "Note prevailing wind, ventilation paths and dead zones."),
        ("Set mounting heights", "Use gas density and release conditions to fix the height."),
        ("Protect people and intakes", "Add detectors at escape routes, doorways and HVAC intakes."),
        ("Plan access", "Make sure each detector can be calibrated and bump tested safely."),
        ("Document and review", "Record the basis for each location and review after plant changes."),
    ]),
    p("This checklist is a practical starting point, but large facilities should base gas detector placement on a formal study following standards such as IEC 60079 29 2. For sensor technology choices, read " + link("/types-of-gas-sensors", "types of gas sensors explained") + ". Wireless options are covered in our article on the " + link("/blog/ue-vanguard-suppliers-in-uae", "UE Vanguard wireless gas detector") + ". For loop design and SIL calculations, see the " + ext("https://zentacalculator.com/engineering/availability-mtbf/", "availability calculator") + " and these " + ext("https://www.instrumentationblog.in/category/process-instrumentation/analytical-measurements/", "analytical measurement articles") + ". To understand how detectors connect to the control system, see this overview of " + ext("https://zentaengineering.com/automation-robotics/scada-system-architecture/", "SCADA system architecture") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Same height for every gas.", "Light and heavy gases need completely different mounting positions."),
        ("Placing detectors in dead air.", "Corners and recesses may never see the gas cloud."),
        ("Mounting directly in a strong draft.", "Fresh air dilutes the gas before it reaches the sensor."),
        ("No access for maintenance.", "Detectors that cannot be reached are rarely calibrated."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("How many gas detectors do I need?", "It depends on leak sources, area size and airflow. A placement study or dispersion model gives the most reliable answer."),
        ("Where should an H2S detector be mounted?", "H2S is heavier than air, so mount detectors about 0.3 to 0.5 m above the floor near likely leak points and in low areas."),
        ("Where should a hydrogen detector be mounted?", "Hydrogen is much lighter than air, so mount detectors at the highest point of the room, where the gas collects."),
    ]),
]

META["infographic"].update({"layout": "levels", "title": "Gas Detector Mounting Heights", "top_label": "Ceiling", "bottom_label": "Floor",
   "levels": [["Heavy gases", "H2S, propane, chlorine: 0.3 to 0.5 m above floor.", 0.08],
              ["Breathing zone", "CO and oxygen: about 1.5 m above floor.", 0.45],
              ["Light gases", "Methane, hydrogen, ammonia: near the ceiling.", 0.93]]})
