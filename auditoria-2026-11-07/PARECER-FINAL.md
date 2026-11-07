# PARECER FINAL — Auditoria do estudo RJ 2026 (`RafaelPanisset/estudo-rj-2026`, commit `f7278de8335458be2f290c15b9a63a220954d639`)

Consolidação da coordenação. Data de corte: 07/11/2026. Horários de Brasília (UTC−3). Este parecer **não aplica correções ao estudo** e não reescreve as conclusões dele. Os números citados vêm dos pareceres e das evidências em `agentes/`, sem número novo inventado. Ver também `ESCOPO.md`, `ACHADOS.csv`, `DIVERGENCIAS.md` e `VERIFICACOES.md`.

## 0. Estado da auditoria: NÃO completa
Foram feitas uma rodada inicial dos nove revisores, réplicas nos pontos disputados (01→A3-13; 05→peças) e a reconferência dos dois achados altos. **A auditoria não está completa em pontos essenciais**, e as conclusões abaixo marcadas como **[provisório]** dependem deles:
1. **Procedência histórica dos dados eleitorais.** Demonstrou-se só que o conteúdo dos recortes é igual ao que o TSE servia em 07/11, e que o ZIP de seções é byte-idêntico. Não foram reverificados os ZIPs-pai nem o manifesto herdado do projeto vizinho (P1-05, R6-05), e `download.py` não foi executado.
2. **Situação jurídica.** Não foram obtidos o acórdão de 08/10, os autos da proclamação, os andamentos da ADPF 1362 nem a certidão de trânsito. Só há notícias institucionais e a decisão interlocutória de 02/10.
3. **Pesquisas.** Faltam PesqEle, microdados e pesos, e os originais da Quaest, do Atlas 3/10 (no domínio do instituto) e da matriz S9-03. A separação entre mudança tardia, seleção, ponderação e comparecimento fica impossível.
4. **Mecanismos de campanha.** Faltam autos e perícia dos santinhos, RDV, exposição e alcance.
5. O asset privado `dados-v1` não foi baixado. Ele foi substituído por um download TSE byte-idêntico, e por isso a exigência do manifesto **foi atendida** por equivalência de SHA-256 (ver §2).

## 1. Veredito: **CONFIÁVEL COM CORREÇÕES** (delimitado)
- **Contabilidade, resultado proclamado e descrição territorial: confiável.** O revisor 06 reproduziu 14/14 produtos byte a byte. Três implementações independentes (02, 06, 07), mais 04, conferem os totais centrais: Ruas 4.271.199, Paes 3.706.984, válidos 8.394.627, margem +564.215, capital −410.961, restante +975.176, Anthony 274.411 como nulos técnicos e 49,27% → 50,88%. A reconciliação seção→zona deu 0 divergências em 37.675 seções. Nenhum revisor achou erro crítico ou alto nessa base.
- **Trajetória das pesquisas: exige correção de impacto alto.** O estudo trata como "final" uma onda Datafolha que não foi a última e omite as ondas finais da Paraná e do Atlas (P1-01/A3-01, P1-02/A3-02). Isso muda magnitudes (erro de margem do Datafolha de 18,51 para 14,51 p.p.; conhecimento do número de 67/44 para 75/52), mas **não inverte a direção** das conclusões: Paes à frente em todas as últimas ondas e Ruas crescendo em todas as séries.
- **Explicação política e causal: parcial [provisório].** A síntese mistura inserção prévia, associação e contribuição eleitoral (R7-01). As explicações concorrentes foram testadas só nas versões extremas (R7-02). Há documentos disponíveis que não foram usados: Rosinha e Clarissa, alianças cruzadas, publicidade, o santinho de 04/10 e o cruzamento S9-03 (A5-01/02/03, A9-01/02/03).
- **Por que não "não confiável":** não há achado crítico, os números centrais se sustentam e os dois achados altos corrigem magnitude e cobertura, sem inverter conclusões. **Por que não "confiável" sem ressalva:** os dois altos, 23 médios únicos e lacunas documentais supríveis.

