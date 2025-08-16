# TraduzAI - Automação de Tradução para Adobe Illustrator

**TraduzAI: Interface Moderna para Criação Automatizada de Variáveis de Texto e Exportação CSV - Perfeito para Fluxos de Tradução**

*Criado por [Wedny Fernandes](https://wednyfernandes.com.br) - Designer Gráfico e Desenvolvedor*

Este script oferece uma interface gráfica moderna para automatizar o processo de criação de variáveis de texto no Adobe Illustrator. Com acompanhamento de progresso em tempo real, processamento em lotes e configurações personalizáveis, é a ferramenta perfeita para fluxos de trabalho de tradução e localização.

> **Testado apenas na versão Adobe Illustrator 2025.**

## � Recursos da Interface Moderna

- **🖥️ Interface Intuitiva**: Interface ScriptUI profissional com feedback em tempo real
- **📊 Acompanhamento de Progresso**: Barra de progresso mostrando status em tempo real
- **⏸️ Controle de Cancelamento**: Pare o processamento a qualquer momento
- **💾 Backup Automático**: Criação opcional de backup antes do processamento
- **⚙️ Configuração Dinâmica**: Edite nomes de ações e configurações diretamente na interface
- **🎯 Processamento em Lotes**: Processa objetos em lotes otimizados de 10
- **🔄 Delays Inteligentes**: Timing otimizado entre lotes para melhor performance

## 🌍 Perfeito para Tradução e Localização

- **Preparação de Documentos**: Converte textos estáticos em variáveis para facilitar tradução
- **Localização de Materiais**: Prepara materiais de marketing para múltiplos mercados
- **Fluxo de Tradução**: Exporta textos para tradutores em formato CSV organizado
- **Reimportação**: Facilita a reimportação de textos traduzidos de volta ao Illustrator
- **Controle de Versões**: Mantém controle sobre diferentes versões linguísticas
- **Projetos Multilíngues**: Agiliza a criação de materiais de design multilíngues

## 🎯 Recursos Principais

- **Interface Moderna**: Interface ScriptUI limpa e profissional com acompanhamento de progresso
- **Processamento em Lotes**: Processa objetos de texto em lotes otimizados para melhor performance
- **Exportação CSV**: Exporta nomes das variáveis e conteúdo para formato CSV com codificação UTF-8
- **Pronto para Tradução**: Ideal para preparar documentos para tradução em múltiplos idiomas
- **Tratamento de Erros**: Sistema robusto de tratamento de erros com log detalhado e recuperação
- **Suporte UTF-8**: Suporte completo para acentos e caracteres especiais (ç, ã, é, etc.)
- **Backup Automático**: Backup automático opcional antes do processamento
- **Configuração Dinâmica**: Edite configurações sem modificar o código do script
- **Suporte a Cancelamento**: Pare o processamento a qualquer momento
- **Otimizado para Performance**: Delays inteligentes e processamento em lotes para computadores mais fracos

## 📋 Requisitos

### Versões do Adobe Illustrator
- ⚠️ **Adobe Illustrator 2023** (pode funcionar, não testado)
- ⚠️ **Adobe Illustrator 2024** (pode funcionar, não testado)
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

### Passo 1: Criar a Ação
Crie uma ação com o nome desejado:

1. Abra o Adobe Illustrator
2. Vá em **Janela > Ações** 
3. Crie um novo conjunto de ações (se necessário)
4. Crie uma nova ação (ex: "setvar")
5. Grave os seguintes passos:
   - Selecione um objeto de texto
   - Vá em **Janela > Variáveis**
   - Clique em "Tornar Texto Dinâmico" ou adicione o texto selecionado como variável
   - Pare a gravação
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
2. **Desagrupe objetos** se necessário - objetos de texto funcionam melhor quando desagrupados para processamento individual
3. Selecione múltiplos objetos de texto que deseja converter em variáveis
3. Vá em **Arquivo > Scripts > CreateTextVariables**
4. Confirme o processamento
5. Escolha se deseja exportar CSV quando solicitado

## 📊 Formato de Saída CSV

O script gera um arquivo CSV com esta estrutura:

> **Dica:** Cada nova tradução deve ser adicionada como uma nova linha abaixo da original, mantendo os cabeçalhos das colunas. Assim, cada versão de idioma fica organizada e fácil de localizar.

```csv
"Variável1","Variável2","Variável3"
"Conteúdo da variável 1","Conteúdo da variável 2","Conteúdo da variável 3"
"Tradução 1","Tradução 2","Tradução 3"
"Traducción 1","Traducción 2","Traducción 3"
```


## 🔄 Fluxo de Trabalho para Tradução

1. **Preparação**: Execute o script nos textos originais
2. **Exportação**: Exporte CSV com textos originais
3. **Tradução**: Envie CSV para tradutores
4. **Organização**: Receba CSVs traduzidos organizados
5. **Traduza o CSV**: Utilize uma IA (ex: ChatGPT) para traduzir e localizar o CSV para o idioma desejado, mantendo a formatação das linhas. Exemplo de prompt:

   > Traduza e localize o conteúdo CSV abaixo para [idioma alvo], mantendo exatamente a formatação das linhas do CSV enviado.

6. **Carregar biblioteca de variáveis**: Carregue o CSV traduzido como biblioteca de variáveis e selecione o conjunto de dados desejado para o documento.
7. **Reimportação**: Use variáveis para atualizar documentos traduzidos

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
Edite as variáveis de configuração no topo de `TraduzAI.jsx`:

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
