# TraduzAI - Adobe Illustrator Translation Automation

**TraduzAI: Modern Interface for Automated Text Variables Creation and CSV Export - Perfect for Document Translation Workflows**

*Created by [Wedny Fernandes](https://wednyfernandes.com.br) - Brazilian Graphic Designer and Developer*

This script provides a modern graphical interface for automating the process of creating text variables in Adobe Illustrator. With real-time progress tracking, batch processing, and customizable settings, it's the perfect tool for translation and localization workflows.

> **Tested only on Adobe Illustrator 2025.**

## 🎨 Modern Interface Features

- **🖥️ Intuitive GUI**: Professional ScriptUI interface with real-time feedback
- **📊 Progress Tracking**: Live progress bar showing processing status
- **⏸️ Cancellation Control**: Stop processing at any time with cancel button
- **💾 Automatic Backup**: Optional backup creation before processing
- **⚙️ Live Configuration**: Edit action names and settings directly in the interface
- **🎯 Batch Processing**: Processes objects in optimized batches of 10
- **🔄 Smart Delays**: Optimized timing between batches for better performance

## 🌍 Perfect for Translation & Localization

- **Document Preparation**: Convert static texts to variables for easy translation
- **Material Localization**: Prepare marketing materials for multiple markets  
- **Translation Workflow**: Export texts to CSV format for translators
- **Reimport Process**: Easily reimport translated texts back to Illustrator
- **Version Control**: Maintain control over different language versions
- **Multilingual Projects**: Streamline creation of multilingual design materials

## 🎯 Core Features

- **Modern Interface**: Clean, professional ScriptUI with progress tracking
- **Batch Processing**: Processes text objects in optimized batches for better performance
- **CSV Export**: Export variable names and content to CSV format with proper UTF-8 encoding
- **Translation Ready**: Ideal for preparing documents for translation into multiple languages
- **Error Handling**: Robust error handling with detailed logging and recovery
- **UTF-8 Support**: Full support for accents and special characters (ç, ã, é, ñ, ü, etc.)
- **Automatic Backup**: Optional automatic backup before processing
- **Live Configuration**: Edit settings without modifying script code
- **Cancellation Support**: Stop processing at any time
- **Performance Optimized**: Smart delays and batch processing for low-end computers

## 📋 Requirements

### Adobe Illustrator Versions
- ✅ **Adobe Illustrator 2025** (tested)
- ⚠️ **Adobe Illustrator 2024** (may work, not tested)
- ⚠️ **Adobe Illustrator 2023** (may work, not tested)
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

### Step 1: Create the Action
Create an action with your desired name:

1. Open Adobe Illustrator
2. Go to **Window > Actions** 
3. Create a new action set (if needed)
4. Create a new action (e.g., "setvar")
5. Record the following steps:
   - Select a text object
   - Go to **Window > Variables**
   - Click "Make Text Dynamic" or add the selected text as a variable
   - Stop recording

### Step 2: Install the Script
1. Download `TraduzAI.jsx`
2. Copy to your Illustrator Scripts folder:
   - **Windows**: `C:\Program Files\Adobe\Adobe Illustrator [Version]\Presets\[Language]\Scripts\`
   - **macOS**: `/Applications/Adobe Illustrator [Version]/Presets/[Language]/Scripts/`

### Step 3: Usage with Modern Interface
1. Open your Illustrator document
2. **Ungroup objects** if necessary - text objects work best when ungrouped for individual processing
3. Select multiple text objects you want to convert to variables
3. Go to **File > Scripts > TraduzAI**
4. **Configure settings** in the interface:
   - **Action Name**: Enter your action name (e.g., "setvar")
   - **Action Set**: Enter your action set name (varies by language)
   - **Variable Prefix**: Choose your CSV column prefix (e.g., "Variable")
   - **Backup Toggle**: Enable/disable automatic backup
5. Click **START** to begin processing
6. Monitor progress in real-time
7. Use **Cancel** button if needed to stop processing
8. Choose CSV export when processing completes

### Step 4: Translation Workflow

#### Method 1: Using Google Sheets (Recommended)
1. **Export CSV**: Export your processed variables to CSV format
2. **Open in Google Sheets**: Import the CSV file into Google Sheets
3. **Add translation rows**: Create new rows below the original content for each target language
4. **Use Google Translate**: Utilize Google Sheets' built-in Google Translate function for each target language column
5. **Handle line breaks**: After translation, replace all `\n` characters with `^n` in the translated content (this is required for Illustrator compatibility)
   - You can do this in Google Sheets using Find & Replace: Find `\n` and replace with `^n`
   - Alternatively, use Illustrator's Find & Replace feature after importing
6. **Export translated CSV**: Download the completed CSV with all language versions

#### Method 2: Using AI Translation
1. **Export CSV**: Export your processed variables to CSV format  
2. **Translate with AI**: Use an AI service (e.g., ChatGPT) to translate and localize the CSV for your target language, keeping the CSV line formatting. Example prompt:

   > Translate and localize the following CSV content to [target language], keeping the CSV line formatting exactly as provided. Replace any \n line breaks with ^n for Illustrator compatibility.

#### Final Steps
3. **Load variable library**: Load the translated CSV as your variable library and select the desired dataset for your document
4. **Apply translations**: Use Illustrator's variables panel to apply translations

## 📊 CSV Output Format

The script generates a CSV file with this structure:

> **Tip:** Each new translation should be added as a new line below the original, keeping the column headers. This way, each language version stays organized and easy to locate.

```csv
"Variável1","Variável2","Variável3"
"Content of variable 1","Content of variable 2","Content of variable 3"
"Translation 1","Translation 2","Translation 3"
"Traducción 1","Traducción 2","Traducción 3"
```


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

5. **Line breaks not working in Illustrator**
   - ❌ **Cause**: Standard `\n` line breaks don't work in Illustrator variables
   - ✅ **Solution**: Replace `\n` with `^n` in your translated content. Use Find & Replace in Google Sheets or Illustrator

6. **Script freezes on large selections**
   - ❌ **Cause**: Too many objects selected
   - ✅ **Solution**: Process in smaller batches (50-100 objects max)

### Compatibility Issues

- **Illustrator 2021 or older**: May not support some script functions
- **Non-Roman alphabets**: May require additional encoding adjustments
- **Very large files**: Performance may degrade with 500+ objects

## 🔧 Configuration

### Language Configuration
Edit the configuration variables at the top of `TraduzAI.jsx`:

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
