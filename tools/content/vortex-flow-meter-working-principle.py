META = {
    "category": "flow-measurement-guides",
    "title": "Vortex Flow Meter Working Principle Explained",
    "keyword": "vortex flow meter",
    "subtitle": "How a bluff body, shedding frequency and the Strouhal number give you volumetric flow",
    "meta_title": "Vortex Flow Meter Working Principle Explained",
    "meta_description": "How a vortex flow meter works: bluff body, Karman vortex street, Strouhal number, sensors, Reynolds number limits, applications and installation tips.",
    "summary": "How vortex shedding behind a bluff body is turned into a flow reading, where vortex meters fit and where they do not.",
    "card_title": "Vortex Flow Meter Working Principle",
    "author": "SWME Technical Staff",
    "published": "2026-11-17",
    "status": "published",
    "sort_order": 3,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "grid",
        "title": "Four Parts of a Vortex Flow Meter",
        "alt": "Infographic showing the four parts of a vortex flow meter: bluff body, vortex street, sensor and transmitter",
        "steps": [
            ["Bluff body", "A shedder bar across the pipe forces the flow to split around it."],
            ["Vortex street", "Vortices form alternately on each side, at a rate set by velocity."],
            ["Sensor", "Piezoelectric or capacitive sensors pick up the alternating forces."],
            ["Transmitter", "Electronics turn the shedding frequency into volumetric flow."],
        ],
    },
}

_C = "#1971c2"


def _vortex(cx, cy, r, cw):
    s = 1 if cw else 0
    return (f'<path d="M{cx - r} {cy} A{r} {r} 0 1 {s} {cx + r} {cy} A{r * 0.6:.0f} {r * 0.6:.0f} 0 1 {s} {cx - r * 0.2:.0f} {cy}" '
            f'fill="none" stroke="{_C}" stroke-width="3"/>')


_diag = (
    arrow_defs(_C)
    + '<rect x="40" y="80" width="720" height="180" fill="#eef5fd"/>'
    + '<line x1="40" y1="80" x2="760" y2="80" stroke="#495057" stroke-width="4"/>'
    + '<line x1="40" y1="260" x2="760" y2="260" stroke="#495057" stroke-width="4"/>'
    + '<line x1="60" y1="130" x2="150" y2="130" stroke="' + _C + '" stroke-width="3" marker-end="url(#ah)"/>'
    + '<line x1="60" y1="170" x2="150" y2="170" stroke="' + _C + '" stroke-width="3" marker-end="url(#ah)"/>'
    + '<line x1="60" y1="210" x2="150" y2="210" stroke="' + _C + '" stroke-width="3" marker-end="url(#ah)"/>'
    + '<text x="60" y="112" font-size="13" font-weight="700" fill="#14508a">Flow, velocity V</text>'
    + '<polygon points="200,138 222,148 222,192 200,202" fill="#495057"/>'
    + '<text x="211" y="295" text-anchor="middle" font-size="13" font-weight="700" fill="#14508a">Bluff body, width d</text>'
    + '<line x1="211" y1="282" x2="211" y2="206" stroke="#495057" stroke-width="1.5"/>'
    + _vortex(290, 135, 20, True) + _vortex(380, 205, 22, False) + _vortex(470, 135, 24, True)
    + _vortex(560, 205, 26, False) + _vortex(650, 135, 28, True)
    + '<rect x="250" y="20" width="110" height="40" rx="8" fill="#dbeafa" stroke="' + _C + '" stroke-width="2"/>'
    + '<text x="305" y="45" text-anchor="middle" font-size="13" font-weight="700" fill="#14508a">Sensor</text>'
    + '<line x1="250" y1="40" x2="222" y2="40" stroke="#495057" stroke-width="2"/>'
    + '<line x1="222" y1="40" x2="222" y2="76" stroke="#495057" stroke-width="2"/>'
    + '<text x="520" y="45" text-anchor="middle" font-size="14" font-weight="700" fill="#14508a">Vortices shed alternately from each side</text>'
    + '<text x="752" y="250" text-anchor="end" font-size="13" fill="#555">Pipe bore D</text>'
    + '<text x="400" y="335" text-anchor="middle" font-size="16" font-weight="700" fill="#14508a">Shedding frequency f = St × V / d</text>'
)

