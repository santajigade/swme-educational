import math as _m

META = {
    "category": "temperature-measurement-guides",
    "title": "Response Time of Temperature Sensors: t50, t63 and t90",
    "keyword": "response time",
    "subtitle": "What the time constant of a temperature sensor means, how t50, t63 and t90 are measured, and why thermowells, junction type and the process fluid change the response time you see in the plant",
    "meta_title": "Temperature Sensor Response Time: t50, t63 and t90",
    "meta_description": "Temperature sensor response time explained: the 63.2% time constant, t50 and t90, test methods, and how thermowells, junction type and the fluid slow a sensor.",
    "summary": "What the time constant and the t50, t63 and t90 values of a temperature sensor mean, how they are tested, and what slows a sensor down in service.",
    "card_title": "Temperature Sensor Response Time",
    "author": "SWME Technical Staff",
    "published": "2026-11-25",
    "status": "published",
    "sort_order": 9,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "grid",
        "title": "Four Ways to Quote Response Time",
        "alt": "Infographic with four cards: t50, t63 time constant, t90 and five time constants, with the share of a step change each one represents",
        "steps": [
            ["t50", "Time to reach 50% of a step change: 0.693 time constants."],
            ["t63, the time constant", "Time to reach 63.2% of a step change."],
            ["t90", "Time to reach 90% of a step change: 2.303 time constants."],
            ["5 time constants", "Roughly the fully stabilised value, 99.3% of the step."],
        ],
    },
}

_C = "#d9480f"
_T = "#a33608"


def _x(n):
    return 90 + n * 110


def _y(f):
    return 300 - f * 240


def _t(x, y, s, size=13, w="700", fill="#495057", anchor="middle"):
    return f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_curve = " ".join(f"{_x(i / 20):.1f},{_y(1 - _m.exp(-i / 20)):.1f}" for i in range(0, 121))
_marks = ""
for _n, _lab in ((1, "63.2%"), (2, "86.5%"), (3, "95.0%"), (5, "99.3%")):
    _f = 1 - _m.exp(-_n)
    _marks += (f'<line x1="{_x(_n):.0f}" y1="{_y(_f):.1f}" x2="{_x(_n):.0f}" y2="300" stroke="{_C}" stroke-dasharray="4 4"/>'
               f'<circle cx="{_x(_n):.0f}" cy="{_y(_f):.1f}" r="5" fill="{_C}"/>'
               + _t(_x(_n) + 10, _y(_f) + 24, _lab, 13, "700", _T, "start"))
_grid = "".join(f'<line x1="{_x(n)}" y1="300" x2="{_x(n)}" y2="306" stroke="#495057"/>' + _t(_x(n), 322, f"{n}τ", 12, "400", "#555")
                for n in range(0, 7))
_yt = "".join(f'<line x1="84" y1="{_y(f / 100):.0f}" x2="90" y2="{_y(f / 100):.0f}" stroke="#495057"/>' + _t(78, _y(f / 100) + 4, f"{f}%", 12, "400", "#555", "end")
              for f in (0, 50, 100))

_diag = (
    f'<line x1="90" y1="{_y(1):.0f}" x2="770" y2="{_y(1):.0f}" stroke="#adb5bd" stroke-dasharray="6 4"/>'
    + _t(700, _y(1) - 8, "New process temperature", 12, "700", "#868e96")
    + '<line x1="90" y1="300" x2="770" y2="300" stroke="#495057" stroke-width="1.5"/>'
    + '<line x1="90" y1="50" x2="90" y2="300" stroke="#495057" stroke-width="1.5"/>'
    + _grid + _yt
    + f'<polyline points="{_curve}" fill="none" stroke="{_C}" stroke-width="3"/>'
    + _marks
    + _t(430, 350, "Time after the step change, in time constants τ", 13, "700")
    + '<text x="30" y="175" text-anchor="middle" font-size="13" font-weight="700" fill="#495057" transform="rotate(270 30 175)">Share of the step</text>'
)

