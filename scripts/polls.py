"""Confronto de pesquisas com a urna e séries separadas por instituto."""
import csv, json, html, pathlib
P = pathlib.Path(__file__).resolve().parents[1]

def require(cond, msg='verificacao de pesquisas falhou'):
    if not cond:
        raise RuntimeError(msg)

(P / 'results').mkdir(parents=True, exist_ok=True)
(P / 'figures').mkdir(parents=True, exist_ok=True)
rows = list(csv.DictReader((P / 'data/pesquisas.csv').open()))
estado = json.loads((P / 'results/resumo.json').read_text())['estado']
validos = estado['validos']
ruas_v = estado['DOUGLAS RUAS']
paes_v = estado['EDUARDO PAES']
anthony_v = estado['nulos_tecnicos']
den_com = validos + anthony_v
den_sem = validos
urna = {
    'paes': 100 * paes_v / den_com,
    'ruas': 100 * ruas_v / den_com,
    'anthony': 100 * anthony_v / den_com,
    'outros': 100 * (den_com - paes_v - ruas_v - anthony_v) / den_com,
}
margem_urna_com = urna['paes'] - urna['ruas']
margem_urna_sem = 100 * (paes_v - ruas_v) / den_sem
nulos_digitados = estado['nulos'] - estado['nulos_tecnicos']
bn_digitados_pct = 100 * (estado['brancos'] + nulos_digitados) / estado['comparecimento']

def num(text):
    return float(text) if text else None

def r2(value):
    return None if value is None else round(value + 0.0, 2)

comparaveis = []
hipoteticos = []
erros = []
for r in rows:
    if r['denominador'] != 'validos':
        continue
    item = {
        'instituto': r['instituto'],
        'campo_fim': r['campo_fim'],
        'cenario': r['cenario'],
        'grau_fonte': r.get('grau_fonte', ''),
        'registro': r['registro'],
        'paes': num(r['paes']),
        'ruas': num(r['ruas']),
        'anthony': num(r['garotinho']),
    }
    if r['cenario'] != 'com Garotinho':
        item['nota'] = (
            'Cenário hipotético: a pesquisa pergunta uma cédula sem Anthony. '
            'A retotalização apenas exclui os votos dele, sem realocá-los. Não há diferença pesquisa-resultado.'
        )
        hipoteticos.append(item)
        continue
    margem_pesq = item['paes'] - item['ruas']
    diferenca = margem_pesq - margem_urna_com
    modelo = 'eleitor provavel' in r['metodo'] or 'eleitor provável' in r['metodo']
    item.update({
        'margem_pesquisa_paes': margem_pesq,
        'margem_resultado_paes': margem_urna_com,
        'diferenca_margens_pp': diferenca,
        'diferenca_margens_pp_2dec': r2(diferenca),
        'denominador_resultado': 'validos com Anthony',
        'mesmo_tipo_de_denominador': not modelo,
        'nota': (
            'Diferença entre a margem da pesquisa e a margem da urna no mesmo rótulo de válidos com Anthony. '
            'Não mede erro amostral puro nem mudança individual.'
            + (' Os válidos desta linha são modelo de eleitor provável, não o mesmo denominador das demais.' if modelo else '')
        ),
    })
    comparaveis.append(item)
    erro = {
        'instituto': r['instituto'],
        'campo_fim': r['campo_fim'],
        'grau_fonte': r.get('grau_fonte', ''),
        'erro_paes': item['paes'] - urna['paes'],
        'erro_ruas': item['ruas'] - urna['ruas'],
        'erro_margem': diferenca,
    }
    if item['anthony'] is not None:
        erro['erro_anthony'] = item['anthony'] - urna['anthony']
        erro['anthony_pesquisa'] = item['anthony']
    if r.get('outros'):
        erro['erro_outros'] = num(r['outros']) - urna['outros']
        erro['outros_pesquisa'] = num(r['outros'])
    erro['aviso'] = 'Saldo líquido por candidato. Não identifica transferência de eleitores.'
    erros.append(erro)

efeito_margem = abs(margem_urna_sem) - abs(margem_urna_com)
efeito_nivel = 100 * ruas_v / den_sem - 100 * ruas_v / den_com
def fracao(efeito, erro_margem):
    return None if not erro_margem else efeito / abs(erro_margem)

