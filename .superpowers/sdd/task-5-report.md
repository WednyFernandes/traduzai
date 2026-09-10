
## Task 5 — Correção do tamanho do lote no README

Confirmado diretamente em `TraduzAI.jsx`: linha 192 `var actualBatchSize = Math.min(batchSize, 2);` e linha 482 `processSelectionAsync(sel, 2);` — o lote efetivo é 2, não 10. Ambos os pontos batem exatamente com o que foi relatado.

Alterado `README.md` e `README.en.md`, seção "Como funciona"/"How it works": troquei "lotes de 10"/"batches of 10" por uma formulação que descreve o valor como constante no código (hoje 2, "de propósito baixo para não travar máquinas fracas"), citando o número atual sem prometer que ele nunca muda — assim o texto continua verdadeiro se a constante for ajustada depois, mas ainda dá o dado concreto ao leitor.

Revisei o resto da seção "Como funciona" (ScriptUI, `app.doScript`, botão "Exportar CSV Existente"/"Export Existing CSV", `File.saveDialog`, UTF-8) contra o código e não encontrei outra divergência — `doScript` é chamado na linha 246, `saveDialog` na 568, e a codificação UTF-8 (com BOM) é setada nas linhas 628/632, tudo consistente com a documentação.
