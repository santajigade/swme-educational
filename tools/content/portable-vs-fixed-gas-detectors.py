META = {
    "category": "gas-detection-guides",
    "title": "Portable vs Fixed Gas Detectors: Which One Do You Need?",
    "keyword": "fixed gas detector",
    "subtitle": "What personal and fixed gas detection each protect, how they alarm and connect, and how they work together",
    "meta_title": "Portable vs Fixed Gas Detectors: Which Do You Need?",
    "meta_description": "Portable vs fixed gas detectors: what each protects, alarms, sensors, power, bump testing, links to PLC and shutdown, confined space use and using both.",
    "summary": "How a fixed gas detector protects an area and a portable monitor protects a worker, and how to decide which your site needs.",
    "card_title": "Portable vs Fixed Gas Detectors",
    "author": "SWME Technical Staff",
    "published": "2026-11-21",
    "status": "published",
    "sort_order": 6,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "grid",
        "title": "Choosing Portable or Fixed Gas Detection",
        "alt": "Infographic with four questions that decide between portable and fixed gas detectors",
        "steps": [
            ["Who or what to protect", "Fixed detectors protect the facility; portable monitors protect the person wearing them."],
            ["Where the gas is", "Fixed suits known leak points; portable follows the worker into new or confined spaces."],
            ["What must happen on alarm", "Fixed systems can start ventilation or shut a process down; portable alarms rely on the worker."],
            ["How it is maintained", "Both need gas tests; portable units are often bump tested in a docking station."],
        ],
    },
}

_C = "#2b8a3e"
_T = "#1f6a2f"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


def _det(x, y):
    return (f'<rect x="{x - 14}" y="{y - 18}" width="28" height="36" rx="5" fill="{_C}"/>'
            f'<circle cx="{x}" cy="{y + 8}" r="5" fill="#fff"/>')


_diag = (
    '<defs><marker id="ahg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="#495057"/></marker></defs>'
    # left: fixed system
    + _t(30, 30, "Fixed: protects the area", 15)
    + '<rect x="30" y="50" width="380" height="270" rx="10" fill="#f8f9fa" stroke="#ced4da" stroke-width="2"/>'
    # equipment
    + '<rect x="70" y="200" width="90" height="100" rx="8" fill="#e9ecef" stroke="#495057" stroke-width="2"/>'
    + _t(115, 255, "Pump", 13, anchor="middle", fill="#495057")
    + '<rect x="230" y="180" width="120" height="120" rx="60" fill="#e9ecef" stroke="#495057" stroke-width="2"/>'
    + _t(290, 245, "Vessel", 13, anchor="middle", fill="#495057")
    + _det(115, 160) + _det(290, 140)
    + _t(115, 128, "Detector", 11, "600", anchor="middle") + _t(310, 136, "Detector", 11, "600")
    # wiring to controller
    + '<path d="M129,160 L200,160 L200,80 L276,80 L276,140" fill="none" stroke="#495057" stroke-width="2" stroke-dasharray="6 4"/>'
    + '<line x1="200" y1="80" x2="200" y2="70" stroke="#495057" stroke-width="2" stroke-dasharray="6 4"/>'
    + '<rect x="150" y="56" width="100" height="16" fill="none"/>'
    + _t(60, 76, "Field wiring", 11, "400", "#555")
    + '<line x1="276" y1="80" x2="440" y2="80" stroke="#495057" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#ahg)"/>'
    + '<rect x="450" y="50" width="150" height="70" rx="8" fill="' + _C + '"/>'
    + _t(525, 80, "Controller,", 13, "700", "#fff", "middle") + _t(525, 100, "PLC or DCS", 13, "700", "#fff", "middle")
    + '<line x1="600" y1="85" x2="640" y2="85" stroke="#495057" stroke-width="2" marker-end="url(#ahg)"/>'
    + _t(650, 66, "Alarms", 12, "600", "#343a40") + _t(650, 86, "Ventilation", 12, "600", "#343a40")
    + _t(650, 106, "Process shutdown", 12, "600", "#343a40")
    # right: portable
    + _t(460, 170, "Portable: protects the worker", 15)
    + '<circle cx="560" cy="210" r="20" fill="#ffe8cc" stroke="#495057" stroke-width="2"/>'
    + '<rect x="535" y="232" width="50" height="80" rx="12" fill="#d0ebff" stroke="#495057" stroke-width="2"/>'
    + '<rect x="565" y="240" width="16" height="22" rx="3" fill="' + _C + '"/>'
    + '<line x1="600" y1="212" x2="600" y2="252" stroke="#c92a2a" stroke-width="2"/>'
    + '<line x1="594" y1="212" x2="606" y2="212" stroke="#c92a2a" stroke-width="2"/>'
    + '<line x1="594" y1="252" x2="606" y2="252" stroke="#c92a2a" stroke-width="2"/>'
    + _t(614, 228, "Within 10 inches", 12, "700", "#c92a2a") + _t(614, 246, "of nose and mouth", 12, "400", "#555")
    + _t(614, 280, "Battery powered", 12, "400", "#555") + _t(614, 298, "alarms the wearer only", 12, "400", "#555")
    + _t(30, 345, "Both are point detectors: they only see gas that reaches the sensor", 13, "600", "#343a40")
)

