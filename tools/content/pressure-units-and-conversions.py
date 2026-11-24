META = {
    "category": "pressure-measurement-guides",
    "title": "Pressure Units and Conversions Explained: Pa, bar, psi and More",
    "keyword": "pressure units",
    "subtitle": "What the pascal, bar, psi, atmosphere, torr and water column units mean, which conversion factors are exact, and how to convert between them without mistakes",
    "meta_title": "Pressure Units and Conversions: Pa, bar, psi Explained",
    "meta_description": "Pressure units explained: pascal, bar, psi, atm, torr, inches of water and kgf/cm2, with NIST conversion factors, worked examples and common mistakes.",
    "summary": "The pressure units you meet on gauges and datasheets, the NIST factors that convert them to pascals, and a simple method for converting any unit to any other.",
    "card_title": "Pressure Units and Conversions",
    "author": "SWME Technical Staff",
    "published": "2026-11-24",
    "status": "published",
    "sort_order": 8,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "grid",
        "title": "Four Pressure Units to Know",
        "alt": "Infographic showing the pascal, bar, psi and standard atmosphere with their values in pascals",
        "steps": [
            ["Pascal (Pa)", "One newton per square metre. The SI unit of pressure."],
            ["bar", "Exactly 100 000 Pa, the same as 100 kPa or 0.1 MPa."],
            ["psi", "One pound force per square inch, 6894.757 Pa in NIST's table."],
            ["Standard atmosphere", "Exactly 101 325 Pa, about 14.70 psi."],
        ],
    },
}

_C = "#5f3dc4"
_T = "#3b2a8c"
_BG = "#f3f0ff"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_units = [
    (130, 70, "1 bar", "100 000 Pa"),
    (400, 50, "1 atm", "101 325 Pa"),
    (670, 70, "1 psi", "6894.757 Pa"),
    (130, 290, "1 kgf/cm²", "98 066.5 Pa"),
    (400, 310, "1 torr", "133.3224 Pa"),
    (670, 290, "1 inH₂O", "249.0889 Pa"),
]


def _hub():
    out = []
    for x, y, name, val in _units:
        out.append(f'<line x1="400" y1="180" x2="{x}" y2="{y}" stroke="{_C}" stroke-width="2" stroke-dasharray="5 4"/>')
    for x, y, name, val in _units:
        out.append(f'<rect x="{x - 95}" y="{y - 30}" width="190" height="60" rx="10" fill="{_BG}" stroke="{_C}" stroke-width="2"/>')
        out.append(_t(x, y - 6, name, 15, "700", _T))
        out.append(_t(x, y + 16, val, 13, "400", "#333"))
    out.append('<circle cx="400" cy="180" r="62" fill="' + _C + '"/>')
    out.append(_t(400, 176, "Pascal", 18, "700", "#fff"))
    out.append(_t(400, 198, "1 Pa = 1 N/m²", 12, "400", "#fff"))
    return "".join(out)


