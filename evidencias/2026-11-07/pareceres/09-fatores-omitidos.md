# Agente 9 — Fatores omitidos e conversão do voto

## 1. Escopo e síntese da rodada inicial

**Referência somente leitura:** `/workspace/rj26/ref`, commit informado `f7278de8335458be2f290c15b9a63a220954d639`. **Corte:** 07/11/2026, America/Sao_Paulo (UTC−3). Revisão documental delimitada, não auditoria integral nem investigação judicial. Não clonei, não executei reprodução/scripts do estudo, não fiz commits, conexões, publicações ou mensagens externas. Escrita somente nesta entrega e em `09-fatores-omitidos/`.

**Resultado:** o estudo já distingue corretamente alegação, endosso e voto; não transforma brancos/nulos em votos de Paes nem saldos territoriais em fluxos individuais. Contudo, há documentação disponível que permite ir além da ressalva genérica de “faltam dados”:

1. **Santinho Paes–22:** notícia contemporânea de 04/10 e foto publicada mostram uma pista localizada muito mais específica que a referência genérica à ação de novembro. A foto contém “GOVERNADOR EDUARDO PAES / JANE REIS / 22”; o número correto estadual de Paes é 55, o 22 estadual é Ruas. O g1 atribui ao TRE localização por fiscais em Nova Iguaçu e anúncio de inquérito. Isso sustenta investigar existência/circulação localizada, **não autoria, tiragem estadual, exposição efetiva, digitação ou efeito decisivo**. Não obtive exemplar original, auto de apreensão ou nota original do TRE.
2. **Cruzamento entre cargos:** reportagem do contratante do Datafolha de 25/09 publica intenções presidenciais dentro dos grupos de intenção estadual (campo 22–24/09). Portanto, há evidência individual publicada, além de coincidências municipais. É evidência secundária metodologicamente parcial, não painel, voto realizado ou prova de transferência presidencial.
3. **Digitação dos nulos:** g1 de 06/10 atribui a RDVs 204.309 confirmações de 13 para governador. Não certifiquei esse total; o CSV de seções só fornece o agregado 96. A descrição oficial do TSE esclarece que o RDV registra digitação e não permite vincular votos entre cargos ou ao eleitor. Existe caminho documental/técnico concreto para testar a digitação, **sem recuperar intenção ou motivo**. Não basta rejeitar o dado porque não está no CSV nem aceitá-lo sem insumo técnico.
4. **Onda final Datafolha omitida (P1-01 do agente 1, sem duplicação):** reconferi no PDF compartilhado e visualmente na p.12: conhecimento correto sobe de 67%/44% para **75% Ruas / 52% Paes**, bases 602/886, margens declaradas 4/3 p.p. Não saber não equivale a errar; erro declarado tampouco equivale a confirmação de voto errado. O dado pré-eleitoral já era assimétrico e melhora nos dois grupos; não mede efeito do santinho de 04/10.

**Nenhum fator foi demonstrado decisivo.** Nenhum achado próprio crítico/alto; as lacunas documentais próprias abaixo são médias. A atualização alta de pesquisas é tratada no P1-01 do agente 1. A contabilidade e a dispensa do segundo turno estadual não são refutadas por estes achados.

## 2. Independência, leitura e método

Primeiras observações em `09-fatores-omitidos/00-observacoes-iniciais.md`, registradas **antes** de abrir pareceres alheios. A mensagem prévia do coordenador sobre turnos e última onda era conhecida e foi marcada como informação a conferir, não evidência. Depois li 01, 02 e 06 e suas fontes compartilhadas; reli a versão atualizada de 01 após orientação do coordenador. P1-02 é sustentação insuficiente por omissão de ondas, não acusação de que o estudo teria negado outras séries.

Lidos integralmente PROMPT-GROK, BRIEFING-ORIGINAL e COMO-USAR; README, ANALISE-DETALHADA, FONTES, HIPOTESES e CRONOLOGIA. Inspeção de `analyze.py`, `prepare.py` e `territory.py` somente como documentos. Ferramentas: Read, rg, Python 3 (inspeção de chaves/domínios e escrita), WebSearch/WebFetch, curl público, pdftoppm. Nenhum código de terceiro executado. Não usei quantidade de revisores concordantes como prova nem aleguei isolamento estatístico.

