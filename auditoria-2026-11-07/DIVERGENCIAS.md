# DIVERGÊNCIAS entre revisores e como foram tratadas

Critério: uma divergência só conta como resolvida quando há evidência documental ou réplica técnica. O número de revisores que concordam não resolve nada. Na tabela-resumo do fim, "resolvida" quer dizer resolvida por evidência e "não resolvida" fica preservada como está.

## D1. "Snapshot autenticado" (01) × "snapshot não autenticado" (03) — RESOLVIDA (terminológica)
- **01:** o parecer inicial falava em base conferida nos canais emissores. 03 condicionou todas as comparações com a urna a um "snapshot arquivado, não autenticado".
- **Réplica (`01-procedencia/REPLICA-A3-13.md` §2):** 01 define "autenticação operacional" como a soma de duas coisas: canal emissor (cdn.tse.jus.br via HTTPS, com cabeçalhos guardados) e comparação de conteúdo registro a registro. O resultado é que os recortes do estudo têm o mesmo conteúdo que o TSE servia em 07/11/2026, entre 08:28 e 08:30. No caso do ZIP de seções, há também identidade de bytes. 01 **retira qualquer leitura mais ampla**: isso não é veracidade nem identidade histórica em 01/11. Os ZIPs-pai têm SHA diferente (regeneração). A comparação de presidente e de 2022 usou `.upper()`, então diferenças só de caixa e linhas duplicadas não seriam detectadas. O código *inline* não foi salvo.
- **Formulação consolidada (obrigatória no parecer):** "Os recortes TSE do estudo têm conteúdo idêntico ao canal oficial do TSE acessado em 07/11/2026; o ZIP de seções é byte-idêntico. A margem de 564.215 votos (6,51 p.p. com Anthony no denominador) é a da publicação oficial do TSE, não uma verificação independente da apuração." Não se usa o rótulo "autenticado".

## D2. A3-13 — RTBD BR-05193 × RJ-08712 — RESOLVIDA por evidência
- 03 apontou que o PDF que 01 havia catalogado como "RTBD governador, BR-05193/2026" é uma pesquisa **presidencial**.
- Na réplica, 01 baixou os dois PDFs do emissor (realtimebigdata.com.br). BR-05193 é presidencial e byte-idêntico à republicação do Poder360 (SHA `2f71a257…`). A RTBD de governador é **RJ-08712/2026** (SHA `65bc0e7b…`, 31 p., campo 25–29/9, n=2.000, cenário 01: Paes 37, Ruas 31, Garotinho 7, nulo/branco 8). Esses números **não foram conferidos visualmente**.
- 01 corrigiu P1-02, o inventário, o CSV e o catálogo, e preservou as versões anteriores. Impacto baixo: 01 não usou números da RTBD.
- O relatório 03 ainda lista A3-13 como "divergência não resolvida" porque foi escrito antes da réplica. Na consolidação ela vale como resolvida, posição que o revisor 08 (§8) também registra.

## D3. S9-03 — cruzamento presidente × governador sem matriz original — NÃO RESOLVIDA
- **Fonte:** g1 de 25/09 (contratante), Datafolha 22–24/09, RJ-02205/2026 e BR-05762/2026, n=1.204. Paes→Lula 64%/Flávio 20%; Ruas→Flávio 86%/Lula 5%; Anthony→Flávio 47%/Lula 34%. A Folha de 26/09 traz a condicional inversa: entre eleitores de Flávio, Ruas 37→56→63% e Paes 26→27→21%.
- **03 (A3-10):** o teste de consistência não fecha sob arredondamento no cenário com Anthony. P(Ruas∩Flávio) dá 25,2–26,4% pela rota do governador e 27,2–28,3% pela rota do presidente, e só fecha no limite com o cenário sem Anthony. O cenário e a base da tabulação não estão identificados. A matriz original e as bases não foram obtidas, e o relatório de governador republicado (dattuss, SHA `22c5865d…`) não traz o cruzamento.
- **09 (A9-02)** e **07 (§3)** concordam no uso **qualitativo** (alinhamento declarado e autonomia parcial das intenções), sem inverter condicionais, sem multiplicar por votos e sem inferir direção causal.
- **Situação:** a divergência interna entre as duas rotas fica preservada. A magnitude depende do original, que não foi obtido.

