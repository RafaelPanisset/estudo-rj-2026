import csv,json,pathlib
P=pathlib.Path(__file__).resolve().parents[1];rows=list(csv.DictReader((P/'data/pesquisas.csv').open()))
out=[]
for r in rows:
 if r['denominador']!='validos':continue
 denom=8669038 if r['cenario']=='com Garotinho' else 8394627
 p=3706984/denom*100;d=4271199/denom*100
 out.append({'instituto':r['instituto'],'campo_fim':r['campo_fim'],'cenario':r['cenario'],'margem_pesquisa_paes':float(r['paes'])-float(r['ruas']),'margem_resultado_paes':p-d,'diferenca_margens_pp':float(r['paes'])-float(r['ruas'])-(p-d),'nota':'Diferença pesquisa-resultado; não mede erro amostral puro nem mudança individual.'})
(P/'results/pesquisas-confronto.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
svg=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 450"><rect width="900" height="450" fill="white"/><g font-family="sans-serif"><text x="30" y="30" font-size="22">Datafolha · intenção estimulada total, com Garotinho</text>']
a=[r for r in rows if r['instituto']=='Datafolha' and r['denominador']=='total']
for field,color in [('paes','#ad5622'),('ruas','#266491'),('garotinho','#666')]:
 points=' '.join(f'{100+i*210},{350-float(r[field])*6}' for i,r in enumerate(a));svg.append(f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="3"/>')
 for i,r in enumerate(a):svg.append(f'<text x="{100+i*210}" y="{340-float(r[field])*6}" fill="{color}">{r[field]}%</text>')
 svg.append(f'<text x="760" y="{350-float(a[-1][field])*6}" fill="{color}">{field}</text>')
for i,r in enumerate(a):svg.append(f'<text x="{70+i*210}" y="380">{r["campo_fim"][5:]}</text>')
svg.append('<text x="30" y="420">Datas: fim do campo. Espaçamento por onda; não é curva diária nem probabilidade de vitória.</text></g></svg>');(P/'figures/pesquisas.svg').write_text('\n'.join(svg))
print('Poll comparisons generated')
