# Estudo eleitoral do Rio de Janeiro — 2026

Investigação independente e apartidária. Fontes consultadas até **7 de novembro de 2026**. Projeto separado de `analise-eleitoral-2026`. Repositório privado autorizado pelo usuário para auditoria; nenhuma publicação pública.

**A expectativa de vitória de Eduardo Paes tinha respaldo nas pesquisas, mas subestimou o resultado de Douglas Ruas. Paes venceu na capital e perdeu a disputa estadual porque sua vantagem carioca foi mais que compensada fora dela. A vitória de Ruas já no primeiro turno teve uma causa adicional e distinta: a anulação dos votos de Anthony Garotinho reduziu o total de votos válidos. Nenhum desses votos foi acrescentado a Ruas.**

Paes abriu **410.961 votos** na capital; Ruas abriu **975.176 fora dela**, vencendo por **564.215 votos** no estado. Ruas recebeu **4.271.199 votos** e Paes, **3.706.984**. A retotalização elevou Ruas de **49,27% para 50,88%** sem mudar esses votos. [Cálculos](results/resumo.json) · [TRE-RJ](https://www.tre-rj.jus.br/comunicacao/noticias/2026/Outubro/retotalizacao-de-votos-aponta-douglas-ruas-como-vencedor-no-primeiro-turno-para-o-governo-do-rj).

**A impressão de que Ruas era pouco conhecido não significa que ele não tivesse base.** Em 2022 recebeu 175.977 votos para deputado, 149.576 em São Gonçalo. Sua candidatura estadual combinou essa base familiar e territorial com o apoio do campo de Flávio Bolsonaro e uma identificação partidária disponível ao eleitor. A amplitude de 2026 excedeu muito São Gonçalo: venceu em 79 dos 92 municípios. Esses fatos sustentam a importância da coalizão e da expansão territorial; não quantificam quantos votos cada liderança produziu. [Análise e fontes](ANALISE-DETALHADA.md).

**Garotinho, aqui, é Anthony Garotinho, candidato a governador pelo Republicanos.** Wladimir Garotinho, seu filho e candidato a deputado federal pelo PL, é outro ator: declarou apoio a Ruas depois da votação, dizendo ter apoiado o pai no primeiro turno. Não ocorreu segundo turno para governador no recorte observado. Portanto, o endosso posterior não demonstra transferência realizada. O efeito jurídico dos 274.411 votos anulados é comprovado; uma operação de transferência política não é. [Cronologia](research/CRONOLOGIA.md).

| Explicação | Classificação | O que a sustenta e o que falta |
|---|---|---|
| A vantagem fora da capital superou a de Paes na capital | **Estabelecida** | TSE, reconciliado por município, zona e seção |
| A exclusão de Garotinho encerrou a disputa no primeiro turno | **Estabelecida no resultado proclamado** | Votação inalterada, denominador menor; há contestação judicial, sem trânsito em julgado demonstrado neste estudo |
| Ruas cresceu durante a campanha | **Apoiada por pesquisas** | Série comparável do Datafolha: 19% → 31% entre agosto e início de outubro; não localiza a ultrapassagem real |
| Base prévia e associação ao bolsonarismo ajudaram Ruas | **Apoiada por evidências convergentes** | Votação anterior, apoios documentados e comparação presidencial; efeitos individuais não identificados |
| Popularidade municipal garantia vitória estadual | **Refutada como garantia** | Paes manteve força carioca, insuficiente para o conjunto do estado |
| Prefeitos, igrejas, propaganda ou um debate explicam uma quantidade determinada de votos | **Ainda não demonstrada** | Faltam exposição individual, painel de mudança e identificação causal; endosso não equivale a entrega |
| Garotinho transferiu seus votos para Ruas | **Ainda não demonstrada** | Anulação não é transferência; apoio de Wladimir é posterior; intenção hipotética de segundo turno não é voto observado |
| Houve uma virada de última hora claramente datada | **Ainda não demonstrada** | Pesquisas mostravam aproximação, mas não separam mudança tardia de vieses de medição e participação |

A conclusão mais segura é uma **combinação de base política já existente, expansão estadual de Ruas, limite territorial da vantagem de Paes e decisão jurídica que dispensou nova votação**. O peso causal de campanha, rejeição, religião, serviços ou redes sociais permanece indeterminado. As pesquisas não autorizavam certeza de vitória de Paes; o resultado tampouco autoriza declarar que sua liderança anterior nunca existiu.

- [Análise detalhada](ANALISE-DETALHADA.md): pesquisas, mecanismos, regiões, história, participação e contraexemplos.
- [Tabelas](results/TABELAS.md), [municípios](results/municipios.csv), [zonas](results/zonas.csv), [seções](results/secoes.csv).
- [Fontes e divergências](research/FONTES.md), [hipóteses e lacunas](research/HIPOTESES.md).
- [Reprodução](REPRODUCAO.md) e [auditoria](AUDITORIA.md).

![Margem municipal](figures/margem.svg)

## Revisão independente

[Prompt completo para o Grok Bot](review-instructions/PROMPT-GROK.md) · [Como conectar e usar](review-instructions/COMO-USAR.md) · [Briefing original](review-instructions/BRIEFING-ORIGINAL.md). O ZIP bruto de seções é um asset da release privada `dados-v1`; restaure-o antes de reproduzir em um clone novo.
