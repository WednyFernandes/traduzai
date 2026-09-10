---
name: TraduzAI
type: Tool
status: no-ar
line: "Automatiza variáveis de texto no Illustrator e exporta CSV pra fluxo de tradução."
line_en: "Automates text variables in Illustrator and exports CSV for a translation workflow."
link: https://github.com/WednyFernandes/traduzai
cta: github
site: true
year: 2025
tags: [illustrator, extendscript]
license: MIT
---

# TraduzAI

> Automatiza variáveis de texto no Illustrator e exporta CSV pra fluxo de tradução.

![Illustrator](https://img.shields.io/badge/Illustrator-2023+-FF9A00?logo=adobeillustrator&logoColor=white)
![ExtendScript](https://img.shields.io/badge/ExtendScript-JSX-FF9A00)
![Status](https://img.shields.io/badge/status-no%20ar-3fb950)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-0969da)

## O que é

Transformar cada texto de uma peça em variável do Illustrator, um por um,
pra depois traduzir, é trabalho repetitivo. O `TraduzAI.jsx` é um script com
interface (ScriptUI) que roda uma Action do Illustrator em lote sobre os
objetos de texto selecionados, com barra de progresso e cancelamento, e no
final exporta os textos coletados num CSV pronto pra mandar pra tradução.

## Stack

| Tecnologia | Versão | Para quê |
|---|---|---|
| Adobe Illustrator | 2023+ | Ambiente de execução do script (`package.json` declara `"illustrator": ">=2023"`) |
| ExtendScript (JSX) | — | Linguagem do script, roda dentro do próprio Illustrator |

## Requisitos

- Adobe Illustrator 2023 ou mais recente (testado até a versão 2025)
- Uma Action do Illustrator já criada, que converta texto selecionado em variável

## Instalação

1. Copie `TraduzAI.jsx` para a pasta de Scripts do Illustrator:
   `Presets/[idioma]/Scripts/`
2. Reinicie o Illustrator (ou abra o menu **File > Scripts** de novo) pra ele
   aparecer na lista.

## Como usar

1. Crie no Illustrator uma Action que converte o texto selecionado em
   variável (Window > Actions, gravar: Window > Variables > "Make Text
   Dynamic").
2. Selecione os objetos de texto no documento e rode
   **File > Scripts > TraduzAI**.
3. Informe na interface o nome da Action, o conjunto de Actions e o prefixo
   das variáveis, clique **START** e acompanhe o progresso.
4. Ao final, exporte o CSV com os textos coletados.

```
$ File > Scripts > TraduzAI
> Nome da Action: setvar
> Conjunto: Ações Padrão
> Prefixo: Variável
> START
Processando 40 de 40...
Processamento concluído! Ação 'setvar' executada para 40 objetos.
Deseja exportar um arquivo CSV com os dados das variáveis? [Sim]
Arquivo CSV exportado com sucesso!
```

Não há flags de linha de comando — toda configuração é feita pela interface
ScriptUI (nome da Action, conjunto de Actions e prefixo de variável, ver
`ACTION_NAME`, `ACTION_SET` e `VARIABLE_PREFIX` no topo de `TraduzAI.jsx`).

## Como funciona

O script usa `ScriptUI` para a interface e processa os objetos selecionados
em lotes de no máximo 2 por vez (`Math.min(batchSize, 2)`, linha 192 de
`TraduzAI.jsx` — valor travado no código, não configurável pela UI, de
propósito para não travar máquinas fracas), rodando a Action informada sobre
cada um via `app.doScript`. Acima de 50 objetos selecionados o script avisa
antes de continuar, e acima de 100 pede confirmação extra. Cada resultado é
coletado e, ao final (ou pelo botão "Exportar CSV Existente", que varre as
variáveis já criadas no documento), gravado num `.csv` em UTF-8 através de
`File.saveDialog`.

## Estrutura

```
TraduzAI.jsx          # o script: interface, processamento em lote, export CSV
LANGUAGE-CONFIG.md     # nomes de Action Set por idioma do Illustrator
```

## Estado

Funciona o fluxo completo: rodar a Action em lote, exportar CSV, reimportar
tradução como variável. Depende de a Action já existir no Illustrator antes
de rodar o script — não há como criar a Action pelo próprio script.

## Licença

MIT.