## 2. O que foi verificado, executado e não acessado (síntese; detalhes em `VERIFICACOES.md`)
**Executado ou verificado:**
- Integridade da referência: 65/65 blobs conferidos por quatro revisores; 66/66 entradas do manifesto conferidas pela coordenação às 09:04.
- Exigência do ZIP de 296 MB: **atendida pelo download TSE de 07/11 (08:27:08) com SHA-256 `ec93c020…3cf5`, igual ao digest do asset `dados-v1`** (06, `list_releases`), com 296.106.129 bytes. A exigência foi mantida, não removida.
- Reprodução com exit 0 e saídas byte-idênticas, idempotente e sem depender do projeto vizinho. Falha com pastas de saída ausentes (R6-02). Asserts somem sob -O em scripts isolados; o orquestrador bloqueia -O (R6-07).
- Recálculos independentes da contabilidade (02, 04, 05, 06, 07).
- Comparação de conteúdo com os arquivos atuais do TSE: governador 2026 e 2022, detalhe, presidente 2026 e 2022 (01); 27 totais do detalhe atual (02).
- PDFs originais das pesquisas: Datafolha 2/10 e 5/10 (v2 da onda 2–3/10), Paraná setembro e outubro, Atlas setembro (01, 03). Atlas 3/10 só em republicação.
- Fontes jurídicas: decisão de 02/10 aberta no PJe; notícias do TSE, TRE, Senado, STF e MPF (02).
- Redes e campanha: 22 URLs, 41 registros de apoios e 16 de campanha (05).
- Santinho: foto do g1 de 04/10; cópia de 91 p. da inicial da AIJE, não autenticada no PJe (05, 09).
- Cruzamento S9-03 em matérias do contratante (03, 09).
- Reconferência independente dos dois altos (§5 de `VERIFICACOES.md`).

**Não executado ou não acessado:** `download.py`; o asset privado; o projeto vizinho; os SHA-pai históricos; acórdão, autos, trânsito e ADPF; PJe da AIJE, auto de apreensão, NFS-e e laudo; PesqEle; microdados e pesos; originais da Quaest, do Atlas 3/10 e da Veritá; matriz S9-03; RDV, BU e especificação de 2026; detalhe presidencial; microdados de 2018 e 2024; peças e anúncios originais e exposição.

## 3. Achados priorizados (54 registros; 49 únicos depois de 5 duplicatas estritas; ver `ACHADOS.csv`)
**Contagem dos 54 registros (status atribuído pelos agentes):**

| Gravidade \ Status | erro confirmado | sustentação insuficiente | divergência não resolvida | não verificável | Total |
|---|---:|---:|---:|---:|---:|
| crítica | 0 | 0 | 0 | 0 | **0** |
| alta | 2 | 2 | 0 | 0 | **4** |
| média | 3 | 18 | 1 | 2 | **24** |
| baixa | 11 | 7 | 1 | 7 | **26** |
| **Total** | **16** | **27** | **2** | **9** | **54** |

**Únicos (sem A3-01, A3-02, A3-05, A3-11 e R4-02, duplicatas de P1-01, P1-02, P1-04, P1-06/07 e A3-04):** 49. Gravidade: 0 crítica, 2 altas, 23 médias, 24 baixas. Status: 13 erros confirmados, 25 de sustentação insuficiente, 2 divergências não resolvidas e 9 não verificáveis. Das duas divergências, **A3-13 foi resolvida depois pela réplica de 01** e não é defeito do estudo, mas do parecer 01. Resta A3-10. Excluindo A3-13, sobram **48 problemas do estudo**.

