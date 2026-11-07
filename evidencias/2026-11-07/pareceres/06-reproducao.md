# Agente 6 — RJ26 Reprodução e código

Revisor: agente 6 (Grok Bot executor, papel "Reprodução e código"). Data: 07/11/2026, horário de Brasília (UTC-3). Commit: `f7278de8335458be2f290c15b9a63a220954d639`. Data de corte da auditoria: 07/11/2026.
Escritas: só em `work/06-reproducao/` (execução) e em `revisao/agentes/06-reproducao/` mais este arquivo. Não fiz clone, commit, push, publicação, mensagem externa nem integração nova. Não modifiquei scripts do estudo. Não li pareceres de outros revisores; minhas primeiras observações estão em `06-reproducao/00-observacoes-iniciais.md`, gravadas às 08:30, antes da execução.

## 1. Veredito delimitado
- **Executou:** sim. `python3 scripts/reproduce.py` terminou com exit 0 em 1,35 s, com `results/` e `figures/` vazios. Com essas pastas **ausentes**, falha (R6-02).
- **Reproduziu:** sim. Os 13 produtos (10 em results, 3 SVG) e `data/correspondencia-tse-ibge.csv` saíram **byte-idênticos** aos da referência. `results/reproducao.json` difere só nos campos de ambiente (python/platform). A reextração do CSV de seções a partir do ZIP também foi byte-idêntica. Uma segunda execução foi idempotente.
- **Está correto (contabilidade):** sim. Minha implementação independente, lida direto dos insumos TSE (ZIP de seções com 6.820.804 linhas, munzona e detalhe), confirma todos os totais, a margem, a divisão capital/restante e o efeito contábil da retotalização. A reconciliação completa seção→zona deu **0 divergências**.
- **Não demonstrado por este agente:** autenticidade das fontes. A integridade dos bytes não prova autenticidade. O "antes" da retotalização é uma reconstrução contábil, não lida de fonte oficial pré-anulação (R6-04). A procedência dos recortes herdados também não foi demonstrada (R6-05).
- **Nenhum erro crítico ou alto confirmado.** Os defeitos são de empacotamento, aquisição e documentação (média/baixa).

## 2. Ambiente (evidencias/00-ambiente.txt)
Debian 13, kernel 6.12.113+, 8 CPUs, 16 GB, Python 3.13.5 (o original usou 3.12.3; o README pede ≥3.11), LANG=C.UTF-8. Sem pacotes pip. A rede não foi desligada: os scripts executados não fazem acesso de rede (leitura de código); `download.py` não foi executado. Um processo pesado por vez; nenhuma concorrência visível com outros revisores (`ps` registrado).

## 3. Integridade da referência e do ZIP (verificação própria, não a alegação do coordenador)
`evidencias/verifica_ref.py` → `verifica_ref.stdout` e, ao final, `verifica_ref_final.stdout`:
- Os 65 blobs da árvore da API em `work/tree.json` (sha = commit fixo, truncated=false) têm SHA-1 git **idêntico** em `/workspace/rj26/ref`: 65/65, 0 divergentes, 0 ausentes. Único extra: `raw/secoes-RJ.zip`, que é esperado (.gitignore).
- `ref/raw/secoes-RJ.zip` e `revisao/catalogo/aquisicao/tse-download-20261107T112708Z/secoes-RJ.zip`: 296.106.129 bytes, SHA-256 `ec93c020ae1f0088216de92e5acc5d3211aefaf1fa589b961132bbf471ee3cf5`. Isso é igual a `snapshot-manifest`, `secoes-download.json`, RELEASE-NOTES e ao digest que a API do GitHub informa para o asset `dados-v1` (lido por `list_releases`).
- **Limitação:** o asset privado não foi baixado diretamente. O arquivo usado é um novo download do TSE CDN (headers: Last-Modified 26/10/2026 17:53:09 GMT; obtido em 07/11 11:27:08Z, 08:27 BRT). A substituição é byte-idêntica e confirmada. Os membros do ZIP são `votacao_secao_2026_RJ.csv` (2.076.543.248 bytes, data interna 26/10/2026 17:47) e `leiame.pdf`. Todas as linhas têm DT_GERACAO 26/10/2026.
- 24/24 hashes do snapshot-manifest conferem.
- A referência continuou intacta depois de todas as execuções (verificação repetida ao final).

