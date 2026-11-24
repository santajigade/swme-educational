META = {
    "category": "flow-measurement-guides",
    "title": "Flow Switches Explained: Types, Setpoint and Deadband",
    "keyword": "flow switch",
    "subtitle": "How paddle, piston, shuttle and thermal flow switches detect flow, how to set the trip point and deadband, and where they protect pumps, boilers and chillers",
    "meta_title": "Flow Switches Explained: Types, Setpoint and Deadband",
    "meta_description": "Flow switches explained: paddle, piston, shuttle and thermal types, how to choose the setpoint, deadband on rising and falling flow, and installation tips.",
    "summary": "How a flow switch trips at a set flow rate, the main sensing types and their limits, and how to pick a setpoint that avoids nuisance trips.",
    "card_title": "Flow Switches Explained",
    "author": "SWME Technical Staff",
    "published": "2026-11-24",
    "status": "published",
    "sort_order": 8,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "steps",
        "title": "How a Flow Switch Trips and Resets",
        "alt": "Infographic showing a flow switch in its normal state, tripping at the setpoint on rising flow, resetting at a lower flow and sending a signal",
        "steps": [
            ["Normal state", "Below the trip point the contacts sit in their normal position."],
            ["Flow rises to setpoint", "The paddle or sensor responds and the contacts change state."],
            ["Flow falls back", "The switch resets at a lower flow rate. The gap is the deadband."],
            ["Signal acts", "The contact stops a pump, trips a boiler or raises an alarm."],
        ],
    },
}

_C = "#1971c2"
_T = "#14508a"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_paddle = (
    '<defs><marker id="afs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="' + _C + '"/></marker></defs>'
    # pipe
    + '<rect x="20" y="182" width="340" height="96" fill="#eef5fd"/>'
    + '<line x1="20" y1="180" x2="360" y2="180" stroke="#495057" stroke-width="4"/>'
    + '<line x1="20" y1="280" x2="360" y2="280" stroke="#495057" stroke-width="4"/>'
    # tee and switch housing
    + '<rect x="166" y="140" width="48" height="40" fill="#adb5bd" stroke="#495057"/>'
    + '<rect x="140" y="60" width="100" height="80" rx="8" fill="#495057"/>'
    + _t(190, 92, "Switch", 13, "700", "#fff")
    + _t(190, 110, "housing", 13, "700", "#fff")
    + _t(190, 128, "C  NO  NC", 11, "400", "#dee2e6")
    # pivot and deflected paddle
    + '<circle cx="190" cy="184" r="6" fill="#14508a"/>'
    + '<line x1="190" y1="184" x2="236" y2="264" stroke="#14508a" stroke-width="7" stroke-linecap="round"/>'
    + '<line x1="190" y1="184" x2="190" y2="264" stroke="#868e96" stroke-width="3" stroke-dasharray="6 5"/>'
    + _t(140, 254, "No flow", 11, "400", "#868e96")
    + _t(285, 254, "Flow at", 11, "700", _T)
    + _t(285, 268, "setpoint", 11, "700", _T)
    # flow arrow
    + '<line x1="36" y1="230" x2="130" y2="230" stroke="' + _C + '" stroke-width="4" marker-end="url(#afs)"/>'
    + _t(80, 216, "Flow", 14, "700", _T)
    + _t(190, 312, "Paddle flow switch", 14, "700", _T)
)

# deadband chart: x = flow 10..18 GPM -> 450..770 px, y: off 250, on 110
def _x(q):
    return 450 + (q - 10) * 40


