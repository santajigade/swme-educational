META = {
    "category": "flow-measurement-guides",
    "title": "Coriolis Mass Flow Meter Explained",
    "keyword": "coriolis mass flow meter",
    "subtitle": "How vibrating tubes, a tiny time delay and resonant frequency give direct mass flow and density",
    "meta_title": "Coriolis Mass Flow Meter Explained: Principle and Use",
    "meta_description": "How a Coriolis mass flow meter works: vibrating tubes, phase shift, density from frequency, accuracy, turndown, limits and installation orientation tips.",
    "summary": "How a Coriolis meter measures mass flow and density directly, where it fits and how to install it for a stable zero.",
    "card_title": "Coriolis Mass Flow Meter Explained",
    "author": "SWME Technical Staff",
    "published": "2026-11-18",
    "status": "published",
    "sort_order": 4,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "flow",
        "title": "How a Coriolis Meter Measures Mass Flow",
        "alt": "Infographic showing four steps of Coriolis mass flow measurement: drive, twist, time delay and output",
        "steps": [
            ["Drive", "A drive coil vibrates the flow tubes at their natural frequency."],
            ["Twist", "Moving fluid creates Coriolis forces that twist the tubes."],
            ["Delta T", "Pickoffs at inlet and outlet see a time delay between their signals."],
            ["Output", "Delta T gives mass flow; tube frequency gives density."],
        ],
    },
}

_C = "#1971c2"


def _sine(x0, y0, w, amp, shift, color):
    pts = []
    import math
    for i in range(0, 101):
        x = x0 + w * i / 100
        y = y0 - amp * math.sin(2 * math.pi * (i / 100 * 2) - shift)
        pts.append(f"{x:.1f},{y:.1f}")
    return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="3"/>'


_diag = (
    arrow_defs(_C)
    # inlet and outlet pipe
    + '<rect x="20" y="300" width="360" height="26" fill="#dee2e6" stroke="#495057" stroke-width="2"/>'
    + '<line x1="30" y1="313" x2="90" y2="313" stroke="' + _C + '" stroke-width="3" marker-end="url(#ah)"/>'
    + '<line x1="310" y1="313" x2="370" y2="313" stroke="' + _C + '" stroke-width="3" marker-end="url(#ah)"/>'
    + '<text x="30" y="350" font-size="13" font-weight="700" fill="#14508a">Inlet</text>'
    + '<text x="370" y="350" text-anchor="end" font-size="13" font-weight="700" fill="#14508a">Outlet</text>'
    # U tubes
    + '<path d="M110 300 L110 90 Q110 50 150 50 L250 50 Q290 50 290 90 L290 300" fill="none" stroke="#495057" stroke-width="12"/>'
    + '<path d="M110 300 L110 90 Q110 50 150 50 L250 50 Q290 50 290 90 L290 300" fill="none" stroke="#dbeafa" stroke-width="6"/>'
    + '<path d="M130 300 L130 100 Q130 72 158 72 L242 72 Q270 72 270 100 L270 300" fill="none" stroke="#495057" stroke-width="12"/>'
    + '<path d="M130 300 L130 100 Q130 72 158 72 L242 72 Q270 72 270 100 L270 300" fill="none" stroke="#dbeafa" stroke-width="6"/>'
    # drive and pickoffs
    + '<rect x="180" y="36" width="40" height="50" rx="6" fill="#ffd8a8" stroke="#e8590c" stroke-width="2"/>'
    + '<text x="200" y="26" text-anchor="middle" font-size="13" font-weight="700" fill="#e8590c">Drive coil</text>'
    + '<rect x="96" y="160" width="48" height="30" rx="6" fill="#d3f9d8" stroke="#2b8a3e" stroke-width="2"/>'
    + '<rect x="256" y="160" width="48" height="30" rx="6" fill="#d3f9d8" stroke="#2b8a3e" stroke-width="2"/>'
    + '<text x="60" y="150" text-anchor="middle" font-size="12" font-weight="700" fill="#2b8a3e">Inlet</text>'
    + '<text x="60" y="166" text-anchor="middle" font-size="12" font-weight="700" fill="#2b8a3e">pickoff</text>'
    + '<text x="342" y="150" text-anchor="middle" font-size="12" font-weight="700" fill="#2b8a3e">Outlet</text>'
    + '<text x="342" y="166" text-anchor="middle" font-size="12" font-weight="700" fill="#2b8a3e">pickoff</text>'
    + '<text x="200" y="220" text-anchor="middle" font-size="12" fill="#555">Two tubes</text>'
    + '<text x="200" y="236" text-anchor="middle" font-size="12" fill="#555">vibrate</text>'
    + '<text x="200" y="252" text-anchor="middle" font-size="12" fill="#555">against</text>'
    + '<text x="200" y="268" text-anchor="middle" font-size="12" fill="#555">each other</text>'
    # signals
    + '<text x="600" y="40" text-anchor="middle" font-size="14" font-weight="700" fill="#14508a">Pickoff signals with flow</text>'
    + '<line x1="430" y1="130" x2="780" y2="130" stroke="#ced4da" stroke-width="1"/>'
    + '<line x1="430" y1="250" x2="780" y2="250" stroke="#ced4da" stroke-width="1"/>'
    + _sine(440, 130, 320, 45, 0, "#2b8a3e")
    + _sine(440, 250, 320, 45, 0.9, "#1971c2")
    + '<text x="440" y="70" font-size="12" font-weight="700" fill="#2b8a3e">Inlet pickoff</text>'
    + '<text x="440" y="192" font-size="12" font-weight="700" fill="#1971c2">Outlet pickoff</text>'
    + '<line x1="520" y1="130" x2="520" y2="300" stroke="#495057" stroke-width="1.2" stroke-dasharray="4 3"/>'
    + '<line x1="543" y1="250" x2="543" y2="300" stroke="#495057" stroke-width="1.2" stroke-dasharray="4 3"/>'
    + '<text x="600" y="334" text-anchor="middle" font-size="14" font-weight="700" fill="#e8590c">Delta T is proportional to mass flow</text>'
    + '<line x1="520" y1="300" x2="543" y2="300" stroke="#e8590c" stroke-width="3"/>'
)