Fontes novas abertas estão transcritas com URLs e limites em `09-fatores-omitidos/fontes-abertas.md` (S9-01 a S9-06). Fontes já adquiridas por outros revisores foram lidas, não novamente baixadas. Datas das fontes, nomes, cargo e números foram confrontados com os arquivos locais; não usei fontes de 2022/2024 para descrever evento de 2026. Exceção metodológica: a página TSE “Votação segura” é geral e sem data editorial na extração, identificada como tal, não manual específico de formato de 2026.

## 3. O que o santinho permite afirmar

### Três peças/mecanismos que não podem ser fundidos

| Peça/pista | Conteúdo e identidade | Fonte, tempo e lugar | Autoria e classificação permitida |
|---|---|---|---|
| Paes–22 | Foto publicada: retrato identificado pelo g1 como Paes, “GOVERNADOR”, “EDUARDO PAES”, “JANE REIS”, “22”, “POR UM RIO DE JANEIRO MAIS FORTE” | S9-01, 04/10/2026 17h12 Brasília; Nova Iguaçu segundo reportagem; imagem `g1-santinho-0410.jpg` lida visualmente | Número incompatível com a candidatura estadual de Paes. Não é mera propaganda conjunta com cargos explicitados na face visível. Reportagem chama os santinhos de falsos e atribui localização aos fiscais; não fiz perícia de montagem, impressão, data/local da foto ou autoria. Nenhuma campanha identificada como autora comprovada; verso não visto |
| Paes–Lula/13 versus Ruas–Flávio/22 | Segundo denúncia descrita pela CNN, Paes e Lula associados ao 13, Ruas e Flávio ao 22 | `01-procedencia/evidencias/curl/acao-novembro.txt` l.1 e S9-02; alegação de material anterior ao pleito | Associação de candidatos presidenciais e estaduais não é, por si, instrução enganosa. Exige ler imagem completa, legendas de cargo e contexto. O mecanismo alegado 13 produziria nulo estadual; o 22 estadual é candidato válido. Não confundir consequências |
| “Valores cristãos/família” | Denúncia relata 100 mil panfletos negativos Paes/Lula e positivos Ruas/Flávio | CNN04/11 relata denúncia em30/09 | Tiragem de100 mil é alegação sobre esta peça, não quantidade comprovada de Paes–22. Mensagem pode atuar por rejeição/persuasão sem erro de número. Autoria e alcance não verificados |

A resposta de Ruas em S9-01 é contraevidência à atribuição automática de autoria à campanha beneficiária aparente: declarou-se também prejudicado e pediu investigação. Isso **não prova sua inocência nem autoria de adversário**. As matérias podem compartilhar nota/foto/origem; não são múltiplas confirmações independentes. A mera imagem estabelece apenas a publicação daquela representação visual; a reportagem acrescenta relato atribuível de localização física. Auto de apreensão e cadeia de custódia seriam avanço distinto.

### Cadeia produção → circulação → exposição → compreensão → intenção → digitação → voto

| Elo | Observado nesta rodada | Elo ainda necessário |
|---|---|---|
| Produção | Foto de impresso; petição noticiada aponta gráfica em Niterói e pede perícia | Arquivo-matriz, exemplar original, ordens/faturas, perícia e autoria; pedido não equivale a perícia concluída |
| Circulação | Reportagem contemporânea atribui aos fiscais localização em Nova Iguaçu | Auto, quantidade, endereços, horários, agentes de distribuição; não assumir disseminação estadual |
| Exposição | Não medida; peça no chão não prova leitura por eleitor | Amostra de exposição anterior à votação e alcance geográfico/temporal |
| Compreensão | Pesquisa anterior mede resposta sobre número pretendido; foto permite analisar ambiguidade | Teste de compreensão da peça específica; não converter não sabe em compreendeu errado |
| Intenção | Pesquisas independentes transversais e cruzamento entre cargos | Painel/exposição datada; intenção antes e depois; alternativas partidárias/locais |
| Digitação | CSV só código96; notícia de RDV lista13 e outros números, ainda não certificada | RDV oficial validado, filtro2026/RJ/governador/turno1, cobertura, esquema e reconciliação com BU/96 |
| Voto registrado | Opções22/55 e nulos estão contabilizados; 22 é voto nominal válido estadual | Nenhum registro administrativo revela se22 foi erro ou escolha deliberada. RDV não associa cargos nem pessoa; confirmação na urna não identifica preferência anterior |