### Altos (alteram descoberta importante)
1. **P1-01 = A3-01, erro confirmado.** ANALISE l.49 e l.63 e `pesquisas-confronto.json` usam o Datafolha de 28/9–1/10 como medida final. A onda de 2–3/10 (RJ-01334/2026, n=2.002) dá válidos 46/38/7 (Paes +8, não +12), totais 41/34/6 e número correto 75% entre eleitores de Ruas e 52% entre os de Paes (não 67/44). O erro de margem contra o snapshot passa a 14,51 p.p., não 18,51. *Efeito:* reduz o desencontro e muda as métricas de número de urna. A direção se mantém.
2. **P1-02 = A3-02, sustentação insuficiente.** Ficaram fora: Paraná 29/9–1/10 (41,9/30,1; válidos 47,9/34,4; série Ruas 15,5→20,3→26,7→30,1); Atlas 27/9–2/10 (46,4/38,0; válidos 48,6/39,8; só republicação); Quaest e RTBD (RJ-08712), secundárias; e séries já presentes nos PDFs arquivados pelo próprio estudo. *Efeito:* reforça o crescimento de Ruas em cinco séries e mostra que, na véspera, Paes tinha de +8 a +13,5 nos válidos. Uma ultrapassagem continua sem data.

### Médios mais relevantes (por impacto na conclusão)
3. **R4-01.** "89 municípios" e "acréscimo local só em SG, Cambuci e Tanguá" dependem do denominador. Em % dos válidos, Ruas supera Flávio em 62 municípios (35 com Anthony). Fora da capital: Ruas 57,21% × Flávio 56,03%.
4. **R7-01 / R7-02.** O rótulo causal agrega coisas distintas, e as alternativas só foram testadas nas versões exclusivas.
5. **A3-06, A3-03, A3-07, A3-15.** O erro líquido por candidato não foi decomposto: Anthony aparece com 6–9% nas pesquisas contra 3,17% na urna. O efeito do denominador não foi quantificado (0,21 p.p. na margem). Falta o teste territorial condicional. A ultrapassagem não é datável.
6. **A3-10 / A9-02.** O cruzamento de intenção S9-03 foi omitido (divergência interna não resolvida).
7. **P1-04 = A3-05.** Os válidos da Quaest vêm de modelo de eleitor provável, e os totais 35/28/4 foram omitidos.
8. **A5-01, A5-02, A5-03.** Rosinha e Clarissa pouco investigadas; inventário nominal de apoios e alianças cruzadas incompleto; publicidade e temas subinvestigados.
9. **A9-01, A9-03.** O santinho Paes/Jane/22 de 04/10 não foi tratado. A via do RDV para os nulos não foi documentada (204.309 não certificado).
10. **A2-01.** Fundamentos do TSE incompletos: parcial provimento quanto à alínea l, com indeferimento mantido por direitos políticos e filiação.
11. **R6-05, R6-06, P1-05.** A aquisição herdada é circular e não roteirizada; `download.py` sobrescreve snapshots.
12. **AD-01, AD-03.** Lacunas sem classificação nem trilha de busca. A tabela atribui percentuais aos válidos, mas a abstenção é calculada sobre aptos.
13. **R4-06, P1-03.** Denominadores presidenciais ausentes; RDV ausente; agregador 48,1/39,0 sem fonte.

### Baixos
P1-06, P1-07, P1-08, P1-09; A3-04 (= R4-02, cenário "sem Anthony" pareado com a retotalização); A3-08, A3-09, A3-11, A3-12, A3-13 (resolvido), A3-14; R4-03 (2018: Paes venceu a capital só no 2º turno), R4-04 (mapa comprimido cerca de 27%), R4-05; R6-01 a R6-04, R6-07 a R6-12; AD-02.

