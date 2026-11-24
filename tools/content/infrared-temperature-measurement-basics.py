META = {
    "category": "temperature-measurement-guides",
    "title": "Infrared Temperature Measurement Basics: Emissivity and Spot Size",
    "keyword": "infrared thermometer",
    "subtitle": "How an infrared thermometer reads temperature without contact, why emissivity and distance to spot ratio decide its accuracy, and what steam, glass and shiny metal do to the reading",
    "meta_title": "Infrared Temperature Measurement: Emissivity and Spot",
    "meta_description": "Infrared temperature measurement basics: how an infrared thermometer works, emissivity settings, distance to spot ratio, shiny surfaces, glass and steam.",
    "summary": "How an infrared thermometer works, how emissivity and the distance to spot ratio affect the reading, and the practical checks that give a reading you can trust.",
    "card_title": "Infrared Temperature Measurement",
    "author": "SWME Technical Staff",
    "published": "2026-11-24",
    "status": "published",
    "sort_order": 8,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "levels",
        "title": "Emissivity: How Well a Surface Radiates",
        "alt": "Infographic ranking surfaces by emissivity from a blackbody at 1.0 down to shiny metals that emit little and reflect a lot",
        "top_label": "Emits more",
        "bottom_label": "Emits less",
        "levels": [
            ["Blackbody, 1.0", "The ideal emitter. Dull black paint comes close to 1.0.", 0.92],
            ["Masking tape, 0.95", "DwyerOmega's value for tape stuck on the target.", 0.72],
            ["High setting", "Fluke: wood, paint and plastic.", 0.5],
            ["Low setting", "Fluke: shiny metals.", 0.28],
            ["Polished metal", "Low emissivity, high reflectivity. Readings may not be possible.", 0.08],
        ],
    },
}

_C = "#d9480f"
_T = "#a33608"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_diag = (
    # target surface
    '<rect x="40" y="60" width="40" height="260" fill="#adb5bd" stroke="#495057"/>'
    + _t(60, 345, "Target", 13, "700", "#495057")
    # spot on target
    + '<ellipse cx="80" cy="190" rx="8" ry="40" fill="' + _C + '" opacity="0.85"/>'
    # field of view cone from lens (x=600, aperture 170..210) to spot (150..230)
    + '<polygon points="84,150 600,172 600,208 84,230" fill="#fff1ea" stroke="' + _C + '" stroke-width="1.5"/>'
    # laser aiming line
    + '<line x1="604" y1="140" x2="84" y2="190" stroke="#c92a2a" stroke-width="1.5" stroke-dasharray="6 4"/>'
    + _t(330, 140, "Laser: aiming aid only", 12, "700", "#c92a2a")
    # IR arrows inside cone
    + '<line x1="140" y1="190" x2="560" y2="190" stroke="' + _C + '" stroke-width="2.5" marker-end="url(#air)"/>'
    + _t(340, 214, "Emitted infrared energy", 12, "700", _T)
    # instrument body
    + '<rect x="600" y="150" width="170" height="80" rx="10" fill="#495057"/>'
    + '<ellipse cx="606" cy="190" rx="8" ry="20" fill="#74c0fc" stroke="#1864ab"/>'
    + _t(634, 252, "Lens", 12, "700", "#495057")
    + '<rect x="660" y="178" width="24" height="24" fill="#ffd43b"/>'
    + _t(672, 140, "Detector", 12, "700", "#495057")
    + '<line x1="672" y1="146" x2="672" y2="176" stroke="#495057" stroke-width="1.2"/>'
    + _t(735, 186, "Signal", 12, "700", "#fff")
    + _t(735, 202, "and display", 12, "700", "#fff")
    # D:S dimension
    + '<line x1="80" y1="290" x2="606" y2="290" stroke="#495057" stroke-width="1.5"/>'
    + '<line x1="80" y1="280" x2="80" y2="300" stroke="#495057" stroke-width="1.5"/>'
    + '<line x1="606" y1="280" x2="606" y2="300" stroke="#495057" stroke-width="1.5"/>'
    + _t(343, 316, "Distance D: 12 inches", 13, "700", "#495057")
    + '<line x1="104" y1="150" x2="104" y2="230" stroke="#495057" stroke-width="1.5"/>'
    + _t(150, 104, "Spot S: 1 inch", 13, "700", "#495057")
    + '<line x1="112" y1="110" x2="104" y2="150" stroke="#495057" stroke-width="1"/>'
    + _t(343, 350, "A 12:1 instrument measures a 1 inch spot from 12 inches away (Fluke example)", 12, "400", "#555")
)
_defs = ('<defs><marker id="air" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
         '<path d="M0,0 L10,5 L0,10 z" fill="' + _C + '"/></marker></defs>')

