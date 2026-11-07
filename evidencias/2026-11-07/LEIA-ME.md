# Evidências usadas na correção de 7/11/2026

Três operações diferentes:

1. **Reprodução dos cálculos.** `python3 scripts/reproduce.py` confere os hashes de `data/snapshot-manifest.json`, o `SHA256SUMS` desta pasta e os links locais. Não relê os PDFs e não decide se a fonte é verdadeira.
2. **Conferência da transcrição.** Abrir o arquivo e a página citados abaixo e comparar com `data/pesquisas.csv`. Foi feita nesta correção com `pdftotext -layout` e, nas páginas de gráfico, com leitura da imagem renderizada por `pdftoppm`.
3. **Autenticação da fonte.** Hash igual ao download da auditoria mostra que o arquivo é o mesmo byte obtido em 7/11/2026. Não prova que o conteúdo já fosse esse antes, nem que uma republicação seja o original do instituto.

As datas da coluna `obtido_em` vêm de `catalogo-fontes-auditoria.csv`, o catálogo da auditoria, no fuso −03:00. São aquisições de 7/11/2026, não registros históricos do estudo. `Last-Modified` é o cabeçalho HTTP gravado nesse download, não uma data inventada.

Para verificar os arquivos já arquivados, nesta pasta:

```bash
sha256sum -c SHA256SUMS
```

Para baixar de novo, use a URL da tabela, grave o arquivo com outro nome, calcule o SHA-256 e a data de hoje. Se o hash divergir, é uma aquisição nova: não substitua o arquivo arquivado e não altere o `SHA256SUMS` para forçar a igualdade.

## Documentos e o que cada um sustenta

