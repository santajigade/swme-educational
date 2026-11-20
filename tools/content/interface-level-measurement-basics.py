META = {
    "category": "level-measurement-guides",
    "title": "Interface Level Measurement Basics",
    "keyword": "interface level measurement",
    "subtitle": "How plants measure the boundary between oil and water, which technologies cope with emulsion, and how to choose one",
    "meta_title": "Interface Level Measurement Basics",
    "meta_description": "Interface level measurement explained: emulsion and rag layers, DP, displacer, guided wave radar, capacitance and nuclear methods, selection and mistakes.",
    "summary": "What an interface is, how DP, displacer, guided wave radar, capacitance and nuclear gauges measure it, and how emulsion changes the choice.",
    "card_title": "Interface Level Basics",
    "author": "SWME Technical Staff",
    "published": "2026-11-20",
    "status": "published",
    "sort_order": 6,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "compare",
        "title": "Three Ways to Find the Interface",
        "alt": "Infographic comparing density based, guided wave radar and capacitance interface level measurement",
        "columns": [
            ["Density based", ["DP or displacer", "Needs a density difference", "Small DP limits accuracy", "Weak with thick emulsion"]],
            ["Guided wave radar", ["Level and interface together", "Upper liquid dielectric below 10", "Dielectric difference above 10", "Emulsion under 50 mm"]],
            ["Capacitance", ["Probe and tank form a capacitor", "Lower liquid dielectric higher", "Stable reading in emulsion", "No density effect"]],
        ],
    },
}

_C = "#0c8599"
_T = "#0a5f6d"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_diag = (
    '<defs><marker id="ahi" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="#1971c2"/></marker></defs>'
    # vessel
    + '<rect x="80" y="60" width="300" height="320" rx="14" fill="#f8f9fa" stroke="#495057" stroke-width="3"/>'
    + _t(230, 100, "Gas", 13, fill="#868e96", anchor="middle")
    # oil
    + '<rect x="83" y="140" width="294" height="100" fill="#ffec99"/>'
    + _t(140, 195, "Oil", 14, fill="#8a6d00", anchor="middle")
    # emulsion band
    + '<rect x="83" y="240" width="294" height="30" fill="#d8c88a"/>'
    + _t(140, 260, "Emulsion", 12, fill="#5c4b00", anchor="middle")
    # water
    + '<rect x="83" y="270" width="294" height="107" rx="10" fill="#a5d8ff"/>'
    + _t(140, 330, "Water", 14, fill="#1864ab", anchor="middle")
    # GWR head and probe
    + '<rect x="250" y="22" width="80" height="38" rx="6" fill="#d3f0f4" stroke="' + _C + '" stroke-width="2"/>'
    + _t(290, 46, "GWR", 13, anchor="middle")
    + '<line x1="290" y1="60" x2="290" y2="360" stroke="#343a40" stroke-width="4"/>'
    # echo arrows
    + '<line x1="310" y1="140" x2="310" y2="72" stroke="#1971c2" stroke-width="2" marker-end="url(#ahi)"/>'
    + '<line x1="326" y1="255" x2="326" y2="72" stroke="#1971c2" stroke-width="3.5" marker-end="url(#ahi)"/>'
    # level lines and labels
    + '<line x1="380" y1="140" x2="440" y2="140" stroke="#868e96" stroke-dasharray="4 3"/>'
    + '<line x1="380" y1="255" x2="440" y2="255" stroke="#868e96" stroke-dasharray="4 3"/>'
    + _t(450, 136, "Total level: echo 1 from oil surface")
    + _t(450, 154, "upper liquid dielectric known, below 10", 12, "400", "#555")
    + _t(450, 251, "Interface: echo 2 at oil and water")
    + _t(450, 269, "dielectric difference above 10", 12, "400", "#555")
    + _t(450, 287, "emulsion layer under 50 mm", 12, "400", "#555")
    + _t(450, 190, "Oil layer thicker than 60 mm", 13)
    + _t(450, 60, "Guided wave radar limits", 14)
    + _t(450, 78, "as stated by Endress+Hauser", 12, "400", "#555")
)