BODY = [
    takeaways([
        "A vortex flow meter counts the vortices shed by a bluff body placed across the pipe.",
        "Shedding frequency is proportional to flow velocity, so the meter reads volumetric flow.",
        "It suits steam, gases and clean, low viscosity liquids, with no moving parts.",
        "It needs turbulent flow, a minimum velocity and enough straight pipe upstream and downstream.",
    ]),
    p("Steam, compressed air, natural gas and water lines often need a robust meter with no moving parts. A <strong>vortex flow meter</strong> meets that need by using a simple effect of fluid flow: when a fluid passes a blunt obstacle, it sheds a regular train of swirls whose rate depends on velocity.",
      "This guide explains the principle, the limits and the installation points that matter. SWME supplies " + link("/flowmeters", "flow meters") + " and " + link("/flow-transmitters", "flow transmitters") + " for process plants across the GCC."),
    toc([("principle", "Vortex flow meter working principle"), ("formula", "The Strouhal relationship"), ("parts", "Main parts"),
         ("fit", "Where vortex meters fit"), ("install", "Installation tips"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("principle", "Vortex Flow Meter Working Principle"),
    p("A bluff body, also called a shedder bar, spans the pipe. As fluid flows past it, vortices form alternately on each side and travel downstream in a pattern known as the Karman vortex street. As " + ext("https://www.globalspec.com/learnmore/sensors_transducers_detectors/flow_sensing/vortex_flow_meters", "GlobalSpec") + " states, the frequency of the vortices is proportional to the flow velocity. Each vortex creates an alternating pressure on the bar, and a sensor counts these pulses."),
    svg(_diag, "Vortex shedding behind a bluff body in a vortex flow meter", 350),
    h2("formula", "The Strouhal Relationship"),
    p("The link between frequency and velocity is the Strouhal number, St, a dimensionless value found by experiment. According to " + ext("https://instrumentationtools.com/working-principle-of-vortex-flow-meter", "Instrumentation Tools") + ", the working formula reduces to f = St × V / d, where f is the shedding frequency, V the velocity and d the width of the bluff body face. The ratio d/D, bar width to pipe bore, is typically 0.22 to 0.26.",
      "Because St stays nearly constant over the working range, frequency rises in a straight line with velocity. Volumetric flow is then velocity times the pipe area. The " + ext("https://zentacalculator.com/engineering/vortex-shedding-frequency/", "vortex shedding frequency calculator") + " shows the relationship with your own numbers, and the " + ext("https://zentacalculator.com/engineering/flow-meter-k-factor/", "flow meter K factor calculator") + " converts pulses to volume."),
    table(["Width ratio w/D", "Strouhal number S"], [["0.1", "0.18"], ["0.3", "0.26"], ["0.5", "0.44"]]),
    p("Experimental Strouhal values quoted by GlobalSpec for different bar width ratios."),
    h2("parts", "Main Parts of a Vortex Meter"),
    INFOGRAPHIC,
    p("The two common sensor types are a pair of piezoelectric crystals built into the shedder bar, which respond to the alternating shedding forces, and variable capacitance sensors, which respond to tiny movements of the bar. Since the meter has no rotating parts, it needs little maintenance in clean service."),
    dyk("A vortex meter has a natural cut off. Vortices only form reliably above a Reynolds number of about 10,000, so below a certain velocity the meter simply stops counting. You can check your line with the " + ext("https://zentacalculator.com/engineering/reynolds-number/", "Reynolds number calculator") + "."),
    h2("fit", "Where a Vortex Flow Meter Fits"),
    twocol([
        ("Good fit", "bi-check-circle", [
            "Steam",
            "Gases, including natural gas",
            "Water and low viscosity liquid chemicals",
            "Lines from 0.5 in up to about 12 in",
        ]),
        ("Poor fit", "bi-x-circle", [
            "High viscosity liquids, which damp the vortices",
            "Very low flow rates below the cut off",
            "Heavy solids that wear or clog the bluff body",
            "Liquids near flashing, where cavitation can occur",
        ]),
    ]),
    p("For low viscosity liquids such as water, Instrumentation Tools quotes a rangeability of about 20:1 at a maximum velocity of 4.6 m/s. Meters below 0.5 in (12 mm) are impractical, and above 12 in (300 mm) they have limited application. Gas service also needs pressure and temperature compensation because gas is compressible; see the " + ext("https://zentacalculator.com/engineering/gas-flow-correction/", "gas flow correction calculator") + ". To compare technologies, read " + link("/types-of-flow-meters", "types of flow meters") + " and " + link("/electromagnetic-flow-meter-working-principle", "electromagnetic flow meter working principle") + "."),
    h2("install", "Installation Tips"),
    checklist([
        ("Straight pipe", "Provide the straight run upstream and downstream that the manufacturer specifies, away from pumps and valves."),
        ("Size for velocity", "Check that the minimum flow stays above the cut off; use the " + ext("https://zentacalculator.com/engineering/pipe-flow-velocity/", "pipe flow velocity calculator") + "."),
        ("Back pressure", "Keep enough downstream pressure on liquids to avoid cavitation."),
        ("Clean bar", "Erosion or deposits such as wax on the shedder bar change the calibration."),
        ("Noise", "Hydraulic noise and loose mounting can disturb the signal."),
    ]),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Oversizing the meter.", "Low velocity drops the flow below the cut off, and the reading goes to zero."),
        ("Viscous liquids.", "Most meters are calibrated for liquids of 1 cSt, and high viscosity reduces rangeability."),
        ("Short upstream run.", "Disturbed flow profiles change the shedding pattern and the accuracy."),
    ]),
    p("If readings drift after installation, our blog on " + link("/blog/flow-meter-incorrect-readings-causes-fixes", "flow meter incorrect readings") + " lists common causes, and " + ext("https://www.instrumentationblog.in/category/process-instrumentation/flow-measurement/", "Instrumentation Blog") + " has more flow measurement reading."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What does a vortex flow meter measure?", "It measures volumetric flow by counting the vortices shed by a bluff body, since their frequency is proportional to velocity."),
        ("Can a vortex flow meter measure steam?", "Yes. Steam, gases and low viscosity liquids are typical applications."),
        ("Why does a vortex meter read zero at low flow?", "Below a Reynolds number of about 10,000 vortices do not form reliably, so the meter has a low flow cut off."),
    ]),
]
