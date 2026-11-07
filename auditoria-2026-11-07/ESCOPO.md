# ESCOPO — Auditoria independente do estudo RJ 2026 (consolidação da coordenação)

Consolidado pela coordenação (Grok Bot) em 07/11/2026, por volta das 09:05–09:30 (horário de Brasília, UTC−3). Todos os horários deste arquivo estão nesse fuso, salvo indicação.

## 1. Objeto
- **Repositório:** `RafaelPanisset/estudo-rj-2026` (privado).
- **Commit auditado:** `f7278de8335458be2f290c15b9a63a220954d639`, "Add reviewer for omitted factors and presidential influence", 07/11/2026 08:21:24 −03:00. Commits anteriores do mesmo dia: `3d708854…` (08:10:02) e `5884a450…` (08:09:51) (`catalogo/aquisicao/snapshot/git-log.txt`).
- **Data de corte:** **07/11/2026**. Os revisores usaram só evidência publicada até essa data. Os documentos acessados em 07/11 foram registrados com a data de acesso. Isso não prova que tivessem o mesmo conteúdo em datas anteriores (ver `agentes/01-procedencia.md`).

## 2. Cadeia de aquisição da referência
1. **Snapshot do código:** `git archive` do commit fixo, obtido pela integração oficial do GitHub (cloud agent): `catalogo/aquisicao/snapshot/estudo-rj-2026-f7278de.tar.gz` (6.531.938 bytes; SHA-256 `f7236bda5375ae31c92f2e4738c0f5cf7ffa1cc766dc0bd42f7932e39717e4dc`, conferido pela coordenação e igual ao prefixo e sufixo citados em `ref.MANIFEST.txt`), mais `git-log.txt` e `ls-tree.txt`.
2. **Montagem da referência somente leitura:** `/workspace/rj26/ref`, montada em 07/11/2026 às 08:31:21. **Os 65 blobs Git foram conferidos com a árvore da API GitHub, com 0 divergências.** Conferiram de forma própria os revisores 02, 05, 06 e 07 (`work/tree.json`; a árvore foi obtida pela coordenação, não pela API por cada revisor). A referência não tem `.git`, então `git rev-parse` não se aplica.
3. **ZIP de seções (296 MB) exigido pelo manifesto:** o asset da release privada `dados-v1` **não foi baixado**. No lugar dele, foi usado um download direto do CDN do TSE (`catalogo/aquisicao/tse-download-20261107T112708Z/secoes-RJ.zip`; cabeçalho HTTP `Date: Sat, 07 Nov 2026 11:27:08 GMT` = 08:27:08 BRT; `Last-Modified: 26/10/2026 17:53:09 GMT`). Ele tem **296.106.129 bytes e SHA-256 `ec93c020ae1f0088216de92e5acc5d3211aefaf1fa589b961132bbf471ee3cf5`**, igual a `data/snapshot-manifest.json`, a `data/secoes-download.json`, ao COMO-USAR e ao digest que a API do GitHub informa para o asset `dados-v1` (conferido pelo revisor 06 com `list_releases`). A **exigência do ZIP de 296 MB foi atendida pelo download TSE byte-idêntico**. Ela não foi removida (R6-01, R6-12). A cópia em `ref/raw/secoes-RJ.zip` é o mesmo arquivo.
4. **Verificação da coordenação no fechamento (07/11, 09:04):** `sha256sum -c` das 66 entradas de `ref.MANIFEST.txt` (65 arquivos do Git mais o ZIP) deu **66/66 OK**. A referência continua intacta.

## 3. Ambiente, ferramentas e capacidades
- Box Linux compartilhado (Debian 13, kernel 6.12, 8 CPUs, 16 GB, segundo o revisor 06), Python 3.13.5 só com a biblioteca padrão (o estudo original usou 3.12.3), poppler 25.03.0, curl, sha256sum e unzip. Os revisores 01, 02, 03, 05 e 09 usaram WebSearch/WebFetch. Nenhuma integração nova foi instalada. Não houve browser com conta, push, commit, PR, release, publicação nem mensagem externa.
- **Nove bots revisores reais com prefixo RJ26** foram criados e coordenados (01 Procedência, 02 Resultados, 03 Pesquisas, 04 Estatística, 05 Redes, 06 Reprodução, 07 Explicações, 08 Aderência, 09 Fatores omitidos). Sequência: fase 1 (01, 02, 06), fase 2 (03, 04, 05, 09), fase 3 (07, 08), depois réplicas (01→A3-13; 05→peças) e reconferência dos altos.
- **Limites de independência:** os bots compartilham computador, arquivos e credenciais. Cada revisor registrou as primeiras observações antes de ler os pareceres alheios. Mesmo assim, 04 e 07 declaram que a mensagem de coordenação já trazia números de outros revisores, então a leitura não foi cega. O parecer 02 descreve a si mesmo como "papel executado como braço do revisor, não como novo bot independente". O número de revisores concordantes não foi tratado como probabilidade de verdade.
- Execuções do estudo só em cópias de trabalho (`/workspace/rj26/work/06-reproducao/`, `work/04-estatistica/`). Só o revisor 06 executou os scripts de reprodução.

