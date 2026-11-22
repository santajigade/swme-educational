META = {
    "category": "industrial-valve-guides",
    "title": "Safety Relief Valve Basics: Set Pressure, Accumulation and Blowdown",
    "keyword": "safety relief valve",
    "subtitle": "How a spring loaded safety relief valve opens and reseats, the key pressure terms, valve types and installation rules",
    "meta_title": "Safety Relief Valve Basics: How They Work",
    "meta_description": "Safety relief valve basics: safety vs relief valves, set pressure, overpressure, accumulation and blowdown, bellows and pilot valves, installation tips.",
    "summary": "How a safety relief valve protects a vessel, what set pressure, accumulation and blowdown mean, and how to install one correctly.",
    "card_title": "Safety Relief Valve Basics",
    "author": "SWME Technical Staff",
    "published": "2026-11-22",
    "status": "published",
    "sort_order": 6,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "grid",
        "title": "Four Pressure Terms for Relief Valves",
        "alt": "Infographic explaining set pressure, overpressure, accumulation and blowdown for a safety relief valve",
        "steps": [
            ["Set pressure", "The gauge pressure at which the valve starts to lift."],
            ["Overpressure", "The pressure rise above set pressure while the valve relieves."],
            ["Accumulation", "The pressure rise above the MAWP of the protected system."],
            ["Blowdown", "The difference between the popping pressure and the reseat pressure."],
        ],
    },
}

_C = "#e67700"
_T = "#a35400"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


def _lbl(x1, y1, x2, y2, tx, ty, s, anchor="start"):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#495057" stroke-width="1.5"/>'
            + _t(tx, ty, s, 13, "700", "#343a40", anchor))


_valve = (
    arrow_defs(_C)
    # inlet nozzle (vertical, from bottom)
    + '<rect x="360" y="300" width="80" height="80" fill="#e9ecef" stroke="#495057" stroke-width="2"/>'
    + '<rect x="375" y="230" width="50" height="150" fill="#ffe8cc" stroke="#495057" stroke-width="2"/>'
    # body
    + '<path d="M300,300 L300,160 L500,160 L500,300 Z" fill="none" stroke="#495057" stroke-width="3"/>'
    # outlet to the right
    + '<rect x="500" y="200" width="120" height="70" fill="#e9ecef" stroke="#495057" stroke-width="2"/>'
    + '<line x1="520" y1="235" x2="610" y2="235" stroke="' + _C + '" stroke-width="3" marker-end="url(#ah)"/>'
    # disc on nozzle
    + '<rect x="360" y="214" width="80" height="16" rx="3" fill="#343a40"/>'
    + '<path d="M355,214 L355,240 L362,240 L362,222 L438,222 L438,240 L445,240 L445,214 Z" fill="#868e96"/>'
    # spindle
    + '<rect x="395" y="70" width="10" height="144" fill="#495057"/>'
    # bonnet
    + '<rect x="340" y="60" width="120" height="100" fill="none" stroke="#495057" stroke-width="3"/>'
    # spring
    + '<path d="M370,150 L430,140 L370,130 L430,120 L370,110 L430,100 L370,90 L430,80" fill="none" stroke="' + _C + '" stroke-width="3"/>'
    + '<rect x="362" y="150" width="76" height="8" fill="#495057"/>'
    + '<rect x="362" y="72" width="76" height="8" fill="#495057"/>'
    # adjusting screw and cap
    + '<rect x="388" y="30" width="24" height="42" fill="#adb5bd" stroke="#495057" stroke-width="1.5"/>'
    # inlet arrow
    + '<line x1="400" y1="395" x2="400" y2="320" stroke="' + _C + '" stroke-width="3" marker-end="url(#ah)"/>'
    # labels
    + _lbl(388, 40, 250, 40, 245, 45, "Adjusting screw", "end")
    + _lbl(370, 115, 250, 100, 245, 105, "Spring pushes the disc down", "end")
    + _lbl(395, 190, 250, 175, 245, 180, "Spindle", "end")
    + _lbl(356, 230, 250, 250, 245, 255, "Disc and huddling chamber", "end")
    + _lbl(375, 300, 250, 320, 245, 325, "Nozzle", "end")
    + _t(415, 395, "Inlet pressure lifts the disc", 13, "700", _T)
    + _t(630, 225, "Outlet", 13, "700", _T)
    + _t(630, 243, "to discharge", 12, "400", "#555")
    + _t(470, 100, "Bonnet", 13, "700", "#343a40")
    + _t(470, 118, "installed vertically upwards", 12, "400", "#555")
)


