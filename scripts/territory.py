import csv, json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]

def require(cond, msg='verificacao territorial falhou'):
    if not cond:
        raise RuntimeError(msg)

(P / 'results').mkdir(parents=True, exist_ok=True)
rs = list(csv.DictReader((P / 'results/municipios.csv').open()))

def num(r, f):
    return int(r[f])

def agg(xs):
    return {f: sum(num(r, f) for r in xs) for f in ['DOUGLAS RUAS', 'EDUARDO PAES', 'validos', 'margem_ruas', 'aptos', 'abstencao', 'nulos_tecnicos', 'validos_presidente_2026', 'presidente22_2026', 'presidente13_2026']}

metro = [r for r in rs if r['regiao_analitica'] in ['Capital', 'Baixada Fluminense', 'Leste Fluminense'] or r['municipio'] == 'PETRÓPOLIS']
require(len(metro) == 22, 'regiao metropolitana')
interior = [r for r in rs if r not in metro]
fora = [r for r in rs if r['municipio'] != 'RIO DE JANEIRO']
capital = [r for r in rs if r['municipio'] == 'RIO DE JANEIRO']

def pct(part, whole):
    return 100 * part / whole

def bloco(xs):
    a = agg(xs)
    den_pre = a['validos'] + a['nulos_tecnicos']
    return {
        'ruas_pct_validos': pct(a['DOUGLAS RUAS'], a['validos']),
        'paes_pct_validos': pct(a['EDUARDO PAES'], a['validos']),
        'ruas_pct_com_anthony': pct(a['DOUGLAS RUAS'], den_pre),
        'flavio_pct_validos_presidenciais': pct(a['presidente22_2026'], a['validos_presidente_2026']),
        'lula_pct_validos_presidenciais': pct(a['presidente13_2026'], a['validos_presidente_2026']),
        'paes_pct_com_anthony': pct(a['EDUARDO PAES'], den_pre),
        'validos_governador': a['validos'],
        'validos_presidente': a['validos_presidente_2026'],
    }

n_abs, n_share, n_share_pre, n_paes_share = [], 0, 0, 0
for r in rs:
    ruas, flavio = num(r, 'DOUGLAS RUAS'), num(r, 'presidente22_2026')
    paes, lula = num(r, 'EDUARDO PAES'), num(r, 'presidente13_2026')
    val, pres, ant = num(r, 'validos'), num(r, 'validos_presidente_2026'), num(r, 'nulos_tecnicos')
    if ruas > flavio:
        n_abs.append(r['municipio'])
    if pres and ruas / val > flavio / pres:
        n_share += 1
    if pres and ruas / (val + ant) > flavio / pres:
        n_share_pre += 1
    if pres and paes / val > lula / pres:
        n_paes_share += 1

def urna_cargo(xs):
    a = agg(xs)
    den = a['validos'] + a['nulos_tecnicos']
    return {
        'paes': pct(a['EDUARDO PAES'], den),
        'ruas': pct(a['DOUGLAS RUAS'], den),
        'anthony': pct(a['nulos_tecnicos'], den),
        'peso_nos_validos_com_anthony': pct(den, agg(rs)['validos'] + agg(rs)['nulos_tecnicos']),
    }

def reponderar(peso, rm, interior_pesq):
    paes = peso * rm[0] + (1 - peso) * interior_pesq[0]
    ruas = peso * rm[1] + (1 - peso) * interior_pesq[1]
    return {'paes': paes, 'ruas': ruas, 'margem_paes': paes - ruas}

peso_rm = urna_cargo(metro)['peso_nos_validos_com_anthony'] / 100
# Percentuais regionais das pesquisas: transcrição da auditoria, não estimativa.
pesquisas_rm = [
    {'onda': 'Datafolha 28/9-1/10', 'fonte': 'PDF de 2/10, p.41', 'rm': (50, 35, 6), 'interior': (39, 35, 13), 'peso_amostra_citado_pct': 74.6},
    {'onda': 'Datafolha 2-3/10', 'fonte': 'PDF v2, p.36', 'rm': (50, 35, 6), 'interior': (35, 47, 8), 'peso_amostra_citado_pct': 75.3},
]
cenarios = []
for item in pesquisas_rm:
    cenario = reponderar(peso_rm, item['rm'], item['interior'])
    cenarios.append({**item, 'reponderacao_so_pelo_peso_da_urna': cenario})

