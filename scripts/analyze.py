"""Descriptive audit. No individual vote-transfer estimates."""
import csv,json,collections,pathlib,unicodedata,hashlib
P=pathlib.Path(__file__).resolve().parents[1]
def read(f):return list(csv.DictReader((P/'raw'/f).open()))
def write(name,rows):
 with (P/'results'/name).open('w') as f:
  w=csv.DictWriter(f,list(rows[0]));w.writeheader();w.writerows(rows)
def norm(s):return ''.join(c for c in unicodedata.normalize('NFD',s.upper()) if not unicodedata.combining(c))
z=collections.defaultdict(collections.Counter);names={};candidates=collections.Counter();meta={}
for r in read('votacao-2026-RJ.csv'):
 assert r['CD_CARGO']=='3' and r['NR_TURNO']=='1' and r['ANO_ELEICAO']=='2026'
 k=(r['CD_MUNICIPIO'],r['NR_ZONA']);names[k[0]]=r['NM_MUNICIPIO']; n=r['NM_URNA_CANDIDATO']; v=int(r['QT_VOTOS_NOMINAIS_VALIDOS']);z[k][n]+=v;candidates[n]+=v;meta[n]=(r['NR_CANDIDATO'],r['SG_PARTIDO'],r['DS_SIT_TOT_TURNO'])
for r in read('detalhe-2026-RJ.csv'):
 assert r['CD_CARGO']=='3' and r['NR_TURNO']=='1'
 k=(r['CD_MUNICIPIO'],r['NR_ZONA'])
 for a,b in [('aptos','QT_APTOS'),('comparecimento','QT_COMPARECIMENTO'),('abstencao','QT_ABSTENCOES'),('validos','QT_TOTAL_VOTOS_VALIDOS'),('brancos','QT_VOTOS_BRANCOS'),('nulos','QT_TOTAL_VOTOS_NULOS'),('nulos_tecnicos','QT_VOTOS_NULOS_TECNICOS')]:z[k][a]+=int(r[b])
for k,v in z.items():
 assert sum(v[n] for n in candidates)==v['validos'],k
 assert v['aptos']==v['comparecimento']+v['abstencao'],k
 assert v['validos']+v['brancos']+v['nulos']==v['comparecimento'],k
municipal=collections.defaultdict(collections.Counter)
for (code,zone),v in z.items():municipal[code].update(v)
for r in read('votacao-2022-RJ.csv'):
 v=municipal[r['CD_MUNICIPIO']]; n=r['NM_URNA_CANDIDATO'];q=int(r['QT_VOTOS_NOMINAIS_VALIDOS'])
 if r['CD_CARGO']=='7':v['ruas_deputado_2022']+=q
 elif r['NR_TURNO']=='1':
  v['validos_governo_2022']+=q
  if 'CASTRO' in n:v['castro_2022']+=q
  if 'FREIXO' in n:v['freixo_2022']+=q
for year in [2022,2026]:
 for r in read(f'presidente-{year}-RJ.csv'):
  if r['NR_TURNO']!='1':continue
  v=municipal[r['CD_MUNICIPIO']];q=int(r['QT_VOTOS_NOMINAIS_VALIDOS']);v[f'validos_presidente_{year}']+=q
  if r['NR_CANDIDATO']=='22':v[f'presidente22_{year}']+=q
  if r['NR_CANDIDATO']=='13':v[f'presidente13_{year}']+=q