BODY = [
    takeaways([
        "The pascal (one newton per square metre) is the SI unit; bar, psi, atm and the liquid column units are all defined against it.",
        "NIST marks the bar (100 000 Pa), the standard atmosphere (101 325 Pa) and the kgf/cm² (98 066.5 Pa) as exact conversion factors.",
        "Inches of water and millimetres of mercury depend on the liquid's reference temperature, so check which basis a datasheet uses.",
        "Convert through pascals: multiply by the factor for the unit you have, then divide by the factor for the unit you want.",
    ]),
    p("A pressure gauge dial in bar, a pump curve in psi and a draft gauge in inches of water may all show up in the same plant. Getting <strong>pressure units</strong> right matters when you specify a range on a purchase order. SWME supplies "
      + link("/pressure-gauges", "pressure gauges") + " and " + link("/pressure-transmitters", "pressure transmitters") + " with dials and ranges in the unit your site uses."),
    toc([("pascal", "The pascal and the SI system"), ("common", "Common pressure units"), ("convert", "How to convert pressure units"),
         ("column", "Liquid column units"), ("specify", "Specifying units on instruments"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("pascal", "The Pascal and the SI System"),
    p("NIST Special Publication 811 defines the pascal as one newton per square metre. It is a small unit, so plants use kilopascals and megapascals: 1 kPa is 1000 Pa and 1 MPa is 1 000 000 Pa. The same publication lists the bar (10⁵ Pa) under units in use temporarily with the SI. It says these units should not be introduced where they are not already used.",
      "The " + ext("https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication811e1991.pdf", "NIST guide to SI units") + " also has rules for writing values: a space between number and symbol (150 kPa), no plural s on a symbol, and no full stop after it except at the end of a sentence."),
    h2("common", "Common Pressure Units"),
    INFOGRAPHIC,
    table(["Unit", "Value in pascals", "Exact?", "Where you see it"],
          [["bar", "100 000", "Yes", "Gauges and transmitters in Europe, the Middle East and Asia"],
           ["millibar (mbar)", "100", "Yes, by definition of the bar", "Low pressure, draft and weather"],
           ["psi (lbf/in²)", "6894.757", "No", "US equipment, pumps, compressors"],
           ["standard atmosphere (atm)", "101 325", "Yes", "Reference conditions, vacuum"],
           ["kgf/cm²", "98 066.5", "Yes", "Older gauges and Asian datasheets"],
           ["torr (mm Hg at 0 °C)", "133.3224", "No", "Vacuum"],
           ["inch of mercury (inHg)", "3386.389", "No", "Vacuum gauges, barometers"],
           ["inch of water (inH₂O)", "249.0889", "No", "Draft, filters, HVAC and low DP"]]),
    p("The values come from the " + ext("https://nist.gov/pml/owm/metric-si/unit-conversion/pressure-and-gas-flow-unit-conversions", "NIST pressure unit conversion table") + ", and NIST SP 811 marks the exact ones with an asterisk. The " + ext("https://www.omega.co.uk/techref/techdata.html", "Omega pressure conversion data") + " gives the same factors to four figures, for example 1 psi = 703.1 mm H₂O."),
    h2("convert", "How to Convert Pressure Units"),
    p("Every factor in the table is a value in pascals, so pascals work as a hub. Multiply your reading by the factor for its unit to get pascals, then divide by the factor for the unit you want."),
    svg(_hub(), "Pascals as the hub: each unit's value in pascals is its conversion factor. Convert to pascals first, then to the unit you need", 360),
    rows([
        ("10 bar to psi", "10 × 100 000 = 1 000 000 Pa; 1 000 000 ÷ 6894.757 = 145.04 psi."),
        ("150 psi to bar", "150 × 6894.757 = 1 034 214 Pa; ÷ 100 000 = 10.34 bar."),
        ("1 atm to bar", "101 325 ÷ 100 000 = 1.01325 bar, or 14.696 psi."),
        ("1 kgf/cm² to bar", "98 066.5 ÷ 100 000 = 0.980665 bar. Close to 1 bar, but not equal."),
        ("25 mbar to inH₂O", "25 × 100 = 2500 Pa; ÷ 249.0889 = 10.04 inH₂O."),
    ], "Worked examples"),
    p("To see what a pressure means as a column of liquid, the " + ext("https://zentacalculator.com/engineering/pressure-to-head/", "pressure to head calculator") + " works out the height of liquid that a given pressure supports, which helps when you set a level transmitter range. The "
      + ext("https://instrumentationblog.in/calculators/pressure/", "pressure calculator collection") + " covers other unit and range sums."),
    dyk("A kgf/cm² is 0.980665 bar, so the two are about 2% apart. At the top of a 0 to 16 range the gap is about 0.31 bar, so a gauge marked in one cannot stand in for the other."),
    h2("column", "Liquid Column Units"),
    p("Inches of water and millimetres of mercury describe pressure as the height of a liquid column, and the liquid's density changes with temperature. Omega labels its factors \"inch of water at 4 °C\" and \"mm of mercury at 0 °C\". NIST SP 811 lists the inch of water at 39.2 °F (249.082 Pa) and at 60 °F (248.84 Pa) as separate units. The difference is under 0.1%, which matters only for precise low pressure work such as calibrating a draft gauge.",
      "The " + ext("https://www.instrumentationblog.in/hydrostatic-pressure-formula/", "hydrostatic pressure formula") + " shows where these units come from: pressure equals density times gravity times height. The " + ext("https://zentacalculator.com/engineering/manometer/", "manometer calculator") + " gives the pressure difference for a manometer reading in your fluid."),
    h2("specify", "Specifying Units on Instruments"),
    checklist([
        ("Say gauge or absolute", "psi alone does not say whether the reading starts from atmosphere or from vacuum. Omega's altitude table gives 14.70 psia at sea level. Our guide to " + link("/gauge-vs-absolute-vs-differential-pressure", "gauge, absolute and differential pressure") + " explains the three references."),
        ("Use one unit per site", "Match the unit already on the P&amp;ID and in the DCS so operators do not convert in their heads."),
        ("Ask for dual scales where needed", "A dial in bar and psi helps when equipment comes from different countries."),
        ("State the reference temperature for water columns", "Write inH₂O at 4 °C or at 60 °F when the range is small."),
        ("Check the transmitter's engineering units", "The 4 to 20 mA range must be set in the same unit as the DCS scaling. The " + ext("https://zentacalculator.com/engineering/absolute-gauge-pressure/", "absolute and gauge pressure calculator") + " converts between the two references when a datasheet uses the other one."),
    ]),
    p("For help choosing a range, see " + link("/how-to-select-a-pressure-gauge", "how to select a pressure gauge") + ". SWME also supplies " + link("/digital-pressure-gauges", "digital pressure gauges") + " alongside dial gauges."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Treating kgf/cm² as bar.", "They differ by about 2%, as the worked example above shows."),
        ("Leaving out the g or a.", "A range of 0 to 10 psi could be gauge or absolute; the order must say which."),
        ("Rounding the factor too early.", "Using 14.5 psi per bar instead of 14.504 adds a small error that grows on high ranges."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Is bar an SI unit?", "No. NIST SP 811 lists it as a unit in use temporarily with the SI. It equals exactly 100 000 Pa."),
        ("How many psi are in one bar?", "100 000 ÷ 6894.757 gives 14.504 psi per bar."),
        ("Why do inches of water have more than one value?", "The value depends on the water temperature used as the reference, such as 4 °C (39.2 °F) or 60 °F."),
    ]),
]
