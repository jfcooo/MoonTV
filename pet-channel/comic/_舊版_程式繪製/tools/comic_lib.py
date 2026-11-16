OL="#4a3b32"  # outline
def g(x,y,s,inner,flip=False,rot=0):
    sx=-s if flip else s
    return f'<g transform="translate({x},{y}) rotate({rot}) scale({sx},{s})" stroke="{OL}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">{inner}</g>'
def eyes_svg(kind,dx=46,y=-8,cat=False):
    o=""
    for sx in (-dx,dx):
        if kind=="dot":
            if cat: o+=f'<ellipse cx="{sx}" cy="{y}" rx="19" ry="21" fill="#f2d24b"/><ellipse cx="{sx}" cy="{y}" rx="6" ry="15" fill="{OL}" stroke="none"/>'
            else: o+=f'<circle cx="{sx}" cy="{y}" r="11" fill="{OL}" stroke="none"/><circle cx="{sx+4}" cy="{y-4}" r="3.5" fill="#fff" stroke="none"/>'
        elif kind=="happy": o+=f'<path d="M{sx-15},{y+4} Q{sx},{y-16} {sx+15},{y+4}" fill="none"/>'
        elif kind=="half":
            o+=f'<path d="M{sx-20},{y} A20,18 0 0 0 {sx+20},{y} Z" fill="#f2d24b"/><ellipse cx="{sx}" cy="{y+8}" rx="5" ry="8" fill="{OL}" stroke="none"/><path d="M{sx-24},{y} L{sx+24},{y}" fill="none"/>'
        elif kind=="closed": o+=f'<path d="M{sx-15},{y} L{sx+15},{y}" fill="none"/>'
        elif kind=="wide":
            o+=f'<circle cx="{sx}" cy="{y}" r="17" fill="#fff"/><circle cx="{sx}" cy="{y}" r="6" fill="{OL}" stroke="none"/>'
        elif kind=="x": o+=f'<path d="M{sx-13},{y-11} L{sx+13},{y} L{sx-13},{y+11}" fill="none"/>' if sx<0 else f'<path d="M{sx+13},{y-11} L{sx-13},{y} L{sx+13},{y+11}" fill="none"/>'
    return o
def mouth_svg(kind,y=44):
    if kind=="smile": return f'<path d="M-18,{y} Q-9,{y+12} 0,{y} Q9,{y+12} 18,{y}" fill="none"/>'
    if kind=="open": return f'<path d="M-20,{y-2} Q0,{y+40} 20,{y-2} Z" fill="#e2675f"/>'
    if kind=="flat": return f'<path d="M-12,{y+4} L12,{y+4}" fill="none"/>'
    if kind=="frown": return f'<path d="M-14,{y+10} Q0,{y-4} 14,{y+10}" fill="none"/>'
    if kind=="tongue": return f'<path d="M-20,{y-2} Q0,{y+34} 20,{y-2} Z" fill="#7a3b33"/><path d="M-8,{y+12} Q0,{y+44} 10,{y+12} Z" fill="#f28a8a"/>'
    return ""
