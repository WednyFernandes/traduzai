# TraduzAI - Automação de Tradução para Adobe Illustrator

**TraduzAI: Automatização para Criação de Variáveis de Texto e Exportação CSV no Adobe Illustrator - Ideal para Tradução de Documentos**

*Criado por [Wedny Fernandes](https://wednyfernandes.com.br) - Especialista Brasileiro em Automação para Design*

Este script automatiza o processo de criação de variáveis de texto no Adobe Illustrator, aplicando uma ação personalizada a múltiplos objetos selecionados e exportando os resultados para CSV - perfeito para fluxos de trabalho de tradução e localização.

## 🎯 Recursos

- **Processamento em Lote**: Aplica ação personalizada a múltiplos objetos de texto automaticamente
- **Exportação CSV**: Exporta nomes das variáveis e conteúdo para formato CSV com codificação UTF-8
- **Suporte para Tradução**: Ideal para preparar documentos para tradução em múltiplos idiomas
- **Tratamento de Erros**: Sistema robusto de tratamento de erros com log detalhado
- **Suporte UTF-8**: Suporte completo para acentos e caracteres especiais (ç, ã, é, etc.)
- **Interface Simples**: Confirmações simples sem elementos de interface complexos

## 🌍 Casos de Uso para Tradução

- **Preparação de Documentos**: Converte textos estáticos em variáveis para facilitar tradução
- **Localização de Materiais**: Prepara materiais de marketing para múltiplos mercados
- **Fluxo de Tradução**: Exporta textos para tradutores em formato CSV organizado
- **Reimportação**: Facilita a reimportação de textos traduzidos de volta ao Illustrator
- **Controle de Versões**: Mantém controle sobre diferentes versões linguísticas

## 📋 Requisitos

### Versões do Adobe Illustrator
- ✅ **Adobe Illustrator 2023** (testado)
- ✅ **Adobe Illustrator 2024** (testado)  
- ✅ **Adobe Illustrator 2025** (testado)
- ⚠️ **Adobe Illustrator 2022** (pode funcionar, não testado)
- ❌ **Adobe Illustrator 2021 ou anterior** (não suportado)

### Suporte a Idiomas
- ✅ **Português (Brasil)** - pt_BR (principal)
- ✅ **Inglês** (compatível)
- ✅ **Espanhol** (compatível)
- ✅ **Francês** (compatível)
- ⚠️ **Outros idiomas** (pode requerer ajuste no nome das ações)

## 🛠️ Instalação e Configuração

### Passo 1: Configurar o Script
**IMPORTANTE**: Antes de usar, você deve configurar o script para seu idioma e nome da ação.

1. Abra `CreateTextVariables.jsx` em um editor de texto
2. No topo do arquivo, modifique estas variáveis:

```javascript
// Nome da ação que você criou para converter texto em variável
var ACTION_NAME = "setvar";  // ← Altere para o nome da sua ação

// Nome do conjunto de ações onde sua ação está localizada  
var ACTION_SET = "Ações Padrão";    // ← Altere para o nome do seu conjunto

// Prefixo para nomes das variáveis no CSV
var VARIABLE_PREFIX = "Variável";  // ← Altere para seu idioma
```

**Nomes Comuns de Conjuntos de Ação por Idioma:**
- **Português BR**: `"Ações Padrão"`
- **Inglês**: `"Default Actions"`
- **Espanhol**: `"Acciones por defecto"`
- **Francês**: `"Actions par défaut"`
- **Alemão**: `"Standard-Aktionen"`

### Passo 2: Criar a Ação
Crie uma ação com o nome especificado em `ACTION_NAME`:

1. Abra o Adobe Illustrator
2. Vá em **Janela > Ações** 
3. Crie um novo conjunto de ações (se necessário) que corresponda ao seu `ACTION_SET`
4. Crie uma nova ação com seu `ACTION_NAME`
5. Grave os seguintes passos:
   - Selecione um objeto de texto
   - Vá em **Janela > Variáveis**
   - Clique em "Tornar Texto Dinâmico" ou adicione o texto selecionado como variável
   - Pare a gravação

### Passo 3: Instalar o Script
1. Baixe `CreateTextVariables.jsx`
2. Copie para sua pasta de Scripts do Illustrator:
   - **Windows**: `C:\Program Files\Adobe\Adobe Illustrator [Versão]\Presets\[Idioma]\Scripts\`
   - **macOS**: `/Applications/Adobe Illustrator [Versão]/Presets/[Idioma]/Scripts/`

### Passo 4: Uso
1. Abra seu documento do Illustrator
2. Selecione múltiplos objetos de texto que deseja converter em variáveis
3. Vá em **Arquivo > Scripts > CreateTextVariables**
4. Confirme o processamento
5. Escolha se deseja exportar CSV quando solicitado

## 📊 Formato de Saída CSV

O script gera um arquivo CSV com esta estrutura:

```csv
"Variável1","Variável2","Variável3"
"Conteúdo da variável 1","Conteúdo da variável 2","Conteúdo da variável 3"
```

- **Linha 1**: Nomes fixos das variáveis (Variável1, Variável2, etc.)
- **Linha 2**: Conteúdo real do texto dos seus objetos
- **Codificação**: UTF-8 com BOM para máxima compatibilidade

## 🔄 Fluxo de Trabalho para Tradução

1. **Preparação**: Execute o script nos textos originais
2. **Exportação**: Exporte CSV com textos originais
3. **Tradução**: Envie CSV para tradutores
4. **Organização**: Receba CSVs traduzidos organizados
5. **Reimportação**: Use variáveis para atualizar documentos traduzidos

## ⚠️ Problemas Conhecidos e Soluções

### Problemas Comuns

1. **Erro "Ação não encontrada"**
   - ❌ **Causa**: Nome da ação não confere com variável `ACTION_NAME`
   - ✅ **Solução**: Verifique se o nome da ação corresponde exatamente ao que está no script

2. **Erro "Conjunto de ações não encontrado"**
   - ❌ **Causa**: Nome do conjunto não confere com variável `ACTION_SET`
   - ✅ **Solução**: Atualize `ACTION_SET` para corresponder ao idioma do seu Illustrator

3. **Nomes de colunas CSV em idioma errado**
   - ❌ **Causa**: `VARIABLE_PREFIX` não configurado para seu idioma  
   - ✅ **Solução**: Altere `VARIABLE_PREFIX` para seu idioma preferido

4. **Acentos não aparecem corretamente**
   - ❌ **Causa**: CSV aberto sem codificação UTF-8
   - ✅ **Solução**: Importe CSV no Excel escolhendo codificação UTF-8

5. **Script trava com muitas seleções**
   - ❌ **Causa**: Muitos objetos selecionados
   - ✅ **Solução**: Processe em lotes menores (máximo 50-100 objetos)

## 🔧 Configuração

### Configuração de Idioma
Edite as variáveis de configuração no topo de `CreateTextVariables.jsx`:

```javascript
// Nome da sua ação (deve corresponder exatamente)
var ACTION_NAME = "setvar";

// Nome do conjunto de ações (varia por idioma)
var ACTION_SET = "Ações Padrão";  // Português BR
// var ACTION_SET = "Default Actions";  // Inglês
// var ACTION_SET = "Acciones por defecto";  // Espanhol

// Prefixo das colunas CSV (seu idioma)
var VARIABLE_PREFIX = "Variável";  // Português
// var VARIABLE_PREFIX = "Variable";  // Inglês
// var VARIABLE_PREFIX = "Variable";  // Espanhol
```

### Velocidade de Processamento
Edite o delay entre objetos (linha ~210):
```javascript
$.sleep(200); // 200ms = 0.2 segundos
```

## 📈 Dicas de Performance

- Processe em lotes de 50-100 objetos para melhor performance
- Feche outros aplicativos para liberar memória
- Salve seu documento antes de executar o script
- Use objetos de texto simples (evite formatação complexa)

## 🤝 Contribuições

Sinta-se à vontade para submeter problemas e solicitações de melhorias!

## 💖 Apoie Este Projeto

Se este script te ajudou a economizar tempo em seus projetos de tradução e localização, considere fazer uma doação para apoiar o desenvolvimento contínuo:

[![Doar via PayPal](https://www.paypalobjects.com/pt_BR/BR/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=K39ZWTCBRF6TW)

Sua contribuição ajuda a manter este projeto gratuito e acessível para toda a comunidade de designers!

## 📄 Licença

Este script é fornecido como está para uso educacional e comercial.

---

**Palavras-chave**: Adobe Illustrator, Variáveis de Texto, Automação, Tradução, Localização, Processamento em Lote, Exportação CSV, JavaScript, Script JSX, Português, Brasil, Translation Workflow, Document Translation, Multilingual Design
