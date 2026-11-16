META = {
    "category": "temperature-measurement-guides",
    "title": "Thermocouple Types Explained: J, K, T, N, R and S",
    "keyword": "thermocouple types",
    "subtitle": "Materials, temperature ranges, atmospheres, colour codes and how to choose",
    "meta_title": "Thermocouple Types Explained: J, K, T, N, R and S",
    "meta_description": "Thermocouple types J, K, T, N, R and S compared: leg materials, temperature ranges, atmospheres, IEC colour codes and tips for choosing the right one.",
    "summary": "How the common thermocouple types differ in materials, range, atmosphere and colour code, and how to choose one.",
    "card_title": "Thermocouple Types Explained",
    "author": "SWME Technical Staff",
    "published": "2026-11-16",
    "status": "published",
    "sort_order": 3,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "levels",
        "title": "Which Thermocouple for Which Temperature?",
        "alt": "Infographic ranking thermocouple types T, J, K, N, R and S by recommended upper temperature",
        "top_label": "Hotter",
        "bottom_label": "Colder",
        "levels": [
            ["Type T", "Minus 200 to 350 degrees C; best choice for cryogenics and moist service.", 0.12],
            ["Type J", "0 to 750 degrees C; suits reducing, inert and vacuum service.", 0.38],
            ["Types K and N", "Up to 1,250 (K) and 1,300 (N) degrees C; N is more stable when hot.", 0.64],
            ["Types R and S", "Platinum types up to 1,450 (R) and 1,400 (S) degrees C.", 0.9],
        ],
    },
}

_TYPES = [("T", -200, 350), ("J", 0, 750), ("K", -200, 1250), ("N", -270, 1300), ("S", 0, 1400), ("R", 0, 1450)]
_x = lambda t: 110 + (t + 300) * 0.37

