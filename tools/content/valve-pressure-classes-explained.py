META = {
    "category": "industrial-valve-guides",
    "title": "Valve Pressure Classes Explained: ASME B16.34 Ratings",
    "keyword": "valve pressure class",
    "subtitle": "What Class 150, 300 and 600 really mean, why the allowed pressure falls as temperature rises, how material groups change the rating, and where Class 800 and PN ratings fit",
    "meta_title": "Valve Pressure Classes Explained: ASME B16.34",
    "meta_description": "Valve pressure class explained: what Class 150, 300 and 600 mean under ASME B16.34, how ratings fall with temperature, material groups, Class 800 and PN.",
    "summary": "What a valve pressure class means under ASME B16.34, how the allowed pressure falls with temperature and material, and where Class 800 and PN ratings fit.",
    "card_title": "Valve Pressure Classes",
    "author": "SWME Technical Staff",
    "published": "2026-11-25",
    "status": "published",
    "sort_order": 8,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "compare",
        "title": "Group 1.1 Carbon Steel: Class 150 vs 300",
        "alt": "Infographic comparing the ASME B16.34 pressure ratings of Class 150 and Class 300 carbon steel valves at ambient, 250 °C and 425 °C",
        "steps": [
            ["Class 150", "19.6 bar at ambient, 12.1 bar at 250 °C, 5.5 bar at 425 °C."],
            ["Class 300", "51.1 bar at ambient, 41.9 bar at 250 °C, 28.8 bar at 425 °C."],
        ],
        "columns": [
            ["Class 150", ["19.6 bar at minus 29 to 38 °C", "12.1 bar at 250 °C", "5.5 bar at 425 °C"]],
            ["Class 300", ["51.1 bar at minus 29 to 38 °C", "41.9 bar at 250 °C", "28.8 bar at 425 °C"]],
        ],
    },
}

_C = "#e67700"
_T = "#a35400"

# ASME B16.34 Table 2-1.1 Group 1.1, as reproduced by wermac.org (bar)
_P150 = [(-29, 19.6), (38, 19.6), (100, 17.7), (200, 13.8), (250, 12.1), (300, 10.2), (400, 6.5), (425, 5.5), (500, 2.8), (538, 1.4)]
_P300 = [(-29, 51.1), (38, 51.1), (100, 46.6), (200, 43.8), (250, 41.9), (300, 39.8), (400, 34.7), (425, 28.8), (500, 11.8), (538, 5.9)]


def _x(t):
    return 90 + (t + 50) * (680 / 600)


def _y(b):
    return 300 - b * (240 / 60)


def _t(x, y, s, size=13, w="700", fill="#495057", anchor="middle"):
    return f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


def _line(pts, col):
    d = " ".join(f"{_x(t):.1f},{_y(b):.1f}" for t, b in pts)
    dots = "".join(f'<circle cx="{_x(t):.1f}" cy="{_y(b):.1f}" r="3.5" fill="{col}"/>' for t, b in pts[1:])
    return f'<polyline points="{d}" fill="none" stroke="{col}" stroke-width="3"/>' + dots


_grid = "".join(
    f'<line x1="90" y1="{_y(b):.0f}" x2="770" y2="{_y(b):.0f}" stroke="#e9ecef"/>' + _t(80, _y(b) + 4, str(b), 12, "400", "#555", "end")
    for b in range(0, 61, 10))
_xt = "".join(
    f'<line x1="{_x(t):.0f}" y1="300" x2="{_x(t):.0f}" y2="306" stroke="#495057"/>' + _t(_x(t), 322, str(t), 12, "400", "#555")
    for t in (0, 100, 200, 300, 400, 500))

