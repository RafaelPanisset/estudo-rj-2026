# Reprodução

Python **3.11 ou superior**, biblioteca padrão; sem dependências externas para recalcular tabelas e mapas. Poppler (`pdftotext` e `pdftoppm`) foi usado para conferir pesquisas; não é necessário para recalcular tabelas. Os mapas são gerados diretamente da malha GeoJSON do IBGE.

Da pasta do projeto:

```bash
python3 scripts/reproduce.py
```

O comando confere os hashes e executa cinco etapas: agregação por município e zona, conferência por seção, mapas, comparação de pesquisas e tabelas. Cria `results/` e `figures/` quando necessário. A execução é local e não depende do projeto anterior. O ZIP de seções precisa estar em `raw/`, conforme as instruções abaixo.

Execute sem `-O` ou `PYTHONOPTIMIZE`. O comando principal recusa esses modos; as verificações de cada script usam `if`/`raise` e permanecem ativas mesmo quando executadas separadamente.

## Obter o ZIP de seções

O arquivo excede o limite do Git e está na release privada `dados-v1`. Com GitHub CLI autenticado para este repositório, execute da raiz do projeto:

```bash
gh release download dados-v1 --repo RafaelPanisset/estudo-rj-2026 --pattern secoes-RJ.zip --dir raw
python3 -c 'import hashlib,pathlib; p=pathlib.Path("raw/secoes-RJ.zip"); actual=hashlib.file_digest(p.open("rb"),"sha256").hexdigest(); expected="ec93c020ae1f0088216de92e5acc5d3211aefaf1fa589b961132bbf471ee3cf5"; print(actual); assert actual == expected, "SHA-256 divergente"'
```

Se o arquivo já existir, confira seu hash sem sobrescrevê-lo. O tamanho esperado é 296.106.129 bytes. Alternativamente, obtenha a URL original em `data/secoes-download.json`; só use o novo download como este snapshot se o SHA-256 coincidir. Preserve versões divergentes separadamente. [Registro do snapshot](data/SNAPSHOT-SECOES.md).

## Arquivos e aquisição

- `raw/votacao-2026-RJ.csv`, `detalhe-2026-RJ.csv`, `votacao-2022-RJ.csv` e `presidente-*-RJ.csv`: recortes dos ZIPs TSE que já estavam no projeto anterior, obtidos ali em 1/11. O SHA-256 herdado está no manifesto. Não houve novo download desses ZIPs nacionais nesta correção. A auditoria de 7/11 encontrou hashes diferentes nos ZIPs atuais e conteúdo idêntico, exceto a geração.
- `scripts/prepare.py` refaz essa extração se o projeto vizinho estiver presente. Confere o hash do ZIP pai antes de gravar, corrige o texto de cada transformação e guarda a versão anterior do manifesto em `source-manifest.anterior.json`. É aquisição opcional. Sem o projeto vizinho, termina com mensagem e não altera arquivos.
- `raw/secoes-RJ.zip`: 296.106.129 bytes, SHA-256 `ec93c020ae1f0088216de92e5acc5d3211aefaf1fa589b961132bbf471ee3cf5`. O asset privado `dados-v1` não foi baixado. Nesta correção o arquivo foi obtido do CDN do TSE e o hash coincidiu com o manifesto e com o digest do asset registrado pela auditoria. `secoes-governador.csv` é o recorte. Para testar a extração, mova o CSV e rode `scripts/sections.py`.
- `scripts/download.py`: documenta URLs de IBGE, pesquisas e páginas. Não baixa o ZIP de seções nem os ZIPs nacionais do TSE. Se o arquivo já existe e o hash confere, não o regrava. Se o hash diverge, grava a versão nova ao lado e preserva o snapshot. O log novo vai para `data/download-attempts.json`. `download-manifest.json` permanece como registro histórico. Este script não foi executado nesta correção.
- `data/source-manifest.json`, `download-manifest.json`, `secoes-download.json`: procedência, datas, transformações, falhas e hashes de aquisição. As entradas presidenciais repetem URL e SHA do mesmo ZIP pai já registrado na entrada irmã.
- `data/snapshot-manifest.json`: hash de todos os insumos preservados, incluindo pesquisas transcritas. Não identifica conteúdo como verdadeiro só por ter hash.
- `data/pesquisas.csv`: transcrição editorial. A execução não extrai novamente os números dos PDFs. Conferir a transcrição é outro passo: as páginas estão em [evidencias/2026-11-07/LEIA-ME.md](evidencias/2026-11-07/LEIA-ME.md). Arquivo local com hash não autentica a fonte. Republicação e impressão de matéria não são originais.
- `data/pesquisas-segundo-turno.csv`: transcrição separada dos cenários Ruas × Paes, também com hash no manifesto. Não é inserida em `pesquisas.csv` nem no confronto com a urna. `polls.py` só confere o formato e grava `results/pesquisas-segundo-turno.json`. A leitura dos PDFs que sustentam esses números está na [seção provisória](research/SEGUNDO-TURNO.md).
- `evidencias/2026-11-07/`: pareceres, réplicas e PDFs usados nas ondas novas. `reproduce.py` confere o `SHA256SUMS` dessa pasta. As datas de obtenção são da auditoria de 7/11/2026, não do estudo anterior.
- `results/correspondencia-tse-ibge.csv`: tabela gerada pela correspondência dos nomes dos 92 municípios. Ela relaciona os códigos do TSE aos do IBGE.

## Conferências realizadas

1. Totais dos candidatos = válidos; válidos + brancos + nulos = comparecimento; aptos = comparecimento + abstenção, nas 183 unidades município-zona.
2. Votação de todos os códigos por seção recompõe as 183 unidades: candidatos, brancos, nulos de urna, nulos técnicos, comparecimento e número de seções principais.
3. Estado coincide com as constantes 8.394.627, 4.271.199, 3.706.984 e 274.411, iguais aos recortes TSE. Não há página do TRE arquivada. A margem usa inteiros, sem subtração de percentuais arredondados. O percentual de 49,27% é reconstrução contábil.
4. Regiões analíticas particionam 92 municípios sem duplicação; Metropolitana é agregação adicional sobreposta, nunca somada às anteriores.
5. Mapas têm 92 correspondências com IBGE; percentuais usam denominadores declarados.
6. Links locais existem; SVG tem XML válido; execução termina com código zero.

[Registro da execução](results/reproducao.json): data, comando, versão de Python, flag de otimização, hashes dos insumos e hashes dos resultados antes e depois. O campo de execução offline não é medido; os scripts chamados não abrem rede. README e análise são textos editoriais e não são reescritos pelos scripts; mudanças de dados exigem revisão humana das afirmações. Os arquivos de terceiros preservados destinam-se à auditoria local; não foi aplicada licença própria ao conteúdo deles.

O registro anterior de reprodução com pastas vazias não traz hashes nem data. [Arquivo histórico](data/clean-reproduction.json).

A reprodução completa exige `evidencias/2026-11-07/SHA256SUMS` não vazio e registra seu SHA-256. Ausência, vazio ou divergência de evidência interrompem a execução antes de gerar resultados. Testes de regressão: `python3 -m unittest discover -s tests`. Eles usam pequenos arquivos sintéticos em diretórios temporários e executam o verificador real; não exigem o ZIP de seções nem os PDFs. A reprodução completa exige os arquivos reais.

Correção editorial posterior à auditoria: a observação dos 57% em `data/pesquisas.csv` explicita a base de 1.769 declarantes; o hash desse CSV foi atualizado, sem alterar números. Os pareceres e documentos da auditoria foram preservados como registro histórico.
