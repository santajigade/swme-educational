META = {
    "category": "flow-measurement-guides",
    "title": "Straight Pipe Run Requirements for Flow Meters",
    "keyword": "straight pipe run",
    "subtitle": "Why bends, valves and pumps upset a flow meter, how many pipe diameters each meter type needs upstream and downstream, what flow conditioners save, and how to spot a short run",
    "meta_title": "Straight Pipe Run Requirements for Flow Meters",
    "meta_description": "Straight pipe run for flow meters: why swirl causes errors, upstream and downstream diameters by meter type, flow conditioners and a worked example.",
    "summary": "How many pipe diameters of straight pipe run each flow meter needs, why bends and valves cause errors, and what flow conditioners and good layout can save.",
    "card_title": "Straight Pipe Run for Flow Meters",
    "author": "SWME Technical Staff",
    "published": "2026-11-26",
    "status": "published",
    "sort_order": 9,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "grid",
        "title": "Typical Minimum Straight Runs by Meter",
        "alt": "Infographic grid of typical minimum upstream and downstream straight runs for electromagnetic, clamp on ultrasonic, vortex, turbine, orifice and Coriolis meters",
        "steps": [
            ["Electromagnetic", "5 D upstream, 2 D downstream (KROHNE)."],
            ["Clamp on ultrasonic", "10 D upstream, 5 D downstream as a typical minimum (Siemens)."],
            ["Vortex", "10 D and 5 D minimum; 35 D upstream for reference accuracy (Rosemount 8800D)."],
            ["Turbine", "At least 10 D upstream and 5 D downstream (Seametrics)."],
            ["Orifice plate", "16 D after one bend at beta 0.4, 44 D at beta 0.65 (ISO 5167)."],
            ["Coriolis", "No inlet or outlet run requirements (Promass 80E and 83E)."],
        ],
    },
}

_C = "#1971c2"
_T = "#14508a"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


def _arrows(x, lens, col):
    out = ""
    ys = [148, 160, 172, 184, 196]
    for y, ln in zip(ys, lens):
        out += f'<line x1="{x}" y1="{y}" x2="{x + ln}" y2="{y}" stroke="{col}" stroke-width="2.5" marker-end="url(#va)"/>'
    return out