BODY = [
    takeaways([
        "A thermocouple is two different metals joined at one end; the junction produces a small voltage that rises with temperature.",
        "Base metal types J, K, T and N cover most process duties; noble metal types R and S cover very high temperatures.",
        "Each type has its own range, atmosphere limits and colour code, so the letter on the datasheet matters.",
        "Extension cable and transmitter input must match the thermocouple type.",
    ]),
    p("Thermocouples measure temperature in services from cryogenic tanks to furnaces well above 1,000 degrees Celsius. They are rugged, fast and simple, but they come in several letter types that are not interchangeable. Knowing the main <strong>thermocouple types</strong> helps you pick a sensor that stays accurate in your process.",
      "This guide compares types J, K, T, N, R and S. SWME supplies " + link("/rtd-thermocouples", "RTD and thermocouple sensors") + ", " + link("/temperature-transmitters", "temperature transmitters") + " and " + link("/thermowells", "thermowells") + " for projects across the GCC."),
    toc([("principle", "How a thermocouple works"), ("types", "Common thermocouple types"), ("ranges", "Temperature ranges compared"),
         ("colours", "Colour codes"), ("select", "How to choose"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("principle", "How a Thermocouple Works"),
    p("A thermocouple is made of two different metals or alloys welded together at the measuring junction. Because each metal has a different Seebeck coefficient, heating the junction produces a voltage of a few millivolts between the free ends. The voltage rises with temperature in a way that is close to, but not exactly, linear.",
      "Published thermocouple tables assume the reference junction, where the wires connect to the instrument, is at 0 degrees Celsius. Real terminals are warmer, so transmitters and controllers include built in cold junction compensation. For example, without it a direct millivolt reading would show a temperature that is too low."),
    svg(
        arrow_defs("#d9480f")
        + '<rect x="20" y="70" width="190" height="180" rx="12" fill="#fff1ea" stroke="#d9480f" stroke-width="2"/>'
        + '<text x="115" y="95" text-anchor="middle" font-size="14" font-weight="700" fill="#a33608">Process</text>'
        + '<circle cx="150" cy="160" r="10" fill="#d9480f"/>'
        + '<text x="115" y="205" text-anchor="middle" font-size="13" fill="#333">Measuring</text><text x="115" y="223" text-anchor="middle" font-size="13" fill="#333">(hot) junction</text>'
        + '<polyline points="150,160 260,130 560,130" fill="none" stroke="#2b8a3e" stroke-width="5"/>'
        + '<polyline points="150,160 260,190 560,190" fill="none" stroke="#adb5bd" stroke-width="5"/>'
        + '<text x="400" y="118" text-anchor="middle" font-size="13" fill="#2b8a3e">Positive leg, for example Chromel (type K)</text>'
        + '<text x="400" y="216" text-anchor="middle" font-size="13" fill="#555">Negative leg, for example Alumel (type K)</text>'
        + '<text x="400" y="248" text-anchor="middle" font-size="12" fill="#555">Thermocouple or matching extension cable</text>'
        + '<rect x="560" y="70" width="220" height="180" rx="12" fill="#f8f9fa" stroke="#495057" stroke-width="2"/>'
        + '<rect x="560" y="115" width="26" height="30" fill="#495057"/><rect x="560" y="175" width="26" height="30" fill="#495057"/>'
        + '<text x="680" y="100" text-anchor="middle" font-size="14" font-weight="700" fill="#333">Transmitter</text>'
        + '<text x="680" y="140" text-anchor="middle" font-size="13" fill="#333">Reference (cold)</text><text x="680" y="158" text-anchor="middle" font-size="13" fill="#333">junction at terminals</text>'
        + '<text x="680" y="190" text-anchor="middle" font-size="13" fill="#333">Cold junction</text><text x="680" y="208" text-anchor="middle" font-size="13" fill="#333">compensation</text>'
        + '<line x1="680" y1="250" x2="680" y2="300" stroke="#d9480f" stroke-width="3" marker-end="url(#ah)"/>'
        + '<text x="680" y="322" text-anchor="middle" font-size="13" fill="#333">4 to 20 mA or HART</text>'
        + '<text x="300" y="300" text-anchor="middle" font-size="14" font-weight="600" fill="#a33608">Millivolt signal depends on the temperature difference</text>'
        + '<text x="300" y="320" text-anchor="middle" font-size="14" font-weight="600" fill="#a33608">between the two junctions</text>',
        "Thermocouple circuit: measuring junction, two dissimilar legs and reference junction with compensation", 340),
    p("Extension wire is made to have the same millivolt output as the thermocouple, but only over a limited range, typically 0 to 200 degrees Celsius. Running plain copper from the sensor would move the reference junction to the wrong place. See this practical guide to " + ext("https://www.instrumentationblog.in/temperature-transmitter-wiring/", "temperature transmitter wiring") + "."),
    h2("types", "Common Thermocouple Types"),
    table(["Type", "Positive leg", "Negative leg", "Recommended range", "Atmosphere notes"], [
        ["J", "Iron", "Constantan", "0 to 750 &deg;C", "Good in reducing, inert and vacuum service; iron leg can rust"],
        ["K", "Chromel", "Alumel", "Minus 200 to 1,250 &deg;C", "Oxidizing or inert; avoid sulphur and reducing service"],
        ["T", "Copper", "Constantan", "Minus 200 to 350 &deg;C", "Reducing, mildly oxidizing and moist service; cryogenics"],
        ["N", "Nicrosil", "Nisil", "Minus 270 to 1,300 &deg;C", "Improved alternative to K with better stability when hot"],
        ["R", "Platinum 13% rhodium", "Platinum", "0 to 1,450 &deg;C", "Oxidizing or inert; reducing service causes drift"],
        ["S", "Platinum 10% rhodium", "Platinum", "0 to 1,400 &deg;C", "Like R, but not interchangeable with it"],
    ]),
    h3("Base metal types: J, K, T and N"),
    p("Type K is the most popular of all thermocouple types because of its wide range and durability. Type N was developed as an improved replacement for K, with a similar range and much better stability at high temperature. Type J has a higher output than K but a lower range, and Type T gives the best accuracy of the base metal types within its range, which makes it the usual choice for cryogenic and food service."),
    h3("Noble metal types: R and S"),
    p("Types R and S use platinum and platinum rhodium wires. They cost far more, but they are stable at temperatures where base metal types drift, for example in furnaces, heat treating and sulphur recovery units. They are usually fitted with a ceramic sheath and should not be placed directly in metal tubes. A third noble metal type, B, covers about 800 to 1,700 degrees Celsius."),
    h2("ranges", "Temperature Ranges Compared"),
    svg(
        "".join(f'<text x="90" y="{58 + k * 44}" text-anchor="end" font-size="15" font-weight="700" fill="#a33608">Type {t}</text>'
                f'<rect x="{_x(lo):.0f}" y="{40 + k * 44}" width="{_x(hi) - _x(lo):.0f}" height="26" rx="5" fill="#d9480f" opacity="{0.75 + k * 0.05:.2f}"/>'
                f'<text x="{_x(hi) - 10:.0f}" y="{58 + k * 44}" text-anchor="end" font-size="13" font-weight="600" fill="#fff">{("minus " + str(-lo)) if lo < 0 else lo} to {hi:,}</text>'
                for k, (t, lo, hi) in enumerate(_TYPES))
        + f'<line x1="{_x(-300):.0f}" y1="312" x2="{_x(1500):.0f}" y2="312" stroke="#495057" stroke-width="2"/>'
        + "".join(f'<line x1="{_x(v):.0f}" y1="312" x2="{_x(v):.0f}" y2="320" stroke="#495057" stroke-width="2"/>'
                  f'<text x="{_x(v):.0f}" y="338" text-anchor="middle" font-size="13" fill="#333">{v:,}</text>' for v in (0, 500, 1000, 1500))
        + f'<line x1="{_x(0):.0f}" y1="30" x2="{_x(0):.0f}" y2="312" stroke="#adb5bd" stroke-dasharray="4 3"/>'
        + '<text x="430" y="362" text-anchor="middle" font-size="13" fill="#555">Recommended range in degrees Celsius</text>',
        "Recommended temperature ranges of common thermocouple types", 375),
    p("Ranges vary slightly between standards and suppliers, and the safe upper limit also depends on wire diameter, sheath and atmosphere. For example, thin Type T wire is rated far lower than heavy gauge wire. Always check the datasheet."),
    INFOGRAPHIC,
    h2("colours", "Thermocouple Colour Codes"),
    p("Under IEC 60584, the negative conductor is always white and the positive conductor and sheath carry the type colour. North American ANSI cables use a red negative instead, so always check which standard a cable follows."),
    rows([
        ("Type K", "green positive, white negative."),
        ("Type J", "black positive, white negative."),
        ("Type T", "brown positive, white negative."),
        ("Type N", "pink positive, white negative."),
        ("Types R and S", "orange positive, white negative."),
    ]),
    dyk("Types R and S look almost identical and share the same IEC colour, but their positive legs contain different amounts of rhodium: 13 percent for R and 10 percent for S. Their outputs differ, so the two types are not interchangeable."),
    h2("select", "How to Choose Between Thermocouple Types"),
    checklist([
        ("Maximum temperature", "Pick a type whose recommended range covers the process with margin."),
        ("Atmosphere", "Match the type to oxidizing, reducing, inert, sulphur or moist conditions."),
        ("Stability", "For long service above about 1,000 degrees Celsius, consider N, R or S."),
        ("Accuracy", "Compare tolerance classes; Type T is tightest at low temperature."),
        ("Signal chain", "Use matching extension cable and set the same type in the transmitter."),
    ]),
    p("Below about 600 degrees Celsius an RTD often gives better accuracy; see " + link("/how-an-rtd-works", "how an RTD works") + " and our blog on " + link("/blog/rtd-vs-thermocouple-high-temperature-guide", "RTD vs thermocouple for high temperature") + ". To check how quickly a sensor follows changes, use the " + ext("https://zentacalculator.com/engineering/sensor-response-time/", "sensor response time calculator") + ", and to scale the output use the " + ext("https://zentacalculator.com/engineering/4-20ma-scaling/", "4 to 20 mA scaling calculator") + ". More articles are on the " + ext("https://www.instrumentationblog.in/category/process-instrumentation/temperature-measurements/", "temperature measurement") + " pages of Instrumentation Blog."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Wrong type set in the transmitter.", "A K sensor read as J gives a large error across the whole range."),
        ("Copper cable instead of extension wire.", "The reference junction moves and the reading shifts."),
        ("Swapping R and S.", "Their rhodium content differs, so the outputs are not interchangeable."),
        ("Type K in reducing or sulphur service.", "The legs degrade and calibration drifts; consider N or a protected sheath."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Which thermocouple type is most common?", "Type K, because of its wide range, durability and moderate cost."),
        ("What is the difference between Type K and Type N?", "Both cover a similar range, but Type N has much better stability at high temperature and was developed as an improved replacement for K."),
        ("Which thermocouple is best for low temperatures?", "Type T is generally the best choice for cryogenic service, with the best accuracy of the base metal types in its range."),
    ]),
]