BODY = [
    takeaways([
        "A fixed gas detector protects a facility and gives early warning of leaks; a portable monitor protects the person wearing it.",
        "Fixed systems can trigger alarms, ventilation, process shutdowns or fire suppression; portable units are not tied to any safety system.",
        "MSA says most portable monitors detect one to four gases, and advanced models up to six.",
        "Both are point detectors that only see gas reaching the sensor, and both need regular gas testing.",
    ]),
    p("A <strong>fixed gas detector</strong> and a portable monitor do different jobs. MSA calls their roles complementary, and Industrial Scientific says you should never give up a personal monitor because a fixed one is already in the area. SWME supplies " + link("/gas-detectors", "gas detectors") + " for oil and gas, utilities and industry across the UAE and GCC."),
    toc([("diff", "Fixed gas detector vs portable"), ("compare", "Side by side"), ("alarm", "Alarms and connections"),
         ("maint", "Testing and maintenance"), ("choose", "How to choose"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("diff", "Fixed Gas Detector vs Portable Monitor"),
    p("" + ext("https://www.indsci.com/en/blog/fixed-gas-detectors-vs-personal-gas-detectors", "Industrial Scientific") + " says fixed monitors are used mainly to protect a facility, detect catastrophic leaks or give early warning, while personal monitors protect the people working in an area. " + ext("https://blog.msasafety.com/fgfd-gas-detectors-fixed-versus-portable-gas-detectors-making-the-right-safety-choice-for-your-application/", "MSA") + " describes a fixed system as anything from one detector to hundreds, hardwired to a wall mounted controller or brought into a PLC or DCS. A portable monitor moves with the user and reads the gas in the breathing zone."),
    INFOGRAPHIC,
    svg(_diag, "Fixed detectors at leak points are wired to a controller that runs alarms and shutdowns; a portable monitor is worn in the breathing zone", 360),
    h2("compare", "Side by Side"),
    table(["Point", "Fixed gas detector", "Portable monitor"],
          [["Protects", "The facility and personnel in the area", "The individual wearing it"],
           ["Mounting", "Installed permanently, usually on walls or near leak points", "Carried or clipped to clothing"],
           ["Power", "Dedicated power supply and field wiring; some are now wireless", "Usually battery powered"],
           ["Response", "Can trigger alarms, ventilation, shutdowns or fire suppression", "Alarms the wearer; the staff decide what to do"],
           ["Best fit", "Continuous monitoring of known hazards, remote points, plants running 24/7", "Confined space entry, maintenance, leak investigation, temporary work"]]),
    p("For sensor choice, MSA notes infrared sensors are more common in fixed systems because of their higher power needs, and ultrasonic leak detection is also typically fixed. Our guide to " + link("/types-of-gas-sensors", "types of gas sensors") + " covers each principle."),
    h2("alarm", "Alarms and Connections"),
    p("Interscan's " + ext("https://gasdetection.com/articles/fixed-or-portable-gas-detectors-what-does-your-facility-need/", "comparison") + " says both types have audible and visual alarms for gas above exposure limits, low oxygen or the LEL. In a fixed system, one sensor in alarm can set off the others on the same control panel. MSA adds that smart detectors with HART or Modbus make integration with a PLC or DCS simpler. For control system layout, see " + ext("https://zentaengineering.com/automation-robotics/plc-hardware-selection/", "PLC hardware selection") + " and " + ext("https://zentaengineering.com/automation-robotics/scada-system-architecture/", "SCADA system architecture") + "."),
    rows([
        ("Breathing zone", "Interscan says to wear a portable unit no more than 10 inches from the nose and mouth."),
        ("Gas behaviour", "MSA notes methane tends to rise, hydrogen sulfide tends to sink and carbon monoxide mixes readily with air. See our " + link("/gas-detector-placement-guide", "gas detector placement guide") + "."),
        ("Sensor life", "MSA puts electrochemical sensor life at commonly two to three years, with newer designs reaching five to seven."),
    ], "At a glance"),
    dyk("MSA points out that few organisations can justify a fixed gas detector in every manhole or confined space. Portable monitors with sampling pumps and tubing let workers test the space before they enter, without exposing themselves."),
    h2("maint", "Testing and Maintenance"),
    p("Industrial Scientific says the only way to be certain a monitor will detect gas is to test it with gas. Interscan says both types ideally need a bump test before every shift, and that fixed sensors are less likely to be bump tested and calibrated in practice. " + ext("https://sensidyne.com/application/should-i-use-portable-gas-detectors-or-fixed-gas-monitors/", "Sensidyne") + " says personal monitors must be checked before each use: battery, response to the target gases and alarms. Read more in " + link("/bump-test-vs-calibration-gas-detectors", "bump test vs calibration") + "."),
    twocol([
        ("Fixed", "bi-building", ["Periodic inspection", "Calibration at the maker's interval", "Sensor replacement by service life"]),
        ("Portable", "bi-person-badge", ["Functional check before each use", "Often bump tested in a docking station", "Rechargeable battery care"]),
    ]),
    h2("choose", "How to Choose"),
    checklist([
        ("Hazard", "A known, continuous leak risk points to a fixed gas detector; changing or temporary work points to portable."),
        ("Action needed", "If gas must start ventilation or shut a process down, only a fixed system can do it."),
        ("People", "For confined space entry and maintenance, MSA points to portable monitors, even where fixed detection exists."),
        ("Gases", "List them; for toxic gas see " + link("/h2s-gas-detection-basics", "H2S gas detection") + " and for flammables " + link("/lel-and-uel-explained", "LEL and UEL") + "."),
        ("Area rating", "MSA lists intrinsically safe and explosion proof or flameproof designs for hazardous locations."),
    ]),
    p("For a wireless fixed option, see our blog on the " + link("/blog/vanguard-wireless-hart-gas-detector-uae", "Vanguard WirelessHART gas detector") + ". Background on analysers is in the " + ext("https://www.instrumentationblog.in/category/process-instrumentation/analytical-measurements/", "Instrumentation Blog analytical section") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Dropping personal monitors because fixed detection is installed.", "Industrial Scientific says a leak and a worker can both end up in a spot no fixed detector covers."),
        ("Treating portable monitors as continuous area monitoring.", "Interscan says they are not made for it."),
        ("Choosing on price alone.", "MSA says the two are not interchangeable on price."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Can a portable monitor replace a fixed gas detector?", "No. MSA says portable detectors supplement fixed systems rather than replace them."),
        ("Can a fixed system shut down a process?", "Yes. It can be configured to trigger alarms, ventilation, process shutdowns or fire suppression."),
        ("How often should I bump test?", "Interscan says ideally before every shift, for both fixed and portable detectors."),
    ]),
]
