META = {
    "category": "level-measurement-guides",
    "title": "Capacitance Level Measurement Explained",
    "keyword": "capacitance level measurement",
    "subtitle": "How a probe and tank wall form a capacitor, why dielectric constant and conductivity matter, and how to calibrate and avoid build up errors",
    "meta_title": "Capacitance Level Measurement Explained",
    "meta_description": "Capacitance level measurement: probe and tank wall as a capacitor, dielectric constants, insulated probes for conductive liquids, calibration and build up.",
    "summary": "How capacitance level probes work, why the dielectric constant and conductivity of the liquid matter, and how to calibrate and install them.",
    "card_title": "Capacitance Level Measurement",
    "author": "SWME Technical Staff",
    "published": "2026-11-22",
    "status": "published",
    "sort_order": 7,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "flow",
        "title": "How a Capacitance Level Probe Works",
        "alt": "Infographic showing how a capacitance probe turns a rising liquid level into a 4 to 20 mA signal",
        "steps": [
            ["Two plates", "The probe rod is one plate and the tank wall or a reference tube is the other."],
            ["Level rises", "Liquid with a higher dielectric constant than air replaces the vapour around the probe."],
            ["Capacitance rises", "An empty tank gives a low capacitance and a full tank a high one."],
            ["Signal out", "The electronics give a relay change or a scaled 4 to 20 mA output."],
        ],
    },
}

_C = "#0c8599"
_T = "#0a5f6d"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_diag = (
    # tank
    '<rect x="250" y="70" width="300" height="290" fill="none" stroke="#495057" stroke-width="4"/>'
    + '<rect x="252" y="200" width="296" height="158" fill="#d3f0f4"/>'
    + '<line x1="252" y1="200" x2="548" y2="200" stroke="' + _C + '" stroke-width="2" stroke-dasharray="6 4"/>'
    # electronics head and probe
    + '<rect x="365" y="20" width="70" height="40" rx="6" fill="' + _C + '"/>'
    + _t(400, 45, "Electronics", 11, "700", "#fff", "middle")
    + '<rect x="390" y="60" width="20" height="12" fill="#868e96"/>'
    + '<rect x="394" y="72" width="12" height="270" rx="5" fill="#f08c00" stroke="#a35400" stroke-width="1.5"/>'
    + '<rect x="397" y="72" width="6" height="266" rx="3" fill="#495057"/>'
    # field lines between probe and wall in liquid
    + ''.join(f'<line x1="410" y1="{y}" x2="546" y2="{y}" stroke="{_C}" stroke-width="1.2" stroke-dasharray="3 4"/>' for y in (230, 270, 310))
    + ''.join(f'<line x1="254" y1="{y}" x2="392" y2="{y}" stroke="{_C}" stroke-width="1.2" stroke-dasharray="3 4"/>' for y in (230, 270, 310))
    # labels left
    + _t(230, 120, "Vapour space", 13, "700", "#495057", "end")
    + _t(230, 138, "dielectric constant about 1", 12, "400", "#555", "end")
    + _t(230, 260, "Liquid", 13, "700", _T, "end")
    + _t(230, 278, "higher dielectric constant,", 12, "400", "#555", "end")
    + _t(230, 296, "for example water about 80", 12, "400", "#555", "end")
    + _t(230, 360, "Tank wall: second plate", 13, "700", "#495057", "end")
    + '<line x1="234" y1="355" x2="250" y2="350" stroke="#495057" stroke-width="1.5"/>'
    # labels right
    + _t(570, 100, "Probe rod: first plate", 13, "700", "#a35400")
    + _t(570, 118, "insulated with PTFE or PFA", 12, "400", "#555")
    + _t(570, 136, "for conductive liquids", 12, "400", "#555")
    + '<line x1="566" y1="104" x2="408" y2="110" stroke="#a35400" stroke-width="1.5"/>'
    + _t(570, 205, "Level", 13, "700", _T)
    + _t(570, 250, "More of the probe is covered,", 12, "400", "#555")
    + _t(570, 268, "so capacitance rises", 12, "400", "#555")
    + _t(470, 45, "4 to 20 mA or relay", 12, "700", _T)
    + '<line x1="435" y1="40" x2="466" y2="40" stroke="' + _C + '" stroke-width="2"/>'
)


