META = {
    "category": "level-measurement-guides",
    "title": "Guided Wave Radar Level Measurement Basics",
    "keyword": "guided wave radar",
    "subtitle": "How a probe guided radar pulse measures level and interface, which probe to choose and how to install it",
    "meta_title": "Guided Wave Radar Level Measurement Basics",
    "meta_description": "Guided wave radar level measurement explained: how the pulse and probe work, dielectric constant, interface, probe types, installation tips and mistakes.",
    "summary": "How guided wave radar measures level and interface, how to choose a probe and how to install it for a reliable reading.",
    "card_title": "Guided Wave Radar Basics",
    "author": "SWME Technical Staff",
    "published": "2026-11-19",
    "status": "published",
    "sort_order": 5,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "steps",
        "title": "How Guided Wave Radar Works",
        "alt": "Infographic showing four steps of guided wave radar level measurement from pulse to level output",
        "steps": [
            ["Pulse sent", "The transmitter sends a low power radar pulse down the probe."],
            ["Guided by the probe", "The probe acts as a waveguide and keeps the pulse focused."],
            ["Echo at the surface", "Part of the pulse reflects where the dielectric constant changes."],
            ["Level calculated", "Time of flight gives the distance, and the distance gives the level."],
        ],
    },
}

_C = "#0c8599"
_T = "#0a5f6d"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_diag = (
    '<defs><marker id="ahl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="#c92a2a"/></marker>'
    '<marker id="ahb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="#1971c2"/></marker></defs>'
    # transmitter head and flange
    + '<rect x="160" y="20" width="120" height="50" rx="8" fill="#d3f0f4" stroke="' + _C + '" stroke-width="2"/>'
    + _t(220, 50, "Transmitter", 13, anchor="middle")
    + '<rect x="190" y="70" width="60" height="16" fill="#adb5bd" stroke="#495057" stroke-width="1.5"/>'
    # tank
    + '<path d="M80 86 L360 86 L360 380 L80 380 Z" fill="none" stroke="#495057" stroke-width="3"/>'
    # oil layer
    + '<rect x="82" y="180" width="276" height="90" fill="#ffec99" opacity="0.8"/>'
    # water layer
    + '<rect x="82" y="270" width="276" height="108" fill="#a5d8ff" opacity="0.8"/>'
    + _t(300, 230, "Oil", 13, fill="#8a6d00", anchor="middle")
    + _t(300, 330, "Water", 13, fill="#1864ab", anchor="middle")
    # probe
    + '<line x1="220" y1="86" x2="220" y2="360" stroke="#343a40" stroke-width="4"/>'
    + '<rect x="212" y="356" width="16" height="12" fill="#343a40"/>'
    # pulse down
    + '<line x1="200" y1="100" x2="200" y2="172" stroke="#c92a2a" stroke-width="2.5" marker-end="url(#ahl)"/>'
    + '<line x1="200" y1="190" x2="200" y2="262" stroke="#c92a2a" stroke-width="2.5" marker-end="url(#ahl)"/>'
    # echoes up
    + '<line x1="240" y1="176" x2="240" y2="104" stroke="#1971c2" stroke-width="2" marker-end="url(#ahb)"/>'
    + '<line x1="256" y1="266" x2="256" y2="104" stroke="#1971c2" stroke-width="3.5" marker-end="url(#ahb)"/>'
    + _t(110, 140, "Pulse", 12, fill="#c92a2a")
    # labels on the right
    + '<line x1="360" y1="180" x2="430" y2="180" stroke="#868e96" stroke-width="1" stroke-dasharray="4 3"/>'
    + '<line x1="360" y1="270" x2="430" y2="270" stroke="#868e96" stroke-width="1" stroke-dasharray="4 3"/>'
    + _t(440, 176, "Echo 1: product surface")
    + _t(440, 194, "weaker echo, oil dielectric about 2", 12, "400", "#555")
    + _t(440, 266, "Echo 2: oil and water interface")
    + _t(440, 284, "strong echo, water dielectric about 80", 12, "400", "#555")
    + _t(440, 60, "Time of flight gives distance")
    + _t(440, 78, "from the reference point to each echo", 12, "400", "#555")
    + _t(440, 112, "Level = reference height", 13)
    + _t(440, 130, "minus measured distance", 13)
    + _t(440, 360, "Probe end near the tank bottom", 12, "400", "#555")
    + '<line x1="232" y1="362" x2="434" y2="356" stroke="#868e96" stroke-width="1" stroke-dasharray="4 3"/>'
)

