META = {
    "category": "gas-detection-guides",
    "title": "H2S Gas Detection Basics",
    "keyword": "H2S gas detection",
    "subtitle": "Why hydrogen sulfide is so dangerous, exposure limits, sensor types and where to place detectors",
    "meta_title": "H2S Gas Detection Basics: Limits, Sensors, Placement",
    "meta_description": "H2S gas detection basics: hydrogen sulfide hazards by ppm, OSHA and NIOSH limits, electrochemical and MOS sensors, detector placement and common mistakes.",
    "summary": "Why hydrogen sulfide needs instrument detection, the key exposure limits, which sensor to use and where to mount detectors.",
    "card_title": "H2S Gas Detection Basics",
    "author": "SWME Technical Staff",
    "published": "2026-11-19",
    "status": "published",
    "sort_order": 5,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "flow",
        "title": "From H2S Release to Alarm",
        "alt": "Infographic showing four stages from an H2S release to a detector alarm and response",
        "steps": [
            ["Release", "H2S escapes from a process, well or drain."],
            ["Sinks low", "Heavier than air, it collects in low lying areas."],
            ["Detected", "A sensor mounted low measures the ppm level."],
            ["Alarm", "Set points trigger alarms so people can respond."],
        ],
    },
}

_C = "#2b8a3e"
_T = "#1f6a2f"

import math as _m


def _x(ppm):
    return 90 + (_m.log10(ppm) + 2) * 125  # 0.01 ppm at x=90, 1,000 ppm at x=715


def _t(x, y, s, size=12, w="400", fill="#495057", anchor="middle"):
    return f'<text x="{x:.0f}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


def _mark(ppm, label1, label2, y, color, dx=0):
    x = _x(ppm)
    return (f'<line x1="{x:.0f}" y1="150" x2="{x:.0f}" y2="{y + 6}" stroke="{color}" stroke-width="1.5" stroke-dasharray="3 3"/>'
            f'<circle cx="{x:.0f}" cy="150" r="5" fill="{color}"/>'
            + _t(x + dx, y + 22, label1, 12, "700", color) + _t(x + dx, y + 38, label2, 12, "400", "#495057"))


_diag = (
    _t(400, 28, "Hydrogen sulfide concentration and key limits (ppm, log scale)", 15, "700", _T)
    # colour band
    + f'<rect x="{_x(0.01):.0f}" y="132" width="{_x(10) - _x(0.01):.0f}" height="18" fill="#d3f9d8"/>'
    + f'<rect x="{_x(10):.0f}" y="132" width="{_x(100) - _x(10):.0f}" height="18" fill="#ffec99"/>'
    + f'<rect x="{_x(100):.0f}" y="132" width="{_x(1000) - _x(100):.0f}" height="18" fill="#ffc9c9"/>'
    + f'<line x1="{_x(0.01):.0f}" y1="150" x2="{_x(1000):.0f}" y2="150" stroke="#495057" stroke-width="2"/>'
    + "".join(f'<line x1="{_x(v):.0f}" y1="150" x2="{_x(v):.0f}" y2="160" stroke="#495057" stroke-width="1.5"/>'
              + _t(_x(v), 176, lab, 12, "700") for v, lab in ((0.01, "0.01"), (0.1, "0.1"), (1, "1"), (10, "10"), (100, "100"), (1000, "1,000")))
    # odour band above
    + f'<rect x="{_x(0.01):.0f}" y="96" width="{_x(1.5) - _x(0.01):.0f}" height="22" rx="4" fill="#e7f5ff" stroke="#1971c2" stroke-width="1.5"/>'
    + _t((_x(0.01) + _x(1.5)) / 2, 112, "Odour threshold 0.01 to 1.5", 12, "700", "#1864ab")
    + f'<rect x="{_x(100):.0f}" y="96" width="{_x(150) - _x(100):.0f}" height="22" rx="4" fill="#fff4e6" stroke="#e8590c" stroke-width="1.5"/>'
    + _t(_x(100) - 6, 88, "Loss of smell 100 to 150", 12, "700", "#e8590c", "end")
    + f'<rect x="{_x(700):.0f}" y="96" width="{_x(1000) - _x(700):.0f}" height="22" rx="4" fill="#ffe3e3" stroke="#c92a2a" stroke-width="1.5"/>'
    + _t(_x(1000), 60, "Knockdown 700 to 1,000", 12, "700", "#c92a2a", "end")
    + f'<line x1="{(_x(700) + _x(1000)) / 2:.0f}" y1="66" x2="{(_x(700) + _x(1000)) / 2:.0f}" y2="96" stroke="#c92a2a" stroke-width="1.2"/>'
    # limits below
    + _mark(10, "10", "NIOSH REL", 190, "#2b8a3e")
    + _mark(20, "20", "OSHA ceiling", 240, "#e67700")
    + _mark(50, "50", "OSHA peak", 290, "#e67700")
    + _mark(100, "100", "NIOSH IDLH", 190, "#c92a2a", 18)
)

