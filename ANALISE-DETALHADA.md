# Análise detalhada

Recorte documental: 7/11/2026. A pergunta é por que a expectativa inicial sobre Paes não se realizou, distinguindo o resultado observado dos mecanismos ainda não identificados. [Resumo](README.md), [fontes](research/FONTES.md) e [tabelas completas](results/TABELAS.md).

## 1. O acontecimento que precisa ser explicado

A votação ocorreu em **4/10/2026**. O segundo turno nacional estava previsto para **25/10**, mas a eleição fluminense de governador terminou no primeiro turno após retotalização. Em 8/10, o TSE manteve o indeferimento de Anthony Garotinho e determinou a anulação dos seus votos; em 10/10 houve retotalização; em 15/10 o TRE-RJ proclamou Ruas eleito. A chapa eleita é Douglas Ruas/Fernanda Louback. A ADPF 1362 e a ação relatada em novembro impedem descrever o resultado como judicialmente incontroverso. Não foi obtida prova de trânsito em julgado. [TRE e STF, fontes F1–F4](research/FONTES.md).

Os oito candidatos com votos válidos estão na tabela reproduzida, com número e partido. A nona candidatura relevante é **Anthony Garotinho (Republicanos, 10)**, ausente das linhas de votos válidos do snapshot estadual. Não confundir com Rosinha, Wladimir ou Clarissa, nem atribuir posição uniforme ao conjunto da família.

| Conta | Antes da exclusão de Anthony | Após a retotalização |
|---|---:|---:|
| Votos de Ruas | 4.271.199 | 4.271.199 |
| Votos de Paes | 3.706.984 | 3.706.984 |
| Denominador válido | 8.669.038 | 8.394.627 |
| Ruas / denominador | 49,2696% | 50,8802% |
| Margem Ruas menos Paes | 564.215 | 564.215 |

A exclusão de 274.411 votos reduz o limiar de maioria pela metade desse volume. Ruas passa a ficar 73.885,5 votos acima da metade dos válidos. Isso explica o encerramento no primeiro turno, **não explica de onde vieram seus 4,27 milhões de votos**. A vantagem sobre Paes já existia antes. Não se pode afirmar quem venceria um segundo turno que não aconteceu.

## 2. Pesquisas: aproximação comprovada, instante da ultrapassagem desconhecido

![Série comparável](figures/pesquisas.svg)

| Campo Datafolha | Paes | Ruas | Anthony | Branco/nulo | Indecisos |
|---|---:|---:|---:|---:|---:|
| 18–20/8 | 41 | 19 | 9 | 16 | 4 |
| 8–10/9 | 43 | 25 | 10 | 9 | 3 |
| 22–24/9 | 43 | 30 | 8 | 6 | 4 |
| 28/9–1/10* | 42 | 31 | 7 | 8 | 4 |

Percentuais totais, pergunta estimulada com Anthony; série retrospectiva do relatório original de 1/10, publicado em 2/10. *A ficha técnica e as tabelas começam em 28/9; a narrativa do próprio relatório e a página começam em 29/9. A divergência foi preservada. As fichas completas das três ondas anteriores não foram obtidas; não se atribuiu a elas automaticamente a amostra da última onda.* [PDF](raw/datafolha-outubro.pdf).

A margem cai de 22 para 11 pontos no total estimulado. Ruas aumenta 12 pontos, enquanto Paes oscila um ponto para cima entre os extremos. Portanto, essa série **não descreve uma perda equivalente de Paes para Ruas**. O crescimento pode reunir antigos indecisos, terceiros, declarantes de voto inválido e mudanças nos dois sentidos. Sem painel, as entradas e saídas são desconhecidas. A faixa de indecisos estimulados, pequena, não representa toda a instabilidade: a espontânea final tinha 32% de indecisos, e 27% ainda admitiam mudança.

| Instituto/documento | Campo | Método/amostra | Paes / Ruas / Anthony | Base |
|---|---|---|---|---|
| Paraná, original | 5–7/9 | Presencial domiciliar; PPT nas duas primeiras etapas, quotas na última; 1.600, 57 municípios; ±2,5 p.p. | 43,5 / 20,3 / 9,8 | Total |
| Atlas, original | 22–27/9 | Recrutamento digital RDR e pós-estratificação; 1.836; ±2 p.p. | 44,1 / 35,7 / 6,3 | Total |
| Atlas, mesmo original | 22–27/9 | Mesma amostra | 45,0 / 36,4 / 6,4 | Válidos com Anthony |
| Datafolha, original | 28/9–1/10* | Presencial em pontos de fluxo; 1.204, 35 municípios; ±3 p.p. | 47 / 35 / 8 | Válidos com Anthony |
| Quaest, notícia CNN | 2–3/10 | 3.204; ±2 p.p.; método não conferido no original | 49 / 40 / 6 | Válidos com Anthony |
| Quaest, notícia CNN | 2–3/10 | Mesmo levantamento | 51 / 43 / — | Cenário sem Anthony |

