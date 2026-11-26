META = {
    "category": "pressure-measurement-guides",
    "title": "How to Calibrate a Pressure Gauge: Step by Step",
    "keyword": "pressure gauge calibration",
    "subtitle": "The reference equipment you need, the test points to run up and down, how to read the error as a percent of span, how to adjust zero, span and linearity, and how often to check",
    "meta_title": "How to Calibrate a Pressure Gauge: Step by Step",
    "meta_description": "Pressure gauge calibration step by step: deadweight tester or comparator, the 4:1 rule, ASME grades, test points up and down, hysteresis and adjustment.",
    "summary": "How to calibrate a pressure gauge against a deadweight tester or reference gauge, run test points up and down, work out the error and adjust the movement.",
    "card_title": "How to Calibrate a Pressure Gauge",
    "author": "SWME Technical Staff",
    "published": "2026-11-26",
    "status": "published",
    "sort_order": 9,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "flow",
        "title": "Pressure Gauge Calibration Sequence",
        "alt": "Infographic of the pressure gauge calibration sequence: exercise the gauge, take readings going up, take readings coming down, then adjust and repeat",
        "steps": [
            ["Exercise", "Apply full scale for a minute, vent, wait a minute. Repeat 2 to 3 times."],
            ["Go up", "Set the pointer exactly on the 25, 50, 75 and 100% marks and read the reference."],
            ["Come down", "Check 75, 50 and 25% on the way down to find hysteresis."],
            ["Adjust, repeat", "Correct zero, span or linearity, then run all points again."],
        ],
    },
}

_C = "#5f3dc4"
_T = "#3b2a8c"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


def _dial(cx, cy, r):
    ticks = ""
    import math
    for k in range(11):
        a = math.radians(225 - k * 27)
        x1, y1 = cx + (r - 4) * math.cos(a), cy - (r - 4) * math.sin(a)
        x2, y2 = cx + (r - 11) * math.cos(a), cy - (r - 11) * math.sin(a)
        ticks += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#495057" stroke-width="1.5"/>'
    a = math.radians(225 - 5 * 27)
    nx, ny = cx + (r - 14) * math.cos(a), cy - (r - 14) * math.sin(a)
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="#495057" stroke-width="3"/>' + ticks
            + f'<line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="#c92a2a" stroke-width="3"/>'
            + f'<circle cx="{cx}" cy="{cy}" r="4" fill="#495057"/>')


_diag = (
    # pump / comparator body
    '<rect x="60" y="250" width="200" height="60" rx="8" fill="#f3f0ff" stroke="#5f3dc4" stroke-width="2.5"/>'
    + '<rect x="260" y="268" width="70" height="24" fill="#e5dbff" stroke="#5f3dc4" stroke-width="2"/>'
    + '<line x1="330" y1="280" x2="372" y2="280" stroke="#5f3dc4" stroke-width="4"/>'
    + '<line x1="372" y1="258" x2="372" y2="302" stroke="#5f3dc4" stroke-width="6" stroke-linecap="round"/>'
    + _t(160, 276, "Hand pump or", 13) + _t(160, 294, "comparator", 13)
    + _t(350, 330, "Screw press for", 12, "400", "#555") + _t(350, 345, "fine adjustment", 12, "400", "#555")
    # manifold
    + '<line x1="160" y1="250" x2="160" y2="215" stroke="#495057" stroke-width="5"/>'
    + '<line x1="100" y1="215" x2="560" y2="215" stroke="#495057" stroke-width="5"/>'
    # vent valve
    + '<line x1="100" y1="215" x2="100" y2="190" stroke="#495057" stroke-width="5"/>'
    + '<polygon points="88,170 112,170 100,190" fill="#ffe8cc" stroke="#d9480f" stroke-width="2"/>'
    + '<polygon points="88,150 112,150 100,170" fill="#ffe8cc" stroke="#d9480f" stroke-width="2"/>'
    + _t(100, 140, "Vent", 12, "700", "#d9480f")
    # reference gauge (lower)
    + '<line x1="330" y1="215" x2="330" y2="170" stroke="#495057" stroke-width="5"/>'
    + '<rect x="285" y="110" width="90" height="60" rx="8" fill="#e7f5ff" stroke="#1864ab" stroke-width="2.5"/>'
    + '<rect x="297" y="122" width="66" height="26" fill="#fff" stroke="#1864ab"/>'
    + _t(330, 141, "5.000", 15, "700", "#1864ab")
    + _t(330, 82, "Reference gauge", 13, "700", "#1864ab")
    + _t(330, 99, "at least 4 times more accurate", 12, "400", "#555")
    # gauge under test (higher)
    + '<line x1="560" y1="215" x2="560" y2="125" stroke="#495057" stroke-width="5"/>'
    + _dial(560, 80, 42)
    + _t(660, 70, "Gauge", 13, "700", _C, "start") + _t(660, 86, "under test", 13, "700", _C, "start")
    # height difference
    + '<line x1="390" y1="170" x2="520" y2="170" stroke="#868e96" stroke-dasharray="5,4"/>'
    + '<line x1="470" y1="125" x2="540" y2="125" stroke="#868e96" stroke-dasharray="5,4"/>'
    + '<line x1="480" y1="129" x2="480" y2="166" stroke="#c92a2a" stroke-width="2" marker-start="url(#hb)" marker-end="url(#hb)"/>'
    + '<defs><marker id="hb" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#c92a2a"/></marker></defs>'
    + _t(462, 152, "h", 15, "700", "#c92a2a", "end")
    + _t(600, 270, "Head error = ρ g h", 14, "700", "#c92a2a")
    + _t(600, 290, "Water, h = 1 m: about 9.8 kPa", 12, "400", "#555")
    + _t(600, 306, "(98 mbar)", 12, "400", "#555")
)