BODY = [
    takeaways([
        "The time constant is the time a sensor takes to reach 63.2% of a sudden temperature change.",
        "Makers also quote t50 and t90. Minco calls the 90% value a better indicator of performance than the 63.2% one.",
        "Tests are done in flowing water or air at set conditions, which rarely match the plant.",
        "A thermowell adds material that heat must cross, so it increases the response time.",
    ]),
    p("The <strong>response time</strong> of a temperature sensor tells you how quickly the reading catches up with a change in the process. It matters for control loops, alarms and trips. SWME supplies " + link("/rtd-thermocouples", "RTDs and thermocouples") + ", " + link("/thermowells", "thermowells") + " and " + link("/temperature-transmitters", "temperature transmitters") + " across the UAE, and the choice of each one changes how fast the measurement responds."),
    toc([("constant", "The time constant"), ("values", "t50, t63 and t90"), ("test", "How response time is tested"),
         ("slow", "What slows a sensor"), ("calc", "Response time calculator"), ("select", "Getting a faster reading"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("constant", "The Time Constant"),
    p("Minco's white paper on " + ext("https://www.minco.com/wp-content/uploads/Minco-Time-Constant-Considerations-Sensors-Whitepaper.pdf", "response time considerations in temperature sensing") + " defines the time constant τ as the time an object needs to undergo 63.2% of a step change in temperature. After that the reading keeps closing on the new value, but more slowly. Minco gives the fractions reached after each time constant as 0.632, 0.865, 0.950, 0.981, 0.993 and 0.997, and says five time constants is often taken as roughly the final value."),
    svg(_diag, "Step response of a sensor that behaves as a simple first order system: 63.2% after one time constant, 86.5% after two, 95.0% after three and 99.3% after five", 370),
    p("In addition, Minco cautions that most real sensors are too complex to follow this simple model exactly, and τ tends to grow as the sensor nears the final value."),
    h2("values", "t50, t63 and t90"),
    INFOGRAPHIC,
    p("WIKA's article on " + ext("https://blog.wika.com/us/products/temperature-products/temperature-sensors-thermowells-and-response-times/", "thermowells and response times") + " lists three measured values: the time to 50%, 63% and 90% of the actual temperature. The 100% value is never reached, so it is not determined. For example, in Minco's test a sensor had τ0.632 of 0.87 s and τ0.9 of 2.09 s, which shows how much longer the 90% point takes."),
    h2("test", "How Response Time Is Tested"),
    p("WIKA describes four test methods: in flowing water, in flowing air, on a surface, or in a solid body. In the water test the water flows at more than 0.2 m/s and a constant temperature, and the sensor is moved very rapidly from an ambient start of 5 to 30 °C into it. The standards WIKA cites include ASTM E644, ASTM E839, VDI/VDE 3522 and IEC 60751.",
      "Air results look very different from water results. DwyerOmega's figures for " + ext("https://www.dwyeromega.com/de-de/resources/thermocouples-response-time", "thermocouple response time") + " are for air at room temperature moving at 65 ft/s. Minco notes that the time constant varies roughly with the inverse of the heat transfer coefficient, and that standard test methods rarely match the heat transfer conditions of actual use."),
    dyk("DwyerOmega gives an exposed butt welded thermocouple junction made from 0.001 inch wire a time constant of 0.003 seconds in air at 65 ft/s. For beaded or ungrounded junctions, it says to multiply its time constants by 1.5."),
    h2("slow", "What Slows a Sensor"),
    twocol([
        ("The installation", "bi-layers", [
            "A thermowell adds another layer of material for heat to cross (WIKA).",
            "Wider, thicker walled wells increase heat dissipation and slow the response.",
            "Narrow, thin walled wells respond faster and read more accurately.",
        ]),
        ("The sensor and the fluid", "bi-thermometer-half", [
            "Ungrounded or beaded thermocouple junctions are slower than grounded or exposed ones (DwyerOmega).",
            "DwyerOmega charts the time constant against wire and sheath diameter from 1/32 to 3/8 inch, so the diameter you specify matters.",
            "Gases transfer heat less well than liquids, so the same probe is slower in air.",
        ]),
    ]),
    p("WIKA also notes that wake frequency calculations to ASME PTC 19.3 TW often make thermowells shorter and thicker, which pulls against fast response. Our guide on " + link("/what-is-a-thermowell", "what a thermowell is") + " covers that check, and the article comparing " + link("/blog/rtd-vs-thermocouple-high-temperature-guide", "RTDs and thermocouples at high temperature") + " helps you pick the element. Choosing the right " + link("/thermocouple-types-explained", "thermocouple type") + " is a separate decision from its junction."),
    h2("calc", "Response Time Calculator"),
    p("If you know a sensor's time constant, the calculator below gives its t50, t90 and t99 and the reading it will show a given time after a step, which helps when you set an alarm delay or check whether a probe is fast enough for a loop."),
    '<div class="my-4"><iframe src="https://zentacalculator.com/embed/engineering/sensor-response-time/" title="Sensor Response Time Calculator (Time Constant, T63, T90)" width="100%" height="640" loading="lazy" style="border:1px solid #e2e5ee;border-radius:12px;max-width:720px;"></iframe>'
    '<p>' + ext("https://zentacalculator.com/engineering/sensor-response-time/", "Sensor Response Time Calculator (Time Constant, T63, T90)") + ' by ' + ext("https://zentacalculator.com/", "Zenta Calculator") + '</p></div>',
    h2("select", "Getting a Faster Reading"),
    checklist([
        ("Compare like with like", "Check whether a datasheet quotes t50, t63 or t90, and in water or air."),
        ("Pick the smallest suitable sensor", "Minco says to reduce density, specific heat capacity and volume, or increase surface area. Lower specific heat and density are often the most effective."),
        ("Choose the junction", "A grounded junction responds faster than an ungrounded one."),
        ("Keep the well thin", "Use the narrowest, thinnest wall that still passes the wake frequency check."),
        ("Allow for the plant", "Expect a slower response in service than in the test bath."),
    ]),
    p("Readings from a fast sensor are only useful if the transmitter passes them on; see our " + link("/temperature-transmitter-basics", "temperature transmitter guide") + ". More reading is in these " + ext("https://www.instrumentationblog.in/category/process-instrumentation/temperature-measurements/", "temperature measurement articles") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Comparing a t63 figure with a t90 figure.", "In Minco's example the 90% time was more than twice the 63.2% time."),
        ("Using a bare probe figure for a sensor in a thermowell.", "The well adds material and slows the response."),
        ("Expecting a water test result in gas.", "Gases transfer heat less well, so the sensor responds more slowly."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What is the time constant of a temperature sensor?", "The time it takes to reach 63.2% of a sudden change in temperature."),
        ("How long until a sensor reads the full change?", "Five time constants is often taken as roughly the final value, about 99.3% of the step."),
        ("Does a thermowell slow the response time?", "Yes. It adds material that heat must cross, and thicker, wider wells slow it more."),
    ]),
]
