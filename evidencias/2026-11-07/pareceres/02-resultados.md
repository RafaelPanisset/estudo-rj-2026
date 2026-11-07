# Agente 2 — Resultados e contexto jurídico

## Escopo e veredito delimitado

Commit auditado: `f7278de8335458be2f290c15b9a63a220954d639`, `RafaelPanisset/estudo-rj-2026`. Corte: **07/11/2026**, horário America/Sao_Paulo (UTC−3). Papel executado como braço do revisor, não como novo bot independente.

**A contabilidade central e o resultado proclamado estão sustentados. Não encontrei erro crítico ou alto nesta especialidade.** Ruas venceu no resultado proclamado no primeiro turno; sua vantagem nominal sobre Paes não foi criada pela decisão sobre Anthony. A redução do denominador foi suficiente para dispensar o segundo turno. Não há demonstração de transferência dos votos anulados, nem de trânsito em julgado do contencioso eleitoral. O contexto jurídico merece complementação pontual, sem inverter a conclusão numérica.

Primeiras observações foram salvas em `02-resultados/PRIMEIRAS-OBSERVACOES.md` antes de qualquer parecer alheio; nenhum parecer alheio foi lido. Instruções integrais, briefing e COMO-USAR lidos. Inicialmente `/ref` estava vazio e `INVENTARIO.md` não existia; comecei pelo GitHub oficial no SHA fixo. Após aviso do coordenador, **verifiquei pessoalmente 65 blobs Git contra a árvore obtida pela API: zero divergências** (`checagem-ref.json`), além do hash do ZIP de seções. `INVENTARIO.md` continuou ausente na reconferência; usei `/workspace/rj26/ref.MANIFEST.txt` e conferência própria.

Não executei scripts do projeto, não clonei nem alterei a referência. Os cálculos abaixo são implementação própria. Python 3.13.5; biblioteca padrão, curl e pdftotext. Escrita apenas na pasta autorizada, relatório e catálogo compartilhado, este com `flock` exclusivo e deduplicação por URL.

## 1. Reconstrução dos candidatos e chapas

Fontes distintas: recorte nominal do **commit**, dados atuais oficiais de candidaturas do TSE baixados nesta revisão e notícias institucionais do resultado. O ZIP oficial `consulta_cand_2026.zip` tem SHA-256 `e35ef1a742564081f6d443c823f3238a1b8597eeb2a5021a14ccce6157ff8984`; membro RJ gerado em 07/11/2026 às 05:30:36 (America/Sao_Paulo). Extração limitada aos campos pertinentes em `fontes/candidaturas-rj-filtradas.json`. Não confundir a situação da totalização com o deferimento do registro.

| Número | Governador: nome de urna (partido) | Vice: nome de urna (partido) | Votos nominais apurados | Destinação no recorte pós-retotalização |
|---|---|---|---:|---|
| 22 | Douglas Ruas (PL) | Fernanda Louback (PL) | 4.271.199 | Válidos; eleito |
| 55 | Eduardo Paes (PSD) | Jane Reis (MDB) | 3.706.984 | Válidos; não eleito |
| 10 | Garotinho / Anthony (Republicanos) | André Monteiro (Democrata); registro anterior de Major Elaine | 274.411 | Nulos técnicos no detalhe; número 10 preservado no recorte por seção |
| 50 | William Siri (PSOL) | Juliana Carvalho (PSOL) | 235.347 | Válidos |
| 14 | Coronel Busnello (Missão) | Rafa Luz (Missão) | 84.889 | Válidos |
| 30 | André Marinho (Novo) | Tenente Coronel Erigreyce (Novo) | 45.359 | Válidos |
| 80 | Juliete (UP) | Bia Martins (UP) | 33.430 | Válidos |
| 16 | Cyro Garcia (PSTU) | Perciliana (PSTU) | 14.642 | Válidos |
| 29 | Luan Monteiro (PCO) | Caetano Albuquerque (PCO) | 2.777 | Válidos |

