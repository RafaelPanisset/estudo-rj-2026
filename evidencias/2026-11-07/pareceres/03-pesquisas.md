# Agente 3: auditoria das pesquisas eleitorais (rodada inicial)

Este relatório cobre o estudo `estudo-rj-2026`, auditado em `/workspace/rj26/ref` (commit f7278de8…). A referência foi lida apenas, sem execução nem alteração. O corte é 7/11/2026 e os horários estão em UTC-3.

Os arquivos de trabalho ficam em `revisao/agentes/03-pesquisas/`:
- `00-observacoes-iniciais.md`: observações próprias, registradas antes de ler outros pareceres.
- `matriz-ondas.csv`: 25 linhas, uma por onda, cenário e denominador.
- `achados-03.csv` (A3-01 a A3-15) e `verificacoes-03.csv` (V3-01 a V3-11).
- `fontes-comandos-limites.md`.
- `scripts/` e `calculos*.json`.
- `evidencias/`, com os PDFs, cabeçalhos e renders.
- `MANIFEST-SHA256.txt`.

## 1. Síntese
Escopo: o corpus levantado nesta rodada tem cinco institutos, todos usados no cenário com Anthony e nos totais, salvo indicação. São originais Datafolha e Paraná (PDFs do emissor) e Atlas 22–27/9 (PDF arquivado pelo estudo); republicação integral para Atlas 27/9–2/10 (Poder360); e somente matérias secundárias para Quaest e RTBD. O resultado eleitoral vem do snapshot arquivado `ref/raw/secoes-governador.csv`, **não autenticado** nesta auditoria; toda comparação com a urna depende dessa condição.

**Grau de cada conclusão:** [C] confirmado em original; [D] documentado só em fonte secundária ou republicação; [K] condicional ou ilustrativo.

1. **A liderança inicial de Paes aparece nos cinco institutos consultados.**
   - [C] Datafolha 18–20/8: 41/19.
   - [C] Paraná agosto (RJ-02422, dentro do PDF de setembro): 44,5/15,5.
   - [C] Atlas, rótulo "31 ago" no gráfico de série p.10: 43,6/27,6. Não há ficha dessa onda.
   - [D] Quaest, valor retrospectivo de cerca de 8/9 citado pelo g1: 39/18.
   - [D] RTBD 14/9: 35/25.
2. **Ruas cresce dentro de cada série do mesmo instituto**, em totais com Anthony, sem misturar institutos nem cenários:
   - [C] Datafolha, 5 ondas: 19 → 25 → 30 → 31 → **34**. A quinta onda, 2–3/10, foi omitida pelo estudo.
   - [C] Paraná, 4 ondas: 15,5 → 20,3 → 26,7 → 30,1.
   - Atlas, 4 pontos: 27,6 → 32,4 → 35,7 [C, gráfico do PDF arquivado] → 38,0 [D, republicação]. Os dois primeiros são só rótulos de gráfico, e a redação da pergunta muda na última onda.
   - [D] Quaest, 4 valores: 18 (≈8/9, retrospectivo) → 23 (19–22/9) → 25 (25–28/9) → 28 (2–3/10). Só os três últimos têm campo, registro e cenário com Anthony declarados. O valor 14, que aparece num título de link da CNN, foi **excluído** por não ter data nem cenário.
   - [D] RTBD, 2 ondas: 25 → 31.
3. **Não é possível datar a ultrapassagem.**
   - [C/D] Nenhuma onda do corpus levantado (25 linhas em matriz-ondas.csv) mostra Ruas à frente. O último campo termina em 3/10. Ondas fora desse corpus não foram buscadas exaustivamente.
   - Nos válidos com Anthony, nas últimas ondas, Paes tinha:
     - Datafolha 2–3/10: +8 [C];
     - Atlas 27/9–2/10: +8,8 [D];
     - Quaest 2–3/10: +9 [D, modelo de eleitor provável];
     - Paraná 29/9–1/10: +13,5 [C].
   - [K] Contra a margem do snapshot (Ruas +6,51), os erros de margem ficam entre 14,5 e 20 p.p., todos na mesma direção.
   - IC95 ilustrativo, por amostragem aleatória simples (SRS) e sem efeito de desenho: ±4 a ±5 na margem. **Não é teste formal.** O erro amostral real, com desenho, conglomerados e ponderação, é maior e não foi estimado. Não afirmo que a diferença "excede o erro amostral real" nem a atribuo integralmente a outra causa.
