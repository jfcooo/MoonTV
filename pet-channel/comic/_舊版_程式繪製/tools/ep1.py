import sys; sys.path.insert(0,sys.argv[2])
from comic_lib import *
out=sys.argv[1]
P={}
# 1: cat sniffing alone
P[1]=panel(
 cat(540,760,1.75,eyes="half",mouth="flat")
 +stink(900,520,2,0.9)+stink(110,560,2,0.8)
 +bubble(250,150,580,210,["……","什麼味道？"],tail=(560,520),size=62)
 +'<text x="850" y="640" font-size="60" fill="#4a3b32" font-weight="900" transform="rotate(-12 850 640)">嗅嗅</text>'
 ,1)
# 2: dog bursts in, dirty and happy
P[2]=panel(
 '<rect x="60" y="330" width="300" height="690" rx="12" fill="#cfe6f0" stroke="#4a3b32" stroke-width="7"/><rect x="60" y="330" width="60" height="690" fill="#b98b5e" stroke="#4a3b32" stroke-width="7"/>'
 +dog(600,800,1.4,eyes="happy",mouth="tongue",dirty=True)
 +stink(250,720,2,0.9)+stink(860,720,2,0.9)+stink(520,470,3,0.7)
 +bubble(330,150,680,230,["我回來了！","今天在草地打滾～"],tail=(600,600),size=58,shout=True)
 ,2,bg="#fff1dc")
# 3: cat with clothespin keeps distance
P[3]=panel(
 cat(260,800,1.3,eyes="closed",mouth="flat",peg=True)
 +dog(820,810,1.25,eyes="dot",mouth="smile",dirty=True,flip=True)
 +stink(760,520,3,0.7)
 +'<path d="M440,1150 L640,1150" stroke="#e8574f" stroke-width="8" stroke-dasharray="20 16"/><path d="M440,1130 L440,1170 M640,1130 L640,1170" stroke="#e8574f" stroke-width="8"/>'
 +'<text x="540" y="1125" font-size="44" text-anchor="middle" fill="#e8574f" font-weight="900">2 m</text>'
 +bubble(90,170,560,220,["請保持","兩公尺距離。"],tail=(270,600),size=58)
 ,3)
# 4: dog scratching, clueless; cat holds sign
P[4]=panel(
 dog(700,850,1.25,eyes="happy",mouth="smile",dirty=True,scratch=True)
 +lines_fx(860,860)+lines_fx(880,930)
 +'<text x="930" y="800" font-size="52" fill="#4a3b32" font-weight="900" transform="rotate(10 930 800)">抓抓</text>'
 +cat(215,930,0.85,eyes="half",mouth="flat",peg=True)
 +'<rect x="205" y="500" width="14" height="330" fill="#b98b5e" stroke="#4a3b32" stroke-width="5"/>'
 +'<rect x="70" y="330" width="300" height="200" rx="18" fill="#fff" stroke="#4a3b32" stroke-width="7"/>'
 +'<text x="220" y="400" font-size="58" text-anchor="middle" dominant-baseline="central" fill="#e8574f" font-weight="900" stroke="#e8574f" stroke-width="1.5">今晚</text><text x="220" y="472" font-size="58" text-anchor="middle" dominant-baseline="central" fill="#e8574f" font-weight="900" stroke="#e8574f" stroke-width="1.5">洗澡</text>'
 +bubble(440,170,560,230,["咦？","我覺得我很香啊"],tail=(700,640),size=56)
 +sweat(380,800,1.2)
 ,4,bg="#fff1dc")
for n,svg in P.items(): open(f"{out}/p{n}.svg","w",encoding="utf-8").write(svg)
# character sheet
W,H=1080,1350
sheet=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="WenQuanYi Zen Hei, sans-serif">
<rect width="{W}" height="{H}" fill="#fdf3e3"/>
<text x="540" y="130" font-size="92" text-anchor="middle" fill="{OL}" font-weight="900" stroke="{OL}" stroke-width="2">豆皮與芝麻</text>
<text x="540" y="200" font-size="38" text-anchor="middle" fill="{OL}" opacity=".7">一隻愛打滾的狗 × 一隻有潔癖的貓</text>
<rect x="50" y="250" width="470" height="1040" rx="36" fill="#fff1dc" stroke="{OL}" stroke-width="7"/>
<rect x="560" y="250" width="470" height="1040" rx="36" fill="#eef1f5" stroke="{OL}" stroke-width="7"/>
{dog(285,540,1.0,eyes="happy",mouth="tongue")}
{cat(795,550,1.0,eyes="half",mouth="flat")}
<text x="285" y="950" font-size="72" text-anchor="middle" fill="{OL}" font-weight="900" stroke="{OL}" stroke-width="1.5">豆皮</text>
<text x="795" y="950" font-size="72" text-anchor="middle" fill="{OL}" font-weight="900" stroke="{OL}" stroke-width="1.5">芝麻</text>
'''
def tl(x,y,lines):
    return "".join(f'<text x="{x}" y="{y+i*52}" font-size="34" text-anchor="middle" fill="{OL}">{l}</text>' for i,l in enumerate(lines))
sheet+=tl(285,1030,["約克夏・弟弟","樂天、少根筋","最愛在草地打滾","皮膚敏感，容易癢","口頭禪：「我很香啊」"])
sheet+=tl(795,1030,["灰貓・姊姊","潔癖、嘴硬心軟","鼻子比誰都靈","家裡的衛生股長","口頭禪：「今晚洗澡」"])
sheet+="</svg>"
open(f"{out}/characters.svg","w",encoding="utf-8").write(sheet)
