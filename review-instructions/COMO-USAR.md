# Usar o Grok Bot para revisar este projeto

Pesquisa feita em **7/11/2026**, priorizando documentação oficial. As recomendações de método abaixo são escolhas para esta auditoria, não promessas de acurácia do produto.

## Recomendação

Use o Grok Bot para coordenar a investigação documental e os pareceres. Use o Cursor se quiser acompanhar edições e correções pelo editor depois. Ambos oferecem recursos de agentes; não há fundamento para dizer que Cursor só serve para código ou que nele cada revisor precisa ser acionado manualmente. A existência de mais bots não garante revisão melhor.

O Cursor anunciou em 14/8/2026 sua aquisição pela SpaceX: [anúncio oficial](https://cursor.com/en-US/blog/joining-spacex). A documentação do Cursor também descreve o Grok Bot: [visão geral](https://cursor.com/docs/grok-bot).

## Como começar

1. Abra o Grok Bot e escolha um bot existente como coordenador desta tarefa. Não precisa mudar seu bot principal.
2. Em **Connect apps**, procure GitHub, ou peça ao bot acesso ao link privado e use o cartão de conexão. Conclua a autenticação no fluxo do provedor. Autorize somente este repositório quando essa seleção estiver disponível. Não cole senha/token no chat.
3. Envie o link direto https://github.com/RafaelPanisset/estudo-rj-2026/blob/main/review-instructions/PROMPT-GROK.md. Peça que leia o arquivo inteiro e execute suas instruções. O caminho local do seu computador não dá acesso ao ambiente do Grok; o link privado também exige a autorização do passo 2. Como alternativa, anexe o arquivo Markdown, mantendo o acesso ao repositório para consultar código, fontes e dados.
4. O briefing já está em [BRIEFING-ORIGINAL.md](BRIEFING-ORIGINAL.md). Os dados e fontes do estudo estão no repositório; o ZIP bruto maior está na release privada `dados-v1`.
5. O coordenador deve confirmar o acesso, registrar o commit, criar os nove revisores e apresentar a divisão antes de começar. Se a versão/conta não permitir criação automática, ele deve fornecer a configuração para criar com **New Bot**, sem fingir que criou.
6. Receba os relatórios e o ZIP de revisão. Não conceda permissão de push só para obter pareceres. Se a integração pedir permissões maiores que leitura, avalie o escopo apresentado; instruir “somente leitura” não muda o escopo técnico do aplicativo.

## Restaurar o arquivo grande para reproduzir

O GitHub bloqueia arquivos acima de 100 MiB no Git normal. O ZIP oficial tem 296.106.129 bytes e foi colocado como asset de release no mesmo repositório privado. Os recortes CSV continuam no Git. [Documentação GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Em uma cópia clonada, com GitHub CLI autenticado para este repositório:

```bash
gh release download dados-v1 --repo RafaelPanisset/estudo-rj-2026 --pattern secoes-RJ.zip --dir raw
python3 -c 'import hashlib,pathlib; p=pathlib.Path("raw/secoes-RJ.zip"); actual=hashlib.file_digest(p.open("rb"),"sha256").hexdigest(); expected="ec93c020ae1f0088216de92e5acc5d3211aefaf1fa589b961132bbf471ee3cf5"; print(actual); assert actual == expected, "SHA-256 divergente"'
python3 scripts/reproduce.py
```

Se o arquivo já existir, confira o hash antes; não use sobrescrita automática. A integração GitHub do Grok pode não disponibilizar credenciais ao `gh`: nesse caso, o bot deve usar a capacidade autenticada de download da integração/navegador ou o usuário pode anexar o asset. Não deve pedir que o usuário exponha token no chat.

Alternativa: a URL pública original está em `data/secoes-download.json`; um novo download do TSE só substitui este snapshot se o SHA-256 coincidir. Se mudou, preserve como nova versão e registre a divergência. Não altere o manifesto para fazer a checagem passar.

A reprodução deve ocorrer em cópia de trabalho porque reescreve `results/`, `figures/` e a tabela de correspondência. As conclusões da cópia de referência devem permanecer intactas.

## O que a documentação confirmou

| Fato do produto | Fonte oficial | Implicação para a revisão |
|---|---|---|
| Bots existentes podem criar bots especializados; tarefas e responsabilidades são dadas por mensagem | [Create and manage Bots](https://docs.x.ai/grok-bot/bots) | Enviar o prompt ao coordenador é um fluxo suportado; ainda depende das capacidades da conta |
| Bots compartilham arquivos, sessões e credenciais num computador persistente | [Computer and apps](https://docs.x.ai/grok-bot/computer-and-apps) | Separar pastas e cópias evita conflitos; não alegar isolamento de segurança entre bots |
| Bots têm memória própria, mas memória não substitui fonte atual | [How Grok Bot works](https://docs.x.ai/grok-bot/how-grok-bot-works) | Reabrir documentos e registrar evidência em arquivos |
| Há integração GitHub e cartões para conexão a repositórios | [Changelog oficial](https://x.ai/changelog/bot) | Usar autorização nativa; o link privado sozinho não libera acesso |
| Bots podem coordenar trabalho e operar em segundo plano | [Cursor: Grok Bot](https://cursor.com/docs/grok-bot) | Entregar tarefa com fim explícito, sem transformar a auditoria em rotina infinita |

## Decisões metodológicas deste projeto

- Nove revisores especializados e coordenador; três primeiros verificam procedência, resultado e reprodução.
- O nono revisor investiga fatores omitidos, santinhos/números de urna e influência presidencial, sem presumir ocorrência ou causalidade.
- Relatórios iniciais separados, seguida de comparação entre revisores; não confundir isso com independência estatística.
- Um commit de referência e diretórios de saída próprios; nenhum push ou alteração remota nesta fase.
- Uma rodada inicial, uma rodada de esclarecimentos e reconferência de achados graves. Checkpoints se faltar limite de uso.
- Auditar fontes e hipóteses, não simplesmente produzir mais texto ou usar maioria de bots como prova.
- Não conectar Gmail, Slack ou outros serviços sem necessidade. Não importar templates públicos de terceiros para esta tarefa.
- Distinguir autenticação de fonte, integridade do arquivo, reprodução do cálculo e sustentação causal: quatro avaliações diferentes.

O repositório privado melhora o acesso ao conjunto e fixa versões; não valida a pesquisa por si só. Este pacote de instruções foi preparado pelo mesmo GPT que fez o estudo: o revisor deve questionar também o protocolo quando ele omitir testes relevantes.
