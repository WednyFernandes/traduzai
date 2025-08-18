# TraduzAI CSV - Interface Gráfica 🌐

Interface gráfica moderna para tradução automatizada de arquivos CSV usando Google Translate.

## 🎯 Recursos

- ✅ **Interface Gráfica Intuitiva** - Fácil de usar, sem linha de comando
- ✅ **Seleção de Arquivos** - Navegue e selecione arquivos CSV facilmente
- ✅ **Múltiplos Idiomas** - Suporte a todos os idiomas do Google Translate
- ✅ **Preservação de Formatação** - Mantém números, URLs, emails e formatação
- ✅ **Configurações Avançadas** - Controle total sobre o processo de tradução
- ✅ **Progresso em Tempo Real** - Acompanhe o progresso da tradução
- ✅ **Log Detalhado** - Veja cada tradução sendo processada
- ✅ **Executável Standalone** - Não requer Python instalado

## 🖥️ Interface

A interface possui as seguintes seções:

### 📁 Seleção de Arquivos
- **Arquivo CSV**: Selecione o arquivo a ser traduzido
- **Arquivo de Saída**: Escolha onde salvar o resultado

### 🌍 Configurações de Idioma
- **Idioma Origem**: Idioma do texto original
- **Idioma Destino**: Idioma para tradução

### ⚙️ Configurações Avançadas
- **Preservar números**: Mantém valores numéricos inalterados
- **Preservar URLs**: Mantém links intactos
- **Preservar emails**: Mantém endereços de email inalterados
- **Converter moeda**: Opção para converter valores monetários
- **Símbolo de moeda**: Defina o símbolo da moeda de destino
- **Taxa de conversão**: Taxa para conversão monetária

### 📊 Monitoramento
- **Barra de Progresso**: Acompanhe o progresso da tradução
- **Status**: Veja o status atual do processo
- **Log**: Histórico detalhado de cada tradução

## 🚀 Como Usar

### Método 1: Interface Gráfica (Recomendado)

1. **Execute a interface**:
   ```bash
   python tradutor_csv_gui.py
   ```

2. **Selecione o arquivo CSV** clicando em "Selecionar"

3. **Configure os idiomas**:
   - Escolha o idioma de origem (ex: "pt - Portuguese")
   - Escolha o idioma de destino (ex: "en - English")

4. **Ajuste configurações avançadas** se necessário

5. **Clique em "Iniciar Tradução"**

6. **Acompanhe o progresso** na barra e no log

### Método 2: Executável Standalone

1. **Gere o executável**:
   ```bash
   # Windows
   criar_executavel.bat
   
   # Ou manualmente
   python criar_executavel.py
   ```

2. **Execute o TraduzAI-CSV.exe** da pasta `dist`

3. **Use normalmente** como descrito acima

## 📋 Requisitos

### Para usar o código Python:
```bash
# Instalar dependências
pip install -r requirements.txt

# Ou individualmente
pip install googletrans==4.0.0rc1
pip install pyinstaller  # Para criar executável
```

### Para usar o executável:
- ✅ Windows 7/8/10/11
- ✅ Conexão com internet
- ❌ Não requer Python instalado

## 🔧 Configurações Avançadas

### Preservação de Elementos

A interface permite preservar diferentes tipos de conteúdo:

- **Números**: `123`, `45.67`, `1,234.56`
- **URLs**: `https://example.com`, `www.site.com`
- **Emails**: `user@domain.com`

### Conversão de Moeda

Quando ativada, converte valores monetários:
- **De**: `R$ 100,00` ou `100 reais`
- **Para**: `$100.00` (com taxa configurada)

### Preservação de Formatação

- **Maiúsculas**: `TEXTO` → `TEXT`
- **Minúsculas**: `texto` → `text`
- **Título**: `Texto` → `Text`
- **Mista**: `TeXtO` → `TeXt` (mantém padrão original)

## 📊 Formato de Saída

O arquivo CSV de saída mantém a estrutura original:

```csv
"Variável1","Variável2","Variável3"
"Texto original 1","Texto original 2","Texto original 3"
"Translated text 1","Translated text 2","Translated text 3"
```

## 🎨 Capturas de Tela

### Interface Principal
```
┌─────────────────────────────────────────────────┐
│              TraduzAI CSV - Tradutor            │
├─────────────────────────────────────────────────┤
│ Arquivo CSV: [________________] [Selecionar]    │
│                                                 │
│ ┌─── Configurações de Idioma ─────────────────┐ │
│ │ Origem: [pt - Portuguese] ▼                 │ │
│ │ Destino: [en - English] ▼                   │ │
│ └─────────────────────────────────────────────┘ │
│                                                 │
│ ┌─── Configurações Avançadas ─────────────────┐ │
│ │ ☑ Preservar números  ☑ URLs  ☑ Emails     │ │
│ │ ☐ Converter moeda Símbolo: [$] Taxa: [1.0] │ │
│ └─────────────────────────────────────────────┘ │
│                                                 │
│ Saída: [arquivo_traduzido.csv] [Selecionar]    │
│                                                 │
│ [████████████████████████████] 100%            │
│ Status: Tradução concluída!                    │
│                                                 │
│ [Iniciar Tradução] [Limpar] [Sair]             │
│                                                 │
│ ┌─── Log de Tradução ─────────────────────────┐ │
│ │ [12:34:56] Iniciando tradução...            │ │
│ │ [12:34:57] Campo 1: "Olá" → "Hello"        │ │
│ │ [12:34:58] Arquivo salvo com sucesso        │ │
│ └─────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────┘
```

## ⚠️ Limitações

- **Limite do Google Translate**: Pode ter limitações de uso por IP
- **Conexão Internet**: Requer conexão estável
- **Qualidade**: Tradução automática pode não ser perfeita
- **Performance**: Arquivos muito grandes podem ser lentos

## 🛠️ Desenvolvimento

### Estrutura do Código

```python
CSVTranslatorGUI/
├── __init__()          # Inicialização da interface
├── setup_ui()          # Configuração da interface
├── select_file()       # Seleção de arquivos
├── validate_inputs()   # Validação de entradas
├── start_translation() # Início da tradução
├── translate_csv()     # Lógica principal de tradução
├── translate_text()    # Tradução de texto individual
└── utility methods...  # Métodos auxiliares
```

### Personalizações

Para personalizar a interface, edite o arquivo `tradutor_csv_gui.py`:

```python
# Mudar idiomas padrão
self.source_lang = tk.StringVar(value='pt')
self.target_lang = tk.StringVar(value='en')

# Mudar configurações padrão
self.preserve_numbers = tk.BooleanVar(value=True)
self.convert_currency = tk.BooleanVar(value=False)

# Mudar aparência
self.root.geometry("800x600")  # Tamanho da janela
style.theme_use('clam')        # Tema da interface
```

## 🤝 Contribuições

Contribuições são bem-vindas! Áreas para melhoria:

- 🎨 **Interface**: Melhorias visuais e UX
- 🌐 **Idiomas**: Suporte a mais serviços de tradução
- ⚡ **Performance**: Otimizações para arquivos grandes
- 🔧 **Recursos**: Novas funcionalidades

## 📄 Licença

Este projeto é distribuído sob licença MIT. Veja `LICENSE` para mais informações.

---

**Criado por [Wedny Fernandes](https://wednyfernandes.com.br)**
