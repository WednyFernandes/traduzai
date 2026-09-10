---
name: TraduzAI
name_en: ""
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

> Automates text variables in Illustrator and exports CSV for a translation workflow.

![Illustrator](https://img.shields.io/badge/Illustrator-2023+-FF9A00?logo=adobeillustrator&logoColor=white)
![ExtendScript](https://img.shields.io/badge/ExtendScript-JSX-FF9A00)
![Status](https://img.shields.io/badge/status-live-3fb950)
![License](https://img.shields.io/badge/license-MIT-0969da)

## What it is

Turning every text in a piece into an Illustrator variable, one by one,
before it can be translated, is repetitive work. `TraduzAI.jsx` is a
scripted UI (ScriptUI) that runs an existing Illustrator Action in batches
over the selected text objects, with a progress bar and cancellation, and
exports the collected text to a CSV ready to send off for translation.

## Stack

| Technology | Version | Used for |
|---|---|---|
| Adobe Illustrator | 2023+ | Runtime for the script (`package.json` declares `"illustrator": ">=2023"`) |
| ExtendScript (JSX) | — | Script language, runs inside Illustrator itself |

## Requirements

- Adobe Illustrator 2023 or newer (tested up to the 2025 release)
- An Illustrator Action already created that converts a selected text object into a variable

## Installation

1. Copy `TraduzAI.jsx` into Illustrator's Scripts folder:
   `Presets/[language]/Scripts/`
2. Restart Illustrator (or reopen the **File > Scripts** menu) so it shows
   up in the list.

## Usage

1. In Illustrator, create an Action that converts the selected text into a
   variable (Window > Actions, record: Window > Variables > "Make Text
   Dynamic").
2. Select the text objects in the document and run
   **File > Scripts > TraduzAI**.
3. In the UI, enter the Action name, the Action set, and the variable
   prefix, click **START**, and watch the progress bar.
4. When it finishes, export the CSV with the collected text.

```
$ File > Scripts > TraduzAI
> Action name: setvar
> Set: Default Actions
> Prefix: Variable
> START
Processing 40 of 40...
Done! Action 'setvar' ran on 40 objects.
Export a CSV with the variable data? [Yes]
CSV file exported successfully!
```

There are no command-line flags — everything is configured through the
ScriptUI interface (Action name, Action set, and variable prefix — see
`ACTION_NAME`, `ACTION_SET` and `VARIABLE_PREFIX` at the top of
`TraduzAI.jsx`).

## How it works

The script uses `ScriptUI` for the interface and processes the selected
objects in batches of at most 2 at a time (`Math.min(batchSize, 2)`, line
192 of `TraduzAI.jsx` — hardcoded, not exposed in the UI, deliberately low
to keep weaker machines from freezing), running the given Action on each
one through `app.doScript`. Above 50 selected objects the script warns
before continuing, and above 100 it asks for an extra confirmation. Every
result is collected and, at the end (or via the "Export existing CSV"
button, which scans the variables already created in the document), written
to a UTF-8 `.csv` through `File.saveDialog`.

## Structure

```
TraduzAI.jsx           # the script: UI, batch processing, CSV export
LANGUAGE-CONFIG.md     # Illustrator Action Set names per language
```

## Status

The full flow works: run the Action in batches, export CSV, re-import the
translation as a variable. It depends on the Action already existing in
Illustrator before the script runs — the script cannot create the Action
itself.

## License

MIT.