_diag = (
    _grid + _xt
    + '<line x1="90" y1="300" x2="770" y2="300" stroke="#495057" stroke-width="1.5"/>'
    + '<line x1="90" y1="60" x2="90" y2="300" stroke="#495057" stroke-width="1.5"/>'
    + f'<rect x="{_x(425):.0f}" y="60" width="{_x(550) - _x(425):.0f}" height="240" fill="#fff4e6" opacity="0.8"/>'
    + _t(_x(487), 80, "Above 425 °C:", 12, "700", _T) + _t(_x(487), 96, "not for prolonged use", 12, "700", _T)
    + _line(_P300, _C) + _line(_P150, "#1864ab")
    + _t(_x(150), _y(51.1) - 4, "Class 300", 14, "700", _C)
    + _t(_x(120), _y(17.7) - 12, "Class 150", 14, "700", "#1864ab")
    + _t(430, 350, "Fluid temperature, °C", 13, "700")
    + '<text x="30" y="180" text-anchor="middle" font-size="13" font-weight="700" fill="#495057" transform="rotate(270 30 180)">Allowed working pressure, bar</text>'
)

BODY = [
    takeaways([
        "The number after \"Class\" is not a pressure in psi. It points to a pressure and temperature rating table in ASME B16.34.",
        "The allowed pressure falls as temperature rises: a Group 1.1 Class 150 valve is good for 19.6 bar at ambient but only 5.5 bar at 425 °C.",
        "The rating also depends on the body material group, so always read the table for your material.",
        "Class 800 is an intermediate class for small forged valves, and PN ratings come from European DIN practice.",
    ]),
    p("A <strong>valve pressure class</strong> sets the pressure and temperature limits of a valve body, and it applies to every " + link("/gate-valves", "gate valve") + ", " + link("/globe-valves", "globe valve") + " and " + link("/ball-valves", "ball valve") + " on a line. It also has to match the flanges. SWME supplies " + link("/industrial-valves", "industrial valves") + " in all common classes across the UAE."),
    toc([("meaning", "What a valve pressure class means"), ("temperature", "How temperature lowers the rating"), ("groups", "Material groups"),
         ("classes", "The standard classes"), ("other", "Class 800, cast iron and PN"), ("select", "Selection checklist"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("meaning", "What a Valve Pressure Class Means"),
    p("Wermac's page on " + ext("https://wermac.org/valves/valves_B16_34.html", "valve pressure classes to ASME B16.34") + " is blunt about it: the number after the word class has nothing to do with the pressure the valve can operate at. It calls the class a dimensionless guideline, and says \"150 pound\" is wrong; the correct form is \"class 150\". The real working limits depend on the fluid temperature and on the material of the body and upper section.",
      "In addition, Valve Magazine's " + ext("https://www.valvemagazine.com/articles/an-overview-of-asme-b16-34-2017", "overview of ASME B16.34 2017") + " adds that a valve which complies may be stamped B16.34, and that marking per MSS SP 25 includes the manufacturer, body and bonnet materials, pressure rating, temperature and size."),
    h2("temperature", "How Temperature Lowers the Rating"),
    p("Wermac reproduces the B16.34 rating table for Group 1.1 materials, which include A105 forgings and A216 WCB castings. The limits vary inversely with fluid temperature. The chart below plots the Class 150 and Class 300 columns."),
    svg(_diag, "ASME B16.34 Group 1.1 ratings for Class 150 and Class 300, as reproduced by wermac.org. Carbide may turn to graphite above 425 °C, so the table notes advise against prolonged use there", 370),
    INFOGRAPHIC,
    p("For example, a Class 150 WCB valve rated 19.6 bar at ambient is down to 12.1 bar at 250 °C. Projectmaterials warns in its " + ext("https://blog.projectmaterials.com/quick-answers/valves/what-is-asme-b16-34/", "ASME B16.34 summary") + " that the allowed pressure may drop by 50% or more at elevated temperature, so check the rating at the design temperature, not only at ambient."),
    dyk("Wermac points out that valves with elastomer or thermoplastic seats have much lower ratings than the metal seated values in B16.34. The seat, not the body, can set the limit."),
    h2("groups", "Material Groups"),
    p("Valve Magazine explains that B16.34 sorts materials into groups: Group 1 for carbon and low alloy steels, Group 2 for stainless and duplex steels, and Group 3 for nickel and nickel alloys, with 49 sub groups in all. Wermac says there are about 50 rating tables, one per group. So the same valve pressure class in two materials can give different limits at the same temperature."),
    h2("classes", "The Standard Classes"),
    p("Projectmaterials lists these ambient ratings for Group 1.1 carbon steel, valid from minus 29 to 38 °C:"),
    table(["Class", "Rating at minus 29 to 38 °C, Group 1.1"], [
        ["150", "285 psi"], ["300", "740 psi"], ["600", "1,480 psi"], ["900", "2,220 psi"],
        ["1500", "3,705 psi"], ["2500", "6,170 psi"], ["4500", "11,100 psi"],
    ]),
    p("Projectmaterials also notes that B16.34 classes line up with ASME B16.5 flange classes, so a Class 300 valve matches a Class 300 flange. Its " + ext("https://blog.projectmaterials.com/quick-answers/valves/class-150-vs-class-300-valve/", "Class 150 vs Class 300 comparison") + " adds that the two are not interchangeable because the bolt patterns differ. Our guide to " + link("/types-of-industrial-valves", "types of industrial valves") + " and the article on " + link("/blog/how-to-select-the-right-industrial-valve", "choosing the right industrial valve") + " cover the other selection points."),
    h2("other", "Class 800, Cast Iron and PN"),
    rows([
        ("Class 800", "Wermac says it is for wrought steel globe, slide and check valves and is not part of B16.34. Under API 602 and ISO 15761 it is interpolated as 1/3 of Class 600 plus 2/3 of Class 900. For A105 at ambient that gives 493 + 1,480 = 1,973 psig."),
        ("Class 125 and 250", "Gray cast iron only. Ductile iron Class 150 and 300 are not in B16.34 either."),
        ("PN", "The DIN ratings PN6 to PN400. PN stands for nominal pressure, with values in bar."),
    ], "Ratings outside the B16.34 tables (wermac)"),
    p("After installation, the line is usually pressure tested. The " + ext("https://zentacalculator.com/engineering/hydrostatic-test-pressure/", "hydrostatic test pressure calculator") + " works out the test pressure for piping or a vessel, including the extra head at the low point, so you can confirm it stays within the rating of the valves in the test section."),
    h2("select", "Selection Checklist"),
    checklist([
        ("Fix the design pressure and temperature", "Before you pick a valve pressure class, use the highest temperature the valve will see, not the normal one."),
        ("Pick the material group", "Body and bonnet material set which B16.34 table applies."),
        ("Read the rating at temperature", "Choose the lowest class whose rating at design temperature covers the design pressure."),
        ("Match the flanges", "Valve and flange class must agree because bolt patterns differ."),
        ("Check the seats", "Soft seats can limit the valve below the body rating."),
    ]),
    p("For relief duty, our " + link("/safety-relief-valve-basics", "safety relief valve guide") + " explains set pressure and sizing."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Reading Class 150 as 150 psi.", "The ambient Group 1.1 rating is 285 psi, and it falls with temperature."),
        ("Using the ambient rating at high temperature.", "At 425 °C a Class 150 WCB valve is down to 5.5 bar."),
        ("Mixing classes on one flange joint.", "Class 150 and Class 300 bolt patterns do not match."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Does Class 150 mean 150 psi?", "No. The class is a designation. For Group 1.1 carbon steel the ambient rating is 285 psi."),
        ("Why is my valve rated lower at high temperature?", "B16.34 ratings vary inversely with fluid temperature, so the allowed pressure falls as the temperature rises. Read the table at your design temperature."),
        ("Is Class 800 in ASME B16.34?", "No. It is an intermediate class for small forged valves under API 602 and ISO 15761."),
    ]),
]
