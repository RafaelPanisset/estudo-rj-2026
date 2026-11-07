"""Offline reproduction from preserved snapshots, no third-party dependencies."""
import pathlib,subprocess,sys,json,hashlib,platform
P=pathlib.Path(__file__).resolve().parents[1]
if not __debug__:raise RuntimeError('Do not use python -O; audit assertions must remain enabled')
manifest=json.loads((P/'data/snapshot-manifest.json').read_text())
for r in manifest:
 f=P/r['file'];actual=hashlib.file_digest(f.open('rb'),'sha256').hexdigest()
 if actual!=r['sha256']:raise ValueError(f'Snapshot changed: {f}')
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
record={'python':sys.version,'platform':platform.platform(),'offline':True,'snapshot_files_verified':len(manifest),'scripts':['analyze','sections','maps','polls','territory'],'local_links':'all exist','svg_xml':'valid','results_sha256':{str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted((P/'results').glob('*')) if f.is_file() and f.name!='reproducao.json'}}
(P/'results/reproducao.json').write_text(json.dumps(record,ensure_ascii=False,indent=2));print('Offline reproduction and integrity checks passed')