BODY = [
    takeaways([
        "An interface is the boundary between two liquids that do not mix and have different densities, usually oil above water.",
        "In practice an emulsion or rag layer sits between them and blurs the boundary for most technologies.",
        "DP and displacers rely on a density difference, guided wave radar and capacitance on a dielectric difference.",
        "No single technology covers every interface application, so the emulsion and the accuracy you need decide the choice.",
    ]),
    p("Separators, desalters and settling tanks have to control where oil ends and water begins. <strong>Interface level measurement</strong> finds that boundary, often together with the total level. SWME supplies " + link("/level-transmitters", "level transmitters") + " and " + link("/level-gauges", "level gauges") + " for interface duties across the GCC."),
    toc([("what", "What an interface is"), ("methods", "Interface level measurement methods"), ("gwr", "Guided wave radar limits"),
         ("select", "Selection checklist"), ("compare", "Strengths and limits"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("what", "What an Interface Is"),
    p("According to " + ext("https://automationforum.co/interface-level-measurement-selection-procedure-complete-2025-guide-for-process-engineers/", "Automation Forum") + ", an interface is the line between two liquids that do not mix and have different densities. An emulsion, or rag layer, is droplets of one liquid dispersed in the other. It makes density and dielectric change gradually instead of in one step, and that degrades DP, displacer and radar readings. Thick rag layers can form at startup or after a surge in production flow."),
    p("Endress+Hauser, writing in " + ext("https://www.processonline.com.au/content/instrumentation/article/interface-level-detection-what-to-consider-1127504616", "Process Online") + ", adds that every extra medium in a vessel brings two interfaces, one on each side of its emulsion layer."),
    dyk("Endress+Hauser counts five interfaces in a vessel holding oil, water, sand and foam."),
    h2("methods", "Interface Level Measurement Methods"),
    INFOGRAPHIC,
    table(["Method", "What it needs", "Watch out for"],
          [["DP (hydrostatic)", "A known density difference between the two liquids", "The DP is small, so accuracy is unreliable; seal temperature effects and density changes add error"],
           ["Displacer", "A density difference; usually a side chamber", "Wear, density changes, poor resolution for small differences, resizing if the media change"],
           ["Guided wave radar", "A known, constant upper liquid dielectric and a clear dielectric difference", "Cannot see through thick emulsion; needs a straight insertion length"],
           ["Capacitance", "Lower liquid dielectric sufficiently higher than the upper one", "Automation Forum notes sensitivity to conductivity changes"],
           ["Nuclear (gamma)", "Access from outside the vessel", "High cost and regulation; usually the last option"]]),
    p("Endress+Hauser says mechanical systems can cost up to three times more than electronic ones on larger projects. Capacitance gives a stable reading even when there is no sharp interface, is not affected by density or temperature, and can be calibrated without filling the vessel. For the DP approach, our guide to " + link("/dp-level-measurement-in-closed-tanks", "DP level measurement in closed tanks") + " shows the tap arrangement, and the " + ext("https://zentacalculator.com/engineering/dp-level-range/", "DP level range calculator") + " helps size it."),
    h2("gwr", "Guided Wave Radar Limits"),
    p("Guided wave radar reads total level and interface from one probe. Endress+Hauser sets the boundary conditions below. Our " + link("/guided-wave-radar-level-measurement", "guided wave radar guide") + " covers probe choice and installation."),
    svg(_diag, "Oil, emulsion and water layers in a separator with a guided wave radar probe receiving echoes from the oil surface and the interface", 400),
    rows([
        ("Upper liquid", "Dielectric constant known, constant and below 10."),
        ("Layer thickness", "The upper layer must be more than 60 mm thick."),
        ("Dielectric difference", "More than 10 between the two liquids."),
        ("Emulsion", "Less than 50 mm thick. Automation Forum notes thin emulsions below 2 inches may still be detected."),
        ("Retrofit", "No wet calibration, density independent, and can replace a displacer in its existing chamber."),
    ], "At a glance"),
    h2("select", "Selection Checklist"),
    checklist([
        ("Total level", "Decide whether total level is constant or variable, and whether you need it as well as the interface."),
        ("Emulsion", "Thin emulsion allows radar or GWR; thick emulsion points to nuclear or a hybrid of capacitance and GWR."),
        ("Accuracy", "Automation Forum gives ±2 mm as a possible need for custody transfer and ±25 mm as enough for control."),
        ("Mounting", "Displacers and GWR usually need side chambers, and internals can block a free space radar."),
        ("Calibration cost", "Methods that need wet calibration, filling the vessel with each fluid, cost more over their life."),
        ("Safety", "A SIL target under IEC 61511 may call for 1oo2 or 2oo3 voting with a primary and backup instrument."),
    ]),
    h2("compare", "Strengths and Limits"),
    twocol([
        ("Clean oil and water", "bi-check-circle", ["DP, displacer, GWR and capacitance all suitable", "Non contact radar rated not suitable", "Choose on cost, accuracy and mounting"]),
        ("Heavy emulsion", "bi-exclamation-triangle", ["DP, displacer, radar and GWR rated not suitable", "Capacitance and hybrid partly suitable", "Nuclear rated suitable"]),
    ]),
    p("These interface level measurement ratings come from Automation Forum's suitability table. For a related article, read about the " + link("/blog/gems-uls-200-capacitive-level-sensor-uae", "Gems ULS 200 capacitive level sensor") + ", and for background see the " + ext("https://www.instrumentationblog.in/category/process-instrumentation/level-measurement/", "Instrumentation Blog level section") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Calibrating at the wrong density.", "Automation Forum advises calibrating at the real process density."),
        ("Ignoring the rag layer.", "A thick emulsion defeats DP, displacer and radar methods."),
        ("Leaving probes dirty.", "Clean probes regularly and keep stilling wells calm."),
    ]),
    p("Setup errors are covered in our post on " + link("/blog/level-transmitter-calibration-mistakes", "level transmitter calibration mistakes") + ". To turn a level into volume, use the " + ext("https://zentacalculator.com/engineering/horizontal-tank-volume/", "horizontal tank volume calculator") + ", and for the hydrostatic basics see " + ext("https://www.instrumentationblog.in/dp-transmitter-level-measurement/", "DP transmitter level measurement") + "."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What is interface level measurement?", "Measuring the boundary between two liquids that do not mix, such as oil on water, often together with total level."),
        ("Can guided wave radar measure interface?", "Yes, when the upper liquid dielectric is below 10, the difference is above 10 and the emulsion is thinner than 50 mm."),
        ("What works with thick emulsion?", "Nuclear gauges are rated suitable; capacitance and hybrid systems are partly suitable."),
    ]),
]
