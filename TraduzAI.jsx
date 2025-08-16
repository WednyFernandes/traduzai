// IllustraVar - Adobe Illustrator Text Variables Automation
// Created by Wedny Fernandes - https://wednyfernandes.com.br
// Version 1.0.0 - Brazilian Design Automation

// =============================================================================
// CONFIGURAÇÕES - ALTERE CONFORME SUA LINGUAGEM E CONFIGURAÇÃO
// =============================================================================

// Nome da ação que você criou para converter texto em variável
var ACTION_NAME = "setvar";

// Nome do conjunto de ações onde sua ação está localizada
var ACTION_SET = "Ações Padrão"; // Português: "Ações Padrão" | English: "Default Actions" | etc.

// Prefixo para nomes das variáveis no CSV (será numerado automaticamente)
var VARIABLE_PREFIX = "Variável"; // Português: "Variável" | English: "Variable" | etc.

// =============================================================================
// INSTRUÇÕES PARA CONFIGURAÇÃO:
// - ACTION_NAME: Nome exato da ação que você criou
// - ACTION_SET: Nome do conjunto onde está a ação (varia por idioma)
// - VARIABLE_PREFIX: Como nomear as colunas no CSV
//
// Exemplos por idioma:
// Português BR: ACTION_SET = "Ações Padrão"
// English: ACTION_SET = "Default Actions" 
// Español: ACTION_SET = "Acciones por defecto"
// Français: ACTION_SET = "Actions par défaut"
// =============================================================================

// Função para coletar dados do objeto de forma segura
function collectObjectData(obj, index) {
    try {
        var data = {
            index: index,
            objectType: "Unknown",
            originalText: ""
        };
        
        // Coleta tipo do objeto de forma segura
        try {
            data.objectType = obj.typename || "Unknown";
        } catch (typeError) {
            data.objectType = "Error";
        }
        
        // Se for um texto, coleta o conteúdo
        try {
            if (data.objectType === "TextFrame" && obj.contents) {
                data.originalText = String(obj.contents);
            }
        } catch (textError) {
            data.originalText = "";
        }
        
        return data;
    } catch (e) {
        return {
            index: index,
            objectType: "Error",
            originalText: ""
        };
    }
}

// Função para coletar dados após o processamento
function collectPostObjectData(obj, index) {
    try {
        var data = {
            currentText: "",
            hasVariables: false
        };
        
        // Se for um texto, coleta o conteúdo atual
        try {
            if (obj.typename === "TextFrame" && obj.contents) {
                data.currentText = String(obj.contents);
            }
        } catch (textError) {
            data.currentText = "";
        }
        
        // Verifica se há variáveis no documento de forma simples
        try {
            var varCount = app.activeDocument.variables.length;
            data.hasVariables = varCount > 0;
            data.variableCount = varCount;
        } catch (varError) {
            data.hasVariables = false;
            data.variableCount = 0;
        }
        
        return data;
    } catch (e) {
        return {
            currentText: "",
            hasVariables: false
        };
    }
}

