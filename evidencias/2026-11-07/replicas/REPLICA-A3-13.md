# Réplica do Agente 1 ao achado A3-13 do Agente 3, e delimitação da "autenticação" do snapshot eleitoral

Feita em 07/11/2026, das 08:56 às 08:58 BRT (America/Sao_Paulo, UTC-3), pelo relógio do box. Li só a linha 63 e a linha A3-13 (l.194) de `03-pesquisas.md`, além das linhas desse arquivo que mencionam "autenticação" (l.15, 93, 109, 203, 226). Não alterei o relatório do Agente 3.

## 1. A3-13: BR-05193 é presidencial e a RTBD de governador é RJ-08712/2026

**Posição: concordo. Era um erro meu, agora confirmado e corrigido.**

Evidências:

| Item | Arquivo / URL | Resultado |
|---|---|---|
| PDF que eu registrei como "RTBD governador" | `evidencias/curl/poder360/Rio-de-Janeiro-BR-05193-2026-Set26.pdf` (baixado 08:33:10 BRT de https://static.poder360.com.br/uploads/2026/10/Rio-de-Janeiro-BR-05193-2026-Set26.pdf). A página do Poder360 (`evidencias/curl/poder360-pesquisas-rj.html`) liga esse arquivo com o rótulo "Real Time Big Data" | Capa (pdftotext p.1): "PESQUISA REGISTRADA: BR-05193/2026 … PESQUISA PRESIDENCIAL RIO DE JANEIRO". As perguntas são "ESTIMULADA PRESIDENTE" (Flávio Bolsonaro, Lula). **Zero** ocorrências de "governador". Imagem da capa: `evidencias/imagens/replica/rtbd-br05193-01.png` |
| Mesmo PDF no emissor | https://realtimebigdata.com.br/wp-content/uploads/2026/09/Rio-de-Janeiro-BR-05193-2026-Set26.pdf, baixado 08:56:30 BRT, `evidencias/curl/replica/…-emissor.pdf`, Last-Modified 30/09/2026 13:58:49 GMT | SHA-256 2f71a257… **idêntico** ao do Poder360: a republicação reproduz o arquivo do emissor, e o arquivo é presidencial |
| RTBD de governador no emissor | https://realtimebigdata.com.br/wp-content/uploads/2026/09/Rio-de-Janeiro-RJ-08712-2026-Set26.pdf, baixado 08:56:29 BRT, `evidencias/curl/replica/Rio-de-Janeiro-RJ-08712-2026-Set26.pdf`, SHA 65bc0e7b…, 31 p., pdfinfo CreationDate 29/09/2026 18:41 -03, Last-Modified 30/09 13:58:54 GMT | Capa: "PESQUISA REGISTRADA: RJ-08712/2026 … PESQUISA ESTADUAL"; campo 25–29/9; 2.000 entrevistas; ±2,0. Estimulada cenário 01 (`curl/replica/rtbd-rj.txt` l.97–108): Paes 37, Ruas 31, Garotinho 7, nulo/branco 8. **Não** conferi visualmente nem em detalhe |
| Contexto (republicações, não confirmação independente) | Broadcast 30/9; Diário do Rio 30/9; Statmapa (agregador do PesqEle) | Coerentes com o emissor: a Broadcast diz "estadual RJ-08712/2026 e presidencial BR-05193/2026". A coerência é com a mesma origem (o próprio instituto) |

**Origem do meu erro.** Atribuí o arquivo pelo rótulo do link no agregador (Poder360) e pelos metadados de campo e amostra, que coincidem com os da pesquisa estadual: mesmo campo e mesmo n. Não li o conteúdo. No inventário escrevi "não extraído em detalhe", mas mesmo assim cravei um registro errado.

**Impacto.** Baixo. Eu não usei números da RTBD. P1-02 só a listava como omitida, e continua omitida, agora com o registro correto.

**Correções feitas, com trilha:**
- `inventario-fontes.md`, linha 41: a linha antiga foi riscada com nota de correção, e foi acrescentada uma linha para RJ-08712/2026. A versão anterior está em `evidencias/inventario-fontes.v2-antes-replica-A3-13.md`.
- `../01-procedencia.md`, P1-02 item (c): BR-05193 trocado por RJ-08712/2026, com nota; a seção "não abri" foi ajustada. A versão anterior está em `evidencias/01-procedencia.v2-antes-replica-A3-13.md`.
- `achados-01.csv`, P1-02: texto ajustado. A versão anterior está em `evidencias/achados-01.v2-antes-replica-A3-13.csv`.
- `/workspace/rj26/revisao/catalogo/fontes.csv`: a linha antiga não foi apagada. Acrescentei uma linha de CORREÇÃO para a URL do Poder360 e duas linhas para os PDFs do emissor (BR-05193 e RJ-08712), com flock.

## 2. Snapshot eleitoral: o que chamo de autenticação e o que os meus logs sustentam

### Definições operacionais usadas

1. **Integridade.** Os bytes de um arquivo são iguais a um hash de referência (SHA-256). Só diz que o arquivo não mudou em relação àquele hash. Se o hash vem do próprio autor, a referência não é externa.
2. **Mesma origem (concordância derivada).** Duas fontes concordam porque derivam do mesmo processo. Exemplos: notícias do TRE-RJ, da Agência Senado e do STF repetindo a totalização e a decisão do TSE; Poder360 republicando um PDF. Mostra coerência de publicação, **não** confirmação independente.
3. **Canal emissor.** O arquivo foi obtido no domínio oficial de quem produz o dado (cdn.tse.jus.br; domínio do instituto), por HTTPS com verificação TLS padrão do curl (sem `-k`), com cabeçalhos HTTP guardados. Liga o conteúdo ao emissor **no instante do acesso**.
4. **Comparação de conteúdo.** Igualdade, registro a registro, entre o recorte do estudo e o arquivo atual do canal emissor. Serve quando os bytes mudam por regeneração mas os dados não mudam.
5. **Veracidade e independência histórica.** O número corresponde ao que de fato ocorreu (urnas, boletins), e o conteúdo era o mesmo em datas passadas, comprovado por fonte independente (arquivo de terceiros com data, boletins de urna, autos). **Não testei isso.**

Chamo de **"autenticação operacional"** apenas a combinação de 3 e 4: o recorte do estudo tem o mesmo conteúdo que o canal emissor servia em 07/11/2026, de 08:28 a 08:30 BRT. Não é veracidade e não é independência.

### O que os logs e as comparações sustentam

| Evidência | Sustenta | Não sustenta |
|---|---|---|
| `curl/votacao_2026.zip.headers`, `votacao_2022.zip.headers`, `detalhe_2026.zip.headers` (HTTP/2 200 de cdn.tse.jus.br; Date 11:28:45–11:29:34 GMT; Last-Modified 07/11 09:14, 07/11 07:28 e 06/11 22:46 GMT) e `votacao2026.sha`/`votacao2022.sha` | Os ZIPs foram servidos pelo CDN oficial nesse instante, com esses hashes (6918f7…, df4038…; detalhe ee996c…) | Que os ZIPs fossem iguais aos usados pelo estudo: **os hashes diferem** dos SHA-pai do manifesto (9832ae…, 3cd620…, 63bbdc…). Não testei a integridade dos ZIPs-pai do estudo |
| `comparacao-votacao2026-repo-vs-tse-atual.txt` | 1.464 linhas de governador 2026: mesmas chaves (turno, município, zona, SQ_CANDIDATO, trânsito) e todos os campos iguais, exceto DT/HH_GERACAO (01/11 no estudo, 07/11 no TSE). Nenhuma diferença, nem de maiúsculas | Que o conteúdo fosse igual entre 01/11 e 07/11 sem interrupção. Que os números sejam verdadeiros (são a publicação oficial, não uma medição independente) |
| `comparacao-detalhe-repo-vs-tse-atual.txt` | 183 linhas idênticas (comparação exata após `strip`), exceto geração (31/10 vs 06/11). Totais: válidos 8.394.627; nulos técnicos 274.411 | O mesmo que acima |
| `comparacao-presidente-e-2022-repo-vs-tse-atual.txt` | Presidente 2026 (2.562), presidente 2022 (2.379), governador 2022 + Ruas (1.464): chaves e campos iguais, exceto geração | **Limite:** comparação sem distinguir maiúsculas (`.upper()`), então diferenças só de caixa não seriam detectadas. A contagem bruta de linhas atuais não foi impressa separadamente das chaves; duplicatas no arquivo atual se colapsariam |
| `sha256-catalogo-secoes-RJ.txt` + `catalogo/aquisicao/tse-download-20261107T112708Z/headers.txt` (download feito por outro agente, Date 11:27:08 GMT, Last-Modified 26/10/2026 17:53:09 GMT) | **Integridade** do ZIP de seções contra o manifesto (ec93c0…), obtido do canal emissor. Neste caso, há identidade de bytes, não só de conteúdo | Que o asset da release `dados-v1` tenha sido conferido por mim: quem afirma a igualdade é o `ref.MANIFEST.txt` do coordenador. Veracidade |
| `secoes-zip-totais-governador.txt`, `secoes-governador-csv-totais.txt` | Coerência interna: as somas por seção igualam os totais municipais e o detalhe | Independência: são todos produtos do mesmo sistema de totalização do TSE |
| WebFetch TRE-RJ, Senado, STF, TSE 2024 (sem bytes preservados; curl 403 no TRE/STF) | Publicações institucionais que repetem os mesmos totais e as mesmas decisões | Confirmação independente dos números (mesma origem factual); autos; ata no DJe |
| Código das comparações | Os resultados foram gravados em arquivo | **Limite:** o código Python rodou *inline* no shell e não foi salvo como script; os CSVs extraídos grandes foram apagados (reprodutíveis com `unzip` a partir dos ZIPs preservados em `evidencias/curl/`) |

### Diferença em relação ao Agente 3 sobre "snapshot não autenticado"

É divergência terminológica, sem conflito de evidência.
- Ele escreve "não autenticado" no sentido de que **ele** não autenticou e de que não há veracidade independente. Concordo com esse limite.
- Eu sustento só a autenticação operacional: conteúdo igual ao canal emissor em 07/11, e integridade de bytes no caso das seções. **Retiro qualquer leitura mais ampla.** A margem de 6,51 p.p. e os 564.215 votos são "conforme a publicação oficial do TSE acessada em 07/11", não "verificados de forma independente".

**Ajuste no parecer 01.** A Síntese 1 já distingue o que é conferido de veracidade, e a Síntese 2 trata a mesma origem. Não há nova correção além da RTBD. Para não haver leitura ampla, valem as definições desta réplica.

## Limitações desta réplica

- Não conferi visualmente o PDF RJ-08712, nem os seus demais cenários e séries.
- Não consultei o PesqEle diretamente (o Statmapa é um agregador).
- Não reexecutei as comparações TSE.

## O que permanece divergente

Nada quanto a A3-13. Quanto à autenticação, a divergência é só terminológica, nos termos acima.
