"""Génère les SVG animés du README de profil (portfolio/readme)."""
import base64, pathlib, sys
racine = pathlib.Path(sys.argv[1])
img = lambda n: 'data:image/webp;base64,' + base64.b64encode((racine / 'images' / n).read_bytes()).decode()
out = racine / 'readme'
POLICE = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"

# 1. Bannière
banniere = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="360" viewBox="0 0 1200 360">
<style>
  .b {{ animation: bouge 14s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
  .b2 {{ animation-duration: 18s; animation-direction: reverse; }}
  @keyframes bouge {{ 50% {{ transform: translate(60px, -30px) scale(1.15); }} }}
  .titre {{ font: 800 84px {POLICE}; letter-spacing: -3px; }}
  .sous {{ font: 500 24px {POLICE}; fill: #9a9ab0; }}
  .petit {{ font: 600 15px {POLICE}; fill: #9a9ab0; letter-spacing: 3px; }}
  .entre {{ opacity: 0; animation: entre 1s cubic-bezier(.22,1,.36,1) forwards; }}
  .d1 {{ animation-delay: .2s; }} .d2 {{ animation-delay: .45s; }} .d3 {{ animation-delay: .7s; }}
  @keyframes entre {{ from {{ opacity: 0; transform: translateY(20px); }} to {{ opacity: 1; transform: none; }} }}
  .mot {{ opacity: 0; animation: mots 12s infinite; }}
  .m2 {{ animation-delay: 3s; }} .m3 {{ animation-delay: 6s; }} .m4 {{ animation-delay: 9s; }}
  @keyframes mots {{ 0% {{ opacity: 0; transform: translateY(14px); }} 4%, 22% {{ opacity: 1; transform: none; }} 26%, 100% {{ opacity: 0; transform: translateY(-14px); }} }}
  .anneau {{ animation: tourne 6s linear infinite; transform-origin: 960px 180px; }}
  .orbite {{ animation: tourne 30s linear infinite; transform-origin: 960px 180px; }}
  @keyframes tourne {{ to {{ transform: rotate(360deg); }} }}
  .flotte {{ animation: flotte 6s ease-in-out infinite; }}
  @keyframes flotte {{ 50% {{ transform: translateY(-8px); }} }}
  .aura {{ animation: respire 4s ease-in-out infinite; transform-origin: 960px 180px; }}
  @keyframes respire {{ 50% {{ opacity: .45; transform: scale(1.12); }} }}
  .point {{ animation: pulse 2s ease-out infinite; transform-origin: 70px 74px; }}
  @keyframes pulse {{ 0% {{ opacity: .7; transform: scale(1); }} 100% {{ opacity: 0; transform: scale(3); }} }}
</style>
<defs>
  <linearGradient id="deg" x1="0" x2="1">
    <stop offset="0" stop-color="#3b82f6"/><stop offset=".45" stop-color="#f26b3a"/><stop offset=".75" stop-color="#e9a91b"/><stop offset="1" stop-color="#3b82f6"/>
    <animate attributeName="x1" values="0;-1;0" dur="6s" repeatCount="indefinite"/><animate attributeName="x2" values="1;0;1" dur="6s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="ring" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3b82f6"/><stop offset=".5" stop-color="#3b82f6" stop-opacity="0"/><stop offset="1" stop-color="#f26b3a"/></linearGradient>
  <radialGradient id="aura"><stop offset="0" stop-color="#3b82f6" stop-opacity=".55"/><stop offset="1" stop-color="#3b82f6" stop-opacity="0"/></radialGradient>
  <filter id="flou" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
  <clipPath id="rond"><circle cx="960" cy="180" r="118"/></clipPath>
  <clipPath id="cadre"><rect width="1200" height="360" rx="24"/></clipPath>
</defs>
<g clip-path="url(#cadre)">
  <rect width="1200" height="360" fill="#0b0b12"/>
  <circle class="b" cx="1080" cy="40" r="170" fill="#3b82f6" opacity=".35" filter="url(#flou)"/>
  <circle class="b b2" cx="160" cy="360" r="170" fill="#7a2a63" opacity=".6" filter="url(#flou)"/>
  <circle class="b" cx="600" cy="200" r="110" fill="#f26b3a" opacity=".18" filter="url(#flou)"/>
  <g class="entre d1">
    <circle class="point" cx="70" cy="74" r="5" fill="#34d399"/><circle cx="70" cy="74" r="5" fill="#34d399"/>
    <text class="petit" x="86" y="79">DÉVELOPPEUR WEB ET MOBILE · GOMA, RDC</text>
  </g>
  <g class="entre d2"><text class="titre" x="60" y="178" fill="#f4f4f7">Salut, je suis</text>
  <text class="titre" x="60" y="262" fill="url(#deg)">Iro007.</text></g>
  <g class="entre d3">
    <text class="sous" x="60" y="318">Je construis</text>
    <text class="sous mot" x="200" y="318" style="fill:#f4f4f7">des marketplaces.</text>
    <text class="sous mot m2" x="200" y="318" style="fill:#f4f4f7">des messageries.</text>
    <text class="sous mot m3" x="200" y="318" style="fill:#f4f4f7">des applis mobiles.</text>
    <text class="sous mot m4" x="200" y="318" style="fill:#f4f4f7">pour Goma.</text>
  </g>
  <circle class="aura" cx="960" cy="180" r="150" fill="url(#aura)"/>
  <g class="orbite"><circle cx="960" cy="180" r="150" fill="none" stroke="#fff" stroke-opacity=".1" stroke-dasharray="4 8"/>
    <circle cx="810" cy="180" r="7" fill="#f26b3a"/><circle cx="1110" cy="180" r="5" fill="#3b82f6"/></g>
  <g class="flotte">
    <image href="{img('photo.webp')}" x="842" y="62" width="236" height="236" clip-path="url(#rond)"/>
    <circle class="anneau" cx="960" cy="180" r="124" fill="none" stroke="url(#ring)" stroke-width="4"/>
  </g>
</g>
</svg>'''
(out / 'banniere.svg').write_text(banniere, encoding='utf-8')

# 2. Cartes projet
def carte(nom, fichier, tag, accent, lueur1, lueur2, lignes, puces):
    texte = ''.join(f'<text class="txt" x="56" y="{232 + 30*i}">{l}</text>' for i, l in enumerate(lignes))
    x, chips = 56, ''
    for p in puces:
        w = 18 + len(p) * 9
        chips += f'<rect x="{x}" y="372" width="{w}" height="32" rx="8" fill="none" stroke="#fff" stroke-opacity=".12"/><text class="chip" x="{x + w/2}" y="393" text-anchor="middle">{p}</text>'
        x += w + 8
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="480" viewBox="0 0 1200 480">
<style>
  .nom {{ font: 800 64px {POLICE}; letter-spacing: -2px; fill: #f4f4f7; }}
  .tag {{ font: 700 14px {POLICE}; letter-spacing: 2px; fill: {accent}; }}
  .txt {{ font: 400 20px {POLICE}; fill: #b4b4c6; }}
  .chip {{ font: 500 15px {POLICE}; fill: #9a9ab0; }}
  .cta {{ font: 700 17px {POLICE}; fill: #0b0b12; }}
  .gauche {{ opacity: 0; animation: entre 1s cubic-bezier(.22,1,.36,1) .1s forwards; }}
  .droite {{ opacity: 0; animation: entre 1.2s cubic-bezier(.22,1,.36,1) .3s forwards; }}
  @keyframes entre {{ from {{ opacity: 0; transform: translateY(24px); }} to {{ opacity: 1; transform: none; }} }}
  .tel {{ animation: flotte 6s ease-in-out infinite; }}
  .ordi {{ animation: flotte 8s ease-in-out infinite reverse; }}
  @keyframes flotte {{ 50% {{ transform: translateY(-10px); }} }}
  .lueur {{ animation: respire 5s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
  @keyframes respire {{ 50% {{ opacity: .35; transform: scale(1.1); }} }}
  .reflet {{ animation: reflet 5s ease-in-out infinite; }}
  @keyframes reflet {{ 0%, 60% {{ transform: translateX(-500px); }} 100% {{ transform: translateX(800px); }} }}
  .fleche {{ animation: fleche 1.6s ease-in-out infinite; }}
  @keyframes fleche {{ 50% {{ transform: translateX(5px); }} }}
</style>
<defs>
  <linearGradient id="l" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{lueur1}"/><stop offset="1" stop-color="{lueur2}"/></linearGradient>
  <linearGradient id="r" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".18"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <filter id="flou" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="50"/></filter>
  <clipPath id="cadre"><rect width="1200" height="480" rx="24"/></clipPath>
  <clipPath id="ecran"><rect x="620" y="96" width="480" height="300" rx="12"/></clipPath>
  <clipPath id="telc"><rect x="1010" y="170" width="130" height="260" rx="20"/></clipPath>
</defs>
<g clip-path="url(#cadre)">
  <rect width="1200" height="480" fill="#0f0f18"/>
  <rect width="1199" height="479" x=".5" y=".5" rx="24" fill="none" stroke="#fff" stroke-opacity=".08"/>
  <g class="gauche">
    <text class="tag" x="56" y="92">{tag}</text>
    <text class="nom" x="52" y="168">{nom}</text>
    {texte}
    {chips}
  </g>
  <rect class="lueur" x="660" y="120" width="420" height="300" rx="60" fill="url(#l)" opacity=".55" filter="url(#flou)"/>
  <g class="droite">
    <g class="ordi">
      <rect x="620" y="70" width="480" height="326" rx="12" fill="#1c1c28"/>
      <circle cx="638" cy="83" r="5" fill="#ff5f57"/><circle cx="654" cy="83" r="5" fill="#febc2e"/><circle cx="670" cy="83" r="5" fill="#28c840"/>
      <image href="{img(fichier + '-ordi.webp')}" x="620" y="96" width="480" height="300" preserveAspectRatio="xMidYMin slice" clip-path="url(#ecran)"/>
      <g clip-path="url(#ecran)"><rect class="reflet" x="620" y="70" width="160" height="326" fill="url(#r)"/></g>
    </g>
    <g class="tel">
      <rect x="1004" y="164" width="142" height="272" rx="24" fill="#1c1c28"/>
      <image href="{img(fichier + '-tel.webp')}" x="1010" y="170" width="130" height="260" preserveAspectRatio="xMidYMin slice" clip-path="url(#telc)"/>
    </g>
  </g>
</g>
</svg>'''

(out / 'rheeka.svg').write_text(carte('RHEEKA', 'rheeka', '01 · MARKETPLACE · RHEEKA.COM', '#f26b3a', '#f26b3a', '#14213d',
    ['Commande. Paie. Reçois.', "L'argent reste bloqué jusqu'à ce que tu", 'donnes ton code au livreur.', 'Personne n\'est payé avant la livraison.'],
    ['React', 'TypeScript', 'Supabase', 'PostGIS', 'Android']), encoding='utf-8')
(out / 'kitty.svg').write_text(carte('Kitty', 'kitty', '02 · MESSAGERIE', '#8fb0ff', '#9b5de5', '#5b82dd',
    ['Écris. Appelle. Partage.', 'Appels vidéo, groupes, statuts de 24 h,', 'sondages, position, 72 stickers maison.', 'La confidentialité est tenue par la base.'],
    ['React', 'TypeScript', 'Realtime', 'LiveKit', 'Web Push']), encoding='utf-8')

# 3. Bandeau des technologies qui défile
techs = ['React', 'TypeScript', 'Flutter', 'Supabase', 'PostgreSQL', 'PostGIS', 'Vite', 'MapLibre', 'LiveKit', 'Web Push', 'Vercel', 'Android']
x, items = 0, ''
for t in techs * 2:
    items += f'<text x="{x}" y="47">{t}</text><text class="e" x="{x + len(t)*15 + 22}" y="44">✦</text>'
    x += len(t) * 15 + 70
moitie = x // 2
bandeau = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="72" viewBox="0 0 1200 72">
<style>
  text {{ font: 700 26px {POLICE}; fill: #f4f4f7; fill-opacity: .4; }}
  .e {{ font-size: 15px; fill: #f26b3a; fill-opacity: .8; }}
  .piste {{ animation: glisse 28s linear infinite; }}
  @keyframes glisse {{ to {{ transform: translateX(-{moitie}px); }} }}
</style>
<defs><linearGradient id="f"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".12" stop-color="#fff"/><stop offset=".88" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<mask id="m"><rect width="1200" height="72" fill="url(#f)"/></mask></defs>
<rect width="1200" height="72" rx="16" fill="#0b0b12"/>
<g mask="url(#m)"><g class="piste">{items}</g></g>
</svg>'''
(out / 'technos.svg').write_text(bandeau, encoding='utf-8')
print('ok', [p.name + ' ' + str(p.stat().st_size // 1024) + ' Ko' for p in out.iterdir()])