# Explicit analytical partition, not an assertion of a unique official regional definition.
groups={
'Capital':'Rio de Janeiro',
'Baixada Fluminense':'Belford Roxo;Duque de Caxias;Guapimirim;Itaguaí;Japeri;Magé;Mesquita;Nilópolis;Nova Iguaçu;Paracambi;Queimados;São João de Meriti;Seropédica',
'Leste Fluminense':'Niterói;São Gonçalo;Itaboraí;Maricá;Tanguá;Rio Bonito;Cachoeiras de Macacu',
'Norte':'Campos dos Goytacazes;Carapebus;Cardoso Moreira;Conceição de Macabu;Macaé;Quissamã;São Fidélis;São Francisco de Itabapoana;São João da Barra',
'Noroeste':'Aperibé;Bom Jesus do Itabapoana;Cambuci;Italva;Itaocara;Itaperuna;Laje do Muriaé;Miracema;Natividade;Porciúncula;Santo Antônio de Pádua;São José de Ubá;Varre-Sai',
'Serrana':'Bom Jardim;Cantagalo;Carmo;Cordeiro;Duas Barras;Macuco;Nova Friburgo;Petrópolis;Santa Maria Madalena;São José do Vale do Rio Preto;São Sebastião do Alto;Sumidouro;Teresópolis;Trajano de Moraes',
'Região dos Lagos e Baixadas Litorâneas':'Araruama;Armação dos Búzios;Arraial do Cabo;Cabo Frio;Casimiro de Abreu;Iguaba Grande;Rio das Ostras;São Pedro da Aldeia;Saquarema;Silva Jardim',
'Costa Verde':'Angra dos Reis;Mangaratiba;Paraty',
'Médio Paraíba':'Barra do Piraí;Barra Mansa;Itatiaia;Pinheiral;Piraí;Porto Real;Quatis;Resende;Rio Claro;Rio das Flores;Valença;Volta Redonda',
'Centro-Sul':'Areal;Comendador Levy Gasparian;Engenheiro Paulo de Frontin;Mendes;Miguel Pereira;Paraíba do Sul;Paty do Alferes;Sapucaia;Três Rios;Vassouras'}
lookup={norm(n):g for g,ns in groups.items() for n in ns.split(';')};assert len(lookup)==92
fields=['DOUGLAS RUAS','EDUARDO PAES','validos','aptos','comparecimento','abstencao','brancos','nulos','nulos_tecnicos','ruas_deputado_2022','castro_2022','freixo_2022','validos_governo_2022','presidente22_2026','presidente13_2026','validos_presidente_2026','presidente22_2022','presidente13_2022','validos_presidente_2022']
def summarize(v):
 d={f:v[f] for f in fields};d['margem_ruas']=v['DOUGLAS RUAS']-v['EDUARDO PAES'];d['ruas_pct']=100*v['DOUGLAS RUAS']/v['validos'];d['paes_pct']=100*v['EDUARDO PAES']/v['validos'];d['abstencao_pct']=100*v['abstencao']/v['aptos'];return d
rows=[{'codigo_tse':code,'municipio':names[code],'regiao_analitica':lookup[norm(names[code])],**summarize(v)} for code,v in sorted(municipal.items())]
write('municipios.csv',rows)
write('zonas.csv',[{'codigo_tse':c,'municipio':names[c],'zona':zone,**{f:v[f] for f in fields[:9]},'margem_ruas':v['DOUGLAS RUAS']-v['EDUARDO PAES']} for (c,zone),v in sorted(z.items())])
regional=[]
for group in groups:
 vals=collections.Counter()
 for code,v in municipal.items():
  if lookup[norm(names[code])]==group:vals.update(v)
 regional.append({'regiao':group,'municipios':sum(r['regiao_analitica']==group for r in rows),**summarize(vals)})
write('regioes.csv',regional)
total=collections.Counter()
for v in municipal.values():total.update(v)
capital=municipal['60011'];rest=total-capital
summary={'estado':summarize(total),'capital':summarize(capital),'fora_capital':summarize(rest),'municipios':len(municipal),'zonas_municipais':len(z),'municipios_ruas_vence':sum(r['margem_ruas']>0 for r in rows),'zonas_capital_ruas_vence':sum(c=='60011' and v['DOUGLAS RUAS']>v['EDUARDO PAES'] for (c,_),v in z.items()),'zonas_capital':sum(c=='60011' for c,_ in z),'ruas_base_2022_sao_goncalo':next(v['ruas_deputado_2022'] for c,v in municipal.items() if names[c]=='SÃO GONÇALO'),'candidatos':[{'nome':n,'numero':meta[n][0],'partido':meta[n][1],'situacao':meta[n][2],'votos':v} for n,v in candidates.most_common()]}
summary['retotalizacao']={'garotinho_votos_documentados':274411,'denominador_antes':total['validos']+274411,'denominador_depois':total['validos'],'ruas_pct_antes':100*total['DOUGLAS RUAS']/(total['validos']+274411),'votos_acima_metade_depois':total['DOUGLAS RUAS']-total['validos']/2,'margem_inalterada':total['DOUGLAS RUAS']-total['EDUARDO PAES']}
assert total['validos']==8394627 and total['DOUGLAS RUAS']==4271199 and total['EDUARDO PAES']==3706984
assert total['nulos_tecnicos']==274411
(P/'results/resumo.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
(P/'results/verificacao.json').write_text(json.dumps({'checks':['candidate votes = valid votes in all municipal-zones','eligible = turnout + abstention in all municipal-zones','valid + blank + null = turnout in all municipal-zones','92 municipalities uniquely partitioned','state totals reconcile with TRE retabulation'],'sha256':{str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted((P/'raw').glob('*.csv'))}},indent=2))
print(json.dumps(summary,ensure_ascii=False,indent=2))