Oito candidaturas válidas somam **8.394.627**. Anthony é a nona candidatura, não desaparecimento de votos das urnas. Os oito totais foram recalculados dos recortes nominal e por seção do commit, sem usar `results/resumo.json` como entrada. Para Ruas, Paes e Anthony também há confirmação textual em TRE-RJ/Senado; não baixei novamente o ZIP nacional nominal de 466.449.807 bytes, cujo tamanho foi consultado por HEAD. A reconciliação externa atual de todas as categorias foi feita com o ZIP de detalhe, abaixo.

Identidades civis dos titulares: Douglas Ruas dos Santos; Eduardo da Costa Paes; Anthony William Garotinho Matheus de Oliveira; William Carlos Brum Bispo; João Jacques Soares Busnello; André Bourguignon Marinho; Juliete Pantoja Alves; Cyro Garcia; Luan Monteiro Paschoal Pires. A chapa proclamada é **Douglas Ruas dos Santos / Fernanda Anchieta Louback**; Jane Reis é **Jeannie Mayr Reis de Oliveira**. A composição oficial atual é Rio Real (PL/Mobiliza/Agir/Avante) e, para Paes, Juntos para Mudar Coragem para Reconstruir (composição integral preservada no JSON). O registro de Paes aparece como **DEFERIDO COM RECURSO** no recorte nominal, distinto de “NÃO ELEITO”.

O arquivo atual de candidaturas traz `DS_SITUACAO_CANDIDATURA=#NE` e não tem os campos de julgamento usados no recorte nominal. Portanto, não usei esse campo vazio para declarar registros deferidos ou processos encerrados. O ZIP registra **os dois vices de Anthony**, não prova sozinho a sequência processual de substituição. A notícia do Valor de 03/10 lista André Monteiro; a reportagem da CNN anterior ainda mencionava Major Elaine e desistência. Sem autos dos vices, essa sequência não é certificada aqui.

## 2. Contas antes/depois e categorias

Comando reexecutável: `python3 /workspace/rj26/revisao/agentes/02-resultados/recalcular_independente.py`. Entradas preservadas `votacao-commit.csv` e `detalhe-commit.csv`, obtidas pelo GitHub oficial; ambas têm bytes iguais aos arquivos locais fixos. Saída: `recalculo.json`. Todos os registros passaram pelos filtros 2026/RJ/cargo 3/turno 1. São 1.464 linhas nominais e 183 unidades município-zona no detalhe; chaves do detalhe únicas.

| Categoria no detalhe pós-retotalização | Total |
|---|---:|
| Aptos para o recorte/cargo | 12.842.517 |
| Comparecimento | 9.845.867 |
| Abstenções | 2.996.650 |
| Válidos = nominais válidos | 8.394.627 |
| Brancos | 501.537 |
| Nulos digitados (`QT_VOTOS_NULOS`, seção 96) | 675.292 |
| Nulos técnicos | 274.411 |
| Nulos totais (digitados + técnicos) | 949.703 |
| Campos próprios de anulados e anulados sub judice | 0 |

Identidades testadas **em cada uma das 183 linhas**, não apenas no agregado:

- `aptos = comparecimento + abstenções`;
- `comparecimento = válidos + brancos + nulos totais`;
- `nulos totais = nulos digitados + nulos técnicos`.

A anulação jurídica de Anthony é registrada neste snapshot na categoria **nulos técnicos**, embora os campos denominados “anulados” estejam zerados. Não se pode somar novamente os 274.411 aos 949.703. O recorte por seção distingue 10/95/96; não revela qual número inválido foi digitado por eleitor nem intenção anterior.

**Reconferência externa:** baixei `https://cdn.tse.jus.br/estatistica/sead/odsele/detalhe_votacao_munzona/detalhe_votacao_munzona_2026.zip`, 4.182.055 bytes, SHA-256 `ee996c10f652f3d90205f6c0b7b794ae0f0520f4db717739fc5bcd3ef20a7b7e`. Membro RJ gerado em 06/11/2026 às 19:32:07 (America/Sao_Paulo). Os **27 totais quantitativos** filtrados por cargo 3/turno 1 são idênticos aos do recorte fixo: `fontes/detalhe-oficial-totais.json` e `reconferencia.json`. O hash do arquivo nacional difere do manifesto antigo, algo esperado numa nova geração; preservei ambos e não substituí insumo do estudo. Igualdade dos totais não implica igualdade de todos os bytes/linhas.