def _bar():
    out = []
    y0, y1 = 300, 40   # pressure 90% at y0, 125% at y1

    def yy(pct):
        return y0 - (pct - 90) / 35 * (y0 - y1)
    out.append('<line x1="160" y1="300" x2="160" y2="30" stroke="#495057" stroke-width="2"/>')
    out.append(_t(150, 24, "Pressure as % of MAWP", 12, "700", "#495057", "start"))
    for pct, lab, col in [(100, "100%: MAWP and set pressure of a single valve", "#343a40"),
                          (110, "110%: maximum accumulation, single valve", _C),
                          (116, "116%: maximum accumulation, multiple valves", "#d9480f"),
                          (121, "121%: maximum accumulation, fire case", "#c92a2a")]:
        y = yy(pct)
        out.append(f'<line x1="150" y1="{y:.0f}" x2="760" y2="{y:.0f}" stroke="{col}" stroke-width="2" stroke-dasharray="7 5"/>')
        out.append(_t(180, y - 8, lab, 13, "700", col))
    out.append(f'<rect x="130" y="{yy(100):.0f}" width="20" height="{yy(90) - yy(100):.0f}" fill="#d3f9d8"/>')
    out.append(_t(180, yy(95) + 5, "Operate at least 10% or 5 psig below set pressure (Kunkle)", 12, "400", "#2b8a3e"))
    return "".join(out)