TSE S9-04 documenta ordem: federal, estadual, dois senadores, **governador e depois presidente**. Nome, foto, cargo e partido exibidos na urna são oportunidade de correção, não prova de que todos perceberam/entenderam. O mesmo22 em cargos sucessivos é mecanismo plausível de simplificação;13 para governador e22 para governador são mecanismos distintos. Não há demonstração de que a ordem tenha causado erro em quantidade determinada.

## 4. Influência presidencial, pesquisas cruzadas e compatibilidade

**Resultados:** `compatibilidade-cargos.json` confere 2026/RJ/cargo1 na base presidencial, turnos1 e2, e cargo3/turno1 no nominal estadual. Nos dois recortes, trânsito=N; as183 unidades município–zona do primeiro turno são iguais. O arquivo presidencial tem2.562 linhas e o estadual1.464. `scripts/analyze.py` l.31–35 seleciona explicitamente turno1 na comparação presidencial, usa válidos presidenciais próprios e números22/13. O arquivo contém Flávio Bolsonaro e Lula, não Jair Bolsonaro como candidato presidencial de2026. Não encontrei mistura de turno2 no cálculo documental examinado. Chaves iguais não provam mesmos votantes: eleitores habilitados a cada cargo, votos válidos e eventuais omissões têm denominadores próprios. Não conferi universo/participação presidencial com arquivo de detalhe próprio; esse é pedido ao revisor4.

**Turnos:** base presidencial contém segundo turno; governador só primeiro, consistente com proclamação do TRE15/10 (`02-resultados/fontes/tre-proclamacao-webfetch-excertos.md` l.7–8) dispensando segundo turno. Essa notícia institucional, já aberta na revisão2, é a evidência positiva sobre encerramento estadual. O ZIP de seções restrito ao primeiro turno **não prova sozinho** a inexistência de segundo turno estadual. Também não se deve usar a notícia de06/10 que ainda previa segundo turno como prova de realização posterior.

**Cruzamento individual publicado — S9-03:** Datafolha22–24/09,1.204 entrevistas, RJ-02205/2026 e BR-05762/2026, reportagem do contratante Globo/Folha. Entre declarantes estaduais: Paes→Lula64%/Flávio20%; Ruas→Flávio86%/Lula5%; Garotinho→Flávio47%/Lula34%. Percentuais restantes não foram imputados. Margem geral de3p.p. não vale automaticamente para subgrupos. Sem bases/ponderações/matriz completa, não teste diferenças de subgrupos nem inverta condicional:86% Flávio entre Ruas não é86% Ruas entre Flávio.

A evidência converge com alinhamento partidário e traz contraexemplo direto à identidade perfeita dos campos (declarações Paes–Flávio e Ruas–Lula). Não prova direção temporal da influência: preferência presidencial pode influir no governador, liderança estadual pode reforçar a presidencial, ambas podem refletir identidade política anterior ou redes locais. Apoio de Flávio, partido22, avaliação de Lula, rejeição nacional, mobilização e mensagem moral são mecanismos separáveis. Original desta onda/microdados, painéis e estudo pós-eleitoral com metodologia **não foram obtidos**; não concluo inexistência.

**Datafolha final:** PDF compartilhado `01-procedencia/evidencias/curl/datafolha-final-0310.pdf`: campo2–3/10, n2.002/35municípios, RJ-01334/2026 e BR-07933/2026, abordagem pessoal em pontos de fluxo, checagem mínima20%; p.2. P.12 visualmente reconferida: Ruas75 corretas/24 não sabe/1 incorreta, Paes52/44/4; bases602/886, margens4/3p.p.; total57/40/3, base1.769 na lâmina. A diferença descritiva de acerto permanece23p.p.; os níveis mudam e ambos melhoram. O anexo de detalhamento informa base ponderada total1.788: não confundir base ponderada com entrevistas; encaminhar eventual conciliação ao revisor de pesquisas. PDF tem caminho05/10 e metadado de criação05/10 segundo P1-01: campo é anterior ao voto, documento/publicação não devem ser automaticamente datados como03/10. Para o corte07/11 a disponibilidade é compatível. Não é medição posterior do dano causado no domingo.

