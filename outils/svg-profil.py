"""SVG animés du texte du profil GitHub : titres de section, terminal « à propos », contact.
Usage : python3 -I svg-profil.py ~/Projets/portfolio"""
import pathlib, sys, html
out = pathlib.Path(sys.argv[1]) / 'readme'
SANS = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"
e = html.escape

def titre(fichier, numero, mot, sous):
    """Titre de section : numéro, grand mot en dégradé qui brille, trait qui se dessine."""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="120" viewBox="0 0 1200 120">
<style>
  .num {{ font: 700 15px {SANS}; letter-spacing: 4px; fill: #f26b3a; }}
  .mot {{ font: 800 52px {SANS}; letter-spacing: -1.5px; }}
  .sous {{ font: 400 18px {SANS}; fill: #9a9ab0; }}
  .entre {{ opacity: 0; animation: entre .9s cubic-bezier(.22,1,.36,1) forwards; }}
  .d2 {{ animation-delay: .15s; }} .d3 {{ animation-delay: .35s; }}
  @keyframes entre {{ from {{ opacity: 0; transform: translateY(14px); }} to {{ opacity: 1; transform: none; }} }}
  .trait {{ stroke-dasharray: 1200; stroke-dashoffset: 1200; animation: trace 1.6s cubic-bezier(.22,1,.36,1) .3s forwards; }}
  @keyframes trace {{ to {{ stroke-dashoffset: 0; }} }}
</style>
<defs>
  <linearGradient id="g" x1="0" x2="1">
    <stop offset="0" stop-color="#f4f4f7"/><stop offset=".4" stop-color="#f4f4f7"/><stop offset=".5" stop-color="#f26b3a"/><stop offset=".6" stop-color="#f4f4f7"/><stop offset="1" stop-color="#f4f4f7"/>
    <animate attributeName="x1" values="-1;1.2" dur="4s" repeatCount="indefinite"/><animate attributeName="x2" values="0;2.2" dur="4s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="t" x1="0" x2="1"><stop offset="0" stop-color="#3b82f6"/><stop offset=".5" stop-color="#f26b3a"/><stop offset="1" stop-color="#f26b3a" stop-opacity="0"/></linearGradient>
</defs>
<text class="num entre" x="4" y="28">{e(numero)}</text>
<text class="mot entre d2" x="0" y="80" fill="url(#g)">{e(mot)}</text>
<text class="sous entre d3" x="1196" y="80" text-anchor="end">{e(sous)}</text>
<line class="trait" x1="2" y1="104" x2="1198" y2="104" stroke="url(#t)" stroke-width="2"/>
</svg>'''
    (out / fichier).write_text(svg, encoding='utf-8')

def terminal():
    """Terminal « whoami » : les commandes se tapent, les réponses apparaissent."""
    lignes = [
        ('cmd', 'whoami'),
        ('out', 'Iro007. Développeur web et mobile, basé à Goma (RDC).'),
        ('cmd', 'cat mission.txt'),
        ('out', 'Des applis qui tiennent le terrain : réseau qui coupe,'),
        ('out', 'téléphones modestes, paiement par mobile money.'),
        ('cmd', 'ls projets/'),
        ('dir', 'RHEEKA/   Kitty/   Estory/   Rice/   Manga_site/'),
        ('cmd', 'cat stack.txt'),
        ('out', 'Flutter · React · TypeScript · Supabase · PostgreSQL · LiveKit'),
        ('cmd', 'echo $STATUT'),
        ('ok',  'Ouvert aux collaborations. Toujours en train d\'apprendre.'),
    ]
    invite = 'iro007@goma:~$ '
    car = 11.4  # largeur d'un caractère à 19px
    y, t, corps, defs = 92, 0.6, '', ''
    for i, (genre, texte) in enumerate(lignes):
        if genre == 'cmd':
            x0 = 40 + len(invite) * car
            duree = max(.35, len(texte) * .06)
            defs += f'<clipPath id="c{i}"><rect x="{x0}" y="{y-20}" width="0" height="28"><animate attributeName="width" from="0" to="{len(texte)*car+4}" begin="{t:.2f}s" dur="{duree:.2f}s" fill="freeze"/></rect></clipPath>'
            corps += (f'<g opacity="0"><set attributeName="opacity" to="1" begin="{t-.25:.2f}s" fill="freeze"/>'
                      f'<text x="40" y="{y}"><tspan class="inv">iro007@goma</tspan><tspan class="sep">:</tspan><tspan class="chem">~</tspan><tspan class="sep">$ </tspan></text>'
                      f'<text class="cmd" x="{x0}" y="{y}" clip-path="url(#c{i})">{e(texte)}</text></g>')
            t += duree + .25
        else:
            cls = {'out': 'out', 'dir': 'dir', 'ok': 'ok'}[genre]
            corps += f'<text class="{cls}" x="40" y="{y}" opacity="0">{e(texte)}<animate attributeName="opacity" from="0" to="1" begin="{t:.2f}s" dur=".35s" fill="freeze"/></text>'
            t += .3
            if i + 1 < len(lignes) and lignes[i + 1][0] == 'cmd':
                y += 12; t += .35
        y += 30
    # Dernière invite avec curseur qui clignote
    corps += (f'<g opacity="0"><set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/>'
              f'<text x="40" y="{y}"><tspan class="inv">iro007@goma</tspan><tspan class="sep">:</tspan><tspan class="chem">~</tspan><tspan class="sep">$ </tspan></text>'
              f'<rect x="{40 + len(invite)*car}" y="{y-17}" width="11" height="22" fill="#f26b3a"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect></g>')
    h = y + 40
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}">
<style>
  text {{ font: 400 19px {MONO}; fill: #c9c9d6; white-space: pre; }}
  .inv {{ fill: #3b82f6; font-weight: 700; }} .sep {{ fill: #9a9ab0; }} .chem {{ fill: #e9a91b; }}
  .cmd {{ fill: #f4f4f7; font-weight: 700; }} .out {{ fill: #b4b4c6; }} .dir {{ fill: #2dd4bf; font-weight: 700; }} .ok {{ fill: #34d399; }}
  .titre {{ font: 600 14px {SANS}; fill: #9a9ab0; }}
</style>
<defs>{defs}
  <filter id="f" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="40"/></filter>
  <clipPath id="cadre"><rect width="1200" height="{h}" rx="20"/></clipPath>
</defs>
<g clip-path="url(#cadre)">
  <rect width="1200" height="{h}" fill="#0b0b12"/>
  <circle cx="1120" cy="{h}" r="160" fill="#3b82f6" opacity=".18" filter="url(#f)"/>
  <circle cx="60" cy="0" r="140" fill="#7a2a63" opacity=".35" filter="url(#f)"/>
  <rect width="1200" height="44" fill="#151522"/>
  <circle cx="28" cy="22" r="7" fill="#ff5f57"/><circle cx="50" cy="22" r="7" fill="#febc2e"/><circle cx="72" cy="22" r="7" fill="#28c840"/>
  <text class="titre" x="600" y="27" text-anchor="middle">iro007 — bash — goma</text>
  {corps}
</g>
<rect x=".5" y=".5" width="1199" height="{h-1}" rx="20" fill="none" stroke="#fff" stroke-opacity=".08"/>
</svg>'''
    (out / 'terminal.svg').write_text(svg, encoding='utf-8')

def contact():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300">
<style>
  .grand {{ font: 800 64px {SANS}; letter-spacing: -2px; }}
  .petit {{ font: 400 21px {SANS}; fill: #9a9ab0; }}
  .btn {{ font: 700 19px {SANS}; fill: #0b0b12; }}
  .entre {{ opacity: 0; animation: entre 1s cubic-bezier(.22,1,.36,1) forwards; }}
  .d2 {{ animation-delay: .15s; }} .d3 {{ animation-delay: .3s; }} .d4 {{ animation-delay: .45s; }}
  @keyframes entre {{ from {{ opacity: 0; transform: translateY(18px); }} to {{ opacity: 1; transform: none; }} }}
  .b {{ animation: bouge 14s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
  @keyframes bouge {{ 50% {{ transform: translate(80px, -30px) scale(1.15); }} }}
  .fleche {{ animation: fleche 1.4s ease-in-out infinite; }}
  @keyframes fleche {{ 50% {{ transform: translateX(6px); }} }}
</style>
<defs>
  <linearGradient id="deg" x1="0" x2="1">
    <stop offset="0" stop-color="#3b82f6"/><stop offset=".45" stop-color="#f26b3a"/><stop offset=".75" stop-color="#e9a91b"/><stop offset="1" stop-color="#3b82f6"/>
    <animate attributeName="x1" values="0;-1;0" dur="6s" repeatCount="indefinite"/><animate attributeName="x2" values="1;0;1" dur="6s" repeatCount="indefinite"/>
  </linearGradient>
  <filter id="f" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
  <clipPath id="cadre"><rect width="1200" height="300" rx="24"/></clipPath>
</defs>
<g clip-path="url(#cadre)">
  <rect width="1200" height="300" fill="#0b0b12"/>
  <circle class="b" cx="300" cy="300" r="170" fill="#7a2a63" opacity=".55" filter="url(#f)"/>
  <circle class="b" cx="950" cy="20" r="150" fill="#3b82f6" opacity=".3" filter="url(#f)" style="animation-direction:reverse"/>
  <text class="grand entre" x="600" y="104" text-anchor="middle" fill="#f4f4f7">Un projet en tête ?</text>
  <text class="grand entre d2" x="600" y="172" text-anchor="middle" fill="url(#deg)">Parlons-en.</text>
  <text class="petit entre d3" x="600" y="212" text-anchor="middle">Une boutique en ligne, une appli, une idée pour Goma.</text>
  <g class="entre d4">
    <rect x="490" y="232" width="220" height="48" rx="24" fill="#f4f4f7"/>
    <text class="btn" x="584" y="263" text-anchor="middle">M'écrire</text>
    <g class="fleche"><path d="M650 256h20m-8-8 8 8-8 8" stroke="#0b0b12" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>
  </g>
</g>
<rect x=".5" y=".5" width="1199" height="299" rx="24" fill="none" stroke="#fff" stroke-opacity=".08"/>
</svg>'''
    (out / 'contact.svg').write_text(svg, encoding='utf-8')

def chiffres():
    """Quatre grands chiffres qui montent l'un après l'autre."""
    items = [('3', 'applis en ligne', 'RHEEKA, Kitty, Estory', '#f26b3a'),
             ('600+', 'tests de base de données', 'chaque règle vérifiée', '#3b82f6'),
             ('18', 'quartiers de Goma', 'dessinés sur la carte', '#e9a91b'),
             ('72', 'stickers originaux', 'dessinés pour Kitty', '#2dd4bf')]
    corps = ''
    for i, (n, label, detail, c) in enumerate(items):
        x = 24 + i * 294
        d = .15 + i * .15
        corps += f'''<g class="entre" style="animation-delay:{d:.2f}s">
  <rect x="{x}" y="24" width="270" height="192" rx="18" fill="#151522" stroke="#fff" stroke-opacity=".07"/>
  <rect x="{x}" y="24" width="270" height="4" rx="2" fill="{c}"><animate attributeName="width" from="0" to="270" begin="{d+.3:.2f}s" dur="1s" fill="freeze"/></rect>
  <text class="n" x="{x+26}" y="112" fill="{c}">{e(n)}</text>
  <text class="l" x="{x+26}" y="152">{e(label)}</text>
  <text class="d" x="{x+26}" y="182">{e(detail)}</text>
</g>'''
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="240" viewBox="0 0 1200 240">
<style>
  .n {{ font: 800 64px {SANS}; letter-spacing: -2px; }}
  .l {{ font: 700 19px {SANS}; fill: #f4f4f7; }}
  .d {{ font: 400 16px {SANS}; fill: #9a9ab0; }}
  .entre {{ opacity: 0; animation: entre .9s cubic-bezier(.22,1,.36,1) forwards; }}
  @keyframes entre {{ from {{ opacity: 0; transform: translateY(22px); }} to {{ opacity: 1; transform: none; }} }}
</style>
{corps}
</svg>'''
    (out / 'chiffres.svg').write_text(svg, encoding='utf-8')

titre('titre-apropos.svg', '01', 'À propos', 'qui je suis, ce que je construis')
titre('titre-projets.svg', '02', 'Projets', 'mes applis et mon bureau')
titre('titre-stack.svg', '03', 'Stack', 'les outils de tous les jours')
titre('titre-chiffres.svg', '04', 'En chiffres', 'ce qui tourne déjà')
titre('titre-contact.svg', '05', 'Contact', 'on construit ensemble ?')
terminal()
contact()
chiffres()
print('ok')