## D4. 204.309 nulos com o 13 para governador — NÃO CERTIFICADO (sem conflito entre revisores)
- O g1 de 06/10 (S9-02) atribui a RDVs de 37.675 seções 204.309 confirmações do 13 para governador (00: 344.840; 12: 15.990; 99: 10.702 etc.) e ressalva que "a coincidência dos números não comprova que os eleitores pretendiam votar nesses candidatos".
- **04 (R4-06):** não há RDV nos insumos. O ZIP só tem `votacao_secao` e `leiame.pdf`, e o código 96 agrega todos os nulos de urna (675.292). A única conta possível é 204.309 ≤ 675.292 (30,3%), compatibilidade aritmética que **não verifica** nada.
- **09 (A9-03):** não certificado; a especificação técnica 2026 deu 403. **07:** não certificado.
- **Situação:** não há divergência entre revisores. Há uma alegação jornalística que ninguém conferiu e que fica como **não verificável**. Mesmo com RDV oficial, seria possível testar a digitação, mas não a intenção nem o pareamento entre cargos.

## D5. "89 municípios" e a comparação presidencial — RESOLVIDA por evidência (reformular)
- O estudo usa votos absolutos (Ruas com menos votos que Flávio em 89 municípios; acréscimo local só em São Gonçalo, Cambuci e Tanguá).
- 04 (R4-01) e 07 recalcularam de forma independente e chegaram aos mesmos números: Ruas supera Flávio em 3 municípios em votos absolutos, em 62 em % dos válidos próprios e em 35 com Anthony no denominador. Fora da capital: Ruas 57,21% × Flávio 56,03%; Paes 38,30% × Lula 36,77%; na capital, Ruas 40,79% × Flávio 47,88%.
- Conclusão comum: as duas bases são legítimas e respondem a perguntas diferentes, nenhuma identifica voto cruzado, e o estudo deve mostrar as duas.

## D6. Direção da ponderação (bases de gráfico × tabela) — NÃO VERIFICÁVEL
- O rascunho de 03 sugeria um efeito de +4 para Ruas e −4 para Paes pela ponderação. Na reconferência, 03 rebaixou isso a hipótese (A3-08), porque o próprio Datafolha usa "entrevistas" também para bases ponderadas.
- 09 registrou a base ponderada de 1.788 contra 1.769 "entrevistas" na lâmina final e pediu conciliação, sem chamar isso de erro.
- Situação: não usar ±4. Falta a definição das bases e das variáveis de ponderação pelo instituto.

## D7. Peça "Rio Escolhe": "Paes governador 13" × "Lula é 13" — RESOLVIDA por evidência
- O parecer 09, com base na CNN, descreve a denúncia como "Paes e Lula associados ao 13".
- A réplica de 05 leu a reprodução da peça na cópia da inicial da AIJE (P03 p.17). O texto literal é "EDUARDO PAES GOVERNADOR E LULA PRESIDENTE / LULA É 13" e "DOUGLAS RUAS GOVERNADOR E FLÁVIO BOLSONARO PRESIDENTE / BOLSONARO É 22". 07 conferiu a imagem da p.17.
- Consolidação: a peça não diz literalmente "Paes governador 13". A alegação de indução pela composição visual é diferente da alteração literal do número estadual vista no santinho Paes/Jane/22 (RP-22A).

## D8. Quantidades de material e valor da multa — PARCIALMENTE NÃO RESOLVIDA
- 05 separou três grandezas: (a) 100 mil unidades do folheto religioso "Evangélico, de que lado você está?" (CNN de 04/11; NFS-e 3531 citada pela parte); (b) 100 mil iniciais + 500 mil + 500 mil = 1,1 milhão da família "Rio Escolhe", **alegados** na inicial; (c) R$ 100 mil de multa diária pedida, segundo o g1 de 06/10.
- O Dia e o Prensa relatam R$ 10 mil de multa, e a petição de 06/10 deu 403. Essa divergência entre veículos **não foi resolvida**. Nenhuma tiragem está autenticada.

## D9. Datas e redação de 01 — RESOLVIDAS
- **Horário do parecer:** o parecer v1 dizia "acessos até 08:50", mas o arquivo tem mtime 08:37. Em `RECONFERENCIA.md`, os downloads ficam entre 08:28:33 e 08:34:11, os acessos web aproximados vão até 08:37 e a reconferência foi das 08:38 às 08:41.
- **Série só do Datafolha:** P1-02 atribuía ao estudo a afirmação de que só o Datafolha tinha série. 01 retirou a atribuição, e P1-02 passou a omissão, com status de sustentação insuficiente.
- **P1-03:** 01 retirou o diagnóstico de "mistura de ondas". Fica só a falta de referência rastreável.
- **Independência factual:** 01 deixou claro que as notícias do TRE, do Senado e do STF não são confirmações factualmente independentes entre si.

