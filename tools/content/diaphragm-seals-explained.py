META = {
    "category": "pressure-measurement-guides",
    "title": "Diaphragm Seals Explained: How They Protect Pressure Instruments",
    "keyword": "diaphragm seal",
    "subtitle": "How a flexible diaphragm and a fill fluid keep corrosive, viscous and hot media away from gauges, switches and transmitters",
    "meta_title": "Diaphragm Seals Explained: How They Work and When to Use",
    "meta_description": "How a diaphragm seal works, when to use one, fill fluid choice, capillary effects, temperature error and the selection points that keep readings accurate.",
    "summary": "How a diaphragm seal isolates a pressure instrument from the process, which fill fluid to choose and how to limit temperature error.",
    "card_title": "Diaphragm Seals Explained",
    "author": "SWME Technical Staff",
    "published": "2026-11-18",
    "status": "published",
    "sort_order": 4,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "levels",
        "title": "Fill Fluid Thermal Expansion",
        "alt": "Infographic ranking diaphragm seal fill fluids glycerin, halocarbon and silicone by thermal expansion coefficient",
        "top_label": "Higher",
        "bottom_label": "Lower",
        "levels": [
            ["Glycerin", "Expansion of 0.00062 ml per ml per degree C, the lowest of the three, so the smallest temperature error.", 0.15],
            ["Halocarbon", "Expansion of 0.00080 ml per ml per degree C; an inert fill used for oxidizing media.", 0.5],
            ["Silicone", "Expansion of 0.00096 ml per ml per degree C, the highest, but its low viscosity gives a fast response.", 0.85],
        ],
    },
}

_C = "#5f3dc4"
_L = "#f3f0ff"

_diag = (
    arrow_defs(_C)
    # gauge
    + '<circle cx="250" cy="80" r="58" fill="#fff" stroke="#495057" stroke-width="4"/>'
    + '<circle cx="250" cy="80" r="4" fill="#495057"/>'
    + '<line x1="250" y1="80" x2="285" y2="52" stroke="#c92a2a" stroke-width="3"/>'
    + '<text x="250" y="118" text-anchor="middle" font-size="12" fill="#555">Gauge</text>'
    # stem, filled with fill fluid
    + '<rect x="240" y="138" width="20" height="62" fill="#ffe8a3" stroke="#495057" stroke-width="2"/>'
    # upper housing
    + '<rect x="150" y="200" width="200" height="48" rx="4" fill="#ffe8a3" stroke="#495057" stroke-width="3"/>'
    # diaphragm
    + '<path d="M150 252 Q175 244 200 252 Q225 260 250 252 Q275 244 300 252 Q325 260 350 252" fill="none" stroke="' + _C + '" stroke-width="4"/>'
    # lower housing with process
    + '<rect x="150" y="256" width="200" height="40" rx="4" fill="#dee2e6" stroke="#495057" stroke-width="3"/>'
    + '<rect x="220" y="296" width="60" height="44" fill="#dee2e6" stroke="#495057" stroke-width="3"/>'
    + '<line x1="250" y1="350" x2="250" y2="305" stroke="#e8590c" stroke-width="3" marker-end="url(#ah)"/>'
    # labels
    + '<line x1="352" y1="224" x2="430" y2="224" stroke="#495057" stroke-width="1.5"/>'
    + '<text x="438" y="220" font-size="14" font-weight="700" fill="#3b2a8c">Upper housing with fill fluid</text>'
    + '<text x="438" y="238" font-size="12" fill="#555">Fluid carries pressure to the gauge</text>'
    + '<line x1="352" y1="252" x2="430" y2="268" stroke="#495057" stroke-width="1.5"/>'
    + '<text x="438" y="272" font-size="14" font-weight="700" fill="#3b2a8c">Flexible diaphragm</text>'
    + '<text x="438" y="290" font-size="12" fill="#555">Separates process from instrument</text>'
    + '<line x1="352" y1="290" x2="430" y2="318" stroke="#495057" stroke-width="1.5"/>'
    + '<text x="438" y="322" font-size="14" font-weight="700" fill="#3b2a8c">Lower housing</text>'
    + '<text x="438" y="340" font-size="12" fill="#555">Wetted by the process medium</text>'
    + '<line x1="262" y1="170" x2="430" y2="150" stroke="#495057" stroke-width="1.5"/>'
    + '<text x="438" y="146" font-size="14" font-weight="700" fill="#3b2a8c">Filled connection</text>'
    + '<text x="438" y="164" font-size="12" fill="#555">Direct mount or capillary</text>'
    + '<text x="120" y="345" text-anchor="end" font-size="14" font-weight="700" fill="#e8590c">Process</text>'
    + '<text x="120" y="363" text-anchor="end" font-size="14" font-weight="700" fill="#e8590c">pressure</text>'
)

