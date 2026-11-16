import sys,re
src,dst,font=sys.argv[1],sys.argv[2],sys.argv[3]
for n in ("p1","p2","p3","p4","characters"):
    s=open(f"{src}/{n}.svg",encoding="utf-8").read()
    head,rest=s.split(">",1); body=rest.rsplit("</svg>",1)[0]
    head=head.replace("WenQuanYi Zen Hei, sans-serif",f"{font}, WenQuanYi Zen Hei, sans-serif")
    # soft ground shadows under characters are added via lib; here: filters
    texts=''.join(re.findall(r'<text.*?</text>',body,flags=re.S)); body=re.sub(r'<text.*?</text>','',body,flags=re.S)
    defs='''<defs>
<filter id="wob" x="-5%" y="-5%" width="110%" height="110%">
 <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="7" result="n1"/>
 <feDisplacementMap in="SourceGraphic" in2="n1" scale="9" xChannelSelector="R" yChannelSelector="G" result="d1"/>
 <feTurbulence type="fractalNoise" baseFrequency="0.55" numOctaves="1" seed="3" result="n2"/>
 <feDisplacementMap in="d1" in2="n2" scale="3.2" xChannelSelector="R" yChannelSelector="G"/>
</filter>
<filter id="paper" x="0" y="0" width="100%" height="100%">
 <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" seed="11"/>
 <feColorMatrix type="matrix" values="0 0 0 0 0.35  0 0 0 0 0.27  0 0 0 0 0.2  0 0 0 -1.1 0.62"/>
</filter>
<filter id="blot" x="0" y="0" width="100%" height="100%">
 <feTurbulence type="fractalNoise" baseFrequency="0.006" numOctaves="3" seed="5"/>
 <feColorMatrix type="matrix" values="0 0 0 0 0.55  0 0 0 0 0.42  0 0 0 0 0.3  0 0 0 -1.6 0.72"/>
</filter>
<filter id="hatch" x="0" y="0" width="100%" height="100%">
 <feTurbulence type="fractalNoise" baseFrequency="0.012 0.35" numOctaves="2" seed="21"/>
 <feColorMatrix type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 -2.2 1.0"/>
</filter>
<filter id="soft" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="1" seed="9" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="3"/></filter>
</defs>'''
    out=(head+">"+defs+f'<g filter="url(#wob)">{body}</g><g filter="url(#soft)">{texts}</g>'
      +'<rect width="100%" height="100%" filter="url(#hatch)" opacity=".22" style="mix-blend-mode:soft-light"/>'
      +'<rect width="100%" height="100%" filter="url(#blot)" opacity=".28" style="mix-blend-mode:multiply"/>'
      +'<rect width="100%" height="100%" filter="url(#paper)" opacity=".55" style="mix-blend-mode:multiply"/></svg>')
    open(f"{dst}/{n}.svg","w",encoding="utf-8").write(out)
