# TraduzAI - Adobe Illustrator Translation Automation

**TraduzAI: Automated Text Variables Creation and CSV Export for Adobe Illustrator - Perfect for Document Translation Workflows**

*Created by [Wedny Fernandes](https://wednyfernandes.com.br) - Brazilian Design Automation Specialist*

This script automates the process of creating text variables in Adobe Illustrator by applying a custom action to multiple selected objects and optionally exporting the results to a CSV file - ideal for translation and localization workflows.

## 🌍 Perfect for Translation & Localization

- **Document Preparation**: Convert static texts to variables for easy translation
- **Material Localization**: Prepare marketing materials for multiple markets  
- **Translation Workflow**: Export texts to CSV format for translators
- **Reimport Process**: Easily reimport translated texts back to Illustrator
- **Version Control**: Maintain control over different language versions
- **Batch Processing**: Handle multiple documents efficiently
- **Multilingual Projects**: Streamline creation of multilingual design materials

## 🎯 Features

- **Batch Processing**: Apply custom action to multiple selected text objects automatically
- **CSV Export**: Export variable names and content to CSV format with proper UTF-8 encoding
- **Translation Ready**: Ideal for preparing documents for translation into multiple languages
- **Error Handling**: Robust error handling with detailed logging
- **UTF-8 Support**: Full support for accents and special characters (ç, ã, é, ñ, ü, etc.)
- **Clean Interface**: Simple confirmation dialogs without complex UI elements
- **Customizable**: Easy configuration for different languages and workflows

## 📋 Requirements

### Adobe Illustrator Versions
- ✅ **Adobe Illustrator 2023** (tested)
- ✅ **Adobe Illustrator 2024** (tested)  
- ✅ **Adobe Illustrator 2025** (tested)
- ⚠️ **Adobe Illustrator 2022** (may work, not tested)
- ❌ **Adobe Illustrator 2021 or older** (not supported)

### Language Support
- ✅ **Portuguese (Brazil)** - pt_BR (primary)
- ✅ **English** (compatible)
- ✅ **Spanish** (compatible)  
- ✅ **French** (compatible)
- ✅ **German** (compatible)
- ⚠️ **Other languages** (may require action name adjustment)

## 🔄 Translation Workflow

1. **Preparation**: Run script on original language texts
2. **Export**: Export CSV with original texts  
3. **Translation**: Send CSV to translators
4. **Organization**: Receive organized translated CSVs
5. **Reimport**: Use variables to update translated documents

## 🛠️ Installation & Setup

### Step 1: Configure the Script
**IMPORTANT**: Before using, you must configure the script for your language and action name.

1. Open `CreateTextVariables.jsx` in a text editor
2. At the top of the file, modify these variables:

```javascript
// Nome da ação que você criou para converter texto em variável
var ACTION_NAME = "setvar";  // ← Change to your action name

// Nome do conjunto de ações onde sua ação está localizada  
var ACTION_SET = "Set 1";    // ← Change to your action set name

// Prefixo para nomes das variáveis no CSV
var VARIABLE_PREFIX = "Variável";  // ← Change to your language
```

**Common Action Set Names by Language:**
- **Portuguese BR**: `"Ações Padrão"`
- **English**: `"Default Actions"`
- **Spanish**: `"Acciones por defecto"`
- **French**: `"Actions par défaut"`
- **German**: `"Standard-Aktionen"`

### Step 2: Create the Action
Create an action with the name you specified in `ACTION_NAME`:

1. Open Adobe Illustrator
2. Go to **Window > Actions** 
3. Create a new action set (if needed) matching your `ACTION_SET`
4. Create a new action with your `ACTION_NAME`
5. Record the following steps:
   - Select a text object
   - Go to **Window > Variables**
   - Click "Make Text Dynamic" or add the selected text as a variable
   - Stop recording

### Step 3: Install the Script
1. Download `CreateTextVariables.jsx`
2. Copy to your Illustrator Scripts folder:
   - **Windows**: `C:\Program Files\Adobe\Adobe Illustrator [Version]\Presets\[Language]\Scripts\`
   - **macOS**: `/Applications/Adobe Illustrator [Version]/Presets/[Language]/Scripts/`

### Step 4: Usage
1. Open your Illustrator document
2. Select multiple text objects you want to convert to variables
3. Go to **File > Scripts > CreateTextVariables**
4. Confirm the processing
5. Choose whether to export CSV when prompted

## 📊 CSV Output Format

The script generates a CSV file with this structure:

```csv
"Variável1","Variável2","Variável3"
"Content of variable 1","Content of variable 2","Content of variable 3"
```

- **Line 1**: Fixed variable names (Variável1, Variável2, etc.)
- **Line 2**: Actual text content from your objects
- **Encoding**: UTF-8 with BOM for maximum compatibility

## ⚠️ Known Issues & Troubleshooting

### Common Problems

1. **"Action not found" error**
   - ❌ **Cause**: Action name doesn't match `ACTION_NAME` variable
   - ✅ **Solution**: Check that your action name matches exactly what's in the script

2. **"Action Set not found" error**
   - ❌ **Cause**: Action set name doesn't match `ACTION_SET` variable
   - ✅ **Solution**: Update `ACTION_SET` to match your Illustrator language

3. **CSV column names in wrong language**
   - ❌ **Cause**: `VARIABLE_PREFIX` not configured for your language  
   - ✅ **Solution**: Change `VARIABLE_PREFIX` to your preferred language

4. **Accents not displaying correctly**
   - ❌ **Cause**: CSV opened without UTF-8 encoding
   - ✅ **Solution**: Import CSV in Excel choosing UTF-8 encoding

5. **Script freezes on large selections**
   - ❌ **Cause**: Too many objects selected
   - ✅ **Solution**: Process in smaller batches (50-100 objects max)

### Compatibility Issues

- **Illustrator 2021 or older**: May not support some script functions
- **Non-Roman alphabets**: May require additional encoding adjustments
- **Very large files**: Performance may degrade with 500+ objects

## 🔧 Configuration

### Language Configuration
Edit the configuration variables at the top of `CreateTextVariables.jsx`:

```javascript
// Your action name (must match exactly)
var ACTION_NAME = "setvar";

// Your action set name (varies by language)
var ACTION_SET = "Ações Padrão";  // Portuguese BR
// var ACTION_SET = "Default Actions";  // English
// var ACTION_SET = "Acciones por defecto";  // Spanish

// CSV column prefix (your language)
var VARIABLE_PREFIX = "Variável";  // Portuguese
// var VARIABLE_PREFIX = "Variable";  // English
// var VARIABLE_PREFIX = "Variable";  // Spanish
```

### Processing Speed
Edit the delay between objects (line ~210):
```javascript
$.sleep(200); // 200ms = 0.2 seconds
```

## 📈 Performance Tips

- Process in batches of 50-100 objects for best performance
- Close other applications to free up memory
- Save your document before running the script
- Use simple text objects (avoid complex formatting)

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## � Support This Project

If this script helped you save time on your translation and localization projects, consider making a donation to support continued development:

[![Donate via PayPal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=K39ZWTCBRF6TW)

Your contribution helps keep this project free and accessible to the entire design community!

## 🌐 Language Versions

- 🇺🇸 [English (this file)](README.md)
- 🇧🇷 [Português Brasil](README-ptBR.md)

## �📄 License

This script is provided as-is for educational and commercial use.

---

**Keywords**: Adobe Illustrator, Text Variables, Automation, Translation, Localization, Document Translation, Batch Processing, CSV Export, JavaScript, JSX Script, Multilingual Design, Translation Workflow, Design Automation, Illustrator Scripts, Variable Data, Dynamic Text, Internationalization, i18n, Document Localization
