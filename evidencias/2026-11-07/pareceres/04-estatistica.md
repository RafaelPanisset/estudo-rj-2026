# Agente 4 — RJ26 Estatística e território: parecer

Revisor 4 (Grok Bot executor). Data de corte: 7/11/2026. Trabalho feito entre 08:39 e 08:47 de 7/11/2026 (America/Sao_Paulo, UTC-3). Referência: `/workspace/rj26/ref`, montada por git archive do commit `f7278de8335458be2f290c15b9a63a220954d639`. Não é um repositório git; a integridade foi aferida pelo `ref.MANIFEST.txt` e pela checagem 65/65 do revisor 6. Fiz uma cópia própria em `work/04-estatistica/repo`, com o ZIP via symlink, mas não executei a reprodução: o revisor 6 já reproduziu byte a byte. Todos os cálculos abaixo vêm de scripts próprios e leves, que leem os CSVs/JSON preservados: `04-estatistica/audit04.py` e `audit04b.py`, com saídas `.log`/`-out.json` e hashes em `scripts.sha256`. Eles levam menos de 2 s e menos de 200 MB; o ZIP de 296 MB não foi aberto além do diretório central. Ambiente: Debian, Python 3.13.5, sem pacotes extras (`ambiente.txt`). As primeiras observações estão em `04-estatistica/PRIMEIRAS-OBSERVACOES.md`, registradas antes de ler 06 e 09. Ressalva: a mensagem de coordenação já trazia números do revisor 6, então não houve cegueira, mas os números foram recalculados.
Não fiz commits, push, publicação, mensagens externas nem Canvas. Limite: as checagens de 2018 e 2024 são documentais (imprensa/TSE notícia via busca web), sem microdados.

## Veredito delimitado
A contabilidade territorial está **correta**. Não encontrei erro crítico nem alto. Os achados são de interpretação e apresentação (1 médio de interpretação, 1 médio de dado inexistente, 4 baixos). A conclusão central se mantém: margem estadual de +564.215, com capital −410.961 e restante +975.176. Também se mantém a maior parte das cautelas contra a falácia ecológica e contra ler saldos como fluxos. Precisa ser reformulada a leitura da comparação com a eleição presidencial (R4-01).

## Verificações bem-sucedidas (teste próprio)
- **Chaves, duplicatas e faltantes:** 0 duplicatas em governador 2026 (1.464 linhas = 8×183), detalhe (183), 2022 (1.281 gov + 183 dep.) e presidente 2022/2026. Os 92 municípios e as 183 zonas são os mesmos em 2022 e 2026. As zonas das seções coincidem com o detalhe nos dois sentidos.
- **Filtros:** ano, cargo e turno são homogêneos em todos os recortes. O presidente tem linhas de T2 (366), excluídas corretamente por `NR_TURNO=='1'`. `'CASTRO'` só casa com Cláudio Castro, e Ruas 2022 tem um único SQ (22022, PL).
- **Trânsito:** ST_VOTO_EM_TRANSITO=N em 100% das linhas. Se houve voto em trânsito, ele não é distinguível nos insumos. As identidades fecham, então isso não afeta os totais.
- **Seções:** 37.675 principais + 1.063 agregadas = 38.738 no total; 0 não instaladas e 0 eleitores em seções não instaladas. O CSV de seções tem exatamente QT_SECOES_PRINCIPAIS por zona, portanto as agregadas estão fundidas nas principais. Há 0 divergências zona×seção em comparecimento, válidos, brancos (95), nulos (96), técnicos (10) e cada candidato. Contagem de seções Ruas/Paes/empate: 24.416/12.998/261. O estudo trata isso como contagem de unidades, não como peso.
- **Identidades:** aptos = comparecimento + abstenção; comparecimento = válidos + brancos + nulos; nulos = 675.292 + 274.411; anulados e sub judice = 0; nominais = válidos.
- **Denominadores e capital/restante:** capital com 38,54% dos válidos (38,49% dos aptos, 37,07% do comparecimento). Abstenção de 26,16% na capital e 21,57% fora dela. Ruas com 49,27% antes e 50,88% depois da anulação; 73.885,5 votos acima de 50%.
- **Regiões:** a partição analítica de 92 municípios equivale às regiões de governo (Petrópolis na Serrana). A sobreposição metropolitana corresponde exatamente à RMRJ de 22 municípios (lista própria, LC 184/2018): +82.243 com a capital e +493.204 sem ela; o restante soma +481.972. Todos os valores regionais e municipais citados em §5 conferem. Top-10 = 502.396, que é 51,5% do saldo líquido fora da capital (49,9% das margens positivas brutas; a diferença é desprezível). Paes vence 13 municípios, confirmados.
- **TSE↔IBGE e geometria:** nomes normalizados únicos 92/92 nos dois lados. A malha tem 92 códigos, todos no cadastro, e a correspondência gerada coincide com a minha. As legendas estão corretas, com a nota de que área não representa votos.
- **Histórico:** Castro 2022 com 58,69% e Freixo com 27,39% dos válidos de 2022 (8.400.962). Ruas 2022: 175.977 votos, dos quais 149.576 (85,0%) em São Gonçalo. O dado de 2024 (Paes 1.861.856; 60,47%) confere com a notícia do TSE de 6/10/2024. A mesma notícia mostra comparecimento de 3.477.280 em 2024 contra 3.649.724 em 2026: Paes perdeu 131.173 votos com o comparecimento em alta de 172.444, o que reforça a cautela do texto de que não são desertores.
- **Inferência:** não encontrei regressão ecológica, matriz de transferência nem preferência religiosa deduzida da composição municipal. Os saldos −659.089 e −695.645 estão rotulados como não fluxos, e o cenário de abstenção não é apresentado como estimativa. A concentração de Anthony em Campos/Norte é lida corretamente como base territorial, não como destino dos votos.