BODY = [
    takeaways([
        "A capacitance probe and the tank wall form a capacitor, and the capacitance rises as liquid covers the probe.",
        "The method depends on the dielectric constant of the product, so the probe must be calibrated empty and full.",
        "Conductive liquids need an insulated probe; nonconductive liquids often need a ground tube or reference electrode.",
        "Coating on the probe can give false high readings unless the probe has build up compensation.",
    ]),
    p("<strong>Capacitance level measurement</strong> works on liquids, slurries, viscous products and many bulk solids, and Emerson rates it as inexpensive. SWME supplies capacitance and other " + link("/level-transmitters", "level transmitters") + " and " + link("/level-switches", "level switches") + " for tanks across the UAE and GCC."),
    toc([("how", "How it works"), ("dielectric", "Dielectric constant"), ("conductive", "Conductive and nonconductive liquids"),
         ("probes", "Probe types and outputs"), ("calibration", "Calibration and build up"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("how", "How Capacitance Level Measurement Works"),
    p("Endress+Hauser describes the conductive tank wall and a probe inside the tank as a capacitor. The " + ext("https://emerson.com/documents/automation/engineering-guide-engineer-s-guide-to-level-measurement-2021-edition-en-77708.pdf", "engineer's guide to level measurement") + " adds that the metal rod is one plate, and the tank wall, or a reference electrode in a nonmetallic vessel, is the other. The " + ext("https://www.endress.com/en/support-overview/learning-center/capacitance-measuring-principle-animation", "capacitance principle animation") + " shows how an empty tank gives a lower capacitance and a full tank a higher one.",
      "The capacitance follows C = εA/d, where ε is the permittivity of the material between the plates, A is the plate area and d is the distance between them. The plates are fixed, so the change comes from the product replacing vapour around the probe. The " + ext("https://www.dwyeromega.com/en-us/resources/capacitance-level-sensor", "capacitance level sensor overview") + " writes the change as (K2 minus K1) × A/D, with air as the reference at K1 = 1.0."),
    INFOGRAPHIC,
    svg(_diag, "Capacitance level probe: the probe rod and tank wall are the two plates, and the liquid between them raises the capacitance as the level rises", 380),
    h2("dielectric", "Why the Dielectric Constant Matters"),
    p("The signal comes from the difference between the dielectric constant of the product and that of the vapour above it, so a product close to air gives a small change. Emerson gives air as 1.00058 and water as 81, both at 20 °C. Typical figures from the " + ext("https://www.vega.com/-/media/PDF-files/List_of_dielectric_constants_EN.pdf", "VEGA list of dielectric constants") + " are shown below."),
    table(["Product", "Dielectric constant (VEGA)"],
          [["Water", "80.3"], ["Acetone", "21.5"], ["Ethanol", "16.2"], ["Glycerol", "13.2"],
           ["Toluene", "2.4"], ["Diesel", "2.1"], ["Oil", "2.0"], ["Plastic pellets", "1.2"]]),
    p("Sources do not all agree on water: VEGA lists 80.3, Emerson 81 and another training source 88. In addition, Emerson notes the dielectric constant of hydrocarbons changes by 0.0013 to 0.05% per degree Celsius, and Omega lists temperature, moisture and humidity as causes of change."),
    dyk("In capacitance level measurement on a conductive liquid such as water, the reading does not depend on the dielectric constant at all. Endress+Hauser explains that the liquid forms a short circuit from the tank wall to the probe insulation, so only the insulation layer acts as the dielectric."),
    h2("conductive", "Conductive and Nonconductive Liquids"),
    twocol([
        ("Conductive liquids", "bi-droplet-fill", [
            "Use a fully insulated probe, for example PTFE or PFA coated",
            "Omega says a bare probe can short at 100 micromhos/cm or more",
            "Endress+Hauser allows factory calibration above 100 µS/cm",
            "Reading does not depend on dielectric constant or tank shape"]),
        ("Nonconductive liquids", "bi-droplet", [
            "A bare or partly insulated probe can be used",
            "Reading depends on dielectric constant and tank geometry",
            "Ground tube probes give a defined geometry",
            "Below 1 µS/cm the device must be calibrated on site"]),
    ]),
    p("Endress+Hauser warns that the range between 1 and 100 µS/cm is a critical range to avoid. Interface measurement follows the same rule: one layer must be above 100 µS/cm and the other below 1 µS/cm. Our guide to " + link("/interface-level-measurement-basics", "interface level measurement") + " compares capacitance with other ways of finding an interface."),
    h2("probes", "Probe Types and Outputs"),
    rows([
        ("Rod probe", "VEGA offers rod probes up to 6 m for liquids."),
        ("Cable probe", "VEGA cable probes reach up to 32 m for tall silos and tanks."),
        ("Concentric tube", "VEGA recommends a tube version for horizontal, spherical or asymmetric tanks."),
        ("Reference probe", "Nonmetallic tanks need a reference probe; Omega also mentions a second parallel probe or a conductive strip."),
        ("Point level", "The output is a relay state for high or low alarms. See our " + link("/level-switch-types", "level switch types") + " guide."),
        ("Continuous", "The output is a scaled 4 to 20 mA signal, often with HART. Omega gives a typical accuracy of 0.25% of range."),
    ]),
    p("To work out the current that matches a given level, use the " + ext("https://zentacalculator.com/engineering/4-20ma-scaling/", "4 to 20 mA scaling calculator") + ". If you need the volume rather than the height, the " + ext("https://zentacalculator.com/engineering/vertical-tank-volume/", "vertical tank volume calculator") + " converts the level reading into stored volume."),
    h2("calibration", "Calibration and Build Up"),
    p("VEGA says the capacitance is entered when the tank is empty and when it is full. A wet calibration sets 0% and 100% on the live process, while a dry calibration enters values directly. Emerson notes that devices for capacitance level measurement cannot be bench calibrated, so this step happens on site. Our blog on " + link("/blog/level-transmitter-calibration-mistakes", "level transmitter calibration mistakes") + " covers the errors that show up at this stage."),
    p("Material that sticks to the probe looks like level and gives a false high reading. Omega describes a second active section of the probe driven at the same potential and frequency as the measuring probe, which makes the reading immune to the coating. Endress+Hauser offers active build up compensation on its Liquicap FTI51 switch for viscous liquids."),
    checklist([
        ("Check conductivity", "Confirm whether the product is above 100 µS/cm or below 1 µS/cm, and avoid the range in between."),
        ("Check the dielectric constant", "A low value such as oil at 2.0 gives a small signal; consider a ground tube."),
        ("Check temperature limits", "Omega says polymer insulators are limited to about 175 to 230 °C."),
        ("Check viscosity and solids", "One training source says capacitance cannot measure liquids above 2000 cSt."),
        ("Plan for coating", "Choose build up compensation for sticky products."),
    ]),
    p("For a packaged sensor, read our blog on the " + link("/blog/gems-uls-200-capacitive-level-sensor-uae", "Gems ULS 200 capacitive level sensor") + ". If the product has a low or changing dielectric constant, " + link("/guided-wave-radar-level-measurement", "guided wave radar level measurement") + " may suit it better. More background on tank measurement is in this " + ext("https://www.instrumentationblog.in/category/process-instrumentation/level-measurement/", "collection of level measurement articles") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Using a bare probe in a conductive liquid.", "The liquid shorts the probe; use a fully insulated probe."),
        ("Skipping the empty and full calibration.", "The reading depends on the product and tank, so it must be set on site."),
        ("Ignoring a change of product.", "A new product with a different dielectric constant shifts the reading in nonconductive service."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Can capacitance level measurement work in a plastic tank?", "Yes, with a reference probe or ground tube, because the tank wall cannot act as the second plate."),
        ("Why does my probe read high when the tank is empty?", "Build up on the probe often causes this. A probe with build up compensation helps."),
        ("Does capacitance work on solids?", "Yes, on many bulk solids such as cement or flour, though Omega advises against light materials under 20 lb/ft³."),
    ]),
]
