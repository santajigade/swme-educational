META = {
    "category": "gas-detection-guides",
    "title": "Bump Test vs Calibration for Gas Detectors",
    "keyword": "bump test",
    "subtitle": "What a bump test proves, what a calibration adjusts and how often each one is needed",
    "meta_title": "Bump Test vs Calibration for Gas Detectors Explained",
    "meta_description": "Bump test vs calibration for gas detectors: definitions, daily checks, intervals, pass limits, what to do after a failure and common mistakes to avoid.",
    "summary": "The difference between a bump test, a calibration check and a full calibration, and how often each is needed.",
    "card_title": "Bump Test vs Calibration",
    "author": "SWME Technical Staff",
    "published": "2026-11-18",
    "status": "published",
    "sort_order": 4,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "compare",
        "title": "Bump Test vs Calibration",
        "alt": "Infographic comparing a gas detector bump test with a full calibration",
        "steps": [
            ["Bump test", "Short exposure to test gas that proves sensors respond and alarms work."],
            ["Full calibration", "Adjusts the sensor reading to match a known, traceable gas concentration."],
        ],
        "columns": [
            ["Bump test", ["Qualitative function check", "Proves sensors and alarms respond", "No adjustment is made", "Takes a few minutes"]],
            ["Full calibration", ["Quantitative adjustment", "Matches reading to known gas", "Done to the maker's method", "Needed after a failed bump test"]],
        ],
    },
}

_C = "#2b8a3e"


def _box(x, y, w, h, text, fill="#ecf8ee", stroke=_C, sub=None):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
    ty = y + h / 2 + (0 if sub else 5)
    out += f'<text x="{x + w / 2}" y="{ty:.0f}" text-anchor="middle" font-size="14" font-weight="700" fill="#1f6a2f">{text}</text>'
    if sub:
        out += f'<text x="{x + w / 2}" y="{ty + 18:.0f}" text-anchor="middle" font-size="12" fill="#555">{sub}</text>'
    return out


def _arrow(x1, y1, x2, y2, label=None, lx=None, ly=None):
    out = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#495057" stroke-width="2" marker-end="url(#ahg)"/>'
    if label:
        out += f'<text x="{lx}" y="{ly}" font-size="13" font-weight="700" fill="#495057">{label}</text>'
    return out


_diag = (
    '<defs><marker id="ahg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="#495057"/></marker></defs>'
    + _box(20, 40, 170, 60, "Before use", sub="each day")
    + _arrow(190, 70, 238, 70)
    + _box(240, 40, 170, 60, "Bump test", sub="test gas, alarms")
    + _arrow(410, 70, 458, 70)
    + '<polygon points="530,30 600,70 530,110 460,70" fill="#fff9db" stroke="#f59f00" stroke-width="2"/>'
    + '<text x="530" y="75" text-anchor="middle" font-size="14" font-weight="700" fill="#a35400">Pass?</text>'
    + _arrow(600, 70, 638, 70, "Yes", 604, 60)
    + _box(640, 40, 140, 60, "Use detector", fill="#d3f9d8")
    + _arrow(530, 110, 530, 168, "No", 538, 145)
    + _box(430, 170, 200, 60, "Full calibration", sub="traceable gas")
    + _arrow(530, 230, 530, 278)
    + '<polygon points="530,280 600,320 530,360 460,320" fill="#fff9db" stroke="#f59f00" stroke-width="2"/>'
    + '<text x="530" y="325" text-anchor="middle" font-size="14" font-weight="700" fill="#a35400">Pass?</text>'
    + _arrow(600, 320, 710, 320, "Yes", 620, 310)
    + '<line x1="710" y1="320" x2="710" y2="102" stroke="#495057" stroke-width="2" marker-end="url(#ahg)"/>'
    + _arrow(460, 320, 312, 320, "No", 420, 310)
    + _box(110, 290, 200, 60, "Remove from service", fill="#ffe3e3", stroke="#c92a2a")
)