## Achados (formato completo em `04-estatistica/achados.csv`)
| ID | Local | Status | Gravidade | Síntese |
|---|---|---|---|---|
| R4-01 | ANALISE L61, L130; HIPOTESES L7 | sustentação insuficiente | média | A comparação presidencial está só em votos absolutos (≈ fração do mesmo comparecimento). Em % dos válidos, Ruas > Flávio em 62 municípios (35 com Anthony no denominador). Fora da capital, Ruas tem 57,21% e Flávio 56,03%; a defasagem se concentra na capital (40,79% contra 47,88%). Paes > Lula em % fora da capital (38,30% contra 36,77%). Os “89 municípios” e o “acréscimo local específico” dependem da base escolhida |
| R4-02 | polls.py; pesquisas-confronto.json | erro confirmado | baixa | Compara o cenário “sem Garotinho” com o resultado pós-anulação, o que não é comparável e contradiz a própria nota de pesquisas.csv. O texto (L49) usa a comparação correta |
| R4-03 | ANALISE L132 | erro confirmado | baixa | 2018: Paes venceu na capital só no 2º turno (51,69%); no 1º, Witzel teve 39,03% contra 24,01% de Paes (UOL, Gazeta do Povo; sem microdados) |
| R4-04 | maps.py L17 | erro confirmado | baixa | Mapa comprimido ~27% na vertical (sem cos(lat)) |
| R4-05 | ANALISE L134 | não verificável | baixa | “Reorganizações” de zonas não demonstradas: os 183 códigos são idênticos em 2022 e 2026. Código igual também não prova o mesmo território |
| R4-06 | pedido do revisor 9 | não verificável | média | Ver abaixo |

## Pedido do revisor 9 (lido após as primeiras observações)
- **Denominadores presidenciais:** as 183 chaves existem para presidente T1, com 12 candidatos cada, e coincidem com as do governador. O recorte presidencial **não tem** aptos, comparecimento, brancos, nulos nem trânsito (só QT_VOTOS_NOMINAIS*). O único denominador próprio é o de válidos (9.369.700, ou 3.471.874 na capital). Comparações em fração do comparecimento presidencial não são possíveis com os insumos, e ficou faltando o detalhe munzona 2026 do cargo 1.
- **204.309 nulos “digitados 13” (g1, 06/10):** não há RDV nos insumos preservados. O ZIP tem só votacao_secao e leiame. O arquivo por seção agrega todo nulo de urna no código 96 (675.292 no estado), sem código 13 para governador. Única conta possível: 204.309 ≤ 675.292 (30,3%), compatibilidade aritmética que **não é** verificação. Seguem hipótese e alegação jornalística não certificadas. Mesmo com RDV oficial, a digitação não mede intenção e não permite parear os votos de um eleitor entre cargos. Dados que faltam: os arquivos RDV oficiais 2026 por urna com hash e especificação, com reconciliação de cobertura e da soma dos nulos de governador com o 96 por seção.

## Comparabilidade 2024/2026 realmente sustentada
Nos insumos há: 2026, governador (munzona, detalhe, seção) e presidente T1/T2 (só votos nominais); 2022, governador T1, Ruas para deputado estadual e presidente T1/T2 (sem detalhe, sem abstenção nem brancos/nulos de 2022); IBGE com cadastro e malha atuais.
- **2022→2026:** sustenta comparação municipal de votos e % de válidos por candidato.
- **Abstenção e nulos históricos:** não sustenta comparação, por falta do detalhe de 2022.
- **2024:** só o total da capital, por fonte documental (notícia do TSE), sem insumo preservado (ver R6-11). A comparação é descritiva e entre cargos diferentes.
- **2018:** só contexto de imprensa.
- **Fronteiras:** códigos e nomes estáveis; a estabilidade territorial das zonas não é verificável.

## Pendências e o que não foi feito
- Não repeti a varredura completa do ZIP nem a reprodução dos scripts (feitas pelo revisor 6; meus números independentes coincidem com os dele).
- Não rodei testes de sensibilidade além de R4-01, o único com potencial de mudar uma leitura.
- Subgrupos e transcrição das pesquisas cabem ao revisor 3.
- Microdados de 2018/2024, RDV e detalhe presidencial ficaram de fora porque exigiriam aquisição externa.