## 4. Matriz dos 10 requisitos do briefing (revisor 08, versão final)
| Item | Requisito | Status | Principal lacuna | Pareceres |
|---|---|---|---|---|
| 1 | Trajetória da disputa | parcial | ondas finais e séries disponíveis fora; PesqEle não conferido | P1-01/A3-01; P1-02/A3-02; A3-04/05/11/14 |
| 2 | Crescimento de Ruas | parcial | mecanismos não separados; número "final" incorreto | A3-01/09/10; A5-02; A9-02; R7-01 |
| 3 | Desempenho de Paes | parcial | campanha e alianças cruzadas superficiais | A5-02/03; R7-02 |
| 4 | Papel de Garotinho | parcial | acórdão; Rosinha e Clarissa; fundamentos jurídicos | A2-01; A5-01 |
| 5 | Regiões do estado | **atendido** | ajustes AD-03 e R4-04 | R4; AD-03 |
| 6 | Máquinas e redes | parcial | inventário nominal e datado incompleto | A5-02; R7-02 |
| 7 | Temas da campanha | parcial | programas, debates, publicidade e redes; peças | A5-03; A9-01/03; réplica 05 |
| 8 | Participação eleitoral | **atendido** | só legenda do denominador (AD-03) | V2-03/07; T7 de 06 |
| 9 | História e voto presidencial | parcial | denominador; turno de 2018; cruzamento omitido | R4-01/03/05; A9-02; A3-10; R6-11 |
| 10 | Explicações concorrentes | parcial | sem teste de contribuições graduais | R7-01/02; A5; A9 |
| F | Formato solicitado | parcial | metadados de aquisição; clareza; delimitação da síntese | R6-02/05/06; P1-05; R7-01; AD-01/02/03 |
**Contagem:** dez itens: 2 atendidos / 8 parciais / 0 não atendidos / 0 n.a. Formato: parcial. Total: 2/9/0/0. A contagem não é nota de qualidade.

## 5. Conclusões do estudo: manter, reformular, rebaixar, retirar
**Manter:**
- Contabilidade: margem +564.215; capital Paes +410.961; restante Ruas +975.176; Ruas vence 79 de 92 municípios. Percentuais 49,27% → 50,88% sem mudança de votos.
- Sem segundo turno estadual no resultado proclamado (TRE-RJ, 15/10). Anulação não é transferência.
- Liderança inicial de Paes documentada; crescimento de Ruas (agora mais robusto).
- Rejeição de Paes estável no Datafolha e na Paraná.
- Base de Ruas em 2022: 175.977 votos, 149.576 em SG.
- Apoio de Wladimir posterior à votação.
- Cautelas: nulos não são votos de Paes; abstenção sem preferência imputada; acusações não são fatos; saldos não são fluxos.

**Reformular:**
- "Datafolha final" e o confronto: Paes +8, não +12; erro de 14,51, não 18,51 p.p.; número 75/52, não 67/44. A frase "rejeição de Ruas 19→29 até a última onda" vale só até 28/9–1/10 (P1-01/A3-01).
- "89 municípios": apresentar votos absolutos e % dos válidos, com e sem Anthony (R4-01).
- Síntese do README l.18/24 e de HIPOTESES l.7: separar inserção, associação e contribuição (R7-01).
- 2018: indicar o 2º turno (R4-03).
- "Reconcilia com TRE" → "conferido contra constantes" (R6-03). 49,27% como reconstrução contábil (R6-04).
- Tabela: "Abstenção (% dos aptos)" (AD-03). Quaest: modelo de eleitor provável e totais (P1-04).
- Linguagem de "autenticação": usar a fórmula de equivalência de conteúdo (D1).
- Fundamentos do TSE (A2-01).

**Rebaixar:**
- "Base + bolsonarismo ajudaram/viabilizaram" passa a: inserção estabelecida; associação e viabilização apoiadas; contribuição eleitoral não identificada (R7-01).
- Refutações de hipóteses fortes não valem como refutação de contribuição parcial (R7-02).
- "Reorganizações de zonas" passa a não verificável (R4-05).
- 2024 passa a dado documental sem insumo preservado (R6-11).

**Retirar, ou rotular como não comparável:**
- Linhas "sem Garotinho" do confronto com a urna (A3-04 = R4-02).
- Menção ao agregador 48,1/39,0, salvo se a fonte for citada (P1-03).
- Uso do Datafolha 28/9–1/10 como medida final.