## 4. Execuções (comando, saída, código, tempo)
Todas em `/workspace/rj26/work/06-reproducao/`. Arquivos `.cmd/.stdout/.stderr/.exit` em `06-reproducao/evidencias/`.

| ID | Comando / condição | Exit | Tempo | Resultado |
|---|---|---|---|---|
| T1 | `python3 scripts/reproduce.py`, results/ e figures/ **ausentes** | 1 | <1 s | analyze.py: FileNotFoundError results/municipios.csv (R6-02) |
| T2 | idem, pastas **vazias** | 0 | 1.353 ms | 14/14 produtos idênticos à ref; reproducao.json difere só no ambiente (`T2-comparacao-com-ref.txt`, `T2-diff-reproducao-json.txt`) |
| T3 | CSV de seções movido; `python3 scripts/sections.py` | 0 | 29.640 ms | CSV reextraído do ZIP = `96664f34…78ff`, `cmp` idêntico; secoes.csv e secoes-resumo.json idênticos |
| T4 | ZIP movido; reproduce.py | 1 | 56 ms | FileNotFoundError cru (R6-01); ZIP restaurado e hash reconferido |
| T5a/b | `python3 -O reproduce.py` / `PYTHONOPTIMIZE=1` | 1/1 | ~0,2 s | a guarda funciona: "Do not use python -O" |
| T5c/d | cópia descartável `t-assert` com +1000 votos de Ruas; analyze.py normal / com -O | 1 / **0** | ~0,1 s | com -O grava um resumo inconsistente sem erro (R6-07) |
| T6 | prepare.py em cópia `t-prepare`, sem projeto vizinho | 1 | 38 ms | FileNotFoundError ../analise-eleitoral-2026/raw/votacao.zip; nenhum arquivo alterado (hashes antes/depois) |
| T7 | `evidencias/recalculo_independente.py` (implementação própria) | 0 | 24.742 ms | ver §5; comparação em `recalculo/comparacao.json` |
| T8–T10 | verificações próprias de números do texto | 0 | <1 s | ver §6 |
| T11 | reexecução de reproduce.py | 0 | 1.577 ms | idempotente, inclusive reproducao.json |

**prepare.py sem o projeto vizinho:** a reprodução entregue funciona sem ele (T2 nunca chama prepare.py). prepare.py, por si, falha (T6).

## 5. Recálculo independente direto dos insumos (T7)
O script `evidencias/recalculo_independente.py` (sha256 em `.sha256`) não importa nem copia código do estudo. Ele lê o ZIP inteiro: 6.820.804 linhas, apenas 2026, turno 1, RJ, cargos 3/5/6/7. O governador tem 315.138 linhas, todas do turno 1, sem chaves (seção, votável) duplicadas. Também lê munzona (1.464 linhas: 8 candidatos × 183, todas "Válido") e detalhe (183 linhas, DT_ULTIMA_TOTALIZACAO 10/10/2026).

| Medida | Recalculado | Estudo |
|---|---:|---:|
| Ruas / Paes | 4.271.199 / 3.706.984 | igual |
| Válidos / brancos / nulos totais | 8.394.627 / 501.537 / 949.703 | igual |
| Nulos de urna (96) + nulos técnicos | 675.292 + 274.411 | igual |
| Comparecimento / abstenção / aptos | 9.845.867 / 2.996.650 / 12.842.517 | igual |
| Margem estadual | +564.215 votos = 6,7211 p.p. dos válidos (50,8802% − 44,1590%) | igual |
| Capital (TSE 60011, 49 zonas) | Ruas 1.319.722; Paes 1.730.683; margem −410.961 | igual |
| Fora da capital | Ruas 2.951.477; Paes 1.976.301; margem +975.176 | igual |
| Anthony (código 10, seções) | 274.411 = Σ nulos técnicos munzona | igual |
| Ruas % com Anthony no denominador (8.669.038) | 49,2696% (Paes 42,7612%; Anthony 3,1654%) | 49,27% |
| Ruas % após a anulação | 50,8802%; 73.885,5 votos acima da metade; antes faltavam 63.320 para 50% | igual |
| Municípios vencidos por Ruas | 79/92 | igual |
| Seções Ruas / Paes / empate | 24.416 / 12.998 / 261 (37.675 principais) | igual |