_diag = (
    '<defs><marker id="va" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#c92a2a"/></marker>'
    '<marker id="da" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#495057"/></marker></defs>'
    # vertical pipe into elbow (same 80 px bore as the horizontal pipe)
    + '<path d="M70 40 L70 176 Q70 216 110 216 L150 216 L150 40 Z" fill="#eef5fd"/>'
    + '<path d="M70 40 L70 176 Q70 216 110 216 L150 216" fill="none" stroke="#495057" stroke-width="3"/>'
    + '<path d="M150 40 L150 136" fill="none" stroke="#495057" stroke-width="3"/>'
    + '<line x1="110" y1="50" x2="110" y2="110" stroke="#c92a2a" stroke-width="2.5" marker-end="url(#va)"/>'
    + _t(110, 30, "Elbow", 13, "700", "#495057")
    # straight pipe
    + '<rect x="150" y="136" width="300" height="80" fill="#eef5fd"/>'
    + '<line x1="150" y1="136" x2="450" y2="136" stroke="#495057" stroke-width="3"/>'
    + '<line x1="150" y1="216" x2="450" y2="216" stroke="#495057" stroke-width="3"/>'
    # skewed profile near elbow (faster at outside of bend = bottom)
    + _arrows(170, [18, 26, 36, 48, 56], "#c92a2a")
    # developed profile before meter
    + _arrows(380, [26, 44, 52, 44, 26], "#c92a2a")
    # meter
    + '<rect x="450" y="116" width="80" height="120" rx="8" fill="#d0ebff" stroke="#1971c2" stroke-width="3"/>'
    + _t(490, 172, "Flow", 14) + _t(490, 190, "meter", 14)
    # downstream pipe
    + '<rect x="530" y="136" width="230" height="80" fill="#eef5fd"/>'
    + '<line x1="530" y1="136" x2="760" y2="136" stroke="#495057" stroke-width="3"/>'
    + '<line x1="530" y1="216" x2="760" y2="216" stroke="#495057" stroke-width="3"/>'
    # control valve downstream (bowtie) at x=690
    + '<polygon points="670,146 690,176 670,206" fill="#ffe8cc" stroke="#d9480f" stroke-width="2"/>'
    + '<polygon points="710,146 690,176 710,206" fill="#ffe8cc" stroke="#d9480f" stroke-width="2"/>'
    + '<line x1="690" y1="176" x2="690" y2="106" stroke="#d9480f" stroke-width="2.5"/>'
    + '<rect x="672" y="92" width="36" height="14" rx="3" fill="#d9480f"/>'
    + _t(690, 80, "Control valve", 13, "700", "#d9480f")
    # dimensions
    + '<line x1="150" y1="226" x2="150" y2="262" stroke="#868e96"/><line x1="450" y1="240" x2="450" y2="262" stroke="#868e96"/>'
    + '<line x1="156" y1="254" x2="444" y2="254" stroke="#495057" stroke-width="1.8" marker-start="url(#da)" marker-end="url(#da)"/>'
    + _t(300, 280, "Upstream straight run, for example 10 D", 13, "700", "#495057")
    + '<line x1="530" y1="240" x2="530" y2="262" stroke="#868e96"/><line x1="670" y1="214" x2="670" y2="262" stroke="#868e96"/>'
    + '<line x1="536" y1="254" x2="664" y2="254" stroke="#495057" stroke-width="1.8" marker-start="url(#da)" marker-end="url(#da)"/>'
    + _t(600, 280, "Downstream, 5 D", 13, "700", "#495057")
    + _t(158, 124, "Skewed profile after the bend", 12, "400", "#c92a2a", "start")
    + _t(440, 124, "Developed profile", 12, "400", "#c92a2a", "end")
    + _t(400, 320, "D = internal pipe diameter. Lengths drawn to a 10 D : 5 D ratio.", 12, "400", "#555")
)