BODY = [
    takeaways([
        "A safety relief valve opens automatically when pressure reaches its set pressure and closes again once pressure falls.",
        "Safety valves pop open on gas and steam; relief valves open in proportion to the rise on liquids; a safety relief valve does both.",
        "Under ASME Section VIII, accumulation is limited to 10% over MAWP for a single valve, 16% for multiple valves and 21% for fire.",
        "Inlet pressure loss should stay within 3% of set pressure, and the bonnet should point vertically upwards.",
    ]),
    p("A <strong>safety relief valve</strong> protects a pressure vessel, boiler or pipeline from overpressure. Inlet static pressure opens it, so it needs no power or signal. SWME supplies " + link("/safety-relief-valves", "safety relief valves") + ", " + link("/pressure-reducing-valves", "pressure reducing valves") + " and other " + link("/industrial-valves", "industrial valves") + " for plants across the UAE and GCC."),
    toc([("types", "Safety, relief and safety relief valves"), ("how", "How it works"), ("terms", "Key pressure terms"),
         ("designs", "Conventional, bellows and pilot valves"), ("install", "Installation and testing"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("types", "Safety Valve, Relief Valve or Safety Relief Valve"),
    rows([
        ("Safety valve", "Spirax Sarco describes it as actuated by inlet static pressure, with rapid opening or pop action. It is used on steam and gases."),
        ("Relief valve", "Opens with a gradual lift that is generally proportional to the overpressure. It is typically used on incompressible fluids such as water and oil."),
        ("Safety relief valve", "Opens with pop action or in proportion to the pressure rise, so it works as a safety valve on gas and as a relief valve on liquid."),
    ]),
    p("This " + ext("https://www.spiraxsarco.com/learn-about-steam/safety-valves/safety-valves", "introduction to safety valves") + " covers the code definitions in more detail. For how these valves fit with the other families, see our guide to " + link("/types-of-industrial-valves", "types of industrial valves") + "."),
    h2("how", "How a Safety Relief Valve Works"),
    p("A spring holds the disc down on the nozzle. The set point is adjusted by turning the adjusting nut to change the spring compression. When inlet pressure on the disc overcomes the spring force, the disc lifts. Fluid then enters the huddling chamber, the annular space between the nozzle exit and the disc holder. This exposes a larger area, the opening force rises and the valve pops open.",
      "With the larger area still exposed, the valve does not reclose at set pressure. Pressure has to fall below it first, and that gap is the blowdown. The " + ext("https://instrumentationtools.com/relief-and-safety-valves", "relief and safety valve overview") + " also notes that a lever on safety valves is used as an operational check."),
    svg(_valve, "Spring loaded safety relief valve: inlet pressure under the disc works against the spring, and the huddling chamber makes the valve pop open", 410),
    h2("terms", "Key Pressure Terms"),
    INFOGRAPHIC,
    table(["Term", "Definition (Spirax Sarco)"],
          [["Set pressure", "The gauge pressure at which direct loaded safety valves commence to lift under operating conditions"],
           ["Overpressure", "A pressure increase over the set pressure of the valve"],
           ["Accumulation", "The increase in pressure over the MAWP of the system being protected"],
           ["Blowdown", "The difference between actual popping pressure and actual reseating pressure"],
           ["MAWP", "The maximum gauge pressure permitted at the top of a completed vessel at a designated temperature"],
           ["Cold differential test pressure", "The pressure at which the valve is set on a test rig at ambient temperature, corrected for back pressure and high temperature"],
           ["Superimposed back pressure", "The gauge pressure on the outlet side of the closed valve"],
           ["Built up back pressure", "The gauge pressure built up at the outlet while the valve is blowing"]]),
    p("The Emerson " + ext("https://www.emerson.com/documents/automation/pressure-relief-valve-engineering-handbook-fr-ca-4259986.pdf", "pressure relief valve engineering handbook") + " gives the ASME Section VIII accumulation limits shown below. For valves with adjustable blowdown, it says the typical reseat pressure is 7% to 10% below set pressure."),
    svg(_bar(), "ASME Section VIII accumulation limits as a percentage of MAWP for a single valve, multiple valves and a fire case", 320),
    p("Spirax Sarco gives typical overpressure of 3% to 10% for compressible fluids and 10% to 25% for liquids, and typical blowdown below 10% for gases and up to 20% for liquids. The Kunkle technical reference advises keeping operating pressure at least 5 psig or 10% below set pressure, whichever is greater. Set pressure is a gauge value; the " + ext("https://zentacalculator.com/engineering/absolute-gauge-pressure/", "absolute and gauge pressure calculator") + " converts it when a datasheet quotes absolute pressure."),
    dyk("API Standard 527 tests seat tightness at 90% of set pressure. Emerson notes that a soft seated valve must show no leakage at all at that pressure."),
    h2("designs", "Conventional, Balanced Bellows and Pilot Operated Valves"),
    twocol([
        ("Conventional spring loaded", "bi-arrow-up-circle", [
            "The spring acts directly on the disc",
            "Emerson: built up back pressure should not exceed 10% of set pressure at 10% overpressure"]),

        ("Balanced bellows", "bi-shield-check", [
            "Built for higher back pressure than a conventional valve",
            "Emerson: total back pressure up to 30% of set pressure with no capacity loss",
            "Limits vary by maker, so check the datasheet"]),
    ]),
    p("In a pilot operated valve, system pressure sits on top of a piston and holds the main valve shut. When the pilot vents that space, inlet pressure opens the main valve. Valve size is often given as an API 526 orifice letter, from D at 0.110 in² to T at 26.00 in², as listed in this " + ext("https://neutrium.net/articles/equipment/relief-valve-orifice-area-to-api-rp-526/", "table of API 526 orifice areas") + "."),
    h2("install", "Installation and Testing"),
    checklist([
        ("Mount it upright", "Spirax Sarco says safety valves should always be installed with the bonnet vertically upwards."),
        ("Limit inlet loss", "ASME VIII Appendix M limits inlet losses to 3% of set pressure; higher losses cause chatter."),
        ("Size the pipes", "Inlet and outlet piping must be at least as large as the valve connections."),
        ("Slope the discharge", "Horizontal runs need a fall of at least 1 in 100 so fluid cannot collect."),
        ("Lock block valves open", "Any block valve must be car sealed open and logged, and closed only for inspection, test or repair."),
        ("Test on a schedule", "Emerson notes API 576 intervals may be as long as ten years, but service history should set the schedule."),
    ]),
    p("This " + ext("https://www.spiraxsarco.com/learn-about-steam/safety-valves/safety-valve-installation", "guide to safety valve installation") + " covers discharge piping in more detail. Our guide to " + link("/check-valve-types-explained", "check valve types") + " covers the valve that stops reverse flow, and the " + link("/blog/how-to-select-the-right-industrial-valve", "valve selection guide") + " helps match a valve to the duty. Further reading is in this " + ext("https://www.instrumentationblog.in/category/process-instrumentation/pressure-measurement/", "collection of pressure measurement articles") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Running too close to set pressure.", "Kunkle advises a margin of at least 10% or 5 psig, whichever is greater."),
        ("Ignoring back pressure.", "Emerson limits built up back pressure on a conventional valve to 10% of set pressure; above that, consider a balanced bellows valve."),
        ("Long or small inlet pipes.", "Inlet loss above 3% of set pressure makes the valve chatter."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What is the difference between overpressure and accumulation?", "Overpressure is measured above the set pressure; accumulation is measured above the MAWP of the system."),
        ("Why does the valve reseat below set pressure?", "Once open, the disc exposes a larger area, so pressure has to fall further before the spring can close it. That gap is blowdown."),
        ("Can I fit an isolation valve under a relief valve?", "Only where the code allows it, and it must be locked open. ASME Section I allows no isolation valve at all."),
    ]),
]
