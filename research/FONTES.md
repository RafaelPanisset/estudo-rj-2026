# Fontes e decisões de procedência

Fontes consultadas até 7/11/2026. URLs, datas de obtenção e hashes estão no [registro de downloads](../data/download-manifest.json), no [manifesto dos recortes TSE](../data/source-manifest.json) e no [registro do ZIP de seções](../data/secoes-download.json). Os hashes permitem conferir se os arquivos mudaram. A comparação com o TSE se refere ao conteúdo disponível em 7/11; não comprova que versões anteriores fossem iguais.

## Documentos centrais

| ID | Fonte | Uso e limite |
|---|---|---|
| F1 | [TRE-RJ, retotalização 10/10](https://www.tre-rj.jus.br/comunicacao/noticias/2026/Outubro/retotalizacao-de-votos-aponta-douglas-ruas-como-vencedor-no-primeiro-turno-para-o-governo-do-rj) | Totais e efeito do denominador; página lida por ferramenta web, sem cópia local; download direto 403 |
| F2 | [TRE-RJ, proclamação 15/10](https://www.tre-rj.jus.br/comunicacao/noticias/2026/Outubro/tre-rj-proclama-douglas-ruas-pl-governador-eleito) | Resultado proclamado; não equivale a trânsito em julgado; download direto 403, sem snapshot local |
| F3 | [Senado, julgamento 8/10](https://www12.senado.leg.br/noticias/materias/2026/10/08/rio-de-janeiro-garotinho-tem-votos-anulados-e-douglas-ruas-sera-declarado-governador-eleito) | Distingue indeferimento, desistência rejeitada e anulação; notícia institucional, não inteiro teor. Não é confirmação independente da notícia do TSE |
| F4 | [STF, ADPF 1362](https://noticias.stf.jus.br/postsnoticias/psd-pede-ao-stf-realizacao-de-segundo-turno-para-governador-do-rio-de-janeiro/) e [andamento](https://portal.stf.jus.br/processos/detalhe.asp?incidente=7724240) | Ação do PSD. Em 12/11/2026 o portal e a peça da medida cautelar foram arquivados. O último andamento confirmado nessa leitura é a liminar indeferida por ora, sem mérito. O despacho de 16/10 é passo anterior. Ver a [seção provisória](SEGUNDO-TURNO.md) |
| F5 | [Datafolha, relatório 2/10](https://media.folha.uol.com.br/datafolha/2026/10/02/n99iwiwkfastqk40w8-wzdovosu-7-st-wj-w16-788.pdf) | Original arquivado; ficha p.2, série total p.10, válidos p.12; campo contraditório dentro do documento. Não é a última onda |
| F6 | [Paraná, setembro](https://paranapesquisas.com.br/wp-content/uploads/2026/09/RJ_Set26.pdf) | Original; metodologia p.3 e cenário p.8 |
| F7 | [Atlas, setembro](https://cdn1.atlasintel.org/pesquisa_atlas__eleicoes_rio_de_janeiro_2026__260928_692ebb57cee1632a.pdf) | Original; método na p.4, totais na p.8 e válidos na p.9; gráficos conferidos visualmente. A p.10 traz rótulos de série |
| F8 | [Quaest final, CNN 3/10](https://www.cnnbrasil.com.br/eleicoes/quaest-eduardo-paes-tem-49-no-1o-turno-no-rj-douglas-ruas-40/), HTML em `raw/quaest-final-cnn.html` | A CNN é assistida por IA e traz só os válidos 49/40/6. O g1 de 3/10, lido na auditoria numa impressão do contratante, informa modelo de eleitor provável e totais 35/28/4. Original Quaest não recuperado |
| F9 | [Alerj, perfil de Ruas](https://www.alerj.rj.gov.br/Deputados/PerfilDeputado/478?AspxAutoDetectCookieSupport=1&Legislatura=20) | Biografia institucional; usada para conferir a trajetória, não para avaliar o desempenho |
| F10 | [O Dia, escolha de Ruas pelo PL, fevereiro](https://odia.ig.com.br/rio-de-janeiro/2026/02/7212908-pl-escolhe-douglas-ruas-como-candidato-ao-governo-do-rio.html) | Relato da articulação com Flávio, Castro e Altineu; não prova entrega de votos |
| F11 | [Exame, prefeitos, 13/7](https://exame.com/brasil/disputa-por-prefeitos-acirra-corrida-ao-governo-do-rio-entre-paes-e-douglas-ruas/) | Reproduz apuração de O Globo; contagem de apoios não é censo independente deste projeto |
| F12 | [NF Notícias, Wladimir, 5/10](https://www.nfnoticias.com.br/noticia-56820/eleito-deputado-federal-wladimir-garotinho-declara-apoio-a-douglas-ruas-no-20-turno-no-rj) | Relata declaração após votação em 4/10, apoio anterior ao pai e posterior a Ruas |
| F13 | [CNN, Anthony, 3/10](https://www.cnnbrasil.com.br/eleicoes/garotinho-rejeita-paes-pondera-sobre-ruas-e-enfrenta-reves-na-justica/) | Posição declarada antes da eleição; não preferência de seus eleitores |
| F14 | [Lupa, sabatinas de 8 e 11/9](https://www.agencialupa.org/checagem/2026/09/11/em-sabatina-ruas-e-paes-omitem-processos-e-tiram-de-contexto-dados-sobre-o-rio/) | Temas e verificação de declarações; não mede persuasão |
| F15 | [CNN, ação de Paes, 4/11](https://www.cnnbrasil.com.br/eleicoes/eduardo-paes-pede-ao-tre-rj-cassacao-de-chapa-de-douglas-ruas/) | Alegações, não fatos provados; inicial completa e perícia não obtidas |
| F16 | [TSE, reeleição de Paes em 2024](https://www.tse.jus.br/comunicacao/noticias/2024/Outubro/prefeito-do-rio-de-janeiro-eduardo-paes-psd-e-reeleito-para-o-cargo) | 1.861.856 e 60,47%; dado documental. O recorte TSE de 2024 não está nos insumos e não foi recalculado |
| F17 | [IBGE, municípios RJ](https://servicodados.ibge.gov.br/api/v1/localidades/estados/33/municipios) e [malha](https://servicodados.ibge.gov.br/api/v3/malhas/estados/33?formato=application/vnd.geo+json&qualidade=minima&intrarregiao=municipio) | Identificação e desenho territorial atual; não características dos eleitores |
| F18 | [TSE, calendário](https://www.tse.jus.br/comunicacao/noticias/2026/Marco/eleicoes-2026-confira-as-principais-datas-do-calendario-eleitoral) | Datas oficiais 4 e 25/10 |
| F19 | [TSE, julgamento de 8/10](https://www.tse.jus.br/comunicacao/noticias/2026/Outubro/tse-decide-pela-retotalizacao-dos-votos-para-governador-no-rio-de-janeiro) | Parcial provimento quanto à alínea “l”; indeferimento mantido por direitos políticos e filiação; anulação por 5 a 2. Notícia, não acórdão. Excerto lido na auditoria |
| F20 | [Datafolha, 2–3/10, PDF v2](../evidencias/2026-11-07/pdfs/datafolha-final-0310.pdf) | Original arquivado. Ficha p.2; totais p.8; válidos p.10; número p.12. Não é a impressão do g1 |
| F21 | [Paraná, outubro](../evidencias/2026-11-07/pdfs/parana-RJ_Out26-original.pdf) | Original arquivado. Metodologia p.3; totais p.8; válidos p.9; série p.10 |
| F22 | [Atlas 27/9–2/10, republicação Poder360](../evidencias/2026-11-07/pdfs/Pesquisa-Atlas_Estadao-Eleicoes-Rio-de-Janeiro-2026-261003.pdf) | Republicação integral, não o PDF do domínio da Atlas. Ficha p.5; totais p.8; válidos p.9; série p.10. “31 ago” e “20 set” são rótulos, sem ficha |
| F30 | [g1 sobre o Datafolha, impressão](../evidencias/2026-11-07/pdfs/datafolha-governo-rj-outubro.pdf) | Não é original do Datafolha. A página salva diz 03/10/2026 18h18 e válidos 46/38/7 |
| F31 | [g1 sobre a Quaest, impressão](../evidencias/2026-11-07/pdfs/quaest-rio-de-janeiro-outubro-governador.pdf) | Não é original da Quaest. Diz modelo likely voter, válidos 49/40 e totais 35/28, indecisos 15, branco/nulo/não vai votar 13 |
| F23 | [g1, santinho, 4/10 17h12](https://g1.globo.com/rj/rio-de-janeiro/eleicoes/2026/noticia/2026/10/04/panfletos-investigacao-mprj-tre.ghtml) | Foto com Paes, Jane Reis e 22; localização em Nova Iguaçu atribuída a fiscais. Sem auto |
| F24 | [g1, cruzamento, 25/9](https://g1.globo.com/rj/rio-de-janeiro/eleicoes/2026/noticia/2026/09/25/datafolha-no-rj-presidencia-25-setembro.ghtml) | Intenção presidente × governador. Sem matriz nem bases. A condicional inversa está na Folha de 26/9, sem URL arquivada aqui |
| F25 | [CBN, clã Garotinho, 19/8](https://cbn.globo.com/coberturas/eleicoes-2026/noticia/2026/08/19/cla-garotinho-busca-unir-forcas-para-retomar-protagonismo-eleitoral-no-rj-apos-anos-de-conflitos.ghtml) | Rosinha no interior e Clarissa nos bastidores. Sem agendas |
| F26 | [O Globo, publicidade, 1/10](https://oglobo.globo.com/politica/eleicoes-2026/noticia/2026/10/01/douglas-ruas-vira-entre-evangelicos-e-eduardo-paes-reage-com-campanha-amigo-das-igrejas-nas-redes.ghtml) | Peças impulsionadas descritas. Sem métrica de exposição. O URL é o da reportagem lida na auditoria |
| F27 | [g1, RDV, 6/10](https://g1.globo.com/rj/rio-de-janeiro/eleicoes/2026/noticia/2026/10/06/coligacao-paes-denuncia-panfletos.ghtml) | Alega 204.309 confirmações do 13. Não certificado |
| F28 | [TSE, ordem de votação](https://www.tse.jus.br/comunicacao/noticias/2026/Marco/eleicoes-2026-conheca-a-ordem-de-votacao-na-urna-eletronica) | Governador antes de presidente |
| F29 | [TSE, votação segura](https://www.tse.jus.br/eleicoes/processo-eleitoral-brasileiro/votacao/votacao-segura) | RDV registra o digitado, sem identificar o eleitor nem parear cargos. BU agrupa brancos e nulos |

## Fontes complementares

- [Veritá, reportagem Portal Política](https://portalpolitica.com.br/pesquisa-verita-no-rio-de-janeiro-paes-e-douglas-ruas-aparecem-tecnicamente-empatados-para-o-governo/): números e registro divergem de outros cadastros; relatório original não recuperado. Excluída da série certificada.
- [Resultado 2018 com dados TSE, UOL](https://placar.eleicoes.uol.com.br/2018/2turno/rj/) e [capital em 2018](https://especiais.gazetadopovo.com.br/eleicoes/2018/resultados/municipios-rio-de-janeiro/rio-de-janeiro-rj/governador/): contexto histórico; microdados 2018 não auditados.
- [PP não indica novo vice, 22/7](https://www.metropoles.com/colunas/igor-gadelha/pp-decide-nao-indicar-novo-vice-para-candidato-de-flavio-no-rio): mostra instabilidade das alianças, não efeito eleitoral.
- [Wladimir, entrevista 12/7](https://mancheterj.com/douglas-ruas-ou-anthony-garotinho-wladimir-explica-quem-apoiara-na-eleicao-para-governador/): contexto familiar/partidário; a declaração posterior com escolha explícita foi priorizada.
- [Malafaia, edição de 24/2](https://tribunadosmunicipios.com.br/wp-content/uploads/2026/02/Tribuna-3330-TM.pdf): relato de apresentação de Ruas em templo, não uma posição de toda denominação.
- [Regiões e fronteiras, Alerj](https://www3.alerj.rj.gov.br/lotus_notes/default.asp?id=161&url=L3NjcHJvMTkyMy5uc2YvMThjMWRkNjhmOTZiZTNlNzgzMjU2NmVjMDAxOGQ4MzMvRDZBMTY0Rjc1NUMxMUVDMTgzMjU4NEI3MDA1Mjk0MEU%2FT3BlbkRvY3VtZW50): explicita diferenças de classificação em relação à Região Metropolitana; a partição analítica é publicada integralmente no código.

## Divergências e pontos não confirmados

1. Datafolha: 28/9 versus 29/9 como início de campo no mesmo documento. O CSV usa a ficha técnica, com nota.
2. Atlas de setembro: PDF original 45,0/36,4 válidos. Os 48,1/39,0 atribuídos a agregadores não têm referência rastreável e foram retirados da série.
3. Veritá: registro conflitante e original indisponível; sem certificação.
4. Algumas notícias dão margem de 564.214 votos; a subtração dos totais oficiais é **564.215**.
5. O TSE afastou a inelegibilidade da alínea “l”, mas manteve o indeferimento por direitos políticos e filiação. O placar de 5–2 se refere à anulação dos votos. A desistência não foi homologada.
6. Notícias de 4–9/10 que anunciam segundo turno descrevem expectativa daquele momento, não um segundo turno efetivamente realizado.
7. O cruzamento do g1 de 25/9 e a condicional inversa da Folha de 26/9 não fecham entre si. Uso só qualitativo.
8. A margem de ±3 p.p. atribuída à Atlas de outubro pelo Estadão não coincide com os ±2 p.p. da ficha republicada. A divergência fica registrada e não entra nos cálculos.

Wikipedia, redes sociais e agregadores foram usados para localizar documentos e hipóteses, não como prova final de fraude, transferência, preferências religiosas ou resultado oficial.
