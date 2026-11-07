"""Extract gubernatorial section votes, retaining original vote labels and no voter data."""
import pathlib,zipfile,csv,io,collections,json,hashlib
P=pathlib.Path(__file__).resolve().parents[1]
def require(cond, msg='verificacao por secao falhou'):
    if not cond: raise RuntimeError(msg)
(P/'results').mkdir(parents=True, exist_ok=True)
archive=P/'raw/secoes-RJ.zip';out=P/'raw/secoes-governador.csv'
if not out.exists() and not archive.exists():
    raise FileNotFoundError('Faltam raw/secoes-governador.csv e raw/secoes-RJ.zip. Restaure o ZIP da release dados-v1 conforme review-instructions/COMO-USAR.md. A exigência do arquivo foi mantida.')
if not out.exists():
 z=zipfile.ZipFile(archive);member=next(n for n in z.namelist() if n.endswith('_RJ.csv'))
 with z.open(member) as f,out.open('w') as g:
  reader=csv.DictReader(io.TextIOWrapper(f,encoding='latin1'),delimiter=';');fields=['CD_MUNICIPIO','NR_ZONA','NR_SECAO','NR_VOTAVEL','NM_VOTAVEL','QT_VOTOS'];w=csv.DictWriter(g,fields);w.writeheader()
  for r in reader:
   if r['CD_CARGO']=='3' and r['NR_TURNO']=='1':w.writerow({k:r[k] for k in fields})
counts=collections.Counter();sections=collections.defaultdict(collections.Counter);labels={};zones=collections.defaultdict(collections.Counter)
for r in csv.DictReader(out.open()):
 n=r['NR_VOTAVEL'];v=int(r['QT_VOTOS']);counts[n]+=v;labels[n]=r['NM_VOTAVEL'];k=(r['CD_MUNICIPIO'],r['NR_ZONA'],r['NR_SECAO']);sections[k][n]+=v;zones[k[:2]][n]+=v
require(counts['22']==4271199 and counts['55']==3706984, 'totais de secao')
errors=[]
for r in csv.DictReader((P/'results/zonas.csv').open()):
 k=(r['codigo_tse'],r['zona'])
 for n,f in [('22','DOUGLAS RUAS'),('55','EDUARDO PAES'),('10','nulos_tecnicos'),('95','brancos')]:
  if zones[k][n]!=int(r[f]):errors.append((k,n,'zonas'))
det={}
for r in csv.DictReader((P/'raw/detalhe-2026-RJ.csv').open()):
 require(r['CD_CARGO']=='3' and r['NR_TURNO']=='1', 'filtro do detalhe')
 det[(r['CD_MUNICIPIO'],r['NR_ZONA'])]=r
cand=collections.defaultdict(collections.Counter)
for r in csv.DictReader((P/'raw/votacao-2026-RJ.csv').open()):
 require(r['CD_CARGO']=='3' and r['NR_TURNO']=='1', 'filtro da votacao')
 cand[(r['CD_MUNICIPIO'],r['NR_ZONA'])][r['NR_CANDIDATO']]+=int(r['QT_VOTOS_NOMINAIS_VALIDOS'])
nsec=collections.Counter()
for k in sections:nsec[k[:2]]+=1
if set(zones)!=set(det):errors.append(('chaves',set(zones)^set(det)))
for k,v in zones.items():
 d=det[k]
 if v['95']!=int(d['QT_VOTOS_BRANCOS']) or v['10']!=int(d['QT_VOTOS_NULOS_TECNICOS']) or v['96']!=int(d['QT_VOTOS_NULOS']):errors.append((k,'codigos-especiais'))
 if sum(v.values())!=int(d['QT_COMPARECIMENTO']):errors.append((k,'comparecimento'))
 if nsec[k]!=int(d['QT_SECOES_PRINCIPAIS']):errors.append((k,'secoes',nsec[k],d['QT_SECOES_PRINCIPAIS']))
 for num,votes in list(cand[k].items())+[(n,v[n]) for n in v if n not in ('95','96','10')]:
  if v[num]!=cand[k][num]:errors.append((k,num))
require(not errors, errors)
with (P/'results/secoes.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['codigo_tse','zona','secao','ruas','paes','anthony_garotinho','brancos','nulos_urna','margem_ruas']);w.writerows((*k,v['22'],v['55'],v['10'],v['95'],v['96'],v['22']-v['55']) for k,v in sorted(sections.items()))
report={'secoes':len(sections),'votos_por_codigo':[{'numero':n,'rotulo':labels[n],'votos':v} for n,v in counts.most_common()],'ruas_vence':sum(v['22']>v['55'] for v in sections.values()),'paes_vence':sum(v['55']>v['22'] for v in sections.values()),'empates':sum(v['55']==v['22'] for v in sections.values()),'reconciliacao_zonas':'183 zonas: todos os códigos de votável, brancos, nulos de urna, nulos técnicos, comparecimento e seções principais, 0 divergências','source_sha256':hashlib.sha256(out.read_bytes()).hexdigest()}
(P/'results/secoes-resumo.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2))