**Reconciliação por seção** (todos os códigos, chaves nos dois sentidos): as 183 zonas existem nos dois lados. Os 8 candidatos batem com munzona; 95 = brancos; 96 = QT_VOTOS_NULOS; 10 = nulos técnicos; soma dos códigos = comparecimento; nº de seções = QT_SECOES_PRINCIPAIS (37.675; há também 1.063 agregadas, que não aparecem como seções próprias). **0 divergências.** As identidades munzona (candidatos = válidos; aptos = comparecimento + abstenção; válidos + brancos + nulos = comparecimento; nulos = urna + técnicos) não falham em nenhuma das 183 unidades.
**Comparação com as saídas do estudo:** zonas.csv 0 campos divergentes; secoes.csv 37.675 linhas, 0 divergentes, 0 chaves faltando ou sobrando; municipios.csv 0 divergentes; resumo.json igual em todos os campos comparados.

## 6. README/relatório confrontados com os dados
- README: todos os inteiros com separador de milhar e todos os percentuais aparecem em `results/` (T9). 175.977 e 149.576 (Ruas, deputado estadual 2022, PL, "ELEITO POR QP") foram recalculados de `votacao-2022-RJ.csv` (T8).
- ANALISE-DETALHADA, recalculados (T10): São Gonçalo 61,45% e margem 114.731; estado sem SG 449.484; Niterói +20.976 para Paes; top-10 = 502.396 = 51,52% do saldo fora da capital; Anthony em Campos 43.421 (15,82%) e no Norte 56.952 (20,75%); 85,0%, 5,09%, 9,65%, −659.089, 206.166, 192.203 conferem. "Lula" = número 13 PT (3.693.021) e o 22 presidencial = Flávio Bolsonaro (PL) aparecem assim no arquivo.
- **Não verificável offline:** os dados de Paes em 2024 (1.861.856; 60,47%) não têm insumo preservado (R6-11).
- O README e a análise são estáticos. Como as saídas reproduzidas são idênticas, não há defasagem atual entre texto e dados.
- Observação para os agentes 2/9 (fato de dados, não conclusão): em `presidente-2026-RJ.csv` (gerado em 01/11/2026) há linhas de turno 2 presidencial (366), mas `votacao-2026-RJ.csv`, do mesmo ZIP e geração, só tem turno 1 para governador. Isso é coerente com a ausência de segundo turno estadual. O ZIP de seções (26/10) não tem turno 2 de cargo nenhum, então não serve de prova sobre isso.

## 7. Constantes e validações circulares
- `analyze.py` afirma totais fixos (8.394.627; 4.271.199; 3.706.984; 274.411); `sections.py` (22/55); `polls.py` usa denominadores e votos fixos (8.669.038; 8.394.627). As constantes estão corretas frente ao TSE (§5), mas a "reconciliação com o TRE" não tem fonte local: as páginas do TRE deram 403 (R6-03). O `garotinho_votos_documentados` fixo é verificado contra o próprio dado: é consistência interna, não fonte independente.
- `verificacao.json` e `secoes-resumo.json` têm frases fixas ("183 municipal-zones matched"); `reproducao.json` tem `offline: true` literal (R6-08/R6-10).
- Filtros: munzona e detalhe filtram cargo/turno (por assert) e os recortes são homogêneos (ano 2026, UF RJ, sem trânsito "S"). `sections.py` filtra cargo e turno, sem ano/UF, o que é inócuo porque o ZIP só tem 2026/RJ. Cache: `secoes-governador.csv` é cache do ZIP; validado em T3.
- Caminhos: todos relativos à raiz do projeto (`Path(__file__).parents[1]`), exceto `prepare.py`, que usa o diretório irmão. Não há caminho absoluto nem download nos scripts de reprodução.