BODY = [
    takeaways([
        "Bends, valves and reducers leave the flow skewed or swirling, and most meters then read high or low. Swirl can take well over 100 diameters to decay.",
        "Upstream length matters more than downstream length. Typical minimums run from 5 D for a magnetic meter to 60 D for an orifice plate at beta 0.65 behind bends in different planes.",
        "Flow conditioners shorten the run, for example from 50 D to 30 D for an orifice plate at beta 0.4, but they do not replace straight pipe.",
        "Put control and isolation valves downstream of the meter, and keep isolation valves fully open or fully closed.",
    ]),
    p("A <strong>straight pipe run</strong> is the length of unobstructed pipe, counted in internal diameters (D), that a flow meter needs before and after it so the flow reaches the sensor in a settled state. Every meter SWME supplies, from " + link("/flowmeters", "flowmeters") + " to " + link("/orifice-plates", "orifice plates") + ", comes with straight run figures in its manual, and they belong on the piping layout before the line is built."),
    toc([("why", "Why the flow profile matters"), ("table", "Straight pipe run by meter type"), ("orifice", "Orifice plates and ISO 5167"),
         ("example", "Worked example"), ("conditioners", "Flow conditioners"), ("layout", "Layout rules"), ("symptoms", "Signs of a short run"),
         ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("why", "Why the Flow Profile Matters"),
    p("McCrometer's article on " + ext("https://www.mccrometer.com/the-challenge-of-flow-disturbances-on-meter-accuracy/", "flow disturbances and meter accuracy") + " names the two common disturbances as asymmetric velocity profiles and swirl. Two elbows out of plane can create swirl, and disturbances can make meters read high or low, with errors of over 50 percent for certain meters after a butterfly valve.",
      "Bell Flow Systems' " + ext("https://www.bellflowsystems.co.uk/images/filemanager/uploads/PDF/an_introduction_to_flow_meter_installation_effects.pdf", "introduction to installation effects") + " adds the numbers behind a settled flow. In turbulent flow, above a Reynolds number of about 5,000, the centre velocity is 1.1 to 1.3 times the average; in laminar flow it is twice the average. A bend skews that profile, and swirl can take well over 100 pipe diameters to decay. The " + ext("https://zentacalculator.com/engineering/reynolds-number/", "Reynolds number calculator") + " tells you which regime your line is in from density, velocity, diameter and viscosity."),
    svg(_diag, "An elbow skews the velocity profile. The upstream straight run lets it settle before the meter, and the control valve sits downstream", 340),
    p("Processing Magazine notes that most flowmeter designs are more affected by the upstream straight run than the downstream one, and the figures below follow that pattern."),
    h2("table", "Straight Pipe Run by Meter Type"),
    p("The figures below are typical minimums from manufacturer documents. Always check the manual of the exact model, because the fitting upstream changes the answer."),
    INFOGRAPHIC,
    table(["Meter type", "Upstream", "Downstream", "Source and notes"], [
        ["Electromagnetic", "5 D", "2 D", ext("https://cdn.krohne.com/archive/TD_MID_INSTALL_e_72.pdf", "KROHNE installation guide") + ", measured from the electrode axis"],
        ["Clamp on ultrasonic", "10 D", "5 D", ext("https://cache.industry.siemens.com/dl/files/334/109765334/att_978425/v1/sitransf_fs220_fi01_en.pdf", "Siemens SITRANS FS220") + "; more for double elbows out of plane or partly open valves"],
        ["Vortex", "10 D minimum, 35 D for reference accuracy", "5 D", ext("https://emerson.com/documents/automation/reference-manual-rosemount-8800d-series-vortex-flow-meter-hart-en-76126.pdf", "Rosemount 8800D manual") + "; the K factor may shift up to 0.5% at 10 D"],
        ["Turbine", "At least 10 D", "5 D", "Seametrics; 20 D after two elbows out of plane, 50 D after a partly open butterfly valve"],
        ["Coriolis", "None", "None", ext("https://portal.endress.com/wa001/dla/5000000/0221/000/08/TI00061DEN_1515.pdf", "Endress+Hauser Promass 80E/83E") + ", provided no cavitation occurs"],
    ]),
    p("Our guides to the " + link("/electromagnetic-flow-meter-working-principle", "electromagnetic flow meter") + " and the " + link("/vortex-flow-meter-working-principle", "vortex flow meter") + " explain why each principle reacts to a distorted profile the way it does. For clamp on meters, the article on the " + link("/blog/xft-clamp-on-ultrasonic-flow-meter-uae", "XFT clamp on ultrasonic flow meter") + " covers a model sold in the UAE."),
    dyk("Rosemount quotes 10 D upstream as the minimum for its 8800D vortex meter but 35 D upstream to reach reference accuracy. At the 10 D minimum, the K factor may shift by up to 0.5%."),
    h2("orifice", "Orifice Plates and ISO 5167"),
    p("For a differential pressure meter the straight pipe run depends on the beta ratio (bore over pipe diameter) as well as the fitting. Emerson's " + ext("https://emerson.com/documents/automation/technical-note-conditioning-orifice-plate-technology-taking-standard-to-a-new-level-of-capability-rosemount-en-77742.pdf", "technical note on conditioning orifice plates") + " reproduces the ISO 5167 values, with the figure after a 19 tube bundle in brackets:"),
    table(["Upstream fitting", "Beta 0.4", "Beta 0.65"], [
        ["Single 90° bend", "16 D", "44 D (30 D)"],
        ["Two or more bends in different planes", "50 D (30 D)", "60 D (30 D)"],
        ["Reducer", "5 D", "12 D"],
        ["Valve", "12 D", "18 D"],
        ["Downstream of the plate", "6 D", "7 D"],
    ]),
    p("The same note says a conditioning orifice plate needs only 2 D upstream of a disturbance and 2 D downstream. Our " + link("/orifice-plate-flow-measurement-basics", "orifice plate guide") + " covers the meter itself, and the " + ext("https://zentacalculator.com/engineering/orifice-flow/", "orifice plate flow calculator") + " works out the beta ratio and flow from bore, pipe ID and differential pressure."),
    h2("example", "Worked Example"),
    p("A 4 inch (DN100) Schedule 40 steel pipe has an outside diameter of 114.3 mm and a 6.02 mm wall, so the internal diameter is 102.26 mm, from the " + ext("https://engineeringtoolbox.com/asme-steel-pipes-sizes-d_42.html", "ASME steel pipe size table") + ". Multiply to get lengths:"),
    rows([
        ("Magnetic meter, 5 D / 2 D", "0.51 m upstream and 0.20 m downstream. KROHNE counts D as the meter size, so 5 × 100 mm = 0.5 m."),
        ("Vortex minimum, 10 D / 5 D", "1.02 m upstream and 0.51 m downstream."),
        ("Vortex reference accuracy, 35 D", "3.58 m upstream, which is often the hardest length to find on a skid."),
    ], "DN100 Schedule 40, ID 102.26 mm"),
    p("The " + ext("https://zentacalculator.com/engineering/pipe-flow-velocity/", "pipe flow velocity calculator") + " gives the velocity from flow and internal diameter, which you need anyway to check the meter range."),
    h2("conditioners", "Flow Conditioners"),
    p("Bell Flow separates straighteners, usually tube bundles, which remove swirl but not asymmetry, from conditioners, which are plates with holes and remove both at a higher pressure loss."),
    twocol([
        ("Tube bundle straightener", "bi-grid-3x3", ["Removes swirl", "Leaves an asymmetric profile", "ISO 5167, beta 0.4, bends in different planes: 50 D down to 30 D"]),
        ("Perforated plate conditioner", "bi-circle", ["Removes swirl and asymmetry", "Higher pressure loss", "Endress+Hauser: reduces the vortex inlet run to 10 DN"]),
    ]),
    p("For the CPA 50E plate, Measurement Canada's " + ext("https://ic.gc.ca/pics/lm/gas/ag/0560r2.pdf", "approval AG 0560") + " sets at least 9 diameters of total upstream run for orifice and ultrasonic meters, with at least 6 between plate and meter; at least 4 between plate and meter for turbines; and 13 and 8 for vortex meters. Seametrics puts it plainly: a flow straightener is not a substitute for the correct straight run."),
    h2("layout", "Layout Rules"),
    checklist([
        ("Fix the meter type before the piping", "The straight pipe run ranges from none for a Coriolis meter to 60 D for an orifice plate behind bends, so the choice drives the layout."),
        ("Identify the worst upstream fitting", "Two bends out of plane or a partly open valve need far more than a single bend or reducer."),
        ("Put valves downstream", "KROHNE: always install control and shutoff valves downstream of the meter. ABB adds that isolation valves must be fully open or fully closed."),
        ("Keep magnetic meters off pump suction", "KROHNE warns against the suction side because of vacuum."),
        ("Place pressure and temperature taps downstream", "The Rosemount 8800D manual shows them downstream of a vortex meter, at four and six diameters."),
    ]),
    h2("symptoms", "Signs of a Short Run"),
    p("A short straight pipe run rarely shows as a fault alarm. Unitecd lists a consistent high or low reading with less than 10 D of straight run as a likely cause, and suggests suspecting installation effects after any piping change, then checking with a clamp on meter. A differential pressure signal may become highly erratic. Our article on " + link("/blog/flow-meter-incorrect-readings-causes-fixes", "incorrect flow meter readings") + " covers the other causes, and more " + ext("https://www.instrumentationblog.in/category/process-instrumentation/flow-measurement/", "flow measurement articles") + " cover individual meter types."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Counting the run from the wrong point.", "KROHNE measures from the electrode axis; check what your meter's manual uses."),
        ("Throttling upstream of the meter.", "A partly open valve can need 50 D on a turbine meter. Throttle downstream."),
        ("Treating a conditioner as a cure.", "It shortens the run but does not remove the need for one."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What does 10 D mean?", "Ten internal pipe diameters. On DN100 Schedule 40 pipe with a 102.26 mm bore, that is about 1.02 m."),
        ("Which meter needs the least straight pipe run?", "Coriolis. The Promass 80E and 83E have no inlet or outlet run requirements, provided there is no cavitation."),
        ("Is downstream straight pipe needed at all?", "Yes, but less. Typical figures are 2 D for a magnetic meter and 5 D for vortex, turbine and clamp on ultrasonic meters."),
    ]),
]
