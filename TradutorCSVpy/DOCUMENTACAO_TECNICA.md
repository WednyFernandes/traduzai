# Tradutor CSV - Documentação Técnica

## 📁 Estrutura dos Arquivos

```
TradutorCSVpy/
├── tradutor_csv.py              # Script principal
├── requirements.txt             # Dependências Python
├── README.md                   # Documentação do usuário
├── config_exemplo.json         # Configuração de exemplo
├── translation_config.json     # Configuração padrão (criada automaticamente)
├── instalar.bat                # Script de instalação (Windows)
├── exemplo_uso.bat             # Exemplo de uso básico
├── demonstracao.bat            # Demonstração completa
├── teste_pequeno.csv           # Arquivo de teste
└── traducoescardapiocasadoouvidor.csv  # Arquivo original
```

## 🔧 Funcionalidades Técnicas

### 1. Preservação de Elementos
O script preserva automaticamente:
- **URLs**: `http://`, `https://`, `www.`
- **Emails**: padrão `usuario@dominio.com`
- **Números**: valores numéricos (opcional)
- **Formatação**: aspas, pontuação, quebras de linha

### 2. Tratamento de Moedas
```python
# Padrões suportados:
- 82,00
- 82.00  
- R$ 82,00
- 1.234,56
- 1,234.56
```

### 3. Opções de Conversão
- **Apenas símbolo**: `R$ 82,00` → `$ 82,00`
- **Com conversão**: `R$ 82,00` → `$ 14.76` (taxa 0.18)
- **Preservar**: mantém valores originais

### 4. Cache de Tradução
- Evita traduzir o mesmo texto múltiplas vezes
- Melhora performance em arquivos grandes
- Baseado em chave: `texto_idioma_origem_idioma_destino`

## 🎯 Casos de Uso

### Restaurantes e Bares
```bash
# Traduzir cardápio mantendo preços em reais
python tradutor_csv.py cardapio.csv -t en --currency-symbol "R$"

# Traduzir e converter preços para dólares
python tradutor_csv.py cardapio.csv -t en --convert-currency --rate 0.18 --currency-symbol "$"
```

### E-commerce
```bash
# Traduzir catálogo preservando códigos de produto
python tradutor_csv.py produtos.csv -t es --preserve-numbers
```

### Documentação Técnica
```bash
# Traduzir preservando URLs e emails
python tradutor_csv.py docs.csv -t fr --preserve-urls --preserve-emails
```

## ⚙️ Configuração Avançada

### Arquivo config.json
```json
{
  "source_language": "pt",           // Idioma origem
  "target_language": "en",           // Idioma destino
  "currency_symbol": "$",            // Símbolo da moeda
  "convert_currency": false,         // Converter valores
  "currency_conversion_rate": 5.5,   // Taxa de conversão
  "preserve_numbers": true,          // Preservar números
  "preserve_urls": true,             // Preservar URLs
  "preserve_emails": true,           // Preservar emails
  "max_retries": 3                   // Tentativas de tradução
}
```

### Idiomas Suportados
| Código | Idioma | Código | Idioma |
|--------|--------|--------|--------|
| `pt` | Português | `en` | Inglês |
| `es` | Espanhol | `fr` | Francês |
| `de` | Alemão | `it` | Italiano |
| `ja` | Japonês | `zh` | Chinês |
| `ko` | Coreano | `ru` | Russo |
| `ar` | Árabe | `hi` | Hindi |

## 🚨 Limitações e Considerações

### Limitações da API
- Google Translate tem limites de uso
- Conexão com internet obrigatória
- Alguns termos específicos podem não traduzir bem

### Performance
- Arquivos muito grandes podem demorar
- Use cache para otimizar traduções repetidas
- Considere dividir arquivos grandes

### Qualidade da Tradução
- Traduções automáticas podem precisar revisão
- Termos técnicos específicos podem ser imprecisos
- Contexto pode ser perdido em frases curtas

## 🔍 Solução de Problemas

### Erro de Conexão
```
ConnectionError: Failed to establish a new connection
```
**Solução**: Verificar conexão com internet e firewall

### Erro de Quota
```
Quota exceeded
```
**Solução**: Aguardar ou usar conta Google Translate paga

### Erro de Encoding
```
UnicodeDecodeError
```
**Solução**: Salvar CSV em UTF-8

### Tradução Incompleta
**Sintomas**: Algumas células não traduzidas
**Solução**: Verificar se há caracteres especiais ou aumentar `max_retries`

## 🧪 Testes

### Teste Básico
```bash
python tradutor_csv.py teste_pequeno.csv -t en
```

### Teste com Moeda
```bash
python tradutor_csv.py teste_pequeno.csv -t en --convert-currency --rate 0.18
```

### Teste de Performance
```bash
# Cronometrar tradução
time python tradutor_csv.py arquivo_grande.csv -t en
```

## 📊 Monitoramento

### Logs de Progresso
O script exibe:
- Número de linhas processadas
- Células traduzidas
- Erros encontrados
- Tempo estimado (para arquivos grandes)

### Métricas de Qualidade
- Taxa de sucesso na tradução
- Elementos preservados corretamente
- Conversões de moeda aplicadas

## 🔄 Workflow Recomendado

1. **Preparação**
   - Backup do arquivo original
   - Verificar encoding (UTF-8)
   - Testar com amostra pequena

2. **Configuração**
   - Definir idiomas de origem e destino
   - Configurar tratamento de moedas
   - Ajustar preservação de elementos

3. **Execução**
   - Executar tradução
   - Monitorar progresso
   - Verificar logs de erro

4. **Validação**
   - Revisar resultado
   - Verificar formatação
   - Validar traduções críticas

5. **Pós-processamento**
   - Ajustes manuais se necessário
   - Validação final
   - Deploy/entrega

## 🚀 Otimizações Futuras

### Possíveis Melhorias
- Suporte a outras APIs de tradução
- Interface gráfica (GUI)
- Tradução em lotes
- Validação de qualidade automática
- Suporte a formatos adicionais (Excel, JSON)

### Integrações
- Sistemas de gerenciamento de conteúdo
- APIs de e-commerce
- Workflows de CI/CD
- Sistemas de controle de versão

---

**Desenvolvido para facilitar traduções profissionais mantendo qualidade e formatação.**
