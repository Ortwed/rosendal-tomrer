"""Genererer illustrationerne til materieludlejningen: python3 src/lav_materiel_svg.py docs/images/materiel

Simple tegninger i navy og messing uden maerker eller logoer. Fotos fra Sebastians Word-dokument maa ikke bruges."""
import os, sys
UD = sys.argv[1]
N, D, M, L, G, LB = "#13257A", "#0C1850", "#B8873A", "#D9B57A", "#C9D2E3", "#8A97B5"
def ramme(navn, indhold):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360" role="img" aria-label="Illustration: {navn}">
<defs><pattern id="g" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="{N}" stroke-opacity=".07"/></pattern></defs>
<rect width="480" height="360" fill="#EEF2F7"/><rect width="480" height="360" fill="url(#g)"/>
<rect y="300" width="480" height="60" fill="{N}" fill-opacity=".05"/><line x1="0" y1="300" x2="480" y2="300" stroke="{N}" stroke-opacity=".14" stroke-width="2"/>
<g stroke-linejoin="round" stroke-linecap="round">{indhold}</g></svg>'''
def hjul(x, y, r=14):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{D}"/><circle cx="{x}" cy="{y}" r="{r*0.4:.0f}" fill="{G}"/>'
def skygge(cx, rx):
    return f'<ellipse cx="{cx}" cy="303" rx="{rx}" ry="7" fill="{N}" fill-opacity=".14"/>'
S = {}
S["bordsav"] = ("Bordsav", skygge(240,150) +
  f'<line x1="130" y1="200" x2="110" y2="298" stroke="{D}" stroke-width="8"/><line x1="350" y1="200" x2="370" y2="298" stroke="{D}" stroke-width="8"/>'
  f'<line x1="160" y1="200" x2="175" y2="298" stroke="{D}" stroke-width="8"/><line x1="320" y1="200" x2="305" y2="298" stroke="{D}" stroke-width="8"/>'
  f'<rect x="170" y="190" width="140" height="40" rx="6" fill="{N}" stroke="{D}" stroke-width="4"/><rect x="180" y="202" width="30" height="16" rx="3" fill="{M}"/>'
  f'<path d="M206 176 A40 40 0 0 1 274 176 Z" fill="{G}" stroke="{D}" stroke-width="4"/>'
  f'<rect x="100" y="172" width="280" height="22" rx="4" fill="{L}" stroke="{D}" stroke-width="4"/><line x1="240" y1="172" x2="240" y2="194" stroke="{D}" stroke-width="3"/>'
  f'<rect x="120" y="156" width="14" height="18" fill="{M}" stroke="{D}" stroke-width="3"/><line x1="127" y1="160" x2="350" y2="160" stroke="{M}" stroke-width="6"/>')
S["girafsliber"] = ("Girafsliber", skygge(220,170) +
  f'<line x1="120" y1="250" x2="370" y2="120" stroke="{D}" stroke-width="14"/><line x1="120" y1="250" x2="370" y2="120" stroke="{N}" stroke-width="8"/>'
  f'<rect x="300" y="122" width="70" height="30" rx="10" transform="rotate(-28 335 137)" fill="{M}" stroke="{D}" stroke-width="4"/>'
  f'<ellipse cx="110" cy="272" rx="58" ry="18" fill="{N}" stroke="{D}" stroke-width="4"/><ellipse cx="110" cy="266" rx="40" ry="10" fill="{L}"/>'
  f'<path d="M370 120 C 400 110 420 150 400 170" fill="none" stroke="{LB}" stroke-width="6"/><line x1="238" y1="186" x2="262" y2="174" stroke="{M}" stroke-width="12"/>')
S["rullestillads"] = ("Rullestillads", skygge(240,110) +
  "".join(f'<line x1="170" y1="{y}" x2="310" y2="{y}" stroke="{N}" stroke-width="6"/>' for y in range(80,290,30)) +
  f'<line x1="170" y1="260" x2="310" y2="170" stroke="{M}" stroke-width="5"/><line x1="170" y1="170" x2="310" y2="80" stroke="{M}" stroke-width="5"/>'
  f'<line x1="170" y1="60" x2="170" y2="282" stroke="{D}" stroke-width="10"/><line x1="310" y1="60" x2="310" y2="282" stroke="{D}" stroke-width="10"/>'
  f'<rect x="160" y="106" width="160" height="10" rx="2" fill="{M}" stroke="{D}" stroke-width="3"/>' + hjul(170,290,11) + hjul(310,290,11))
S["bukkestillads"] = ("Bukkestillads", skygge(240,170) +
  "".join(f'<path d="M{x-35} 298 L{x} 180 L{x+35} 298" fill="none" stroke="{D}" stroke-width="9"/><line x1="{x-24}" y1="260" x2="{x+24}" y2="260" stroke="{N}" stroke-width="6"/>'
          f'<rect x="{x-30}" y="172" width="60" height="12" rx="3" fill="{N}" stroke="{D}" stroke-width="3"/>' for x in (140, 340)) +
  f'<rect x="80" y="152" width="320" height="20" rx="3" fill="{L}" stroke="{D}" stroke-width="4"/><line x1="140" y1="162" x2="340" y2="162" stroke="{M}" stroke-width="3" stroke-dasharray="14 10"/>')
S["varmeblaeser"] = ("Varmeblæser", skygge(240,100) +
  f'<rect x="160" y="120" width="160" height="160" rx="16" fill="{N}" stroke="{D}" stroke-width="5"/>'
  f'<circle cx="240" cy="200" r="56" fill="{D}"/>' + "".join(f'<circle cx="240" cy="200" r="{r}" fill="none" stroke="{G}" stroke-width="3"/>' for r in (16,30,44)) +
  f'<circle cx="240" cy="200" r="8" fill="{M}"/><path d="M190 120 L190 96 Q190 86 200 86 L280 86 Q290 86 290 96 L290 120" fill="none" stroke="{D}" stroke-width="9"/>'
  f'<rect x="176" y="280" width="128" height="14" rx="4" fill="{D}"/><circle cx="298" cy="134" r="6" fill="{M}"/>')
S["transportvogn"] = ("Transportvogn", skygge(250,170) +
  f'<rect x="120" y="226" width="260" height="22" rx="4" fill="{L}" stroke="{D}" stroke-width="4"/><rect x="120" y="248" width="260" height="10" fill="{N}"/>'
  f'<line x1="120" y1="240" x2="60" y2="210" stroke="{D}" stroke-width="8"/><rect x="40" y="198" width="34" height="14" rx="6" fill="{M}" stroke="{D}" stroke-width="3"/>'
  + hjul(160,278,20) + hjul(340,278,20))
S["gipshejs"] = ("Gipshejs", skygge(240,140) +
  f'<line x1="240" y1="270" x2="150" y2="292" stroke="{D}" stroke-width="9"/><line x1="240" y1="270" x2="330" y2="292" stroke="{D}" stroke-width="9"/><line x1="240" y1="270" x2="240" y2="294" stroke="{D}" stroke-width="9"/>'
  + hjul(150,294,8) + hjul(330,294,8) + hjul(240,296,8) +
  f'<line x1="240" y1="270" x2="240" y2="70" stroke="{N}" stroke-width="12"/><line x1="240" y1="270" x2="240" y2="70" stroke="{D}" stroke-width="4"/>'
  f'<rect x="120" y="62" width="240" height="14" rx="3" fill="{M}" stroke="{D}" stroke-width="3"/><line x1="140" y1="76" x2="140" y2="98" stroke="{D}" stroke-width="6"/><line x1="340" y1="76" x2="340" y2="98" stroke="{D}" stroke-width="6"/>'
  f'<circle cx="262" cy="200" r="20" fill="{G}" stroke="{D}" stroke-width="4"/><line x1="262" y1="200" x2="290" y2="176" stroke="{D}" stroke-width="5"/>')
S["affugter"] = ("Affugter", skygge(240,90) +
  f'<rect x="180" y="96" width="120" height="186" rx="14" fill="{N}" stroke="{D}" stroke-width="5"/>'
  + "".join(f'<line x1="198" y1="{y}" x2="282" y2="{y}" stroke="#FFFFFF" stroke-opacity=".45" stroke-width="4"/>' for y in range(120,180,12)) +
  f'<rect x="198" y="200" width="84" height="56" rx="6" fill="{G}" stroke="{D}" stroke-width="3"/><rect x="206" y="226" width="68" height="22" rx="3" fill="{L}"/>'
  f'<path d="M210 96 L210 78 L270 78 L270 96" fill="none" stroke="{D}" stroke-width="8"/><circle cx="284" cy="110" r="5" fill="{M}"/>' + hjul(196,290,9) + hjul(284,290,9))
S["betonblander"] = ("Betonblander", skygge(240,120) +
  f'<line x1="240" y1="200" x2="180" y2="292" stroke="{D}" stroke-width="12"/><line x1="240" y1="200" x2="300" y2="294" stroke="{D}" stroke-width="12"/>' + hjul(180,290,18) +
  f'<g transform="rotate(-28 240 170)"><rect x="170" y="128" width="130" height="86" rx="34" fill="{M}" stroke="{D}" stroke-width="5"/>'
  f'<rect x="210" y="130" width="8" height="82" fill="#9A6E2C"/><rect x="250" y="130" width="8" height="82" fill="#9A6E2C"/>'
  f'<path d="M298 140 L340 152 L340 190 L298 202 Z" fill="{L}" stroke="{D}" stroke-width="5"/></g>'
  f'<rect x="256" y="222" width="40" height="30" rx="5" fill="{N}" stroke="{D}" stroke-width="4"/>')
S["dumper"] = ("Dumper", skygge(240,170) +
  f'<rect x="96" y="246" width="260" height="40" rx="20" fill="{D}"/>' + "".join(hjul(x,266,13) for x in (118,184,250,334)) +
  f'<path d="M80 246 L60 160 L230 160 L230 246 Z" fill="{M}" stroke="{D}" stroke-width="5"/><rect x="54" y="152" width="184" height="12" rx="3" fill="{L}" stroke="{D}" stroke-width="3"/>'
  f'<rect x="236" y="196" width="100" height="52" rx="8" fill="{N}" stroke="{D}" stroke-width="5"/><line x1="320" y1="196" x2="380" y2="110" stroke="{D}" stroke-width="9"/>'
  f'<line x1="368" y1="104" x2="398" y2="118" stroke="{M}" stroke-width="12"/>')
S["paelebor"] = ("Pælebor", skygge(240,90) +
  f'<line x1="240" y1="170" x2="240" y2="296" stroke="{D}" stroke-width="8"/>'
  + "".join(f'<path d="M226 {y} Q240 {y-8} 254 {y}" fill="none" stroke="{N}" stroke-width="8"/>' for y in range(196,296,16)) +
  f'<rect x="200" y="112" width="80" height="58" rx="12" fill="{N}" stroke="{D}" stroke-width="5"/><rect x="214" y="124" width="52" height="16" rx="4" fill="{M}"/>'
  f'<line x1="120" y1="150" x2="360" y2="150" stroke="{D}" stroke-width="10"/><rect x="100" y="142" width="34" height="16" rx="7" fill="{M}" stroke="{D}" stroke-width="3"/><rect x="346" y="142" width="34" height="16" rx="7" fill="{M}" stroke="{D}" stroke-width="3"/>')
S["jordbor"] = ("Mobilt jordbor", skygge(240,170) +
  f'<line x1="300" y1="240" x2="60" y2="250" stroke="{D}" stroke-width="10"/><circle cx="56" cy="250" r="10" fill="{M}" stroke="{D}" stroke-width="3"/>'
  f'<line x1="300" y1="110" x2="300" y2="240" stroke="{N}" stroke-width="12"/><line x1="300" y1="240" x2="300" y2="296" stroke="{D}" stroke-width="8"/>'
  + "".join(f'<path d="M282 {y} Q300 {y-9} 318 {y}" fill="none" stroke="{N}" stroke-width="8"/>' for y in range(256,296,14)) +
  f'<rect x="250" y="90" width="100" height="56" rx="10" fill="{N}" stroke="{D}" stroke-width="5"/><rect x="264" y="102" width="40" height="16" rx="4" fill="{M}"/>'
  f'<line x1="300" y1="146" x2="190" y2="244" stroke="{D}" stroke-width="7"/>' + hjul(200,280,16) + hjul(370,280,16) +
  f'<line x1="200" y1="280" x2="370" y2="280" stroke="{D}" stroke-width="6"/>')
for k, (navn, ind) in S.items():
    with open(os.path.join(UD, f"{k}.svg"), "w", encoding="utf-8") as f:
        f.write(ramme(navn, ind))
print(len(S), "illustrationer")
