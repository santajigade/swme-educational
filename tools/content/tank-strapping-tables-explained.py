import math as _m

META = {
    "category": "level-measurement-guides",
    "title": "Tank Level to Volume: Strapping Tables Explained",
    "keyword": "strapping table",
    "subtitle": "What a tank strapping table is, why level and volume are not proportional in horizontal and spherical tanks, how tanks are calibrated, and how transmitters and DCS systems use the table",
    "meta_title": "Tank Level to Volume: Strapping Tables Explained",
    "meta_description": "Strapping table explained: tank level to volume, the horizontal tank formula, calibration methods, transmitter linearisation, interpolation and TOV to GSV.",
    "summary": "How a strapping table converts a measured tank level into volume, why horizontal and spherical tanks need one, how tanks are calibrated and how transmitters use it.",
    "card_title": "Tank Strapping Tables",
    "author": "SWME Technical Staff",
    "published": "2026-11-26",
    "status": "published",
    "sort_order": 10,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "steps",
        "title": "From Measured Level to Standard Volume",
        "alt": "Infographic showing how a tank level reading becomes a volume: measure level, read the strapping table, get total observed volume, subtract free water, apply the volume correction factor",
        "steps": [
            ["Measure the level", "A level gauge or transmitter gives the liquid height."],
            ["Read the table", "The tank capacity table gives the volume at that height, interpolating between rows."],
            ["Total observed volume", "The table volume is the TOV, after any shell temperature correction."],
            ["Subtract free water", "TOV minus free water gives the gross observed volume, GOV."],
            ["Correct to standard", "GOV times the volume correction factor gives GSV at 15 °C or 60 °F."],
        ],
    },
}

_C = "#0c8599"
_T = "#0a5f6d"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="middle"):
    return f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


def _frac(k):
    # filled fraction of a horizontal cylinder at level fraction k (0 to 1)
    h = 2 * k
    if h <= 0:
        return 0.0
    if h >= 2:
        return 1.0
    return (_m.acos(1 - h) - (1 - h) * _m.sqrt(2 * h - h * h)) / _m.pi


# cross section, centre (170, 190), radius 110, level at 30% of diameter
_cx, _cy, _r = 170, 190, 110
_k = 0.30
_ly = _cy + _r - 2 * _r * _k
_dx = _m.sqrt(_r * _r - (_ly - _cy) ** 2)
_seg = (f'<path d="M{_cx - _dx:.1f},{_ly:.1f} A{_r},{_r} 0 0 0 {_cx + _dx:.1f},{_ly:.1f} Z" fill="#d3f0f4" stroke="none"/>')

# chart area
_X0, _X1, _Y0, _Y1 = 420, 760, 300, 60


def _px(k):
    return _X0 + k * (_X1 - _X0)


def _py(v):
    return _Y0 - v * (_Y0 - _Y1)


_curve = " ".join(f"{_px(i / 50):.1f},{_py(_frac(i / 50)):.1f}" for i in range(51))
_grid = "".join(
    f'<line x1="{_px(g / 100):.0f}" y1="{_Y0}" x2="{_px(g / 100):.0f}" y2="{_Y1}" stroke="#eef1f4"/>'
    f'<line x1="{_X0}" y1="{_py(g / 100):.0f}" x2="{_X1}" y2="{_py(g / 100):.0f}" stroke="#eef1f4"/>'
    + _t(_px(g / 100), _Y0 + 18, str(g), 12, "400", "#555")
    + _t(_X0 - 8, _py(g / 100) + 4, str(g), 12, "400", "#555", "end")
    for g in range(0, 101, 25))

