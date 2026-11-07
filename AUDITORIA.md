# Verificações e limitações

O estudo aproveitou os métodos de conferência do projeto `analise-eleitoral-2026`: preservação das fontes, checagem dos totais e comparação entre municípios. As conclusões sobre a eleição estadual foram construídas separadamente.

## O que foi conferido

- Votos e participação em 92 municípios, 183 pares município-zona e 37.675 seções principais de governador.
- Dados do TSE de 2022 e 2026, incluindo a votação presidencial no primeiro turno. Os nomes e a malha dos municípios vêm do IBGE.
- Os totais por seção coincidem com os totais por zona. A soma dos votos válidos, brancos e nulos coincide com o comparecimento.
- Foram arquivados os relatórios originais do Datafolha de 2/10 e de 2–3/10, da Paraná de setembro e outubro e da Atlas de setembro. A última Atlas está numa republicação do Poder360. Faltam o original dessa onda no site do instituto, o relatório original da Quaest e a conferência visual dos PDFs da Real Time Big Data.
- A história judicial foi conferida em notícias institucionais. As páginas do TRE retornaram erro 403 no download e não têm cópia local. O acórdão de 8/10 não foi obtido.

## Limitações que afetam a interpretação

1. **Mudança de voto.** Não há pesquisa que acompanhe os mesmos eleitores durante toda a campanha. Os resultados municipais mostram diferenças entre lugares, mas não revelam quem mudou de candidato ou por quê.
2. **Campanha.** O levantamento de apoios, propostas, anúncios, gastos e debates é parcial. Faltam medidas de audiência e de exposição dos eleitores. As buscas realizadas estão em [lacunas](research/LACUNAS.md).
3. **Pesquisas.** Faltam fichas das primeiras ondas do Datafolha, consulta ao PesqEle, microdados e pesos. O cruzamento presidencial de 25/9 não tem a tabela original, e os percentuais publicados não fecham entre si. As divergências estão em [fontes](research/FONTES.md).
4. **Comparações históricas.** Os dados de 2018 vêm de veículos que reproduzem o TSE; os de 2024, de notícia do próprio TSE. Não há recortes locais para recalculá-los. Os 183 códigos de zona coincidem em 2022 e 2026, mas isso não garante que as áreas abrangidas sejam iguais.
5. **Situação jurídica.** Ruas foi proclamado eleito, mas não foi comprovado o encerramento definitivo dos processos. Faltam o acórdão de 8/10, a certidão de trânsito e os andamentos completos da ADPF 1362. A ação de novembro contém acusações ainda sem comprovação pericial neste estudo.
6. **Território.** As regiões usadas na análise estão definidas no código. A Região Metropolitana é uma agregação adicional e sobreposta às demais. Os mapas usam a malha simplificada do IBGE; não há mapas dos limites de zonas ou seções.
7. **Participação.** Os totais de comparecimento não mostram quais eleitores passaram a votar ou deixaram de votar. Falta o detalhamento da participação na disputa presidencial. Não houve segundo turno estadual no resultado proclamado.
8. **Arquivos de origem.** Os ZIPs nacionais não foram baixados novamente na correção do estudo. A auditoria de 7/11 encontrou conteúdo eleitoral igual ao dos recortes, embora os hashes dos ZIPs fossem diferentes por regeneração dos arquivos. O projeto anterior não estava disponível naquela etapa. O script de download preserva versões anteriores.
9. **Erros de número.** O código 96 reúne os votos nulos e não permite contar os digitados como 13. A alegação de 204.309 ocorrências não foi confirmada. Saber ou não o número numa entrevista também não determina o que a pessoa digitou na urna.
10. **Afirmações sem fonte suficiente.** Permanecem sem confirmação os números 48,1/39,0 atribuídos a um agregador, a fala de Anthony em 4/10 e a sucessão de Ricardo Couto. Também não foram verificados a estabilidade territorial das zonas, as bases brutas dos gráficos e o download direto do asset privado. Essas limitações estão indicadas nos trechos correspondentes.

O estudo permite conferir a votação e avaliar as explicações disponíveis, mas não medir o peso de cada causa. Os comandos executados e os hashes dos resultados estão em [reproducao.json](results/reproducao.json).

O [registro anterior de reprodução limpa](data/clean-reproduction.json) relata uma execução com pastas vazias, mas não contém data, hashes ou log suficientes para verificá-la por conta própria. Os [pareceres da auditoria de 7/11](auditoria-2026-11-07/PARECER-FINAL.md) ficam preservados como histórico da revisão.
