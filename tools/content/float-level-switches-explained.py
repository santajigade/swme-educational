META = {
    "category": "level-measurement-guides",
    "title": "Float Level Switches: How They Work",
    "keyword": "float level switch",
    "subtitle": "How a float, a magnet and a reed contact turn a liquid level into a switch signal, how vertical and side mounted switches differ, and what stops a float switch working",
    "meta_title": "Float Level Switches: How They Work",
    "meta_description": "How a float level switch works: float, magnet and reed contact, normally open or closed, vertical and side mounting, hysteresis for pumps, and buildup risks.",
    "summary": "How a float level switch uses a magnet and a reed contact to switch at a set level, how to choose the contact and mounting, and what makes floats stick.",
    "card_title": "Float Level Switches",
    "author": "SWME Technical Staff",
    "published": "2026-11-25",
    "status": "published",
    "sort_order": 9,
    "thumbnail": "thumbnail.webp",
    "infographic": {
        "layout": "levels",
        "title": "Two Stage Float Switch on a Sump",
        "alt": "Infographic of a two stage float switch on a sump: the pump starts at the first stage, the second stage alarms or shuts off the source, and the pump stops at a lower point",
        "top_label": "High",
        "bottom_label": "Low",
        "levels": [
            ["Second stage", "If the level keeps rising, it shuts off the source or raises an alarm.", 0.88],
            ["First stage: pump on", "The switch energises the pump.", 0.6],
            ["Pump off", "The shut off point can sit much lower than the turn on point, so the pump cycles less.", 0.2],
        ],
    },
}

_C = "#0c8599"
_T = "#0a5f6d"