## 8. Achados (tabela completa em `06-reproducao/achados.csv`, 11 colunas)
| ID | Arquivo | Status | Gravidade | Resumo |
|---|---|---|---|---|
| R6-01 | reproduce.py / manifesto | erro confirmado | baixa | Sem o ZIP, FileNotFoundError cru; o ZIP é exigido só por hash. Exigência mantida, não removida |
| R6-02 | todos os scripts de saída | erro confirmado | baixa | Pastas results/ e figures/ ausentes fazem a reprodução falhar |
| R6-03 | analyze.py, verificacao.json | sustentação insuficiente | baixa | "Reconcilia com TRE" = constantes, sem snapshot do TRE; números corretos frente ao TSE |
| R6-04 | analyze.py, README §2 | sustentação insuficiente | baixa | 49,27% é reconstrução contábil correta, não lida de totalização oficial anterior |
| R6-05 | prepare.py, source-manifest | erro confirmado | média | Depende do vizinho; hash conferido depois de escrever; sobrescreve o manifesto; textos e metadados errados ou faltando nos recortes presidenciais |
| R6-06 | download.py | erro confirmado | média | Sobrescreve snapshots sem preservar; aquisição dos ZIPs TSE não roteirizada |
| R6-07 | analyze/sections/maps/territory | erro confirmado | baixa | Com -O isolado, as asserções somem (demonstrado com cópia adulterada) |
| R6-08 | sections.py | sustentação insuficiente | baixa | O código reconcilia só 4 códigos; a reconciliação completa independente deu 0 divergências |
| R6-09 | maps.py | erro confirmado | baixa | Reescreve um arquivo em data/ |
| R6-10 | clean-reproduction.json, reproducao.json | sustentação insuficiente | baixa | Registro sem hashes, data ou versão; "offline" literal (substância confirmada por T2/T11) |
| R6-11 | ANALISE L69 | não verificável | baixa | Dados de 2024 sem insumo preservado |
| R6-12 | release dados-v1 | não verificável | baixa | Substituição byte-idêntica pelo download TSE; asset privado não baixado |

**Bloqueios ou erros altos/críticos:** nenhum. O bloqueio inicial (ref vazia e ZIP ausente) foi resolvido pela coordenação às 08:31, e o resultado foi verificado por mim (§3).

## 9. Testes bem-sucedidos (resumo preciso)
Integridade 65/65 blobs e 24/24 snapshots; ZIP SHA-256 = manifesto = digest da API; reprodução exit 0 com saídas byte-idênticas (14/14); reextração ZIP→CSV byte-idêntica; idempotência; guarda contra -O/PYTHONOPTIMIZE no orquestrador; reprodução independente de prepare.py e do projeto vizinho; recálculo independente com 0 divergências em totais, margem, capital/restante, retotalização, zonas, municípios e 37.675 seções; números do README e da ANALISE conferidos (exceto 2024).

## 10. Limitações e o que não foi executado
- Autenticidade e procedência das fontes (TRE, notícias, PDFs de pesquisa) cabem aos agentes 1/2/3. Não as validei.
- Não executei `download.py` (alteraria snapshots e usaria a rede) nem um novo download dos ZIPs munzona/detalhe 2022/2026 para reverificar os hashes pais (9832ae21…, 63bbdcc1…, 3cd62031…). **Próximo passo possível:** baixar os ZIPs TSE munzona numa pasta separada e comparar os hashes com `source-manifest.json`, preservando ambos.
- Não reextraí os recortes presidenciais e munzona (dependem dos ZIPs nacionais ausentes).
- `maps.py` e `polls.py` foram reproduzidos byte a byte, mas a geometria e as transcrições de pesquisas não foram auditadas quanto ao mérito (agentes 3/4).
- Não testei outro sistema operacional nem Python 3.11 exatamente.
- Integridade ≠ autenticidade: hashes iguais mostram apenas que os bytes são os mesmos que o TSE serve hoje e que o autor registrou.

## 11. Evidências (caminhos)
`/workspace/rj26/revisao/agentes/06-reproducao/` contém: `00-observacoes-iniciais.md`, `achados.csv` e `evidencias/`. Em `evidencias/`: `00-ambiente.txt`, `verifica_ref.py`, `verifica_ref*.stdout`, `01-hashes-saidas-originais-ref.txt`, `T1–T7, T11 .{cmd,stdout,stderr,exit}` (T8–T10 foram comandos inline; só a saída foi salva via tee), `T2-hashes-saidas.txt`, `T2-comparacao-com-ref.txt`, `T3-hashes.txt`, `T6-antes/depois.txt`, `recalculo_independente.py`, `recalculo/recalculo.json`, `recalculo/comparacao.json`, `T8-ruas-2022.txt`, `T9-numeros-texto-vs-resultados.txt`, `T10-derivados-analise.txt` e `run.sh`. Cópias de execução: `/workspace/rj26/work/06-reproducao/{repo,guardado,t-assert,t-prepare}`. `guardado/` contém só a cópia do CSV de seções usada em T3. `t-assert` contém um insumo adulterado de propósito, só para o teste T5.