BODY = [
    takeaways([
        "Hydrogen sulfide is toxic, flammable and heavier than air, so it collects in low lying areas.",
        "At about 100 ppm it can deaden the sense of smell within minutes, so odour is not a warning.",
        "OSHA sets a 20 ppm ceiling for general industry; NIOSH sets 100 ppm as immediately dangerous to life and health.",
        "Electrochemical sensors are the usual choice for toxic H2S; MOS and optical options suit some conditions.",
    ]),
    p("Hydrogen sulfide is one of the most common hazards in oil and gas production, wastewater and chemical plants. It smells of rotten eggs at low levels, which gives a false sense of safety, because higher concentrations destroy the sense of smell. Reliable <strong>H2S gas detection</strong> with instruments is the only dependable warning.",
      "This guide explains the hazard, the limits, the sensor options and where detectors go. SWME supplies fixed and portable " + link("/gas-detectors", "gas detectors") + " and " + link("/test-calibration", "calibration equipment") + " across the UAE and GCC."),
    toc([("hazard", "Why H2S is so dangerous"), ("limits", "Exposure limits"), ("sensors", "Sensors for H2S gas detection"),
         ("placement", "Where to place detectors"), ("checklist", "Good practice checklist"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("hazard", "Why H2S Is So Dangerous"),
    p("" + ext("https://www.osha.gov/hydrogen-sulfide/hazards", "OSHA") + " describes hydrogen sulfide as a highly flammable, explosive gas with an explosive range in air of 4.3 to 45 percent. Workers are exposed mainly by breathing it. The odour threshold is 0.01 to 1.5 ppm, but at 100 ppm OSHA reports loss of smell after 2 to 15 minutes. " + ext("https://s1-live.emerson.com/documents/automation/technical-note-detecting-hydrogen-sulfide-gas-understanding-its-danger-in-field-rosemount-en-72142.pdf", "Emerson") + " adds that H2S is heavier than air and sinks to the lowest lying area."),
    table(["Concentration", "Effect reported by OSHA"],
          [["2 to 5 ppm", "Prolonged exposure may cause nausea, tearing eyes and headaches"],
           ["20 ppm", "Possible fatigue, headache, irritability, poor memory and dizziness"],
           ["100 ppm", "Coughing, eye irritation and loss of smell after 2 to 15 minutes"],
           ["500 to 700 ppm", "Staggering and collapse in 5 minutes; death after 30 to 60 minutes"],
           ["700 to 1,000 ppm", "Rapid unconsciousness within 1 or 2 breaths"]]),
    h2("limits", "Exposure Limits"),
    rows([
        ("OSHA PEL, general industry", "20 ppm ceiling, with a 50 ppm peak allowed for up to 10 minutes if there is no other exposure during the shift."),
        ("OSHA PEL, construction and shipyards", "10 ppm as an 8 hour average."),
        ("NIOSH REL", "10 ppm as a 10 minute ceiling."),
        ("NIOSH IDLH", "100 ppm, immediately dangerous to life and health."),
    ], "Limits published by OSHA"),
    svg(_diag, "Hydrogen sulfide concentrations on a log scale with odour threshold, exposure limits and knockdown level", 340),
    p("Local rules can be stricter. For example, Emerson quotes UK HSE limits of 5 ppm over 8 hours and 10 ppm over 15 minutes. Set alarm levels to your site procedure and the applicable regulation. The flammable range sits far above the toxic levels; for flammable gas basics read " + link("/lel-and-uel-explained", "LEL and UEL explained") + "."),
    h2("sensors", "Sensors for H2S Gas Detection"),
    p("Emerson compares the main technologies used for H2S gas detection. Our guide to " + link("/types-of-gas-sensors", "types of gas sensors") + " covers how each one works."),
    table(["Sensor", "Strengths", "Limitations"],
          [["Electrochemical", "High sensitivity and repeatability; T90 about 30 seconds in temperate conditions", "Affected by heat, dryness and humidity; slows near minus 20 degrees C; calibration about every six months"],
           ["Metal oxide semiconductor (MOS)", "Long life; works well at high temperature and in very dry air", "T90 up to 120 seconds for some makers; can stop responding until bump tested"],
           ["Open path optical", "Inherently fail safe; covers a line across an area", "Cannot give an accurate ppm value; needs a clear beam"]]),
    dyk("Electrochemical H2S sensors can dry out in hot, dry climates. Emerson notes that electrolyte evaporation in these conditions shortens sensor life, which matters for outdoor detectors in the Gulf summer."),
    h2("placement", "Where to Place Detectors"),
    INFOGRAPHIC,
    p("Good H2S gas detection depends on placement as much as on the sensor. Because H2S sinks, sensing elements must be placed to reflect that tendency. Mount fixed detectors low, close to likely leak points and wherever gas could collect. " + ext("https://www.draeger.com/en_sea/Safety/H2S-Dangers-and-Detection", "Draeger") + " recommends fixed, continuous monitoring for long production phases and personal monitors for field work. For mounting heights across gas types, see our " + link("/gas-detector-placement-guide", "gas detector placement guide") + "."),
    twocol([
        ("Fixed detectors", "bi-broadcast", ["Continuous area monitoring", "Mounted low near leak sources", "Alert at preset set points", "Suit long production phases"]),
        ("Portable monitors", "bi-person-badge", ["Worn by the individual worker", "Used during field inspection", "Single gas or multigas units", "Follow the same test routine"]),
    ]),
    h2("checklist", "Good Practice Checklist"),
    checklist([
        ("Know the source", "Map where H2S can be released and where it can collect."),
        ("Mount low", "Place sensors near ground level and in low points."),
        ("Match the climate", "Choose a sensor rated for local heat and humidity."),
        ("Test and calibrate", "Follow a routine; see " + link("/bump-test-vs-calibration-gas-detectors", "bump test vs calibration") + "."),
        ("Record results", "Log alarms, tests and calibrations for each detector."),
    ]),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Relying on smell.", "Lethal concentrations cannot be detected by nose, as Draeger warns."),
        ("Mounting detectors high.", "H2S is heavier than air and collects low."),
        ("Stretching calibration intervals.", "Drift and dry out go unnoticed without routine checks."),
    ]),
    p("For wireless fixed detection, see our " + link("/blog/vanguard-wireless-hart-gas-detector-uae", "Vanguard WirelessHART gas detector") + " post. The " + ext("https://zentacalculator.com/engineering/sensor-response-time/", "sensor response time calculator") + " helps compare T90 values, and " + ext("https://www.instrumentationblog.in/category/process-instrumentation/analytical-measurements/", "Instrumentation Blog") + " has more on analytical instruments."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("At what level is H2S dangerous?", "NIOSH lists 100 ppm as immediately dangerous to life and health, and OSHA sets a 20 ppm ceiling for general industry."),
        ("Where should H2S detectors be mounted?", "Low, near leak sources and low points, because hydrogen sulfide is heavier than air."),
        ("Which sensor is best for H2S gas detection?", "Electrochemical sensors are the usual choice for toxic H2S; MOS can suit very hot, dry sites."),
    ]),
]
