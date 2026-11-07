# VERIFICAÇÕES — o que foi executado, por quem, com qual resultado, e o que não foi executado

Data: 07/11/2026, horário de Brasília (UTC−3). "Executou", "reproduziu" e "está correto" são coisas distintas. Integridade de bytes não equivale a autenticidade, e autenticidade não equivale a veracidade.

## 1. Integridade da referência e do ZIP
| Verificação | Quem | Comando/evidência | Resultado |
|---|---|---|---|
| 65 blobs Git × árvore da API no commit fixo | 02, 05, 06, 07 (cada um com cálculo próprio) | `sha1(b"blob "+len+NUL+bytes)` contra `work/tree.json`; `02-resultados/checagem-ref.json`, `05-redes/checagem-ref.json`, `06-reproducao/evidencias/verifica_ref*.stdout`, `07-explicacoes/checagem-ref.json` | 65/65 iguais, 0 divergências. A árvore foi obtida pela coordenação, não reobtida por cada um |
| 24 hashes de `data/snapshot-manifest.json` | 06; 01 | `verifica_ref.py` | 24/24 conferem |
| ZIP de seções: SHA-256 e tamanho | 06, 02, 01 | sha256sum; `catalogo/aquisicao/.../headers.txt` | 296.106.129 bytes, `ec93c020…3cf5`, igual ao manifesto, a `secoes-download.json`, ao COMO-USAR e ao digest do asset `dados-v1` informado pela API (06, `list_releases`) |
| Referência intacta depois das execuções | 06 (no fim da sua rodada); coordenação | `verifica_ref_final.stdout`; `sha256sum -c` de `ref.MANIFEST.txt` às 09:04 | Intacta; 66/66 OK |

## 2. Reprodução (revisor 06; cópia isolada `work/06-reproducao/repo`)
| ID | Comando/condição | Exit | Resultado |
|---|---|---|---|
| T1 | `python3 scripts/reproduce.py` com `results/` e `figures/` **ausentes** | 1 | FileNotFoundError (R6-02) |
| T2 | idem, com pastas **vazias** | 0 (1.353 ms) | 14/14 produtos byte-idênticos à referência (10 em results, 3 SVG e `data/correspondencia-tse-ibge.csv`); `reproducao.json` difere só nos campos de ambiente |
| T3 | CSV de seções removido; `sections.py` | 0 (29.640 ms) | reextração a partir do ZIP byte-idêntica (`96664f34…78ff`) |
| T4 | ZIP removido | 1 | FileNotFoundError cru (R6-01); ZIP restaurado e hash reconferido |
| T5a/b | `python3 -O` / `PYTHONOPTIMIZE=1` no orquestrador | 1/1 | a guarda funciona |
| T5c/d | cópia adulterada `t-assert` (+1000 votos de Ruas); analyze.py normal / com -O | 1 / **0** | com -O grava um resumo inconsistente sem erro (R6-07). **Essa cópia é adulterada de propósito e não serve como evidência eleitoral** |
| T6 | `prepare.py` sem o projeto vizinho | 1 | FileNotFoundError `../analise-eleitoral-2026/raw/votacao.zip`; nenhum arquivo alterado |
| T11 | segunda execução | 0 | idempotente |
Conclusão de 06: **executou e reproduziu**. A reprodução entregue não depende de `prepare.py` nem do projeto vizinho.