BODY = [
    takeaways([
        "A Coriolis mass flow meter measures mass flow directly, not volume.",
        "Flow twists vibrating tubes; the time delay between inlet and outlet pickoffs is proportional to mass flow.",
        "The natural frequency of the tubes gives fluid density, so one meter reports mass flow, density and volume flow.",
        "Liquid meters must run completely full, and mounting stress upsets the zero.",
    ]),
    p("Custody transfer, batching and dosing often need mass, not volume. A <strong>coriolis mass flow meter</strong> measures mass flow directly, so changes in temperature, pressure, viscosity or density do not need separate compensation. That makes it a common choice for chemicals, hydrocarbons and food products.",
      "This guide explains the principle, the numbers to know and the installation points that protect accuracy. SWME supplies " + link("/flowmeters", "flowmeters") + " and " + link("/flow-transmitters", "flow transmitters") + " for process plants across the GCC."),
    toc([("principle", "Coriolis mass flow meter working principle"), ("density", "Density and volume flow"), ("numbers", "Accuracy and turndown"),
         ("fit", "Where Coriolis meters fit"), ("install", "Installation tips"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("principle", "Coriolis Mass Flow Meter Working Principle"),
    p("In a common dual tube design described by " + ext("https://www.emersonautomationexperts.com/2016/measurement-instrumentation/the-theory-of-coriolis-how-the-technology-measures-mass-flow-and-density/", "Emerson") + ", the flow splits so that half enters each of two parallel tubes. A drive coil makes the tubes vibrate against each other at their natural resonant frequency. Magnet and coil assemblies called pickoffs, mounted at the inlet and outlet sides, produce a sine wave that tracks the tube motion."),
    p("With no flow, both pickoff signals are in phase. When fluid moves through the vibrating tubes, Coriolis forces twist them in opposition, so the signals shift out of phase. The time difference, called Delta T, is measured in microseconds and is directly proportional to the mass flow rate."),
    svg(_diag, "Dual U tube Coriolis meter with drive coil, pickoffs and the time delay between pickoff signals", 360),
    INFOGRAPHIC,
    h2("density", "Density and Volume Flow"),
    p("The same tubes also act as a densitometer. Emerson compares them to a spring with weights: a heavier mass oscillates at a lower frequency. Because tube stiffness stays essentially constant, a change in natural frequency reflects a change in fluid density. Volume flow is then calculated from mass flow and density. To move between the two, use the " + ext("https://zentacalculator.com/engineering/mass-flow-rate/", "mass flow rate calculator") + "."),
    dyk("Coriolis meters do not depend on Reynolds number or velocity profile. According to " + ext("https://instrumentationtools.com/coriolis-mass-flow-meter-working-principle", "Instrumentation Tools") + ", they need no upstream or downstream straight run or flow conditioning, which is rare among flow technologies."),
    h2("numbers", "Accuracy and Turndown"),
    rows([
        ("Base accuracy", "Commonly on the order of 0.2%, linear over the full flow range."),
        ("Turndown, curved tubes", "About 100:1 to 200:1."),
        ("Turndown, straight tubes", "About 30:1 to 50:1, with lower accuracy."),
        ("Zero stability", "The main limit at low flow; total error grows as flow falls toward the zero stability value."),
        ("Gas service", "A minimum gas density of about 4.5 kg/m³ is needed, depending on vendor."),
    ], "At a glance (Instrumentation Tools)"),
    p("Use the " + ext("https://zentacalculator.com/engineering/turndown-ratio/", "turndown ratio calculator") + " and the " + ext("https://zentacalculator.com/engineering/instrument-accuracy/", "instrument accuracy calculator") + " to test these figures against your own flow range."),
    h2("fit", "Where a Coriolis Mass Flow Meter Fits"),
    twocol([
        ("Good fit", "bi-check-circle", [
            "Liquids where mass or density matters",
            "Slurries and non Newtonian fluids",
            "Some compressed gases and cryogenic liquids",
            "Pulsating flow and short pipe runs",
        ]),
        ("Poor fit", "bi-x-circle", [
            "Large lines; the largest unit cited has 6 in flanges",
            "Low pressure gas, described as marginal below 150 psig",
            "Liquids near boiling, which can cavitate",
            "Low pressure drop budgets with small bore designs",
        ]),
    ]),
    p("Instrumentation Tools also notes that the meter is costly, although often comparable to a volumetric meter plus a densitometer. To compare technologies, see " + link("/types-of-flow-meters", "types of flow meters") + " and " + link("/vortex-flow-meter-working-principle", "vortex flow meter working principle") + "."),
    h2("install", "Installation Tips"),
    checklist([
        ("Keep it full", "A liquid meter must be completely full. " + ext("https://www.processingmagazine.com/process-control-automation/instrumentation/flow-measurement/article/55350912/quiz-corner-coriolis-mass-flowmeter-orientation-for-liquid-applications-part-2-of-3", "Processing Magazine") + " warns that an inverted U tube can trap gas and should not be used for liquids."),
        ("Choose orientation", "For a standard U tube meter on liquid, the flag position is usually the most practical; tubes down and horizontal also work with piping changes."),
        ("Avoid stress", "Support the piping so the meter body carries no load, because mounting stress upsets the zero."),
        ("Watch pressure drop", "Check the drop across the meter and keep liquids above vapour pressure."),
        ("Check the signal", "Scale the output with the " + ext("https://zentacalculator.com/engineering/4-20ma-scaling/", "4 to 20 mA scaling calculator") + "."),
    ]),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Mounting the tubes up on liquid service.", "Gas collects at the top of the loop and the reading becomes unstable."),
        ("Oversizing for low pressure drop.", "Flow then sits near the zero stability limit, where error grows."),
        ("Bolting into misaligned flanges.", "Stress on the meter shifts the zero."),
    ]),
    p("If readings drift, our blog on " + link("/blog/flow-meter-incorrect-readings-causes-fixes", "flow meter incorrect readings") + " lists common causes, and " + ext("https://www.instrumentationblog.in/category/process-instrumentation/flow-measurement/", "Instrumentation Blog") + " has more flow measurement reading."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What does a Coriolis meter measure?", "It measures mass flow directly and also density and volume flow, from one instrument."),
        ("Does a Coriolis meter need straight pipe?", "No straight run or flow conditioning is normally required, because the measurement does not depend on velocity profile."),
        ("Can a Coriolis meter measure gas?", "Yes, for some compressed gases, but low pressure gas is difficult and a minimum gas density applies."),
    ]),
]
