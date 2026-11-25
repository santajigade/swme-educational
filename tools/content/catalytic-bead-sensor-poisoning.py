META = {
    "category": "gas-detection-guides",
    "title": "Catalytic Bead Sensor Poisoning and How to Avoid It",
    "keyword": "catalytic bead sensor",
    "subtitle": "How silicones, lead, sulfur compounds and halogenated solvents poison or inhibit an LEL sensor, how the two differ, and the filter, handling and test habits that keep a catalytic bead sensor reading correctly",
    "meta_title": "Catalytic Bead Sensor Poisoning: Causes and Prevention",
    "meta_description": "How a catalytic bead sensor is poisoned or inhibited by silicones, lead, H2S and halogenated solvents, the difference between the two, and how to prevent it.",
    "summary": "How silicones, lead, sulfur compounds and halogenated solvents poison or inhibit a catalytic bead LEL sensor, and the habits that prevent it.",
    "card_title": "Catalytic Bead Sensor Poisoning",
    "author": "SWME Technical Staff",
    "published": "2026-11-25",
    "status": "published",
    "sort_order": 9,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "steps",
        "title": "Keeping an LEL Sensor Free of Poisons",
        "alt": "Infographic with four steps to protect a catalytic bead LEL sensor: use the recommended filter, keep silicones away, test before use and service after exposure",
        "steps": [
            ["Fit the recommended filter", "Change it weekly, or straight after exposure to a poison."],
            ["Keep silicones away", "No silicone lubricants, polishes, sealants or hand creams near the instrument."],
            ["Test before use", "Always test the monitor before you rely on it."],
            ["Service after exposure", "Clean the pump and replace the tubing, filter and gasket."],
        ],
    },
}

_C = "#2b8a3e"
_T = "#1f6a2f"


