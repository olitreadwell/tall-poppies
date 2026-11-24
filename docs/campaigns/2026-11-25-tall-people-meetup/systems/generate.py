#!/usr/bin/env python3
"""Generate three-page moodboards for every era, in one photo-led layout.

Colour is repaired, not rejected: if a text colour misses 4.5:1 on its
background it is nudged towards black or white until it passes.
"""

import pathlib

ROOT = pathlib.Path(__file__).parent
GOOGLE = (
    "https://fonts.googleapis.com/css2?"
    "family=Anton&family=Archivo+Black&family=Bebas+Neue&family=Fraunces:wght@400;700"
    "&family=Inter:wght@400;700&family=Oswald:wght@400;700"
    "&family=Playfair+Display:wght@400;700&family=Space+Grotesk:wght@400;700"
    "&family=Space+Mono&display=swap"
)

E = [
 dict(slug="victorian", n=1, name="Victorian playbill", year=1850,
      desc="Wood type, double rules, dense columns. The programme for an evening that actually happened.",
      pal=[("Stock","#FFFFFF"),("Ink","#0A0A0A"),("Seal","#B00020"),("Rule","#3A3A3A")],
      disp="Playfair Display", text="Inter", mono="Space Mono",
      photo="01-victorian.jpg", words=["busy","formal","printed","1850"],
      do=["Stack many sizes","Rule everything","Justify the body"],
      dont=["Use one weight","Leave air inside a block","Use a sans display"]),
 dict(slug="nouveau", n=2, name="Art Nouveau", year=1900,
      desc="Green arch, gold hairline, blush curve. Nothing straight, everything drawn by hand.",
      pal=[("Ground","#0E3B2E"),("Ink","#FFFFFF"),("Gold","#F2D06B"),("Blush","#F6C7C0")],
      disp="Fraunces", text="Inter", mono="Space Mono",
      photo="02-nouveau.jpg", words=["organic","ornate","1900","hand-drawn"],
      do=["Curve the frame","One gold hairline","Centre the type"],
      dont=["Use a grid visible","Add a third colour","Use condensed caps"]),
 dict(slug="constructivist", n=3, name="Constructivist", year=1920,
      desc="Red diagonal on black, condensed caps, no ornament. A poster that behaves like a shout.",
      pal=[("Ground","#0F0F0F"),("Ink","#FFFFFF"),("Signal","#E01B24"),("Steel","#8A8A8A")],
      disp="Anton", text="Oswald", mono="Space Mono",
      photo="03-constructivist.jpg", words=["loud","angular","1920","political"],
      do=["One diagonal","Huge condensed caps","Block the corners"],
      dont=["Round anything","Use more than two colours","Add a photo credit inline"]),
 dict(slug="bauhaus", n=4, name="Bauhaus", year=1925,
      desc="Yellow field, red circle, blue triangle. Shape carries the composition so type can stay quiet.",
      pal=[("Field","#FFD400"),("Ink","#111111"),("Red","#D62828"),("Blue","#1C4FD8")],
      disp="Archivo Black", text="Space Grotesk", mono="Space Mono",
      photo="04-bauhaus.jpg", words=["geometric","primary","playful","1925"],
      do=["Three shapes maximum","Lowercase type","Align to a quarter grid"],
      dont=["Use a gradient","Set body in caps","Add a drop shadow"]),
 dict(slug="deco", n=5, name="Art Deco", year=1927,
      desc="Gold rays on black, wide letterspacing, one emerald seal. Built for a room with a doorman.",
      pal=[("Ground","#0A0A0A"),("Ink","#FFFFFF"),("Gold","#E7C56A"),("Jade","#1FA37A")],
      disp="Playfair Display", text="Inter", mono="Space Mono",
      photo="05-deco.jpg", words=["sharp","metallic","grand","1927"],
      do=["Letterspace wide","Symmetry only","One metallic accent"],
      dont=["Use a warm shadow","Mix serif weights","Stack three lines of body"]),
 dict(slug="swiss", n=6, name="Swiss Style", year=1955,
      desc="Helvetica grid, one red bar, facts in order. The safest way to look like a real event.",
      pal=[("Ground","#FFFFFF"),("Ink","#111111"),("Signal","#E30613"),("Support","#6B6B6B")],
      disp="Archivo Black", text="Inter", mono="Space Mono",
      photo="06-swiss.jpg", words=["precise","quiet","legible","unhurried"],
      do=["Align everything left","One red rule, once","Set the date largest"],
      dont=["Centre the headline","Add a second accent","Round any corner"]),
 dict(slug="travel", n=7, name="Mid-century travel", year=1958,
      desc="Flat litho shapes in cobalt, coral and sunflower. Optimistic without a single photograph.",
      pal=[("Sky","#0B4FA8"),("Ink","#FFFFFF"),("Sun","#FFC93C"),("Coral","#FF6B4A")],
      disp="Oswald", text="Space Grotesk", mono="Space Mono",
      photo="07-travel.jpg", words=["flat","hopeful","1958","holiday"],
      do=["Layer flat shapes","Keep one horizon","Use a warm sun"],
      dont=["Add texture","Use a photo as the ground","Set body in caps"]),
 dict(slug="pop", n=8, name="Pop Art", year=1963,
      desc="Ben-Day dots, speech bubble, loud magenta. Comic grammar applied to a drinks notice.",
      pal=[("Ground","#FFFFFF"),("Ink","#000000"),("Magenta","#C4005F"),("Cyan","#00B8E6")],
      disp="Anton", text="Space Grotesk", mono="Space Mono",
      photo="08-pop.jpg", words=["comic","loud","flat","1963"],
      do=["Outline the bubble","Halftone the ground","One hard shadow"],
      dont=["Use a soft edge","Set body in comic caps","Add three accents"]),
 dict(slug="polish", n=9, name="Polish film poster", year=1965,
      desc="Burgundy and mustard, one surreal form, a serif that whispers. Built to intrigue rather than explain.",
      pal=[("Ground","#5C1A1B"),("Ink","#F5F5F0"),("Mustard","#E0A33E"),("Bark","#8C5A2B")],
      disp="Fraunces", text="Inter", mono="Space Mono",
      photo="09-polish.jpg", words=["muted","strange","1965","quiet"],
      do=["One odd shape","Small type, low",'Leave the frame mostly empty'],
      dont=["Use a straight grid","Add a second form","Explain the image"]),
 dict(slug="psychedelic", n=10, name="Psychedelic", year=1967,
      desc="Deep purple, pink and yellow blobs, type on a tilt. Fillmore ballroom energy at a smaller scale.",
      pal=[("Ground","#1B0B2E"),("Ink","#FFFFFF"),("Pink","#FF4FA3"),("Lime","#38D66B")],
      disp="Fraunces", text="Space Grotesk", mono="Space Mono",
      photo="10-psychedelic.jpg", words=["swirling","saturated","1967","trippy"],
      do=["Tilt the type","Overlap two blobs","Break the baseline"],
      dont=["Use a straight edge","Keep the palette small","Set body in caps"]),
 dict(slug="funk", n=11, name="Funk", year=1973,
      desc="Burnt orange band, gold rules, heavy slab. Album sleeve logic, cheap to print, loud on a wall.",
      pal=[("Ground","#2A1208"),("Ink","#FFFFFF"),("Orange","#FF7A1A"),("Gold","#FFC93C")],
      disp="Archivo Black", text="Oswald", mono="Space Mono",
      photo="11-funk.jpg", words=["warm","heavy","1973","soul"],
      do=["Band across the top","One gold rule","Heavy display weight"],
      dont=["Use a thin face","Cool the palette","Add a gradient"]),
 dict(slug="punk", n=12, name="Punk zine", year=1979,
      desc="Photocopy, ransom letters, no grid. Looks made by a person at 2am, which is the point.",
      pal=[("Ground","#000000"),("Ink","#FFFFFF"),("Signal","#FF1F1F"),("Paper","#D8D8D8")],
      disp="Anton", text="Space Grotesk", mono="Space Mono",
      photo="12-punk.jpg", words=["loud","handmade","scrappy","unpolished"],
      do=["Rotate each word","Cut the edges","Let it go off-grid"],
      dont=["Straighten it","Use a second typeface","Add a shadow"]),
 dict(slug="memphis", n=13, name="Memphis", year=1984,
      desc="Pastel pink, teal blocks, zigzags. The look of a design studio that refused to sit still.",
      pal=[("Ground","#FFD6E8"),("Ink","#000000"),("Teal","#00C2CB"),("Lemon","#FFE94A")],
      disp="Anton", text="Space Grotesk", mono="Space Mono",
      photo="13-memphis.jpg", words=["playful","clashing","geometric","1984"],
      do=["Rotate one element","Mix two shapes","Keep the palette tight"],
      dont=["Add a third pattern","Use a serif","Centre anything"]),
 dict(slug="corporate", n=14, name="Corporate brochure", year=1986,
      desc="Navy and teal, thin rules, a data table. Deliberately dull, which reads as trustworthy.",
      pal=[("Ground","#0B2A5B"),("Ink","#FFFFFF"),("Teal","#2BB3C0"),("Steel","#8FB8C4")],
      disp="Archivo Black", text="Inter", mono="Space Mono",
      photo="14-corporate.jpg", words=["sober","structured","1986","plain"],
      do=["Use a table","Thin rules only","Keep type small"],
      dont=["Add a photo cutout","Use a display serif","Set body in caps"]),
 dict(slug="surf", n=15, name="Surf rad", year=1991,
      desc="Hot pink, cyan sky, striped sun. Built for a phone screen and a hot afternoon.",
      pal=[("Ground","#FF2D87"),("Ink","#0A0A0A"),("Sky","#00D4FF"),("Sun","#FFE94A")],
      disp="Bebas Neue", text="Space Grotesk", mono="Space Mono",
      photo="15-surf.jpg", words=["bright","fast","summer","loud"],
      do=["Stack the words tight","Put the sun behind type","One hard shadow"],
      dont=["Soften the edges","Use pastel","Gradient behind text"]),
 dict(slug="rave", n=16, name="Rave flyer", year=1992,
      desc="Black ground, cyan and magenta, repetition, mono. Information density as the aesthetic.",
      pal=[("Ground","#000000"),("Ink","#FFFFFF"),("Cyan","#00F0FF"),("Magenta","#FF00C8")],
      disp="Anton", text="Space Mono", mono="Space Mono",
      photo="16-rave.jpg", words=["dense","late","1992","loud"],
      do=["Repeat the name","Small mono details","Two neon accents"],
      dont=["Leave white space","Use a serif","Explain the flyer"]),
 dict(slug="grunge", n=17, name="Grunge", year=1993,
      desc="Black, rust and xerox grit. Type that looks photocopied twice and stuck on a wall.",
      pal=[("Ground","#000000"),("Ink","#FFFFFF"),("Rust","#C05621"),("Ash","#7A7A7A")],
      disp="Oswald", text="Space Grotesk", mono="Space Mono",
      photo="17-grunge.jpg", words=["rough","dark","1993","worn"],
      do=["Offset the baseline","One rust accent","Let the noise show"],
      dont=["Use a clean grid","Add a third colour","Make it precious"]),
 dict(slug="y2k", n=18, name="Y2K chrome", year=1999,
      desc="Silver gradient, bubbles, pill buttons. The future as drawn on a 1999 software box.",
      pal=[("Ground","#DCE6F2"),("Ink","#1B2E4B"),("Blue","#1E3FA8"),("Silver","#8FA6C4")],
      disp="Archivo Black", text="Inter", mono="Space Mono",
      photo="18-y2k.jpg", words=["metallic","glossy","optimistic","future"],
      do=["Round the pill","Let the chrome shine","Keep one hard edge"],
      dont=["Use a flat grey","Add a serif","Stack three fonts"]),
 dict(slug="aero", n=19, name="Frutiger Aero", year=2007,
      desc="Sky gradient, gloss, bubbles, aqua. Corporate optimism with the edges sanded off.",
      pal=[("Sky","#8EDFF0"),("Ink","#0A3A4A"),("Mint","#B9F0DA"),("Deep","#3FA9B8")],
      disp="Inter", text="Inter", mono="Space Mono",
      photo="19-aero.jpg", words=["glossy","clean","2007","aqua"],
      do=["Round every corner","One gloss highlight","Soft blue palette"],
      dont=["Use a hard black","Add texture","Set type in caps"]),
 dict(slug="cyberpunk", n=20, name="Cyberpunk", year=2020,
      desc="Amber terminal on black, teal signal, scanlines. Readable at 3am from across a bar.",
      pal=[("Ground","#050505"),("Amber","#FFB000"),("Teal","#00E5C0"),("Dim","#7A5A20")],
      disp="Anton", text="Space Mono", mono="Space Mono",
      photo="20-cyberpunk.jpg", words=["nocturnal","terminal","signal","rain"],
      do=["Mono for everything","One teal accent","Keep the grid strict"],
      dont=["Add purple","Use a clean sans","Soften the black"]),
]


