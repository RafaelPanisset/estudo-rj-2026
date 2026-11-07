# Agente 1 — RJ26 Procedência e autenticidade — parecer (rodada inicial + reconferência dos achados altos)

- **Commit auditado:** f7278de8335458be2f290c15b9a63a220954d639. Leitura inicial pela integração oficial GitHub (`get_file_contents`, ref fixa). Depois, conferência com `/workspace/rj26/ref`, montada pelo coordenador às 08:31 BRT: os 24 hashes de `data/snapshot-manifest.json` conferem. **As linhas citadas abaixo seguem a cópia `ref/`.** As cópias via API tinham 2 linhas de invólucro, e por isso a versão anterior deste parecer citava linhas deslocadas em +2; corrigido.
- **Data de corte:** 07/11/2026.
  - Downloads por curl: 07/11/2026, de 08:28:33 a 08:34:11 BRT (UTC-3), segundo mtimes e cabeçalhos HTTP `Date` (11:28:33–11:34:02 GMT).
  - WebFetch/WebSearch: de cerca de 08:29 a cerca de 08:37 BRT, sem log com segundos.
  - Reconferência visual e correções: das 08:38 às 08:41 BRT, sem novos downloads.
  - Não afirmo que o conteúdo era idêntico em datas anteriores a esses acessos. Os documentos trazem as próprias datas de publicação ou geração, indicadas em cada caso.
- **Ferramentas:** curl, WebFetch/WebSearch, poppler 25.03.0 (`pdftotext`, `pdftoppm`, `pdfinfo`), Python 3, `sha256sum`, `unzip`, `iconv`. Não executei scripts do estudo e não alterei `ref/`.
- **Arquivos deste agente:**
  - `01-procedencia/00-observacoes-iniciais.md` (registrado antes de ler qualquer parecer de outro revisor);
  - `inventario-fontes.md`, `achados-01.csv`, `RESULTADO-INTERMEDIARIO.md`, `RECONFERENCIA.md`;
  - `evidencias/` (downloads, comparações, imagens de página; versão anterior deste parecer em `evidencias/01-procedencia.v1-antes-reconferencia.md`).

## Síntese delimitada

1. **Dados baixados dos canais dos emissores e conferidos.**
   - **Microdados do TSE (cdn.tse.jus.br).** Os recortes do estudo são idênticos em conteúdo, campo a campo exceto DT/HH_GERACAO, aos arquivos baixados hoje do mesmo CDN: votação de governador 2026 e 2022 (mais Ruas, deputado estadual 2022), detalhe 2026, presidente 2026 e 2022 (UF=RJ) e seções 2026. O ZIP de seções tem SHA-256 igual ao manifesto.
   - **PDFs e páginas dos institutos.** Datafolha 2/10, Paraná setembro e Atlas setembro baixados dos domínios dos institutos têm SHA-256 igual ao manifesto.
   - **APIs do IBGE.** SHA igual.
   - **Limites.** Isso estabelece que os bytes ou o conteúdo correspondem ao que esses canais servem hoje. Não estabelece a verdade dos números das pesquisas.
2. **Fatos jurídicos e de totalização.** As notícias institucionais do TRE-RJ, da Agência Senado e do STF (notícia e andamento) e a notícia do TSE de 2024 conferem com os microdados. São independentes do autor do estudo, mas **não são confirmações factualmente independentes entre si**: todas reportam a mesma totalização da Justiça Eleitoral e a mesma decisão do TSE. A concordância delas com os microdados mostra coerência entre publicações oficiais da mesma origem, não uma medição independente. Não abri autos, acórdãos nem a ata da retotalização no DJe.
3. **Fontes sem original verificado:**
   - Quaest (só republicações; os "válidos" vêm de modelo de eleitor provável segundo os veículos do contratante);
   - Veritá;
   - agregador citado para os números 48,1/39,0;
   - páginas TRE/STF (lidas, sem bytes preservados no estudo; curl recebe 403);
   - Atlas de 3/10 (íntegra só como republicação do Poder360).
