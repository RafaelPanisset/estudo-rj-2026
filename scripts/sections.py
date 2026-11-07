"""Extract gubernatorial section votes, retaining original vote labels and no voter data."""
import pathlib,zipfile,csv,io,collections,json,hashlib
P=pathlib.Path(__file__).resolve().parents[1];archive=P/'raw/secoes-RJ.zip';out=P/'raw/secoes-governador.csv'
if not out.exists():
 z=zipfile.ZipFile(archive);member=next(n for n in z.namelist() if n.endswith('_RJ.csv'))
 with z.open(member) as f,out.open('w') as g:
  reader=csv.DictReader(io.TextIOWrapper(f,encoding='latin1'),delimiter=';');fields=['CD_MUNICIPIO','NR_ZONA','NR_SECAO','NR_VOTAVEL','NM_VOTAVEL','QT_VOTOS'];w=csv.DictWriter(g,fields);w.writeheader()
  for r in reader:
   if r['CD_CARGO']=='3' and r['NR_TURNO']=='1':w.writerow({k:r[k] for k in fields})
counts=collections.Counter();sections=collections.defaultdict(collections.Counter);labels={};zones=collections.defaultdict(collections.Counter)
for r in csv.DictReader(out.open()):
 n=r['NR_VOTAVEL'];v=int(r['QT_VOTOS']);counts[n]+=v;labels[n]=r['NM_VOTAVEL'];k=(r['CD_MUNICIPIO'],r['NR_ZONA'],r['NR_SECAO']);sections[k][n]+=v;zones[k[:2]][n]+=v
assert counts['22']==4271199 and counts['55']==3706984
errors=[]
for r in csv.DictReader((P/'results/zonas.csv').open()):
 k=(r['codigo_tse'],r['zona'])
 for n,f in [('22','DOUGLAS RUAS'),('55','EDUARDO PAES'),('10','nulos_tecnicos'),('95','brancos')]:
  if zones[k][n]!=int(r[f]):errors.append((k,n))
assert not errors,errors
with (P/'results/secoes.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['codigo_tse','zona','secao','ruas','paes','anthony_garotinho','brancos','nulos_urna','margem_ruas']);w.writerows((*k,v['22'],v['55'],v['10'],v['95'],v['96'],v['22']-v['55']) for k,v in sorted(sections.items()))
report={'secoes':len(sections),'votos_por_codigo':[{'numero':n,'rotulo':labels[n],'votos':v} for n,v in counts.most_common()],'ruas_vence':sum(v['22']>v['55'] for v in sections.values()),'paes_vence':sum(v['55']>v['22'] for v in sections.values()),'empates':sum(v['55']==v['22'] for v in sections.values()),'reconciliacao_zonas':'Ruas, Paes, Anthony vs technical null and blanks: 183 municipal-zones matched','source_sha256':hashlib.sha256(out.read_bytes()).hexdigest()}
(P/'results/secoes-resumo.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2))