4. **[K] O denominador explica pouco da margem**: cerca de 0,2 p.p. (ver 3.4).
5. **[K] Teste territorial agregado (RM × interior):**
   - O teste supõe que a "RM" do Datafolha equivalha à RM analítica de 22 municípios do estudo. Essa equivalência é hipotética, porque a definição do instituto não foi verificada.
   - Sob essa premissa, o peso da RM nos válidos da amostra (74,6% e 75,3%) é próximo do peso no snapshot (74,2%). Reponderar só por esse corte não altera a margem.
   - O teste **não exclui** erro geográfico dentro das regiões (capital × Baixada, municípios, bairros) nem composição por outras variáveis.
6. **Os dados disponíveis não separam mudança tardia, seleção/não resposta, ponderação e comparecimento.** As evidências parciais e os limites estão em 3.5.

## 2. Pistas recebidas: o que foi confirmado de forma independente
- **Datafolha 2–3/10** (pista P1-01, confirmada: A3-01, erro confirmado, alta).
  - Fonte: PDF do emissor baixado por mim (SHA idêntico ao do revisor 1).
  - Ficha p.2/p.25: n=2.002, 35 municípios, ±2, RJ-01334/2026, BR-07933/2026, Folha/TV Globo.
  - Intenção: totais 41/34/6 (p.8), B/N 6, indecisos 5; válidos 46/38/7 (p.10).
  - Cenário sem Anthony: totais 43/35, válidos 49/40.
  - Número correto (p.12): 57% no total, 75% entre eleitores de Ruas e 52% entre os de Paes.
  - O PDF v2 é de 5/10, mas a impressão do g1 de 3/10 já tinha os mesmos números, então eles foram divulgados antes da eleição.
  - Consequência [K, snapshot]: o erro de margem do Datafolha passa a **14,51** p.p., não 18,51. Recalculado por fonte em `scripts/calc_reconferencia.py`: pesquisa 46−38 = Paes +8 (df-0510.pdf p.10); snapshot (3.706.984 − 4.271.199)/8.669.038 = −6,508; 8 − (−6,508) = 14,51.
  - Essa onda não tem pergunta de rejeição, então a frase "rejeição de Ruas 19→29 até a última onda auditada" vale só até 28/9–1/10.
- **Paraná 29/9–1/10** (confirmada): RJ-07095/2026, 54 municípios. Totais 41,9/30,1/8,2, B/N 8,3, NS 4,3; válidos 47,9/34,4/9,4.
- **Atlas 27/9–2/10** (confirmada só por republicação): RJ-02601/2026, n=2.244. Totais 46,4/38,0/6,1; válidos 48,6/39,8/6,4.
- **P1-02** (sustentação insuficiente): concordo e amplio (A3-02).
  - A onda de agosto do Paraná e a série interna da Atlas **já estavam dentro dos PDFs arquivados pelo estudo** e não foram usadas.
  - Acrescento Quaest (3 ondas com ficha e 1 valor retrospectivo; secundárias) e RTBD (2 ondas; secundárias).
- **P1-03** (agregador): não reavaliei; sigo como não verificável.
- **Divergência com o revisor 1 (A3-13):** o PDF BR-05193 que ele cita como RTBD de governador é uma pesquisa **presidencial**. A RTBD de governador de 25–29/9 tem registro RJ-08712/2026.
- **Erros nas matérias da CNN (texto assistido por IA):** atribui à Atlas n=1.206 e o registro RJ-01334, que é do Datafolha 2–3/10; grafa "2016" no registro da RTBD.

## 3. Respostas às perguntas do roteiro

### 3.1 Liderança inicial de Paes
- Documentada, ver a síntese.
- A afirmação do README (l.17) e a tabela ANALISE l.25–32 conferem com o PDF, p.10 (V3-01).
- A FONTES F5 cita a página errada: p.11 em vez de p.10 (A3-11).

### 3.2 Crescimento de Ruas
- Está corroborado por cinco institutos, cada um dentro da própria série.
- Medidas auxiliares:
  - Espontânea Datafolha: 8 → 13 → 20 → 19 → 22.
  - Rejeição de Ruas: Datafolha 19 → 29; Paraná 12,6 → 19,9.
  - A rejeição de Paes fica estável nos dois institutos (V3-03), o que corrobora o estudo.
  - Imagem Atlas 22–27/9: só 10% "não sei" sobre Ruas (A3-09).
- Ressalvas sobre a Atlas: a redação da pergunta muda, o campo se sobrepõe em 27/9 e o rótulo "28 Set" não corresponde ao campo de 22–27/9 (A3-12).

