# Revisor 8 — RJ26 Aderência e clareza

## 1. Escopo, commit e diagnóstico delimitado

Referência: `RafaelPanisset/estudo-rj-2026`, commit **f7278de8335458be2f290c15b9a63a220954d639**, exportado em `/workspace/rj26/ref`. Data de corte: **7/11/2026**. Relatório encerrado em 2026-11-07 09:02:17 -03 (America/Sao_Paulo).

**Aderência parcial, não ausência de investigação:** dos dez requisitos, **2 atendidos (regiões e participação), 8 parciais, 0 não atendidos, 0 n.a.** O formato é **parcial**: seus quatro componentes existem, mas documentação da aquisição e clareza ainda precisam correção. Total dez+formato: **2/9/0/0**. Não se usa essa contagem como nota de qualidade ou probabilidade de verdade.

A entrega responde diretamente às três perguntas finais e sustenta a contabilidade; a resposta política é menos completa que a descrição. Faltam investigações documentais possíveis de campanha, redes e explicações concorrentes. Ausência de painel não justifica dispensá-las. Os maiores problemas de evidência são as pesquisas finais omitidas, de **P1-01/A3-01** e **P1-02/A3-02** (altos, sem novo ID aqui). **Nenhum crítico próprio**; os três achados próprios abaixo são dois médios e um baixo. Não apresento uma auditoria integral de fontes como se a tivesse executado.

## 2. Método, sequência e limites da leitura