**Incorporar (lacunas supríveis):** ondas finais e RJ-08712 (não BR-05193); S9-03 como intenção declarada; santinho de 04/10 e peças separadas; Rosinha e Clarissa; catálogo nominal de apoios; publicidade de O Globo 01/10; erro líquido por candidato; tabela de denominadores.

## 6. Respostas independentes
**6.1 Fundamento da expectativa de Paes e por que falhou.** A liderança medida existia nos cinco institutos consultados (03):
- Datafolha 18–20/8: 41/19 [original];
- Paraná, agosto: 44,5/15,5 [original];
- Atlas, rótulo 31/8: 43,6/27,6 [gráfico];
- Quaest, cerca de 8/9: 39/18 [secundária];
- RTBD 14/9: 35/25 [secundária].

Nas últimas ondas, Paes ainda liderava nos válidos com Anthony: Datafolha +8, Atlas +8,8, Quaest +9 (modelo) e Paraná +13,5. Intenção não é probabilidade de vitória.

*Onde* falhou: a vantagem na capital (+410.961) não cobriu o déficit no restante (+975.176 para Ruas), sobretudo na periferia metropolitana (Ruas +493.204 na RMRJ sem a capital). Na capital, Paes teve 1.730.683 votos, contra 1.861.856 em 2024 (este número só documental), com o comparecimento em alta de 172.444 (04). *Por que* falhou: não identificado. O erro de margem fica entre 14,5 e 20 p.p., na mesma direção em todos os institutos [condicionado ao snapshot]. O denominador explica cerca de 0,21 p.p. O restante pode ser mudança tardia, erro comum de medição (seleção, não resposta, ponderação), comparecimento ou uma combinação, e os dados não distinguem essas hipóteses (03, 07). **[provisório]**

**6.2 Construção da votação de Ruas.** Ruas não partiu do zero: 175.977 votos para deputado estadual em 2022, 149.576 em SG (85,0%), além de trajetória administrativa e rede familiar (Capitão Nelson). A articulação com Flávio, Castro e Altineu está registrada (O Dia, 24/02). A expansão foi muito além de SG: sem SG, a margem estadual é 449.484, e os 10 maiores saldos somam 502.396 (51,5% do saldo fora da capital). Ele cresceu em cinco séries (Datafolha 19→34; Paraná 15,5→30,1). O cruzamento S9-03 mostra alinhamento declarado com Flávio (86% dos eleitores de Ruas), mas com voto cruzado e alianças cruzadas (Washington Reis apoiou Paes, Flávio e Castro). *Conclusão permitida:* estrutura prévia e associação nacional são mecanismos de viabilização apoiados. Os efeitos de partido, líder, candidato, redes, mensagens e mobilização não foram separados. **[provisório]**

**6.3 Papel de cada Garotinho.**
- **Anthony William Garotinho Matheus de Oliveira** (Republicanos, número 10): seus 274.411 votos viraram nulos técnicos. Concentravam-se em Campos (43.421; 15,82%) e no Norte (56.952; 20,75%). A exclusão desses votos tirou Ruas de "liderança sem maioria" para eleito no 1º turno, mas não mudou a margem nominal. A CNN de 03/10 registra Anthony rejeitando apoiar Paes e tratando um apoio a Ruas como muito improvável.
- **Wladimir** (PL 2258, eleito): apoiou o pai antes da votação e disse "agora é 22" depois dela (NF, 05/10). É declaração posterior, sem transferência demonstrada.
- **Rosinha:** a CBN de 19/08 relata coordenação regional da campanha de Anthony no Norte e Noroeste. Não há lista de participantes nem votos atribuíveis.
- **Clarissa:** articulação de bastidores (CBN). Não certifica endosso a Ruas.
- As intenções hipotéticas dos eleitores de Anthony (43/41) não podem ser multiplicadas por 274.411. Ausência de transferência mensurada não prova ausência de influência (A5-01).

