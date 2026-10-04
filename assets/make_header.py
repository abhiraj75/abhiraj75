# Generates assets/header.svg: a macOS-style terminal window that types out the profile intro.
from html import escape

L = {
 "A": [" █████╗ ","██╔══██╗","███████║","██╔══██║","██║  ██║","╚═╝  ╚═╝"],
 "B": ["██████╗ ","██╔══██╗","██████╔╝","██╔══██╗","██████╔╝","╚═════╝ "],
 "H": ["██╗  ██╗","██║  ██║","███████║","██╔══██║","██║  ██║","╚═╝  ╚═╝"],
 "I": ["██╗","██║","██║","██║","██║","╚═╝"],
 "R": ["██████╗ ","██╔══██╗","██████╔╝","██╔══██╗","██║  ██║","╚═╝  ╚═╝"],
 "S": ["███████╗","██╔════╝","███████╗","╚════██║","███████║","╚══════╝"],
 "N": ["███╗   ██╗","████╗  ██║","██╔██╗ ██║","██║╚██╗██║","██║ ╚████║","╚═╝  ╚═══╝"],
 "G": [" ██████╗ ","██╔════╝ ","██║  ███╗","██║   ██║","╚██████╔╝"," ╚═════╝ "],
 " ": ["   "] * 6,
 "J": ["     ██╗","     ██║","     ██║","██   ██║","╚█████╔╝"," ╚════╝ "],
}
art = ["".join(L[c][r] for c in "ABHIRAJ") for r in range(6)]

W, H = 860, 412
FS, CW = 15, 9.0  # font size, approx monospace char width
FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,'DejaVu Sans Mono','Liberation Mono',monospace"
PROMPT = "abhiraj@github:~$ "

out = []
def typed(y, cmd, begin, dur, cid):
    # prompt is shown instantly, the command is revealed left to right
    px = 24 + len(PROMPT) * CW
    out.append(f'<clipPath id="{cid}"><rect x="{px}" y="{y-FS}" width="0" height="{FS+6}">'
               f'<animate attributeName="width" from="0" to="{len(cmd)*CW+4}" begin="{begin}s" dur="{dur}s" fill="freeze"/></rect></clipPath>')
    out.append(f'<g opacity="0"><animate attributeName="opacity" to="1" begin="{begin-0.3}s" dur="0.01s" fill="freeze"/>'
               f'<text x="24" y="{y}"><tspan fill="#22C55E">abhiraj@github</tspan><tspan fill="#86EFAC">:</tspan>'
               f'<tspan fill="#4ADE80">~</tspan><tspan fill="#86EFAC">$ </tspan></text>'
               f'<text x="{px}" y="{y}" fill="#BBF7D0" clip-path="url(#{cid})">{escape(cmd)}</text></g>')

def appear(inner, begin):
    out.append(f'<g opacity="0"><animate attributeName="opacity" to="1" begin="{begin}s" dur="0.15s" fill="freeze"/>{inner}</g>')

typed(78, "figlet abhiraj", 0.6, 0.8, "c1")
for i, row in enumerate(art):
    appear(f'<text x="24" y="{112+i*21}" font-size="18" fill="url(#g)" xml:space="preserve">{escape(row)}</text>', 1.6 + i*0.09)
typed(262, "whoami", 2.6, 0.45, "c2")
appear('<text x="24" y="288" fill="#BBF7D0">Full-Stack &amp; AI Engineer <tspan fill="#3F7A55">·</tspan> Open Source Contributor</text>'
       '<text x="24" y="310" fill="#3F7A55"># agentic LLM pipelines, voice AI, and guardrails enforced in code</text>', 3.3)
typed(346, "cat status.txt", 3.9, 0.7, "c3")
appear('<text x="24" y="372" fill="#BBF7D0"><tspan fill="#22C55E">●</tspan> open to internships, collabs and open-source work</text>', 4.8)
# final prompt with blinking block cursor
cx = 24 + len(PROMPT) * CW
appear(f'<text x="24" y="400"><tspan fill="#22C55E">abhiraj@github</tspan><tspan fill="#86EFAC">:</tspan><tspan fill="#4ADE80">~</tspan><tspan fill="#86EFAC">$ </tspan></text>'
       f'<rect x="{cx}" y="{400-FS+2}" width="{CW}" height="{FS+2}" fill="#22C55E">'
       f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1s" repeatCount="indefinite"/></rect>', 5.1)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H+12}" viewBox="0 0 {W} {H+12}" font-family="{FONT}" font-size="{FS}">
<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#22C55E"/><stop offset="1" stop-color="#0A7A33"/></linearGradient></defs>
<rect x="0.5" y="0.5" width="{W-1}" height="{H+11}" rx="10" fill="#0C0C0C" stroke="#2B2B2B"/>
<path d="M0.5 10.5a10 10 0 0 1 10-10h{W-21}a10 10 0 0 1 10 10v24h-{W-1}z" fill="#171717"/>
<line x1="0.5" y1="34.5" x2="{W-0.5}" y2="34.5" stroke="#2B2B2B"/>
<circle cx="22" cy="18" r="6" fill="#ff5f56"/><circle cx="42" cy="18" r="6" fill="#ffbd2e"/><circle cx="62" cy="18" r="6" fill="#27c93f"/>
<text x="{W/2}" y="22" fill="#3F7A55" font-size="13" text-anchor="middle">abhiraj@github: ~ — zsh</text>
{chr(10).join(out)}
</svg>'''
open(__file__.replace("make_header.py", "header.svg"), "w").write(svg)