| Conta | Antes da exclusão | Depois |
|---|---:|---:|
| Votos de Ruas | 4.271.199 | 4.271.199 |
| Votos de Paes | 3.706.984 | 3.706.984 |
| Denominador juridicamente computado | 8.669.038 | 8.394.627 |
| Ruas | 49,269584% | 50,880152% |
| Paes | 42,761192% | 44,159008% |
| Maioria absoluta mínima, inteira | 4.334.520 | 4.197.314 |
| Margem nominal Ruas − Paes | 564.215 | 564.215 |

O denominador anterior foi **reconstruído**, não extraído de um segundo snapshot pré-decisão: `8.394.627 + 274.411 = 8.669.038`, em concordância com percentuais das notícias institucionais. Ruas ficava 63.321 votos abaixo do mínimo anterior e 73.885 acima do mínimo posterior. A análise fala em **73.885,5 acima da metade**, o que também está correto; não é a mesma definição que excesso sobre a maioria mínima inteira. Não registrei falso erro de “meio voto”.

Reconferi o recorte por seção: votos 10 = **274.411**, nome **Anthony William Garotinho Matheus de Oliveira**; igualdade com nulos técnicos nas **183 unidades município-zona, zero divergências**. Todas as opções de seção somam 9.845.867. Saída `recalculo-secoes.json`. Verifiquei SHA do ZIP de seções `ec93c020ae1f0088216de92e5acc5d3211aefaf1fa589b961132bbf471ee3cf5` e seus 296.106.129 bytes; **não repeti sua descompressão integral e a extração do recorte**.

Decomposição nominal reconstituída: capital Ruas 1.319.722, Paes 1.730.683, margem Paes 410.961; fora Ruas 2.951.477, Paes 1.976.301, margem Ruas 975.176. `975.176 − 410.961 = 564.215`. Não identifica fluxos individuais nem causa da escolha.

## 3. Cronologia jurídica: o que cada fonte prova

| Data (America/Sao_Paulo) | Fato e nível documental |
|---|---|
| 28/08/2026 | Liminar de Floriano sustando restrições de campanha é descrita na própria decisão posterior de 02/10, Rcl 0601745-49.2026.6.00.0000. Não era registro definitivamente deferido. |
| 11/09/2026 | Indeferimento regional relatado em fontes institucionais e petição. A decisão de 02/10 contém “11.9.2025”, aparente erro material da fonte; não o propaguei como data real da eleição de 2026. |
| 02/10/2026 | **Decisão judicial diretamente aberta no PJe**: revoga liminar e determina votos como anulados sub judice; menciona direitos políticos, filiação e inelegibilidade; pendência documental havia sido saneada nos embargos. É interlocutória da reclamação, não acórdão de mérito de 08/10. |
| 04/10/2026 | Votação. Inclusão provisória dos votos no denominador por decisão de Nunes Marques é narrada pelo Senado, não conferida aqui no inteiro teor dessa decisão. |
| 05/10/2026 | Pedido de desistência do recurso (notícia MPF); ato posterior ao pleito, não desistência homologada. |
| 08/10/2026 | Notícia **do próprio TSE**: desistência não homologada; parcial provimento para afastar inelegibilidade da alínea l por LC 219/2025, mas manutenção do indeferimento por ausência de condições de elegibilidade — direitos políticos e filiação. Anulação/retotalização por 5–2. Não confundir unanimidade da rejeição da desistência com placar da anulação. RO-EI 0602359-26.2026.6.19.0000. |
| 10/10/2026 | Retotalização: TRE-RJ informa votos e 50,88%; notícia ainda previa posterior apreciação/proclamação. Não era por si só certidão de trânsito. |
| 14/10/2026 | STF noticia ADPF 1362, ajuizada pelo **PSD**, pedindo segundo turno. Argumentos da parte não são conclusões do Tribunal. |
| 15/10/2026 | TRE-RJ noticia homologação unânime e proclamação da chapa Ruas/Louback. Diz que não houve reclamação à Comissão Apuradora durante a disponibilização do relatório. Isso não contradiz ADPF em outra instância. Processo mencionado: 0604643-07.2026.6.19.0000 (normalização do número impresso na notícia). |
| 25/10/2026 | Calendário nacional previa eventual segundo turno; **não ocorreu segundo turno fluminense para governador segundo o resultado proclamado e as bases examinadas**. Não confundir com a eleição presidencial. |
| 27/10/2026 | Estudo afirma prestação de informações do TSE na ADPF. A extração atual da página pública do STF mostrou cabeçalho/abas, não este andamento. Não reconfirmado independentemente. |
| 04/11/2026 | CNN relata ação de Paes e coligação contra Ruas/Louback. Alegações de abuso, panfletos e compra de votos, não fatos judicialmente reconhecidos. Inicial integral, provas e número desta ação não foram recuperados aqui. |