def _t(x, y, s, size=13, w="700", fill=_T, anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


_diag = (
    # tank with liquid
    '<rect x="60" y="70" width="300" height="270" fill="none" stroke="#495057" stroke-width="3"/>'
    + '<rect x="62" y="170" width="296" height="168" fill="#d3f0f4"/>'
    + '<line x1="62" y1="170" x2="358" y2="170" stroke="' + _C + '" stroke-width="2"/>'
    + _t(110, 192, "Liquid", 13, "700", _T)
    # mounting plug and stem
    + '<rect x="185" y="52" width="50" height="20" fill="#868e96"/>'
    + '<rect x="203" y="72" width="14" height="240" fill="#e9ecef" stroke="#495057" stroke-width="1.5"/>'
    # reed switch inside stem
    + '<rect x="207" y="150" width="6" height="40" fill="#ffd43b" stroke="#a35400"/>'
    # collars (stops)
    + '<rect x="196" y="128" width="28" height="7" fill="#495057"/>'
    + '<rect x="196" y="212" width="28" height="7" fill="#495057"/>'
    # float with magnet ring
    + '<rect x="176" y="152" width="68" height="36" rx="10" fill="' + _C + '" opacity="0.9"/>'
    + '<rect x="196" y="164" width="28" height="12" fill="#c92a2a"/>'
    # labels
    + '<line x1="244" y1="170" x2="380" y2="196" stroke="#495057"/>' + _t(386, 200, "Float with magnet", 13, "700", "#495057", "start")
    + '<line x1="213" y1="150" x2="380" y2="140" stroke="#495057"/>' + _t(386, 144, "Reed contact in the stem", 13, "700", "#495057", "start")
    + '<line x1="224" y1="131" x2="380" y2="80" stroke="#495057"/>' + _t(386, 84, "Adjusting collar limits travel", 13, "700", "#495057", "start")
    + '<line x1="217" y1="250" x2="380" y2="250" stroke="#495057"/>' + _t(386, 254, "Guide tube (stem)", 13, "700", "#495057", "start")
    # reed detail panels
    + '<rect x="560" y="170" width="200" height="70" rx="8" fill="#f8f9fa" stroke="#adb5bd"/>'
    + _t(660, 162, "Float away: contacts open", 12, "700", "#495057")
    + '<rect x="580" y="195" width="160" height="22" rx="11" fill="none" stroke="#74c0fc" stroke-width="2"/>'
    + '<line x1="590" y1="206" x2="655" y2="203" stroke="#495057" stroke-width="3"/>'
    + '<line x1="730" y1="206" x2="665" y2="209" stroke="#495057" stroke-width="3"/>'
    + '<rect x="560" y="270" width="200" height="70" rx="8" fill="#f8f9fa" stroke="#adb5bd"/>'
    + _t(660, 262, "Magnet alongside: contacts close", 12, "700", "#495057")
    + '<rect x="580" y="295" width="160" height="22" rx="11" fill="none" stroke="#74c0fc" stroke-width="2"/>'
    + '<line x1="590" y1="306" x2="664" y2="306" stroke="#495057" stroke-width="3"/>'
    + '<line x1="730" y1="306" x2="656" y2="306" stroke="#495057" stroke-width="3"/>'
    + '<rect x="630" y="322" width="60" height="12" fill="#c92a2a"/>'
    + _t(660, 360, "Normally open reed contact", 12, "400", "#555")
)

BODY = [
    takeaways([
        "A float level switch has a hollow float with a magnet that slides on a guide tube; a reed contact inside the tube switches when the magnet passes it.",
        "Contacts are normally open or normally closed, and on a stem switch you reverse the action by moving the float stops.",
        "Float switches can have a lot of hysteresis, which keeps a pump from cycling.",
        "Dirt, deposits, foam and turbulence are the usual reasons a float stops moving freely.",
    ]),
    p("A <strong>float level switch</strong> is one of the simplest ways to know that a tank has reached a set level. It gives an on/off signal that can start or stop a pump, raise an alarm or open and close a valve. SWME supplies float and other " + link("/level-switches", "level switches") + " for tanks and sumps across the UAE."),
    toc([("work", "How a float level switch works"), ("contacts", "Normally open or normally closed"), ("mounting", "Vertical and side mounted switches"),
         ("pumps", "Pump control and hysteresis"), ("limits", "What stops a float working"), ("select", "Selection checklist"), ("mistakes", "Common mistakes"), ("faq", "FAQ")]),
    h2("work", "How a Float Level Switch Works"),
    p("WIKA's explanation of " + ext("https://blog.wika.com/en/products/level-products/what-is-a-float-switch-and-how-does-it-actually-work/", "how a float switch works") + " starts with buoyancy: a hollow float of low density rises and falls with the level. In a modern electric switch the float carries a magnet and slides on a guide tube, adjusting collars limit how far it travels, and a reed contact sits inside the tube.",
      "In addition, APG describes the reed switch as two ferromagnetic contact tips sealed in a glass tube, inside a stem of plastic, brass or stainless steel. The strongest part of the magnet's field, the centre lobe, is what closes the reeds. APG's article on " + ext("https://apgsensors.com/magnetic-fields-and-a-liquid-level-switch", "magnetic fields in a liquid level switch") + " adds that float stops are what make a stem switch repeatable."),
    svg(_diag, "Vertical stem float switch: the float magnet closes the reed contact inside the stem when the float reaches the switch point (not to scale)", 375),
    rows([
        ("Float", "Hollow and buoyant, with a built in magnet."),
        ("Guide tube", "The stem the float slides on. The reed contact sits inside it, sealed from the liquid."),
        ("Adjusting collars", "Stops above and below the float that limit its travel."),
        ("Reed contact", "Changes state when the magnet comes alongside."),
    ], "Parts of a stem float switch (WIKA)"),
    h2("contacts", "Normally Open or Normally Closed"),
    p("WIKA explains that a normally open reed contact closes when a magnetic field is applied and a normally closed one opens. A change over contact has three contact leaves, so it gives a normally closed and a normally open contact at the same time. The leaves are preloaded, so the contact only changes state while the field is present.",
      "APG says you order the switch normally open or normally closed. On a stem switch you can reverse the state by moving the float stops: moving the float up makes a normally open switch act normally closed, and the other way round."),
    dyk("APG found that the outer lobes of the magnet's field can also move the reeds, but only so far: the furthest they have moved a float to use the second outer lobe is about 1/2 an inch."),
    h2("mounting", "Vertical and Side Mounted Switches"),
    p("Gems notes in its " + ext("https://www.gemssensors.com/blog/blog-details/float-switch-work", "float level switch guide") + " that mounting makes a big difference to how the switch works. Vertical switches are set to switch at specific levels. Gems builds single point units, multipoint units with up to seven levels, and continuous float transmitters."),
    twocol([
        ("Vertical (top mounted)", "bi-arrow-down-up", [
            "Enters through the tank roof.",
            "Can carry more than one float for several set points.",
            "Float stops on the stem fix each switch point.",
        ]),
        ("Side mounted (horizontal)", "bi-arrow-left-right", [
            "Fits through the tank wall at the switch level.",
            "The magnet is guided directly to the reed switch (APG).",
            "Bellows sealed and magnet actuated versions are used on boilers.",
        ]),
    ]),
    p("For an overview of the other technologies, read our guide to " + link("/level-switch-types", "level switch types") + ". If you need a reading rather than a switch point, compare " + link("/point-level-vs-continuous-level-measurement", "point and continuous level measurement") + " or look at our " + link("/level-transmitters", "level transmitters") + ". A magnetic float is also the heart of " + link("/how-a-magnetic-level-gauge-works", "a magnetic level gauge") + "."),
    h2("pumps", "Pump Control and Hysteresis"),
    INFOGRAPHIC,
    p("Sump and condensate pumps are a common job for a float level switch. For example, the " + ext("https://en.wikipedia.org/wiki/Float_switch", "float switch article on Wikipedia") + " describes a switch that runs the pump until the level is substantially reduced, and a two stage switch whose second stage shuts off the source or triggers an alarm if the level keeps rising. Float switches can include substantial hysteresis: the turn on point may be much higher than the shut off point, which reduces pump cycling.",
      "The same article lists the float type low water cutoff, which shuts down a gas or oil burner when the boiler level falls. Our article on " + link("/blog/pump-protection-pressure-flow-temperature-instruments", "instruments for pump protection") + " shows where a level switch fits with pressure, flow and temperature protection."),
    h2("limits", "What Stops a Float Working"),
    p("A float needs to move freely. Wikipedia notes that dirt on the float impedes its motion, debris and foam can interfere, and a stilling well helps against turbulence and debris. Gems warns that deposits such as lime or calcium can build up until the switch fails. Buoyancy depends on the liquid density and the size and density of the float, so check density, viscosity and temperature when you size one. Picking the right float density even lets a float sink in one liquid and float on another, such as oil and water."),
    table(["Float material", "Typical use (Wikipedia)"], [
        ["316 stainless steel", "High temperature, corrosion or pressure"],
        ["Buna Nitrile", "Oil, petroleum, lubrication and hydraulics"],
        ["Polypropylene", "Extreme pH and lower temperatures, often food"],
        ["Kynar", "Harsh chemicals, also food"],
    ]),
    h2("select", "Selection Checklist"),
    checklist([
        ("Define the job", "High or low alarm, pump start and stop, or a burner low water cutoff."),
        ("Choose the contact", "Normally open, normally closed or change over, for the action you need on loss of signal."),
        ("Choose the mounting", "Vertical for one or more set points from the roof, side mounted at a single level."),
        ("Check the liquid", "Density, viscosity and temperature set the float size, and chemistry sets the material."),
        ("Plan for dirt", "Use a stilling well where the surface is turbulent or carries debris, and schedule cleaning where deposits form."),
    ]),
    p("Level switches often share a tank with " + link("/level-gauges", "level gauges") + " for local reading. More background is in these " + ext("https://www.instrumentationblog.in/category/process-instrumentation/level-measurement/", "level measurement articles") + "."),
    h2("mistakes", "Common Mistakes to Avoid"),
    mistakes([
        ("Ordering the wrong contact state.", "Decide normally open or closed before ordering, or plan to move the float stops."),
        ("Installing in a turbulent inlet zone.", "Waves and debris move the float; a stilling well calms the surface."),
        ("Ignoring deposits.", "Lime and calcium buildup can stop the float and the switch fails to act."),
    ]),
    h2("faq", "Frequently Asked Questions"),
    faq([
        ("What is inside a float level switch?", "A float with a magnet, a guide tube, collars that limit float travel, and a reed contact sealed inside the tube."),
        ("Can I change a float switch from normally open to normally closed?", "On a stem switch, yes, by moving the float stops so the float works the other way up."),
        ("Why does my float switch not reset?", "Usually the float is stuck by dirt, deposits or foam. Clean it and check that it moves freely."),
    ]),
]