[Dados e registros](data/pesquisas.csv). Margens declaradas para o conjunto da amostra, não automaticamente para subgrupos, diferenças entre candidatos ou cenários normalizados. A ficha Paraná informa 95% de confiança, assim como Atlas e Datafolha. Campo sobreposto e método diferente impedem ordenar institutos como se fossem uma única série temporal.

No Atlas, os gráficos das páginas 8 e 9 foram conferidos visualmente: não foram adotados os 48,1/39,0 encontrados em agregadores. A divergência permanece sem solução documental. Também há reportagem sobre Veritá com 42,3/41,9 válidos, campo 13–18/9, mas registros divergentes entre fontes (RJ-01332 e RJ-05322). O original não foi recuperado. É um **alerta contra a afirmação de unanimidade dos institutos**, não uma observação certificada incorporada à curva.

Com denominador comparável incluindo Anthony, a margem oficial Ruas–Paes era 6,51 pontos; Datafolha tinha Paes +12 e Quaest Paes +9. A diferença entre pesquisa e resultado é grande mesmo antes da retotalização. Logo, a decisão judicial **não explica o desencontro entre sondagens e votação**. [Teste reproduzido](results/pesquisas-confronto.json).

Não é legítimo converter 47% de intenção ou uma margem amostral de 95% em “95% de chance de vencer”. Uma previsão exigiria modelo de comparecimento, erro não amostral, correlação entre institutos, mudanças até a votação e validação histórica. Este estudo não construiu tal modelo. Expectativa jornalística de favoritismo, intenção medida, reconhecimento do nome e chance de vitória são grandezas distintas.

## 3. Ruas: base anterior, expansão e limites da explicação partidária

A votação oficial de 2022 foi **175.977 para deputado estadual**, com **149.576 em São Gonçalo (85,0%)**. A ficha da Alerj documenta sua trajetória; a ligação familiar com o prefeito Capitão Nelson é pública. A votação é evidência direta de inserção anterior, mais forte que a impressão de desconhecimento. Não é prova de retenção das mesmas pessoas quatro anos depois.

A candidatura recebeu aval de Flávio Bolsonaro, Castro e Altineu Côrtes na articulação partidária relatada em fevereiro. O cargo de secretário de Cidades e a presidência da Alerj oferecem canais de projeção e contato. São mecanismos plausíveis de viabilização; ocupar cargo não demonstra uso ilícito da máquina nem votos entregues. [Fontes F9–F11](research/FONTES.md).

O resultado de São Gonçalo, onde Ruas obteve 61,45% dos válidos e margem de 114.731, é consistente com essa base. Mas São Gonçalo responde por apenas uma parte da vantagem: **retirado o município da conta, Ruas ainda teria margem estadual de 449.484 votos**. Essa subtração é uma decomposição territorial, não o resultado de uma eleição hipotética sem a cidade.

Flávio Bolsonaro obteve no RJ **4.966.844 votos presidenciais no primeiro turno**, 695.645 acima de Ruas. Ruas ultrapassou a votação absoluta presidencial do 22 em apenas três municípios: São Gonçalo, Cambuci e Tanguá. Isso é compatível com um campo partidário amplo e um acréscimo local específico. Também impede igualar automaticamente o eleitorado de Ruas ao de Flávio. Os cargos têm quantidades distintas de válidos; não se pode ler a diferença como 695.645 pessoas que abandonaram Ruas.

O Datafolha final observou, entre declarantes de voto em cada candidato, conhecimento correto do número de **67% para Ruas e 44% para Paes**. Isso distingue familiaridade com a pessoa de capacidade declarada de identificar a opção na urna. Não demonstra que todos os que não sabiam o número erraram o voto, nem fornece estimativa do efeito de santinhos ou propaganda.

## 4. Paes: força real na capital, alcance estadual insuficiente

Paes venceu na capital com **53,50%**, 1.730.683 votos e margem de 410.961. Ruas teve 40,79%. Fora da capital, Paes ficou em **38,30%**, Ruas em **57,21%**. A capital concentrou 38,54% dos válidos estaduais: vencer ali não bastava. A derrota não deve ser narrada como desaparecimento total da popularidade carioca.