| Arquivo | Grau | URL | Obtido em (−03:00) | SHA-256 | Versão / cabeçalho | Páginas usadas |
|---|---|---|---|---|---|---|
| `pdfs/datafolha-final-0310.pdf` | Original Datafolha | https://media.folha.uol.com.br/datafolha/2026/10/05/xdwelu0lqnxn2-5oke87g-v2.pdf | 2026-11-07T08:34:11 | `b9448e38a6180aa7ad04cd445081a26b5980d82df20247bf555a718b0f4061a9` | PDF v2. HTTP Date 07/11 11:32:47 GMT. Last-Modified 05/10/2026 17:00:46 GMT | p.2 ficha 02–03/10, n=2.002, RJ-01334/2026 e BR-07933/2026; p.8 totais 41/34/6; p.10 válidos, inclusive 22–24/9 = 48/33/9 e 2–3/10 = 46/38/7; p.12 número 57 / 75 / 52 |
| `pdfs/datafolha-final-0310.html` | Página do instituto | https://datafolha.folha.uol.com.br/eleicoes/2026/10/na-vespera-da-eleicao-eduardo-paes-psd-tem-46-dos-votos-validos-douglas-ruas-pl-cresce-e-alcanca-38.shtml | 2026-11-07T08:34:02 | `1f2080ce8ae679b390c1618c26bd9bd3741756f0a43048f8dade71cec348ecb8` | HTTP Date 07/11 11:34:02 GMT. Título com data 04/10/2026 | Data editorial 04/10/2026 no título. Não substitui o PDF |
| `pdfs/datafolha-governo-rj-outubro.pdf` | Impressão de matéria do g1, não é original Datafolha | https://static.poder360.com.br/uploads/2026/10/datafolha-governo-rj-outubro.pdf | 2026-11-07T08:33:10 | `ef2bc352a1209dffbff9b3666b344444d862abd6ebfe6bc49bd1a04cd4f4c1e8` | HTTP Date 07/11 11:33:10 GMT. Last-Modified 04/10/2026 01:35:20 GMT | Diz “03/10/2026 18h18” e válidos 46/38/7. A hora depende desta impressão |
| `pdfs/parana-RJ_Out26-original.pdf` | Original Paraná Pesquisas | https://paranapesquisas.com.br/wp-content/uploads/2026/10/RJ_Out26.pdf | 2026-11-07T08:33:22, catálogo do revisor 01 | `70926dfa18d7a747f4f8b65ffd9becee5a87399883b92890a3534ffa5695d183` | Cabeçalho arquivado é o do revisor 03: Date 07/11 11:43:00 GMT. Last-Modified 02/10/2026 17:12:38 GMT | p.3 coleta 29/09–01/10, n=1.600, 54 municípios, ±2,5, RJ-07095/2026; p.8 totais 41,9/30,1/8,2; p.9 válidos 47,9/34,4/9,4; p.10 série 15,5 → 20,3 → 26,7 → 30,1 |
| `pdfs/Pesquisa-Atlas_Estadao-Eleicoes-Rio-de-Janeiro-2026-261003.pdf` | Republicação integral do Poder360. O original no domínio da Atlas não foi localizado | https://static.poder360.com.br/uploads/2026/10/Pesquisa-Atlas_Estadao-Eleicoes-Rio-de-Janeiro-2026-261003.pdf | 2026-11-07T08:33:09 | `b7a7d3ea63ed13195ec53d223caf57caea9ed2e427c839632597ac5e8f5c7bdd` | HTTP Date 07/11 11:33:09 GMT. Last-Modified 03/10/2026 23:36:57 GMT | p.5 coleta 27/09/2026–02/10/2026, n=2.244, ±2, RJ-02601/2026; p.8 totais 46,4/38,0/6,1; p.9 válidos 48,6/39,8/6,4; p.10 rótulos 31 ago, 20 set, 28 Set e 03 Out |
| `raw/atlas-setembro.pdf` | Original Atlas, já estava no estudo | https://cdn1.atlasintel.org/pesquisa_atlas__eleicoes_rio_de_janeiro_2026__260928_692ebb57cee1632a.pdf | 2026-11-07T08:28:35, conferido ao manifesto | `200b30bbf8eb8d231fc5470dd6cdc744ed87feb25996f9ea7c67787d20eec121` | Hash também em `data/snapshot-manifest.json` | p.4 método; p.5 coleta só 22/09/2026–27/09/2026; p.8–9 a onda dessa ficha; p.10 os rótulos 31 ago, 20 set e 28 Set, sem outra ficha |
| `pdfs/quaest-rio-de-janeiro-outubro-governador.pdf` | Impressão de matéria do g1, não é original Quaest | https://static.poder360.com.br/uploads/2026/10/quaest-rio-de-janeiro-outubro-governador.pdf | 2026-11-07T08:33:11 | `12e2b9eec3cc98ed3c9c68a116e21652c199b4dbad969e53d07b7c759bf6f9bf` | HTTP Date 07/11 11:33:10 GMT. Last-Modified 04/10/2026 01:38:07 GMT | “modelo likely voter”; válidos 49/40; totais 35/28; indecisos 15; branco/nulo/não vai votar 13. A CNN em `raw/quaest-final-cnn.html` não traz isso |

Os nove pareceres estão em `pareceres/`. As réplicas que separam as divergências estão em `replicas/REPLICA-A3-13.md` (BR-05193 é presidencial; a RTBD de governador é RJ-08712) e `replicas/REPLICA-PECAS.md` (o texto da peça é “Lula é 13”, não “Paes governador 13”).

## O que continua sem o documento

| Afirmação | O que falta | Confiança |
|---|---|---|
| Atlas 27/9–2/10 no domínio da Atlas | PDF original em cdn1.atlasintel.org ou no site do instituto | Os números 46,4/38,0 e 48,6/39,8 ficam como republicação. Não são original |
| Real Time Big Data 37/31/7 e 35/25 | PDFs RJ-08712 e RJ-03902 conferidos visualmente | Baixa. Não entram no gráfico |
| Quaest além da matéria do g1 | Relatório do instituto | Secundária. O modelo e os totais dependem da impressão do g1 |
| PesqEle, microdados, pesos, acórdão de 8/10, RDV | Não estão neste pacote | Lacunas em `research/LACUNAS.md` |
