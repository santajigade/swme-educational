META = {
    "category": "flow-measurement-guides",
    "title": "Turbine Flow Meter Basics: Principle, K Factor and Installation",
    "keyword": "turbine flow meter",
    "subtitle": "How the rotor and pickup make a pulse signal, what the K factor means, how viscosity affects accuracy and how much straight pipe the meter needs",
    "meta_title": "Turbine Flow Meter Basics: Principle and K Factor",
    "meta_description": "Turbine flow meter basics: rotor and pickup principle, K factor and flow formula, accuracy and turndown, viscosity effects, straight run and strainers.",
    "summary": "How a turbine flow meter turns rotor speed into pulses, how to use the K factor, and the viscosity and installation rules that decide its accuracy.",
    "card_title": "Turbine Flow Meter Basics",
    "author": "SWME Technical Staff",
    "published": "2026-11-23",
    "status": "published",
    "sort_order": 7,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "flow",
        "title": "From Rotor Speed to Flow Rate",
        "alt": "Infographic showing how a turbine flow meter turns rotor speed into pulses and then into a flow rate using the K factor",
        "steps": [
            ["Flow turns the rotor", "Fluid on the angled blades spins the rotor in proportion to its velocity."],
            ["Pickup makes pulses", "A pickup senses the passing blades; each pulse stands for a small volume."],
            ["Pulses form a frequency", "The pickoff frequency is proportional to the flow rate."],
            ["K factor gives flow", "Divide frequency by the K factor for flow, or count pulses for the total."],
        ],
    },
}

_C = "#1971c2"
_T = "#14508a"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_wave = "M620,100 " + " ".join(f"L{620 + 20 * k},{100 if k % 2 == 0 else 60} L{640 + 20 * k},{100 if k % 2 == 0 else 60}" for k in range(8))

_diag = (
    '<defs><marker id="aht" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="' + _C + '"/></marker></defs>'
    # pipe and flanges
    + '<rect x="40" y="132" width="560" height="116" fill="#eef5fd"/>'
    + '<line x1="40" y1="130" x2="600" y2="130" stroke="#495057" stroke-width="4"/>'
    + '<line x1="40" y1="250" x2="600" y2="250" stroke="#495057" stroke-width="4"/>'
    + '<rect x="150" y="114" width="12" height="152" fill="#adb5bd" stroke="#495057"/>'
    + '<rect x="498" y="114" width="12" height="152" fill="#adb5bd" stroke="#495057"/>'
    # hangers and shaft
    + '<line x1="220" y1="132" x2="220" y2="248" stroke="#868e96" stroke-width="5"/>'
    + '<line x1="440" y1="132" x2="440" y2="248" stroke="#868e96" stroke-width="5"/>'
    + '<line x1="220" y1="190" x2="440" y2="190" stroke="#495057" stroke-width="4"/>'
    + '<ellipse cx="220" cy="190" rx="10" ry="16" fill="#868e96"/>'
    + '<ellipse cx="440" cy="190" rx="10" ry="16" fill="#868e96"/>'
    # rotor
    + '<polygon points="318,176 342,176 354,136 330,136" fill="' + _C + '"/>'
    + '<polygon points="318,204 342,204 330,244 306,244" fill="' + _C + '"/>'
    + '<rect x="314" y="174" width="32" height="32" rx="4" fill="#14508a"/>'
    # pickup and cable
    + '<rect x="314" y="76" width="32" height="52" rx="4" fill="#495057"/>'
    + '<line x1="346" y1="90" x2="610" y2="90" stroke="#495057" stroke-width="2"/>'
    + _t(356, 82, "Magnetic pickup", 13, "700", "#495057")
    + '<path d="' + _wave + '" fill="none" stroke="#c92a2a" stroke-width="2.5"/>'
    + _t(620, 46, "Pulse output", 13, "700", "#c92a2a")
    + _t(620, 124, "Frequency rises", 12, "400", "#555")
    + _t(620, 140, "with flow rate", 12, "400", "#555")
    # flow arrow
    + '<line x1="52" y1="190" x2="135" y2="190" stroke="' + _C + '" stroke-width="4" marker-end="url(#aht)"/>'
    + _t(56, 176, "Flow", 14, "700", _T)
    # labels under the pipe
    + _t(220, 284, "Upstream hanger", 12, "700", "#495057", "middle")
    + _t(330, 284, "Rotor", 12, "700", _C, "middle")
    + _t(440, 284, "Downstream hanger", 12, "700", "#495057", "middle")
    + _t(220, 300, "and bearing", 12, "400", "#555", "middle")
    + _t(440, 300, "and bearing", 12, "400", "#555", "middle")
    # straight run
    + '<line x1="40" y1="330" x2="150" y2="330" stroke="#495057" stroke-width="1.5"/>'
    + '<line x1="40" y1="322" x2="40" y2="338" stroke="#495057" stroke-width="1.5"/>'
    + '<line x1="150" y1="322" x2="150" y2="338" stroke="#495057" stroke-width="1.5"/>'
    + _t(95, 352, "10D straight run", 12, "700", "#495057", "middle")
    + '<line x1="510" y1="330" x2="600" y2="330" stroke="#495057" stroke-width="1.5"/>'
    + '<line x1="510" y1="322" x2="510" y2="338" stroke="#495057" stroke-width="1.5"/>'
    + '<line x1="600" y1="322" x2="600" y2="338" stroke="#495057" stroke-width="1.5"/>'
    + _t(555, 352, "5D outlet", 12, "700", "#495057", "middle")
    # formula box
    + '<rect x="620" y="190" width="170" height="78" rx="10" fill="#eef5fd" stroke="' + _C + '" stroke-width="2"/>'
    + _t(705, 216, "Q = 60 f / K", 15, "700", _T, "middle")
    + _t(705, 238, "Q in gpm, f in Hz", 12, "400", "#555", "middle")
    + _t(705, 255, "K in pulses per gallon", 12, "400", "#555", "middle")
)

