META = {
    "category": "temperature-measurement-guides",
    "title": "Temperature Transmitter Basics",
    "keyword": "temperature transmitter",
    "subtitle": "What a temperature transmitter does, mounting styles, 4 to 20 mA and HART, failure signals and selection",
    "meta_title": "Temperature Transmitter Basics: How They Work",
    "meta_description": "Temperature transmitter basics: why convert RTD and thermocouple signals, head, rail and field mounting, 4 to 20 mA, HART, NAMUR NE43 and selection tips.",
    "summary": "What a temperature transmitter does, how head, rail and field mounting compare, and how to choose one for an RTD or thermocouple.",
    "card_title": "Temperature Transmitter Basics",
    "author": "SWME Technical Staff",
    "published": "2026-11-19",
    "status": "published",
    "sort_order": 5,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "compare",
        "title": "Head vs Rail vs Field Mount",
        "alt": "Infographic comparing head mount, rail mount and field mount temperature transmitters",
        "columns": [
            ["Head mount", ["Fits inside the sensor connection head", "Shortest sensor wiring", "Copper pair to the control room"]],
            ["Rail mount", ["Clips onto a DIN rail in a cabinet", "Sensor wired back to the panel", "Spring clips for quick fitting"]],
            ["Field mount", ["Own housing on the equipment", "Mounted outdoors at the process", "Choose an enclosure rating to suit"]],
        ],
    },
}

_C = "#d9480f"
_T = "#a33608"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


def _mx(ma):
    return 60 + ma * 30  # 0 mA at x=60, 22 mA at x=720


_ne43 = (
    _t(400, 30, "4 to 20 mA signal ranges under NAMUR NE43", 15)
    + f'<rect x="{_mx(0)}" y="70" width="{_mx(3.6) - _mx(0)}" height="50" fill="#ffc9c9" stroke="#c92a2a" stroke-width="1.5"/>'
    + f'<rect x="{_mx(3.6)}" y="70" width="{_mx(4) - _mx(3.6)}" height="50" fill="#fff3bf" stroke="#f59f00" stroke-width="1.5"/>'
    + f'<rect x="{_mx(4)}" y="70" width="{_mx(20) - _mx(4)}" height="50" fill="#d3f9d8" stroke="#2b8a3e" stroke-width="1.5"/>'
    + f'<rect x="{_mx(20)}" y="70" width="{_mx(21) - _mx(20)}" height="50" fill="#fff3bf" stroke="#f59f00" stroke-width="1.5"/>'
    + f'<rect x="{_mx(21)}" y="70" width="{_mx(22) - _mx(21)}" height="50" fill="#ffc9c9" stroke="#c92a2a" stroke-width="1.5"/>'
    + _t((_mx(0) + _mx(3.6)) / 2, 100, "Failure", 14, fill="#c92a2a")
    + _t((_mx(21) + _mx(22)) / 2, 100, "Fail", 11, fill="#c92a2a")
    + _t((_mx(4) + _mx(20)) / 2, 92, "Measuring range", 14, fill="#2b8a3e")
    + _t((_mx(4) + _mx(20)) / 2, 110, "0 to 100 percent", 12, "400", "#2b8a3e")
    + "".join(f'<line x1="{_mx(v)}" y1="120" x2="{_mx(v)}" y2="134" stroke="#495057" stroke-width="1.5"/>' for v in (0, 3.6, 4, 20, 21))
    + _t(_mx(0), 152, "0", 12, "700", "#495057")
    + _t(_mx(3.6) - 8, 152, "3.6", 12, "700", "#495057")
    + _t(_mx(4) + 10, 152, "4", 12, "700", "#495057")
    + _t(_mx(20) - 6, 152, "20", 12, "700", "#495057")
    + _t(_mx(21) + 8, 152, "21", 12, "700", "#495057")
    + _t(_mx(22) + 30, 152, "mA", 12, "700", "#495057")
    + _t(_mx(3.8), 196, "3.8 mA: lowest valid", 12, "400", "#555")
    + _t(_mx(3.8), 212, "measurement signal", 12, "400", "#555")
    + f'<line x1="{_mx(3.8)}" y1="120" x2="{_mx(3.8)}" y2="180" stroke="#f59f00" stroke-width="1.5" stroke-dasharray="3 3"/>'
    + _t(_mx(20.5) - 40, 196, "20.5 mA: highest valid", 12, "400", "#555")
    + _t(_mx(20.5) - 40, 212, "measurement signal", 12, "400", "#555")
    + f'<line x1="{_mx(20.5)}" y1="120" x2="{_mx(20.5)}" y2="180" stroke="#f59f00" stroke-width="1.5" stroke-dasharray="3 3"/>'
    + _t(400, 250, "At or below 3.6 mA, or at or above 21 mA, the host treats the signal as a fault.", 13, "400", "#495057")
)

