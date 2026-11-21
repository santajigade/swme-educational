META = {
    "category": "pressure-measurement-guides",
    "title": "Pressure Gauge Accessories: Snubbers, Siphons and Gauge Valves",
    "keyword": "pressure gauge accessories",
    "subtitle": "What snubbers, siphons, throttle screws and gauge valves protect against, and how to fit them on pulsating or hot service",
    "meta_title": "Pressure Gauge Snubbers, Siphons and Gauge Valves",
    "meta_description": "Pressure gauge accessories explained: snubber types, steam siphons, throttle screws, gauge valves and block and bleed, with ratings and installation tips.",
    "summary": "Which pressure gauge accessory to fit for pulsation, steam or isolation, how each one works and the ratings that matter.",
    "card_title": "Snubbers, Siphons and Gauge Valves",
    "author": "SWME Technical Staff",
    "published": "2026-11-21",
    "status": "published",
    "sort_order": 6,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "compare",
        "title": "Snubber vs Siphon vs Gauge Valve",
        "alt": "Infographic comparing a pressure gauge snubber, a steam siphon and a gauge valve by what each protects against",
        "steps": [
            ["Snubber", "Damps pulses and pressure peaks from pumps and compressors."],
            ["Siphon", "Holds condensate so steam never reaches the gauge."],
            ["Gauge valve", "Isolates the gauge for protection or removal."],
        ],
        "columns": [
            ["Snubber", ["Fights pulsation and spikes", "Porous disc, piston or adjustable", "Pumps, compressors, hydraulics", "Does not change process pressure"]],
            ["Siphon", ["Fights live steam and heat", "Pigtail, coil or compact", "Fill with water before fitting", "Refinery and power plant steam"]],
            ["Gauge valve", ["Isolates the instrument", "Needle valve or block and bleed", "Lets you remove the gauge", "Mounts directly to the gauge"]],
        ],
    },
}

_C = "#5f3dc4"
_T = "#3b2a8c"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_diag = (
    '<defs><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="#c92a2a"/></marker></defs>'
    # steam header
    + '<rect x="60" y="400" width="680" height="44" fill="#fff5f5" stroke="#495057" stroke-width="2"/>'
    + _t(80, 428, "Steam header", 13, fill="#c92a2a")
    + '<line x1="560" y1="422" x2="700" y2="422" stroke="#c92a2a" stroke-width="3" marker-end="url(#ahs)"/>'
    # tap
    + '<rect x="292" y="350" width="16" height="50" fill="#dee2e6" stroke="#495057" stroke-width="2"/>'
    # gauge valve (bowtie)
    + '<polygon points="270,320 270,350 300,335" fill="#fff" stroke="#495057" stroke-width="2"/>'
    + '<polygon points="330,320 330,350 300,335" fill="#fff" stroke="#495057" stroke-width="2"/>'
    + '<line x1="300" y1="335" x2="300" y2="305" stroke="#495057" stroke-width="2"/>'
    + '<line x1="285" y1="305" x2="315" y2="305" stroke="#495057" stroke-width="3"/>'
    + '<line x1="300" y1="350" x2="300" y2="350"/>'
    # pipe from valve up to siphon
    + '<rect x="292" y="270" width="16" height="35" fill="#dee2e6" stroke="#495057" stroke-width="2"/>'
    # pigtail loop with water
    + '<path d="M300,270 C300,225 360,225 360,195 C360,160 240,160 240,195 C240,225 300,225 300,180" fill="none" stroke="#495057" stroke-width="14"/>'
    + '<path d="M300,270 C300,225 360,225 360,195 C360,160 240,160 240,195 C240,225 300,225 300,180" fill="none" stroke="#74c0fc" stroke-width="8"/>'
    # snubber
    + '<rect x="285" y="140" width="30" height="40" rx="4" fill="' + _C + '"/>'
    # gauge
    + '<line x1="300" y1="140" x2="300" y2="122" stroke="#495057" stroke-width="6"/>'
    + '<circle cx="300" cy="72" r="50" fill="#fff" stroke="' + _C + '" stroke-width="4"/>'
    + '<circle cx="300" cy="72" r="4" fill="#343a40"/>'
    + '<line x1="300" y1="72" x2="326" y2="46" stroke="#c92a2a" stroke-width="3"/>'
    # leader lines and labels
    + '<line x1="352" y1="72" x2="430" y2="72" stroke="#adb5bd" stroke-width="1.5"/>'
    + _t(440, 68, "Pressure gauge", 14) + _t(440, 88, "reads the cooled, damped pressure", 12, "400", "#555")
    + '<line x1="318" y1="160" x2="430" y2="160" stroke="#adb5bd" stroke-width="1.5"/>'
    + _t(440, 156, "Snubber", 14) + _t(440, 176, "damps pulses and spikes", 12, "400", "#555")
    + '<line x1="366" y1="205" x2="430" y2="225" stroke="#adb5bd" stroke-width="1.5"/>'
    + _t(440, 222, "Siphon (pigtail)", 14) + _t(440, 242, "trapped water keeps steam off the gauge", 12, "400", "#555")
    + '<line x1="334" y1="335" x2="430" y2="310" stroke="#adb5bd" stroke-width="1.5"/>'
    + _t(440, 306, "Gauge valve", 14) + _t(440, 326, "isolates the gauge for removal", 12, "400", "#555")
    + _t(40, 320, "Typical steam gauge point", 14)
    + _t(40, 340, "process at the bottom, gauge at the top", 12, "400", "#555")
    + _t(226, 200, "Water", 12, "600", "#1864ab", "end")
)

