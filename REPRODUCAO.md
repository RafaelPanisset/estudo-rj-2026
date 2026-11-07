# Reprodução

Python **3.11 ou superior**, biblioteca padrão; sem pacotes pip para reproduzir cálculos, mapas SVG e auditorias. Poppler (`pdftotext` e `pdftoppm`) foi usado para conferir pesquisas; não é necessário para recalcular tabelas. Os mapas são gerados diretamente da malha GeoJSON do IBGE.

Da pasta do projeto:

```bash
python3 scripts/reproduce.py
```

O comando verifica hashes dos snapshots antes de executar a agregação municipal e por zona, a reconciliação por seção, mapas, confronto de pesquisas e tabelas. Não use `python -O`: as verificações contábeis usam assertivas. A reprodução é local e não exige acesso ao projeto anterior.

## Arquivos e aquisição

- `raw/votacao-2026-RJ.csv`, `detalhe-2026-RJ.csv`, `votacao-2022-RJ.csv` e `presidente-*-RJ.csv`: recortes dos ZIPs TSE que já estavam no projeto anterior, obtidos ali em 1/11. SHA-256 dos ZIPs foi conferido com o manifesto anterior; extração em 7/11. Não se alegou novo download vivo desses arquivos.
- `scripts/prepare.py` documenta e refaz essa extração caso os ZIPs do projeto vizinho estejam presentes. É uma etapa opcional de aquisição, não dependência da reprodução entregue. Não modifica o projeto anterior.
- `raw/secoes-RJ.zip`: download novo do TSE em 7/11; `secoes-governador.csv`: recorte reproduzível do ZIP. Para testar a extração novamente, mova o CSV temporariamente e rode `scripts/sections.py`.
- `scripts/download.py`: documenta URLs e baixa IBGE, pesquisas e páginas. Reexecutá-lo pode substituir snapshots por versões atuais; guarde a versão anterior e regenere os manifestos apenas após revisar mudanças.
- `data/source-manifest.json`, `download-manifest.json`, `secoes-download.json`: procedência, datas, transformações, falhas e hashes de aquisição.
- `data/snapshot-manifest.json`: hash de todos os insumos preservados, incluindo pesquisas transcritas. Não identifica conteúdo como verdadeiro só por ter hash.
- `data/pesquisas.csv`: transcrição editorial dos originais; páginas e ressalvas na coluna observação. A execução não extrai novamente os números dos PDFs.
- `data/correspondencia-tse-ibge.csv`: junção explícita de 92 municípios, nomes normalizados únicos; não usar código TSE como código IBGE.

## Verificações relevantes

1. Totais dos candidatos = válidos; válidos + brancos + nulos = comparecimento; aptos = comparecimento + abstenção, nas 183 unidades município-zona.
2. Votação de Ruas e Paes por seção recompõe as mesmas 183 unidades; Anthony recompõe nulos técnicos e brancos recompõem seu total.
3. Estado coincide com totais publicados pelo TRE; margem calculada com inteiros, sem subtração de percentuais arredondados.
4. Regiões analíticas particionam 92 municípios sem duplicação; Metropolitana é agregação adicional sobreposta, nunca somada às anteriores.
5. Mapas têm 92 correspondências com IBGE; percentuais usam denominadores declarados.
6. Links locais existem; SVG tem XML válido; execução termina com código zero.

[Registro da execução](results/reproducao.json). README e análise são textos editoriais e não são reescritos pelos scripts; mudanças de dados exigem revisão humana das afirmações. Hashes de resultados permitem comparar execuções. Os arquivos de terceiros preservados destinam-se à auditoria local; não foi aplicada licença própria ao conteúdo deles.

Validação adicional: reprodução offline com pastas de resultados e figuras inicialmente vazias produziu arquivos idênticos. [Registro](data/clean-reproduction.json).