_diag = (
    _seg
    + f'<circle cx="{_cx}" cy="{_cy}" r="{_r}" fill="none" stroke="#495057" stroke-width="3"/>'
    + f'<line x1="{_cx - _dx:.1f}" y1="{_ly:.1f}" x2="{_cx + _dx:.1f}" y2="{_ly:.1f}" stroke="{_C}" stroke-width="2.5"/>'
    + '<defs><marker id="sh" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#c92a2a"/></marker></defs>'
    + f'<line x1="{_cx}" y1="{_cy + _r - 4}" x2="{_cx}" y2="{_ly + 4:.1f}" stroke="#c92a2a" stroke-width="2" marker-start="url(#sh)" marker-end="url(#sh)"/>'
    + _t(_cx + 12, (_cy + _r + _ly) / 2 + 5, "h", 15, "700", "#c92a2a", "start")
    + f'<line x1="{_cx - _r}" y1="{_cy}" x2="{_cx + _r}" y2="{_cy}" stroke="#adb5bd" stroke-dasharray="4,4"/>'
    + _t(_cx, 60, "Horizontal tank, end view", 13, "700", "#495057")
    + _t(_cx, 330, "Level 30% of diameter holds", 12, "400", "#555")
    + _t(_cx, 346, f"only {_frac(_k) * 100:.0f}% of the volume", 12, "400", "#555")
    # chart
    + _grid
    + f'<line x1="{_X0}" y1="{_Y0}" x2="{_X1}" y2="{_Y0}" stroke="#495057" stroke-width="1.5"/>'
    + f'<line x1="{_X0}" y1="{_Y0}" x2="{_X0}" y2="{_Y1}" stroke="#495057" stroke-width="1.5"/>'
    + f'<line x1="{_X0}" y1="{_Y0}" x2="{_X1}" y2="{_Y1}" stroke="#868e96" stroke-width="2" stroke-dasharray="7,5"/>'
    + f'<polyline points="{_curve}" fill="none" stroke="{_C}" stroke-width="3.5"/>'
    + f'<circle cx="{_px(_k):.1f}" cy="{_py(_frac(_k)):.1f}" r="5" fill="#c92a2a"/>'
    + _t(_px(0.62), _py(0.30), "Horizontal cylinder", 13, "700", _C, "start")
    + _t(_px(0.08), _py(0.62), "Vertical cylinder", 13, "700", "#868e96", "start")
    + _t(_px(0.08), _py(0.62) + 16, "(straight line)", 12, "400", "#868e96", "start")
    + _t((_X0 + _X1) / 2, 342, "Level, % of diameter or height", 13, "700", "#495057")
    + f'<text x="372" y="180" text-anchor="middle" font-size="13" font-weight="700" fill="#495057" transform="rotate(270 372 180)">Volume, % of full</text>'
)

