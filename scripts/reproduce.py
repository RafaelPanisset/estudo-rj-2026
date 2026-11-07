"""Offline reproduction from preserved snapshots, no third-party dependencies."""
import pathlib,subprocess,sys,json,hashlib,platform,datetime
P=pathlib.Path(__file__).resolve().parents[1]
if not __debug__:raise RuntimeError('Não use python -O nem PYTHONOPTIMIZE: as verificações precisam permanecer ativas.')
manifest=json.loads((P/'data/snapshot-manifest.json').read_text())
missing=[r['file'] for r in manifest if not (P/r['file']).exists()]
if missing:raise FileNotFoundError(
 'Insumo ausente: '+', '.join(missing)+'. A reprodução exige os arquivos do manifesto, inclusive raw/secoes-RJ.zip '
 '(296.106.129 bytes, SHA-256 ec93c020ae1f0088216de92e5acc5d3211aefaf1fa589b961132bbf471ee3cf5). '
 'Restaure o asset da release privada dados-v1 conforme review-instructions/COMO-USAR.md. A exigência de integridade foi mantida.')
for r in manifest:
 f=P/r['file'];actual=hashlib.file_digest(f.open('rb'),'sha256').hexdigest()
 if actual!=r['sha256']:raise ValueError(f'Snapshot changed: {f}')
(P/'results').mkdir(parents=True, exist_ok=True); (P/'figures').mkdir(parents=True, exist_ok=True)
def digest_dir(folder):
 return {str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(folder.glob('*')) if f.is_file()}
before_results=digest_dir(P/'results'); before_figures=digest_dir(P/'figures')
for script in ['analyze.py','sections.py','maps.py','polls.py','territory.py']:
 result=subprocess.run([sys.executable,str(P/'scripts'/script)],capture_output=True,text=True)
 if result.returncode:raise RuntimeError(script+'\n'+result.stdout+'\n'+result.stderr)
 print(script,'OK')
# Markdown local links and SVG syntax
import re,xml.etree.ElementTree as ET
broken=[]
for f in P.rglob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if '://' in target or target.startswith('#'):continue
  path=target.split('#')[0]
  if path and (f.parent/path).resolve()!=(P/'results/reproducao.json').resolve() and not (f.parent/path).exists():broken.append((str(f),target))
if broken:raise ValueError(broken)
for f in (P/'figures').glob('*.svg'):ET.parse(f)
record={'executed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':'python3 scripts/reproduce.py','python':sys.version,'platform':platform.platform(),'optimize_flag':sys.flags.optimize,'offline':'não medido; os scripts chamados não abrem rede','snapshot_files_verified':len(manifest),'inputs_sha256':{r['file']:r['sha256'] for r in manifest},'scripts':['analyze','sections','maps','polls','territory'],'local_links':'all exist','svg_xml':'valid','results_sha256_before':before_results,'figures_sha256_before':before_figures,'results_sha256':{k:v for k,v in digest_dir(P/'results').items() if not k.endswith('reproducao.json')},'figures_sha256':digest_dir(P/'figures')}
(P/'results/reproducao.json').write_text(json.dumps(record,ensure_ascii=False,indent=2));print('Offline reproduction and integrity checks passed')
