// TraduzAI - Adobe Illustrator Text Variables Automation
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

// ===============================
// INTERFACE SCRIPTUI
// ===============================
var win = new Window('dialog', 'TraduzAI - Wedny Fernandes');
win.orientation = 'column';
win.alignChildren = ['center', 'top'];
win.spacing = 15;

// Barra de progresso
var progressBar = win.add('progressbar', undefined, 0, 100);
progressBar.preferredSize.width = 350;
var progressText = win.add('statictext', undefined, 'Aguardando início...');
progressText.alignment = 'center';

// Botão Start (maior e azul)
var startBtn = win.add('button', undefined, 'START');
startBtn.preferredSize.width = 200;
startBtn.preferredSize.height = 40;
startBtn.fillBrush = startBtn.graphics.newBrush(startBtn.graphics.BrushType.SOLID_COLOR, [0.2, 0.4, 0.8, 1]);

// Botão cancelar
var cancelBtn = win.add('button', undefined, 'Cancelar');
cancelBtn.preferredSize.width = 120;
cancelBtn.enabled = false;

// Toggle para backup
var backupGroup = win.add('group');
backupGroup.orientation = 'row';
backupGroup.alignment = 'center';
var backupCheckbox = backupGroup.add('checkbox', undefined, 'Criar backup automático');
backupCheckbox.value = true;

// Separador
var separator = win.add('panel');
separator.preferredSize.height = 2;

// Campos editáveis (seção configurações)
var configTitle = win.add('statictext', undefined, 'Configurações Avançadas');
configTitle.alignment = 'center';

var actionNameGroup = win.add('group');
actionNameGroup.add('statictext', undefined, 'Action Name:');
var actionNameField = actionNameGroup.add('edittext', undefined, ACTION_NAME);
actionNameField.characters = 20;

var actionSetGroup = win.add('group');
actionSetGroup.add('statictext', undefined, 'Action Set:');
var actionSetField = actionSetGroup.add('edittext', undefined, ACTION_SET);
actionSetField.characters = 20;

var variablePrefixGroup = win.add('group');
variablePrefixGroup.add('statictext', undefined, 'Variable Prefix:');
var variablePrefixField = variablePrefixGroup.add('edittext', undefined, VARIABLE_PREFIX);
variablePrefixField.characters = 20;

// Separador
var separator2 = win.add('panel');
separator2.preferredSize.height = 2;

// Créditos (no final)
var credits = win.add('statictext', undefined, 'Desenvolvido por Wedny Fernandes - wednyfernandes.com.br');
credits.alignment = 'center';
credits.graphics.font = ScriptUI.newFont('dialog', 'ITALIC', 10);

// Variável de controle de cancelamento
var cancelRequested = false;

// Função para atualizar progresso
function updateProgress(current, total) {
    progressBar.value = Math.round((current / total) * 100);
    progressText.text = 'Processando ' + current + ' de ' + total + '...';
}

