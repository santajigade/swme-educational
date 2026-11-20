META = {
    "category": "pressure-measurement-guides",
    "title": "Differential Pressure Gauges and Their Applications",
    "keyword": "differential pressure gauge",
    "subtitle": "How piston, diaphragm, bellows and Bourdon designs read the difference between two pressures, and where plants use them",
    "meta_title": "Differential Pressure Gauges and Their Applications",
    "meta_description": "Differential pressure gauge guide: piston, diaphragm, bellows and Bourdon designs, working pressure, filter, flow and level uses, selection and mistakes.",
    "summary": "How a differential pressure gauge works, which sensing design suits your fluid, and how plants use DP gauges on filters, flow and level.",
    "card_title": "Differential Pressure Gauges",
    "author": "SWME Technical Staff",
    "published": "2026-11-20",
    "status": "published",
    "sort_order": 5,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "flow",
        "title": "How a DP Gauge Reads a Filter",
        "alt": "Infographic showing how a differential pressure gauge reads the pressure drop across a filter from high port to pointer",
        "steps": [
            ["High port", "Upstream pressure enters the high side of the gauge."],
            ["Low port", "Downstream pressure enters the low side."],
            ["Sensing element", "A piston, diaphragm, bellows or Bourdon element moves with the difference."],
            ["Pointer", "A magnet or linkage turns the pointer to show P1 minus P2."],
        ],
    },
}

_C = "#5f3dc4"
_T = "#3b2a8c"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_diag = (
    '<defs><marker id="ahp" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="#1971c2"/></marker></defs>'
    # pipe
    + '<rect x="40" y="250" width="720" height="50" fill="#e7f5ff" stroke="#495057" stroke-width="2"/>'
    # filter housing
    + '<rect x="330" y="225" width="140" height="100" rx="10" fill="#f1f3f5" stroke="#495057" stroke-width="2.5"/>'
    + '<line x1="400" y1="232" x2="400" y2="318" stroke="#868e96" stroke-width="10" stroke-dasharray="3 3"/>'
    + _t(400, 350, "Filter element", 13, anchor="middle", fill="#495057")
    # flow arrows
    + '<line x1="60" y1="275" x2="140" y2="275" stroke="#1971c2" stroke-width="3" marker-end="url(#ahp)"/>'
    + '<line x1="640" y1="275" x2="730" y2="275" stroke="#1971c2" stroke-width="3" marker-end="url(#ahp)"/>'
    + _t(60, 320, "Flow", 13, fill="#1864ab")
    # taps
    + '<line x1="250" y1="250" x2="250" y2="150" stroke="#495057" stroke-width="3"/>'
    + '<line x1="550" y1="250" x2="550" y2="150" stroke="#495057" stroke-width="3"/>'
    + '<line x1="250" y1="150" x2="345" y2="150" stroke="#495057" stroke-width="3"/>'
    + '<line x1="455" y1="150" x2="550" y2="150" stroke="#495057" stroke-width="3"/>'
    + _t(180, 205, "P1 upstream", 13)
    + _t(565, 205, "P2 downstream", 13)
    # gauge
    + '<circle cx="400" cy="110" r="62" fill="#fff" stroke="' + _C + '" stroke-width="4"/>'
    + '<circle cx="400" cy="110" r="5" fill="#343a40"/>'
    + '<line x1="400" y1="110" x2="430" y2="70" stroke="#c92a2a" stroke-width="3"/>'
    + '<rect x="345" y="140" width="20" height="20" fill="' + _C + '"/>'
    + '<rect x="435" y="140" width="20" height="20" fill="' + _C + '"/>'
    + _t(355, 185, "H", 14, anchor="middle")
    + _t(445, 185, "L", 14, anchor="middle")
    + _t(400, 135, "DP gauge", 12, "600", anchor="middle")
    # notes
    + _t(40, 40, "Gauge reads P1 minus P2", 14)
    + _t(40, 60, "the pressure drop across the filter", 12, "400", "#555")
    + _t(560, 40, "Reading rises as the", 14)
    + _t(560, 60, "element clogs", 12, "400", "#555")
)