_chart = (
    '<line x1="450" y1="270" x2="780" y2="270" stroke="#495057" stroke-width="1.5"/>'
    + '<line x1="450" y1="60" x2="450" y2="270" stroke="#495057" stroke-width="1.5"/>'
    + _t(615, 304, "Flow rate (GPM)", 12, "700", "#495057")
    + _t(430, 114, "Tripped", 11, "700", "#495057", "end")
    + _t(430, 254, "Normal", 11, "700", "#495057", "end")
    + "".join(_t(_x(q), 288, str(q), 11, "400", "#555") for q in (10, 12, 14, 15, 16, 18))
    # rising path (blue)
    + f'<polyline points="{_x(10)},244 {_x(15)},244 {_x(15)},116 {_x(18)},116" fill="none" stroke="{_C}" stroke-width="3" marker-end="url(#afs)"/>'
    # falling path (red)
    + f'<polyline points="{_x(18)},104 {_x(14)},104 {_x(14)},256 {_x(10)},256" fill="none" stroke="#c92a2a" stroke-width="3"/>'
    + _t(_x(16.6), 162, "Rising: trips at 15", 12, "700", _C)
    + _t(_x(12.3), 82, "Falling: resets at 14", 12, "700", "#c92a2a")
    + f'<line x1="{_x(14)}" y1="180" x2="{_x(15)}" y2="180" stroke="#495057" stroke-width="1.5"/>'
    + _t(_x(15) + 8, 184, "Deadband", 11, "700", "#495057", "start")
)