4. **Achados altos** (reconferidos visualmente; ver `RECONFERENCIA.md`):
   - **P1-01:** o estudo usa a onda Datafolha de 28/9–1/10 como medida pré-eleitoral no confronto com a urna e para o conhecimento do número. Existia uma onda posterior (2–3/10) publicada pelo Datafolha.
   - **P1-02:** o corpus de pesquisas omite as últimas ondas da Paraná (29/9–1/10) e do Atlas (27/9–2/10) e a série de 4 ondas que a própria Paraná publica.
   - Nenhum dos dois inverte a direção das conclusões: Paes à frente nas últimas pesquisas e Ruas crescendo. Ambos alteram magnitudes e o conjunto de evidências.

## Achados

| ID | Agente | Arquivo / seção / linha (ref) | Afirmação examinada (texto do estudo) | Problema | Evidência | Status | Gravidade | Confiança | Impacto | Correção |
|---|---|---|---|---|---|---|---|---|---|---|
| P1-01 | 1 | ANALISE-DETALHADA.md l.49; l.63; results/pesquisas-confronto.json (Datafolha campo_fim 2026-10-01); research/CRONOLOGIA.md l.22 ("Datafolha auditado final"); research/HIPOTESES.md l.9 ("final auditado") | l.49: "Datafolha tinha Paes +12 e Quaest Paes +9", em confronto com o resultado. l.63: "O Datafolha final observou… 67% para Ruas e 44% para Paes" | O estudo **não diz** que essa foi a última onda do instituto: "auditado final" pode ser lido como a última onda auditada pelo estudo. Mas usa essa onda como a medida Datafolha no confronto com a urna e chama de "Datafolha final" a estatística de número. Antes do corte, o Datafolha publicou a onda **2–3/10/2026**: 2.002 entrevistas, 35 municípios, ±2 p.p., RJ-01334/2026 e BR-07933/2026, contratantes Folha de S.Paulo e TV Globo. **Totais com Garotinho:** Paes 41, Ruas 34, Garotinho 6, branco/nulo/nenhum 6, indecisos 5. **Válidos com Garotinho:** 46/38/7, Paes +8, base de 1.769 entrevistas. **Válidos sem Garotinho:** 49/40. **Menções corretas do número:** 57% no total; 75% entre eleitores de Ruas (base 602, ±4 p.p.); 52% entre eleitores de Paes (base 886, ±3 p.p.) | Original: https://media.folha.uol.com.br/datafolha/2026/10/05/xdwelu0lqnxn2-5oke87g-v2.pdf (SHA-256 b9448e38…; 57 p.; pdfinfo CreationDate 05/10/2026 13:00 -03), conferido visualmente nas p.2 (ficha), p.8 (série de totais, 5 ondas), p.10 (válidos) e p.12 (número). O PDF está ligado na página do instituto datada de 04/10/2026. Imagens em `evidencias/imagens/reconf/df-final-*.png` | erro confirmado (no uso como medida final e na atribuição "Datafolha final"; não no rótulo isolado de CRONOLOGIA) | alta | alta: original do emissor, conferido visualmente; republicações da mesma origem (g1, CNN, Band, O Globo) não contam como confirmação independente | Diferença pesquisa–resultado Datafolha com Garotinho: 18,51 → 14,51 p.p., contra margem oficial de Ruas de +6,51 com Garotinho no denominador. Muda as métricas de número de urna. A frase "a decisão judicial não explica o desencontro" continua sustentada | Incluir a onda 2–3/10 e refazer `pesquisas.csv`, a figura e `pesquisas-confronto.json`; ajustar o termo "final" |
| P1-02 | 1 | ANALISE-DETALHADA.md l.36–43 (tabela de institutos); README.md l.17 ("Série comparável do Datafolha: 19% → 31%"); AUDITORIA.md l.9 ("Três relatórios originais: Datafolha, Paraná, Atlas") | O estudo apresenta uma onda de Paraná e uma de Atlas e só a série Datafolha como evidência de crescimento. **Não afirma** que só o Datafolha tinha série; a versão anterior deste parecer atribuía isso ao estudo, o que foi retirado | Estavam publicadas antes do corte e não foram usadas: (a) **Paraná Pesquisas, 29/9–1/10/2026**, original no site do instituto; (b) **Atlas/Estadão, 27/9–2/10/2026**; (c) Real Time Big Data, 25–29/9, **RJ-08712/2026** (governador; original no domínio do emissor), não examinado em detalhe. *[Correção da réplica A3-13: a versão anterior citava BR-05193/2026, que é a pesquisa presidencial RTBD; ver `01-procedencia/REPLICA-A3-13.md`.]* Detalhes no bloco abaixo da tabela | (a) https://paranapesquisas.com.br/wp-content/uploads/2026/10/RJ_Out26.pdf, conferido visualmente nas p.3, 8, 9 e 10. (b) Íntegra republicada por Poder360 (static.poder360.com.br/uploads/2026/10/Pesquisa-Atlas_Estadao-Eleicoes-Rio-de-Janeiro-2026-261003.pdf), conferida visualmente nas p.5, 8 e 9; ficha coerente com atlasintel.org/poll/brazil-rio-de-janeiro-pesquisa-atlasestadao-2026-10-03 | sustentação insuficiente (corpus incompleto; a existência das fontes está confirmada) | alta | alta para Paraná (original do emissor); média-alta para Atlas 3/10 (republicação integral, original no domínio Atlas não aberto) | Há séries comparáveis dentro da Paraná que corroboram o crescimento de Ruas. A dispersão entre institutos na véspera (Paes +8 a +13,5 nos válidos) e as respostas sobre datação mudam | Incluir as ondas por instituto sem misturar curvas e registrar o RTBD |
| P1-03 | 1 | research/FONTES.md l.40; ANALISE-DETALHADA.md l.47 | "agregadores encontrados traziam 48,1/39,0"; divergência "sem solução documental" | Não há referência rastreável: nenhum agregador é citado. Não localizei esses números exatos. **Hipótese não confirmada:** confusão com outras ondas Atlas. Encontrei, só em republicações, 48,1 para Paes no cenário sem Garotinho de 15–20/9 (Gazeta do Povo) e 48,6/39,8 em 3/10, mas não a combinação 48,1/39,0 | WebSearch em 07/11 | não verificável | média | média | Pequeno nos números adotados (o estudo não os usou) | Citar o agregador e a data, ou retirar a menção |
| P1-04 | 1 | research/FONTES.md l.16 (F8); ANALISE-DETALHADA.md l.42–43 e l.49; data/pesquisas.csv (linhas Quaest) | Quaest 49/40 "válidos", "método não conferido" | A fonte é uma republicação da CNN, que declara usar IA para extrair dados. Os veículos do contratante (g1 e O Globo, 03/10) dizem que os válidos da Quaest vêm de modelo de eleitor provável e informam totais 35/28/4 (indecisos 15, branco/nulo 13). A comparação com o resultado mistura válidos modelados com renormalizados | g1 03/10 17:36; O Globo/Pulso 03/10 (via WebSearch). O "PDF Quaest" do Poder360 é impressão de matéria do g1 (pdfinfo Title "…\| G1") | sustentação insuficiente | média | média-alta (método declarado por republicações da mesma origem; original Quaest não obtido) | Decomposição "quanto do erro é denominador" | Obter o relatório Quaest; registrar totais e método |
| P1-05 | 1 | scripts/prepare.py l.3, l.21–24; data/source-manifest.json | Hashes dos ZIPs-pai verificados; "obtained_original 2026-11-01" | (a) A conferência compara com o manifesto do projeto vizinho, que não foi entregue: é circular. (b) A data é uma *string* fixa no código. (c) As entradas presidenciais não têm URL, data nem SHA do pai. (d) O texto "additionally Douglas Ruas state deputy 2022" aparece também em arquivos onde não se aplica. (e) Os ZIPs atuais do TSE têm outros hashes porque são regenerados | `evidencias/comparacao-*.txt`; `sha256sum` dos ZIPs | sustentação insuficiente (a–c) e erro confirmado (d) | média | alta | Nenhum nos números (conteúdo idêntico, verificado); afeta a reprodutibilidade da aquisição | Publicar o manifesto herdado ou registrar DT_GERACAO; completar o manifesto |
| P1-06 | 1 | research/FONTES.md l.13 (F5 "série total p.11"), l.15 (F7 "p.5 método") | Páginas citadas | No PDF Datafolha de 2/10, a série de totais com Garotinho está na p.10 (a p.11 é o cenário sem Garotinho). No Atlas de setembro, a metodologia está na p.4 (a p.5 é a ficha) | pdftotext por página | erro confirmado | baixa | alta | Rastreabilidade | Corrigir |
| P1-07 | 1 | data/pesquisas.csv, coluna `divulgacao`, 3 ondas Datafolha | 21/8, 11/9, 24/9 | Datas ausentes do PDF citado | PDF de 2/10, p.9–12 | sustentação insuficiente | baixa | alta | Cronologia | Citar fonte |
| P1-08 | 1 | ANALISE-DETALHADA.md l.55 (Capitão Nelson), l.96 ("em 4/10 voltou a afastar…"); research/CRONOLOGIA.md l.12 (Ricardo Couto) | Fatos de contexto | Sem URL ou arquivo. Couto tem apoio parcial (Datafolha 2/10, p.6; Exame 13/7) | busca no repositório | não verificável | baixa | média | Contexto | Anexar fontes |
| P1-09 | 1 | research/FONTES.md F1, F2, F4; AUDITORIA.md l.22 | Páginas TRE/STF lidas por ferramenta web | Bytes não preservados; o conteúdo lido hoje confere | WebFetch 07/11; curl 403 | não verificável (bytes) | baixa | alta | Nenhum nos números | Preservar captura ou ata do DJe |