## 3. Recálculos independentes da contabilidade
| Quem | Implementação | Resultado |
|---|---|---|
| 06 (T7) | `06-reproducao/evidencias/recalculo_independente.py`, direto do ZIP (6.820.804 linhas), do munzona (1.464) e do detalhe (183) | Ruas 4.271.199; Paes 3.706.984; válidos 8.394.627; brancos 501.537; nulos 949.703 (675.292 + 274.411); comparecimento 9.845.867; abstenção 2.996.650; aptos 12.842.517; margem +564.215 (6,7211 p.p.); capital −410.961; restante +975.176; Anthony 274.411 (código 10 = Σ nulos técnicos); 49,2696% → 50,8802%; 79/92 municípios; seções 24.416/12.998/261. **Reconciliação seção→zona com todos os códigos: 0 divergências (37.675 seções principais)** |
| 02 | `02-resultados/recalcular_independente.py` → `recalculo.json`, `recalculo-secoes.json` | identidades testadas nas 183 linhas; denominador 8.669.038 → 8.394.627; maioria mínima 4.334.520 → 4.197.314; código 10 = 274.411 nas 183 unidades, 0 divergências; **27 totais do detalhe atual do TSE** (`detalhe_votacao_munzona_2026.zip`, SHA `ee996c10…`) iguais aos do recorte |
| 04 | `04-estatistica/audit04.py`, `audit04b.py` (CSVs preservados) | 0 duplicatas; filtros homogêneos; trânsito = N em 100%; 37.675 + 1.063 = 38.738 seções; 0 não instaladas; RMRJ de 22 municípios: +82.243 com a capital, +493.204 sem ela; top-10 = 502.396; Castro 2022 58,69%; R4-01 (3/62/35) |
| 05 | `base-ruas-recalculo.json` | Ruas deputado estadual 2022: 175.977, sendo 149.576 em São Gonçalo (84,997%) |
| 07 | `reconferencia-contabil.json` | 4.271.199 / 3.706.984 / 564.215; −410.961 / +975.176; 274.411; R4-01 recalculado (3/62/35) |
| 08 | `verificar_aderencia.py` → `03-verificacoes.json` | 28 testes de coerência entre produtos: 27 positivos e 1 ausência literal (975.176 não aparece escrito na ANALISE, mas é igual a 493.204 + 481.972); 18/18 linhas de TABELAS conferem |
| 03 | `scripts/calc_denominador.py`, `calc_ondas_finais.py`, `calc_reconferencia.py` | retotalização desloca a margem em 0,21 p.p.; erros de margem: DF 2–3/10 14,51; DF 28/9–1/10 18,51; Atlas 15,31; Paraná 20,01; Quaest 15,51 (condicionados ao snapshot) |

## 4. Procedência e conteúdo das fontes
- **01:** recortes TSE iguais, campo a campo exceto a geração, aos arquivos atuais do CDN: governador 2026 (1.464 linhas), detalhe (183), presidente 2026 (2.562), presidente 2022 (2.379), governador 2022 + Ruas (1.464). PDFs Datafolha 2/10, Paraná setembro e Atlas setembro baixados dos emissores com SHA igual ao manifesto. `.txt` do estudo reproduzidos byte a byte por `pdftotext -layout`. ZIPs-pai atuais têm outros hashes (6918f7…, df4038…, detalhe ee996c…) frente a 9832ae…, 3cd620…, 63bbdc… do manifesto herdado.
- **02:** candidaturas oficiais (`consulta_cand_2026.zip`, SHA `e35ef1a7…`); decisão PJe de 02/10 aberta diretamente; notícias TSE 08/10, TRE-RJ 10/10 e 15/10, Senado, MPF e STF via WebFetch (download direto deu 403). Foram preservados excertos, não o HTML original.
- **03:** 25 linhas de ondas em `matriz-ondas.csv`; verificações V3-01 a V3-11 em `verificacoes-03.csv` (transcrições Datafolha, Paraná e Atlas; rejeição; 67/44 da onda 28/9–1/10; margem 6,51; 14,51; hashes; eleitores de Anthony 43/41; ficha Atlas).
- **05:** 22 URLs acessadas com HTTP/SHA; 41 registros de apoios/relações; 16 de campanha; réplica de peças com foto do g1 de 04/10 e cópia de 91 p. da inicial da AIJE no ConJur (não autenticada no PJe).
- **09:** S9-01 a S9-06 (`fontes-abertas.md`); foto `g1-santinho-0410.jpg`; `compatibilidade-cargos.json` (183 chaves iguais; presidente com turnos 1 e 2, governador só turno 1).