BODY = [
    takeaways([
        "An infrared thermometer focuses the energy a surface radiates onto a detector, so it reads temperature without touching the target.",
        "Emissivity is the ratio of the energy a surface emits to what a blackbody emits at the same temperature; shiny metal emits little and reflects a lot.",
        "The distance to spot ratio sets how large an area you measure: at 12:1, a 1 inch spot from 12 inches away.",
        "Steam, dust, smoke and glass all get between the surface and the detector and change the reading.",
    ]),
    p("An <strong>infrared thermometer</strong> reads the temperature of a surface from a distance, without touching it. It sees the surface only, not the fluid inside a pipe. For process temperature you still need a contact sensor, such as the " + link("/rtd-thermocouples", "RTDs and thermocouples") + " and " + link("/temperature-gauges", "temperature gauges") + " that SWME supplies across the UAE."),
    toc([("work", "How an infrared thermometer works"), ("emissivity", "Emissivity"), ("spot", "Distance to spot ratio"),
         ("errors", "What disturbs the reading"), ("tips", "Getting a good reading"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("work", "How an Infrared Thermometer Works"),
    p("DwyerOmega describes the basic design as a lens that focuses infrared energy onto a detector, which turns it into an electrical signal. The signal is compensated for ambient temperature and shown as a temperature. Its " + ext("https://www.dwyeromega.com/en-ca/resources/infrared-thermometer", "infrared thermometer guide") + " covers the optics in more detail.",
      "Fluke's " + ext("https://www.fluke.com/en-us/learn/blog/temperature-calibration/infrared-temperature-calibration-101", "infrared temperature calibration primer") + " says the most common spectral band for general purpose infrared thermometers is 8 to 14 µm. The optics filter the incoming energy to that band."),
    svg(_defs + _diag, "Infrared thermometer: the lens collects energy from a spot on the target and focuses it on the detector. The laser only shows where you are aiming (not to scale)", 365),
    h2("emissivity", "Emissivity"),
    p("Fluke defines emissivity as the ratio of the radiant energy a surface emits to the energy a blackbody emits at the same temperature. A blackbody has an emissivity of 1.0 and real surfaces fall between 0 and 1. Smooth metals have low emissivity and high reflectivity, so an infrared thermometer pointed at them picks up reflected energy from the room as well."),
    INFOGRAPHIC,
    p("Fluke shows how much this matters: a 1% error in emissivity at 500 °C gives a 3.5 °C error in the calibration. Simple instruments have a Low setting for shiny metals and a High setting for wood, paint and plastic. Others let you adjust the value, which the methods below rely on."),
    rows([
        ("Tape", "Stick masking tape (emissivity 0.95) on the surface, measure the tape, and set the emissivity so a reading beside it matches. DwyerOmega limits this to about 500 °F (260 °C)."),
        ("Paint", "Coat a small area with dull black paint, close to 1.0, and use it the same way."),
        ("Drilled hole", "At high temperature, drill a hole at least 6 times as deep as its diameter. It acts as a blackbody."),
        ("Known temperature", "Heat a sample of the material to a known temperature and adjust emissivity until the instrument reads it."),
    ], "Four ways to find emissivity (DwyerOmega)"),
    h2("spot", "Distance to Spot Ratio"),
    p("The distance to spot ratio, written D:S, tells you how large an area the instrument averages over. Fluke's example: a 12:1 ratio means you measure a 1 inch spot from 12 inches away. Step back and the spot grows. DwyerOmega says the target should completely fill the field of view. Otherwise the instrument averages the target with whatever is behind it.",
      "The laser dot does not show the measured area. Fluke stresses that it is only an aiming aid. On a small pipe, move closer until the pipe is wider than the spot."),
    dyk("Fluke notes that glass is transparent to visible light but opaque to infrared longer than about 3 µm. An 8 to 14 µm thermometer pointed through a window reads the glass, not what is behind it."),
    h2("errors", "What Disturbs the Reading"),
    twocol([
        ("Between you and the target", "bi-cloud-haze2", [
            "Steam, dust and smoke scatter infrared energy (Fluke).",
            "Glass and inspection windows block the 8 to 14 µm band.",
            "Fluke also warns about dirty or scratched lenses.",
        ]),
        ("At the target or the instrument", "bi-thermometer-half", [
            "Shiny metal reflects energy from walls and windows, so the instrument may under report.",
            "A very cold target in a warm room is hard to read (Fluke).",
            "Below the dew point, ice can form on the target and change its emissivity.",
        ]),
    ]),
    h2("tips", "Getting a Good Reading"),
    checklist([
        ("Let the instrument settle", "Fluke suggests leaving it in its working environment for about 30 minutes before critical readings, and avoiding sudden temperature changes."),
        ("Set the emissivity", "Use the tape, paint or reference methods above on shiny or unknown surfaces."),
        ("Fill the spot", "Work out the spot size from the D:S ratio and your distance, and make sure the target is larger."),
        ("Keep the path clear", "Measure away from steam and dust, and never through glass."),
        ("Calibrate against a radiation source", "Fluke explains that infrared thermometers are calibrated against a blackbody cavity or flat plate source checked with a radiometer, not against a contact thermometer alone."),
    ]),
    p("Calibration of contact instruments is a different job; our " + link("/test-calibration", "test and calibration equipment") + " page lists what we supply, and the " + ext("https://www.instrumentationblog.in/temperature-gauge-calibration/", "temperature gauge calibration steps") + " show the contact method. For fixed process points, read " + link("/how-an-rtd-works", "how an RTD works") + " or our guide to " + link("/temperature-transmitter-basics", "temperature transmitters") + ". More background is in the " + ext("https://www.instrumentationblog.in/category/process-instrumentation/temperature-measurements/", "temperature measurement articles") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Reading the laser dot as the measured area.", "The measured spot is set by the D:S ratio and your distance, not by the dot."),
        ("Pointing at bare stainless or aluminium.", "Low emissivity makes the instrument under report. Use tape or paint, as Fluke's " + ext("https://www.fluke.com/en-sg/learn/blog/temperature/how-to-get-great-results-with-an-infrared-thermometer", "infrared thermometer tips") + " recommend."),
        ("Measuring through a sight glass.", "The instrument reads the glass, which is opaque in its band."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Can an infrared thermometer measure the fluid inside a pipe?", "No. It reads the surface it sees. For the process fluid, use a contact sensor in a thermowell."),
        ("What does a D:S ratio of 12:1 mean?", "At 12 inches from the target you measure a spot 1 inch across."),
        ("Why does my infrared thermometer read low on shiny metal?", "Shiny metal has low emissivity, so it emits less energy than the instrument expects. Correct the emissivity or cover the spot with tape or paint."),
    ]),
]
