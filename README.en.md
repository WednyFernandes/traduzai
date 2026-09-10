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

Automates text variables in Illustrator and exports CSV for a translation workflow.

## What it is

Turning every text object in a piece into an Illustrator variable, one by
one, before translating it, is repetitive work. `TraduzAI.jsx` is a script
with a GUI (ScriptUI) that runs an Illustrator Action in batch over the
selected text objects, with a progress bar and cancellation, and at the end
exports the collected texts to a CSV ready to send off for translation.

## How to use it

1. In Illustrator, create an Action that converts the selected text into a
   variable (Window > Actions, record: Window > Variables > "Make Text
   Dynamic").
2. Copy `TraduzAI.jsx` to the Illustrator Scripts folder
   (`Presets/[language]/Scripts/`).
3. Select the text objects in the document and run
   **File > Scripts > TraduzAI**.
4. In the interface, enter the Action name, the Action set, and the
   variable prefix, click **START**, and watch the progress.
5. At the end, export the CSV with the collected texts.

Tested on Adobe Illustrator 2025.

## How it works

The script uses `ScriptUI` for the interface and processes the selected
objects in batches of 10, running the given Action on each one via
`app.doScript`; each result is collected and, at the end (or via the
"Export Existing CSV" button, which scans the variables already created in
the document), written to a `.csv` file in UTF-8 through `File.saveDialog`.

## State

The full workflow works: run the Action in batch, export CSV, reimport the
translation as a variable. It depends on the Action already existing in
Illustrator before running the script — the script itself can't create the
Action.

## License

MIT.