def dog(x,y,s=1,eyes="dot",mouth="smile",flip=False,rot=0,dirty=False,scratch=False):
    TAN="#ecbd80";TAN2="#f8e2b8";GREY="#8f9bb0";EAR="#c98f52"
    b=""
    b+=f'<path d="M95,170 Q175,150 160,80" fill="none" stroke-width="26" stroke="{OL}"/><path d="M95,170 Q175,150 160,80" fill="none" stroke-width="14" stroke="{GREY}"/>'
    b+=f'<ellipse cx="0" cy="160" rx="108" ry="88" fill="{GREY}"/><ellipse cx="0" cy="178" rx="58" ry="62" fill="{TAN2}" stroke="none"/>'
    if scratch:
        b+=f'<ellipse cx="-52" cy="238" rx="30" ry="20" fill="{TAN}"/>'
        b+=f'<path d="M70,225 Q150,190 96,96" fill="none" stroke-width="40" stroke="{OL}"/><path d="M70,225 Q150,190 96,96" fill="none" stroke-width="26" stroke="{TAN}"/>'
    else:
        b+=f'<ellipse cx="-52" cy="238" rx="30" ry="20" fill="{TAN}"/><ellipse cx="52" cy="238" rx="30" ry="20" fill="{TAN}"/>'
    b+=f'<path d="M-112,-60 L-92,-178 L-28,-96 Z" fill="{EAR}"/><path d="M112,-60 L92,-178 L28,-96 Z" fill="{EAR}"/>'
    b+=f'<path d="M-92,-90 L-86,-140 L-56,-98 Z" fill="#f2b5a0" stroke="none"/><path d="M92,-90 L86,-140 L56,-98 Z" fill="#f2b5a0" stroke="none"/>'
    b+=f'<ellipse cx="0" cy="0" rx="128" ry="110" fill="{TAN}"/>'
    # side fluff
    b+=f'<path d="M-120,20 Q-150,60 -112,84 Q-120,60 -100,60" fill="{TAN}"/><path d="M120,20 Q150,60 112,84 Q120,60 100,60" fill="{TAN}"/>'
    b+=f'<ellipse cx="0" cy="46" rx="66" ry="46" fill="{TAN2}" stroke="none"/>'
    # topknot + bow
    b+=f'<path d="M-16,-104 Q-26,-160 0,-176 Q26,-160 16,-104 Z" fill="{TAN2}"/>'
    b+=f'<path d="M0,-112 L-34,-132 L-34,-94 Z" fill="#e8574f"/><path d="M0,-112 L34,-132 L34,-94 Z" fill="#e8574f"/><circle cx="0" cy="-112" r="9" fill="#e8574f"/>'
    b+=eyes_svg(eyes)
    b+=f'<ellipse cx="0" cy="26" rx="17" ry="12" fill="{OL}" stroke="none"/>'
    b+=mouth_svg(mouth)
    b+=f'<ellipse cx="-78" cy="34" rx="17" ry="10" fill="#f6a59a" stroke="none" opacity=".7"/><ellipse cx="78" cy="34" rx="17" ry="10" fill="#f6a59a" stroke="none" opacity=".7"/>'
    if dirty:
        for cx,cy,r in ((-60,150,16),(40,200,13),(80,-40,12),(-90,-20,10),(20,120,9)):
            b+=f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*.8}" fill="#8a6a4a" stroke="none" opacity=".85"/>'
    return g(x,y,s,b,flip,rot)
def cat(x,y,s=1,eyes="half",mouth="flat",flip=False,rot=0,peg=False):
    C="#666b7a";W="#ffffff"
    b=""
    b+=f'<path d="M80,210 Q190,220 170,120 Q160,80 135,96" fill="none" stroke-width="30" stroke="{OL}"/><path d="M80,210 Q190,220 170,120 Q160,80 135,96" fill="none" stroke-width="17" stroke="{C}"/>'
    b+=f'<ellipse cx="0" cy="158" rx="92" ry="86" fill="{C}"/><ellipse cx="0" cy="180" rx="48" ry="56" fill="{W}" stroke="none"/>'
    b+=f'<ellipse cx="-44" cy="238" rx="28" ry="18" fill="{W}"/><ellipse cx="44" cy="238" rx="28" ry="18" fill="{W}"/>'
    b+=f'<path d="M-118,-40 L-104,-150 L-30,-88 Z" fill="{C}"/><path d="M118,-40 L104,-150 L30,-88 Z" fill="{C}"/>'
    b+=f'<path d="M-98,-70 L-92,-118 L-58,-88 Z" fill="#f2b5a0" stroke="none"/><path d="M98,-70 L92,-118 L58,-88 Z" fill="#f2b5a0" stroke="none"/>'
    b+=f'<ellipse cx="0" cy="0" rx="124" ry="100" fill="{C}"/>'
    b+=f'<path d="M-62,62 Q-70,18 0,14 Q70,18 62,62 Q40,92 0,90 Q-40,92 -62,62 Z" fill="{W}" stroke="none"/>'
    b+=eyes_svg(eyes,dx=50,y=-12,cat=True)
    if peg:
        b+=f'<rect x="-13" y="6" width="26" height="62" rx="6" fill="#f0b93a"/><path d="M0,10 L0,60" fill="none" stroke-width="4"/>'
    else:
        b+=f'<path d="M-10,26 L10,26 L0,38 Z" fill="#f28a8a"/>'
    b+=mouth_svg(mouth,y=46)
    for sgn in (-1,1):
        b+=f'<path d="M{sgn*70},36 L{sgn*128},26 M{sgn*70},50 L{sgn*128},58" fill="none" stroke-width="4"/>'
    return g(x,y,s,b,flip,rot)
