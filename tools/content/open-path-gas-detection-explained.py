META = {
    "category": "gas-detection-guides",
    "title": "Open Path Gas Detection Explained: LEL.m, Range and Alarms",
    "keyword": "open path gas detection",
    "subtitle": "How an infrared beam detects flammable gas anywhere along its path, what an LEL.m reading means, and when open path detectors beat a row of point detectors",
    "meta_title": "Open Path Gas Detection Explained: LEL.m and Alarms",
    "meta_description": "Open path gas detection explained: infrared beam principle, LEL.m readings, path lengths, alarm settings, fault signals and how it compares with point sensors.",
    "summary": "How open path infrared detectors work, what LEL.m means, typical ranges and alarm levels, and where they fit compared with point gas detectors.",
    "card_title": "Open Path Gas Detection",
    "author": "SWME Technical Staff",
    "published": "2026-11-24",
    "status": "published",
    "sort_order": 8,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "compare",
        "title": "Point Detector vs Open Path Detector",
        "alt": "Infographic comparing point gas detectors and open path gas detectors on what they measure, units, coverage and strengths",
        "columns": [
            ["Point detector", ["Measures gas at one spot", "Reads in ppm or %LEL", "Gives a precise location", "Outdoors needs a weather shield, which slows response"]],
            ["Open path detector", ["Measures gas along a beam", "Reads in LEL.m or ppm.m", "Covers a line a few metres to hundreds of metres long", "Indicates the size of the gas cloud"]],
        ],
    },
}

_C = "#2b8a3e"
_T = "#1f6a2f"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_diag = (
    '<defs><marker id="aop" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="' + _C + '"/></marker></defs>'
    # transmitter
    + '<rect x="30" y="110" width="90" height="60" rx="8" fill="#495057"/>'
    + _t(75, 136, "Transmitter", 12, "700", "#fff")
    + _t(75, 154, "IR source", 11, "400", "#dee2e6")
    + '<rect x="65" y="170" width="20" height="90" fill="#868e96"/>'
    # receiver
    + '<rect x="680" y="110" width="90" height="60" rx="8" fill="#495057"/>'
    + _t(725, 136, "Receiver", 12, "700", "#fff")
    + _t(725, 154, "two bands", 11, "400", "#dee2e6")
    + '<rect x="715" y="170" width="20" height="90" fill="#868e96"/>'
    # gas cloud
    + '<ellipse cx="400" cy="140" rx="95" ry="58" fill="#ffe066" opacity="0.75"/>'
    + _t(400, 72, "Gas cloud", 13, "700", "#8a6d00")
    # beam
    + '<line x1="122" y1="140" x2="676" y2="140" stroke="' + _C + '" stroke-width="4" marker-end="url(#aop)"/>'
    + _t(210, 128, "Infrared beam", 12, "700", _T)
    # cloud width dimension
    + '<line x1="305" y1="215" x2="495" y2="215" stroke="#495057" stroke-width="1.5"/>'
    + '<line x1="305" y1="205" x2="305" y2="225" stroke="#495057" stroke-width="1.5"/>'
    + '<line x1="495" y1="205" x2="495" y2="225" stroke="#495057" stroke-width="1.5"/>'
    + _t(400, 240, "Cloud width on the beam: 2 m", 12, "700", "#495057")
    # path length dimension
    + '<line x1="75" y1="290" x2="725" y2="290" stroke="#495057" stroke-width="1.5"/>'
    + '<line x1="75" y1="280" x2="75" y2="300" stroke="#495057" stroke-width="1.5"/>'
    + '<line x1="725" y1="280" x2="725" y2="300" stroke="#495057" stroke-width="1.5"/>'
    + _t(400, 314, "Path length: 5 to 200 m for Searchline Excel, depending on model", 12, "700", "#495057")
    # reading box
    + '<rect x="200" y="330" width="400" height="52" rx="10" fill="#ecf8ee" stroke="' + _C + '" stroke-width="2"/>'
    + _t(400, 352, "50% LEL × 2 m = 1 LEL.m", 15, "700", _T)
    + _t(400, 372, "The same reading as 25% LEL over 4 m", 12, "400", "#555")
)

