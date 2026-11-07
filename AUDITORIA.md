# Auditoria e limitações

O projeto anterior foi consultado em README, AUDITORIA, manifesto e scripts: foram aproveitadas a separação de evidência e hipótese, identidades contábeis, rastreabilidade e cautela com fluxos individuais. Não foram copiadas suas conclusões presidenciais nem presumida eleição estadual em dois turnos.

## Alcance verificado

- 92 municípios; 183 pares município-zona; 37.675 seções principais de governador.
- TSE 2022/2026 para comparações municipais e eleição presidencial no primeiro turno; IBGE para correspondência e malha atual.
- Três relatórios originais: Datafolha, Paraná, Atlas. Quaest final é evidência secundária identificada.
- Resultado oficial reconciliado e história jurídica checada em notícias institucionais, com consulta ao andamento da ADPF.
- Fontes e amostras não foram consideradas homogêneas por conveniência.

## Limites materiais

1. **Causalidade:** não há painel individual, amostragem pós-eleitoral validada, dados completos de exposição ou estratégia de identificação causal. Resultados territoriais não revelam transferências de pessoas.
2. **Cobertura documental:** não se completou inventário de todos os endossos, programas, anúncios, gastos, métricas de redes e debates. O relatório registra o que foi encontrado e não atribui efeito aos itens ausentes.
3. **Pesquisas:** fichas das ondas iniciais Datafolha não foram recuperadas separadamente; a série vem de original posterior. Quaest e Veritá têm graus diferentes de disponibilidade. Divergências internas e entre republicações constam em FONTES.
4. **História:** 2018 é contextual, sem microdados auditados; 2024 usa total oficial municipal. Não se estimam fluxos 2018–2026 nem estabilidade dos limites de zonas.
5. **Situação jurídica:** proclamação é fato; trânsito em julgado não foi demonstrado. Ação de novembro contém alegações, não conclusão pericial deste estudo. As notícias oficiais não substituem todos os autos e acórdãos.
6. **Território:** regiões analíticas definidas explicitamente; Metropolitana é sobreposta. Geometria IBGE simplificada; sem mapas de limites de seção inventados.
7. **Participação:** comparecimento agregado não identifica entradas/saídas individuais. Não existiu segundo turno estadual no recorte; o presidencial não é seu substituto.
8. **Aquisição:** dois downloads do TRE deram 403, embora as páginas fossem lidas pela ferramenta web. Não há HTML local desses dois endereços. Data/hashes dos recortes herdados são distintos de uma revalidação viva dos ZIPs nacionais.
9. **Número errado:** código 96 agrupa nulos e não informa se foram digitados como 13, nem qual era a intenção. A pesquisa de conhecimento de número não é contagem de erros reais.

A entrega é uma síntese descritiva auditável e uma avaliação das explicações disponíveis, não uma determinação causal exaustiva. As lacunas acima também aparecem próximas às afirmações no relatório. Verificações executadas e hashes dos produtos estão em [reproducao.json](results/reproducao.json).

Validação adicional: reprodução offline com pastas de resultados e figuras inicialmente vazias produziu arquivos idênticos. [Registro](data/clean-reproduction.json).