## 5. Matriz obrigatória de hipóteses

| Hipótese | Mecanismo | Evidência favorável | Evidência contrária/limitante | Cronologia | Alcance observado | Elo faltante | Alternativa | Conclusão permitida | Dado necessário |
|---|---|---|---|---|---|---|---|---|---|
| Santinho Paes–22 alterou registro estadual | Preferência Paes, instrução22, confirmação Ruas | Foto com nome/cargo22; relato de fiscais S9-01 | Tela identifica Ruas; campanha Ruas pede apuração; autoria/efeito ausentes |04/10, durante dia do primeiro turno; horário real de exposição não conhecido | Nova Iguaçu segundo reportagem; sem quantidade | Exposição→compreensão→confirmação e intenção prévia | Peça vista e rejeitada/ignorada; voto22 deliberado; montagem não periciada | Pista específica de existência/circulação localizada; não fator decisivo | Auto, exemplares, custódia, tiragem, distribuição, estudo individual |
| Associação Paes–Lula/13 anulou escolhas estaduais | Troca de cargo/número produz13 nulo | Denúncia CNN; notícia RDV204.309 S9-02 | Nulo13 pode ser deliberado ou outro erro; total não certificado | Alegação anterior ao pleito; notícia06/10 | Alegação sobre estado; RDVs não lidos | Exposição e intenção antes do13 | Protesto, memória partidária, desinformação diversa | Investigar digitação; não “votos perdidos por Paes” | RDVs/esquema/cobertura e pesquisa de motivos; perícia das peças |
| Assimetria de conhecimento dificultou conversão de intenção | Mais dificuldade para localizar número55 | DF75/52 final e67/44 anterior |52% não significa48% erro; menções incorretas são4% Paes; cola/tela/correção possíveis |22–24/09→2–3/10; antes do domingo | Grupos declarantes na amostra, não eleitorado inteiro | Resposta→digitação confirmada | Campanha esclarecedora; medição de lembrança sem efeito | Assimetria descritiva apoiada; magnitude eleitoral indeterminada | Painel, apoio na votação, exposição, simulação validada |
| Campo presidencial ajudou expansão Ruas | Identificação partidária, líder, número compartilhado, mobilização | Apoios prévios no corpus; cruzamento86% Flávio entre Ruas; votação presidencial ampla | Voto cruzado declarado; absolutos diferentes; endosso não entrega | Apoios anteriores; cruzamento setembro; turno1 em04/10 | Intenções e resultados agregados RJ | Mudança individual atribuível ao vínculo nacional | Base local/familiar, candidato, segurança, seleção prévia | Alinhamento apoiado; efeito presidencial causal não identificado | Matriz original, painéis/motivos, exposição e rede local comparáveis |
| Rejeição nacional prejudicou Paes | Associação Lula desperta rejeição/mensagem moral | Peça alegada de valores; alinhamento parcial em S9-03 |20% Paes declaravam Flávio; série do estudo não mostra explosão de rejeição Paes | Mensagens alegadas até30/09; campo pré-eleição | Sem audiência medida | Mensagem→rejeição→mudança | Avaliação estadual, serviços, rivalidade partidária anterior | Plausível e testável, sem peso atribuível | Série rejeição/motivos, originais de peças e alcance |
| Acontecimento tardio explica diferença pesquisa–urna | Mudança após última entrevista, convencimento/mobilização | DF final19% admitiam mudar; Ruas cresce até34 totais | Pesquisas ainda Paes à frente; séries transversais não são painel |2–3/10→04/10 | Amostra prévia; sem evento causal medido | Evento/exposição→mudança/comparecimento | Não resposta, seleção, ponderação, modelo de comparecimento | Não há virada causal datada; atualizar ondas antes de discutir | Microdados, pesos, auditoria de campo, painel pré/pós |
| Abstenção diferencial decidiu | Mobilização desigual de preferências | Análise122: capital maior abstenção | Preferências dos ausentes desconhecidas; composição/denominadores distintos |04/10 | Taxas territoriais, não trajetórias | Ausente→preferência contrafactual | Estrutura demográfica e mobilidade | Descrição de taxas sustentada; decisão causal não | Estudo de comparecimento individual, universo e pesos |
| Anulação Anthony causou migração a Ruas | Expectativa jurídica induz voto útil antes; exclusão muda denominador depois | Decisão02/10; exclusão274.411 após voto | Anulação posterior não adiciona votos; Wladimir endossa depois; intenções de segundo turno divididas |02/10 antes;08–15/10 depois | Efeito contábil conhecido; persuasão não | Conhecimento jurídico→decisão pré-voto | Voto consolidado, redes independentes | Separar voto útil prévio, ainda aberto, de retotalização contábil estabelecida | Painel datado sobre informação jurídica e decisão; não multiplicar pesquisa por votos anulados |

