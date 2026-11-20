META = {
    "category": "flow-measurement-guides",
    "title": "Orifice Plate Flow Measurement Basics",
    "keyword": "orifice plate",
    "subtitle": "How an orifice plate turns flow into differential pressure, how to choose the beta ratio and taps, and how to install it",
    "meta_title": "Orifice Plate Flow Measurement Basics",
    "meta_description": "Orifice plate flow measurement explained: square root law, beta ratio, pressure loss, plate and tap types, straight run, turndown and common mistakes.",
    "summary": "How an orifice plate measures flow through differential pressure, how beta ratio affects pressure loss, and what a good installation needs.",
    "card_title": "Orifice Plate Basics",
    "author": "SWME Technical Staff",
    "published": "2026-11-20",
    "status": "published",
    "sort_order": 5,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "levels",
        "title": "Pressure Along an Orifice Run",
        "alt": "Infographic showing line pressure upstream of an orifice plate, the low pressure just downstream and the partly recovered pressure further down the pipe",
        "top_label": "High",
        "bottom_label": "Low",
        "levels": [
            ["Upstream tap", "Full line pressure before the plate. This is the high side of the DP.", 0.85],
            ["Recovered pressure", "Pressure partly recovers downstream. What is not recovered, often 40 to 80% of the DP, is lost.", 0.5],
            ["Downstream tap", "Pressure is lowest just after the bore. This is the low side of the DP.", 0.15],
        ],
    },
}

_C = "#1971c2"
_T = "#14508a"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_diag = (
    '<defs><marker id="aho" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="#1971c2"/></marker></defs>'
    # pipe walls
    + '<line x1="40" y1="150" x2="760" y2="150" stroke="#495057" stroke-width="3"/>'
    + '<line x1="40" y1="250" x2="760" y2="250" stroke="#495057" stroke-width="3"/>'
    + '<rect x="40" y="152" width="720" height="96" fill="#eef5fd"/>'
    # orifice plate: two halves leaving a central bore
    + '<rect x="296" y="140" width="8" height="45" fill="#343a40"/>'
    + '<rect x="296" y="215" width="8" height="45" fill="#343a40"/>'
    # streamlines contracting through the bore and expanding downstream
    + '<path d="M60 175 C200 175 260 188 300 192 C340 194 380 194 430 186 C520 172 600 168 740 168" fill="none" stroke="#74c0fc" stroke-width="2"/>'
    + '<path d="M60 225 C200 225 260 212 300 208 C340 206 380 206 430 214 C520 228 600 232 740 232" fill="none" stroke="#74c0fc" stroke-width="2"/>'
    + '<line x1="70" y1="200" x2="170" y2="200" stroke="#1971c2" stroke-width="3" marker-end="url(#aho)"/>'
    + _t(70, 190, "Flow", 13, fill="#1864ab")
    # taps
    + '<line x1="260" y1="150" x2="260" y2="80" stroke="#495057" stroke-width="3"/>'
    + '<line x1="340" y1="150" x2="340" y2="80" stroke="#495057" stroke-width="3"/>'
    + '<line x1="260" y1="80" x2="285" y2="80" stroke="#495057" stroke-width="3"/>'
    + '<line x1="340" y1="80" x2="315" y2="80" stroke="#495057" stroke-width="3"/>'
    + '<rect x="250" y="30" width="100" height="42" rx="8" fill="#dbeafa" stroke="' + _C + '" stroke-width="2"/>'
    + _t(300, 56, "DP transmitter", 12, anchor="middle")
    + _t(245, 110, "H", 14, anchor="end")
    + _t(355, 110, "L", 14)
    # labels
    + _t(300, 285, "Orifice plate, bore d", 13, anchor="middle")
    + _t(300, 303, "sharp square edge faces upstream", 12, "400", "#555", anchor="middle")
    + _t(40, 285, "Pipe inside diameter D", 13)
    + _t(40, 303, "beta ratio = d / D", 12, "400", "#555")
    + _t(560, 285, "Pressure partly recovers", 13)
    + _t(560, 303, "the rest is permanent loss", 12, "400", "#555")
    + _t(420, 56, "Q is proportional to the square root of DP", 13)
)

