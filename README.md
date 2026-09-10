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
tags: [python, illustrator]
---

# TraduzAI

Automatiza variáveis de texto no Illustrator e exporta CSV pra fluxo de tradução.

## O que é

Transformar cada texto de uma peça em variável do Illustrator, um por um,
pra depois traduzir, é trabalho repetitivo. O `TraduzAI.jsx` é um script com
interface (ScriptUI) que roda uma Action do Illustrator em lote sobre os
objetos de texto selecionados, com barra de progresso e cancelamento, e no
final exporta os textos coletados num CSV pronto pra mandar pra tradução.

## Como usar

1. Crie no Illustrator uma Action que converte o texto selecionado em
   variável (Window > Actions, gravar: Window > Variables > "Make Text
   Dynamic").
2. Copie `TraduzAI.jsx` para a pasta de Scripts do Illustrator
   (`Presets/[idioma]/Scripts/`).
3. Selecione os objetos de texto no documento e rode
   **File > Scripts > TraduzAI**.
4. Informe na interface o nome da Action, o conjunto de Actions e o prefixo
   das variáveis, clique **START** e acompanhe o progresso.
5. Ao final, exporte o CSV com os textos coletados.

Testado no Adobe Illustrator 2025.

## Como funciona

O script usa `ScriptUI` para a interface e processa os objetos selecionados
em lotes de 10, rodando a Action informada sobre cada um via
`app.doScript`; cada resultado é coletado e, ao final (ou pelo botão
"Exportar CSV Existente", que varre as variáveis já criadas no documento),
gravado num `.csv` em UTF-8 através de `File.saveDialog`.

## Estado

Funciona o fluxo completo: rodar a Action em lote, exportar CSV, reimportar
tradução como variável. Depende de a Action já existir no Illustrator antes
de rodar o script — não há como criar a Action pelo próprio script.

## Licença

MIT.