**6.4 Efeito jurídico versus transferência.** O denominador caiu de 8.669.038 para 8.394.627, e Ruas passou de 49,2696% para 50,8802% com os mesmos 4.271.199 votos. A maioria mínima caiu de 4.334.520 para 4.197.314: Ruas estava 63.321 votos abaixo dela antes e ficou 73.885 acima depois. **Nenhum voto foi transferido.**
- Base jurídica (notícia do TSE de 08/10): desistência não homologada; parcial provimento para afastar a inelegibilidade da alínea l; indeferimento mantido por falta de direitos políticos e de filiação; anulação e retotalização por 5–2.
- Proclamação em 15/10. A ADPF 1362 (PSD) foi noticiada sem decisão conhecida. A AIJE de 04/11 contém alegações.
- Não há trânsito em julgado demonstrado. O "antes" é reconstrução contábil, não snapshot oficial anterior (R6-04). **[provisório quanto à situação processual]**

**6.5 Houve virada datável?** **Não.** Nenhuma onda das 25 do corpus mostra Ruas à frente, e o último campo termina em 3/10 (03). Para conciliar as pesquisas com a urna seria preciso uma mudança de cerca de 14 p.p. de margem depois do campo, um erro comum aos institutos, ou uma combinação dos dois, e os dados não distinguem. Não datar a virada pelo debate, pela decisão de 02/10 nem pelo dia da votação.

**6.6 Lacunas exatas.**
- Jurídicas: acórdão de 08/10 e certidão de trânsito; andamentos da ADPF 1362.
- Pesquisas: PesqEle; microdados e pesos; originais da Quaest e do Atlas 3/10; matriz S9-03 (RJ-02205/BR-05762); definição da RM do Datafolha; painel ou pós-eleitoral.
- Votação e urna: RDV/BU 2026 com especificação; detalhe presidencial (cargo 1).
- Procedência: SHA-pai e manifesto herdado.
- Santinhos e campanha: auto de apreensão e nota do TRE; PJe da AIJE e da notícia 0600024; NFS-e e laudo; agendas da família Garotinho; declarações originais de prefeitos e líderes; anúncios e programas; debates codificados.
- Histórico: microdados de 2018 e 2024.

## 7. Santinhos, influência presidencial e outras omissões
**Santinhos e números de urna.**
- *Demonstrado:*
  - **RP-22A:** foto publicada pelo g1 em 04/10 às 17h12 de um santinho com "GOVERNADOR / EDUARDO PAES / JANE REIS / 22". O número de Paes é 55; o 22 é de Ruas. O g1 atribui a fiscais do TRE a localização em Nova Iguaçu.
  - **RP-22B:** colinha "Minha Colinha" em dois modelos.
  - **RP-13:** peça "Rio Escolhe", que diz literalmente "Lula é 13" e "Bolsonaro é 22", e não "Paes governador 13".
  - **RP-100K:** folheto religioso "Evangélico, de que lado você está?".
- *Só alegado:* autoria (as duas campanhas se acusam). Quantidades: 100 mil unidades do folheto religioso e 1,1 milhão da família "Rio Escolhe", segundo a inicial da AIJE, numa cópia republicada não autenticada no PJe. Também só alegada a distribuição.
- *Plausível:* confusão de número localizada. O mecanismo do 22 (voto válido para Ruas) é diferente do mecanismo do 13 (nulo).
- *Falta para estimar magnitude:* auto com quantidade, endereço e custódia; exemplares originais; NFS-e e laudo; exposição e compreensão; RDV validado. Mesmo assim, o RDV mostraria só a digitação, não a intenção. **Nenhum fator demonstrado decisivo.**

**Influência presidencial.**
- *Demonstrado:* apoios prévios (Flávio, Castro, Altineu) e o cruzamento de intenção S9-03 (Ruas→Flávio 86%; Paes→Lula 64%, mas Paes→Flávio 20%). Os cálculos das condicionais não fecham entre si (D3).
- *Plausível:* identificação partidária, efeito de líder, número 22 compartilhado nos dois cargos e rejeição nacional.
- *Não identificado:* direção causal e magnitude.
- *Falta:* matriz original com bases; painel e motivos; detalhe presidencial com participação.