def bubble(x,y,w,h,lines,tail=None,size=54,fill="#fff",color=None,shout=False):
    color=color or OL
    o=""
    if tail:
        tx,ty=tail; bx=min(max(tx,x+70),x+w-70); by=y+h if ty>y+h/2 else y
        o+=f'<path d="M{bx-28},{by} L{tx},{ty} L{bx+28},{by} Z" fill="{fill}" stroke="{OL}" stroke-width="6" stroke-linejoin="round"/>'
    o+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{46}" fill="{fill}" stroke="{OL}" stroke-width="6"/>'
    if tail:
        o+=f'<path d="M{bx-24},{by+(-4 if by>y else 4)} L{bx+24},{by+(-4 if by>y else 4)}" stroke="{fill}" stroke-width="12"/>'
    lh=size*1.3; y0=y+h/2-lh*(len(lines)-1)/2
    for i,l in enumerate(lines):
        o+=f'<text x="{x+w/2}" y="{y0+i*lh}" font-size="{size}" text-anchor="middle" dominant-baseline="central" fill="{color}" font-weight="{900 if shout else 700}" stroke="{color}" stroke-width="{1.6 if shout else 1}">{l}</text>'
    return o
def stink(x,y,n=3,s=1,col="#8aa84f"):
    o=""
    for i in range(n):
        xx=x+i*46*s
        o+=f'<path d="M{xx},{y} q{-18*s},{-28*s} 0,{-56*s} q{18*s},{-28*s} 0,{-56*s} q{-18*s},{-28*s} 0,{-56*s}" fill="none" stroke="{col}" stroke-width="{9*s}" stroke-linecap="round" opacity=".85"/>'
    return o
def sweat(x,y,s=1):
    return f'<path d="M{x},{y} q{-16*s},{30*s} 0,{40*s} q{16*s},{-10*s} 0,{-40*s} Z" fill="#9fd4f2" stroke="{OL}" stroke-width="4"/>'
def lines_fx(x,y,kind="scratch"):
    o=""
    for i in range(3):
        o+=f'<path d="M{x+i*26},{y-i*8} q14,-22 30,-8" fill="none" stroke="{OL}" stroke-width="5" stroke-linecap="round"/>'
    return o
def panel(inner,n,bg="#fdf3e3",floor="#f3dcc0",title="豆皮與芝麻",ep="第 1 話　誰臭？",W=1080,H=1350):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="WenQuanYi Zen Hei, sans-serif">
<rect width="{W}" height="{H}" fill="{bg}"/><rect y="{H-330}" width="{W}" height="330" fill="{floor}"/>
<path d="M0,{H-330} L{W},{H-330}" stroke="{OL}" stroke-width="5" opacity=".35"/>
{inner}
<rect x="24" y="24" width="{W-48}" height="{H-48}" rx="36" fill="none" stroke="{OL}" stroke-width="10"/>
<circle cx="96" cy="96" r="44" fill="#e8574f" stroke="{OL}" stroke-width="6"/><text x="96" y="98" font-size="52" text-anchor="middle" dominant-baseline="central" fill="#fff" font-weight="900">{n}</text>
<text x="{W/2}" y="{H-70}" font-size="34" text-anchor="middle" fill="{OL}" opacity=".7">{title}｜{ep}</text>
</svg>'''