Em 2024, Paes havia recebido **1.861.856 votos e 60,47%** para prefeito, segundo o TSE. Em 2026, na mesma cidade, foram 131.173 votos e 6,97 pontos percentuais a menos. Cargo, adversários, alianças, participação e composição do eleitorado mudaram: não são 131.173 desertores identificados. Sua vantagem na capital se manteve, mas Ruas venceu em **9 das 49 zonas municipais**; a heterogeneidade carioca não pode ser ocultada pelo total da cidade. [Zonas](results/zonas.csv).

A rejeição de Paes no Datafolha permaneceu em 26% entre agosto e a última onda auditada, enquanto a de Ruas foi de 19% a 29%. Esse é um contraexemplo a uma explicação simples de “explosão da rejeição de Paes”. Crescimento de conhecimento também pode elevar rejeição e intenção simultaneamente. Faltam medidas anteriores comparáveis de conhecimento pessoal para quantificar o suposto anonimato inicial de Ruas.

Paes conquistou apoios fora da sua legenda e procurou prefeitos do interior. A aliança com Jane Reis e o grupo de Washington Reis oferecia uma ponte para a Baixada: o [próprio MDB anunciou o apoio em 19/2](https://www.mdb.org.br/mdb-e-psd-oficializam-alianca-para-o-governo-do-rio-com-chapa-paes-jane-reis/), antes da convenção de julho. Mesmo assim, na partição de 13 municípios da Baixada, Ruas somou vantagem de 309.109 votos; em Duque de Caxias, 30.129. Isso limita a tese de que endossos garantiam resultado local. Não prova que o apoio não ajudou Paes: faltaria o resultado contrafactual sem esse apoio.

## 5. Geografia: margens e volume, não somente vencedores

![Margens](figures/margem.svg)

Veja a [tabela de todas as regiões](results/TABELAS.md). A partição é **analítica e explicitamente reproduzida em `analyze.py`**. Capital, Baixada e Leste são separados; Região dos Lagos é apresentada junto das Baixadas Litorâneas (10 municípios); Centro-Sul foi acrescentado para cobrir o estado inteiro. A região Serrana inclui Petrópolis. Não se apresenta isso como uma classificação oficial única do IBGE.

Em uma segunda agregação sobreposta, a Região Metropolitana contém 22 municípios (Capital + Baixada + Leste + Petrópolis). **Essa linha não deve ser somada à partição anterior.** Malha e identificação dos 92 municípios vêm do IBGE; correspondência por nome normalizado é unívoca e auditada. O mapa usa geometria simplificada, sem reconstruir limites de zonas ou seções.

- **Metropolitana:** Ruas +82.243; fora da capital metropolitana, +493.204. O restante do estado contribuiu +481.972. Portanto, “foi o interior” omite metade do déficit de Paes fora da capital.
- **Baixada:** maior contribuição regional positiva para Ruas, +309.109. Nova Iguaçu e Belford Roxo tiveram margens maiores que Duque de Caxias.
- **Leste:** +161.567 para Ruas; São Gonçalo e Itaboraí contrastam com Niterói, onde Paes abriu 20.976. Não existe um bloco leste uniforme.
- **Lagos/Baixadas Litorâneas:** Ruas 66,13%, +174.921; contribuição maior que a do Norte, embora o Norte tenha centralidade na história de Garotinho.
- **Norte e Noroeste:** margens +79.030 e +44.084. Campos teve Ruas +46.438; Conceição de Macabu e Cardoso Moreira favoreceram Paes, assim como municípios do Noroeste.
- **Serrana, Costa Verde, Médio Paraíba e Centro-Sul:** +88.692, +44.123, +55.807 e +17.843. Valença favoreceu Paes; nenhum desses agregados substitui a tabela municipal.

Os dez municípios com maiores margens pró-Ruas somam **502.396 votos de vantagem**, 51,5% do saldo fora da capital. Há concentração importante e uma contribuição extensa dos demais. Ruas venceu 79 municípios, mas a contagem de cidades, sozinha, não mede a vitória: a capital vencida por Paes pesa mais que dezenas de municípios pequenos.

## 6. Anthony, Wladimir e a decisão judicial

O indeferimento de Anthony em setembro se relacionou à suspensão de direitos políticos por condenação de improbidade; a notícia do Senado distingue manutenção do indeferimento, rejeição da desistência do recurso e votação de 5 a 2 sobre anulação. **Não foi simplesmente uma retirada voluntária homologada**, como resumem algumas páginas. O inteiro teor completo não foi arquivado; a descrição jurídica usa documentos/notícias institucionais e é limitada a esse alcance.

Em 3/10 Anthony rejeitou apoio a Paes e considerou muito improvável apoiar Ruas; em 4/10 voltou a afastar apoio aos dois, segundo cobertura jornalística. Wladimir, em discurso após a votação, disse ter apoiado Anthony no primeiro turno e passou a apoiar Ruas. A notícia foi publicada em 5/10. A filiação de Wladimir ao PL não prova apoio anterior a Ruas. A posição de Clarissa e um inventário completo da rede de Rosinha não foram documentados suficientemente para atribuir-lhes um efeito.

O Datafolha perguntava por um segundo turno hipotético: entre apoiadores de Anthony, 43% diziam Paes e 41% Ruas. Isso enfraquece a suposição de destino único, mas não mede transferência real, tem base de subgrupo pequena e foi anterior ao resultado. Não se multiplicaram esses percentuais pelos 274.411 votos das urnas.

O arquivo por seção identifica nominalmente **Anthony William Garotinho Matheus de Oliveira**, número 10, com 274.411 votos. Eles reconciliam com os nulos técnicos em todas as 183 unidades município-zona; Campos concentra 43.421 (15,82% da votação de Anthony), e o Norte soma 56.952 (20,75%). Essa concentração documenta sua base territorial, não seu destino posterior. No mesmo território pode haver eleitores diferentes de Anthony e de Ruas. [Auditoria por seção](results/secoes-resumo.json).

A base contém 37.675 seções principais: Ruas supera Paes em 24.416, Paes supera Ruas em 12.998, com 261 empates. São comparações entre os dois nomes, não uma análise de quem ganhou todos os cargos. O voto nulo digitado aparece agregado no código 96: este arquivo não permite isolar a alegação de votos digitados como 13, nem inferir intenção de votar em Paes.

## 7. Redes, campanha e mensagens: o que está documentado

A matriz de [apoios e acontecimentos](research/CRONOLOGIA.md) distingue data do evento, publicação e força da fonte. Não foi produzido um índice de “máquina” a partir da legenda de prefeitos. Há registro de avanço de Paes entre gestores de partidos originalmente próximos de Ruas e de rupturas da aliança PL/PP; isso contraria uma versão de máquina estadual inteiramente unificada. A sucessão de Castro levou Ricardo Couto ao governo interino, portanto também é inadequado chamar todo ato do Executivo de ação de campanha de Ruas.

As sabatinas de setembro abordaram segurança, educação, orçamento e corrupção. A checagem da Lupa identifica falas e problemas factuais de ambos; não mede audiência efetiva, persuasão ou votos. A trajetória policial de Ruas torna a segurança um atributo eleitoral plausível; a gestão municipal de Paes torna serviços e capacidade administrativa atributos plausíveis. Nenhum desses vínculos estima o efeito de propostas.

A religião aparece em entrevistas individuais do Datafolha, não apenas no mapa: Paes tinha 48% entre católicos e 29% entre evangélicos; Ruas, 29% e 40%, respectivamente. São intenções declaradas, com margens de subgrupo maiores, não prova de obediência a pastores. O endosso de Malafaia é uma liderança específica; não representa todos os evangélicos. Nenhuma composição religiosa municipal foi convertida em preferência de pessoas.

A denúncia ajuizada por Paes em novembro inclui alegações de santinhos com número incorreto, desinformação e compra de votos. **Acusação não é fato judicialmente demonstrado**, e ocorrência de peça falsa não determina alcance nem mudança de voto. Faltam acervo periciado, origem, tiragem/distribuição, métricas de exposição e vínculo com decisões individuais. Da mesma forma, visualizações e engajamento em rede não seriam suficientes para inferir persuasão.

Há propostas concretas documentadas: em [entrevista à CNN](https://www.cnnbrasil.com.br/eleicoes/cnn-entrevista-eduardo-paes-candidato-ao-governo-do-rj-assista/), Paes defendeu unificar a segurança e recuperar o serviço ferroviário; Ruas apresentou segurança, transporte e saúde como prioridades na [entrevista de 17/8 à Record](https://record.r7.com/balanco-geral-rj/video/no-balanco-geral-rj-douglas-ruas-detalha-plano-de-governo-assista-a-entrevista-na-integra-17082026/). Na agenda de 7/9, [O Dia registrou](https://odia.ig.com.br/rio-de-janeiro/2026/09/7299647-candidatos-falam-em-propostas-para-educacao-e-bem-estar-animal.html) Ruas defendendo ampliação de escolas cívico-militares e Paes prometendo hospitais veterinários regionais. Isso comprova mensagens oferecidas, não sua recepção. Para transporte, economia, saúde, publicidade e debates, o corpus não oferece avaliação comparável de propostas e exposição com efeito mensurável. O projeto não atribui a esses temas uma quantidade de votos. Isso limita a conclusão causal, não a contabilidade da derrota. Uma explicação que escolha um debate ou um vídeo como causa principal excederia os documentos obtidos.

## 8. Participação: denominadores e saldos

Foram **12.842.517 aptos**, **9.845.867 comparecimentos**, **2.996.650 abstenções (23,33%)**, **501.537 brancos** e **949.703 nulos totais**, incluindo **274.411 nulos técnicos**. Brancos e nulos são, respectivamente, 5,09% e 9,65% do comparecimento. Somam-se válidos + brancos + nulos = comparecimento, em cada unidade município-zona. Não somar os votos de Anthony novamente aos nulos totais.

![Abstenção](figures/abstencao.svg)

A abstenção foi 26,16% na capital e 21,57% fora dela. Isso é compatível com oportunidades distintas de mobilização, mas não prova que ausentes preferiam Paes nem que o diferencial causou sua derrota. Aumentar artificialmente o comparecimento da capital supondo preferências constantes produziria um cenário, não uma estimativa. Este relatório não o apresenta como resultado observado.

Não há variação entre turnos de governador a calcular. O segundo turno presidencial teve outro conjunto de escolhas; usá-lo como segundo turno estadual inventaria um evento. Mesmo em comparações históricas, saldos líquidos não identificam antigos ausentes que voltaram, antigos votantes que faltaram ou mudanças de domicílio.

## 9. História e autonomia dos cargos

O PL já dispunha de grande votação: Castro recebeu 4.930.288 votos para governador em 2022, contra 4.271.199 de Ruas em 2026. O saldo de −659.089 **não é uma transferência identificada**; candidatos, coligações, conjuntura, eleitores e denominadores são diferentes. Demonstra, contudo, que a vitória de Ruas não exige imaginar um campo estadual criado do zero.

Paes teve 3.706.984 votos estaduais, muito acima dos 2.300.980 de Freixo em 2022; a comparação tampouco identifica a mesma coalizão ou eleitores. No primeiro turno presidencial de 2026, Lula teve 3.693.021 no RJ: a proximidade estadual com Paes oculta diferenças locais. Na capital, Paes superou Lula em 206.166 votos; fora dela, ficou 192.203 abaixo. Compensações agregadas não significam voto casado.

Em 2018, Paes já vencera na capital e perdera a disputa estadual para Witzel; essa comparação é contextual, apoiada em resultados TSE reproduzidos na imprensa, sem auditoria de microdados 2018 neste projeto. Em 2024, o sucesso municipal de Paes coexistiu com o campo presidencial da direita. Esses antecedentes impedem tratar identidade partidária como destino imutável de cada pessoa.

Municípios são a unidade de comparação histórica usada; não foi feito painel de zonas 2022–2026 porque reorganizações e seções agregadas exigem correspondência própria. A correspondência municipal IBGE atual não certifica automaticamente estabilidade de todas as fronteiras históricas. Não há regressão ecológica convertida em comportamento individual.

## 10. Melhor explicação e explicações rivais

A evidência permite ligar **sequência temporal** (crescimento de Ruas nas sondagens), **estrutura política anterior** (base local e apoios nacionais), **geografia da votação** (vantagem metropolitana periférica e interiorana) e **mecanismo jurídico** (redução do denominador). Essa combinação é mais informativa que uma lista de correlações.

Não permite repartir os votos de Ruas entre notoriedade pessoal, partido, líderes, religião, rejeição e mensagens. Mudança tardia, seleção/não resposta nas pesquisas, erro de comparecimento e dificuldade de converter intenção em voto são explicações concorrentes ainda abertas. Seria necessário painel pré/pós-eleição, microdados e ponderações dos institutos, auditoria de não resposta e participação, documentação de exposição e desenho capaz de distinguir seus efeitos. [Matriz completa](research/HIPOTESES.md).

**Resposta direta:** Paes perdeu apesar de liderar pesquisas porque o resultado efetivo lhe deu vantagem insuficiente na capital e desvantagem maior no resto do estado; o corpus não identifica precisamente por que as pesquisas ficaram distantes das urnas. Ruas ampliou uma base preexistente para uma votação estadual extensa, com associação política ao bolsonarismo documentada, mas sem decomposição causal dos apoios. Anthony Garotinho teve papel jurídico decisivo na dispensa do segundo turno; transferência efetiva de sua rede ou de seus eleitores para Ruas não foi demonstrada.