BODY = [
    takeaways([
        "A temperature transmitter converts a small RTD or thermocouple signal into a standard output, usually 4 to 20 mA.",
        "It removes noise, linearises and scales the reading, and lets plain copper wire replace sensor cable.",
        "Head, rail and field mounting suit different plants; the choice affects wiring length and access.",
        "NAMUR NE43 failure currents and HART diagnostics help the control system spot a broken sensor.",
    ]),
    p("RTD and thermocouple signals are low level, and sending them a long way to a control room invites noise and error. Current signals outperform voltage over long distances and in noisy environments, so a <strong>temperature transmitter</strong> converts the sensor signal close to the process.",
      "This guide covers how it works, mounting options, output signals and how to choose one. SWME supplies " + link("/temperature-transmitters", "temperature transmitters") + " and matching " + link("/rtd-thermocouples", "RTD and thermocouple sensors") + " in the UAE and the wider GCC."),
    toc([("what", "What a temperature transmitter does"), ("chain", "The signal chain"), ("mounting", "Mounting styles"),
         ("signals", "Output and failure signals"), ("select", "Selection checklist"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("what", "What a Temperature Transmitter Does"),
    p("" + ext("https://automationforum.co/temperature-transmitter-selection-guide/", "Automation Forum") + " describes a temperature transmitter as a device that takes the signal from a thermocouple or RTD and converts it to a standard output that control systems can read. Its main jobs are signal conditioning (noise removal, linearisation and scaling), transmission and remote monitoring."),
    rows([
        ("RTD input", "Two, three or four wire RTDs; four wire gives the best accuracy. Read " + link("/how-an-rtd-works", "how an RTD works") + " for the basics."),
        ("Thermocouple input", "Types J, K, T, E, N, R, S and B, with built in cold junction compensation. See " + link("/thermocouple-types-explained", "thermocouple types explained") + "."),
        ("Isolation", "Automation Forum recommends galvanic isolation of at least 1,500 V between input, output and power to prevent ground loops."),
        ("System accuracy", "The accuracy of the loop is the sum of the sensor and the transmitter errors."),
    ], "Inputs and key terms"),
    h2("chain", "The Signal Chain"),
    p("" + ext("https://control.com/technical-articles/loop-powered-two-wire-transmitters-for-analog-sensors/", "Control.com") + " explains that a loop powered transmitter takes its power from the loop current, so all its circuitry must run on less than 4 mA. The supply is usually, but not always, 24 V DC. When the transmitter sits in the sensor head, the wiring to the control room can be a single pair of copper wires instead of thermocouple cable or the three or four wires an RTD needs."),
    svg_chain(["Sensor|RTD or TC", "Transmitter|condition, scale", "Two wire loop|4 to 20 mA", "Control system|PLC or DCS"],
              "Signal chain from a temperature sensor through a loop powered transmitter to the control system",
              ["ohms or millivolts", "near the process", "copper pair, 24 V DC", "reads the current"]),
    h2("mounting", "Mounting Styles"),
    INFOGRAPHIC,
    p("Head mount units sit inside the connection head of the sensor. According to " + ext("https://instrumentationtools.com/head-mount-temperature-transmitter/amp/", "Instrumentation Tools") + ", this removes the need for lead wire compensation and long compensating cable on thermocouples. Rail mount units clip onto a DIN rail in a cabinet, while field mount units have their own housing on the process equipment."),
    h2("signals", "Output and Failure Signals"),
    p("The 4 to 20 mA signal uses an elevated zero: 4 mA is 0 percent and 20 mA is 100 percent. Control.com notes that this allows readings slightly below 0 percent and makes a broken wire easy to detect. Digital protocols such as HART, Modbus, PROFIBUS and Foundation Fieldbus add remote configuration and diagnostics."),
    svg(_ne43, "NAMUR NE43 current ranges for a 4 to 20 mA temperature transmitter", 270),
    p("Under NAMUR NE43, " + ext("https://www.electricalvolt.com/what-is-namur-ne-43", "Electrical Volt") + " gives 3.8 mA and 20.5 mA as the limits of the valid measurement signal, and Automation Forum gives 3.6 mA and 21 mA as the failure limits. Set the transmitter to drive upscale or downscale on sensor failure to suit the safe state of the loop. The " + ext("https://zentacalculator.com/engineering/4-20ma-scaling/", "4 to 20 mA scaling calculator") + " converts current to temperature, and the " + ext("https://zentacalculator.com/engineering/loop-resistance/", "loop resistance calculator") + " checks the supply budget."),
    dyk("A transmitter can only be as accurate as its sensor. Automation Forum suggests about plus or minus 0.1 degrees C with drift under 0.1 degrees C per year for critical loops, and plus or minus 0.3 to 0.5 degrees C for general monitoring loops."),
    h2("select", "Temperature Transmitter Selection Checklist"),
    checklist([
        ("Sensor type", "Match the input: RTD wiring (two, three or four wire) or the thermocouple letter type."),
        ("Mounting", "Head, rail or field, based on wiring distance, access and ambient conditions."),
        ("Output", "4 to 20 mA, HART or a fieldbus that your control system reads."),
        ("Isolation and EMC", "Galvanic isolation and compliance with IEC 61326 near motors and drives."),
        ("Hazardous area", "Certification to IEC 60079 where the plant needs it."),
        ("Safety loops", "SIL capability to IEC 61508 for safety instrumented functions."),
    ]),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Wrong input configuration.", "A K type sensor read as J, or a three wire RTD set as two wire, gives a steady but wrong reading."),
        ("Copper wire on a remote thermocouple.", "Use matching extension cable up to the transmitter, or mount the transmitter in the head."),
        ("Ignoring failure direction.", "Choose upscale or downscale burnout to match the safe action of the loop."),
    ]),
    p("For wiring diagrams, see " + ext("https://www.instrumentationblog.in/temperature-transmitter-wiring/", "Instrumentation Blog") + ". For sensor choice at high temperature, read our post on " + link("/blog/rtd-vs-thermocouple-high-temperature-guide", "RTD vs thermocouple") + ", and check lead wire effects with the " + ext("https://zentacalculator.com/engineering/rtd-lead-wire-error/", "RTD lead wire error calculator") + "."),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What does a temperature transmitter do?", "It converts the RTD or thermocouple signal into a standard output such as 4 to 20 mA that a PLC or DCS can read."),
        ("Is a temperature transmitter loop powered?", "Most are two wire, loop powered devices that run on less than 4 mA drawn from a 24 V DC loop."),
        ("Head mount or rail mount?", "Head mount keeps sensor wiring short; rail mount keeps the electronics in a cabinet for easy access."),
    ]),
]
