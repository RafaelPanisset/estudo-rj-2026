import json,csv,pathlib,unicodedata,html
P=pathlib.Path(__file__).resolve().parents[1]
def norm(s):return ''.join(c for c in unicodedata.normalize('NFD',s.upper()) if not unicodedata.combining(c))
rows=list(csv.DictReader((P/'results/municipios.csv').open()));ibge=json.loads((P/'raw/ibge-municipios.json').read_text());geo=json.loads((P/'raw/ibge-malha.json').read_text())
byname={norm(r['municipio']):r for r in rows};byid={str(m['id']):byname[norm(m['nome'])] for m in ibge};assert len(byid)==92
with (P/'data/correspondencia-tse-ibge.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['codigo_tse','codigo_ibge','municipio','metodo']);w.writerows((r['codigo_tse'],i,r['municipio'],'nome normalizado univoco; 92/92') for i,r in byid.items())
for kind,title in [('margem','Margem Ruas − Paes (% dos votos válidos)'),('abstencao','Abstenção (% dos aptos)')]:
 svg=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680"><rect width="1100" height="680" fill="#fafafa"/>',f'<text x="30" y="35" font-family="sans-serif" font-size="23">RJ 2026 · {title}</text>']
 for feature in geo['features']:
  r=byid[feature['properties']['codarea']];value=float(r['ruas_pct'])-float(r['paes_pct']) if kind=='margem' else float(r['abstencao_pct'])
  if kind=='margem':
   t=min(abs(value)/50,1);base=(38,100,145) if value>=0 else (177,86,34)
  else:t=min(max((value-10)/25,0),1);base=(80,55,140)
  color='#'+''.join(f'{round(245+(x-245)*t):02x}' for x in base)
  geometry=feature['geometry'];polys=geometry['coordinates'] if geometry['type']=='MultiPolygon' else [geometry['coordinates']]
  d=' '.join('M'+' L'.join(f'{50+(lon+44.9)*235:.1f},{70+(-20.7-lat)*185:.1f}' for lon,lat in ring)+' Z' for poly in polys for ring in poly)
  svg.append(f'<path d="{d}" fill="{color}" stroke="#777" stroke-width=".5" fill-rule="evenodd"><title>{html.escape(r["municipio"])}: {value:.2f}%</title></path>')
 legend='Laranja: Paes · Branco: equilíbrio · Azul: Ruas. Saturação: até 50 p.p.' if kind=='margem' else 'Branco → roxo: 10% → 35% de abstenção.'
 svg.extend([f'<text x="30" y="610" font-family="sans-serif" font-size="17">{legend}</text>','<text x="30" y="640" font-family="sans-serif" font-size="14">TSE, snapshot nov/2026; malha municipal IBGE simplificada. Área não representa quantidade de votos.</text>','</svg>'])
 (P/'figures'/f'{kind}.svg').write_text('\n'.join(svg))
print('92 municipalities matched, two maps generated')