## 4. Fontes desta consolidação
- `agentes/01-procedencia.md` … `agentes/09-fatores-omitidos.md` e as pastas de cada um (versões atuais). Inclui `01-procedencia/RECONFERENCIA.md` e `REPLICA-A3-13.md`, e `05-redes/REPLICA-PECAS.md`. `01-procedencia/RESULTADO-INTERMEDIARIO.md` está **superado** e não foi usado como fonte de conclusão.
- `coordenacao/notas.md`, `/workspace/rj26/ref.MANIFEST.txt` e `catalogo/` (`fontes.csv` e `aquisicao/`).
- Script desta consolidação: `coordenacao/consolidar_achados.py`, que gera `ACHADOS.csv` a partir dos CSV/JSON dos agentes e das transcrições dos achados que só existem em Markdown (R7-01/02, A9-01/02/03).

## 5. O que ficou fora (escopo não executado)
- `scripts/download.py` (sobrescreveria snapshots e usaria a rede) e nova aquisição dos ZIPs munzona nacionais para verificar os SHA-pai do manifesto herdado. O revisor 01 baixou ZIPs atuais do TSE: os hashes **diferem** dos SHA-pai (regeneração), mas o conteúdo é idêntico campo a campo, exceto a geração.
- O asset privado `dados-v1` (substituído pelo download TSE byte-idêntico) e o projeto vizinho `analise-eleitoral-2026` (`prepare.py` falha sem ele).
- Acórdão de 08/10, decisão de Nunes Marques de 04/10, autos da proclamação, andamentos completos da ADPF 1362, certidão de trânsito em julgado, autos e anexos autenticados no PJe da AIJE 0605082-18.2026.6.19.0000, notícia de irregularidade 0600024-96.2026.6.19.0238, auto de apreensão e nota original do TRE sobre os santinhos.
- PesqEle, microdados e pesos das pesquisas, originais da Quaest, do Atlas (no domínio próprio) e da Veritá, relatório presidencial RJ do Datafolha 22–24/09 com bases (matriz de S9-03), agregador "48,1/39,0".
- RDV e BU de 2026 e especificação técnica legível; detalhe de participação presidencial (cargo 1); microdados TSE de 2018 e 2024.
- Exposição, alcance e efeito de publicidade, peças ou debates; painel ou pesquisa pós-eleitoral.
- Aplicação de correções ao estudo (etapa posterior, fora deste escopo).

## 6. Exclusões do pacote `revisao-rj26.zip`
O ZIP contém a pasta `revisao/` inteira, **exceto**:
| Arquivo excluído | Tamanho (bytes) | Motivo |
|---|---:|---|
| `revisao/catalogo/aquisicao/tse-download-20261107T112708Z/secoes-RJ.zip` | 296.106.129 | ZIP TSE de 296 MB (SHA-256 `ec93c020…3cf5`); recuperável no TSE ou na release `dados-v1` |
| `revisao/agentes/01-procedencia/evidencias/curl/votacao_candidato_munzona_2026.zip` | 466.449.807 | Arquivo acima de 50 MB; ZIP nacional do TSE baixado em 07/11 (SHA-256 `6918f759…379a`) |
| `revisao/agentes/01-procedencia/evidencias/curl/votacao_candidato_munzona_2022.zip` | 579.575.416 | Arquivo acima de 50 MB; ZIP nacional do TSE baixado em 07/11 (SHA-256 `df403887…401a`) |

Também não entram: a referência `/workspace/rj26/ref` (inclusive `ref/raw/secoes-RJ.zip`) e as cópias de trabalho `/workspace/rj26/work/`, que ficam fora de `revisao/`.
