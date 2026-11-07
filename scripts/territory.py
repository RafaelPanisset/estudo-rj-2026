import csv,json,pathlib
P=pathlib.Path(__file__).resolve().parents[1];rs=list(csv.DictReader((P/'results/municipios.csv').open()))
def agg(xs):return {f:sum(int(r[f]) for r in xs) for f in ['DOUGLAS RUAS','EDUARDO PAES','validos','margem_ruas','aptos','abstencao']}
metro=[r for r in rs if r['regiao_analitica'] in ['Capital','Baixada Fluminense','Leste Fluminense'] or r['municipio']=='PETRÓPOLIS'];assert len(metro)==22
result={'metropolitana_22':agg(metro),'metropolitana_sem_capital':agg([r for r in metro if r['municipio']!='RIO DE JANEIRO']),'interior_fora_metropolitana':agg([r for r in rs if r not in metro]),'ruas_menos_presidente22':sum(int(r['DOUGLAS RUAS'])-int(r['presidente22_2026']) for r in rs),'municipios_ruas_supera_presidente22_absoluto':[(r['municipio'],int(r['DOUGLAS RUAS'])-int(r['presidente22_2026'])) for r in rs if int(r['DOUGLAS RUAS'])>int(r['presidente22_2026'])],'top10_margem_fora_capital':sum(int(r['margem_ruas']) for r in sorted(rs,key=lambda r:-int(r['margem_ruas']))[:10])}
(P/'results/testes-territoriais.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
reg=list(csv.DictReader((P/'results/regioes.csv').open()));s=json.loads((P/'results/resumo.json').read_text())
lines=['# Tabelas reproduzidas','', 'Percentuais entre válidos após retotalização; margem = Ruas menos Paes. Partição analítica descrita na análise.','', '| Região | Municípios | Ruas | Paes | Margem em votos | Abstenção |','|---|---:|---:|---:|---:|---:|']
for r in reg:lines.append(f'| {r["regiao"]} | {r["municipios"]} | {float(r["ruas_pct"]):.2f}% | {float(r["paes_pct"]):.2f}% | {int(r["margem_ruas"]):,} | {float(r["abstencao_pct"]):.2f}% |')
lines+=['','## Candidatos com votos válidos','', '| Nome | Número | Partido | Votos |','|---|---:|---|---:|']
for c in s['candidatos']:lines.append(f'| {c["nome"]} | {c["numero"]} | {c["partido"]} | {c["votos"]:,} |')
lines+=['','Anthony Garotinho (Republicanos, 10) recebeu 274.411 votos posteriormente anulados, conforme documentos judiciais/notícias oficiais; não aparece nas linhas de candidatos do snapshot munzona pós-retotalização. Não é uma nona votação válida.','', '## Maiores margens absolutas favoráveis a Ruas','', '| Município | Margem | Ruas entre válidos |','|---|---:|---:|']
for r in sorted(rs,key=lambda r:-int(r['margem_ruas']))[:15]:lines.append(f'| {r["municipio"]} | {int(r["margem_ruas"]):,} | {float(r["ruas_pct"]):.2f}% |')
(P/'results/TABELAS.md').write_text('\n'.join(lines)+'\n');print('Territorial tests and tables generated')
