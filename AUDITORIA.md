# Auditoria e limitações

O projeto anterior foi consultado em README, AUDITORIA, manifesto e scripts: foram aproveitadas a separação de evidência e hipótese, identidades contábeis, rastreabilidade e cautela com fluxos individuais. Não foram copiadas suas conclusões presidenciais nem presumida eleição estadual em dois turnos.

## Alcance verificado

- 92 municípios; 183 pares município-zona; 37.675 seções principais de governador.
- TSE 2022/2026 para comparações municipais e eleição presidencial no primeiro turno; IBGE para correspondência e malha atual.
- Relatórios originais arquivados: Datafolha de 2/10, Paraná de setembro e Atlas de setembro. A onda Datafolha de 2–3/10, o Paraná de outubro e a Atlas de 3/10 entraram por transcrição da auditoria de 7/11/2026; os PDFs novos não estão neste repositório. Quaest e Real Time Big Data são evidência secundária.
- Resultado reconciliado contra os recortes e contra constantes do código. As páginas do TRE deram 403 e não há snapshot local. A história jurídica usa notícias institucionais. O acórdão de 8/10 não foi obtido.
- Fontes e amostras não foram consideradas homogêneas por conveniência.

## Limites materiais

1. **Causalidade:** não há painel individual, amostragem pós-eleitoral validada, dados completos de exposição ou estratégia de identificação causal. Resultados territoriais não revelam transferências de pessoas.
2. **Cobertura documental:** não se completou inventário de todos os endossos, programas, anúncios, gastos, métricas de redes e debates. O que foi buscado e não obtido está em [lacunas](research/LACUNAS.md). O relatório não atribui efeito aos itens ausentes.
3. **Pesquisas:** fichas das ondas iniciais do Datafolha não foram recuperadas separadamente. PesqEle, microdados e pesos não foram obtidos. A Atlas de 3/10 só está em republicação. Os números da Real Time Big Data não foram conferidos visualmente. O cruzamento de 25/9 não tem matriz, e as duas rotas não fecham. Divergências constam em FONTES.
4. **História:** 2018 é contextual, sem microdados; o turno está indicado. 2024 é dado documental da notícia do TSE, sem recorte preservado. Os 183 códigos de zona coincidem em 2022 e 2026; a estabilidade do território não é verificável. Não se estimam fluxos.
5. **Situação jurídica:** proclamação é fato; trânsito em julgado não foi demonstrado. Faltam o acórdão de 8/10, a certidão e os andamentos completos da ADPF 1362. Ação de novembro contém alegações, não conclusão pericial.
6. **Território:** regiões analíticas definidas explicitamente; Metropolitana é sobreposta. Geometria IBGE simplificada, com escala vertical corrigida; sem mapas de limites de seção inventados.
7. **Participação:** comparecimento agregado não identifica entradas/saídas individuais. Não existiu segundo turno estadual no resultado proclamado; o presidencial não é seu substituto. O detalhe de participação do cargo 1 não está nos insumos.
8. **Aquisição:** dois downloads do TRE deram 403. Não há HTML local desses endereços. Os SHA dos ZIPs-pai não foram reverificados por novo download; a auditoria de 7/11 registrou hashes atuais diferentes e conteúdo idêntico, exceto a geração. `download.py` não foi executado nesta correção e passou a preservar snapshots. O projeto vizinho não estava disponível.
9. **Número errado:** código 96 agrupa nulos e não informa se foram digitados como 13. A alegação de 204.309 não foi certificada. A pesquisa de conhecimento de número não é contagem de erros reais.
10. **O que não é fato:** achados não verificáveis da auditoria — agregador 48,1/39,0, PesqEle, reorganização territorial, bases brutas dos gráficos, asset privado baixado diretamente — entram como ressalva, não como constatação. A fala de Anthony em 4/10 e a sucessão de Couto seguem sem fonte preservada.

A entrega é uma síntese descritiva auditável e uma avaliação das explicações disponíveis, não uma determinação causal exaustiva. As lacunas acima também aparecem próximas às afirmações no relatório. Verificações executadas e hashes dos produtos estão em [reproducao.json](results/reproducao.json).

O registro de reprodução limpa de 7/11 ([clean-reproduction.json](data/clean-reproduction.json)) não tem data, hashes nem log. Confirma uma execução anterior com pastas vazias. Não é, sozinho, uma trilha auditável. O registro novo fica em `results/reproducao.json`.

A correção aplicada a partir da auditoria independente está descrita no pull request e os pareceres consolidados estão em [auditoria-2026-11-07](auditoria-2026-11-07/PARECER-FINAL.md).