BODY = [
    takeaways([
        "Use a reference at least 4 times more accurate than the gauge you are checking, the traditional 4:1 test uncertainty ratio.",
        "Exercise the gauge, then read at least 3 to 5 points going up and the same points coming down, so hysteresis shows.",
        "Work the error out as a percent of span and compare it with the ASME B40.100 grade: a Grade 1A gauge must stay within ±1% of span.",
        "Correct for any height difference when the test medium is a liquid. One metre of water is about 98 mbar.",
    ]),
    p("<strong>Pressure gauge calibration</strong> means comparing the gauge with a more accurate reference at known pressures, recording the error, and adjusting the movement if the error is outside the gauge's accuracy grade. SWME supplies " + link("/pressure-gauges", "pressure gauges") + " and the " + link("/test-calibration", "test and calibration equipment") + " used to check them, including hand pumps and reference gauges."),
    toc([("equipment", "Reference equipment and the 4:1 rule"), ("grades", "Accuracy grades"), ("procedure", "Pressure gauge calibration step by step"),
         ("adjust", "Adjusting zero, span and linearity"), ("example", "Worked example"), ("head", "Test medium and head correction"),
         ("interval", "Calibration interval"), ("faults", "Troubleshooting"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("equipment", "Reference Equipment and the 4:1 Rule"),
    p("Fluke's comparison of " + ext("https://www.fluke.com/en-us/learn/blog/pressure-calibration/pressure-comparators-and-digital-reference-pressure-gauges-vs-deadweight-testers", "deadweight testers and pressure comparators") + " describes the two common setups. A deadweight tester generates, controls and measures pressure from force over area, and the pressure is typically known to 0.025% or better, with 0.015% models available. Its masses must be adjusted for local gravity if the tester moves to another site, and loading them is slow and can be done wrong.",
      "A comparator has two ports, one for the reference gauge and one for the device under test. It is easier to use and usually cheaper, but less accurate than a deadweight tester, and the pressure needs time to settle after each change. Either way, Fluke gives the traditional requirement as a 4:1 test uncertainty ratio. For example, its 700G digital reference gauge is rated 0.05% of scale and the 2700G 0.02% of scale, so both are good references for a 1% gauge. The same check applies if one of SWME's " + link("/digital-pressure-gauges", "digital pressure gauges") + " is used as the reference."),
    twocol([
        ("Deadweight tester", "bi-box-seam", ["Pressure from known masses on a known piston area", "Typically 0.025% or better", "Masses corrected for local gravity", "Slower, and masses can be loaded wrongly"]),
        ("Comparator with reference gauge", "bi-speedometer2", ["Two ports: reference and gauge under test", "Easier to use, usually cheaper", "Accuracy set by the reference gauge", "Let pressure settle after each change"]),
    ]),
    h2("grades", "Accuracy Grades"),
    p("You cannot call a gauge in or out of tolerance without its grade. Ashcroft's page on " + ext("https://blog.ashcroft.com/what-are-asme-accuracy-grades-for-mechanical-pressure-gauges", "ASME accuracy grades for mechanical gauges") + " lists the B40.100 grades, all as a percent of span. The last column is our arithmetic for a 0 to 10 bar gauge."),
    table(["ASME B40.100 grade", "Accuracy, % of span", "On a 0 to 10 bar gauge"], [
        ["4A", "±0.1% over the full dial", "±0.01 bar"],
        ["3A", "±0.25% over the full dial", "±0.025 bar"],
        ["2A", "±0.5% over the full dial", "±0.05 bar"],
        ["1A", "±1% over the full dial", "±0.1 bar"],
        ["A", "±1% in the middle, ±2% at the ends", "±0.1 bar middle, ±0.2 bar ends"],
        ["B", "Between ±2% and ±3%", "±0.2 to ±0.3 bar"],
    ]),
    p("Beamex adds that B40.100 classes run from 0.1 to 5% and EN 837 classes from 0.1 to 4%, so a class 1 gauge of 0 to 100 psi is good to ±1 psi. Our guide on " + link("/how-to-select-a-pressure-gauge", "how to select a pressure gauge") + " covers choosing the grade in the first place."),
    h2("procedure", "Pressure Gauge Calibration Step by Step"),
    p("The setup below is a comparator with the reference and the gauge under test on one manifold. Beamex's list of " + ext("https://blog.beamex.com/how-to-calibrate-pressure-gauges", "pressure gauge calibration tips") + " and Reotemp's " + ext("https://reotemp.com/wp-content/uploads/2015/12/CPGINSTR-0105.pdf", "gauge calibration procedure") + " give the sequence."),
    svg(_diag, "Comparator setup for pressure gauge calibration. Any height h between the reference and the gauge under test adds a head error when the medium is a liquid", 360),
    INFOGRAPHIC,
    checklist([
        ("Mount the gauge as it is used", "Usually vertical. Beamex says a 5 degree change in position should not shift the reading by more than half the accuracy class."),
        ("Leak test", "Pressurise, let the pressure stabilise, and watch for a drop before you take readings."),
        ("Exercise the movement", "Apply the maximum pressure for a minute, vent and wait a minute, two or three times."),
        ("Read going up", "Reotemp applies 25, 50, 75 and 100%. Adjust the pressure until the pointer sits exactly on a mark, look straight at the dial, and tap the case lightly to settle the pointer before you read the reference."),
        ("Read coming down", "Reduce pressure slowly and check 75, 50 and 25%. With a hand pump, do not overshoot a point and come back, or the hysteresis result is lost."),
        ("Record and decide", "Note every error as found, adjust if needed, then repeat the full run and record the results as left."),
    ]),
    p("The difference between the up and down readings at one point is the hysteresis. Beamex's note on " + ext("https://blog.beamex.com/hysteresis-in-pressure-calibration", "hysteresis in pressure calibration") + " gives an example: 49.95 kPa rising and 50.05 kPa falling at the 50 kPa point, which is 0.10 kPa of hysteresis."),
    h2("adjust", "Adjusting Zero, Span and Linearity"),
    p("Reotemp's procedure gives the adjustments for a Bourdon tube movement, in this order:"),
    rows([
        ("Zero", "If the gauge has a stop pin, set the pointer at 10% with 10% pressure applied. With no stop pin, set the pointer at zero with no pressure."),
        ("Span", "Move the full scale slide. If the reference reads higher than the gauge, reduce the distance between pushrod and shaft; if it reads lower, increase it."),
        ("Linearity", "Adjust the pushrod length. If the reference reads higher than the gauge, lengthen the pushrod; if lower, shorten it. Repeat until every point is within limits."),
    ], "Adjustments on a mechanical gauge (Reotemp)"),
    h2("example", "Worked Example"),
    p("Take a 0 to 10 bar Grade 1A gauge, so the tolerance is ±0.1 bar. At a reference of 5.00 bar it reads 5.06 bar going up. The error is 0.06 bar, which is 0.6% of span and uses 60% of the tolerance, so this point passes. On the way down it reads 5.09 bar, so the hysteresis at that point is 0.03 bar, or 0.3% of span. The " + ext("https://zentacalculator.com/engineering/five-point-calibration/", "five point calibration table") + " gives the 25, 50 and 75% test pressures for any range, and the calculator below works out the error as a percent of span and how much of the tolerance it uses, from the range, the reference value and the reading."),
    '<div class="my-4"><iframe src="https://zentacalculator.com/embed/engineering/calibration-error/" title="Calibration Error Calculator" width="100%" height="640" loading="lazy" style="border:1px solid #e2e5ee;border-radius:12px;max-width:720px;"></iframe>'
    '<p>' + ext("https://zentacalculator.com/engineering/calibration-error/", "Calibration Error Calculator") + ' by ' + ext("https://zentacalculator.com/", "Zenta Calculator") + '</p></div>',
    h2("head", "Test Medium and Head Correction"),
    p("Beamex says low pressure gauges are practical to calibrate with air or gas, while for higher pressure a liquid is more practical and safer. With a liquid, any height difference between the reference and the gauge adds a pressure of ρgh. For water, a 1 m difference causes an error of 9.8 kPa, which is 98 mbar or 1.42 psi."),
    dyk("On a 0 to 10 bar Grade 1A gauge the whole tolerance is ±0.1 bar, or 100 mbar. A 1 m height difference with water, at 98 mbar, would use almost all of it, so put the reference and the gauge at the same height or correct the readings."),
    p("More " + ext("https://www.instrumentationblog.in/category/process-instrumentation/calibration/", "calibration procedures for field instruments") + " cover transmitters and switches, and the " + ext("https://instrumentationblog.in/calculators/calibration/", "calibration calculators") + " help with error and tolerance sums."),
    h2("interval", "Calibration Interval"),
    p("Ashcroft's note on " + ext("https://blog.ashcroft.com/pressure-gauge-calibration-interval", "pressure gauge calibration intervals") + " suggests a check once every 12 months, with shorter intervals for high vibration, pulsation or rapid cycling. The end user sets the interval, not a standards body. Recalibrate at once if the pointer is not at zero or sits outside the zero box."),
    h2("faults", "Troubleshooting"),
    p("Some faults found during pressure gauge calibration come from the service rather than the movement. WIKA lists " + ext("https://blog.wika.com/us/knowhow/8-common-reasons-for-pressure-gauge-failure/", "common reasons for pressure gauge failure") + ":"),
    table(["What you see", "Likely cause (WIKA)", "Remedy"], [
        ["Metal filings or dust inside the window, pointer off zero", "Vibration", "Liquid filled case or remote mounting"],
        ["Pointer flutter", "Pulsation", "Restrictor or snubber"],
        ["Bent pointer, shaped like a fish hook", "Pressure spikes", "A range about twice the maximum pressure"],
        ["Pointer buried against the stop pin", "Overpressure, which can deform the Bourdon tube", "Larger range, overpressure protection"],
        ["Reads near zero with the system running", "Clogged connection", "Clear the port, consider a diaphragm seal"],
    ]),
    p("Beamex adds that contamination can obstruct moving parts and cause hysteresis. Our guide to " + link("/pressure-gauge-snubbers-siphons-and-gauge-valves", "snubbers, siphons and gauge valves") + " explains the accessories that prevent most of these faults."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Reading only on the way up.", "Without the descending points you cannot see hysteresis."),
        ("Using a reference that is barely better than the gauge.", "Keep to at least 4:1, for example a 0.05% reference for a 1% gauge."),
        ("Ignoring the height of a liquid column.", "One metre of water adds about 98 mbar."),
        ("Recording only the final result.", "Keep the readings as found and as left, so you can see drift over time."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("How many points should I test?", "Additel says 3 to 5 points are typically taken going up and then coming down. Reotemp uses 25, 50, 75 and 100% up and 75, 50 and 25% down."),
        ("How accurate must the reference be?", "Traditionally at least 4 times more accurate than the gauge under test, the 4:1 test uncertainty ratio."),
        ("How often should a pressure gauge be calibrated?", "Ashcroft suggests every 12 months, and more often with vibration, pulsation or rapid cycling. You set the interval for your plant."),
    ]),
]