decomposicao = {
    'margem_ruas_com_anthony_pp': abs(margem_urna_com),
    'margem_ruas_sem_anthony_pp': abs(margem_urna_sem),
    'efeito_denominador_na_margem_pp': efeito_margem,
    'ruas_pct_com_anthony': 100 * ruas_v / den_com,
    'ruas_pct_sem_anthony': 100 * ruas_v / den_sem,
    'efeito_denominador_no_nivel_ruas_pp': efeito_nivel,
    'brancos_mais_nulos_digitados_pct_comparecimento': bn_digitados_pct,
    'nota': (
        'O denominador muda o limiar de 50% e o nível de Ruas; desloca pouco a margem. '
        'O antes é reconstrução contábil (válidos após a retotalização mais os votos de Anthony), não snapshot oficial anterior.'
    ),
}
for erro in erros:
    if erro['instituto'] == 'Datafolha' and erro['campo_fim'] in ('2026-10-01', '2026-10-03'):
        chave = 'datafolha_' + erro['campo_fim']
        decomposicao[chave] = {
            'fracao_do_erro_de_margem': fracao(efeito_margem, erro['erro_margem']),
            'fracao_do_erro_de_nivel_ruas': fracao(efeito_nivel, erro['erro_ruas']),
        }

out = {
    'denominador_urna': {
        'validos_com_anthony': den_com,
        'validos_sem_anthony': den_sem,
        'margem_paes_menos_ruas_com_anthony': margem_urna_com,
        'urna_pct_validos_com_anthony': urna,
    },
    'comparacoes_com_anthony': comparaveis,
    'cenarios_hipoteticos_nao_comparaveis': hipoteticos,
    'erro_liquido_por_candidato': erros,
    'decomposicao_denominador': decomposicao,
}
(P / 'results/pesquisas-confronto.json').write_text(json.dumps(out, ensure_ascii=False, indent=2))

def ondas(instituto):
    return [r for r in rows if r['instituto'] == instituto and r['denominador'] == 'total' and r['cenario'] == 'com Garotinho' and r['paes'] and r['ruas']]

paineis = [
    ('Datafolha', 'Datafolha · total estimulado, com Anthony', ondas('Datafolha')),
    ('Parana', 'Paraná · total estimulado, com Anthony', ondas('Paraná')),
    ('Atlas', 'Atlas · total estimulado, com Anthony', ondas('Atlas')),
]
svg = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 980"><rect width="980" height="980" fill="white"/>', '<g font-family="sans-serif">']
for i, (key, title, serie) in enumerate(paineis):
    y0 = 16 + i * 300
    svg.append(f'<text x="30" y="{y0 + 28}" font-size="20">{html.escape(title)}</text>')
    require(len(serie) >= 2, key)
    step = 760 / (len(serie) - 1)
    baseline = y0 + 230
    scale = 2.5
    for field, color, nome in [('paes', '#ad5622', 'Paes'), ('ruas', '#266491', 'Ruas'), ('garotinho', '#666666', 'Anthony')]:
        pts = []
        for j, r in enumerate(serie):
            if not r[field]:
                continue
            pts.append((80 + j * step, baseline - float(r[field]) * scale, r[field]))
        if len(pts) >= 2:
            svg.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="3"/>' % (' '.join(f'{x:.1f},{y:.1f}' for x, y, _ in pts), color))
        for x, y, val in pts:
            svg.append(f'<text x="{x:.1f}" y="{y - 8:.1f}" fill="{color}" font-size="13" text-anchor="middle">{html.escape(str(val).replace(".", ","))}%</text>')
        if pts:
            svg.append(f'<text x="900" y="{pts[-1][1]:.1f}" fill="{color}" font-size="14">{nome}</text>')
    for j, r in enumerate(serie):
        rotulo = r['campo_fim'][5:] if r['campo_fim'] else 'ago*'
        svg.append(f'<text x="{80 + j * step:.1f}" y="{baseline + 28}" font-size="13" text-anchor="middle">{html.escape(rotulo)}</text>')
svg.append('<text x="30" y="940" font-size="14">Fim de campo (mês-dia), ou “ago*” quando o PDF só diz agosto. Séries separadas: não formam uma curva única nem uma probabilidade de vitória.</text>')
svg.append('<text x="30" y="964" font-size="14">Quaest e Real Time Big Data ficam fora do desenho: fonte secundária e, no caso da Quaest, válidos de modelo de eleitor provável.</text></g></svg>')
(P / 'figures/pesquisas.svg').write_text('\n'.join(svg))
print('Poll comparisons generated')