def _t(x, y, s, size=13, w="700", fill="#495057", anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


def _res(cx, cy, ang, label, lx, ly, anchor):
    return (f'<rect x="{cx - 22}" y="{cy - 8}" width="44" height="16" fill="#fff" stroke="#495057" stroke-width="2" transform="rotate({ang} {cx} {cy})"/>'
            + _t(lx, ly, label, 13, "700", "#495057", anchor))


def _bead(cx, cy, fill, label, lx, ly, anchor, sub):
    return (f'<circle cx="{cx}" cy="{cy}" r="16" fill="{fill}" stroke="#495057" stroke-width="2"/>'
            + _t(lx, ly, label, 13, "700", _T, anchor) + _t(lx, ly + 16, sub, 12, "400", "#555", anchor))


_diag = (
    # bridge diamond A(330,50) M1(200,180) M2(460,180) B(330,310)
    '<polyline points="330,50 200,180 330,310 460,180 330,50" fill="none" stroke="#495057" stroke-width="2"/>'
    + _bead(265, 115, "#ffa94d", "Detector", 245, 92, "end", "catalyst, gas burns here")
    + _bead(265, 245, "#dee2e6", "Compensator", 245, 262, "end", "matched to the detector")
    + _res(395, 115, 45, "Fixed R1", 420, 100, "start")
    + _res(395, 245, -45, "Fixed R2", 420, 270, "start")
    # output meter between M1 and M2
    + '<line x1="200" y1="180" x2="310" y2="180" stroke="#495057" stroke-width="2"/>'
    + '<line x1="350" y1="180" x2="460" y2="180" stroke="#495057" stroke-width="2"/>'
    + '<circle cx="330" cy="180" r="20" fill="#fff" stroke="' + _C + '" stroke-width="2.5"/>' + _t(330, 186, "V", 16, "700", _C)
    + _t(330, 220, "Output", 12, "700", _C)
    # supply on left
    + '<polyline points="330,50 60,50 60,160" fill="none" stroke="#495057" stroke-width="2"/>'
    + '<polyline points="60,200 60,310 330,310" fill="none" stroke="#495057" stroke-width="2"/>'
    + '<line x1="40" y1="160" x2="80" y2="160" stroke="#495057" stroke-width="3"/>'
    + '<line x1="50" y1="172" x2="70" y2="172" stroke="#495057" stroke-width="3"/>'
    + '<line x1="40" y1="188" x2="80" y2="188" stroke="#495057" stroke-width="3"/>'
    + '<line x1="50" y1="200" x2="70" y2="200" stroke="#495057" stroke-width="3"/>'
    + _t(100, 184, "Supply", 12, "700", "#495057", "start")
    # explanation panel
    + '<rect x="560" y="60" width="220" height="240" rx="10" fill="#ecf8ee" stroke="' + _C + '"/>'
    + _t(670, 88, "In gas", 14, "700", _T)
    + _t(670, 114, "Gas oxidises on the", 12, "400", "#333") + _t(670, 130, "detector and heats it", 12, "400", "#333")
    + _t(670, 156, "Its resistance changes", 12, "400", "#333") + _t(670, 172, "relative to the compensator", 12, "400", "#333")
    + _t(670, 198, "The bridge goes out of", 12, "400", "#333") + _t(670, 214, "balance: output voltage", 12, "400", "#333")
    + '<line x1="580" y1="232" x2="760" y2="232" stroke="' + _C + '"/>'
    + _t(670, 256, "Poisoned detector:", 13, "700", "#c92a2a")
    + _t(670, 274, "less oxidation, less signal,", 12, "400", "#333") + _t(670, 290, "the reading falls", 12, "400", "#333")
)

BODY = [
    takeaways([
        "A catalytic bead sensor burns gas on a heated catalyst and measures the heat as a change in resistance in a bridge circuit.",
        "Poisons such as silicones cause a permanent loss of sensitivity; inhibitors such as halogenated solvents depress readings, and the sensor usually recovers in clean air.",
        "Just a few ppm of silicone vapour can degrade the sensor.",
        "A recommended filter, changed weekly, plus testing before use, are the main defences.",
    ]),
    p("A <strong>catalytic bead sensor</strong> is the classic way to measure flammable gas as a percentage of the LEL. Some chemicals that are common on industrial sites can reduce its sensitivity, partly or completely. SWME supplies fixed and portable " + link("/gas-detectors", "gas detectors") + " across the UAE."),
    toc([("work", "How a catalytic bead sensor works"), ("poison", "Poisons and inhibitors"), ("sources", "Where poisons come from"),
         ("prevent", "How to prevent poisoning"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("work", "How a Catalytic Bead Sensor Works"),
    p("Honeywell's technical note on " + ext("https://automation.honeywell.com/content/dam/his-sandbox/products/gas-and-flame-detection/documents/Technical-Note-144_Handling-LEL-Sensor-Poisons_03-99.pdf", "handling LEL sensor poisons") + " describes a matched detector and compensator, each a coil of platinum wire embedded in a catalytic bead. When combustible gas oxidises, the heat changes the resistance of one element relative to the other. The bridge circuit detects this as an out of balance voltage.",
      "The sensor needs oxygen to detect gas, as JJS Technical Services points out in its notes on the " + ext("https://jjstech.com/limitations-of-lel-sensors.html", "limitations of LEL sensors") + ". Our " + link("/types-of-gas-sensors", "guide to gas sensor types") + " compares it with infrared and other sensors, and " + link("/lel-and-uel-explained", "LEL and UEL explained") + " covers what the reading means."),
    svg(_diag, "Bridge circuit of a catalytic bead sensor: gas burning on the detector bead unbalances the bridge and produces an output voltage. A poisoned detector burns less gas, so the output falls", 340),
    h2("poison", "Poisons and Inhibitors"),
    p("Honeywell separates the two: poisoning is a permanent degradation, while inhibition is usually recoverable by exposure to clean air. It adds that silicones are usually counted as a poison and H2S as an inhibitor, but most compounds fall into both categories to some degree."),
    table(["Compound", "Effect", "Source"], [
        ["Silicones, silanes, silicates", "The most serious poisons; a few ppm degrade performance", "Honeywell"],
        ["Tetraethyl lead", "Reduces sensitivity, especially for methane and other gases with high ignition temperatures", "Honeywell"],
        ["Phosphate esters, phosphorus compounds", "Poison; oxidised to mineral acids that may corrode the sensor", "Honeywell, JJS"],
        ["H2S and other sulfur compounds", "Inhibitor and poison; corrosive byproducts can damage the bead permanently", "JJS"],
        ["Halogenated hydrocarbons (Freons, trichloroethylene, methylene chloride)", "Inhibitor; depresses readings while present, mostly recovers in fresh air", "JJS"],
        ["High concentrations of combustible gas", "Damages the sensor", "JJS"],
    ]),
    p("JJS explains that whether H2S does lasting harm depends on how fast the bead cooks off its byproducts. That in turn depends on bead operating temperature, bead size and whether the bead is powered continuously or pulsed. In addition, Honeywell notes that high concentrations of halogenated hydrocarbons break down to HCl on the bead, which can corrode it and give low readings."),
    dyk("Silicone resistant sensors carry an external filter that removes most silicone vapour before it reaches the bead. JJS notes the trade off: the heavier the hydrocarbon, the more the filter reduces the sensor's response to it."),
    h2("sources", "Where Poisons Come From"),
    twocol([
        ("Silicone sources", "bi-droplet", [
            "Lubricants and mould release agents.",
            "Polishes, adhesives and hand creams.",
            "Silicone rubber, caulk and sealants.",
        ]),
        ("Inhibitor and corrosive sources", "bi-cloud-haze2", [
            "Chlorinated solvents.",
            "PVC insulated wire overheated during soldering.",
            "Hot organic acids such as acetic acid, and acid gases.",
        ]),
    ]),
    h2("prevent", "How to Prevent Poisoning"),
    INFOGRAPHIC,
    checklist([
        ("Use the recommended filter", "Honeywell says to always fit one and change it weekly, or immediately after exposure to a poison."),
        ("Keep silicones out of the workshop", "Do not use silicone polishes, cleaners, lubricants or hand creams where instruments are assembled, tested or stored, and never use silicone lubricated gas valves or regulators with LEL sensors."),
        ("Use the maker's spare parts", "Silicone gaskets, potting, self stick labels and some moulded plastics can carry poisons into the monitor."),
        ("Limit exposure", "Turn portable monitors off when not in use, and in poison environments reduce the flow over the sensor or use a diffusion monitor."),
        ("Test before use", "Honeywell says to always test gas monitors before use, and to clean the pump and replace tubing, filter and gasket after serious exposure."),
    ]),
    p("A bump test is the quick way to prove the sensor still responds; read " + link("/bump-test-vs-calibration-gas-detectors", "bump test vs calibration") + " for the difference, and see our " + link("/test-calibration", "test and calibration equipment") + ". When you choose the detector itself, our " + link("/portable-vs-fixed-gas-detectors", "portable vs fixed detector guide") + " and the article on the " + link("/blog/vanguard-wireless-hart-gas-detector-uae", "Vanguard wireless gas detector") + " cover the options. More reading is in these " + ext("https://www.instrumentationblog.in/category/process-instrumentation/analytical-measurements/", "analytical measurement articles") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Spraying silicone lubricant near detectors.", "A few ppm of silicone vapour is enough to degrade a catalytic bead sensor."),
        ("Leaving the same filter in for months.", "Honeywell's guidance is weekly, or straight after poison exposure."),
        ("Assuming a low reading means no gas.", "A poisoned or inhibited sensor reads low. Test it with gas before you trust it."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What is the difference between poisoning and inhibition?", "Poisoning permanently degrades the sensor. Inhibition depresses the reading while the compound is present, and the sensor usually recovers in clean air."),
        ("What is the worst poison for a catalytic bead sensor?", "Silicones. Honeywell calls silicon compounds the most serious poisons."),
        ("Does a catalytic bead sensor need oxygen?", "Yes. It needs oxygen to burn the gas on the bead."),
    ]),
]