BODY = [
    takeaways([
        "A flow switch does not measure flow rate. It changes its contacts when flow passes a setpoint.",
        "Paddle, piston, shuttle and thermal dispersion designs suit different pipe sizes, pressures and fluids.",
        "Gems advises a setpoint at least 25% below the low end of your normal flow, because switch accuracy can be 10 to 20%.",
        "Every flow switch has a deadband: it trips on rising flow at one rate and resets on falling flow at a lower one.",
    ]),
    p("A <strong>flow switch</strong> watches a pipe and changes a contact when flow reaches a set rate. DwyerOmega describes it as a device that makes and breaks an electric current to monitor flow. Gems is clear that it will not show the actual flow rate, only when flow has reached the setpoint. SWME supplies " + link("/flow-switches", "flow switches") + " for plants across the UAE."),
    toc([("work", "How a flow switch works"), ("types", "Flow switch types"), ("setpoint", "Setpoint and deadband"),
         ("uses", "Where flow switches are used"), ("select", "Selection and installation"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("work", "How a Flow Switch Works"),
    p("The " + ext("https://control.com/textbook/discrete-process-measurement/flow-switches/", "flow switch chapter of an industrial instrumentation textbook") + " describes the common paddle design: fluid moving past a paddle pushes it, and the motion actuates one or more switch contacts. The switch is in its normal state for any flow below the trip threshold. Normally open and normally closed describe the contacts in that low flow state."),
    INFOGRAPHIC,
    svg(_paddle + _chart, "Left: a paddle in a tee deflects with flow and operates the switch. Right: a textbook example of a switch tripping at 15 GPM rising and resetting near 14 GPM falling", 330),
    h2("types", "Flow Switch Types"),
    table(["Type", "How it senses flow", "Gems figures"],
          [["Paddle or vane", "Flow deflects a paddle that operates the contacts", "Up to 2000 PSI, pipes up to 10 inch"],
           ["Piston", "A magnetic piston moves with flow and operates a sealed reed switch", "Port sizes down to ¼ inch NPT"],
           ["Shuttle", "A shuttle moves with flow, with low pressure drop at full flow", "¾ to 2 inch NPT, suits viscous liquids"],
           ["Thermal dispersion", "Flow carries heat away from a heated sensor", "No moving parts, ½ to 1½ inch NPT"]]),
    p("The " + ext("https://www.gemssensors.com/knowledge/technology-functionality/select-liquid-flow-switch-guide", "Gems liquid flow switch selection guide") + " gives these ranges and says thermal switches need little or no filtration. DwyerOmega's " + ext("https://www.dwyeromega.com/en-us/resources/what-is-flow-switch", "flow switch overview") + " explains the thermal type with two temperature sensors: higher flow cools the heated sensor more, so the temperature difference between them falls.",
      "RS lists further types. Magnetic switches use Faraday's law and need a conductive fluid, which is why they are common in wastewater. Clamp on ultrasonic switches need particles or bubbles in the liquid, so they do not suit drinking or distilled water. In addition, variable area switches use a float in a tapered tube, the same idea as " + link("/how-a-rotameter-works", "how a rotameter works") + "."),
    h2("setpoint", "Setpoint and Deadband"),
    p("Gems recommends finding the average flow rate first and setting the trip point at least 25% below the low end of your flow range. Setting it too close to normal flow causes nuisance trips. Switch accuracy may be 10 to 20%. For example, a 1 GPM setpoint at 20% accuracy may switch anywhere from 0.8 to 1.2 GPM. Gems quotes setpoints from 50 ml/min up to 50 gal/min across its range.",
      "The same textbook gives the deadband example in the diagram: a switch that trips at 15 GPM rising will not reset at 15 GPM falling, but more likely near 14 GPM. Deadband is also called differential. If your setpoint is in GPM or litres per minute, the " + ext("https://zentacalculator.com/engineering/pipe-flow-velocity/", "pipe flow velocity calculator") + " shows what velocity that means in your pipe size."),
    dyk("RS notes that most flow switches made for fire sprinkler systems include a delay timer, so a brief surge in the line does not raise a false alarm."),
    h2("uses", "Where Flow Switches Are Used"),
    twocol([
        ("Protecting equipment", "bi-shield-check", [
            "Pumps: stop the motor on loss of supply to prevent dry running (RS).",
            "Coolant lines: Gems names loss of coolant flow as the most common use.",
            "Chillers: stop on low or no flow that can lead to freeze damage (RS).",
            "Boilers: trip on low water flow (RS).",
        ]),
        ("Confirming flow", "bi-check2-circle", [
            "Fire sprinklers: detect water flow above a set rate.",
            "Boiler flues: a gas flow switch stops firing until the flue is venting.",
            "HVAC ducts: air flow switches trip above or below a set rate.",
            "Pool and spa heat pumps: stop when water flow is interrupted.",
        ]),
    ]),
    p("Our blog on " + link("/blog/pump-protection-pressure-flow-temperature-instruments", "pump protection instruments") + " shows how a flow switch works alongside pressure and temperature switches. For product examples, see the " + link("/blog/dwyer-v4-flow-switch-suppliers-in-uae", "Dwyer V4 flow switch") + " and the " + link("/blog/dwyer-v6-flow-switch-suppliers-in-uae", "Dwyer V6 flow switch") + "."),
    h2("select", "Selection and Installation"),
    checklist([
        ("Know the flow range", "Find the average flow, then set the trip point below the low end as Gems advises."),
        ("Match the fluid", "Check wetted parts and body material against the liquid. RS says paddles are sensitive to debris and residue, and industrial paddles avoid magnetic parts in rusty water."),
        ("Check temperature and pressure", "RS lists high temperature switches rated up to 350 °C and above."),
        ("Give it straight pipe", "RS suggests a straight section of ideally 10 pipe diameters before and after the switch, away from bends, valves, drains and size changes."),
        ("Plan for testing", "RS suggests watching the switch change state, or checking continuity across the contacts with an ohmmeter."),
    ]),
    p("If you also need to see the flow rate, a " + link("/rotameters", "rotameter") + " or a " + link("/flowmeters", "flow meter") + " shows it. Our guide to " + link("/types-of-flow-meters", "types of flow meters") + " compares the options, and the " + ext("https://www.instrumentationblog.in/category/process-instrumentation/flow-measurement/", "flow measurement articles") + " go deeper into each principle."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Setting the trip point near normal flow.", "Switch accuracy of 10 to 20% puts the trip inside normal operation and causes nuisance trips."),
        ("Expecting the switch to reset at the trip point.", "Allow for the deadband when you write the pump or alarm logic."),
        ("Ignoring wear and scale.", "RS notes that paddles wear and need replacement, and that limescale degrades switches in shower pumps."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What is the difference between a flow switch and a flow meter?", "A flow switch only changes a contact at a setpoint. A flow meter measures and shows the flow rate."),
        ("Which flow switch has no moving parts?", "The thermal dispersion type, which senses the heat that flow carries away from a heated sensor."),
        ("Why does my flow switch reset at a lower flow than it trips?", "That gap is the deadband, also called differential. The textbook example is a switch that trips at 15 GPM rising and resets near 14 GPM falling."),
    ]),
]