**Outras omissões.**
- Assimetria de conhecimento do número (75% contra 52%; entre eleitores de Paes, 44% não sabiam e 4% citaram número incorreto). "Não sabe" não é voto perdido.
- Ordem de votação: governador antes de presidente (TSE).
- Abstenção maior na capital (26,16% contra 21,57%).
- Publicidade religiosa impulsionada (O Globo, 01/10).
- 204.309 nulos com o 13 (g1, 06/10): **não certificado**; 204.309 ≤ 675.292 é só compatibilidade aritmética.
- Compra de votos e fraude: alegações, não fatos.
- Tudo isso é plausível ou testável, sem peso atribuível.

## 8. Plano de correção por impacto
**A. Ajustes simples (texto e dados já disponíveis):**
1. Incluir a onda Datafolha 2–3/10, refazer `pesquisas.csv`, a figura e o confronto, e retirar o rótulo "final" (P1-01/A3-01).
2. Apresentar séries por instituto, com ondas finais e grau de fonte; RTBD = RJ-08712 (P1-02/A3-02).
3. Confrontar com a urna só o cenário com Anthony; rotular o cenário sem Anthony como hipotético (A3-04/R4-02); registrar o modelo da Quaest (P1-04).
4. Mostrar as duas bases na comparação presidencial (R4-01); corrigir o turno de 2018 (R4-03).
5. Legenda da abstenção (AD-03); glossário (AD-02); páginas e datas (P1-06/07, A3-11).
6. Fundamentos do TSE (A2-01); "constantes" em vez de "TRE" (R6-03); 49,27% como reconstrução (R6-04).
7. Código: `mkdir` das pastas de saída (R6-02); mensagem clara sem o ZIP (R6-01); `if/raise` no lugar de `assert` (R6-07); conferir o hash antes de gravar e corrigir textos do manifesto (R6-05); correspondência TSE-IBGE fora de `data/` (R6-09); registro de reprodução com hashes (R6-10); proporção do mapa (R4-04).

**B. Novas análises com insumos existentes:**
8. Desagregar a síntese causal e testar hipóteses aditivas com previsões discriminantes (R7-01/02).
9. Erro líquido por candidato; decomposição do denominador; teste territorial condicional (A3-03/06/07).
10. Incorporar S9-03 como intenção declarada (A3-10/A9-02); catálogos 05 e 09: Rosinha e Clarissa, apoios nominais e alianças cruzadas, publicidade, peças separadas (A5-01/02/03, A9-01).
11. Quadro de lacunas com questão, busca, canal, data, resultado e tipo (AD-01).

**C. Aquisição externa (não executada nesta auditoria):**
12. Acórdão de 08/10, certidão de trânsito, andamentos da ADPF 1362, autos da proclamação.
13. PesqEle, microdados e pesos, originais Quaest e Atlas, relatório presidencial Datafolha 22–24/09 com bases.
14. Script de aquisição TSE com verificação de hash e preservação de versões (R6-06); manifesto herdado ou DT_GERACAO (P1-05); recortes de 2024 e 2018 (R6-11).
15. Detalhe presidencial cargo 1; RDV e especificação 2026, para digitação, nunca para intenção (A9-03/R4-06).
16. Auto de apreensão, nota do TRE, PJe da AIJE e da notícia 0600024, NFS-e e laudo; anúncios e programas; painel ou estudo pós-eleitoral.

## 9. Limites desta consolidação
- Os revisores são bots no mesmo computador. Independência intelectual parcial: 04 e 07 viram números antes; 02 se descreve como braço do revisor.
- Hash ≠ autenticidade ≠ veracidade.
- Republicações da mesma origem não contam como confirmação independente.
- Nenhuma evidência posterior ao corte foi usada.
- A referência e os relatórios dos agentes não foram alterados.
- Nenhuma correção foi aplicada ao estudo.
- Não houve push, commit, PR, publicação nem mensagem externa.