BODY = [
    takeaways([
        "A bump test is a quick qualitative check that sensors respond and alarms work; it makes no adjustment.",
        "A full calibration adjusts the reading to match a known, traceable gas concentration.",
        "Guidance calls for a bump test or calibration check before each day's use of portable detectors.",
        "A detector that fails a bump test must be fully calibrated, or removed from service.",
    ]),
    p("A gas detector that looks fine can still be blind. Sensors age, drift and can be poisoned, and nothing on the display shows it. A <strong>bump test</strong> and a calibration are the two routine checks that catch this, but they answer different questions.",
      "This guide explains each check, how often to do them and what to do when a detector fails. SWME supplies fixed and portable " + link("/gas-detectors", "gas detectors") + " and " + link("/test-calibration", "test and calibration equipment") + " across the GCC."),
    toc([("terms", "Bump test vs calibration: the terms"), ("compare", "Side by side"), ("frequency", "How often to test"),
         ("fail", "When a detector fails"), ("tips", "Good practice checklist"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("terms", "Bump Test vs Calibration: The Terms"),
    p("" + ext("https://instrumentationtools.com/bump-testing", "Instrumentation Tools") + " summarises the definitions used in OSHA guidance on verifying direct reading portable gas monitors:"),
    rows([
        ("Bump test", "A qualitative function check. The sensors are exposed to a challenge gas high enough to activate at least the low alarm. It confirms that gas reaches the sensors, that they respond, that response time is normal and that alarms work."),
        ("Calibration check", "A quantitative test with a traceable, known gas concentration, to confirm the reading falls within the manufacturer's limits."),
        ("Full calibration", "Adjusting the instrument response to match a known, traceable gas concentration, by the method the manufacturer sets."),
        ("Zero", "Setting the sensors to read zero in clean air. If the air is not clean, every later reading is offset."),
    ]),
    h2("compare", "Side by Side"),
    INFOGRAPHIC,
    table(["Point", "Bump test", "Full calibration"],
          [["Purpose", "Proves response and alarms", "Corrects reading accuracy"],
           ["Result", "Pass or fail", "Sensor adjusted to known gas"],
           ["Adjustment", "None", "Yes"],
           ["Time", "A few minutes", "Considerably longer"],
           ["When", "Before each day's use", "Maker's schedule, and after a failed test"]]),
    p("The timing points come from " + ext("https://www.ishn.com/articles/91365-dont-hesitate-to-calibrate", "ISHN") + ", which notes that a bump test can take as little as a few minutes while a full calibration through the instrument menu takes considerably longer."),
    h2("frequency", "How Often to Test"),
    p("ISHN quotes the ISEA position: a bump test or full calibration of direct reading portable gas monitors should be made before each day's use. Instrumentation Tools adds that less frequent checks may be allowed only after at least 10 days of daily checks in the intended atmosphere with no adjustments needed, and the interval should not exceed 30 days."),
    rows([
        ("New detector", "Bump test or calibrate before first use, since shipping can cause damage."),
        ("Harsh conditions", "Test more often where sensor poisons or harsh environments are suspected."),
        ("After a knock", "Recalibrate after a drop, damage or servicing."),
        ("Confined space entry", "ISHN cites OSHA 1910.146, which requires testing with a calibrated instrument for oxygen, then flammable gases, then toxic contaminants."),
    ]),
    dyk("Sensors do not last forever. ISHN gives a typical sensor life of two to three years, and notes that drift does not happen at predictable intervals, which is why the check is daily rather than yearly. For sensor types, read " + link("/types-of-gas-sensors", "types of gas sensors") + "."),
    h2("fail", "When a Detector Fails"),
    p("An instrument that fails a bump test or calibration check must be fully calibrated before further use, or taken out of service. As an example of a pass limit, Instrumentation Tools describes a tolerance of plus or minus 10%: with 20 ppm H2S test gas, the reading must settle between 18 and 22 ppm. Manufacturers set their own limits, so always use the value in the manual. The " + ext("https://zentacalculator.com/engineering/calibration-error/", "calibration error calculator") + " helps you work out the error as a percentage."),
    svg(_diag, "Daily bump test and calibration decision flow for a portable gas detector", 370),
    h2("tips", "Good Practice Checklist"),
    checklist([
        ("Use certified gas", "Use calibration gas certified to a traceable standard and never past its expiry date."),
        ("Zero in clean air", "Zero only where the air is known to be clean."),
        ("Clear the peaks", "Bump tests and calibrations record new peak readings, so clear peaks afterwards."),
        ("Keep records", "Log every bump test and calibration with date, gas and result."),
        ("Know your alarms", "Set alarm levels with " + link("/lel-and-uel-explained", "LEL and UEL") + " in mind for flammable gas."),
    ]),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Treating a bump test as a calibration.", "A bump test proves response, not accuracy, and makes no adjustment."),
        ("Skipping the daily check.", "Drift is not predictable, so a detector can fail between scheduled calibrations."),
        ("Using expired gas.", "Old or uncertified gas can pass a bad sensor or fail a good one."),
    ]),
    p("For response checks, the " + ext("https://zentacalculator.com/engineering/sensor-response-time/", "sensor response time calculator") + " is useful, and " + ext("https://www.instrumentationblog.in/category/process-instrumentation/calibration/", "Instrumentation Blog") + " has more calibration reading. For wireless fixed detectors, see our " + link("/blog/vanguard-wireless-hart-gas-detector-uae", "Vanguard WirelessHART gas detector") + " post."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What is a bump test?", "A short exposure to test gas that proves the sensors respond and the alarms activate. It does not adjust the reading."),
        ("How often should a gas detector be bump tested?", "Industry guidance calls for a bump test or calibration before each day's use of portable detectors."),
        ("What happens if a bump test fails?", "The detector must be fully calibrated before further use, or removed from service."),
    ]),
]