result = {
    'metropolitana_22': agg(metro),
    'metropolitana_sem_capital': agg([r for r in metro if r['municipio'] != 'RIO DE JANEIRO']),
    'interior_fora_metropolitana': agg(interior),
    'ruas_menos_presidente22': sum(num(r, 'DOUGLAS RUAS') - num(r, 'presidente22_2026') for r in rs),
    'municipios_ruas_supera_presidente22_absoluto': [(r['municipio'], num(r, 'DOUGLAS RUAS') - num(r, 'presidente22_2026')) for r in rs if num(r, 'DOUGLAS RUAS') > num(r, 'presidente22_2026')],
    'top10_margem_fora_capital': sum(num(r, 'margem_ruas') for r in sorted(rs, key=lambda r: -num(r, 'margem_ruas'))[:10]),
    'comparacao_presidencial': {
        'nota': 'Votos absolutos e percentuais dos válidos respondem perguntas diferentes. Nenhum dos dois identifica voto cruzado.',
        'municipios_ruas_supera_flavio_em_votos': n_abs,
        'municipios_ruas_supera_flavio_pct_validos': n_share,
        'municipios_ruas_supera_flavio_pct_com_anthony_no_denominador': n_share_pre,
        'municipios_paes_supera_lula_pct_validos': n_paes_share,
        'estado': bloco(rs),
        'capital': bloco(capital),
        'fora_da_capital': bloco(fora),
    },
    'cenario_territorial_condicional': {
        'nota': 'Cenário, não estimativa. Supõe, sem verificação, que a RM do Datafolha seja a RM analítica de 22 municípios. Não exclui geografia intrarregional, comparecimento diferencial, não resposta nem seleção.',
        'urna_rm': urna_cargo(metro),
        'urna_interior': urna_cargo(interior),
        'ondas': cenarios,
    },
}
(P / 'results/testes-territoriais.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
reg = list(csv.DictReader((P / 'results/regioes.csv').open()))
s = json.loads((P / 'results/resumo.json').read_text())

def br_int(n):
    return f'{int(n):,}'.replace(',', '.')

def br_pct(x):
    return f'{float(x):.2f}'.replace('.', ',') + '%'

lines = ['# Tabelas reproduzidas', '', 'Ruas e Paes: percentuais dos votos válidos após a retotalização. Abstenção: percentual dos aptos. Margem = Ruas − Paes, em votos. Partição analítica descrita na análise.', '', '| Região | Municípios | Ruas (% dos válidos) | Paes (% dos válidos) | Margem em votos | Abstenção (% dos aptos) |', '|---|---:|---:|---:|---:|---:|']
for r in reg:
    lines.append(f'| {r["regiao"]} | {r["municipios"]} | {br_pct(r["ruas_pct"])} | {br_pct(r["paes_pct"])} | {br_int(r["margem_ruas"])} | {br_pct(r["abstencao_pct"])} |')
lines += ['', '## Candidatos com votos válidos', '', '| Nome | Número | Partido | Votos |', '|---|---:|---|---:|']
for c in s['candidatos']:
    lines.append(f'| {c["nome"]} | {c["numero"]} | {c["partido"]} | {br_int(c["votos"])} |')
lines += ['', 'Anthony Garotinho (Republicanos, 10) recebeu 274.411 votos posteriormente anulados, conforme documentos judiciais e notícias oficiais; não aparece nas linhas de candidatos do snapshot munzona pós-retotalização. Não é uma nona votação válida.', '', '## Maiores margens absolutas favoráveis a Ruas', '', '| Município | Margem | Ruas entre válidos |', '|---|---:|---:|']
for r in sorted(rs, key=lambda r: -num(r, 'margem_ruas'))[:15]:
    lines.append(f'| {r["municipio"]} | {br_int(r["margem_ruas"])} | {br_pct(r["ruas_pct"])} |')
lines += ['', 'Esta tabela é de votação, não de pesquisa. As séries de intenção e as ressalvas de data e de fonte estão na análise e em `figures/pesquisas.svg`: “31 ago” e “20 set” da Atlas são rótulos de gráfico, sem ficha de campo; o eixo dessa figura é por onda, não proporcional ao tempo; a onda Atlas de 27/9–2/10 está só em republicação do Poder360; a Quaest é fonte secundária e os válidos são modelo de eleitor provável.']
(P / 'results/TABELAS.md').write_text('\n'.join(lines) + '\n')
print('Territorial tests and tables generated')