BODY = [
    takeaways([
        "Fluid spins a bladed rotor at a speed proportional to its velocity, and a pickup turns that rotation into pulses.",
        "The K factor is the number of pulses per unit volume; flow rate is the pulse frequency divided by K.",
        "Liquid turbine meters are sensitive to viscosity, so a meter calibrated on water reads wrong on a thicker fluid.",
        "Omega gives a standard straight run of 10 pipe diameters upstream and 5 downstream, with more after elbows and valves.",
    ]),
    p("A <strong>turbine flow meter</strong> measures volumetric flow by counting how fast a rotor turns in the stream. Emerson lists fiscal and custody transfer of hydrocarbons among its uses, and DwyerOmega adds aerospace and cryogenic service. SWME supplies turbine and other " + link("/flowmeters", "flow meters") + " for plants across the UAE and GCC."),
    toc([("principle", "How a turbine flow meter works"), ("kfactor", "The K factor"), ("accuracy", "Accuracy and turndown"),
         ("viscosity", "Viscosity effects"), ("install", "Installation rules"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("principle", "How a Turbine Flow Meter Works"),
    p("Emerson explains that the angular velocity of the rotor is directly proportional to the fluid velocity, and the angle of the blades to the stream sets how fast it turns. A pickoff on the meter body senses the rotor, and its output frequency is proportional to the flow rate. Each pulse also stands for a small fixed volume, so a totaliser can count total flow with a maximum error of one pulse, whatever the volume. The " + ext("https://www.emerson.com/pl-pl/automation/measurement-instrumentation/flow-measurement/about-liquid-turbine-flow-meters", "liquid turbine meter overview") + " covers the rotor and pickoff design.",
      "DwyerOmega lists solid state pickups (reluctance, inductance, capacitive and Hall effect) and mechanical gear or magnetic drives. Hall effect sensors work down to 0.2 ft/s, while magnetic pickups need 0.5 to 1.0 ft/s."),
    INFOGRAPHIC,
    svg(_diag, "Turbine flow meter: the rotor sits on bearings between two hangers, and a magnetic pickup turns rotor speed into a pulse frequency", 365),
    h2("kfactor", "The K Factor"),
    p("Flomec defines the K factor as a calibration constant from the meter manufacturer: the number of pulses per unit volume, for example pulses per gallon or per litre. Omega writes it as K = 60f/Q, with f in Hz, Q in gpm and K in pulses per gallon. Flomec's worked example: 500 Hz × 60 s ÷ 100 pulses per gallon = 300 gpm. The " + ext("https://flomecmeters.com/blogs/did-you-know/turbine-flow-meter-frequency-and-k-factor", "frequency and K factor explainer") + " also shows how to work in litres.",
      "The calculator below solves for flow rate, frequency or K factor when you know the other two, so you can check a flow computer or PLC scaling against the meter's calibration sheet."),
    '<div class="my-4"><iframe src="https://zentacalculator.com/embed/engineering/flow-meter-k-factor/" title="Flow Meter K-Factor Calculator" width="100%" height="640" loading="lazy" style="border:1px solid #e2e5ee;border-radius:12px;max-width:720px;"></iframe>'
    '<p>' + ext("https://zentacalculator.com/engineering/flow-meter-k-factor/", "Flow Meter K Factor Calculator") + ' by ' + ext("https://zentacalculator.com/", "Zenta Calculator") + '</p></div>',
    dyk("DwyerOmega notes that a K factor applies only to the fluid the meter was calibrated on. Change the fluid and the pulses per gallon change too."),
    h2("accuracy", "Accuracy and Turndown"),
    rows([
        ("Accuracy", "Typically stated as a percentage of actual rate. Omega gives ±1% of rate or better, and ±0.5% of reading on low viscosity fluids."),
        ("Linear range", "DwyerOmega says barstock meters are linear to ±0.25% of rate over a 10:1 flow range."),
        ("Repeatability", "±0.2% to ±0.02% over the linear range (DwyerOmega); ±0.1% for the Blancett B1100."),
        ("Turndown", "Up to 100:1 if accuracy is derated to 1% of full scale. Gas meters reach 20:1 at low pressure and up to 100:1 at elevated pressure."),
        ("Low end", "Meters can show a nonlinear hump in the lower 25 to 30% of their range."),
    ], "At a glance"),
    p("For gas, DwyerOmega notes that meters are designed to make up for the lower driving torque of a low density fluid, and natural gas turbine meters follow " + ext("https://webstore.ansi.org/standards/aga/agaxq0601", "AGA Report No. 7") + ". Our guide to " + link("/types-of-flow-meters", "types of flow meters") + " shows where turbines sit against other technologies."),
    h2("viscosity", "Viscosity Effects"),
    p("Omega calls turbine meters very sensitive to viscosity and viscosity changes. Meters are calibrated on water at 1 centistoke, and a thicker fluid shifts the low end of the range most. DwyerOmega says the meter performs well when the Reynolds number is above 4,000 and up to 20,000, and that temperature effects on viscosity must be compensated or controlled. You can check your line with the " + ext("https://zentacalculator.com/engineering/reynolds-number/", "Reynolds number calculator") + ".",
      "Omega's remedy is a Universal Viscosity Calibration. " + ext("https://www.nist.gov/node/426151", "NIST turbine meter calibration research") + " plots Strouhal number against Reynolds or Roshko number, and finds the data collapse to a single curve for Reynolds numbers above 2000. NIST avoids the name universal viscosity curve because it does not hold over every part of the curve."),
    h2("install", "Installation Rules"),
    table(["Upstream fitting", "Straight run before the meter (Omega)"],
          [["Standard minimum", "10 diameters (5 downstream)"], ["Concentric reducer", "15 diameters"],
           ["Sweeping elbow or tee", "20 diameters"], ["Two sweeping elbows", "25 diameters"],
           ["Wide open valve", "14 diameters"], ["Partially open valve", "50 diameters"]]),
    checklist([
        ("Strain the line", "Omega gives mesh 100 for 1/4 to 1/2 inch meters, mesh 70 up to 1 1/4 inch and mesh 40 for 1 1/2 to 3 inch. DwyerOmega asks for a strainer or filter at least 20 diameters upstream when solids exceed 100 mg/l of +75 micron size."),
        ("Size for the average flow", "DwyerOmega suggests an expected average flow of 60 to 75% of maximum capacity, with 3 to 5 psid pressure drop at maximum flow."),
        ("Prevent cavitation", "Keep downstream pressure at 1.25 times the vapour pressure plus twice the pressure drop."),
        ("Fill slowly", "The Blancett manual says to open the upstream isolating valve slowly to avoid hydraulic shock."),
        ("Watch the bearings", "Omega says bearing life is roughly inversely proportional to the square of bearing speed; at 33% of maximum flow, life extends by a factor of ten."),
    ]),
    p("SWME stocks " + link("/strainers", "strainers") + " for meter protection and " + link("/flow-transmitters", "flow transmitters") + " for the pulse signal. For another meter that also gives a frequency output, read about the " + link("/vortex-flow-meter-working-principle", "vortex flow meter working principle") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Blowing air or gas through a liquid meter.", "The Blancett manual warns excess air pressure can damage the rotor and bearings by overspinning."),
        ("Using a water K factor on oil.", "Viscosity shifts the calibration; calibrate on the actual fluid or use a viscosity calibration."),
        ("Skipping the straight run.", "The Blancett manual says accuracy may be affected without 10D upstream and 5D downstream. Our blog on " + link("/blog/flow-meter-incorrect-readings-causes-fixes", "flow meter incorrect readings") + " lists other causes."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What output does a turbine flow meter give?", "A pulse frequency proportional to flow rate. Counting the pulses gives the total volume."),
        ("How do I find the flow from the frequency?", "Divide the frequency by the K factor. For gpm with K in pulses per gallon, flow = 60 × f ÷ K."),
        ("Why does my turbine meter read wrong at low flow?", "The low end is most affected by viscosity and the nonlinear hump in the lower 25 to 30% of the range."),
    ]),
]