BODY = [
    takeaways([
        "An open path detector sends an infrared beam across an area and detects flammable gas anywhere along it.",
        "It reads the product of gas concentration and cloud width in LEL.m (also written LFL.m), not the concentration at one point.",
        "Honeywell's Searchline Excel reads 0 to 5 LEL.m with default alarms at 1 and 3 LEL.m, the same levels used in North Sea offshore systems.",
        "A reference wavelength lets the detector separate gas absorption from fog, rain and dirt on the optics.",
    ]),
    p("<strong>Open path gas detection</strong> covers a line through a plant instead of a single spot. It is widely used in petroleum and petrochemical plants to find flammable gas leaks quickly. SWME supplies " + link("/gas-detectors", "gas detectors") + " for plants in the UAE and GCC."),
    toc([("work", "How open path gas detection works"), ("units", "What LEL.m means"), ("specs", "Range, response and alarms"),
         ("compare", "Open path vs point detectors"), ("design", "Design and installation"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("work", "How Open Path Gas Detection Works"),
    p("The " + ext("https://en.wikipedia.org/wiki/Infrared_open_path_detector", "infrared open path detector article") + " describes two layouts. A transmitter and receiver sit at opposite ends of the path, or a combined unit sends the beam to a retroreflector and reads it on return. The beam is typically a few metres to a few hundred metres long.",
      "Flammable gas absorbs infrared at certain wavelengths. The detector also measures at one or more reference wavelengths that the gas does not absorb, and works out the gas from the ratio of the two signal losses. Rain and fog reduce the signal strength, and Honeywell says the double band pass filters in Searchline Excel fully compensate for fog, rain and mist. Common measuring wavelengths are 3.4 µm for hydrocarbons and 2.3 µm, where the response to many gases is fairly uniform in LEL terms. Modern units usually use a xenon flash tube as the source."),
    svg(_diag, "Open path detector: the receiver sees the total gas along the beam. A 2 m wide cloud at 50% LEL gives a reading of 1 LEL.m", 395),
    h2("units", "What LEL.m Means"),
    p("A point detector reads concentration in %LEL or ppm. An open path detector reads a path integral: concentration multiplied by the length of beam that passes through gas. The natural units are LEL.m (or LFL.m) for flammables and ppm.m for toxic gas. As the diagram shows, a cloud 2 m wide at 50% LEL and a cloud 4 m wide at 25% LEL both read 1 LEL.m.",
      "The reading therefore reflects the size of a release more than the concentration at any one place. Our guide to " + link("/lel-and-uel-explained", "LEL and UEL") + " explains the %LEL scale the reading is built on."),
    INFOGRAPHIC,
    h2("specs", "Range, Response and Alarms"),
    rows([
        ("Range", "0 to 5 LEL.m on a 4 to 20 mA output (Honeywell Searchline Excel)."),
        ("Alarms", "Low at 1 LEL.m and high at 3 LEL.m. The same levels, with 5 LEL.m full scale, are typical in North Sea offshore fire and gas systems."),
        ("Path length", "Short range 5 to 40 m, medium 40 to 120 m and long range 120 to 200 m."),
        ("Response", "T90 under 3 seconds in normal conditions."),
        ("Alignment", "Tolerates ±0.5° misalignment, about ±170 cm at 200 m on the long range model."),
        ("Gases", "Calibrated for methane, ethane, propane, butane, pentane, ethylene, propylene and butadiene."),
    ], "At a glance (Searchline Excel)"),
    p("Honeywell's " + ext("https://automation.honeywell.com/us/en/products/gas-and-flame-detection/fixed-gas-and-flame-detection/fixed-gas-detectors/searchline-excel-open-path-infrared-gas-detector", "Searchline Excel product page") + " also lists special loop currents: 2 mA for a fault, 2.5 mA for a blocked beam, 3 mA for dirty optics and 21 mA for over range. To check what the DCS should show for a loop current between 4 and 20 mA, the " + ext("https://zentacalculator.com/engineering/4-20ma-scaling/", "4 to 20 mA scaling calculator") + " converts it to LEL.m on a 0 to 5 range."),
    dyk("Searchline, from Sieger Zellweger and later Honeywell, was the first open path detector certified for hazardous areas. The 2001 PLMS Pulsar was the first to monitor the alignment of its transmitter and receiver."),
    h2("compare", "Open Path vs Point Detectors"),
    twocol([
        ("Where open path helps", "bi-arrows-expand", [
            "Outdoors, where a gas cloud moves in ways you cannot predict.",
            "Along a pipeline or around a plant perimeter, where it can cost less than a row of point detectors.",
            "Honeywell lists wider coverage, no blocked gas path to the sensor and detector location being less critical.",
        ]),
        ("Where point detectors help", "bi-geo-alt", [
            "They give a precise location of the gas.",
            "They give the concentration at one spot.",
            "An open path principles paper notes that point detectors are more reliable in extreme weather.",
        ]),
    ]),
    p("One open path detector usually costs more than one point detector, and that toxic gas such as H₂S is possible in principle but not yet widely adopted. For H₂S, see our " + link("/h2s-gas-detection-basics", "H2S gas detection basics") + "; for point sensor options, see " + link("/types-of-gas-sensors", "types of gas sensors") + "."),
    h2("design", "Design and Installation"),
    checklist([
        ("Plan the beam routes", "Open path suits pipelines and plant perimeters, where a row of point detectors would otherwise be needed. Our " + link("/gas-detector-placement-guide", "gas detector placement guide") + " covers how gas density affects mounting height."),
        ("Pick the range model", "Choose short, medium or long range to match the distance between the two units."),
        ("Mount on rigid structures", "Alignment tolerance is ±0.5°, so the mounts must not move."),
        ("Check the certification", "Confirm the hazardous area approvals, such as ATEX or " + ext("https://www.iecex.com/", "IECEx") + ", and performance testing to IEC 60079 29 4."),
        ("Wire the fault states", "Make sure the DCS shows beam block and dirty optics, not just gas alarms. Our blog on " + link("/blog/vanguard-wireless-hart-gas-detector-uae", "wireless gas detectors") + " shows another way to get signals back from remote areas."),
    ]),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Reading LEL.m as %LEL.", "1 LEL.m can be a thin rich cloud or a wide lean one. It is not a concentration."),
        ("Ignoring the 2.5 mA signal.", "A blocked beam means the path is not protected until it clears."),
        ("Expecting a location.", "The detector shows gas somewhere on the beam, not where. Add point detectors where you need to know."),
    ]),
    p("For more on analyser and gas sensing principles, see the " + ext("https://www.instrumentationblog.in/category/process-instrumentation/analytical-measurements/", "analytical measurement articles") + "."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What does open path gas detection measure?", "The total gas along the beam, as concentration times cloud width, in LEL.m or ppm.m."),
        ("What alarm levels are typical?", "Low at 1 LEL.m and high at 3 LEL.m on a 0 to 5 LEL.m range."),
        ("Does fog stop an open path detector?", "Honeywell says Searchline Excel fully compensates for fog, rain and mist, and it sends 2.5 mA when the beam is blocked."),
    ]),
]
