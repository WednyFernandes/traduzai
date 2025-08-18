# Tradutor CSV 🌐

Script Python para tradução e localização de textos em arquivos CSV, mantendo formatação, pontuação, aspas e oferecendo opções avançadas para tratamento de valores monetários.

## 🎯 Comportamento do Arquivo Final

O script cria um arquivo CSV com a seguinte estrutura:
- **Linha 1**: Cabeçalho original (preservado)
- **Linha 2**: Dados originais em português (preservado)  
- **Linha 3**: Tradução dos dados da linha 2 no idioma solicitado

### Exemplo de Resultado:
```csv
"Variável1","Variável2","Variável3","Variável4"
"STROGONOFF DE FILÉ MIGNON","Sabor sofisticado","82,00","Pratos"
"FILET MIGNON STROGANOFF","Sophisticated flavor","$82,00","Dishes"
```

## 🚀 Características

- ✅ **Tradução automática** usando Google Translate
- ✅ **Preserva estrutura original** (cabeçalho + dados originais + traduções)
- ✅ **Preserva formatação** (aspas, pontuação, quebras de linha)
- ✅ **Preserva caixa alta** (texto em MAIÚSCULAS mantém formatação)
- ✅ **Funciona com alemão** e outros idiomas europeus
- ✅ **Opções de moeda** (conversão ou apenas troca de símbolo)
- ✅ **Preserva elementos** (números, URLs, emails)
- ✅ **Cache de tradução** para eficiência
- ✅ **Configuração flexível** via JSON ou linha de comando
- ✅ **Suporte a múltiplos idiomas**

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Conexão com a internet (para tradução)

## 🔧 Instalação

### Método 1: Instalação automática (Windows)
```bash
# Execute o arquivo de instalação
instalar.bat
```

### Método 2: Instalação manual
```bash
# Instalar dependências
pip install googletrans==4.0.0rc1
```

## 🎯 Uso Básico

### Tradução simples
```bash
# Traduzir do português para inglês
python tradutor_csv.py seu_arquivo.csv
```

### Especificar idiomas e arquivo de saída
```bash
python tradutor_csv.py cardapio.csv -s pt -t en -o menu_english.csv
```

### Traduzir para espanhol
```bash
python tradutor_csv.py cardapio.csv -s pt -t es -o menu_espanol.csv
```

## 💰 Opções de Moeda

### Apenas trocar símbolo da moeda
```bash
python tradutor_csv.py cardapio.csv -t en --currency-symbol "$"
# R$ 82,00 → $ 82,00
```

### Converter valores com taxa de câmbio
```bash
python tradutor_csv.py cardapio.csv -t en --convert-currency --rate 5.5 --currency-symbol "$"
# R$ 82,00 → $ 451.00
```

### Manter valores originais
```bash
python tradutor_csv.py cardapio.csv -t en --preserve-numbers
# Mantém todos os números sem alteração
```

## ⚙️ Configuração Avançada

### Criar arquivo de configuração
```bash
python tradutor_csv.py --create-config
```

### Usar arquivo de configuração
```bash
python tradutor_csv.py cardapio.csv --config minha_config.json
```

### Exemplo de configuração (config.json):
```json
{
  "source_language": "pt",
  "target_language": "en",
  "currency_symbol": "$",
  "convert_currency": false,
  "currency_conversion_rate": 5.5,
  "preserve_numbers": true,
  "preserve_urls": true,
  "preserve_emails": true,
  "max_retries": 3
}
```

## 🌍 Idiomas Suportados

| Código | Idioma |
|--------|--------|
| `pt` | Português |
| `en` | Inglês |
| `es` | Espanhol |
| `fr` | Francês |
| `de` | Alemão |
| `it` | Italiano |
| `ja` | Japonês |
| `zh` | Chinês |
| `ko` | Coreano |
| `ru` | Russo |
| `ar` | Árabe |
| `hi` | Hindi |

## 📊 Exemplos Práticos

### Exemplo 1: Cardápio de Restaurante
```bash
# Traduzir cardápio para inglês mantendo preços em reais
python tradutor_csv.py cardapio.csv -t en --currency-symbol "R$"

# Traduzir para inglês convertendo preços para dólares
python tradutor_csv.py cardapio.csv -t en --convert-currency --rate 5.2 --currency-symbol "$"
```

### Exemplo 2: Lista de Produtos
```bash
# Traduzir preservando códigos de produto e URLs
python tradutor_csv.py produtos.csv -s pt -t es --preserve-numbers --preserve-urls
```

### Exemplo 3: Usando configuração personalizada
```bash
# Criar configuração específica
python tradutor_csv.py --create-config
# Editar config.json conforme necessário
python tradutor_csv.py dados.csv --config config.json
```

## 🛠️ Opções de Linha de Comando

```
python tradutor_csv.py [arquivo] [opções]

Argumentos:
  arquivo                    Arquivo CSV de entrada

Opções:
  -h, --help                Mostra esta ajuda
  -o, --output ARQUIVO      Arquivo de saída
  -s, --source IDIOMA       Idioma de origem (padrão: pt)
  -t, --target IDIOMA       Idioma de destino (padrão: en)
  --currency-symbol SÍMBOLO Símbolo da moeda (padrão: $)
  --convert-currency        Converter valores monetários
  --rate TAXA               Taxa de conversão
  --preserve-numbers        Preservar números
  --config ARQUIVO          Arquivo de configuração
  --create-config           Criar arquivo de configuração
```

## 🔍 Como Funciona

1. **Leitura**: O script lê o arquivo CSV preservando a estrutura original
2. **Preservação**: Identifica e preserva elementos especiais (números, URLs, emails)
3. **Tradução**: Traduz cada célula usando Google Translate
4. **Restauração**: Restaura elementos preservados no texto traduzido
5. **Conversão**: Aplica conversões de moeda se configurado
6. **Saída**: Salva o arquivo traduzido mantendo a formatação

## 🧪 Exemplo de Resultado

**Entrada (português):**
```csv
"Prato","Descrição","Preço"
"STROGONOFF DE FILÉ MIGNON","Sabor sofisticado. Cubos de filé, cremosidade aveludada.","82,00"
```

**Saída (inglês):**
```csv
"Dish","Description","Price"
"FILET MIGNON STROGANOFF","Sophisticated flavor. Filet cubes, velvety creaminess.","$82.00"
```

## ⚠️ Limitações

- Requer conexão com internet para tradução
- API do Google Translate pode ter limites de uso
- Traduções automáticas podem precisar de revisão manual
- Alguns termos específicos podem não traduzir corretamente

## 🐛 Solução de Problemas

### Erro de instalação
```bash
# Tente instalar como administrador ou usar:
pip install --user googletrans==4.0.0rc1
```

### Erro de conexão
- Verifique sua conexão com internet
- Alguns firewalls podem bloquear o Google Translate

### Tradução não funciona
- Verifique se os códigos de idioma estão corretos
- Tente reduzir o tamanho do arquivo CSV

## 📝 Licença

Este script é fornecido como está, para uso educacional e comercial.

## 🤝 Contribuição

Sugestões e melhorias são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Contribuir com código

---

**Desenvolvido com ❤️ para facilitar traduções de CSV mantendo qualidade e formatação.**
