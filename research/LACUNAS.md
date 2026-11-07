# Lacunas declaradas

Corte: 7/11/2026. Este quadro separa o que foi procurado e não obtido, o que não foi investigado e o que os dados usados não podem responder. Não transforma ausência de documento em ausência do fato. A trilha abaixo é a da auditoria independente e dos manifestos deste repositório. Esta correção não refez as buscas externas nem rodou `download.py`.

| Questão | Documento | Canal e data | Resultado | Tipo |
|---|---|---|---|---|
| Fundamento completo do julgamento de Anthony | Acórdão de 8/10 e certidão de trânsito | Notícia do TSE (F19) e do Senado (F3), lidas em 7/11; PJe da decisão de 2/10 aberto na auditoria | Notícia obtida. Acórdão e certidão não obtidos | Suprível |
| Segundo turno pedido pelo PSD | Andamentos da ADPF 1362 e decisão de mérito | Notícia e página de andamento do STF, sem bytes preservados | Prestação de informações em 27/10. Decisão de mérito não encontrada no corpus | Suprível; busca não exaustiva |
| Proclamação | Autos da proclamação | Notícias do TRE de 10/10 e 15/10; download direto 403 | Texto lido por ferramenta web. HTML não arquivado | Suprível |
| Fichas oficiais das pesquisas | PesqEle | Não consultado | Registros citados nas fontes não foram conferidos. A ordem dos números não segue a ordem das ondas; isso pode ser normal e não foi verificado | Suprível. Não é evidência de ficha falsa |
| Separar mudança tardia, seleção, ponderação e comparecimento | Microdados, pesos e questionários | PDFs e matérias dos contratantes | Não obtidos. A Quaest original, a Atlas de 3/10 no domínio do instituto e a Veritá também não | Suprível |
| Cruzamento presidente × governador | Relatório presidencial do Datafolha 22–24/9, RJ-02205/2026 e BR-05762/2026, com matriz e bases | g1 25/9 e Folha 26/9 | Condicionais publicadas. Matriz não obtida. As duas rotas não fecham | Suprível. Uso só qualitativo |
| Agregador 48,1/39,0 | Página do agregador e data | Busca em 7/11 | Não localizado. Números retirados da série | Não verificável |
| Quem digitou 13 para governador | RDV, BU e especificação de 2026 | g1 6/10; especificação oficial retornou 403 | 204.309 não certificado. 204.309 ≤ 675.292 é só compatibilidade | Suprível para a digitação. A intenção continuaria inacessível |
| Denominadores do cargo presidencial | Detalhe de votação do cargo 1, com aptos, comparecimento, brancos e nulos | Os insumos têm só votos nominais presidenciais | Não está no snapshot | Suprível |
| Procedência dos ZIPs nacionais | SHA dos ZIPs-pai de 1/11 e manifesto do projeto vizinho | `prepare.py` sem o projeto vizinho; sem novo download dos ZIPs nacionais | Hash herdado não reverificado aqui. A auditoria viu conteúdo igual ao TSE de 7/11 e SHA diferente por regeneração | Suprível |
| Asset `dados-v1` | O ZIP publicado na release | CDN do TSE nesta correção | SHA-256 igual ao manifesto e ao digest registrado pela auditoria. O asset privado em si não foi baixado | Equivalência de bytes, não autenticidade |
| Santinhos | Auto de apreensão, nota do TRE, PJe da AIJE 0605082-18.2026.6.19.0000, notícia 0600024-96.2026.6.19.0238, NFS-e e laudo | g1 4/10 e 6/10; cópia de 91 páginas da inicial no ConJur, não autenticada no PJe | Peças separadas. Autoria, tiragem e distribuição só alegadas | Suprível |
| Cada Garotinho | Agendas, listas de participantes e declarações originais | CBN 19/8 | Rosinha e Clarissa descritas. Sem lista e sem votos atribuíveis | Suprível |
| Apoios nominais | Originais de prefeitos, vereadores e líderes | Reportagens já usadas na cronologia | Catálogo parcial. Base de vereadores não certifica endosso | Suprível; o que existe não esgota o universo |
| Efeito de publicidade e debates | Anúncios originais, biblioteca, programas e métricas | O Globo 1/10; sabatinas e Lupa | Mensagens descritas. Exposição e efeito não medidos | Suprível para o inventário. O efeito pode continuar não identificável |
| 2018 e 2024 | Microdados TSE | Imprensa para 2018; notícia do TSE para 2024 | Sem recorte preservado | Suprível |
| Zonas 2022–2026 | Cadastro de seções e locais | Códigos de zona nos dois anos | 183 códigos iguais. Território não verificável | Suprível com o cadastro |
| Bases dos gráficos do Datafolha | Definição do instituto | PDFs | Não identificadas. Não se conclui a direção da ponderação | Não verificável neste corpus |
| Fala de Anthony em 4/10 e sucessão de Couto | URL ou documento | Busca no repositório | Sem fonte preservada | Não verificável aqui |

Impossibilidade dos dados, distinta de documento faltante: saldos municipais não são fluxos de pessoas; anulação não é transferência; RDV não recupera intenção nem pareia cargos; intenção de pesquisa não é probabilidade de vitória.