BODY = [
    takeaways([
        "A strapping table, also called a tank capacity table, lists the volume of liquid at each measured height.",
        "In a vertical cylinder volume rises in a straight line with level. In horizontal and spherical tanks the cross section changes with height, so the relationship curves.",
        "Between rows, transmitters and DCS characterisers interpolate in straight lines, so closer rows give smaller errors.",
        "The table volume is the total observed volume. Free water, temperature and sediment corrections turn it into a standard or net volume.",
    ]),
    p("A <strong>strapping table</strong> converts the level a gauge or " + link("/level-transmitters", "level transmitter") + " measures into the volume of liquid in the tank. APG explains in its note on " + ext("https://apgsensors.com/what-is-a-tank-strapping-chart/", "tank strapping charts") + " that the name comes from measuring the tank with a steel tape, or strap, and that the table is most useful for tanks whose shape is not linear. SWME supplies the transmitters and " + link("/level-gauges", "level gauges") + " that feed these tables in tank farms across the UAE."),
    toc([("why", "Why level and volume differ"), ("formulas", "Volume formulas"), ("example", "Worked example and interpolation"),
         ("calibration", "How tanks are strapped"), ("use", "Using a strapping table"), ("volumes", "From observed to standard volume"),
         ("recal", "Recalibration"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("why", "Why Level and Volume Differ"),
    p("The " + ext("https://control.com/textbook/signal-characterization/material-volume-measurement/", "control.com textbook chapter on material volume") + " defines a strapping table as a data table correlating known volumes with measured heights. For a vertical cylinder the cross section is constant, so volume is proportional to height. For a horizontal cylinder the volume is complicated because the cross sectional area changes with height, and the same applies to a sphere."),
    svg(_diag, "Left: a horizontal tank filled to 30% of its diameter. Right: volume against level for a horizontal cylinder (curve) and a vertical cylinder (straight line), calculated from the segment formula", 360),
    h2("formulas", "Volume Formulas"),
    rows([
        ("Vertical cylinder", "V = (π × D² ÷ 4) × h, as on the " + ext("https://zentacalculator.com/engineering/vertical-tank-volume/", "vertical tank volume calculator") + "."),
        ("Horizontal cylinder", "V = L [R² cos⁻¹((R − h) ÷ R) − (R − h) √(2Rh − h²)], with h the height above the bottom, from " + ext("https://mathworld.wolfram.com/HorizontalCylindricalSegment.html", "MathWorld's horizontal cylindrical segment") + "."),
        ("Sphere", "V = π h² (3R − h) ÷ 3, from the " + ext("https://zentacalculator.com/engineering/spherical-tank-volume/", "spherical tank volume calculator") + "."),
        ("Cone bottom", "Within the cone V = π h (d² + d Ds + Ds²) ÷ 12; above it, the cone volume plus π D² (h − hc) ÷ 4. The " + ext("https://zentacalculator.com/engineering/cone-bottom-tank-volume/", "cone bottom tank calculator") + " handles the change at the joint."),
    ], "Level to volume for common shapes"),
    p("These formulas assume a perfect shape. Real tanks also have tilt and deadwood, which the calibration standards below correct for."),
    h2("example", "Worked Example and Interpolation"),
    p("Take a horizontal tank 2.0 m in diameter and 6.0 m long, with flat ends. Full, it holds π × 1.0² × 6.0 = 18.850 m³. The segment formula gives the rows below; the " + ext("https://zentacalculator.com/engineering/horizontal-tank-volume/", "horizontal tank volume calculator") + " returns the same figures and can also solve for level from volume."),
    table(["Level, m", "Volume, m³", "% of full"], [
        ["0.25", "1.360", "7.2"], ["0.50", "3.685", "19.6"], ["0.75", "6.456", "34.3"],
        ["1.00", "9.425", "50.0"], ["1.50", "15.164", "80.4"], ["2.00", "18.850", "100.0"],
    ]),
    p("The first 0.5 m of level holds 3.69 m³, while the next 0.5 m adds 5.74 m³. Now suppose the table had rows only every 0.5 m. Linear interpolation at 0.75 m would give (3.685 + 9.425) ÷ 2 = 6.555 m³, against the exact 6.456 m³: about 1.5% high. Closer rows near the bottom and top of a horizontal tank, where the curve bends most, keep that error down."),
    dyk("Emerson's engineer's guide to tank gauging says older calibration methods often state an uncertainty of 0.10% in the tank capacity table, while electro optical distance ranging has shown figures as low as 0.01% to 0.02%."),
    h2("calibration", "How Tanks Are Strapped"),
    p("Large upright tanks are calibrated to the API Manual of Petroleum Measurement Standards, Chapter 2.2. AmSpec's " + ext("https://www.amspecgroup.com/wp-content/uploads/2014/10/amspecnewtank-calibration.pdf", "summary of tank calibration methods") + " describes the main ones:"),
    rows([
        ("API 2.2A, manual strapping", "Circumferences taped at about 20% and 80% of the height of each shell ring."),
        ("API 2.2B, optical reference line", "A reference circumference on the first ring, then a trolley with a millimetre scale up the shell."),
        ("API 2.2D, internal electro optical distance ranging", "A total station at the tank centre takes radius readings on each ring."),
        ("ISO 4269, liquid calibration", "Batches of liquid are added through volumetric meters and the level recorded."),
    ], "Calibration methods"),
    p("The calculation then applies corrections. ISO 7507 Part 1 requires a liquid head correction, because tanks expand under the head of liquid they hold, and covers shell temperature, tilt up to 3% from vertical, and deadwood, meaning any fitting that adds or takes up volume."),
    h2("use", "Using a Strapping Table"),
    INFOGRAPHIC,
    p("The table can live in the field device or in the control system."),
    twocol([
        ("In the transmitter", "bi-cpu", ["Endress+Hauser Cerabar S, Deltabar S and Deltapilot S accept a linearisation table of 2 to 32 points", "Points entered by hand or semi automatically", "VEGA's VEGAMET 515 offers linear, cylindrical tank, spherical tank and user curves"]),
        ("In the DCS or tank gauging system", "bi-hdd-network", ["A characteriser block interpolates linearly between the nearest pair of points", "Typically ten to one hundred points"]),
    ]),
    p("The " + ext("https://bdih-download.endress.com/file/c68cad95c62b340c53fd8f69e97601ea/BA00274PEN_1311.pdf", "Endress+Hauser Cerabar S manual") + " describes the 32 point table. A " + link("/dp-level-measurement-in-closed-tanks", "differential pressure level transmitter") + " measures head, so density matters too; the " + ext("https://www.instrumentationblog.in/hydrostatic-pressure-formula/", "hydrostatic pressure formula") + " links head to level. Our comparison of " + link("/radar-vs-ultrasonic-level-measurement", "radar and ultrasonic level measurement") + " covers the other common inputs to a strapping table."),
    h2("volumes", "From Observed to Standard Volume"),
    p("Emerson's " + ext("https://www.emerson.com/documents/automation/-engineer-s-guide-to-tank-gauging-en-175314.pdf", "engineer's guide to tank gauging") + " sets out the chain. The tank capacity table turns level into total observed volume, TOV. Subtracting free water gives gross observed volume, GOV. GOV multiplied by the volume correction factor gives gross standard volume, GSV, at 15 °C or 60 °F, and subtracting sediment and water gives net standard volume, NSV. Floating roof tanks also need a correction for the volume the roof displaces."),
    p("The table itself also changes with shell temperature. For a carbon steel shell Emerson applies a factor of (1 + ΔT × 0.000022), so a 20 °C difference between calibration and shell temperature changes the table volume by 0.044%."),
    h2("recal", "Recalibration"),
    p("ISO 7507 Part 1 says tanks should be recalibrated as national regulations require, or whenever the calibration becomes suspect. AmSpec, quoting API, suggests total recalibration every 15 years for custody transfer tanks, 15 to 20 years for others, and a check of the bottom course, including tilt, every five years for custody transfer service. Related " + ext("https://www.instrumentationblog.in/category/process-instrumentation/level-measurement/", "level measurement articles") + " cover the instruments themselves."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Scaling a horizontal tank linearly.", "At 30% of the diameter the tank holds only about 25% of its volume."),
        ("Too few linearisation points.", "Rows every 0.5 m on a 2 m horizontal tank put the interpolated value 1.5% high at 0.75 m."),
        ("Checking the transmitter but not the table.", "Our article on " + link("/blog/level-transmitter-calibration-mistakes", "level transmitter calibration mistakes") + " covers the instrument side; the table needs its own review after tank repairs."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("Is a strapping table the same as a tank capacity table?", "Yes. Both terms describe the table of volume against measured height for one particular tank."),
        ("Why can't I use a formula instead?", "You can for an ideal shape. Real tanks have tilt and deadwood, and large tanks are calibrated to API or ISO methods that correct for them."),
        ("How many points does a transmitter need?", "It depends on the device. The Endress+Hauser Cerabar S accepts up to 32 points; DCS characterisers typically use ten to one hundred."),
    ]),
]
