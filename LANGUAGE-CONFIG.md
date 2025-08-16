# Language Configuration Guide

## Common Action Set Names by Language

### Portuguese (Brazil)
```javascript
var ACTION_SET = "Ações Padrão";
var VARIABLE_PREFIX = "Variável";
```

### English (US/UK)
```javascript
var ACTION_SET = "Default Actions";
var VARIABLE_PREFIX = "Variable";
```

### Spanish
```javascript
var ACTION_SET = "Acciones por defecto";
var VARIABLE_PREFIX = "Variable";
```

### French
```javascript
var ACTION_SET = "Actions par défaut";
var VARIABLE_PREFIX = "Variable";
```

### German
```javascript
var ACTION_SET = "Standard-Aktionen";
var VARIABLE_PREFIX = "Variable";
```

### Italian
```javascript
var ACTION_SET = "Azioni predefinite";
var VARIABLE_PREFIX = "Variabile";
```

### Japanese
```javascript
var ACTION_SET = "初期設定アクション";
var VARIABLE_PREFIX = "変数";
```

### Korean
```javascript
var ACTION_SET = "기본 동작";
var VARIABLE_PREFIX = "변수";
```

### Chinese (Simplified)
```javascript
var ACTION_SET = "默认动作";
var VARIABLE_PREFIX = "变量";
```

### Chinese (Traditional)
```javascript
var ACTION_SET = "預設動作";
var VARIABLE_PREFIX = "變數";
```

### Dutch
```javascript
var ACTION_SET = "Standaardacties";
var VARIABLE_PREFIX = "Variabele";
```

### Russian
```javascript
var ACTION_SET = "Действия по умолчанию";
var VARIABLE_PREFIX = "Переменная";
```

## How to Find Your Action Set Name

1. Open Adobe Illustrator
2. Go to Window > Actions
3. Look at the default action set name in your language
4. Use that exact name in the ACTION_SET variable

## Translation Workflow Tips

### For Translation Agencies
- Use consistent VARIABLE_PREFIX across all projects
- Create standard action names for all translators
- Document your configuration for team consistency

### For Freelance Designers
- Keep a configuration file for each client's language preferences
- Use descriptive action names like "make-translatable" instead of "setvar"
- Save different script versions for different language workflows

### For Design Studios
- Standardize action names across all workstations
- Create a style guide for variable naming conventions
- Train team members on consistent script configuration