A página pública do STF confirmou **ADPF 1362 / 0187813-76.2026.1.00.0000 / relator Cristiano Zanin**, mas não mostrou decisões nem andamentos na extração. Não declarei procedência, improcedência, suspensão ou trânsito em julgado. A notícia do TRE-RJ sobre diplomação em dezembro também não comprova diplomação já realizada no corte.

Documentos acessados não equivalentes: notícia TSE/TRE = comunicação institucional do julgamento; PJe 02/10 = decisão diretamente disponibilizada; PDF do ConJur encontrado na pesquisa = **petição da coligação de Paes em 06/10**, não acórdão. PDF mantido e identificado, sem promover suas alegações a fatos. O inteiro teor do acórdão de 08/10 e dos autos de proclamação não foi obtido.

## 4. Quem é cada Garotinho

- **Anthony William Garotinho Matheus de Oliveira**: ex-governador, candidato ao governo em 2026 pelo Republicanos, **10**. É ele quem recebeu 274.411 votos anulados. Não é Wladimir.
- **Wladimir Barros Assed Matheus de Oliveira**: filho de Anthony e Rosinha; ex-prefeito de Campos, candidato a deputado federal pelo **PL, 2258**, situação oficial atual **ELEITO POR QP**. A notícia NF de 05/10 atribui o discurso à comemoração após a votação de 04/10: “Eu honrei o meu pai ... apertei 10 ... Mas, agora é 22”. Isso documenta declaração posterior e a afirmação do próprio ator de apoio anterior ao pai, não leitura de sua escolha secreta nem de todos os seus eleitores. A notícia diz 81.797 votos; não fiz nova totalização federal para certificar esse total.
- **Rosinha Matheus / Rosinha Garotinho (Rosângela Barros Assed Matheus de Oliveira)**: ex-governadora e ex-prefeita de Campos, esposa de Anthony, mãe de Wladimir/Clarissa. Não é a candidatura de governador 10 em 2026. A notícia histórica do TSE identifica Rosinha e Anthony separadamente; o Senado situa a condenação mencionada no período do governo de Rosinha. Isso não prova condenação eleitoral nova de Rosinha em 2026. CBN de 19/08 relata “Rosinha pelo interior”, reuniões e coordenação regional da campanha do marido; é pista contemporânea concreta, não prova de votos entregues.
- **Clarissa Garotinho**: nome civil na Câmara **Clarissa Barros Assed Matheus de Oliveira**, filha de Anthony e Rosinha, irmã de Wladimir; ex-deputada federal, mandatos 2015–2019 e 2019–2023. A biografia legislativa antiga não certifica sua filiação atual; a CBN de 19/08/2026 descreve atuação privada e articulação nos bastidores. Não aparece como candidata na extração de 2026 pelo nome civil correspondente; a ausência de candidatura não prova ausência de influência ou endosso. Não atribuí a ela voto, cargo ou adesão específica sem documento.

A alegação genérica de “Garotinho apoiou Ruas” precisa nomear pessoa e data. Para **Wladimir**, existe a declaração posterior; para **Anthony**, ela não é demonstrada por essa fonte. A existência de influência familiar anterior não é refutada pela inexistência de transferência individual mensurável. O estudo toma corretamente esse cuidado.