### 3.3 Ultrapassagem
- Não é datável no corpus levantado (V3-06, A3-15).
- Retirei a extrapolação linear da versão anterior, porque não acrescentava evidência.
- [K] Para conciliar as últimas ondas com o snapshot seria preciso uma de três coisas, que os dados não distinguem:
  - uma mudança de cerca de 14 p.p. de margem entre o fim do campo e a votação;
  - um erro comum aos cinco institutos consultados (dois com originais, três com republicação ou secundária);
  - uma combinação dos dois.
- Não converto intenção em probabilidade de vitória.

### 3.4 Quanto o denominador explica (scripts/calc_denominador.py, calc_ondas_finais.py, calc_reconferencia.py)

Todas as linhas "urna" abaixo são do snapshot arquivado e não foram autenticadas; a margem não é chamada de "oficial".

| Denominador (urna, snapshot) | Votos | Ruas | Paes | Anthony | Margem |
|---|---|---|---|---|---|
| Comparecimento | 9.845.867 | 43,38 | 37,65 | 2,79 | 5,73 |
| Válidos com Anthony | 8.669.038 | 49,27 | 42,76 | 3,17 | **6,51** |
| Válidos sem Anthony (retotalização) | 8.394.627 | 50,88 | 44,16 | — | 6,72 |

- A retotalização desloca a margem em **0,21 p.p.**: cerca de 1,1% do erro do Datafolha 28/9–1/10 e 1,5% do de 2–3/10.
- Desloca o nível de Ruas em 1,61 p.p.: cerca de 10% a 14% do erro de nível. É isso que leva Ruas acima de 50%.
- Brancos e nulos digitados somam 11,95% do comparecimento. Nas pesquisas, B/N mais indecisos somam cerca de 11% (Datafolha final). Excluir esses grupos não explica o erro.
- O cenário "sem Anthony" das pesquisas é uma cédula hipotética. Confrontá-lo com a retotalização, como faz `polls.py`, é um erro de pareamento (A3-04). Recálculo por fonte (calculos_reconferencia.json), só para reproduzir os números:
  - Datafolha 28/9–1/10 sem Anthony (p.13): margem 48−38 = 10; 10 + 6,72 = 16,72, igual a pesquisas-confronto.json.
  - Datafolha 2–3/10 sem Anthony (df-0510 p.11): margem 49−40 = 9; 9 + 6,72 = 15,72.
  - Esses números não devem ser usados como erro.
- Os válidos da Quaest vêm de um modelo de eleitor provável e não equivalem aos dos outros institutos (A3-05). A renormalização simples dos totais 35/28/4 dá 48,6/38,9/5,6.
- O resultado eleitoral foi tomado só do snapshot arquivado, sem autenticação. Os cálculos são aritmética sobre esse insumo (V3-07).

**Erro líquido por candidato** (válidos com Anthony, pesquisa − urna). Mostra saldos, não fluxos de eleitores (A3-06).

| Onda | Paes | Ruas | Anthony | Outros | Erro de margem |
|---|---|---|---|---|---|
| Datafolha 2–3/10 | +3,2 | −11,3 | +3,8 | +5,2 | 14,51 |
| Datafolha 28/9–1/10 | +4,2 | −14,3 | +4,8 | +5,2 | 18,51 |
| Atlas 27/9–2/10 | +5,8 | −9,5 | +3,2 | +0,4 | 15,31 |
| Paraná 29/9–1/10 | +5,1 | −14,9 | +6,2 | +3,5 | 20,01 |
| Quaest 2–3/10 (modelo) | +6,2 | −9,3 | +2,8 | +0,2 | 15,51 |

- Anthony nos válidos com Anthony, contra 3,17% no snapshot, separando o campo pela data de 2/10. Essa data de revogação da liminar vem só da CRONOLOGIA do estudo (l.24, fonte F3) e não foi verificada por mim; a hora da decisão é desconhecida.
  - Campo **anterior**: Datafolha 28/9–1/10, 8%; Paraná 29/9–1/10, 9,4%.
  - Campo **misto**: Atlas 27/9–2/10, 6,4%, com a maior parte do campo antes de 2/10.
  - Campo **iniciado no dia da decisão**: Datafolha 2–3/10, 7%; Quaest 2–3/10, 6% (modelo). Parte pode ser anterior à decisão, dependendo da hora.
- A queda de 8 para 7 entre as duas ondas Datafolha cabe dentro do arredondamento e da variação amostral.
- O excesso é compatível com abandono tardio de Anthony e com erro de medição. As pesquisas não distinguem as duas coisas.

