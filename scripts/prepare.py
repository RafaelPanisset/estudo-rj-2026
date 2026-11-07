"""Extract RJ snapshots from the reference project's TSE archives.

Optional acquisition step. Reproduction of the published calculations does not
call this script and does not need the neighboring project.
"""
import csv, io, json, hashlib, pathlib, datetime, shutil, zipfile
P = pathlib.Path(__file__).resolve().parents[1]
source = P.parent / 'analise-eleitoral-2026'
if not (source / 'data/source-manifest.json').exists():
    raise FileNotFoundError(
        f'Projeto vizinho ausente em {source}. prepare.py só refaz a extração herdada; '
        'a reprodução dos cálculos não depende dele.'
    )
parent_manifest = json.loads((source / 'data/source-manifest.json').read_text())

def parent_of(filename):
    original = next(x for x in parent_manifest if x['file'] == filename)
    archive = source / 'raw' / filename
    if not archive.exists():
        raise FileNotFoundError(f'ZIP pai ausente: {archive}. Nenhum recorte foi alterado.')
    sha = hashlib.file_digest(archive.open('rb'), 'sha256').hexdigest()
    if sha != original['sha256']:
        raise ValueError(f'Hash do ZIP pai diverge antes da extracao: {filename}')
    return archive, sha, original

manifest = []
obtained = '2026-11-01 (reference project; filesystem and manifest)'
for filename, year, kind in [('votacao.zip', 2026, 'votacao'), ('detalhe.zip', 2026, 'detalhe'), ('votacao-2022.zip', 2022, 'votacao')]:
    archive, sha, original = parent_of(filename)
    z = zipfile.ZipFile(archive)
    member = next(n for n in z.namelist() if n.endswith('_RJ.csv'))
    out = P / 'raw' / f'{kind}-{year}-RJ.csv'
    with io.TextIOWrapper(z.open(member), encoding='latin1') as f, out.open('w') as g:
        reader = csv.DictReader(f, delimiter=';')
        writer = csv.DictWriter(g, reader.fieldnames)
        writer.writeheader()
        for row in reader:
            deputy = kind == 'votacao' and year == 2022 and row['CD_CARGO'] == '7' and 'DOUGLAS RUAS' in row['NM_URNA_CANDIDATO']
            if row['CD_CARGO'] == '3' or deputy:
                writer.writerow(row)
    transformation = 'CD_CARGO=3; UTF-8 comma CSV'
    if year == 2022 and kind == 'votacao':
        transformation = 'CD_CARGO=3; additionally Douglas Ruas state deputy 2022; UTF-8 comma CSV'
    manifest.append({
        'file': str(out.relative_to(P)), 'member': member, 'parent_archive': filename,
        'parent_sha256': sha, 'url': original['url'], 'sha256': hashlib.sha256(out.read_bytes()).hexdigest(),
        'obtained_original': obtained, 'extracted_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'transformation': transformation,
        'parent_hash_note': 'Conferido contra o manifesto herdado antes de gravar. Nao e um novo download do TSE.',
    })
    if kind == 'votacao':
        memberbr = next(n for n in z.namelist() if n.endswith('_BR.csv'))
        op = P / 'raw' / f'presidente-{year}-RJ.csv'
        with io.TextIOWrapper(z.open(memberbr), encoding='latin1') as f, op.open('w') as g:
            reader = csv.DictReader(f, delimiter=';')
            writer = csv.DictWriter(g, reader.fieldnames)
            writer.writeheader()
            for row in reader:
                if row['SG_UF'] == 'RJ':
                    writer.writerow(row)
        manifest.append({
            'file': str(op.relative_to(P)), 'member': memberbr, 'parent_archive': filename,
            'parent_sha256': sha, 'url': original['url'], 'sha256': hashlib.sha256(op.read_bytes()).hexdigest(),
            'obtained_original': obtained, 'extracted_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'transformation': 'SG_UF=RJ; UTF-8 comma CSV',
            'parent_hash_note': 'Mesmo ZIP pai da votacao estadual. Nao e um novo download do TSE.',
        })
dest = P / 'data/source-manifest.json'
if dest.exists():
    shutil.copyfile(dest, P / 'data/source-manifest.anterior.json')
dest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
print('Snapshots extracted and parent hashes verified before writing')