Incidentes técnicos, filas, transporte e compra de votos não receberam hipótese causal nova sem documento específico suficiente. A CNN relata denúncias de compra, não demonstra ocorrência/magnitude; encaminhar acervo ao revisor5. A ordem de votação é verificada como condição do mecanismo, não nova explicação comprovada. Não fiz cenários de sensibilidade nem estimativas de votos desviados.

## 6. Achados no formato obrigatório

### A9-01 — Investigação de santinhos permanece genérica apesar de pista contemporânea localizada
- **Agente:**9.
- **Arquivo/linhas:** `ANALISE-DETALHADA.md` l.102,112; `research/HIPOTESES.md` l.17; `research/FONTES.md` l.23 (F15).
- **Afirmação:** denúncia de novembro inclui santinhos incorretos; falta acervo/perícia/alcance.
- **Problema:** cautela correta, mas não identifica a peça Paes–22, seu cargo, local e notícia contemporânea de localização por fiscais nem a resposta de Ruas; também não separa13 nulo de22 válido ou tiragem alegada de outra peça. É tratamento parcial da pista, não falsidade da cautela.
- **Fonte/comando:** S9-01 e S9-02 abertos via WebFetch; leitura visual de `g1-santinho-0410.jpg`; CNN compartilhada `01-procedencia/evidencias/curl/acao-novembro.txt` l.1; candidaturas em `02-resultados/fontes/candidaturas-rj-filtradas.json` (números55/22).
- **Status:** sustentação insuficiente (completude da investigação).
- **Gravidade:** média.
- **Confiança:** alta na omissão textual e no conteúdo da foto publicada; média na ocorrência física relatada, sem auto/nota original; baixa para autoria/alcance/efeito, que não afirmo.
- **Impacto:** melhora o diagnóstico de “mera acusação geral” para pista concreta e localizada; não muda vencedor nem demonstra fraude atribuível à chapa.
- **Correção:** anexar imagem contextualizada e reportagem de04/10 como secundárias; solicitar auto de apreensão, representação, perícia, autoria e distribuição; separar peças/efeitos e não declarar decisividade.

### A9-02 — Evidência individual cruzada publicada ficou fora do exame presidencial
- **Agente:**9.
- **Arquivo/linhas:** `README.md` l.18; `ANALISE-DETALHADA.md` l.61,130,140; `research/HIPOTESES.md` l.7.
- **Afirmação:** apoio político e votação presidencial sustentam associação; faltam cruzamentos individuais por voto realizado/motivação.
- **Problema:** falta de voto realizado/painel é real, mas há cruzamento **de intenção** publicado em25/09 que pode qualificar o alinhamento e os contraexemplos sem esperar desenho causal perfeito. A fonte não aparece no catálogo do estudo. Não atribuo ao estudo a afirmação de inexistência de qualquer cruzamento.
- **Fonte/comando:** S9-03, WebFetch, RJ-02205/2026 e BR-05762/2026; excertos em `fontes-abertas.md` seçãoS9-03.
- **Status:** sustentação insuficiente (cobertura documental e teste de explicação concorrente).
- **Gravidade:** média.
- **Confiança:** alta na existência/conteúdo da reportagem e omissão no corpus; média nos percentuais sem relatório original/microdados e bases de subgrupo.
- **Impacto:** fortalece alinhamento e autonomia parcial dos cargos; não identifica direção de influência, persuasão ou transferência.
- **Correção:** obter original/matriz/base/ponderação da onda; incorporar intenção condicionada corretamente rotulada; manter necessidade de painel/voto realizado para outras perguntas. Não inverter condicionais nem extrapolar para urna.