BODY = [
    takeaways([
        "An orifice plate is a thin plate with a bore that creates a differential pressure; flow is proportional to the square root of that DP.",
        "Standard practice keeps the beta ratio, bore over pipe diameter, between 0.20 and 0.75.",
        "Permanent pressure loss is often 40 to 80% of the measured DP, and it rises as the beta ratio falls.",
        "A good installation needs enough straight pipe, the sharp edge facing upstream and clean impulse lines.",
    ]),
    p("The <strong>orifice plate</strong> is still one of the most common flow elements in process plants. It has no moving parts and is built to published standards. SWME supplies " + link("/orifice-plates", "orifice plates") + " together with " + link("/differential-pressure-transmitters", "DP transmitters") + " and " + link("/manifolds-fittings", "manifolds") + " for complete flow loops."),
    toc([("principle", "How it works"), ("beta", "Beta ratio and pressure loss"), ("types", "Plate and tap types"),
         ("install", "Installation checklist"), ("compare", "Strengths and limits"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("principle", "How Orifice Plate Flow Measurement Works"),
    p("The plate sits between flanges. As fluid passes through the smaller bore it speeds up and its pressure falls. According to " + ext("https://www.blog.projectmaterials.com/quick-answers/instrumentation/what-is-orifice-plate/", "Projectmaterials") + ", flow is worked out from Bernoulli's principle and the continuity equation, using the DP between a tap upstream and a tap downstream of the plate."),
    p("A common sizing form is Q = Cd &times; E &times; (&pi;/4) &times; d&sup2; &times; &radic;(2 &Delta;P / &rho;), where E = 1 / &radic;(1 - &beta;<sup>4</sup>). Projectmaterials notes that sizing follows ISO 5167 Part 2 or AGA Report No. 3. The " + ext("https://zentacalculator.com/engineering/orifice-flow/", "orifice flow calculator") + " runs this equation, and the " + ext("https://www.instrumentationblog.in/flow-rate-formula/", "flow rate formula guide") + " explains the terms."),
    INFOGRAPHIC,
    svg(_diag, "Orifice plate in a pipe with upstream and downstream taps to a DP transmitter, showing the flow contracting through the bore", 320),
    h2("beta", "Beta Ratio and Pressure Loss"),
    p("The beta ratio is the bore diameter divided by the pipe inside diameter. ISO 5167 limits it to 0.20 to 0.75 for concentric plates with corner, flange or D and D/2 taps. The " + ext("https://blog.projectmaterials.com/quick-answers/pipes/how-to-size-orifice-plate/", "Projectmaterials sizing guide") + " gives this trade off:"),
    table(["Beta ratio", "Typical use", "Permanent loss (share of DP)"],
          [["0.20 to 0.40", "Low flow, high accuracy", "70 to 90%"],
           ["0.40 to 0.55", "Standard", "55 to 70%"],
           ["0.55 to 0.65", "Most common range for process piping", "40 to 55%"],
           ["0.65 to 0.75", "High flow", "25 to 40%"]]),
    p("Because flow follows the square root of DP, " + ext("https://www.ics-schneider.de/messblende-auslegen-beta-verhaeltnis-und-bleibenden-druckverlust-richtig-abwaegen/?lang=en", "ICS Schneider") + " points out that 50% of the DP corresponds to about 70.7% of flow. The " + ext("https://zentacalculator.com/engineering/dp-flow-square-root/", "DP flow square root calculator") + " does this conversion."),
    dyk("At 10% of full flow an orifice plate produces only 1% of its full scale DP. That square law is why Projectmaterials puts orifice turndown at typically 3:1 to 5:1. Check your own range with the " + ext("https://zentacalculator.com/engineering/turndown-ratio/", "turndown ratio calculator") + "."),
    h2("types", "Plate and Tap Types"),
    rows([
        ("Concentric", "Centred round bore; Projectmaterials says it is used in more than 90% of installations."),
        ("Eccentric and segmental", "Offset or segment shaped bore. ICS Schneider describes the eccentric plate as a deliberately asymmetrical special design."),
        ("Quadrant edge and conical", "Special inlet shapes; Projectmaterials lists quadrant edge plates for Re 500 to 10,000. See the " + ext("https://zentacalculator.com/engineering/reynolds-number/", "Reynolds number calculator") + "."),
        ("Flange taps", "1 inch (25.4 mm) from each plate face; most common in oil and gas and in North America."),
        ("Corner taps", "At the plate face itself, common in Europe under ISO 5167."),
        ("D and D/2 taps", "One pipe diameter upstream and half a diameter downstream."),
    ], "At a glance"),
    h2("install", "Installation Checklist"),
    checklist([
        ("Face the edge upstream", "The bore edge must be sharp, square and burr free, and the sharp inlet edge must face the flow."),
        ("Give it straight pipe", "Projectmaterials quotes typically 15D to 44D upstream and 5D to 8D downstream under ISO 5167. Two elbows in different planes may need 40D or more without a flow conditioner."),
        ("Do not use a rule of thumb", "ICS Schneider warns against applying a general 10D upstream and 5D downstream; take the figure from the standard for your fittings and beta ratio."),
        ("Centre the plate", "ICS Schneider lists an off centre plate among the causes of error, along with bends, valves and swirl upstream."),
        ("Keep impulse lines clean", "Gas bubbles in liquid lines, condensate in gas lines and blockages all distort the DP."),
        ("Watch for cavitation", "ICS Schneider warns of cavitation when local pressure at the bore falls below the vapour pressure of the liquid."),
    ]),
    h2("compare", "Strengths and Limits"),
    twocol([
        ("Strengths", "bi-check-circle", ["No moving parts", "Built to ISO 5167, ASME MFC 3M and AGA Report No. 3", "Concentric plates cover more than 90% of installations"]),
        ("Limits", "bi-exclamation-triangle", ["Turndown typically 3:1 to 5:1", "Permanent pressure loss of 40 to 80% of the DP", "Needs long straight runs", "Edge damage causes error"]),
    ]),
    p("If pressure loss or turndown rules the plate out, compare other technologies in our " + link("/types-of-flow-meters", "types of flow meters") + " guide or read how a " + link("/vortex-flow-meter-working-principle", "vortex flow meter") + " works."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Installing the plate backwards.", "Projectmaterials says this can cause errors above 15%."),
        ("Forgetting square root extraction.", "Without it the system shows 50% flow at 50% DP instead of about 70.7%."),
        ("Ignoring worn or damaged bore edges.", "ICS Schneider names a damaged or eroded edge as a source of measurement error, so inspect the plate."),
    ]),
    p("For more field causes of bad readings, see our post on " + link("/blog/flow-meter-incorrect-readings-causes-fixes", "flow meter incorrect readings") + ", or browse the " + ext("https://www.instrumentationblog.in/category/process-instrumentation/flow-measurement/", "Instrumentation Blog flow section") + "."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("How does an orifice plate measure flow?", "It creates a pressure drop across a bore; a DP transmitter measures it and flow is calculated from the square root of the DP."),
        ("What is a good beta ratio?", "Between 0.20 and 0.75. Projectmaterials calls 0.55 to 0.65 the most common range for process piping."),
        ("Which side of the plate faces the flow?", "The sharp, square edge of the bore faces upstream."),
    ]),
]