## 5. Achados no formato obrigatório

### A2-01 — Contexto do mérito jurídico incompleto

- **Agente:** 2 — Resultados e contexto jurídico.
- **Arquivo/seção/linha:** `ANALISE-DETALHADA.md`, §6, linhas 92–96; `research/CRONOLOGIA.md`, linha 29; `research/FONTES.md`, F3. Linhas conferidas nos arquivos do commit e nas cópias locais `commit-*`.
- **Afirmação examinada:** resumo do indeferimento por suspensão de direitos políticos e manutenção do indeferimento/anulação em 08/10, apoiado principalmente em notícia do Senado.
- **Problema preciso:** o resumo é correto sobre resultado e desistência, porém não reconstrói **o parcial provimento para afastar a causa de inelegibilidade da alínea l** nem o fundamento autônomo de **filiação partidária inválida** que permanece com a falta de plenitude de direitos políticos. Sem isso, o leitor não distingue inelegibilidade afastada de ausência de condições de elegibilidade mantida. Não afirmo que o estudo tenha expressamente dito o contrário.
- **Fonte/página ou comando/cálculo:** notícia oficial TSE de 08/10, seção “O resultado do julgamento”, URL `https://www.tse.jus.br/comunicacao/noticias/2026/Outubro/tse-decide-pela-retotalizacao-dos-votos-para-governador-no-rio-de-janeiro`; excerto literal preservado em `fontes/tse-julgamento-webfetch-excertos.md`. Decisão PJe de 02/10 em `fontes/pje-2out.html` mostra a pluralidade dos fundamentos anteriores; MPF confirma a questão da filiação.
- **Status:** sustentação insuficiente (completude da reconstrução jurídica, não erro confirmado do resultado).
- **Gravidade:** média.
- **Confiança justificada:** alta quanto à omissão textual e ao conteúdo expresso da notícia do próprio TSE; limitada quanto ao inteiro teor, não recuperado.
- **Impacto na conclusão:** localizado. Não muda votos, denominador, proclamação nem ausência de segundo turno; melhora a explicação de por que o registro continuou indeferido.
- **Correção/evidência necessária:** acrescentar a distinção entre art. 14, §3º, II/V da CF e inelegibilidade da LC 64/1990; citar notícia original TSE e, preferencialmente, juntar acórdão/certidão de 08/10. Não trocar “indeferimento” por “desistência homologada”.

Não classifiquei falta de autos acessíveis como falsidade; não criei achado alto para uma limitação já admitida pelo estudo. **Não há achados críticos/altos nem erro factual central confirmado a comunicar em prioridade.** A declaração sobre andamento de 27/10 permanece não verificável nesta revisão, sem presunção de falsidade.

## 6. Verificações bem-sucedidas e rastreabilidade

| ID | Verificação | Evidência exata / teste |
|---|---|---|
| V2-01 | Integridade da referência fixa | `checagem-ref.json`: 65 blobs calculados por `sha1(b"blob "+len+NUL+bytes)` contra SHA da árvore GitHub no commit; 0 divergências. ZIP SHA-256 igual a `data/secoes-download.json`/COMO-USAR. Não é prova independente da verdade dos dados. |
| V2-02 | Candidatos, partidos, números, chapa eleita | `recalculo.json` seção candidatos/identidades + `fontes/candidaturas-rj-filtradas.json`; TRE-RJ 15/10 cita chapa Ruas/Fernanda e 50,88%. |
| V2-03 | Categorias e participação | `recalcular_independente.py`/`recalculo.json`, 183 identidades locais; `fontes/detalhe-oficial-totais.json`, linhas 4–30, reconfirma 27 totais de arquivo oficial novo. |
| V2-04 | Retotalização não transfere votos | `recalculo.json`, retotalizacao; TRE-RJ 10/10 conserva 4.271.199 e exclui 274.411 do denominador. |
| V2-05 | Anthony corresponde a nulos técnicos | `recalculo-secoes.json`: número10 =274.411; 183 município-zonas, 0 divergências. Código96 =675.292; código95 =501.537. |
| V2-06 | Margens capital/restante | `recalculo.json`, territorio; diferença estadual 564.215. Confere README e análise §§1/4. |
| V2-07 | Não houve segundo turno estadual no resultado vigente | TRE-RJ15/10 proclama eleito no primeiro turno e diz segundo turno desnecessário; TSE calendário25/10 é eventual, não prova de realização estadual. |
| V2-08 | Situação processual sem trânsito presumido | PJe02/10 é interlocutória; TSE08/10 noticia mérito; TRE15/10 proclama; STF14/10 noticia ação do PSD. Análise linhas7/94 distingue limite de autos. |
| V2-09 | Alegação não tratada como fato | CNN04/11 usa acusação/petição; análise linhas112 e96/100 separa alegações, endosso e voto. Não validei compra de votos/fraude ou magnitude. |
| V2-10 | Apoio posterior de Wladimir não explica voto já depositado | NF05/10, discurso após votação04/10; sem segundo turno estadual efetivo, não demonstra transferência realizada. |