### 3.5 Limites para separar os mecanismos
- **Composição territorial:** teste agregado [K] (A3-07). Supõe que a "RM" do Datafolha equivalha à RM analítica de 22 municípios do estudo, o que não foi verificado.
  - RM: pesquisa 50/35/6 contra snapshot 45,6/46,9/2,5.
  - Interior: pesquisa 35/47/8 contra snapshot 34,6/56,2/5,0.
  - Reponderar só pelo peso RM/interior não muda a margem: +12,2 e +8,1.
  - Sob a premissa, o erro não vem da proporção entre esses dois agregados. Não exclui erro geográfico dentro das regiões nem a hipótese de a RM do instituto ser outra.
- **Ponderação: hipótese não verificada** (A3-08, rebaixado).
  - Os rodapés dos gráficos dizem "(1.769 entrevistas)" e as tabelas trazem "Base ponderada". Mas o próprio Datafolha escreve "base ponderada de 2.002 entrevistas" (df-0510, Perfil da amostra), ou seja, usa "entrevistas" também para bases ponderadas.
  - Nenhum texto da fonte afirma que as bases dos gráficos são contagens brutas.
  - A leitura "+4 Ruas / −4 Paes pela ponderação" é **só uma hipótese**. As diferenças entre bases de gráfico e de tabela (por exemplo, eleitores de Ruas 602 no gráfico de conhecimento do número contra cerca de 679 implícitos na tabela) podem vir de outra definição de base.
  - Nenhuma conclusão do relatório depende dessa hipótese.
- **Mudança tardia:** a última onda termina cerca de 1 dia antes da eleição. Não há painel nem rastreamento diário.
- **Comparecimento:** entre os cinco institutos, só a Quaest tem modelo de eleitor provável relatado, e apenas por fonte secundária. A margem desse modelo (+9) não ficou mais próxima do snapshot que a dos outros.
- Separar esses mecanismos exigiria:
  - microdados com pesos;
  - registros no PesqEle (questionário, plano amostral, ponderação);
  - painel ou recontato;
  - pesquisas pós-eleitorais com voto recordado e validação de comparecimento.
- Nada disso está no corpus. A pergunta fica aberta, sem narrativa preferida.

## 4. Pista S9-03: cruzamento presidente × governador (A3-10)
**O que foi obtido**
- Datafolha 22–24/9 (RJ-02205/2026; BR-05762/2026), segundo o g1 de 25/9 (URL em fontes-comandos-limites.md), com os mesmos números repetidos pela Revista Fórum:
  - entre eleitores de Paes: 64% Lula, 20% Flávio;
  - entre eleitores de Ruas: 86% Flávio, 5% Lula;
  - entre eleitores de Anthony: 47% Flávio, 34% Lula.
- A Folha de 26/9 traz a condicional inversa: entre eleitores de Flávio, Ruas 37 → 56 → 63% e Paes 26 → 27 → 21%.

**O que não foi obtido**
- A matriz original e as bases de subgrupo.
- A republicação do relatório de governador de 22–24/9 (dattuss, SHA 22c5865d…) não contém cruzamento. Os relatórios de governador de 2/10 e de 3/10 também não.

**Bases e denominadores**
- 22–24/9: n=1.204. Base válida ponderada 1.082 no cenário A, 1.067–1.068 no B (tabelas). Os rodapés dos gráficos dizem 1.084 "entrevistas", com 317 eleitores de Ruas, 564 de Paes e 86 de Anthony. Não está provado se essas contagens são brutas ou ponderadas (ver 3.5).
- Bases ponderadas aproximadas por subgrupo (cenário, SRS): Paes cerca de 518 (±4,3), Ruas cerca de 361 (±5,2), Anthony cerca de 96 (±10).
- Onda final 2–3/10:
  - Base válida: 1.769 no rodapé do gráfico ("entrevistas") contra 1.788 "base ponderada" na tabela. Sem Anthony: 1.743 contra 1.766.
  - Subgrupos: Ruas 602 no gráfico contra cerca de 679 implícitos (38% × 1.788); Paes 886 contra cerca de 822 (46%); Anthony 123 contra cerca de 125 (7%). A natureza das bases não foi esclarecida.
  - Não há cruzamento presidencial publicado para essa onda.

**Teste de consistência**
- P(Ruas∩Flávio) pela rota do governador: 25,2–26,4%.
- Pela rota do presidente: 27,2–28,3%.
- Não fecha sob arredondamento no cenário com Anthony. Fecha só no limite se o cálculo usar o cenário sem Anthony (Ruas 31%).
- Status: **divergência não resolvida**. O cenário e a base da tabulação não estão identificados.

