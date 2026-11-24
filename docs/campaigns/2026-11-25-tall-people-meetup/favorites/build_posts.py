#!/usr/bin/env python3
"""Write twelve editable social posts, three per shortlisted style."""

import pathlib

ROOT = pathlib.Path(__file__).parent
POSTS = ROOT / "posts"
GOOGLE = (
    "https://fonts.googleapis.com/css2?"
    "family=Bebas+Neue&family=Space+Grotesk:wght@400;700"
    "&family=Orbitron:wght@400;700;900&family=Michroma"
    "&family=Bangers&family=Archivo+Black&family=Jost:wght@400;600;800"
    "&family=Space+Mono&display=swap"
)

BASE = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:#222}
body{display:flex;justify-content:center}
.post{width:1080px;overflow:hidden;position:relative;background:#fff}
.post.feed{height:1350px}
.post.story{height:1920px}
img{display:block}
.kicker{font-family:'Space Mono',monospace;letter-spacing:.18em;text-transform:uppercase}
"""


def doc(title, css, body):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{GOOGLE}" rel="stylesheet">
<style>{BASE}{css}</style></head><body>{body}</body></html>"""


SURF_CSS = """
.surf{font-family:'Space Grotesk',sans-serif;color:#0A0A0A}
.surf h1,.surf h2{font-family:'Bebas Neue',sans-serif;font-weight:400;line-height:.84;letter-spacing:-.01em}
.surf .pink{background:#FF2D87}
.surf .cyan{background:#00D4FF}
.surf .yellow{background:#FFE94A}
.surf .black{background:#0A0A0A;color:#fff}
.s1 .photo{height:610px;overflow:hidden}
.s1 .photo img{width:100%;height:100%;object-fit:cover}
.s1 .pink{padding:36px 64px 30px}
.s1 .kicker{font-size:16px;margin-bottom:12px}
.s1 h1{font-size:112px;max-width:900px}
.s1 .details{display:grid;grid-template-columns:1fr 1fr;gap:4px 28px;margin-top:26px;font-size:22px;font-weight:700}
.s1 .black{height:92px;display:flex;align-items:center;justify-content:center;font-family:'Space Mono',monospace;font-size:22px;letter-spacing:.14em}
.s1 .sun{position:absolute;right:38px;top:560px;width:150px;height:150px;border:6px solid #0A0A0A;border-radius:50%}
.s2{background:#FF2D87}
.s2 .top{height:880px;position:relative;padding:54px 64px;display:flex;flex-direction:column;justify-content:space-between}
.s2 .kicker{font-size:19px}
.s2 .sun{position:absolute;left:50%;top:90px;width:720px;height:720px;transform:translateX(-50%)}
.s2 h1{position:relative;z-index:2;font-size:250px;line-height:.8;text-align:center;margin-top:250px}
.s2 .date{position:relative;z-index:2;font-family:'Space Mono',monospace;font-size:30px;letter-spacing:.12em;text-align:center;margin-top:8px}
.s2 .cyan{height:290px;padding:40px 64px;display:flex;flex-direction:column;justify-content:space-between}
.s2 h2{font-size:70px;line-height:.92}
.s2 .cyan p{font-size:24px;font-weight:700;letter-spacing:.04em}
.s2 .black{height:180px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;font-family:'Space Mono',monospace;font-size:28px;letter-spacing:.14em}
.s2 .tag{background:#FFE94A;color:#0A0A0A;padding:8px 16px;font-size:17px}
.s3 .hero{height:880px;overflow:hidden}
.s3 .hero img{width:100%;height:100%;object-fit:cover}
.s3 .pink{height:760px;padding:44px 64px;position:relative}
.s3 .kicker{font-size:18px}
.s3 h1{font-size:210px;line-height:.82;margin-top:12px}
.s3 h2{font-size:96px;margin-top:2px}
.s3 p{font-size:26px;font-weight:700;margin-top:18px}
.s3 .sun{position:absolute;right:54px;bottom:58px;width:190px;height:190px}
.s3 .yellow{height:280px;display:flex;align-items:center;justify-content:center;font-family:'Bebas Neue',sans-serif;font-size:112px;letter-spacing:.02em}
"""

Y2K_CSS = """
.y2k{font-family:'Space Grotesk',sans-serif;color:#1B2E4B;background:#DCE6F2}
.y2k h1,.y2k h2{font-family:'Orbitron',sans-serif;font-weight:900;line-height:.95;letter-spacing:-.03em}
.y2k .mono{font-family:'Michroma',sans-serif;letter-spacing:.12em;text-transform:uppercase}
.y1 .ramp{height:220px;overflow:hidden}
.y1 .ramp img{width:100%;height:100%;object-fit:cover}
.y1 .body{padding:38px 64px 0}
.y1 .pill{display:inline-block;background:#1B2E4B;color:#fff;border-radius:999px;padding:16px 30px;font-family:'Michroma',sans-serif;font-size:20px;letter-spacing:.1em}
.y1 h1{font-size:112px;margin-top:28px}
.y1 .photo{height:430px;margin-top:28px;border:8px solid #1B2E4B;border-radius:34px;overflow:hidden;position:relative}
.y1 .photo img{width:100%;height:100%;object-fit:cover}
.y1 .star{position:absolute;width:120px;right:48px;top:330px}
.y1 .details{margin-top:26px;display:grid;grid-template-columns:1fr 1fr;gap:6px 24px;font-size:23px;font-weight:700}
.y1 .welcome{margin-top:24px;background:#1E3FA8;color:#fff;border-radius:999px;text-align:center;padding:18px;font-family:'Orbitron',sans-serif;font-size:26px;letter-spacing:.16em}
.y2{background:#1B2E4B;color:#DCE6F2}
.y2 .top{padding:54px 64px 0;display:flex;justify-content:space-between;align-items:flex-start}
.y2 .kicker{font-size:17px}
.y2 .big{background:linear-gradient(180deg,#fff 0%,#DCE6F2 34%,#8FA6C4 60%,#1B2E4B 100%);color:#1B2E4B;border:8px solid #DCE6F2;border-radius:48px;margin:34px 64px 0;padding:42px 42px 34px}
.y2 .big h1{font-size:92px}
.y2 .big p{font-family:'Michroma',sans-serif;font-size:20px;margin-top:16px;letter-spacing:.08em}
.y2 .photo{height:470px;margin:34px 64px 0;border-radius:200px 200px 34px 34px;overflow:hidden;border:8px solid #DCE6F2}
.y2 .photo img{width:100%;height:100%;object-fit:cover}
.y2 .bottom{padding:30px 64px 0;display:flex;justify-content:space-between;align-items:center}
.y2 .details{font-size:22px;font-weight:700;line-height:1.5}
.y2 .welcome{background:#fff;color:#1B2E4B;border-radius:999px;padding:14px 24px;font-family:'Orbitron',sans-serif;font-size:18px;letter-spacing:.12em}
.y3{background:linear-gradient(180deg,#FFFFFF 0%,#DCE6F2 44%,#8FA6C4 72%,#1E3FA8 100%);color:#1B2E4B}
.y3 .header{padding:54px 64px 0;text-align:center}
.y3 .kicker{font-size:18px}
.y3 h1{font-size:280px;line-height:.82;margin-top:26px;color:#1B2E4B}
.y3 .month{font-family:'Michroma',sans-serif;font-size:54px;letter-spacing:.3em;margin-top:10px}
.y3 .bubble{position:absolute;width:250px;right:30px;top:80px}
.y3 .star{position:absolute;width:120px;left:40px;top:520px}
.y3 .photo{position:absolute;left:64px;right:64px;top:920px;height:560px;border-radius:280px 280px 42px 42px;overflow:hidden;border:10px solid #fff}
.y3 .photo img{width:100%;height:100%;object-fit:cover}
.y3 .info{position:absolute;left:64px;right:64px;top:1520px;text-align:center}
.y3 .info h2{font-size:64px}
.y3 .info p{font-size:24px;font-weight:700;margin-top:10px}
.y3 .welcome{position:absolute;left:64px;right:64px;bottom:66px;background:#1B2E4B;color:#fff;border-radius:999px;text-align:center;padding:22px;font-family:'Orbitron',sans-serif;font-size:24px;letter-spacing:.14em}
"""

POP_CSS = """
.pop{font-family:'Space Grotesk',sans-serif;color:#000;background:#fff}
.pop h1,.pop h2{font-family:'Bangers',sans-serif;font-weight:400;letter-spacing:.02em;line-height:.9}
.pop .heavy{font-family:'Archivo Black',sans-serif}
.p1{background:#fff url('../../patterns/pop-art/halftone.svg');background-size:220px}
.p1 .panel{margin:54px 54px 0;border:10px solid #000;height:620px;overflow:hidden}
.p1 .panel img{width:100%;height:100%;object-fit:cover}
.p1 .bubble{position:absolute;left:70px;top:520px;width:760px}
.p1 .bubble span{position:absolute;left:82px;right:82px;top:70px;font-family:'Bangers',sans-serif;font-size:74px;line-height:.94;text-align:center}
.p1 .details{position:absolute;left:54px;right:54px;top:970px;background:#000;color:#fff;padding:28px 34px}
.p1 .details div:first-child{font-size:28px;font-weight:700;letter-spacing:.04em}
.p1 .details div:last-child{font-size:18px;font-family:'Space Mono',monospace;margin-top:10px;letter-spacing:.08em}
.p1 .burst{position:absolute;right:40px;bottom:38px;width:210px;height:210px}
.p1 .burst span{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-family:'Bangers',sans-serif;font-size:46px;transform:rotate(-8deg)}
.p2{background:#C4005F url('../../patterns/pop-art/halftone.svg');background-size:180px}
.p2 .top{padding:44px 64px 0;text-align:center}
.p2 .kicker{color:#fff;font-size:18px}
.p2 .burst{position:relative;width:720px;height:720px;margin:16px auto 0}
.p2 .burst img{width:100%;height:100%}
.p2 .burst h1{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center;font-size:100px;padding:120px;color:#000;transform:rotate(-5deg)}
.p2 .cyan{background:#00B8E6;border:10px solid #000;margin:0 54px;padding:28px 34px;text-align:center}
.p2 .cyan h2{font-size:74px;line-height:.92}
.p2 .details{background:#fff;border:10px solid #000;margin:20px 54px 0;padding:22px 32px;font-size:22px;font-weight:700;display:grid;grid-template-columns:1fr 1fr;gap:6px 20px}
.p2 .welcome{position:absolute;left:0;right:0;bottom:0;height:92px;background:#000;color:#FFE94A;display:flex;align-items:center;justify-content:center;font-family:'Bangers',sans-serif;font-size:50px;letter-spacing:.08em}
.p3{background:#fff;padding:26px}
.p3 .strip{height:1868px;border:10px solid #000;display:grid;grid-template-rows:1fr 1fr 1fr}
.p3 .cell{border-bottom:10px solid #000;position:relative;overflow:hidden;background:#fff}
.p3 .cell:last-child{border-bottom:0}
.p3 .photo img{width:100%;height:100%;object-fit:cover}
.p3 .cell2{background:#C4005F url('../../patterns/pop-art/halftone.svg');background-size:160px;display:flex;align-items:center;justify-content:center}
.p3 .bubblebox{position:relative;width:760px}
.p3 .bubblebox img{width:100%}
.p3 .bubblebox span{position:absolute;left:82px;right:82px;top:64px;font-family:'Bangers',sans-serif;font-size:92px;line-height:.9;text-align:center;color:#000}
.p3 .cell3{background:#FFE94A;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.p3 .cell3 h2{font-size:160px;line-height:.85}
.p3 .cell3 p{font-family:'Archivo Black',sans-serif;font-size:30px;margin-top:16px}
.p3 .meta{position:absolute;left:20px;right:20px;bottom:20px;display:flex;justify-content:space-between;font-family:'Space Mono',monospace;font-size:16px}
"""

BAUHAUS_CSS = """
.bau{font-family:'Jost',sans-serif;color:#111;background:#FFD400}
.bau h1,.bau h2{font-family:'Archivo Black',sans-serif;font-weight:400;line-height:.88;letter-spacing:-.03em}
.b1{background:#FFD400}
.b1 .top{padding:54px 64px 0}
.b1 .kicker{font-size:18px;letter-spacing:.16em}
.b1 h1{font-size:140px;margin-top:24px}
.b1 .shapes{position:absolute;top:480px;left:0;width:1080px;height:360px}
.b1 .circle{position:absolute;left:72px;top:0;width:300px;height:300px;border-radius:50%;background:#D62828}
.b1 .tri{position:absolute;right:0;top:20px;width:0;height:0;border-left:250px solid transparent;border-right:250px solid transparent;border-bottom:340px solid #1C4FD8}
.b1 .bar{position:absolute;left:400px;top:120px;width:300px;height:54px;background:#111}
.b1 .details{position:absolute;left:64px;right:64px;top:900px;display:grid;grid-template-columns:1fr 1fr;gap:8px 30px;font-size:24px;font-weight:600}
.b1 .photo{position:absolute;left:64px;right:64px;top:1010px;height:250px;border:10px solid #111;overflow:hidden}
.b1 .photo img{width:100%;height:100%;object-fit:cover}
.b1 .welcome{position:absolute;left:0;right:0;bottom:0;height:90px;background:#111;color:#fff;display:flex;align-items:center;justify-content:center;font-size:28px;letter-spacing:.18em}
.b2{background:#111;color:#fff}
.b2 .top{height:820px;position:relative;padding:54px 64px}
.b2 .kicker{font-size:18px;letter-spacing:.16em}
.b2 h1{font-size:250px;line-height:.8;margin-top:20px}
.b2 .circle{position:absolute;right:-100px;top:120px;width:420px;height:420px;border-radius:50%;background:#D62828}
.b2 .arch{position:absolute;left:64px;bottom:0;width:300px;height:380px;border-radius:150px 150px 0 0;background:#FFD400}
.b2 .blue{position:absolute;right:64px;bottom:40px;width:360px;height:150px;background:#1C4FD8}
.b2 .details{position:absolute;left:64px;right:64px;top:900px;display:grid;grid-template-columns:1fr 1fr;gap:8px 30px;font-size:24px;font-weight:600}
.b2 .welcome{position:absolute;left:64px;right:64px;bottom:70px;background:#FFD400;color:#111;padding:24px 30px;font-family:'Archivo Black',sans-serif;font-size:52px;text-align:center;letter-spacing:.02em}
.b3{background:#fff}
.b3 .top{height:760px;background:#FFD400;position:relative;padding:54px 64px}
.b3 .kicker{font-size:18px;letter-spacing:.16em}
.b3 h1{font-size:200px;line-height:.82;margin-top:24px}
.b3 .circle{position:absolute;right:-80px;bottom:-120px;width:440px;height:440px;border-radius:50%;background:#D62828}
.b3 .mid{height:620px;background:#111;color:#fff;padding:54px 64px;position:relative}
.b3 .mid h2{font-size:180px;line-height:.82}
.b3 .mid p{font-size:28px;font-weight:600;margin-top:20px;letter-spacing:.06em}
.b3 .tri{position:absolute;right:0;bottom:0;width:0;height:0;border-left:230px solid transparent;border-right:230px solid transparent;border-bottom:320px solid #1C4FD8}
.b3 .bottom{height:540px;background:#1C4FD8;color:#fff;padding:54px 64px;position:relative}
.b3 .bottom h2{font-size:150px;line-height:.84}
.b3 .bottom p{font-size:26px;font-weight:600;margin-top:14px;letter-spacing:.08em}
.b3 .photo{position:absolute;right:64px;bottom:54px;width:360px;height:250px;border:10px solid #fff;overflow:hidden}
.b3 .photo img{width:100%;height:100%;object-fit:cover}
"""


def post(style, name, kind, css, body):
    folder = POSTS / style
    folder.mkdir(parents=True, exist_ok=True)
    html = doc(name, css, body)
    (folder / f"{name}.html").write_text(html)


def build_surf():
    css = SURF_CSS
    post("surf-rad", "01-launch", "feed", css, """
<div class="post feed surf s1">
  <div class="photo"><img src="../../photos/surf-cc0.jpg" alt=""></div>
  <img class="sun" src="../../patterns/surf-rad/sun-stripes.svg" alt="">
  <div class="pink">
    <div class="kicker">Tall People Meetup Wellington</div>
    <h1>NOT THE<br>TALLEST<br>IN THE ROOM</h1>
    <div class="details"><div>WED 25 NOV</div><div>5PM TO 8PM</div><div>ROSIE'S RED-HOT CANTINA</div><div>4 QUEENS WHARF</div></div>
  </div>
  <div class="black">ALL WELCOME / BRING A MATE</div>
</div>""")
    post("surf-rad", "02-date", "feed", css, """
<div class="post feed surf s2">
  <div class="top">
    <div class="kicker">Wellington / first meetup</div>
    <img class="sun" src="../../patterns/surf-rad/sun-stripes.svg" alt="">
    <h1>25 NOV</h1>
    <div class="date">5PM TO 8PM</div>
  </div>
  <div class="cyan"><h2>ROSIE'S RED-HOT CANTINA</h2><p>4 QUEENS WHARF / WELLINGTON</p></div>
  <div class="black"><span class="tag">DRINK PRIZE TO THE TALLEST PERSON</span><span>ALL WELCOME</span></div>
</div>""")
    post("surf-rad", "03-story", "story", css, """
<div class="post story surf s3">
  <div class="hero"><img src="../../photos/surf-cc0.jpg" alt=""></div>
  <div class="pink"><div class="kicker">Tall People Meetup Wellington</div><h1>5 TO 8</h1><h2>ROSIE'S</h2><p>WED 25 NOV / 4 QUEENS WHARF</p><img class="sun" src="../../patterns/surf-rad/sun-stripes.svg" alt=""></div>
  <div class="yellow">ALL WELCOME</div>
</div>""")


def build_y2k():
    css = Y2K_CSS
    post("y2k-chrome", "01-launch", "feed", css, """
<div class="post feed y2k y1">
  <div class="ramp"><img src="../../patterns/y2k-chrome/chrome-ramp.svg" alt=""></div>
  <div class="body"><div class="pill">TALL PEOPLE MEETUP</div><h1>WELLINGTON<br>LAUNCH</h1>
    <div class="details"><div>WED 25 NOV</div><div>5PM TO 8PM</div><div>ROSIE'S RED-HOT CANTINA</div><div>4 QUEENS WHARF</div></div>
    <div class="welcome">ALL WELCOME</div></div>
  <img class="star" src="../../patterns/y2k-chrome/star-four.svg" alt="">
</div>""")
    post("y2k-chrome", "02-room", "feed", css, """
<div class="post feed y2k y2">
  <div class="top"><div class="kicker">Wellington / 25 Nov 2026</div><div class="mono">All welcome</div></div>
  <div class="big"><h1>NO DUCKING<br>REQUIRED</h1><p>A drink and a chat with people who fit.</p></div>
  <div class="photo"><img src="../../photos/y2k-chrome.jpg" alt=""></div>
  <div class="bottom"><div class="details">ROSIE'S RED-HOT CANTINA<br>4 QUEENS WHARF<br>5PM TO 8PM</div><div class="welcome">ALL WELCOME</div></div>
</div>""")
    post("y2k-chrome", "03-story", "story", css, """
<div class="post story y2k y3">
  <img class="bubble" src="../../patterns/y2k-chrome/bubble-gloss.svg" alt="">
  <img class="star" src="../../patterns/y2k-chrome/star-four.svg" alt="">
  <div class="header"><div class="kicker">Tall People Meetup Wellington</div><h1>25</h1><div class="month">NOVEMBER</div></div>
  <div class="photo"><img src="../../photos/y2k-chrome.jpg" alt=""></div>
  <div class="info"><h2>ROSIE'S</h2><p>4 QUEENS WHARF / 5PM TO 8PM</p></div>
  <div class="welcome">ALL WELCOME</div>
</div>""")


def build_pop():
    css = POP_CSS
    post("pop-art", "01-launch", "feed", css, """
<div class="post feed pop p1">
  <div class="panel"><img src="../../photos/pop-comic.jpg" alt=""></div>
  <div class="bubble"><img src="../../patterns/pop-art/speech-bubble.svg" alt=""><span>FINALLY, A ROOM WHERE YOU'RE NOT THE TALLEST</span></div>
  <div class="details"><div>WED 25 NOV / 5PM TO 8PM</div><div>ROSIE'S RED-HOT CANTINA / 4 QUEENS WHARF</div></div>
  <div class="burst"><img src="../../patterns/pop-art/burst.svg" alt=""><span>ALL<br>WELCOME</span></div>
</div>""")
    post("pop-art", "02-mates", "feed", css, """
<div class="post feed pop p2">
  <div class="top"><div class="kicker">Tall is not a membership card</div></div>
  <div class="burst"><img src="../../patterns/pop-art/burst.svg" alt=""><h1>BRING<br>YOUR<br>MATES</h1></div>
  <div class="cyan"><h2>EVERYONE IS WELCOME.<br>YES, EVEN THEM.</h2></div>
  <div class="details"><div>WED 25 NOV</div><div>5PM TO 8PM</div><div>ROSIE'S RED-HOT CANTINA</div><div>4 QUEENS WHARF</div></div>
  <div class="welcome">ALL WELCOME</div>
</div>""")
    post("pop-art", "03-story", "story", css, """
<div class="post story pop p3"><div class="strip">
  <div class="cell photo"><img src="../../photos/pop-comic.jpg" alt=""></div>
  <div class="cell cell2"><div class="bubblebox"><img src="../../patterns/pop-art/speech-bubble.svg" alt=""><span>5 TO 8<br>AT ROSIE'S</span></div></div>
  <div class="cell cell3"><h2>ALL<br>WELCOME</h2><p>WED 25 NOV / 4 QUEENS WHARF</p><div class="meta"><span>TALL PEOPLE MEETUP</span><span>WELLINGTON</span></div></div>
</div></div>""")


def build_bauhaus():
    css = BAUHAUS_CSS
    post("bauhaus", "01-launch", "feed", css, """
<div class="post feed bau b1">
  <div class="top"><div class="kicker">Wellington / 2026</div><h1>TALL<br>PEOPLE<br>MEETUP</h1></div>
  <div class="shapes"><div class="circle"></div><div class="bar"></div><div class="tri"></div></div>
  <div class="details"><div>WED 25 NOV</div><div>5PM TO 8PM</div><div>ROSIE'S RED-HOT CANTINA</div><div>4 QUEENS WHARF</div></div>
  <div class="photo"><img src="../../photos/bauhaus-dessau.jpg" alt=""></div>
  <div class="welcome">ALL WELCOME</div>
</div>""")
    post("bauhaus", "02-date", "feed", css, """
<div class="post feed bau b2">
  <div class="top"><div class="kicker">Wellington / first meetup</div><h1>25<br>NOV</h1><div class="circle"></div><div class="arch"></div><div class="blue"></div></div>
  <div class="details"><div>5PM TO 8PM</div><div>ROSIE'S RED-HOT CANTINA</div><div>4 QUEENS WHARF</div><div>WELLINGTON</div></div>
  <div class="welcome">ALL WELCOME</div>
</div>""")
    post("bauhaus", "03-story", "story", css, """
<div class="post story bau b3">
  <div class="top"><div class="kicker">Tall People Meetup Wellington</div><h1>TALL<br>PEOPLE</h1><div class="circle"></div></div>
  <div class="mid"><h2>5 TO 8</h2><p>WED 25 NOV<br>ROSIE'S RED-HOT CANTINA<br>4 QUEENS WHARF</p><div class="tri"></div></div>
  <div class="bottom"><h2>ALL<br>WELCOME</h2><div class="photo"><img src="../../photos/bauhaus-dessau.jpg" alt=""></div></div>
</div>""")


if __name__ == "__main__":
    build_surf()
    build_y2k()
    build_pop()
    build_bauhaus()
    print("wrote 12 posts")