BODY = [
    takeaways([
        "Guided wave radar sends low power pulses down a probe and times the echo from the product surface.",
        "The echo strength depends on the dielectric constant: water (about 80) reflects strongly, oil (about 2) much less.",
        "A second echo from a lower, higher dielectric liquid lets one transmitter measure both level and interface.",
        "Probe choice, nozzle size and clearance from metal decide whether the reading is reliable.",
    ]),
    p("Many tanks, separators and bypass chambers need a level reading that does not drift with density, pressure or temperature. <strong>Guided wave radar</strong>, often shortened to GWR, meets that need with a probe that hangs into the liquid and a pulse that is timed electronically.",
      "This guide explains how it works, how to pick a probe and how to avoid the usual installation problems. SWME supplies " + link("/level-transmitters", "level transmitters") + " and " + link("/level-gauges", "level gauges") + " for process plants across the GCC."),
    toc([("principle", "How guided wave radar works"), ("dielectric", "Dielectric constant and interface"), ("probes", "Probe types"),
         ("install", "Installation checklist"), ("compare", "Strengths and limits"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("principle", "How Guided Wave Radar Works"),
    p("According to " + ext("https://www.emerson.com/en-ca/automation/measurement-instrumentation/level/continuous-level-measurement/about-guided-wave-radar", "Emerson") + ", GWR uses time domain reflectometry. The transmitter sends radar pulses down a probe that acts as a waveguide. When a pulse meets the product surface, part of it reflects back. The transmitter measures the time between sending the pulse and receiving the echo, converts it to a distance and subtracts that distance from the reference height to give level."),
    INFOGRAPHIC,
    rows([
        ("Contacting", "The probe is in the vessel contents, unlike a non contacting radar that sends its signal through the vapour space."),
        ("No moving parts", "Emerson notes that no compensation is needed for density, conductivity, viscosity, pH, temperature or pressure, unlike a displacer."),
        ("Vapour and foam", "The reading is largely unaffected by most vapour space conditions. Light to moderate foam is usually penetrated, while very dense foam can cause errors."),
        ("Outputs", "Most units give a 4 to 20 mA signal with HART. The " + ext("https://zentacalculator.com/engineering/4-20ma-scaling/", "4 to 20 mA scaling calculator") + " converts level to current."),
    ], "At a glance"),
    h2("dielectric", "Dielectric Constant and Interface"),
    p("The size of the echo depends on the dielectric constant, or relative permittivity, of the product. Emerson gives water at about 80 and oil at about 2, and states that its high sensitivity transmitters measure media down to a dielectric constant of 1.2. Check the value for your own product with the supplier before you order."),
    p("For interface, the first echo comes from the top liquid and the remaining energy reflects again at the lower liquid. " + ext("https://www.chemicalprocessing.com/articles/2011/make-the-most-of-radar/", "Chemical Processing") + " adds three conditions: the lower dielectric fluid must be on top, its dielectric value must be known, and the two liquids should differ by at least about 10. For example, a hydrocarbon layer of about 2 over a water based layer above 40 works well, while emulsions are hard to measure."),
    svg(_diag, "Guided wave radar measuring oil level and an oil and water interface with two echoes", 400),
    h2("probes", "Probe Types"),
    table(["Probe", "Best for", "Watch out for"],
          [["Coaxial", "Clean liquids, short to medium ranges, bypass chambers; high signal strength", "Clogging and buildup in dirty service"],
           ["Rigid single lead", "Shorter chambers, low dielectric products and interface", "Must not touch the chamber wall"],
           ["Flexible single lead", "Tall tanks and limited headroom", "Needs a weight and must stay clear of the wall"],
           ["Segmented single lead", "Tall chambers and pipes up to 10 m with limited headroom", "Assembly length and centring"],
           ["Twin lead", "General liquids", "Clogging and buildup in sticky service"]]),
    p("Probe uses come from Emerson, and the buildup notes from Chemical Processing, which recommends single lead probes for dirty, sticky or coating liquids. For level in a chamber, our guide to " + link("/how-a-magnetic-level-gauge-works", "how a magnetic level gauge works") + " shows how a GWR transmitter often shares a chamber with a float indicator."),
    dyk("Steam is one of the few vapours that affects GWR. Chemical Processing notes that above roughly 30 to 35 bar steam pressure, guided wave radar needs dynamic vapour compensation to stay accurate in boiler drums and feedwater heaters."),
    h2("install", "Installation Checklist"),
    checklist([
        ("Nozzle size", "Chemical Processing advises nozzles at least 2 inches in diameter and no more than 6 inches high."),
        ("Clear the probe", "Keep the probe away from the wall, pipes, baffles and agitators. Only a coaxial probe may touch metal."),
        ("Chamber size", "Use 75 mm or 100 mm chambers; smaller chambers raise the risk of buildup and wall contact."),
        ("Keep flow off the probe", "Do not let a fill stream fall onto the probe or into the measuring path."),
        ("Heat viscous service", "Insulate and heat trace chambers on viscous products, or choose a non contacting radar."),
        ("Set the medium", "Enter the correct dielectric and thresholds, since oil and water need different settings."),
    ]),
    h2("compare", "Strengths and Limits"),
    twocol([
        ("Strengths", "bi-check-circle", ["Level and interface from one device", "Works on liquids, sludges, slurries and some solids", "No moving parts and little maintenance", "Unaffected by density changes"]),
        ("Limits", "bi-exclamation-triangle", ["Probe is in contact with the product", "Not suited near agitators, pumps or hopper outlets", "Very viscous or heavily coating products", "Metal contact degrades the signal"]),
    ]),
    p("If the probe cannot go into the vessel, read " + link("/radar-vs-ultrasonic-level-measurement", "radar vs ultrasonic level measurement") + ". For a pressure based option, see " + link("/dp-level-measurement-in-closed-tanks", "DP level measurement in closed tanks") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Twin or coaxial probes in sticky service.", "They clog; a single lead probe tolerates buildup better."),
        ("A probe touching the chamber wall.", "Use a centring disk, a weight on flexible probes and a chamber of the right size."),
        ("Ignoring the dielectric value.", "A low or changing dielectric weakens the echo, especially with turbulence or boiling."),
    ]),
    p("For field faults, " + ext("https://www.instrumentationblog.in/guided-wave-radar-troubleshooting/", "Instrumentation Blog") + " has a GWR troubleshooting guide, and our post on " + link("/blog/level-transmitter-calibration-mistakes", "level transmitter calibration mistakes") + " covers setup errors. To turn level into volume, try the " + ext("https://zentacalculator.com/engineering/vertical-tank-volume/", "vertical tank volume calculator") + "."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What is guided wave radar?", "A level transmitter that sends radar pulses down a probe and times the echo from the product surface to calculate level."),
        ("Can guided wave radar measure interface?", "Yes, when a lower dielectric liquid sits on top of a higher dielectric liquid and the two differ by at least about 10."),
        ("Which probe suits sticky liquids?", "A single lead probe, because coaxial and twin probes are more prone to clogging and buildup."),
    ]),
]