- Li integralmente `/workspace/rj26/PROMPT-GROK.md`, briefing original e COMO-USAR; README, ANALISE-DETALHADA, AUDITORIA, REPRODUCAO; os três research/*.md; results/TABELAS e todos os seis results/*.json; docs/PLANO; source/download/snapshot manifests; secoes-download e clean-reproduction. Inspecionei todos os oito scripts e data/pesquisas.csv.
- Consultei raw/*.txt por busca temática e trechos (Datafolha110–170; Paraná1–79; Atlas235–293); não os li integralmente nem os confundi com conferência visual dos PDFs. Não executei/importei scripts do estudo, não descomprimi ZIP, não rodei reprodução, não reabri web ou autos. Essas verificações são atribuídas, quando utilizadas, aos revisores especializados.
- Gravei `01-primeiras-observacoes.md` às **08:57:03 America/Sao_Paulo**, antes de qualquer parecer alheio. Gravei matriz inicial às **08:57:24 America/Sao_Paulo**; versão preservada em `02-matriz-inicial.md`. Só depois li integralmente 01,02,03,04,05,06,09 e, quando chegou, **07-explicacoes.md**. Incluí também **01-procedencia/REPLICA-A3-13.md** e **05-redes/REPLICA-PECAS.md**. O aviso inicial do coordenador continha escopo/estado de disponibilidade, não números nem resultados técnicos; não alego independência estatística entre papéis.
- `git rev-parse HEAD` falhou porque a referência não tem `.git`; não aleguei certificação própria do SHA por esse comando. A correspondência65blobs é verificação atribuída a02/06 e reconfirmada por05/07, não número de agentes usado como prova. Identidade com canal emissor em07/11, integridade, reprodução e veracidade são camadas distintas (réplica01).
- Executei apenas script próprio leve `08-aderencia/verificar_aderencia.py`, sobre produtos existentes. Ambiente registrado: Python3.13.5, Linux; saída `03-verificacoes.json`. Ele compara oito candidatos e dez linhas regionais, presença de seis números em README/ANALISE e quatro identidades, e localiza jargão/expressões de completude. Não é recálculo eleitoral a partir das urnas.
- **Resultado do script:**28 testes,27 positivos e1 ausência textual:975.176 aparece no README, mas não literalmente na ANALISE. Não é divergência: ANALISE83 fornece493.204+481.972=975.176. Preservei a saída com o “false” de presença literal; não criei erro numérico artificial. Análise humana separa ausência de repetição e contradição.
- Escritas somente em `08-aderencia/` e neste parecer. Referência intacta; sem publicação, mensagem externa, commit, push, PR, integração ou execução pesada.

## 3. Briefing e matriz final

O briefing exige investigar, não só citar temas: linhas15–24 listam trajetória; crescimento de Ruas; desempenho de Paes; Garotinho; regiões; máquinas/redes; campanha; participação; história/presidência; rivais. As **dez citações literais e as quatro exigências de formato** estão preservadas em `01-primeiras-observacoes.md`, extraídas das linhas15–24 e32–35.

Duas exigências que norteiam a classificação: linha28, “Não quero apenas dezenas de correlações ou uma coleção de notícias”; linha37, “Se faltar evidência para identificar uma causa, diga exatamente o que falta e apresente a melhor conclusão possível com o material disponível”. Linha39 exige responder expectativa sobre Paes, construção de Ruas e papel de Garotinho. Não exigir causalidade perfeita, mas também não confundir prudência com investigação executada.

# Matriz final de aderência — dez requisitos + formato

Status de atendimento não é status de veracidade. “Parcial” preserva investigação realmente feita; não equivale a tema ignorado. Todos os localizadores simples apontam a `/workspace/rj26/ref/`; as referências P1/A2/A3/R4/A5/R6/R7/A9 apontam aos pareceres locais correspondentes, e não a novos achados desta revisão.

| Item | Requisito | Status | Evidência arquivo/seção/linha | Lacuna (tipo) | Inevitável ou trabalho adicional possível | Pareceres relacionados | Mudança |
|---|---|---|---|---|---|---|---|
| 1 | Trajetória da disputa | parcial | ANALISE 25–51; data/pesquisas.csv 2–12; README 17 | Fonte não recuperada e análise não executada: ondas finais/séries disponíveis ficaram fora; registros PesqEle sem conferência | Possível: incorporar Datafolha2–3/10, Paraná/Atlas finais e séries internas, separar métodos/cenários; originais restantes a buscar, não presumir inexistência | P1-01/A3-01; P1-02/A3-02; A3-04/05/11/14 | parcial → parcial; lacuna deixou de ser apenas indisponibilidade alegada: omissões supríveis confirmadas |
| 2 | Crescimento de Ruas | parcial | ANALISE 55–63; README 9,18; HIPOTESES 6–7 | Análise dos mecanismos parcial; menções e associação não separam reconhecimento, partido, líder, redes e rejeição; última medida de número incorreta como final | Possível: atualizar ondas, explorar imagem/conhecimento disponível, integrar redes e cruzamento individual atribuído; efeitos individuais separados não identificáveis desses agregados | A3-01/09/10; A5-02; A9-02; R7-01 | parcial mantido; evidência adicional aumenta o trabalho documental possível |
| 3 | Desempenho de Paes | parcial | ANALISE 67–73,108–114 | Tratamento superficial da campanha/propostas/obstáculos e alianças cruzadas; geografia/rejeição investigadas | Possível: programas/peças simétricos, agendas e apoios nominais com alvo por cargo; rejeição estável não exclui contribuição parcial | A5-02/03; R7-02 | parcial mantido; sem rebaixar a contabilidade correta |
| 4 | Papel de Garotinho | parcial | ANALISE 94–102; CRONOLOGIA 26–32; README 11 | Fonte não recuperada: acórdão; análise não executada suficiente de Rosinha/Clarissa; contexto jurídico incompleto | Possível: incluir atuação familiar já relatada, fundamentos TSE e autos; transferência individual não é inferível de anulação/endosso posterior | A2-01; A5-01; V2-04/05/10 | parcial mantido; lacuna familiar comprovadamente suprível por reportagem contemporânea |
| 5 | Regiões do estado | atendido | ANALISE 79–90; TABELAS 5–16; analyze.py 36–60; territory.py 4–5 | Cobertura substantiva presente; apresentação de abstenção na tabela requer correção, sem mudar cobertura ou margens | Possível ajuste AD-03 e cartográfico R4-04; Metropolitana sobreposta corretamente; não exigir mapa inexistente de seção | R4 verificações 10–19; AD-03 | atendido mantido; testes técnicos não revelaram falha substantiva regional |
| 6 | Máquinas e redes | parcial | CRONOLOGIA 9–14,37; ANALISE 57,73,106,110 | Tratamento seletivo/superficial e análise não executada: vereadores/deputados, endossos e datas completos dos atores prioritários | Possível: incorporar catálogo nominal, distinguir endosso/parentesco/presença/filiação, alianças cruzadas e mudanças; não exigir censo universal nem estimar entrega | A5-02; R7-02 | parcial mantido; fontes acessadas pelos revisores mostram margem real para completar |
| 7 | Temas da campanha | parcial | ANALISE 108–114; HIPOTESES 18; AUDITORIA 16 | Tratamento superficial e análise não executada: programas/debates/publicidade/redes/alcance; busca sem evidência não documentada sistematicamente | Possível: peças originais e programas, circulação datada, debate codificado, audiência disponível; pericia/autoria/exposição podem seguir não verificáveis. Não confundir nenhuma mensuração causal com nenhum documento | A5-03; A9-01/03; réplica05 RP-22A/B,RP-13,RP-100K | parcial mantido; foto contemporânea/inicial republicada e publicidade relatada reduzem a parcela atribuível a falta de documentação |
| 8 | Participação eleitoral | atendido | ANALISE 118–124; resumo.json 5–11,31–36,56–61 | Sem falta substantiva no recorte pedido: comparecimento/abstenção/brancos/nulos e limites explícitos; cláusula de segundo turno estadual n.a. | Preferências dos ausentes/entradas e saídas individuais não identificáveis nesses dados. Possível apenas corrigir legenda de denominador na tabela (AD-03) | V2-03/07; revisor06 T7; R4 verificações14–15 | atendido mantido após validação técnica; não inventar segundo turno nem impor painel como requisito para descrever taxas |
| 9 | História e voto presidencial | parcial | ANALISE 128–134,61; HIPOTESES 7; resumo.json 12–21 | Análise histórica restrita e compatibilidade de fronteiras não executada; interpretação presidencial sensível a denominador; cruzamento de intenção omitido | Possível: corrigir referência a turno2018, apresentar válidos por cargo, obter detalhe presidencial e originais do cruzamento, conferir história municipal. Não identificar voto dividido realizado com totais | R4-01/03/05; A9-02; A3-10; R6-11 | parcial mantido; sensibilidade altera a interpretação dos 89 municípios, sem alterar os absolutos |
| 10 | Explicações concorrentes | parcial | HIPOTESES 5–18; ANALISE 138–142; README 18–22 | Tratamento parcial: hipóteses fortes/exclusivas sem confronto simétrico de contribuições graduais; associação e contribuição eleitoral no mesmo rótulo | Possível: formular hipóteses aditivas e observações discriminantes, incorporar evidências já disponíveis; pesos causais podem continuar indeterminados | R7-01/02; A5-01–03; A9-01–03 | atendido → parcial após leitura de07: matriz existe, mas não conclui o confronto exigido pelo item10 |
| F | Formato solicitado | parcial | BRIEFING 32–35; README5–24; ANALISE; REPRODUCAO15–22; AUDITORIA15–25; manifestos | Quatro componentes presentes; metadados de fonte/data/hash incompletos e aquisição restrita; linguagem/tabela e qualificação da síntese requerem ajuste | Possível: completar manifestos e orientações, glossário/legendas e delimitação da síntese; reprodução central funciona, não declarar falha geral de execução | R6-02/05/06; P1-05; R7-01; AD-01/02/03 | atendido → parcial: não por inexistência de arquivos, mas por exigência documental/clareza não plenamente cumprida |

## Contagem
Dez itens: **2 atendidos / 8 parciais / 0 não atendidos / 0 não aplicáveis**. Formato: **parcial**. Total de onze linhas: **2 / 9 / 0 / 0**. A cláusula “se houve segundo turno” do item8 é n.a.; o item inteiro é atendido. Ausência de peso causal identificável não torna requisitos políticos n.a.

## Desdobramento do formato (não adicionar à contagem)
- README: conclusão simples e classes existem; qualificação da explicação e termos “final” precisam ajustes (R7-01; P1-01). Não é ausência de resposta.
- Análise detalhada: cronologia, tabelas, mapas, testes, fontes e hipóteses presentes; cobertura política/documental parcial nos itens indicados.
- Código/reprodução: execução central e produtos confirmados pelo revisor6, não executados por08; fontes/data/hashes incompletos em entradas presidenciais e aquisição (P1-05/R6-05). Pastas ausentes falham (R6-02), o que NÃO significa falha no clone entregue com pastas existentes.
- Limitações: próximas das afirmações em muitos pontos; falta distinguir sistematicamente ausência de fonte, busca frustrada e análise ainda não executada (AD-01); limites técnicos não substituem investigação documental.

## Distinção obrigatória das lacunas
1. **Busca documentada sem evidência:** deve informar questão/consulta/data/canal/resultado; uma nota “não obtido” é registro de ausência no corpus, não diário suficiente. O estudo não fornece trilha comparável para todos os documentos políticos faltantes.
2. **Fonte inacessível:** manifesto registra 403 nas duas páginas TRE; o próprio estudo diz que foram lidas por ferramenta web. Falha do download não implica indisponibilidade do conteúdo ou dos autos em geral.
3. **Análise não executada:** inventários/avaliação comparativa de programas, anúncios, debates; correspondências históricas; sensibilidade de denominadores; uso de séries e módulos já preservados. Trabalho possível, sujeito a conferir originais.
4. **Tratamento superficial:** algumas propostas, poucos apoios e matriz de hipóteses com exclusividade no lugar de confronto gradual; temas foram mencionados e parcialmente documentados, não ignorados por inteiro.

Não foi comprovado, para nenhum conjunto documental político inteiro, que sua ausência fosse inevitável em7/11/2026. Limites inerentes dos agregados (intenção, fluxos, persuasão) são inevitáveis **com esses insumos**, não prova de inexistência mundial de painel/estudo individual. A linha de trabalho possível não promete sucesso de novas aquisições.

## Histórico
A versão anterior aos pareceres está em `02-matriz-inicial.md`, copiada sem mudança antes desta atualização; o registro independente `01-primeiras-observacoes.md` permanece intacto. Inicial: dez itens3/7/0/0 + formato atendido. Final: item10 e formato rebaixados; demais status mantidos com motivos mais precisos. Parecer07 e réplicas01/05 incluídos.


## 4. Achados próprios — formato obrigatório

Estes são problemas de aderência/apresentação transversais ou localizados. As omissões técnicas e os problemas causais específicos permanecem nos IDs de01–07/09; não reapresento esses casos como novos achadosAD. As verificações positivas estão em seção separada porque os quatro status obrigatórios são status de problemas.

### AD-01

- **ID:** AD-01
- **agente:** 8 — Aderência e clareza
- **arquivo/seção/linha:** AUDITORIA.md 15–19,22,25; ANALISE-DETALHADA.md 32,47,96,114,140; research/HIPOTESES.md 8,18
- **afirmação examinada:** Limitações apresentam o que não foi obtido/documentado e o que faltaria para explicar mecanismos.
- **problema preciso:** Não há classificação sistemática nem trilha de busca que permita distinguir fonte procurada sem êxito, falha de acesso, investigação adiada e impossibilidade dos dados usados. Isso dificulta ao leitor decidir se a resposta parcial era inevitável ou se exige trabalho documental ainda possível. O estudo admite incompletude; não lhe atribuo declaração falsa de inexistência de documentos.
- **fonte/página ou comando/cálculo:** Confronto dessas linhas com BRIEFING-ORIGINAL.md 21,24,35,37 e download-manifest.json 63–74: há 403 específicos do TRE, mas não diário de busca equivalente para programas/endossos/fichas. Matriz02 distingue cada situação. A5/A9 documentam omissões próprias; não são novos casos AD.
- **status:** sustentação insuficiente
- **gravidade:** média
- **confiança justificada:** Alta sobre a ausência da distinção/trilha nos arquivos lidos; limitada sobre buscas efetivamente feitas fora do pacote. Não concluo que não foram feitas.
- **impacto na conclusão:** A resposta política permanece parcial sem plano claro do que é suprível; a limitação de identificação causal pode ser confundida com esgotamento da investigação documental. Não altera totais ou vencedor.
- **correção ou evidência necessária:** Acrescentar quadro questão/documento buscado/canal/data/tentativa/resultado/tipo de lacuna/próximo passo. Marcar explicitamente não investigado quando couber e inacessível apenas no alcance da tentativa; integrar IDs técnicos já existentes, sem duplicá-los.

### AD-02

- **ID:** AD-02
- **agente:** 8 — Aderência e clareza
- **arquivo/seção/linha:** ANALISE-DETALHADA.md 7,38–39; research/HIPOTESES.md 17
- **afirmação examinada:** ADPF 1362; PPT; RDR e pós-estratificação; RDV/BU.
- **problema preciso:** As siglas e termos metodológicos não são definidos em linguagem acessível na primeira ocorrência nem remetem a glossário. O README é mais acessível, mas a análise exigida como explicação verificável a um leigo requer interpretação de termos não explicados.
- **fonte/página ou comando/cálculo:** Leitura de ANALISE/HIPOTESES e busca temática própria em verificar_aderencia.py, localizadores em03-verificacoes.json. Paraná TXT55 explica PPT, porém essa expansão não é transportada à tabela da análise.
- **status:** erro confirmado
- **gravidade:** baixa
- **confiança justificada:** Alta: ausência textual verificável no conjunto editorial lido. Não é erro de método ou de significado das fontes.
- **impacto na conclusão:** Dificulta compreender limites jurídicos, diferenças de amostragem e o que dados de urna podem revelar. Sem efeito nos cálculos.
- **correção ou evidência necessária:** Definir ADPF como ação constitucional de controle; PPT como seleção proporcional ao tamanho; explicar RDR e pós-estratificação sem sugerir equivalência de métodos; expandir RDV/BU e distinguir digitação de totalização, conforme fonte técnica efetivamente conferida. Usar glossário curto com links.

### AD-03

- **ID:** AD-03
- **agente:** 8 — Aderência e clareza
- **arquivo/seção/linha:** results/TABELAS.md 3,5–16; scripts/territory.py 8–9; scripts/analyze.py 51
- **afirmação examinada:** “Percentuais entre válidos após retotalização”, acima de tabela que inclui coluna Abstenção.
- **problema preciso:** A nota global atribui aos percentuais a base votos válidos, mas Abstenção é calculada sobre aptos. A coluna não explicita essa exceção. Os números estão corretos; o denominador da apresentação é impreciso. Pontos decimais/vírgulas de milhar também divergem do padrão brasileiro do texto, questão secundária de legibilidade.
- **fonte/página ou comando/cálculo:** analyze.py51 calcula 100*abstencao/aptos; resumo.json31–33: 1.292.986/4.942.710*100=26,159455%, arredondado26.16% na Capital; por válidos seria39,9665%, não26.16%. ANALISE118/122 define base corretamente. verificar_aderencia.py confirma linhas contra CSV regional.
- **status:** erro confirmado
- **gravidade:** média
- **confiança justificada:** Alta: nota literal, fórmula inspecionada e conta aritmética própria; sem executar código do estudo.
- **impacto na conclusão:** Pode fazer o leitor interpretar taxas de participação com base errada ao ler só a tabela. Não altera taxas efetivamente calculadas nem a aderência substantiva dos itens5/8.
- **correção ou evidência necessária:** Trocar nota por “Ruas/Paes: % dos válidos após retotalização; abstenção: % dos aptos; margem: Ruas−Paes em votos”; nomear coluna “Abstenção (% dos aptos)”; padronizar separadores em português.

## 5. Clareza para leigo, respostas diretas e coerência

### Resposta direta não equivale a explicação causal encerrada

| Pergunta do briefing | Resposta que a entrega efetivamente dá | Avaliação delimitada |
|---|---|---|
| Por que expectativa sobre Paes falhou? | README5–7/24 e ANALISE49–51/142: liderança medida tinha respaldo, mas não era certeza; margem fora da capital superou a capital; desencontro com pesquisas não identificado | Resposta direta presente. A frase “perdeu ... porque” deve ser lida como conta/onde, não mecanismo político. ANALISE19 distingue isso explicitamente, e142 reconhece lacuna; trazer a distinção para a abertura, conforme R7-01. Atualizar ondas altera magnitudes, não transforma liderança anterior em fictícia |
| Como Ruas construiu votação? | README9 e ANALISE55–63: base2022 e rede familiar, apoios prévios, crescimento e expansão | Há investigação substantiva da inserção prévia. “Ajudaram”/“melhor explicação” agrega associação e efeito; adotar desagregação R7-01 e preencher mecanismos documentáveis A5/A9. Não substituir por “nada pode ser sabido” |
| Qual Garotinho e papel? | README11 e ANALISE94–102/142: Anthony candidato10, Wladimir endosso posterior, anulação muda denominador; família não uniforme | Distinção pessoal/jurídica/temporal clara. A resposta organizativa de Rosinha/Clarissa está incompleta, suprível por A5-01; fundamento jurídico por A2-01. Não inferir transferência nem ausência de influência |

### Limitações próximas das afirmações

Verificações concretas: ANALISE32 preserva campo contraditório e fichas faltantes;34 rejeita fluxo Paes→Ruas;45 restringe margens de subgrupos;59 qualifica a subtração de São Gonçalo;61 diferencia votos entre cargos;69 rejeita “desertores”;73 rejeita contrafactual sem apoio;94 limita fontes jurídicas;98 qualifica segundo turno hipotético;102 limita código96;110 distingue entrevista religiosa e obediência;112 distingue acusação;114 mensagem/recepção;122 preferência de ausentes;134 limites históricos. Não procede acusar o estudo de ausência geral de ressalvas.

Contudo, as notas locais não dizem sistematicamente o que foi procurado versus adiado (AD-01). A síntese README18/24 precisa delimitação causal R7-01. “Sem experimento/painel” na matriz não encerra o item7 nem o teste de rivais graduais R7-02.

### Jargão e apresentação

O README usa formulação mais simples que a análise. Nesta, ADPF, PPT, RDR/pós-estratificação e RDV/BU precisam primeira definição/glossário (AD-02). “Denominador” está tornado concreto na tabela antes/depois, o que é verificável; “nulos técnicos” deve manter explicação e distinção de nulo digitado. Formatação numérica deTABELAS diverge do padrão do texto; mais importante, a nota de percentual não ressalva os aptos da abstenção (AD-03).

### Promessas de completude e auditoria

Busca editorial não encontrou promessa geral “definitivo” ou “todas as causas”. AUDITORIA25 declara “síntese descritiva auditável ... não uma determinação causal exaustiva”; isso é delimitação real. “Tabelas completas” (ANALISE3), “matriz completa” (140) e “prompt completo” (README35) referem-se a artefatos, não afirmação de exaustividade política. “Auditado” em campo Datafolha e “correspondência ... auditada” não certificam automaticamente toda a investigação. O problema concreto com “Datafolha final” já está em P1-01/A3-01; não invento novo defeito para cada uso de palavra.

### Coerência entre arquivos

- Oito candidatos deTABELAS22–29 correspondem aresumo.json, inclusive votos/partido/número; dez linhas regionais coincidem comregioes.csv: **18 comparações positivas** pelo script próprio.
- Totais4271199/3706984, margem564215, capital410961 e Anthony274411 aparecem em README eANALISE;975176 do README é coerente com decomposição daANALISE83 e JSON, embora não seja repetido literalmente.
- Regiões somam margem estadual; capital+restante também; válidos+brancos+nulos=comparecimento; oito candidatos=total válido. Isso comprova **coerência interna dos produtos**, não veracidade de fonte.
- AUDITORIA7–10 enumera cobertura e reconciliação; não contradiz esses totais. Reprodução byte-idêntica e recálculos efetivos são atribuídos a06; autenticidade operacional delimitada a01. Não há defasagem numérica atual do texto nos números testados; há **omissão de evidências posteriores às ondas usadas, mas anteriores ao corte**, e problemas de interpretação de cenário/denominador já identificados por03/04.

## 6. Verificações bem-sucedidas — evidência e alcance

| ID de verificação | Teste/evidência | Resultado permitido |
|---|---|---|
| VA-01 | Leitura literal briefing15–24/32–35 versus arquivos; dez transcrições e matriz salva antes dos pares | Nenhum requisito foi omitido desta revisão; todos receberam status com evidência; cláusula de segundo turno n.a. corretamente separada |
| VA-02 | Script próprio: oito candidatosTABELAS versusresumo.json; dez regiões versusCSV |18/18 linhas conferem; não é conferência de microdados |
| VA-03 | Script próprio: quatro identidades entre produtos, números compartilhados e leitura daANALISE83 | Conta publicada coerente; uma ausência literal não foi convertida em divergência |
| VA-04 | Leitura README13–24, ANALISE19/94–124 eAUDITORIA25 | Classes e limites locais existem; anulação não é transferência; descrição não autoriza fluxo; não há promessa geral de determinação causal exaustiva |
| VA-05 | R4 verificações16–17; V2-03/07; R6 T2/T3/T7 (atribuídos, não executados por08) | Suportam manter atendimento dos itens5/8 e não declarar fracasso geral da reprodução; falhas documentais não mudam automaticamente esses status |

## 7. Lacunas inevitáveis com estes dados e trabalho possível — prioridade por impacto

### Limites dos insumos, não licença para desistir

1. Totais territoriais não identificam quem mudou, dividiu voto, pretendiaPaes ou recebeu influência. Diferenças de votos entre cargos e anos não são trajetórias. Esse limite é inevitável **nesses agregados**.
2. Código96 não informa número nulo digitado, motivo ou intenção. RDV validado pode avançar na digitação, nunca parear eleitor/cargos ou reconstruir preferência anterior.204.309 é alegação jornalística não certificada pelos revisores, não resultado desta auditoria.
3. Sem segundo turno estadual realizado, não há transições observadas entre turnos desse cargo. Não substituir pelo presidencial nem aplicar43/41 de intenção hipotética a274.411 votos reais.
4. Sem painel/ponderações/exposição/comparecimento validado, o material não separa completamente mudança tardia, seleção, não resposta, ponderação e mobilização. Não afirme que tais dados inexistem em todo lugar em7/11: isso não foi demonstrado.
5. Certidão de trânsito ou acórdão ausente no corpus não autoriza conclusão judicial definitiva. Indisponibilidade integral não foi comprovada; há notícias/decisão interlocutória e réplicas que avançam parcialmente.

### Trabalho adicional possível

| Prioridade | Trabalho | Por que pode mudar diagnóstico | Estado/exata evidência necessária |
|---|---|---|---|
|1 alta| Atualizar ondas/séries, rótulo final, confronto correto de cenários e modeloQuaest | Muda magnitude do desencontro e trajetória/número; não muda sinal do crescimento | P1-01/A3-01 eP1-02/A3-02 já documentam originais/republicações; usarRJ-08712 paraRTBD, nãoBR-05193. Fichas/PesqEle/microdados seguem pendentes |
|2 média| Desagregar síntese e rivais graduais; integrar denominadores presidenciais e intenção cruzada | Muda alcance da explicação, evita usar geografia como causa e versões extremas como único teste | R7-01/02; R4-01; A9-02/A3-10. Cruzamento tem cenário/base divergentes sem original: uso qualitativo atribuído, não nova matriz conjunta |
|3 média| Completar atores/datas/territórios/apoios por cargo e atuação familiar | Esclarece construção de coalizão, obstáculos dePaes e papel de cadaGarotinho | A5-01/02 já mostram informação acessível; faltam documentos/eventos originais e cobertura justificada. Não requer prova experimental para documentar atuação |
|4 média| Investigar programas, publicidade, redes, debates e peças de número com cadeia explícita | Troca menção genérica por mecanismo/documento datado e permite avaliar alcance possível | A5-03/A9-01/03 e réplica05: fotoPaes22 localizada, colinha, “Lula é13” e folheto religioso distintos; inicial republicada não autenticada noPJe. Não juntar tiragens alegadas nem chamar tudo de “Paes governador13” |
|5 média| Seguir pistas oficiais de autos, nota/auto de apreensão, fiscais, RDV/esquema2026 e participação presidencial | Reduz incerteza jurídica/técnica/localizada, não identifica motivo individual | Validar documentos originais, cobertura/integridade; reconciliarRDV com675.292 nulos digitados se adquirido; participação exige detalhe próprio |
|6 média/baixa| Completar fontes/datas/hashes e distinção de buscas, glossário e notas de tabela | Torna entrega auditável e inteligível sem confundir acessibilidade e causalidade | AD-01/02/03; P1-05/R6-05/06; registrar pastas necessárias R6-02. Nenhum ajuste aplicado à referência |
|7 localizada| História2018/2024 e fronteiras | Corrige referência a turno e aumenta comparabilidade | R4-03/05 eR6-11; códigos iguais não provam geometrias iguais; totais2024 foram confirmados documentalmente por01/02/04, não por execução offline06 |

## 8. Mudanças após pareceres e réplicas — sem duplicatas

- **Item10: atendido→parcial** após R7-01/02. Antes havia sido reconhecida matriz substantiva com ressalva sobre exclusividades; depois ficou explicitado que não há teste simétrico de contribuições parciais nem previsões discriminantes suficientes. Não reclassifico toda evidência observacional como conjectura.
- **Formato: atendido→parcial** após P1-05/R6-05/06 e revisão de clareza. Arquivos presentes não suprem metadados faltantes de aquisição; execução central funciona. R6-02 é condição específica de pastas ausentes, não falha total de clone ou prova de números incorretos.
- **Itens1–4/6–7/9 mantidos parciais**, agora com lacunas mais precisas. Omissões de ondasP1/A3, atuaçãoA5, peçasA9 e sensibilidadeR4 mostram trabalho possível em vez de inevitabilidade geral. Problemas técnicos permanecem nos seus IDs originais.
- **Itens5/8 mantidos atendidos**, com base nos testes efetivos de02/04/06 e nossa cobertura editorial. AD-03 é legenda localizada, não falha de contabilidade. Não rebaixar por contagem de revisores ou por defeito sem impacto no requisito.
- **Réplica01/A3-13:** divergência do registroRTBD foi resolvida pelo próprio revisor01:BR-05193 é presidencial; governadorRJ-08712.03 ainda a listava como não resolvida em sua versão; nesta matriz é **resolvida documentalmente**, não por consenso. “Snapshot não autenticado” de03 e “autenticação operacional” de01 têm escopos distintos, não conflito de números; não declaro veracidade independente das urnas.
- **Réplica05:** “inicial não obtida” foi parcialmente superado: cópia públicaConJur de91p lida por05, sem autenticaçãoPJe. A peçaRP-13 diz “Lula é13”, não literalmente “Paes governador13”;100mil religioso,100mil inicial/1,1milhão alegadoRIOESCOLHE e multa não se confundem. Todas essas são informações atribuídas à réplica, não perícia própria nem prova de distribuição/efeito.
- **Parecer07 incluído integralmente**, lido depois dos registros independentes. Não permanece pendência de ausência do revisor7. Não dupliquei R7-01/02 como achadosAD; sua avaliação estrutura a clareza e o rebaixamento do item10.

## 9. Limitações desta revisão e entrega

Revisão de aderência/clareza, não nova autenticação eleitoral ou execução do projeto. Não li integralmente todos os CSVs, PDFs, HTMLs ouTXT; usei produtos/scripts para cobertura e trechos necessários. Não acessei docs externos, PesqEle, autos, microdados/pesos, bibliotecas de anúncios ouRDV. A acessibilidade de cada fonte nova é evidência atribuída aos revisores que a abriram, com os limites deles. Não tratei número de pareceres concordantes como probabilidade.

A revisão é sobre um corte fixo; novas versões de pareceres depois deste encerramento podem exigir consolidação pelo coordenador. Não alterei estudo nem apliquei correções. Não há avaliação quantitativa da probabilidade de vitória, efeito eleitoral de igrejas/santinhos/partido ou fraude.

Arquivos: relatório `revisao/agentes/08-aderencia.md`; pasta `08-aderencia/` com registro inicial imutável, matriz inicial/final eCSV, `achados.csv` (11 colunas,3 problemas próprios), `achados.json`, script próprio e saídajson. As verificações positivas não entram noCSV de problemas para preservar os quatro status obrigatórios sem fingir que sucesso é erro.