## 7. Fontes, limitações de acesso e reconferência

Fontes abertas centrais: TRE-RJ retotalização10/10 e proclamação15/10; TSE julgamento08/10/pauta/calendário; decisão PJe02/10; Senado08/10; MPF08/10; STF notícia14/10 e cabeçalho ADPF; TSE dados de candidaturas/detalhe; NF05/10; CBN19/08; CNN04/11; Valor03/10; biografia Câmara. URLs, obtenção com offset −03, SHA-256 e tipo do snapshot em `fontes-usadas.json` e catálogo compartilhado `revisao/catalogo/fontes.csv`.

Downloads HTML diretos de TRE/TSE e STF retornaram **403**, mas WebFetch apresentou texto legível. Preservei respostas HTTP de erro separadas e **excertos da extração WebFetch**, explicitamente não HTML original, sem apresentar hash de página de bloqueio como autenticidade da notícia. WebFetch pode usar cache: a leitura nesta revisão não certifica a geração naquele instante. Senado, MPF, PJe, NF, CBN, CNN e Valor foram também preservados em HTML legível. AeF é republicação, não confirmação independente do TSE.

**Não obtido/reexecutado:** inteiro teor do acórdão08/10; decisão de Nunes Marques04/10; autos/relatório integral da proclamação15/10; decisões completas/andamentos carregados da ADPF e prova do evento27/10; inicial/provas/identificação processual completa da ação noticiada04/11; processos de substituição dos vices de Anthony; certidão de trânsito eleitoral; extração integral do ZIP de seções; nova aquisição do ZIP nacional de votação nominal. As identidades individuais de escolha ou transferência e a magnitude de alegada fraude não são recuperáveis por simples soma territorial.

Para procurar o inteiro teor, fiz buscas pelo número RO-EI e consultei documento oficial PJe disponível, notícia original TSE e republicação PDF, que se revelou petição. A extração STF não trouxe abas internas. Pesquisa de método adicional (skill unblock-research): memória sem método salvo; busca web por Grok Bot/PJe sem solução pública específica comprovada; tentativa de busca pública X rejeitada por operador inválido. Não tratei resultados dessas buscas como prova jurídica, não instalei integração, não usei endpoints internos nem contornei login. Limitei a conclusão ao material realmente aberto.

**Reconferência:** ref65blobs e ZIP; soma por seção versus nominal; 27 totais do novo detalhe oficial; cálculo direto das maiorias e margem (`reconferencia.json`). Nenhum problema grave emergiu. A ressalva jurídica A2-01 foi confrontada com texto TSE original, não sustentada apenas em republicação. A pista CBN/Rosinha deve ser compartilhada na consolidação com o papel de redes políticas; não a dupliquei como erro factual do estudo.

### Próximo passo por materialidade

Manter a contabilidade, o primeiro turno proclamado, a separação anulação/transferência e o tratamento cauteloso das acusações. Complementar fundamento jurídico e obter autos centrais para fechar o estado processual. Ampliar rede Rosinha/Clarissa com documentos/eventos datados, sem prometer quantificação causal de votos. Este é parecer da especialidade, não auditoria integral do projeto.