## 5. Reconferência dos achados altos
| Achado | Primeiro a apontar | Confirmação independente | Outras reconferências | Resultado |
|---|---|---|---|---|
| **P1-01 / A3-01**: onda Datafolha 2–3/10 omitida; "final" usado para a onda 28/9–1/10 | 01 (download curl 08:28–08:34; reconferência visual p.2, 8, 10 e 12 às 08:38–08:41) | **03: download próprio às 08:42 do mesmo URL do emissor, SHA-256 `b9448e38…` igual**; p.2/p.25, 8, 10 e 12; g1 de 03/10 18h18 com os mesmos números | 07: extração e render próprios do PDF compartilhado (p.8–12), sem novo download. 09: leitura visual da p.12 do PDF compartilhado. **Coordenação (09:04):** `pdftotext -f 10 -l 10` do PDF baixado por 03 traz a série Paes 51/49/48/47/**46** e Ruas 23/28/33/35/**38**; 8 − (−6,508) = **14,51 p.p.** e 12 − (−6,508) = 18,51 p.p. | **Erro confirmado, alta.** Válidos 46/38/7 (Paes +8); totais 41/34/6; número 75/52 (não 67/44); erro de margem 14,51 em vez de 18,51. A direção se mantém |
| **P1-02 / A3-02**: ondas finais e séries omitidas | 01 (Paraná original do emissor; Atlas 3/10 em republicação Poder360) | **03: Paraná outubro baixado de forma independente (SHA `70926dfa…`, igual ao original de 01)**; séries internas já presentes nos PDFs arquivados pelo estudo; Quaest e RTBD só secundárias | 07: leitura da extração do Paraná original (p.8–10) e render próprio do Atlas republicado (p.9) | **Sustentação insuficiente, alta.** Paraná 29/9–1/10: 41,9/30,1, válidos 47,9/34,4, série Ruas 15,5→20,3→26,7→30,1. Atlas 27/9–2/10: 46,4/38,0, válidos 48,6/39,8, **só republicação** (original no domínio Atlas não aberto). Nenhuma confirmação independente do Atlas no emissor |
Nenhum achado crítico foi identificado por nenhum revisor, então não houve reconferência de críticos.

## 6. O que NÃO foi executado ou acessado
| Item | Situação | Consequência |
|---|---|---|
| `scripts/download.py` | não executado (sobrescreveria snapshots e usaria a rede) | aquisição não reproduzida pelo código (R6-06) |
| Asset privado `dados-v1` | não baixado; substituído por download TSE byte-idêntico (SHA = digest do asset) | exigência do manifesto atendida por equivalência de bytes (R6-12) |
| Projeto vizinho e manifesto herdado | indisponíveis | procedência dos ZIPs-pai e da extração herdada não reverificável (P1-05, R6-05) |
| Nova aquisição e comparação dos ZIPs munzona com os SHA-pai do manifesto | 01 baixou os atuais (hashes diferentes por regeneração; conteúdo igual); ninguém obteve os pais históricos | só a identidade de conteúdo atual foi demonstrada |
| Descompressão integral do ZIP por 02, 04 e 07 | não feita (06 fez) | atribuída a 06 |
| Acórdão TSE de 08/10, decisão de 04/10, autos de proclamação, andamentos da ADPF 1362, certidão de trânsito | não obtidos | situação jurídica só por notícias institucionais e pela decisão interlocutória de 02/10 |
| Autos da AIJE no PJe, notícia 0600024-96.2026.6.19.0238, atos ID 127115068/127133860, auto de apreensão e nota original do TRE sobre santinhos, NFS-e, laudo | não obtidos (só cópia republicada da inicial) | autoria, tiragem e distribuição não verificadas |
| PesqEle | não consultado | registros das pesquisas não conferidos (A3-14) |
| Microdados e pesos das pesquisas; painel; pós-eleitoral | não obtidos | mudança tardia × seleção × ponderação × comparecimento inseparáveis |
| Originais Quaest, Atlas 3/10 (no domínio), Veritá; RJ-08712 conferido em detalhe; agregador 48,1/39,0 | não obtidos ou não conferidos | P1-03, P1-04/A3-05; Atlas só republicado |
| Relatório presidencial RJ Datafolha 22–24/09 com bases (S9-03) | não obtido | D3 não resolvida |
| RDV/BU 2026 e especificação legível | não obtidos (curl 403) | 204.309 não certificado |
| Detalhe presidencial cargo 1 (aptos, comparecimento, brancos, nulos) | não está nos insumos | comparação de participação entre cargos impossível (R4-06) |
| Microdados TSE 2018/2024 | não obtidos | R4-03 e R6-11 só documentais |
| Biblioteca de anúncios, peças originais, debates integrais, métricas de exposição | não obtidos | A5-03: efeito não mensurável |
| Teste em outro SO ou em Python 3.11 exato | não feito | — |