BODY = [
    takeaways([
        "Snubbers suppress pressure pulses and peaks, which WIKA names as common reasons for gauge failure.",
        "A siphon holds condensate between steam and the gauge. Ashcroft puts a gauge's operating rating at 200 to 250 °F (93 to 121 °C).",
        "Fill a siphon with water before you fit it.",
        "A gauge valve or block and bleed valve lets you isolate the gauge and take it off without shutting the line.",
    ]),
    p("WIKA names pressure pulses and peaks as common reasons for gauge failure, and live steam and service access bring their own problems. Each is handled by one of three <strong>pressure gauge accessories</strong>: a snubber, a siphon or a gauge valve. SWME supplies " + link("/gauge-accessories", "gauge accessories") + " and " + link("/pressure-gauges", "pressure gauges") + " for plants across the UAE and GCC."),
    toc([("how", "How pressure gauge accessories work"), ("snubbers", "Snubbers and throttle screws"), ("siphons", "Siphons for steam"),
         ("valves", "Gauge valves and block and bleed"), ("select", "Selection checklist"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("how", "How Pressure Gauge Accessories Work"),
    p("Pressure gauge accessories each deal with one problem. A snubber slows the pressure change reaching the gauge, a siphon puts a column of cool water between the gauge and hot media, and a gauge valve shuts the gauge off from the line. The diagram below shows all three stacked on one steam tapping."),
    INFOGRAPHIC,
    svg(_diag, "Steam gauge point: gauge valve on the tapping, a pigtail siphon holding water, a snubber, then the pressure gauge", 460),
    h2("snubbers", "Snubbers and Throttle Screws"),
    p("WIKA's " + ext("https://blog.wika.com/en/knowhow/fittings-pressure-gauges-mitigating-effects-dynamic-load-cycles/", "guide to dynamic load cycles") + " says they often come from pump surges and show up as a fluctuating pointer, and that they eventually shorten the gauge's service life. Its " + ext("https://www.wika.com/en-us/910_12_100_910_12_200_910_12_300.WIKA", "910.12 snubber page") + " lists reciprocating pumps, compressors, hydraulic presses and fluid power systems as typical duties. As " + ext("https://tameson.com/pages/pressure-gauge-snubber", "Tameson") + " notes, a snubber does not change the process pressure itself."),
    table(["Type", "How it works", "Notes from the sources"],
          [["Porous disc", "A fixed mesh disc restricts flow to the gauge", "Cheapest type. It can clog, is cleaned with solvent from the gauge side and cannot be tuned (Tameson)"],
           ["Piston", "A free piston moves against the orifice when pressure rises quickly", "Self cleaning. Tuned by changing the piston; WIKA supplies five pistons"],
           ["Adjustable", "A needle valve restricts flow ahead of a piston snubber", "Some have a tight shutoff so the gauge can be removed (Tameson)"],
           ["Throttle screw", "A restrictor that fits completely inside the gauge socket", "Ashcroft calls it economical; threaded versions come out for cleaning"]]),
    rows([
        ("WIKA 910.12 ratings", "Brass 3000 to 5000 psi, stainless steel 5000 to 15,000 psi, media temperature minus 10 to 120 °C, 1/4 or 1/2 NPT."),
        ("Ashcroft 1112 disc grades", "D for oil, E for water and light oils, G for air, steam and gases, HX for mercury. Ashcroft says its large filter area makes it less prone to clog than orifice type devices."),
        ("Material", "Tameson advises against brass for salt water, seawater, distilled water, acids and chlorides."),
    ], "At a glance"),
    p("Tameson adds that a liquid filled gauge can do the same job as a snubber at a higher cost, and the two can be combined. For pressure surges in the line itself, the " + ext("https://zentacalculator.com/engineering/water-hammer/", "water hammer calculator") + " estimates the pressure rise."),
    h2("siphons", "Siphons for Steam"),
    p("A siphon is a looped tube between the line and the gauge. In " + ext("https://blog.ashcroft.com/how-do-siphons-work", "Ashcroft's explanation") + ", steam cools and condenses in the loop, so only cooler liquid reaches the instrument. Gauges are commonly rated for 200 to 250 °F (93 to 121 °C), and Ashcroft warns that even low temperature steam can go past that."),
    rows([
        ("Pigtail", "Made for vertical piping."),
        ("Coil", "Works on vertical or horizontal piping; a small dip in the loop traps the water."),
        ("Compact", "WIKA's " + ext("https://www.wika.com/en-us/910_24.WIKA", "910.24 mini siphon") + " replaces the pigtail and coil, with an inner chamber that reduces surges and water hammer."),
        ("Finned and microtube", "Ashcroft's finned siphon cools media from up to 700 °F and is rated to 3,000 psi. Its MicroTube, in 316L stainless steel, handles up to 800 °F and 5,000 psi."),
    ]),
    dyk("Boshart gives a rough figure of about 75 °F of cooling for each 12 inch section of 1/2 inch pipe, and says the real figure depends on the process. Its " + ext("https://support.boshart.com/what-does-a-siphon-do", "siphon note") + " also lists pressure switches, controllers and recorders as instruments a siphon protects."),
    h2("valves", "Gauge Valves and Block and Bleed"),
    p("Ashcroft describes a gauge valve as mounting directly to the instrument to isolate it for protection or removal. A two valve block and bleed adds a vent so you can release trapped pressure before you unscrew the gauge. For differential pressure instruments, three and five valve manifolds isolate, equalise and bleed. See SWME " + link("/manifolds-fittings", "manifolds and fittings") + "."),
    twocol([
        ("Single gauge valve", "bi-sliders", ["Isolates the gauge", "Mounts directly to the instrument", "Needle valves also throttle"]),
        ("Block and bleed", "bi-shield-check", ["Isolates the gauge", "Adds a bleed for the media", "Mounts directly to the instrument"]),
    ]),
    h2("select", "Selection Checklist"),
    checklist([
        ("Problem", "Pulsation calls for a snubber, steam or hot media for a siphon, and removal under pressure for a valve."),
        ("Pressure rating", "Tameson warns that a lower rated snubber on a high pressure system will be a problem."),
        ("Temperature", "Check the snubber's media limit, and fit a siphon wherever steam can reach the gauge."),
        ("Threads", "Match the line and the gauge connection, for example 1/2 NPT."),
        ("Material", "Use stainless steel where brass is not suitable."),
        ("Gauge choice", "Read our " + link("/how-to-select-a-pressure-gauge", "pressure gauge selection guide") + ", and for corrosive or viscous media see " + link("/diaphragm-seals-explained", "diaphragm seals") + "."),
    ]),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Fitting a dry siphon.", "Ashcroft and Boshart both say to fill it with water first."),
        ("Leaving a porous snubber in dirty service.", "Tameson notes the disc can clog."),
        ("No isolation valve.", "Without one the gauge cannot be removed without shutting the line."),
    ]),
    p("More background is in the " + ext("https://www.instrumentationblog.in/category/process-instrumentation/pressure-measurement/", "Instrumentation Blog pressure section") + ", and switches can use the same pressure gauge accessories; see " + link("/pressure-switches", "pressure switches") + "."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Does a snubber change the pressure reading?", "No. Tameson says it damps spikes and pulses without altering the process pressure."),
        ("Do I need a siphon on every steam gauge?", "Ashcroft says siphons should be used wherever instruments need protecting from live steam."),
        ("Can a liquid filled gauge replace a snubber?", "Tameson says it can serve the same purpose at a higher cost, and the two can be used together."),
    ]),
]