def lum(hex_colour):
    v = hex_colour.lstrip("#")
    ch = [int(v[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in ch]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def cr(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def to_rgb(h):
    v = h.lstrip("#")
    return [int(v[i:i + 2], 16) for i in (0, 2, 4)]


def to_hex(rgb):
    return "#%02X%02X%02X" % tuple(max(0, min(255, round(c))) for c in rgb)


def fix_pair(bg, candidates, target=4.5):
    """Return (text, background), keeping the text honest.

    The first candidate that clears target wins, so ink stays ink. If no
    candidate clears, keep the highest-contrast text and move only the panel
    a few percent towards white or black until the pair passes. The returned
    background is what the board and the swatch both use.
    """
    for fg in candidates:
        if cr(fg, bg) >= target:
            return fg, bg
    fg = max(candidates, key=lambda c: cr(c, bg))
    toward = [255, 255, 255] if lum(fg) < 0.4 else [0, 0, 0]
    rgb = to_rgb(bg)
    for step in range(1, 101):
        t = step / 100
        trial = to_hex([rgb[i] + (toward[i] - rgb[i]) * t for i in range(3)])
        if cr(fg, trial) >= target:
            return fg, trial
    return fg, to_hex(toward)


STYLE = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;font-family:'__TEXT__',sans-serif;background:__BG__;color:__INK__}
.page{width:1080px;height:1350px;position:relative;overflow:hidden;display:flex;flex-direction:column}
.top{padding:52px 64px 18px;background:__BG__}
.tag{font-family:'__MONO__',monospace;font-size:19px;letter-spacing:.22em;text-transform:uppercase;color:__TAG__}
h1{font-family:'__DISP__',sans-serif;font-size:142px;line-height:.82;letter-spacing:-.03em;margin-top:16px}
h2{font-family:'__DISP__',sans-serif;font-size:60px;line-height:.94}
.heroimg{flex:1;min-height:0;overflow:hidden}
.heroimg img{width:100%;height:100%;object-fit:cover;display:block}
.mid{padding:22px 64px 0;background:__BG__}
p.lede{font-size:26px;line-height:1.4;max-width:700px}
.words{display:flex;gap:10px;flex-wrap:wrap;margin-top:20px}
.words span{font-family:'__MONO__',monospace;font-size:17px;border:2px solid __INK__;padding:7px 12px;letter-spacing:.1em;text-transform:uppercase}
.sw{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;padding:20px 64px 62px;background:__BG__}
.sw i{display:block;height:96px;border:2px solid __INK__}
.sw b{display:block;font-family:'__MONO__',monospace;font-size:15px;margin-top:6px}
.sw u{display:block;font-family:'__MONO__',monospace;font-size:13px;text-decoration:none}
.foot{position:absolute;left:64px;right:64px;bottom:26px;display:flex;justify-content:space-between;font-family:'__MONO__',monospace;font-size:14px;letter-spacing:.1em}
.coltitle{padding:56px 64px 18px}
.collage{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:0 64px}
.collage img{width:100%;height:230px;object-fit:cover;display:block}
.rows{flex:1;display:flex;flex-direction:column;justify-content:space-evenly;padding:0 64px 76px}
.frame{border:3px solid __INK__;position:relative;overflow:hidden}
.fb{height:300px;background:__ACC__;color:__ONACC__}
.ig{height:300px;background:__BG2__;color:__ONBG2__}
.st{height:170px;background:__BG__;color:__INK__;display:flex;align-items:center;padding:0 26px;font-family:'__MONO__',monospace;font-size:19px;letter-spacing:.14em}
.frame .t{position:absolute;left:24px;top:20px;font-family:'__DISP__',sans-serif;font-size:52px;line-height:.88;text-transform:uppercase}
.frame .b{position:absolute;left:24px;bottom:18px;font-family:'__MONO__',monospace;font-size:16px;letter-spacing:.1em}
"""

DOC = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{google}" rel="stylesheet">
<style>{style}</style></head><body>{body}</body></html>"""


def theme(e):
    labels = [p[0] for p in e["pal"]]
    bg, ink, acc, bg2 = (p[1] for p in e["pal"])
    ink, bg = fix_pair(bg, [ink, "#111111", "#FFFFFF"])
    on_acc, acc = fix_pair(acc, [ink, "#FFFFFF", "#000000"])
    on_bg2, bg2 = fix_pair(bg2, [ink, "#FFFFFF", "#000000"])
    pal = [(labels[0], bg), (labels[1], ink), (labels[2], acc), (labels[3], bg2)]
    tag = acc
    if cr(tag, bg) < 4.5:
        if cr(ink, bg) >= 4.5:
            tag = ink
        else:
            toward = [0, 0, 0] if cr("#000000", bg) >= cr("#FFFFFF", bg) else [255, 255, 255]
            src = to_rgb(acc)
            for step in range(1, 101):
                trial = to_hex([src[i] + (toward[i] - src[i]) * step / 100 for i in range(3)])
                if cr(trial, bg) >= 4.5:
                    tag = trial
                    break
    return dict(BG=bg, INK=ink, ACC=acc, BG2=bg2, TAG=tag,
                ONACC=on_acc, ONBG2=on_bg2, PAL=pal,
                DISP=e["disp"], TEXT=e["text"], MONO=e["mono"])


def style(t):
    s = STYLE
    for k in ("BG", "INK", "ACC", "BG2", "TAG", "ONACC", "ONBG2", "DISP", "TEXT", "MONO"):
        s = s.replace("__%s__" % k, t[k])
    return s


def page(t, n, body):
    foot = ('<div class="foot"><span>Tall People Meetup Wellington</span>'
            f'<span>Page {n} of 3</span></div>')
    return DOC.format(google=GOOGLE, style=style(t), body=f'<div class="page">{body}{foot}</div>')


def boards(e, t):
    words = "".join(f"<span>{w}</span>" for w in e["words"])
    sw = "".join(f'<div><i style="background:{h}"></i><b>{n}</b><u>{h}</u></div>'
                 for n, h in t["PAL"])
    p1 = (f'<div class="top"><div class="tag">{e["n"]:02d} / {e["year"]}</div>'
          f'<h1>{e["name"]}</h1></div>'
          f'<div class="heroimg"><img src="../../photos/{e["photo"]}" alt=""></div>'
          f'<div class="mid"><p class="lede">{e["desc"]}</p><div class="words">{words}</div></div>'
          f'<div class="sw">{sw}</div>')
    p2 = (f'<div class="coltitle"><div class="tag">Page 2 / Images, type, rules</div>'
          f'<h2>Four crops, one idea</h2></div><div class="collage">' +
          "".join(f'<div style="overflow:hidden;border:3px solid {t["INK"]}">'
                  f'<img src="../../photos/{e["photo"]}" style="object-position:{pos}" alt=""></div>'
                  for pos in ["20% 20%", "80% 30%", "30% 80%", "70% 70%"]) +
          f'</div><div class="sw" style="margin-top:36px">{sw}</div>'
          f'<div style="padding:18px 64px 0;font-family:\'{e["mono"]}\',monospace;font-size:17px">'
          f'{e["disp"]} / {e["text"]} / {e["mono"]}</div>')
    p3 = ('<div class="coltitle"><div class="tag">Page 3 / Applied</div><h2>Three surfaces</h2></div>'
          '<div class="rows">'
          '<div class="frame fb"><div class="t">Tall<br>People<br>Meetup</div>'
          '<div class="b">5PM TO 8PM / ROSIE\u2019S</div></div>'
          '<div class="frame ig"><div class="t">25<br>NOV</div>'
          '<div class="b">ALL WELCOME / 4 QUEENS WHARF</div></div>'
          '<div class="frame st">NO CHARGE - JUST TURN UP - ALL WELCOME</div>'
          '</div>')
    return [page(t, 1, p1), page(t, 2, p2), page(t, 3, p3)]


for e in E:
    t = theme(e)
    d = ROOT / e["slug"]
    d.mkdir(parents=True, exist_ok=True)
    for i, html in enumerate(boards(e, t), 1):
        (d / f"board-{i}.html").write_text(html)
    print(e["slug"], "on-accent", t["ONACC"], "on-support", t["ONBG2"])