**Detalhe das fontes omitidas em P1-02:**

- **Paraná Pesquisas, 29/9–1/10/2026:**
  - RJ-07095/2026, 1.600 entrevistas, 54 municípios, ±2,5 p.p.; documento datado Curitiba, 02/10.
  - Cenário 1, totais: Paes 41,9, Ruas 30,1, Garotinho 8,2, nenhum/branco/nulo 8,3, não sabe 4,3.
  - Válidos: 47,9/34,4/9,4.
  - Comparativo do próprio documento, mesmo cenário, para Ruas: RJ-02422 (agosto) 15,5 → RJ-01671 20,3 → RJ-04036 26,7 → RJ-07095 30,1.
- **Atlas/Estadão, 27/9–2/10/2026:**
  - RJ-02601/2026 e BR-02842/2026, 2.244 respondentes, ±2 p.p. pela ficha da p.5. Estadão e Terra dizem ±3: divergência entre republicação e ficha.
  - Totais: 46,4/38,0/6,1. Válidos: 48,6/39,8/6,4.

## Verificações bem-sucedidas (com teste)

- **TSE governador 2026:** 1.464 linhas idênticas ao CDN atual, exceto a geração.
  - Válidos somam 8.394.627.
  - Ruas 4.271.199; Paes 3.706.984; margem 564.215.
  - Capital: Paes +410.961. Fora da capital: Ruas +975.176. Ruas vence em 79 de 92 municípios.
  - Garotinho não aparece no arquivo de candidatos; os 274.411 votos estão como nulos técnicos no `detalhe`.