BODY = [
    takeaways([
        "A differential pressure gauge has a high and a low port and shows the difference between the two pressures on one dial.",
        "Piston and diaphragm designs are common at ±2% or ±5% of full scale; bellows and Bourdon designs reach ±1/2% or ±1%.",
        "In most DP service the working pressure on the ports is far higher than the DP range, so check the maximum working pressure first.",
        "Typical jobs are filter and strainer monitoring, flow across an orifice and level in open or closed tanks.",
    ]),
    p("Two ordinary gauges cannot show a small difference sitting on a high line pressure. A <strong>differential pressure gauge</strong> takes both pressures into one instrument and shows only the difference. SWME supplies " + link("/differential-pressure-gauges", "differential pressure gauges") + " and " + link("/gauge-accessories", "gauge accessories") + " for plants across the UAE and GCC."),
    toc([("principle", "How it works"), ("designs", "Sensing designs"), ("pressure", "Working pressure and range"),
         ("uses", "Applications"), ("select", "Selection checklist"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("principle", "How a Differential Pressure Gauge Works"),
    p("The gauge has a high pressure port and a low pressure port. The sensing element sits between them and moves with the difference, and a magnet or linkage turns the pointer. For the difference between gauge, absolute and DP readings, see our guide to " + link("/gauge-vs-absolute-vs-differential-pressure", "gauge vs absolute vs differential pressure") + "."),
    INFOGRAPHIC,
    svg(_diag, "Differential pressure gauge connected across a filter: the dial shows upstream pressure P1 minus downstream pressure P2", 370),
    h2("designs", "Sensing Designs"),
    p("The " + ext("https://midwestinstrument.com/differential-pressure/differential-pressure-product-selection-guide/", "Midwest Instrument selection guide") + " and " + ext("https://www.noshok.com/support/support-tools-faq/application-insights/advantages-of-using-differential-pressure-gauges", "NOSHOK") + " describe four main designs."),
    table(["Design", "How it senses", "Suits", "Stated accuracy"],
          [["Piston", "A floating piston and magnet move in a bore against a calibrated spring; a rotary magnet outside drives the pointer", "Liquids. A little liquid bypasses from high to low port, which Midwest says is often too much for gas", "±2% or ±5% full scale"],
           ["Diaphragm", "An elastomer diaphragm moves against a range spring and carries an internal magnet", "Dissimilar fluids, air, gases and liquids with a high solids content, because the ports are fully isolated", "±2% or ±5% full scale"],
           ["Bellows", "DP acts on a bellows and linkage that drive the pointer", "Clean service where accuracy matters", "±1/2% or ±1% full scale"],
           ["Bourdon", "A Bourdon tube sits inside a pressure chamber and reads the difference between inside and outside, coupled by magnet", "High working pressures", "±1/2% or ±1% full scale"]]),
    p("WIKA leaves bellows out of its DP range because bellows are susceptible to pressure spikes, and recommends diaphragm types instead. Where a 4 to 20 mA signal is needed rather than a local dial, use a " + link("/differential-pressure-transmitters", "differential pressure transmitter") + "."),
    h2("pressure", "Working Pressure and Range"),
    p("WIKA's " + ext("https://blog.wika.com/us/knowhow/introduction-to-differential-pressure-measurement/", "introduction to DP measurement") + " notes that in almost every DP application the working pressure is much higher than the DP range, and the maximum working pressure is very critical. Midwest protects its bellows and Bourdon units against overrange in either direction up to the rated working pressure, with a relief valve that opens to equalise the two sides."),
    rows([
        ("Low end", "Ranges go as low as 0.2 inches of water for air handling, and WIKA lists models from 2.5 mbar."),
        ("High end", "WIKA says a Bourdon type DP gauge can work at up to 15,000 psi."),
        ("Piston leakage", "Midwest states piston bypass will not exceed 15 SCFH of air at 100 PSID."),
        ("Weight", "Some DP gauges weigh up to 30 lbs (13.6 kg), so plan the mounting bracket."),
    ], "At a glance"),
    dyk("WIKA gives a simple example: 10 inches of water is 0.36 psi. Two standard gauges reading about 100 psi could not show that difference, but one DP gauge can."),
    h2("uses", "Applications"),
    rows([
        ("Filters and strainers", "DP rises as the element clogs and tells you when to change it. WIKA describes " + ext("https://blog.wika.com/en/applications/safe-filter-monitoring-with-differential-pressure-gauges/", "filter monitoring on reverse osmosis membranes") + " with microswitch alarms that still work in a power failure."),
        ("Flow", "An orifice, venturi or nozzle creates a DP; WIKA notes the drop is proportional to the square of the flow rate. See our " + link("/types-of-flow-meters", "types of flow meters") + " guide."),
        ("Level", "On an open tank the low side vents to atmosphere. On a sealed tank the high side goes to the bottom and the low side to the top, so the gas pressure cancels."),
        ("Other duties", "NOSHOK lists pumps, separators, leak detection and heat exchangers; Midwest adds HVAC and irrigation filtration."),
    ]),
    p("For level work the " + ext("https://zentacalculator.com/engineering/hydrostatic-pressure/", "hydrostatic pressure calculator") + " gives the DP for a liquid height, and the " + ext("https://zentacalculator.com/engineering/dp-flow-square-root/", "DP flow square root calculator") + " converts a reading to flow. More background is in the " + ext("https://www.instrumentationblog.in/category/process-instrumentation/pressure-measurement/", "Instrumentation Blog pressure section") + "."),
    h2("select", "Selection Checklist"),
    checklist([
        ("DP range", "Size the dial for the difference you expect, not the line pressure."),
        ("Maximum working pressure", "Confirm the rating covers the highest line pressure and any one sided overpressure."),
        ("Fluid", "Piston for liquids; diaphragm for gas, mixed or dirty media; bellows or Bourdon for best accuracy."),
        ("Wetted materials", "Corrosive media may need stainless steel. Ask about NACE or oxygen service if required."),
        ("Connections", "WIKA says filters typically use inline end connections, low air pressures use hose barbs, and level often uses four ports with 1/4 inch NPT female threads."),
        ("Options", "Switches, output signals and a valve manifold with shutoff and an equalising bypass. See " + link("/manifolds-fittings", "manifolds and fittings") + "."),
    ]),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Choosing by DP range alone.", "The working pressure rating usually decides the design."),
        ("A piston gauge on gas.", "The bypass between ports can be too large; use an isolated diaphragm design."),
        ("Adding diaphragm seals without checking.", "Midwest does not recommend seals on several of its models and says fitting them voids the warranty."),
    ]),
    p("For a DP alarm without a dial, see " + link("/differential-pressure-switches", "differential pressure switches") + " and our guide on " + link("/what-is-a-pressure-switch", "what a pressure switch is") + "."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What does a differential pressure gauge measure?", "The difference between the pressure at its high port and its low port, shown on one dial."),
        ("Which design suits gas?", "A diaphragm type, because its ports are fully isolated. Piston types allow a small bypass that can be too large for gas."),
        ("Why is working pressure so important?", "The ports often see a line pressure far above the DP range, and the gauge must withstand it on either side."),
    ]),
]