**Como ler esses números**
- São intenções simultâneas declaradas e indicam alinhamento declarado.
- Não são transferência nem causa. Não multipliquei os percentuais por votos.

## 5. Achados (detalhe em achados-03.csv)

| ID | Tema | Status | Gravidade |
|---|---|---|---|
| A3-01 | Onda Datafolha 2–3/10 omitida; "final" equivocado | erro confirmado | alta |
| A3-02 | Ondas e séries omitidas: Paraná, Atlas, Quaest, RTBD | sustentação insuficiente | alta |
| A3-03 | Efeito do denominador não quantificado | sustentação insuficiente | média |
| A3-04 | Cenário sem Anthony pareado com a retotalização | erro confirmado | baixa |
| A3-05 | Quaest: válidos de modelo; totais omitidos | sustentação insuficiente | média |
| A3-06 | Erro líquido por candidato e sobrestimação de Anthony | sustentação insuficiente | média |
| A3-07 | Teste territorial agregado não feito (condicional à equivalência de RM) | sustentação insuficiente | média |
| A3-08 | Direção da ponderação: só hipótese (bases não esclarecidas) | não verificável | baixa |
| A3-09 | Medidas indiretas de conhecimento e rejeição omitidas | sustentação insuficiente | baixa |
| A3-10 | Cruzamento presidente × governador | divergência não resolvida | média |
| A3-11 | Páginas, bases e datas; ficha da onda 3 recuperável | erro confirmado | baixa |
| A3-12 | Comparabilidade da série Atlas | sustentação insuficiente | baixa |
| A3-13 | BR-05193 é presidencial (diverge do revisor 1) | divergência não resolvida | baixa |
| A3-14 | Registros não conferidos no PesqEle | não verificável | baixa |
| A3-15 | Ultrapassagem: delimitar as hipóteses | sustentação insuficiente | média |

As verificações que conferiram estão em verificacoes-03.csv:
- transcrições Datafolha, Paraná e Atlas;
- rejeição;
- números 67/44 da onda 28/9–1/10;
- divergência de data 28/9 contra 29/9, preservada no estudo;
- margem de 6,51 no snapshot (aritmética; não autentica o resultado);
- 14,51 do revisor 1;
- hashes;
- eleitores de Anthony 43/41;
- ficha Atlas.

## 6. Correções necessárias ao estudo
1. Incluir a onda Datafolha 2–3/10 e deixar de chamar a de 28/9–1/10 de "final" (ANALISE l.49, l.63; CRONOLOGIA l.22; confronto).
2. Apresentar séries por instituto, incluindo as ondas finais e marcando o grau de cada fonte.
3. Confrontar com a urna só os cenários com Anthony e mostrar a tabela de denominadores.
4. Registrar o modelo de eleitor provável e os totais da Quaest.
5. Acrescentar o erro líquido por candidato e a decomposição regional, com o aviso de que não mostram fluxos.
6. Corrigir as páginas e datas citadas e conferir os registros no PesqEle.

## 7. Reconferência crítica (07/11, 08:52 UTC-3)
Correções feitas a pedido do coordenador, sem investigação nova:
1. Frases territoriais absolutas trocadas por um teste agregado condicional à equivalência de RM.
2. Direção da ponderação rebaixada a hipótese, porque a fonte usa "entrevistas" também para bases ponderadas. A3-08 passa a "não verificável".
3. Campo das pesquisas separado em anterior, misto e iniciado em 2/10; a data de 2/10 vem só do estudo.
4. Contagem da Quaest corrigida (4 valores, 3 com ficha; o valor 14 foi excluído).
5. IC95 SRS marcado como ilustrativo, sem teste formal.
6. "Nenhuma onda" e "todos os institutos" limitados ao corpus e aos cinco institutos consultados, com o grau de cada fonte.
7. Erro de 14,51 e pareamento sem Anthony recalculados por fonte (calculos_reconferencia.json); extrapolação linear retirada.
8. Margem da urna sempre condicionada ao snapshot não autenticado.

## 8. Bloqueios e limites
- Nenhum bloqueio de ferramenta.
- Não obtidos:
  - PesqEle;
  - originais da Atlas (no domínio próprio), da Quaest e da RTBD;
  - relatório presidencial RJ do Datafolha com bases;
  - fichas das ondas Datafolha de agosto e de 8–10/9;
  - microdados e pesos.
- Lacunas detalhadas e evidências posteriores ao corte: ver fontes-comandos-limites.md §6.
