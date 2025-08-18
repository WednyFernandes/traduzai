# TraduzAI - Automação de Tradução para Adobe Illustrator

**TraduzAI: Interface Moderna para Criação Automatizada de Variáveis de Texto e Exportação CSV - Perfeito para Fluxos de Trabalho de Tradução de Documentos**

*Criado por [Wedny Fernandes](https://wednyfernandes.com.br) - Designer Gráfico e Desenvolvedor Brasileiro*

Este script fornece uma interface gráfica moderna para automatizar o processo de criação de variáveis de texto no Adobe Illustrator. Com acompanhamento de progresso em tempo real, processamento em lote e configurações personalizáveis, é a ferramenta perfeita para fluxos de trabalho de tradução e localização.

> **Testado apenas no Adobe Illustrator 2025.**

## 🎨 Recursos da Interface Moderna

- **🖥️ Interface Intuitiva**: Interface ScriptUI profissional com feedback em tempo real
- **📊 Acompanhamento de Progresso**: Barra de progresso ao vivo mostrando o status do processamento
- **⏸️ Controle de Cancelamento**: Pare o processamento a qualquer momento com o botão cancelar
- **💾 Backup Automático**: Criação opcional de backup antes do processamento
- **⚙️ Configuração Dinâmica**: Edite nomes de ações e configurações diretamente na interface
- **🎯 Processamento em Lote**: Processa objetos em lotes otimizados de 10
- **🔄 Delays Inteligentes**: Temporização otimizada entre lotes para melhor desempenho

## 🌍 Perfeito para Tradução e Localização

- **Preparação de Documentos**: Converta textos estáticos em variáveis para tradução fácil
- **Localização de Materiais**: Prepare materiais de marketing para múltiplos mercados
- **Fluxo de Trabalho de Tradução**: Exporte textos para formato CSV para tradutores
- **Processo de Reimportação**: Reimporte facilmente textos traduzidos de volta para o Illustrator
- **Controle de Versão**: Mantenha controle sobre diferentes versões de idiomas
- **Projetos Multilíngues**: Simplifique a criação de materiais de design multilíngues

## 🎯 Recursos Principais

- **Interface Moderna**: ScriptUI limpa e profissional com acompanhamento de progresso
- **Processamento em Lote**: Processa objetos de texto em lotes otimizados para melhor desempenho
- **Exportação CSV**: Exporte nomes de variáveis e conteúdo para formato CSV com codificação UTF-8 adequada
- **Pronto para Tradução**: Ideal para preparar documentos para tradução em múltiplos idiomas
- **Tratamento de Erros**: Tratamento robusto de erros com logging detalhado e recuperação
- **Suporte UTF-8**: Suporte completo para acentos e caracteres especiais (ç, ã, é, ñ, ü, etc.)
- **Backup Automático**: Backup automático opcional antes do processamento
- **Configuração Dinâmica**: Edite configurações sem modificar o código do script
- **Suporte ao Cancelamento**: Pare o processamento a qualquer momento
- **Otimizado para Performance**: Delays inteligentes e processamento em lote para computadores menos potentes

## 📋 Requisitos

### Versões do Adobe Illustrator
- ✅ **Adobe Illustrator 2025** (testado)
- ⚠️ **Adobe Illustrator 2024** (pode funcionar, não testado)
- ⚠️ **Adobe Illustrator 2023** (pode funcionar, não testado)
- ⚠️ **Adobe Illustrator 2022** (pode funcionar, não testado)
- ❌ **Adobe Illustrator 2021 ou anterior** (não suportado)

### Suporte a Idiomas
- ✅ **Português (Brasil)** - pt_BR (principal)
- ✅ **Inglês** (compatível)
- ✅ **Espanhol** (compatível)
- ✅ **Francês** (compatível)
- ✅ **Alemão** (compatível)
- ⚠️ **Outros idiomas** (podem requerer ajuste no nome da ação)

## 🔄 Fluxo de Trabalho de Tradução

1. **Preparação**: Execute o script nos textos do idioma original
2. **Exportação**: Exporte CSV com textos originais
3. **Tradução**: Envie CSV para tradutores
4. **Organização**: Receba CSVs traduzidos organizados
5. **Reimportação**: Use variáveis para atualizar documentos traduzidos

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

### Passo 2: Instalar o Script
1. Baixe `TraduzAI.jsx`
2. Copie para a pasta de Scripts do Illustrator:
   - **Windows**: `C:\Program Files\Adobe\Adobe Illustrator [Versão]\Presets\[Idioma]\Scripts\`
   - **macOS**: `/Applications/Adobe Illustrator [Versão]/Presets/[Idioma]/Scripts/`

### Passo 3: Uso com Interface Moderna
1. Abra seu documento do Illustrator
2. **Desagrupe objetos** se necessário - objetos de texto funcionam melhor quando desagrupados para processamento individual
3. Selecione múltiplos objetos de texto que você quer converter em variáveis
4. Vá em **Arquivo > Scripts > TraduzAI**
5. **Configure as opções** na interface:
   - **Nome da Ação**: Digite o nome da sua ação (ex: "setvar")
   - **Conjunto de Ações**: Digite o nome do seu conjunto de ações (varia por idioma)
   - **Prefixo da Variável**: Escolha o prefixo da coluna CSV (ex: "Variável")
   - **Alternador de Backup**: Ative/desative backup automático
6. Clique em **INICIAR** para começar o processamento
7. Monitore o progresso em tempo real
8. Use o botão **Cancelar** se necessário para parar o processamento
9. Escolha a exportação CSV quando o processamento for concluído

### Passo 4: Fluxo de Trabalho de Tradução

#### Método 1: Usando Google Sheets (Recomendado)
1. **Exportar CSV**: Exporte suas variáveis processadas para formato CSV
2. **Abrir no Google Sheets**: Importe o arquivo CSV no Google Sheets
3. **Adicionar linhas de tradução**: Crie novas linhas abaixo do conteúdo original para cada idioma de destino
4. **Usar Google Translate**: Utilize a função integrada do Google Translate do Google Sheets para cada coluna de idioma de destino
5. **Tratar quebras de linha**: Após a tradução, substitua todos os caracteres `\n` por `^n` no conteúdo traduzido (isso é necessário para compatibilidade com o Illustrator)
   - Você pode fazer isso no Google Sheets usando Localizar e Substituir: Localizar `\n` e substituir por `^n`
   - Alternativamente, use o recurso Localizar e Substituir do Illustrator após importar
6. **Exportar CSV traduzido**: Baixe o CSV completo com todas as versões de idiomas

#### Método 2: Usando Tradução por IA
1. **Exportar CSV**: Exporte suas variáveis processadas para formato CSV
2. **Traduzir com IA**: Use um serviço de IA (ex: ChatGPT) para traduzir e localizar o CSV para seu idioma de destino, mantendo a formatação de linha CSV. Exemplo de prompt:

   > Traduza e localize o seguinte conteúdo CSV para [idioma de destino], mantendo a formatação de linha CSV exatamente como fornecida. Substitua qualquer quebra de linha \n por ^n para compatibilidade com o Illustrator.

#### Passos Finais
3. **Carregar biblioteca de variáveis**: Carregue o CSV traduzido como sua biblioteca de variáveis e selecione o conjunto de dados desejado para seu documento
4. **Aplicar traduções**: Use o painel de variáveis do Illustrator para aplicar as traduções

## 📊 Formato de Saída CSV

O script gera um arquivo CSV com esta estrutura:

> **Dica:** Cada nova tradução deve ser adicionada como uma nova linha abaixo da original, mantendo os cabeçalhos das colunas. Dessa forma, cada versão de idioma fica organizada e fácil de localizar.

```csv
"Variável1","Variável2","Variável3"
"Conteúdo da variável 1","Conteúdo da variável 2","Conteúdo da variável 3"
"Translation 1","Translation 2","Translation 3"
"Traducción 1","Traducción 2","Traducción 3"
```

## ⚠️ Problemas Conhecidos e Solução de Problemas

### Problemas Comuns

1. **Erro "Ação não encontrada"**
   - ❌ **Causa**: Nome da ação não coincide com a variável `ACTION_NAME`
   - ✅ **Solução**: Verifique se o nome da sua ação coincide exatamente com o que está no script

2. **Erro "Conjunto de ações não encontrado"**
   - ❌ **Causa**: Nome do conjunto de ações não coincide com a variável `ACTION_SET`
   - ✅ **Solução**: Atualize `ACTION_SET` para coincidir com o idioma do seu Illustrator

3. **Nomes de colunas CSV no idioma errado**
   - ❌ **Causa**: `VARIABLE_PREFIX` não configurado para seu idioma
   - ✅ **Solução**: Altere `VARIABLE_PREFIX` para seu idioma preferido

4. **Acentos não sendo exibidos corretamente**
   - ❌ **Causa**: CSV aberto sem codificação UTF-8
   - ✅ **Solução**: Importe CSV no Excel escolhendo codificação UTF-8

5. **Quebras de linha não funcionando no Illustrator**
   - ❌ **Causa**: Quebras de linha padrão `\n` não funcionam em variáveis do Illustrator
   - ✅ **Solução**: Substitua `\n` por `^n` no seu conteúdo traduzido. Use Localizar e Substituir no Google Sheets ou Illustrator

6. **Script trava em seleções grandes**
   - ❌ **Causa**: Muitos objetos selecionados
   - ✅ **Solução**: Processe em lotes menores (máximo 50-100 objetos)

### Problemas de Compatibilidade

- **Illustrator 2021 ou anterior**: Pode não suportar algumas funções do script
- **Alfabetos não latinos**: Podem requerer ajustes adicionais de codificação
- **Arquivos muito grandes**: Performance pode degradar com mais de 500 objetos

## 🔧 Configuração

### Configuração de Idioma
Edite as variáveis de configuração no topo do `TraduzAI.jsx`:

```javascript
// Nome da sua ação (deve coincidir exatamente)
var ACTION_NAME = "setvar";

// Nome do seu conjunto de ações (varia por idioma)
var ACTION_SET = "Ações Padrão";  // Português BR
// var ACTION_SET = "Default Actions";  // Inglês
// var ACTION_SET = "Acciones por defecto";  // Espanhol

// Prefixo da coluna CSV (seu idioma)
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

## 🐍 Componente Python - Tradutor CSV

O projeto inclui um script Python adicional para tradução automatizada de arquivos CSV:

### Recursos do Tradutor CSV
- ✅ **Tradução automática** usando Google Translate
- ✅ **Preserva estrutura original** (cabeçalho + dados originais + traduções)
- ✅ **Preserva formatação** (aspas, pontuação, quebras de linha)
- ✅ **Preserva caixa alta** (texto em MAIÚSCULAS mantém formatação)
- ✅ **Opções de moeda** (conversão ou apenas troca de símbolo)
- ✅ **Cache de tradução** para eficiência
- ✅ **Configuração flexível** via JSON

### Instalação do Componente Python
```bash
# Windows - Execute o instalador automático
cd TradutorCSVpy
instalar.bat

# Ou instalação manual
pip install googletrans==4.0.0rc1
```

### Uso do Tradutor CSV
```bash
# Traduzir arquivo CSV
python tradutor_csv.py arquivo.csv en

# Com configurações personalizadas
python tradutor_csv.py arquivo.csv en --config config.json
```

## 🤝 Contribuindo

Sinta-se à vontade para enviar problemas e solicitações de melhorias!

## 💝 Apoie Este Projeto

Se este script te ajudou a economizar tempo em seus projetos de tradução e localização, considere fazer uma doação para apoiar o desenvolvimento contínuo:

[![Doar via PayPal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=K39ZWTCBRF6TW)

Sua contribuição ajuda a manter este projeto gratuito e acessível para toda a comunidade de design!

## 🌐 Versões de Idioma

- 🇺🇸 [English](README.md)
- 🇧🇷 [Português Brasil (este arquivo)](README-ptBR.md)

## 📄 Licença

Este script é fornecido como está para uso educacional e comercial.

---

**Palavras-chave**: Adobe Illustrator, Variáveis de Texto, Automação, Tradução, Localização, Tradução de Documentos, Processamento em Lote, Exportação CSV, JavaScript, Script JSX, Design Multilíngue, Fluxo de Trabalho de Tradução, Automação de Design, Scripts do Illustrator, Dados Variáveis, Texto Dinâmico, Internacionalização, i18n, Localização de Documentos