BODY = [
    takeaways([
        "A diaphragm seal places a flexible barrier between the process and a pressure instrument.",
        "Pressure on the diaphragm is passed hydraulically to the instrument through a sealed fill fluid.",
        "Seals protect gauges, switches and transmitters from corrosive, viscous, abrasive, hot or toxic media.",
        "Temperature error comes from fill fluid expansion, so fill choice, fill volume and capillary length matter.",
    ]),
    p("Some process media will destroy a bourdon tube or block a small pressure port within weeks. A <strong>diaphragm seal</strong>, also called a chemical seal, solves this problem by keeping the medium away from the instrument while still passing the pressure through.",
      "This guide explains how a seal works, when you need one and how to keep the reading accurate. SWME supplies " + link("/diaphragm-seals", "diaphragm seals") + " with matching " + link("/pressure-gauges", "pressure gauges") + " and " + link("/pressure-transmitters", "pressure transmitters") + " for plants across the GCC."),
    toc([("how", "How a diaphragm seal works"), ("when", "When to use one"), ("fill", "Fill fluid selection"),
         ("error", "Temperature error and capillaries"), ("select", "Selection checklist"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("how", "How a Diaphragm Seal Works"),
    p("According to " + ext("https://blog.wika.com/us/products/pressure-products/diaphragm-seal/", "WIKA") + ", a diaphragm seal is a protective device placed between the process media and the pressure instrument. A flexible metal or elastomer diaphragm keeps the medium out of the instrument. The space between the diaphragm and the instrument is completely filled with a fill fluid, which transmits the pressure hydraulically to the sensing element.",
      "The instrument can mount directly on the seal or connect through a capillary. The seal connects to the process by thread, flange, clamp or an inline body, and the instrument connects to the seal by thread or weld."),
    svg(_diag, "Cross section of a diaphragm seal with a direct mounted pressure gauge", 370),
    h2("when", "When to Use a Diaphragm Seal"),
    p("WIKA lists the main reasons to fit a seal. In addition, " + ext("https://blog.ashcroft.com/fill-fluid-options-pressure-instruments", "Ashcroft") + " notes that many instrument sensing elements have material limits and may not suit the process medium."),
    rows([
        ("Corrosive media", "The seal and diaphragm are made in a resistant material, so the instrument itself does not need to be."),
        ("Viscous, crystallizing or solid laden media", "Fewer and larger wetted openings mean fewer places for clogs to form."),
        ("High temperature", "A cooling element between seal and instrument protects the gauge or transmitter."),
        ("Sanitary service", "Inline and sanitary designs avoid dead spaces where bacteria can grow."),
        ("Toxic or dangerous media", "The process stays contained behind the diaphragm."),
    ]),
    p("For general gauge selection, see our guide on " + link("/how-to-select-a-pressure-gauge", "how to select a pressure gauge") + ". Seals fit switches as well; read " + link("/what-is-a-pressure-switch", "what is a pressure switch") + "."),
    h2("fill", "Fill Fluid Selection"),
    p("The fill fluid must suit the process and ambient temperatures and must not contaminate the process if the thin diaphragm ruptures. Ashcroft gives these points:"),
    table(["Fill fluid", "Key property", "Typical use"],
          [["Glycerin", "Viscosity 1300 cSt; may lose tolerance below 20 °F", "General service, food grade"],
           ["Silicone", "Viscosity 10 to 50 cSt; case fill range minus 40 to 200 °F", "Fast response, wide temperature"],
           ["Syltherm", "Formulas from minus 150 °F up to 750 °F", "High and low temperature"],
           ["Halocarbon", "Inert fill", "Oxidizing media"],
           ["Distilled water", "Freezes at 32 °F, boils at 212 °F", "Sanitary and oxidizing media"]]),
    h2("error", "Temperature Error and Capillaries"),
    p("Every filled system reads slightly differently as temperature changes. An " + ext("https://www.ashcroft.com/wp-content/uploads/2020/09/pi-page-diaphragm-seals-temperature-error-ds-pi-14.pdf", "Ashcroft technical note") + " explains that errors result from expansion or contraction of the fill. The size of the error depends on the fill expansion coefficient, the diaphragm spring rate, the total fill volume and the gauge range."),
    INFOGRAPHIC,
    p("For example, the note works through a 100 psi gauge on a direct mounted seal and finds an error of about 1.25 psi. With a 5 ft flexible line at a 250 °F process, the error rises to about 2 psi, because each foot of line adds 0.8 ml of fill. Lower range gauges show larger percentage errors. You can check what that means for your loop with the " + ext("https://zentacalculator.com/engineering/instrument-accuracy/", "instrument accuracy calculator") + " and the " + ext("https://zentacalculator.com/engineering/thermal-expansion/", "thermal expansion calculator") + "."),
    dyk("A seal that is too small can be the hidden cause of drift. " + ext("https://reotemp.com/diaphragm-seal-frequently-asked-questions/", "REOTEMP") + " warns that undersized diaphragms can lead to many performance issues, including sensitivity to temperature drift."),
    twocol([
        ("Reduces temperature error", "bi-check-circle", [
            "A fill with a low expansion coefficient",
            "A low spring rate diaphragm",
            "The shortest practical capillary",
            "A higher instrument range where possible",
        ]),
        ("Increases temperature error", "bi-x-circle", [
            "Long capillaries exposed to sun or heat",
            "Low range gauges",
            "Overfilling, underfilling or trapped air",
            "Large swings in ambient temperature",
        ]),
    ]),
    h2("select", "Diaphragm Seal Selection Checklist"),
    checklist([
        ("Process conditions", "Confirm pressure, temperature, viscosity, solids and any pulsation or shock."),
        ("Wetted materials", "Choose diaphragm, lower housing and gasket materials compatible with the medium."),
        ("Diaphragm size", "Make sure displacement drives the instrument through its full range at the required accuracy."),
        ("Fill fluid", "Match the fill to temperature limits and to what is safe if it leaks into the process."),
        ("Connection", "Pick threaded, flanged, clamped or inline, and decide on direct mount or capillary."),
        ("Vacuum", "REOTEMP advises contacting the factory for deep vacuum below 5 psia."),
    ]),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Unscrewing the instrument from the seal.", "Breaking a filled connection loses fill fluid and lets air in, which ruins accuracy."),
        ("Ignoring pulsation.", "REOTEMP names pulsation as a common cause of gauge failure; fit a damping option."),
        ("Using a low range gauge on a long capillary.", "Temperature error becomes a large share of the reading."),
    ]),
    p("For unit checks, the " + ext("https://zentacalculator.com/engineering/absolute-gauge-pressure/", "absolute and gauge pressure calculator") + " helps, and " + ext("https://www.instrumentationblog.in/category/process-instrumentation/pressure-measurement/", "Instrumentation Blog") + " has more pressure measurement reading."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What is a diaphragm seal used for?", "It protects a pressure instrument from corrosive, viscous, abrasive, hot or toxic media by isolating it behind a flexible diaphragm."),
        ("Can a diaphragm seal be used with a transmitter?", "Yes. Seals fit pressure gauges, switches and transmitters, directly or through a capillary."),
        ("Why does a sealed gauge read differently when it gets hot?", "The fill fluid expands with temperature, which adds a small error. Fill choice, fill volume and capillary length decide how large it is."),
    ]),
]