## D10. Data da revogação da liminar (02/10) — RESOLVIDA por evidência
03 (A3-06) usou a data de 02/10 só a partir da CRONOLOGIA do estudo, sem verificá-la. O revisor 02 abriu diretamente no PJe a decisão de 02/10 (Rcl 0601745-49.2026.6.00.0000), que revoga a liminar e determina que os votos sejam tratados como anulados sub judice. A hora da decisão segue desconhecida, então continua aberto quanto do campo de 02/10 é anterior a ela.

## D11. Publicação da onda Datafolha 2–3/10 antes da eleição — RESOLVIDA (com uma fonte)
O PDF v2 é de 05/10 (metadados). 03 conferiu que a matéria do g1 de 03/10 às 18h18 já trazia os mesmos números. 07 não fez essa reconferência em fonte nova e 09 recomenda não datar o documento como 03/10. A disponibilidade antes do corte está confirmada. A anterioridade à votação se apoia na matéria do contratante.

## D12. Segundo turno estadual — RESOLVIDA, com ressalva de evidência
- **02:** o resultado proclamado (TRE-RJ, 15/10) dispensa o segundo turno.
- **06:** o ZIP de seções (26/10) não tem turno 2 de nenhum cargo e, por isso, não prova nada sozinho. Em `votacao-2026-RJ.csv` o governador só tem turno 1, enquanto o presidente tem 366 linhas de turno 2.
- **09:** a notícia de 06/10 que ainda previa segundo turno é anterior à retotalização.
- Conclusão comum: não houve segundo turno estadual no resultado vigente. A evidência positiva é a proclamação, não o ZIP.

## D13. Definições "73.885" × "73.885,5" e "63.320" × "63.321" — SEM CONFLITO
- 02 calcula contra a maioria absoluta mínima inteira: 4.334.520 antes e 4.197.314 depois. Ruas fica 63.321 abaixo do mínimo antes e 73.885 acima depois.
- O estudo e 06 calculam contra a metade exata: 73.885,5 acima; antes faltavam 63.320 (06).
- São definições diferentes, ambas corretas, e 02 não registrou falso erro.

## D14. Divergências pequenas entre fontes externas — NÃO RESOLVIDAS e imateriais
- Atlas 27/9–2/10: margem ±2 p.p. na ficha (p.5) contra ±3 no Estadão/Terra (01, A3-12).
- Malafaia em Cabo Frio: 21/02 (S11) contra "dois dias após 20/02" (S22). O estudo só diz "fevereiro" (05).
- A decisão de 02/10 contém "11.9.2025", aparente erro material da fonte, que 02 não propagou.
- Matérias da CNN geradas com IA atribuem ao Atlas n=1.206 e o registro RJ-01334 (que é do Datafolha) e grafam "RJ-08712/2016" (03).

## D15. Status de aderência — evolução registrada pelo revisor 08
Item 10 (explicações concorrentes) e o formato passaram de "atendido" para "parcial" depois dos pareceres 07, P1-05 e R6-05/06. Não é conflito entre revisores. É revisão por evidência nova, documentada em `08-aderencia/02-matriz-inicial.md` (3/7/0/0 com formato atendido) e `02-matriz.md` (2/8/0/0 com formato parcial).

## Resumo
| # | Tema | Revisores | Situação |
|---|---|---|---|
| D1 | autenticado × equivalência de conteúdo | 01 × 03 | resolvida (réplica 01) |
| D2 | A3-13 RTBD | 03 × 01 | resolvida (réplica 01) |
| D3 | S9-03 sem matriz | 03, 07, 09 | **não resolvida** |
| D4 | 204.309 nulos com 13 | 04, 07, 09 | **não certificado / não verificável** |
| D5 | 89 municípios | 04, 07 | resolvida (reformular) |
| D6 | ponderação ±4 | 03, 09 | **não verificável** |
| D7 | "Lula é 13" | 09 × 05 | resolvida (réplica 05) |
| D8 | tiragens / multa | 05 | **multa não resolvida**; tiragens alegadas |
| D9 | horários e redação de 01 | 01 × coordenação | resolvida |
| D10 | data de 02/10 | 03 × 02 | resolvida (PJe) |
| D11 | divulgação DF 2–3/10 | 03, 07, 09 | resolvida (g1 03/10) |
| D12 | segundo turno estadual | 02, 06, 09 | resolvida |
| D13 | definições de maioria | 02, 06 | sem conflito |
| D14 | detalhes de fontes externas | 01, 03, 05 | não resolvidas, imateriais |
| D15 | status de aderência | 08 | evolução documentada |