- **Detalhe 2026:** só 1º turno para governador; 37.675 seções principais.
- **Seções:** o ZIP de seções tem SHA igual ao manifesto. `secoes-governador.csv` tem 315.138 linhas, totais iguais e inclui Garotinho com 274.411.
- **2022:** Ruas, deputado estadual, 175.977 votos, sendo 149.576 em São Gonçalo. Castro: 4.930.288.
- **Presidente 2026/2022:** conteúdo idêntico.
- **Notícias institucionais** (mesma origem factual, ver Síntese 2): TRE-RJ 10/10 e 15/10, Senado 8/10, STF 14/10 e andamento (último em 03/11, conclusos) e TSE 2024 (1.861.856; 60,47%) conferem com os números do estudo.
- **Pesquisas usadas pelo estudo:** números do `pesquisas.csv` conferidos contra Datafolha 2/10 (p.10, 12, 13), Paraná setembro (p.3 e 8) e Atlas setembro (p.8 e 9, visualmente). Os `.txt` do estudo são reproduzidos byte a byte por `pdftotext -layout`.
- **Wladimir:** o texto da NF Notícias de 05/10 confere.

## O que não abri ou não verifiquei

- Autos, acórdãos e DJe.
- Original da Quaest.
- Atlas 3/10 no domínio do Atlas.
- Original da Veritá. RTBD governador (RJ-08712/2026): original do emissor baixado na réplica A3-13, mas não conferido em detalhe.
- Agregador "48,1/39,0".
- Registros no sistema de pesquisas do TSE (PesqEle).
- Projeto anterior e o seu manifesto.
- Fontes secundárias de contexto (F9, F10, F18, MDB, Metrópoles e outras).