### A9-03 — Caminho concreto de digitação por RDV não foi documentado
- **Agente:**9.
- **Arquivo/linhas:** `ANALISE-DETALHADA.md` l.102,112; `research/HIPOTESES.md` l.17.
- **Afirmação:** arquivo por seção não isola13; faltam RDV/BU apropriados e perícia.
- **Problema:** limitação do CSV é correta e RDV já é citado como necessidade. Contudo, notícia anterior à data de corte declara extração de RDVs, cobertura e números específicos, oferecendo pista testável. BU e RDV não são intercambiáveis: BU totaliza categorias, RDV pode preservar digitação, nenhum recupera intenção/pareamento individual. A lacuna é de seguimento documental, não erro de dizer que aquele CSV não permite isolar13.
- **Fonte/comando:** S9-02 (alegação204.309 e cobertura37.675seções); S9-05 (TSE “Votação segura”); S9-06 (tentativa da especificação oficial2026:curl403; não decodificada).
- **Status:** sustentação insuficiente; total204.309 permanece não verificável por este agente, **não certificado**.
- **Gravidade:** média.
- **Confiança:** alta na distinção entre agregado96 e digitação e no que a página oficial descreve; média na aplicabilidade técnica específica sem esquema2026; nenhuma inferência sobre motivo.
- **Impacto:** pode reduzir incerteza sobre quais números nulos foram confirmados, não sobre por quê ou quem pretendia votar emPaes. Não autoriza chamar esses nulos de votos desviados.
- **Correção:** adquirir especificação oficial2026 e RDVs com integridade, cobertura/cargo/turno, reconciliar a soma com675.292 nulos de urna do recorte; tratar204.309 como dado jornalístico atribuído até conferência. Não prometer reconstruir voto dividido a partir deRDV.

**Referência cruzada, sem novo ID:** P1-01 (alta, erro confirmado no uso/atribuição da medida final) deve corrigir os números67/44 de `ANALISE` l.63 e o confronto das pesquisas. Reconferência própria p.12 salva. O estudo pode ter usado “final auditado” como recorte de auditoria; não lhe atribuo a frase literal “não houve outra onda”. P1-02 atual é omissão/sustentação insuficiente, não erro sobre suposta exclusividade de séries.

## 7. Verificações bem-sucedidas e limites

| ID | Teste/evidência | Resultado e limite |
|---|---|---|
| V9-01 | Leitura `ANALISE`34,61,69,98,102,112,118,122–124,130 | Ressalvas corretas: sem painel, sem transferências individuais, sem anulação→Ruas ou nulos→Paes. Manter |
| V9-02 | `analyze.py`31–35 e inspeção CSV em `compatibilidade-cargos.json` | Comparação presidencial filtra turno1, mesmas183chaves,2026/RJ/trânsitoN; resultado não pareia eleitores |
| V9-03 | TRE proclamação l.7–8 + domínios dos recortes | Segundo turno presidencial existe nos dados; governador proclamado no1º. ZIP só1º não serve sozinho |
| V9-04 | PDF DF compartilhado p.12 visual e extração l.91–93,302–347 |75/52, bases e margens conferidos; lembrança/número pretendido não é voto registrado |
| V9-05 | S9-04 TSE | Ordem oficial e identificação visual do cargo documentadas; exposição/compreensão reais não medidas |
| V9-06 | S9-05 TSE | RDV não identifica eleitor nem associação dos votos por cargo; BU informa agregados |
| V9-07 | S9-01 e imagem local lida | Face publicada associa explicitamente Paes/governador22; não confundir com mera peça presidencial de outro ano; autenticidade física/autor não certificados |