// Função para exportar dados para CSV no formato solicitado
function exportVariablesToCSV(data) {
    try {
        // Solicita local para salvar o arquivo
        var saveFile = File.saveDialog("Salvar CSV de Variáveis", "*.csv");
        
        if (saveFile) {
            // Configura codificação UTF-8 com BOM para melhor compatibilidade
            saveFile.encoding = "UTF-8";
            saveFile.lineFeed = "Unix"; // Força quebra de linha Unix
            saveFile.open("w");
            
            // Escreve BOM UTF-8 manualmente para garantir compatibilidade
            saveFile.write("\uFEFF");
            
            // Arrays para armazenar nomes das variáveis e conteúdos
            var variableNames = [];
            var variableContents = [];
            
            // Função para limpar e formatar texto para CSV preservando acentos
            function formatForCSV(text) {
                if (!text) return '""';
                // Converte para string se necessário
                text = String(text);
                // Remove apenas quebras de linha, preserva todos os outros caracteres
                text = text.replace(/[\r\n\t]/g, " ");
                // Remove espaços duplos
                text = text.replace(/\s+/g, " ");
                // Remove espaços no início e fim
                text = text.replace(/^\s+|\s+$/g, "");
                // Escapa aspas duplas duplicando-as (padrão CSV)
                text = text.replace(/"/g, '""');
                return '"' + text + '"'; // Envolve em aspas duplas
            }
            
            // Processa os dados para extrair conteúdos
            for (var i = 0; i < data.length; i++) {
                var item = data[i];
                
                // Nome fixo da variável usando o prefixo configurado
                variableNames.push('"' + VARIABLE_PREFIX + (i + 1) + '"');
                
                // Conteúdo: usa o texto após processamento (ou original se não houver)
                var content = "";
                if (item.postData && item.postData.currentText) {
                    content = item.postData.currentText;
                } else if (item.preData && item.preData.originalText) {
                    content = item.preData.originalText;
                }
                variableContents.push(formatForCSV(content));
            }
            
            // Escreve o cabeçalho (nomes fixos das variáveis)
            saveFile.writeln(variableNames.join(","));
            
            // Escreve a linha de conteúdo
            saveFile.writeln(variableContents.join(","));
            
            saveFile.close();
            
            // Tenta verificar se os acentos foram salvos corretamente
            try {
                var testFile = new File(saveFile.fsName);
                testFile.encoding = "UTF-8";
                testFile.open("r");
                var content = testFile.read();
                testFile.close();
                
                // Se não há acentos no conteúdo, tenta reescrever com codificação alternativa
                if (content.indexOf("ção") === -1 && content.indexOf("ã") === -1 && content.indexOf("é") === -1) {
                    // Reescreve com codificação padrão do sistema
                    saveFile.encoding = "BINARY";
                    saveFile.open("w");
                    saveFile.writeln(variableNames.join(","));
                    saveFile.writeln(variableContents.join(","));
                    saveFile.close();
                }
            } catch (testError) {
                // Ignora erro de teste, arquivo já foi salvo
            }
            
            alert("Arquivo CSV exportado com sucesso!\nLocal: " + saveFile.fsName + "\n\nSe os acentos não aparecerem corretamente, abra o arquivo no Excel e escolha 'UTF-8' na importação.");
        }
    } catch (e) {
        alert("Erro ao exportar CSV: " + e);
    }
}

// CÓDIGO PRINCIPAL - SEM INTERFACE
if (app.documents.length > 0) {
    var sel = app.selection;
    
    if (sel.length > 0) {
        // Array para armazenar dados das variáveis para CSV
        var variablesData = [];
        
        // Limpa a seleção inicial
        app.activeDocument.selection = null;
        
        // Processa cada objeto individualmente
        for (var i = 0; i < sel.length; i++) {
            try {
                // Seleciona apenas o objeto atual
                sel[i].selected = true;
                
                // Coleta dados básicos
                var objectData = collectObjectData(sel[i], i+1);
                
                // Executa o macro configurado
                app.doScript(ACTION_NAME, ACTION_SET);
                
                // Delay de 0.2 segundos para estabilizar
                $.sleep(200);
                
                // Coleta dados após processamento
                var postObjectData = collectPostObjectData(sel[i], i+1);
                
                // Adiciona os dados ao array
                variablesData.push({
                    index: i+1,
                    preData: objectData,
                    postData: postObjectData
                });
                
                // Limpa a seleção
                app.activeDocument.selection = null;
                
            } catch (e) {
                // Em caso de erro, limpa seleção e continua
                try {
                    app.activeDocument.selection = null;
                } catch (clearError) {
                    // Ignora erro de limpeza
                }
                
                // Adiciona dados de erro
                variablesData.push({
                    index: i+1,
                    preData: { index: i+1, objectType: "Error", originalText: "Erro: " + e },
                    postData: { currentText: "", hasVariables: false }
                });
            }
        }
        
        // Pergunta se deseja exportar CSV
        var exportCSV = confirm("Processamento concluído! Ação '" + ACTION_NAME + "' executada para " + sel.length + " objetos.\n\nDeseja exportar um arquivo CSV com os dados das variáveis?");
        
        if (exportCSV && variablesData.length > 0) {
            exportVariablesToCSV(variablesData);
        } else if (!exportCSV) {
            alert("Processamento concluído sem exportação de CSV.");
        } else {
            alert("Nenhum dado de variável foi coletado para exportação.");
        }
        
    } else {
        alert("Por favor, selecione alguns objetos primeiro.");
    }
} else {
    alert("Nenhum documento aberto.");
}