// Função principal de processamento (em lotes) - OTIMIZADA PARA PCs FRACOS
function processSelectionAsync(sel, batchSize) {
    var total = sel.length;
    var i = 0;
    var variablesData = [];
    cancelRequested = false;
    
    // OTIMIZAÇÕES MÁXIMAS DE PERFORMANCE PARA PC DE 8GB
    try {
        // Desabilita completamente o redraw e preview
        app.redraw();
        app.coordinateSystem = CoordinateSystem.ARTBOARDCOORDINATESYSTEM;
        
        // Força garbage collection antes de começar
        $.gc();
        
        // Desabilita preview em tempo real se possível
        try {
            app.preferences.setBooleanPreference("ShowRealTimeDrawing", false);
        } catch (prefError) {}
        
    } catch (perfError) {
        // Ignora erros de otimização
    }
    
    function processBatch() {
        if (cancelRequested) {
            progressText.text = 'Processamento cancelado.';
            startBtn.enabled = true;
            cancelBtn.enabled = false;
            // Reabilita redraw e restaura configurações
            try {
                app.redraw();
                app.preferences.setBooleanPreference("ShowRealTimeDrawing", true);
            } catch (restoreError) {}
            return;
        }
        
        // Lotes menores para PCs fracos (3 objetos por vez)
        var actualBatchSize = Math.min(batchSize, 3);
        var batchEnd = Math.min(i + actualBatchSize, total);
        
        for (; i < batchEnd; i++) {
            try {
                // Força garbage collection a cada 5 objetos para liberar memória
                if (i % 5 === 0) {
                    $.gc();
                }
                
                // Limpa toda a seleção primeiro
                app.activeDocument.selection = null;
                // Seleciona apenas o objeto atual
                sel[i].selected = true;
                
                // Coleta dados ANTES (simplificado para economizar memória)
                var objectData = {
                    index: i+1,
                    originalText: ""
                };
                
                try {
                    if (sel[i].typename === "TextFrame" && sel[i].contents) {
                        objectData.originalText = String(sel[i].contents);
                    }
                } catch (textError) {
                    objectData.originalText = "";
                }
                
                // Aplica a ação IMEDIATAMENTE
                app.doScript(actionNameField.text, actionSetField.text);
                $.sleep(50); // Delay mínimo para aplicação da ação
                
                // Coleta dados APÓS (simplificado)
                var postObjectData = {
                    currentText: ""
                };
                
                try {
                    if (sel[i].typename === "TextFrame" && sel[i].contents) {
                        postObjectData.currentText = String(sel[i].contents);
                    }
                } catch (textError) {
                    postObjectData.currentText = "";
                }
                
                // Armazena os dados (estrutura simplificada)
                variablesData.push({
                    index: i+1,
                    preData: objectData,
                    postData: postObjectData
                });
                
                // Limpa a seleção novamente
                app.activeDocument.selection = null;
                
            } catch (e) {
                try { app.activeDocument.selection = null; } catch (clearError) {}
                // Estrutura de erro simplificada
                variablesData.push({
                    index: i+1,
                    preData: { index: i+1, originalText: "Erro: " + e },
                    postData: { currentText: "" }
                });
            }
            updateProgress(i + 1, total);
        }
        
        if (i < total) {
            // Delay mínimo entre lotes para PCs fracos
            $.sleep(200);
            // Força garbage collection entre lotes
            $.gc();
            processBatch();
        } else {
            progressText.text = 'Processamento concluído!';
            startBtn.enabled = true;
            cancelBtn.enabled = false;
            
            // Reabilita redraw e configurações no final
            try {
                app.redraw();
                app.preferences.setBooleanPreference("ShowRealTimeDrawing", true);
                $.gc(); // Limpeza final de memória
            } catch (restoreError) {}
            
            // Pergunta se deseja exportar CSV
            var exportCSV = confirm("Processamento concluído! Ação '" + actionNameField.text + "' executada para " + total + " objetos.\n\nDeseja exportar um arquivo CSV com os dados das variáveis?");
            if (exportCSV && variablesData.length > 0) {
                exportVariablesToCSV(variablesData, variablePrefixField.text);
            } else if (!exportCSV) {
                alert("Processamento concluído sem exportação de CSV.");
            } else {
                alert("Nenhum dado de variável foi coletado para exportação.");
            }
        }
    }
    processBatch();
}

// Botão cancelar
cancelBtn.onClick = function() {
    cancelRequested = true;
    cancelBtn.enabled = false;
    startBtn.enabled = true;
    progressText.text = 'Cancelamento solicitado...';
};

// Botão start
startBtn.onClick = function() {
    if (app.documents.length === 0) {
        alert('Nenhum documento aberto.');
        return;
    }
    var sel = app.selection;
    if (!sel || sel.length === 0) {
        alert('Por favor, selecione alguns objetos primeiro.');
        return;
    }
    // Backup automático (apenas se ativado)
    if (backupCheckbox.value) {
        try {
            var doc = app.activeDocument;
            var originalPath = doc.fullName;
            var backupPath = originalPath.parent + "/" + originalPath.name.replace(/\.ai$/i, "-backup.ai");
            doc.saveAs(new File(backupPath));
            alert("Backup salvo em: " + backupPath);
        } catch (backupError) {
            alert("Não foi possível salvar o backup automático: " + backupError);
        }
    }
    startBtn.enabled = false;
    cancelBtn.enabled = true;
    cancelRequested = false;
    updateProgress(0, sel.length);
    
    // Força garbage collection antes de começar
    $.gc();
    
    // Lotes menores para PCs fracos (5 ao invés de 10)
    processSelectionAsync(sel, 5);
};

// Mostrar interface
win.show();

// ===============================

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
function exportVariablesToCSV(data, variablePrefix) {
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
                variableNames.push('"' + variablePrefix + (i + 1) + '"');
                
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