**Acesso e erros:** buscas públicas restritas ao TRE não localizaram nota original/auto; índice incompleto não prova inexistência. A síntese automática de uma busca negou candidatura dePaes usando diplomação municipal2024; descartei-a por incompatibilidade temporal/cargo. Não a chamei de prova de fraude da fonte. WebFetch do pacote técnico devolveu binário ilegível; curl ao mesmoURL retornou403 e não houve extração. Sem contorno de autenticação ou insistência. Foto g1 baixada com sucesso; hashes em `manifesto-09.json` atestam preservação, não autenticidade. Inspeção CSV: primeira tentativa comSniffer falhou; leitura com delimitadorvírgula declarado funcionou. Nada disso executou reprodução do estudo.

**Não obtidos:** autos/perícia/inquérito/notaTRE original do santinho; autoria, verso, tiragem/distribuição; original/microdados do cruzamento presidencial; painel pré/pós ou estudo pós-eleitoral metodologicamente verificável; RDVs/BU2026 e especificação legível; detalhe de participação presidencial. O SHA da referência foi informado e a correspondência dos blobs foi verificada por02/06; não fiz nova autenticaçãoGit nem declarei verificação própria integral de65blobs. Nenhuma evidência posterior ao corte foi usada. Rodada encerrada aqui, com tarefas materiais delimitadas.

## 8. Pedidos concretos via coordenador (não enviados aos revisores)

- **Revisor4:** conferir comparação turno1/cargo1 versus3 nas183unidades com detalhe presidencial de aptos/comparecimento/válidos, habilitação e trânsito; explicitar denominadores próprios. Se validar dadoRDV, reconciliar cobertura/tipos/nulos13 e total96 sem inferir motivação nem pareamento entre cargos. Nenhum cenário como estimativa de desvio.
- **Revisor5:** obter representação/auto/notaTRE e exemplares dePaes–22/Paes–13; catalogar pessoa/autoria alegada e comprovada, data/local, distribuição, resposta dasduas campanhas. Separar peça22, peça13 e100mil alegados de “valores”. Verificar originais de propaganda conjunta e endossos presidenciais pré04/10; não duplicarA9-01 como outro caso.
- **Revisor7:** confrontar narrativa de alinhamento nacional com cruzamentoPaes–Flávio/Ruas–Lula, redes locais e assimetria de conhecimento; manter partido/líder/rejeição/mobilização/erro de conversão como mecanismos distintos. Incorporar atualizaçãoP1-01 e não usar exposição desconhecida ou204.309 nulos noticiados para declarar fator decisivo.
- **Coordenação/revisor3:** adquirir relatório completo da onda22–24/09 que fundamenta S9-03, bases de subgrupo e matriz; conciliar base ponderada1.788 do anexo com1.769 entrevistas da lâmina final sem chamar de erro antes da definição. Tratar fontes de06/10 como cronologia anterior à decisão, não realidade após15/10.

## 9. Entregáveis

- `/workspace/rj26/revisao/agentes/09-fatores-omitidos.md` — este parecer, achados, matriz e pedidos.
- `/workspace/rj26/revisao/agentes/09-fatores-omitidos/00-observacoes-iniciais.md` — registro anterior aos pareceres.
- `09-fatores-omitidos/fontes-abertas.md` — URLs, excertos e limitesS9-01–06.
- `09-fatores-omitidos/compatibilidade-cargos.json` — inspeção de chaves/domínios.
- `09-fatores-omitidos/g1-santinho-0410.jpg` — imagem publicada, sem perícia.
- `09-fatores-omitidos/datafolha-final-p12.png` — reconferência visual da fonte compartilhada.
- `09-fatores-omitidos/manifesto-09.json` — integridade dos artefatos próprios.

**Conclusão permitida:** há evidências adicionais de mensagem de número incorreto localizada e de alinhamento individual de intenções, e uma via concreta para auditar digitação de nulos. Não há identificação de votos perdidos por Paes, desviados para Ruas ou causalmente entregues pela presidencial; não há magnitude suficiente para declarar qualquer desses fatores decisivo. Corrigir a medida final Datafolha e aprofundar estas pistas é necessário sem rebaixar as ressalvas corretas do estudo.
