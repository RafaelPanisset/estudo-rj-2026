"""Extract independently reproducible RJ snapshots from the reference project's TSE archives."""
import csv,io,zipfile,json,hashlib,pathlib,datetime
P=pathlib.Path(__file__).resolve().parents[1]; source=P.parent/'analise-eleitoral-2026'
manifest=[]
for filename,year,kind in [('votacao.zip',2026,'votacao'),('detalhe.zip',2026,'detalhe'),('votacao-2022.zip',2022,'votacao')]:
 archive=source/'raw'/filename
 z=zipfile.ZipFile(archive); member=next(n for n in z.namelist() if n.endswith('_RJ.csv'))
 out=P/'raw'/f'{kind}-{year}-RJ.csv'
 with io.TextIOWrapper(z.open(member),encoding='latin1') as f,out.open('w') as g:
  reader=csv.DictReader(f,delimiter=';');writer=csv.DictWriter(g,reader.fieldnames);writer.writeheader()
  for row in reader:
   if row['CD_CARGO']=='3' or (kind=='votacao' and year==2022 and row['CD_CARGO']=='7' and 'DOUGLAS RUAS' in row['NM_URNA_CANDIDATO']):writer.writerow(row)
 # presidential results reside in BR, not RJ
 if kind=='votacao':
  memberbr=next(n for n in z.namelist() if n.endswith('_BR.csv')); op=P/'raw'/f'presidente-{year}-RJ.csv'
  with io.TextIOWrapper(z.open(memberbr),encoding='latin1') as f,op.open('w') as g:
   reader=csv.DictReader(f,delimiter=';');writer=csv.DictWriter(g,reader.fieldnames);writer.writeheader()
   for row in reader:
    if row['SG_UF']=='RJ':writer.writerow(row)
  manifest.append({'file':str(op.relative_to(P)),'member':memberbr,'parent_archive':filename,'sha256':hashlib.sha256(op.read_bytes()).hexdigest(),'transformation':'SG_UF=RJ; UTF-8 comma CSV'})
 original=next(x for x in json.loads((source/'data/source-manifest.json').read_text()) if x['file']==filename)
 sha=hashlib.file_digest(archive.open('rb'),'sha256').hexdigest()
 if sha!=original['sha256']:raise ValueError('Archive hash mismatch')
 manifest.append({'file':str(out.relative_to(P)),'member':member,'parent_archive':filename,'parent_sha256':sha,'url':original['url'],'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'obtained_original':'2026-11-01 (reference project; filesystem and manifest)','extracted_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'transformation':'CD_CARGO=3; additionally Douglas Ruas state deputy 2022; UTF-8 comma CSV'})
(P/'data/source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('Snapshots extracted and parent hashes verified')
